"""Detect new earnings-related DART filings and update the repository log."""
from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from datetime import datetime, timedelta, timezone
from io import BytesIO
from pathlib import Path

COMPANY = "티씨케이"
STOCK_CODE = "064760"
KEYWORDS = ("사업보고서", "반기보고서", "분기보고서", "영업(잠정)실적")
ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "data" / "disclosure_watch.json"
LOG_PATH = ROOT / "report" / "DISCLOSURE_UPDATE_LOG.md"


def get_json(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=30) as response:
        return json.load(response)


def get_corp_code(api_key: str) -> str:
    url = "https://opendart.fss.or.kr/api/corpCode.xml?" + urllib.parse.urlencode({"crtfc_key": api_key})
    with urllib.request.urlopen(url, timeout=60) as response:
        payload = response.read()
    with zipfile.ZipFile(BytesIO(payload)) as archive:
        root = ET.fromstring(archive.read("CORPCODE.xml"))
    for company in root.findall("list"):
        if (company.findtext("stock_code") or "").strip() == STOCK_CODE:
            return (company.findtext("corp_code") or "").strip()
    raise RuntimeError(f"DART 고유번호를 찾지 못했습니다: {STOCK_CODE}")


def is_earnings_filing(report_name: str) -> bool:
    return any(keyword in report_name for keyword in KEYWORDS)


def collect_filings(api_key: str, corp_code: str) -> list[dict]:
    today = datetime.now(timezone.utc).date()
    params = {
        "crtfc_key": api_key,
        "corp_code": corp_code,
        "bgn_de": (today - timedelta(days=21)).strftime("%Y%m%d"),
        "end_de": today.strftime("%Y%m%d"),
        "last_reprt_at": "Y",
        "page_count": "100",
        "sort": "date",
        "sort_mth": "desc",
    }
    payload = get_json("https://opendart.fss.or.kr/api/list.json?" + urllib.parse.urlencode(params))
    status = payload.get("status")
    if status == "013":
        return []
    if status != "000":
        raise RuntimeError(f"DART 공시 검색 실패: {status} {payload.get('message', '')}")
    filings = []
    for row in payload.get("list", []):
        name = row.get("report_nm", "")
        if not is_earnings_filing(name):
            continue
        rcept_no = row.get("rcept_no", "")
        if not rcept_no:
            continue
        filings.append(
            {
                "receipt_number": rcept_no,
                "receipt_date": row.get("rcept_dt", ""),
                "report_name": name,
                "filer": row.get("flr_nm", ""),
                "url": f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={rcept_no}",
            }
        )
    return filings


def write_log(state: dict) -> None:
    rows = state["filings"][:20]
    lines = [
        "# [공시 갱신 기록]",
        "",
        f"대상 회사: {state['company']} ({state['stock_code']})",
        "",
        "이 파일은 DART에서 새로 감지된 정기보고서와 영업잠정실적 공시를 기록한다. 숫자 실제치, 전망, DCF·RIM·PER, 투자의견과 목표주가는 이 로그만으로 변경하지 않는다.",
        "",
        "| 접수일 | 공시명 | 제출인 | 원문 |",
        "| --- | --- | --- | --- |",
    ]
    if rows:
        for item in rows:
            lines.append(f"| {item['receipt_date']} | {item['report_name']} | {item['filer']} | [DART 원문]({item['url']}) |")
    else:
        lines.append("| - | 아직 자동 기록된 공시가 없습니다. | - | - |")
    lines.extend(["", "공시 원문과 회사 IR 자료를 대조한 뒤 실제치와 평가 가정을 수정한다.", ""])
    LOG_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    api_key = os.environ.get("DART_API_KEY")
    if not api_key:
        raise RuntimeError("GitHub Actions secret DART_API_KEY가 설정되지 않았습니다.")
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    corp_code = get_corp_code(api_key)
    known = {item["receipt_number"] for item in state.get("filings", [])}
    found = collect_filings(api_key, corp_code)
    new_items = [item for item in found if item["receipt_number"] not in known]
    if not new_items:
        print("새 실적 관련 공시가 없습니다.")
        return 0
    state["corp_code"] = corp_code
    state["filings"] = sorted(new_items + state.get("filings", []), key=lambda x: (x["receipt_date"], x["receipt_number"]), reverse=True)
    state["filings"] = state["filings"][:100]
    state["last_update_utc"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_log(state)
    print(f"새 공시 {len(new_items)}건을 기록했습니다.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(1)
