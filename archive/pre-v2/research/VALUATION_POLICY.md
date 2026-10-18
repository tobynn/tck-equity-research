# Valuation policy & vintage

## 분석 빈티지

- valuation memo date: 2026-10-17
- actuals cutoff: 2026-06-30 (2026 Q2/반기)
- latest FY actual: FY2025; 별도 기준 수치 사용 시 반드시 별도 표기
- currency/unit: KRW / 십억원
- market price, diluted shares, net cash, equity bridge: valuation date에 검증된 공식 입력이 준비되기 전 주당가치 제시 보류

## Primary: normalized mid-cycle DCF

TCK는 chamber consumable의 장수명/반복 교체와 공정 미세화 수혜가 구조적 가치 동인일 수 있지만, 고객 설비투자와 생산 가동률의 순환도 큽니다. DCF 매출을 fab/장비 설치와 가동률·소비량·점유율로 나누고, 제품 mix별 영업마진, 재고·매출채권·CAPEX를 연결해야 합니다. 2026 H1 매출/이익 성장률의 단순 연환산은 금지합니다.

현재 계산기는 성장에 필요한 재투자를 `FCFF = NOPAT × (1−g/ROIC)`로 표시하는 reinvestment identity proxy를 제공합니다. ROIC는 공시된 자본 기반 추출 전 분석자 가정입니다. 이는 충분히 공시된 세부 운전자본·D&A·CAPEX 스케줄을 대신하는 정식 FCFF가 아니며 가격목표로 표시하지 않습니다. 실전 모델에서는 D&A, maintenance/growth CAPEX, ΔNWC를 각 항목으로 모델링하고, H1 일시적 회복의 지속성을 시나리오로 바꿉니다.

## 마진 vintage

2025 OPM 약 27.8%를 출발점으로 둡니다. 과거 peak로 인용되는 약 40%를 영구 margin으로 사용하지 않습니다. `bear 25% / base 30% / bull 33%`는 주기 저점~회복을 위한 명시적 민감도이며, 현장 제품 mix/고객가동률·정규화 이익으로 분기마다 갱신해야 하는 분석자 판단입니다. Base가 2025를 넘는 근거는 2026 H1 회복과 고정비 흡수 가능성이지만, 공식적인 연간 guidance로 오인하지 않습니다.

## RIM — 잔여이익 교차검증

RIM은 기초 지배주주 자본 + 초과 ROE에서 나오는 잔여이익의 현재가치로 계산합니다. SiC 소비부품의 경쟁력이 주주가치로 이어지는지 자본효율로 묻습니다. 현금이 누적되어 장부 자본이 커질 경우, 현금수익률과 영업 ROE를 분리해야 합니다. 회사 현금/금융자산, 희석 주식수, 주주환원, 정상 ROE 및 cost of equity를 확인한 후 적용합니다.

## PER — reference only

최종연도 peak EPS가 아니라 H1 재고·가동률 영향 조정 후 normalized EPS를 씁니다. peer 표본 부족 시 목표 배수 보류. 성장 프리미엄을 주려면 공정/제품별 인증 유지와 반복 주문, 높은 중간 사이클 ROIC가 확인돼야 하며 DCF 성장 반영과 중복하지 않습니다.

## Bear/base/bull 설계

- Bear: 고객 가동률·NAND/DRAM/파운드리 투자 둔화, mix 악화, 25% normalized OPM
- Base: 2026 H1을 출발선으로 삼되 점진 정상화, 30% OPM
- Bull: 여러 공정의 인증·교체 수요가 확장되고 수율과 mix 개선, 33% OPM
- 시나리오 확률을 곱한 하나의 정밀 목표가보다 개별 가정, EV 범위, 필요한 증거를 먼저 공개
