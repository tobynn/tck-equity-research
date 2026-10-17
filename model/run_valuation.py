#!/usr/bin/env python3
"""Mid-cycle EV sensitivity proxy for TCK; not a full FCFF valuation."""
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parent
with (ROOT.parent / "data" / "actuals.csv").open(encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
base = next(r for r in rows if r["period"] == "2025")
rev0 = float(base["revenue_bn_krw"])
scenarios = {
    "bear": dict(g1=0.04, g=0.03, margin=0.25, roic=0.14, wacc=0.11, tg=0.015),
    "base": dict(g1=0.12, g=0.09, margin=0.30, roic=0.18, wacc=0.10, tg=0.020),
    "bull": dict(g1=0.20, g=0.15, margin=0.33, roic=0.20, wacc=0.095, tg=0.025),
}
tax = 0.24
out = []
for name, p in scenarios.items():
    revenue, pv = rev0, 0.0
    for year in range(1, 6):
        revenue *= 1 + (p["g1"] if year == 1 else p["g"])
        # Steady-state reinvestment identity; ROIC is an analyst assumption.
        growth = p["g1"] if year == 1 else p["g"]
        nopat = revenue * p["margin"] * (1 - tax)
        fcff_proxy = nopat * (1 - growth / p["roic"])
        pv += fcff_proxy / (1 + p["wacc"]) ** year
    terminal_nopat = nopat * (1 + p["tg"])
    terminal_fcff = terminal_nopat * (1 - p["tg"] / p["roic"])
    tv = terminal_fcff / (p["wacc"] - p["tg"])
    ev = pv + tv / (1 + p["wacc"]) ** 5
    out.append({"scenario": name, "revenue_growth_y1": p["g1"], "revenue_growth_y2_y5": p["g"], "normalized_ebit_margin": p["margin"],
                "normalized_roic": p["roic"], "wacc": p["wacc"], "terminal_growth": p["tg"], "ev_proxy_krw_bn": round(ev, 1),
                "status": "ROIC reinvestment-identity DCF proxy; analyst ROIC and bridge inputs pending DART extraction"})
with (ROOT / "dcf_sensitivity.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=out[0].keys()); w.writeheader(); w.writerows(out)
for r in out:
    print(f"{r['scenario']}: EV proxy KRW {r['ev_proxy_krw_bn']:,.1f}bn")
