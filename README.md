# 티씨케이 (064760) | Equity Research

**분석 빈티지: 2026-10-17 · 실적 기준: 2026년 2분기/반기 · 통화: KRW · 단위: 십억원**

티씨케이는 반도체 공정에 쓰이는 CVD SiC 부품, 흑연 부품 및 susceptor를 공급합니다. 핵심 평가 변수는 반도체 장비 매출의 단순 성장률이 아니라, Solid SiC의 출하·교체 주기, 고객의 가동률과 공정 전환, 제품 믹스, 고정비 흡수 및 중간 사이클 마진입니다.

## 핵심 관점

- 2025년 매출 301.334십억원, 영업이익 83.887십억원(별도 기준 공시 기반 수치)으로 영업이익률은 약 27.8%입니다.
- 2026년 상반기 매출 +26.0%, 영업이익 +28.9%, 순이익 +37.3% YoY(별도 기준)로 회복 신호가 확인됩니다. 다만 빠른 상반기 성장을 장기 성장률로 복제하지 않고, 2022년 약 40%의 고점 OPM 이후 2025년 27.8%로 내려온 이력을 통해 마진 정상화 폭을 제한합니다.
- 2026년 반기 누적 매출에서 Solid SiC 비중이 약 90%라는 공시 기반 요약은 제품 집중도를 드러냅니다. replacement 수요의 탄력성은 장점이지만 최종 메모리/파운드리 가동률과 고객·공정 집중 위험도 함께 큽니다.
- 넓은 반도체 장비/소재 peer 평균 PER은 직접 적용하지 않습니다. 제품, 가치사슬 위치, 소모성, 고객 인증, 매출총이익/ROIC를 갖춘 유사 상장사가 부족하면 배수는 참고 범위로만 남깁니다.

## 결과 상태

이 저장소는 재현 가능한 초기 분석 프레임워크입니다. 현재 생성값은 탐색용 EV proxy로, 투자판단용 적정가치가 아닙니다. 순현금, 희석주식수, 공정별 CAPEX·감가상각 및 고객 집중 상세를 원문 사업보고서에서 재대조하기 전 주당 적정가를 제시하지 않습니다. `model/run_valuation.py`는 성장-재투자 항등식(FCFF = NOPAT × (1−g/ROIC))에 따른 EV proxy를 산출합니다. ROIC 가정과 D&A·CAPEX·운전자본은 공시 기반 정식 모델로 대체하기 전까지 불확실하므로 가격목표로 해석하면 안 됩니다.

## 경로 안내

| 경로 | 내용 |
|---|---|
| `research/THESIS_AND_DRIVERS.md` | SiC consumable economics, 공정/사이클 및 가치 동인 |
| `research/PEER_SELECTION.md` | peer fit 기준, 보조 비교군, 배제 사유 |
| `research/VALUATION_POLICY.md` | 중간 사이클 DCF·RIM·PER 및 premium gates |
| `data/actuals.csv` | 기준 실적 및 출처 구분 |
| `sources/source_register.csv` | DART/회사 IR/보조 데이터 출처 |
| `model/assumptions.csv` | base/bear/bull 가정과 적용 근거 |
| `model/run_valuation.py` | 5년 중간 사이클 EV proxy 계산 |
| `report/INVESTMENT_MEMO.md` | 요약 투자 가설과 반증조건 |

## 실행

```bash
python model/run_valuation.py
```

## 업데이트 기준

다음 실적 공시 시 Actuals를 별도 기준으로 업데이트하고, Solid SiC/Graphite/Susceptor 매출, 상위 고객·전방산업, 교체수요와 증설 CAPEX를 각각 재확인합니다. 상반기 누적 성장률과 전년 동기 계절성을 분리해 연간 전망을 다시 구성합니다.

본 자료는 교육·연구 목적이며 투자 권유가 아닙니다.
