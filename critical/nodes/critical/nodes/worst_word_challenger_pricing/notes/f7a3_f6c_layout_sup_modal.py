#!/usr/bin/env python3
"""F7-A3 + F6 third family (floor campaign, Modal): the layout-sup sweep.

ONE instrument, two floors:
- F7-A3 (engineered challenger stacking): the adversary controls the word
  layout; sweep 30 layouts x 2 scalar modes per (cell, q) and take the MAX
  challenger count — the empirical sup over the adversarial layout space.
  PRE-REGISTERED alarm: max exceeding the fitted envelope constant by a
  sustained > 3x across q (layout-engineered envelope violation).
- F6 third (word-class anti-concentration): the BAND-DETERMINATION floor
  dies if true counts collapse BELOW the model for some word class
  (crossing lower than first-moment). Same sweep, MIN and dispersion:
  PRE-REGISTERED alarm: a word class with counts sustained < 1/3 of the
  first-moment model across q (fat lower tail / anti-concentration).
Exact cells throughout (the census's own exact_cell).
"""
import json
import re
from pathlib import Path

import modal

app = modal.App("rs-mca-f7a3-layoutsup")
image = modal.Image.debian_slim().pip_install("numpy")

HERE = Path('/home/u2470931/smooth-read-solomin/prize/critical/nodes/'
            'worst_word_challenger_pricing/notes')
CELLS = [(16, 8, 1), (16, 4, 1)]
QS = [97, 193, 337]
LAYOUTS = ["cyclic_step_1"] + [f"shuffle_{s}" for s in range(101, 130)]
SCALARS = ["linear", "geometric"]


def _sources():
    core = (HERE / 'e22_core.py').read_text()
    census = (HERE / 'e22_census_modal.py').read_text()
    census = re.sub(r'^import modal\s*$', '', census, flags=re.M)
    census = re.sub(r'^app = modal\.App.*$', '', census, flags=re.M)
    census = re.sub(r'^image = .*$', '', census, flags=re.M)
    census = re.sub(r'^@app\.\w+\(.*\)\s*$', '', census, flags=re.M)
    return core, census


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def cell_at(payload):
    import sys
    import types
    core_src, census_src, q, n, k, sigma, layout, scalar = payload
    ns = {"__name__": "e22_core", "__file__": "/tmp/a/b/e22_core.py"}
    exec(core_src, ns)
    ns["P"] = q
    mod = types.ModuleType("e22_core")
    mod.__dict__.update(ns)
    sys.modules["e22_core"] = mod
    ns2 = {"__name__": "e22_census", "__file__": "/tmp/a/b/e22_census.py"}
    exec(census_src, ns2)
    ns2["P"] = q
    cell = ns2["exact_cell"](n, k, sigma, layout, scalar)
    cc = cell.get("class_counts", {})
    return {"q": q, "cell": [n, k, sigma], "layout": layout, "scalar": scalar,
            "challengers": cc.get("full_petal", 0) + cc.get("mixed_petal", 0),
            "planted": cc.get("planted", 0),
            "unclassified": cell.get("unclassified", 0)}


@app.local_entrypoint()
def main():
    import math
    core, census = _sources()
    payloads = [(core, census, q, n, k, s, lay, sc)
                for (n, k, s) in CELLS for q in QS
                for lay in LAYOUTS for sc in SCALARS]
    print(f"{len(payloads)} exact cells")
    results = [r for r in cell_at.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]
    unc_total = sum(r["unclassified"] for r in results)
    print(f"completed {len(results)}; total unclassified {unc_total}")
    for (n, k, s) in CELLS:
        print(f"\n== cell n={n} k={k} sigma={s} ==")
        for q in QS:
            rows = [r for r in results
                    if r["cell"] == [n, k, s] and r["q"] == q]
            if not rows:
                continue
            counts = sorted(r["challengers"] for r in rows)
            fm = math.comb(n, k + s) * q ** (-s)   # first-moment challengers-scale
            print(f"  q={q:>4}: layouts={len(rows)} min={counts[0]} "
                  f"med={counts[len(counts)//2]} max={counts[-1]} "
                  f"firstmom~{fm:.1f} maxlayout={max(rows, key=lambda r: r['challengers'])['layout']}")
    with open("/tmp/f7a3_results.json", "w") as f:
        json.dump(results, f, indent=1)
