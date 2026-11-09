from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
state = json.loads((ROOT / "data" / "disclosure_watch.json").read_text(encoding="utf-8"))
required = {"company", "stock_code", "filings"}
missing = required - state.keys()
assert not missing, f"누락된 상태 필드: {sorted(missing)}"
assert isinstance(state["filings"], list), "filings는 배열이어야 합니다"
for item in state["filings"]:
    assert {"receipt_number", "receipt_date", "report_name", "filer", "url"} <= item.keys(), "공시 필드가 부족합니다"
    assert item["url"].startswith("https://dart.fss.or.kr/"), "DART 원문 URL이 아닙니다"
print("disclosure watch: PASS")
