#!/usr/bin/env python3
"""F4-A1 (floor campaign, Modal): the top-band count scaling ladder.

FLOOR UNDER ATTACK: PETAL-ESCAPE-BUDGET (top-band full-petal contribution
fits n^B at official-like rows). ATTACK: the banked stress run found exact
realizable counts concentrated at/beyond the top-defect band (max 5005 vs
1 below-top) at a single scale-cluster; the floor lives or dies on the
SCALING of those top-band counts. Run the existing scan (source-shipped
verbatim, stdlib-only, its own gate) at a prime LADDER — one Modal job per
target prime — and test the max top-band exact count for polynomial
growth with a scale-independent exponent. Cells truncated by the combo cap
or deadline are marked and EXCLUDED from the fit (exact cells only);
truncation is reported, never silently dropped.

PRE-REGISTERED: the falsifier fires on sustained super-polynomial growth
of exact top-band counts across >= 3 ladder rungs (the node's own dag
falsifier scoped to the floor). Poisson-scale wobble and capped cells do
not count.
"""
import json
from pathlib import Path

import modal

app = modal.App("rs-mca-f4a2b-capture")
image = modal.Image.debian_slim()

def _src():
    return Path('/home/u2470931/smooth-read-solomin/prize/experiments/'
                'petal_excess_local_scan.py').read_text()
LADDER = [3209]   # A2b: full per-config capture at the largest scale


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def rung(payload):
    import io
    import os
    import sys
    src, target = payload
    os.makedirs("/tmp/experiments/amber_stress", exist_ok=True)
    ns = {"__name__": "petal_scan", "__file__": "/tmp/a/experiments/petal_scan.py"}
    exec(src, ns)
    sys.argv = ["petal_scan", "--targets", str(target),
                "--time-limit", "45", "--combo-cap", "250000",
                "--c-min", "2", "--c-max", "14"]
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        ns["main"]()
    finally:
        sys.stdout = old
    out = Path("/tmp/experiments/amber_stress/petal_excess_local_scan_results.json")
    res = json.loads(out.read_text()) if out.exists() else {}
    configs = res.get("configs", [])
    rows = []
    for cfg in configs:
        for row in cfg.get("rows", cfg.get("cells", [])):
            rows.append(row)
    return {"target": target, "summary": res.get("summary"),
            "configs_full": configs, "n_configs": len(configs)}


@app.local_entrypoint()
def main():
    src = _src()
    payloads = [(src, t) for t in LADDER]
    results = [r for r in rung.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]
    for r in sorted(results, key=lambda r: r["target"]):
        s = r.get("summary") or {}
        print(f"p={r['target']:>6}: configs={r['n_configs']} "
              f"summary keys: { {k: s[k] for k in list(s)[:6]} if s else 'none'}")
    with open("/tmp/f4a1_ladder.json", "w") as f:
        json.dump(results, f, indent=1)
    print("raw banked to /tmp/f4a1_ladder.json — fit analysis follows locally")
