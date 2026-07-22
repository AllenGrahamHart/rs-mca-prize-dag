#!/usr/bin/env python3
"""F7-A2 (floor campaign, Modal): envelope stress across q — second attack
family on the ROWWISE-ENVELOPE floor.

The floor asserts the non-planted low-slack contribution obeys the
certified envelope ~ K_cell/q^sigma at official-convention (bg <= 1)
rows. ATTACK: exact challenger counts at fixed cell shapes across a
q-LADDER (q ≡ 1 mod n, the field overridden per job); the law predicts
count*q ~ K_cell constant at sigma = 1. PRE-REGISTERED: alarm = challenger
counts EXCEEDING the fitted K_cell envelope by a sustained, growing-in-q
factor (envelope violation); flat or 1/q-tracking counts = survival.
Window-regime small q (< ~50) excluded per the banked window law.
"""
import json
import re
from pathlib import Path

import modal

app = modal.App("rs-mca-f7a2-envelope")
image = modal.Image.debian_slim().pip_install("numpy")

HERE = Path('/home/u2470931/smooth-read-solomin/prize/critical/nodes/'
            'worst_word_challenger_pricing/notes')
QLADDER = [97, 113, 193, 241, 337, 449, 577, 769, 1153]
CELLS = [(16, 8, 1, "cyclic_step_1", "linear"),
         (16, 8, 1, "cyclic_step_1", "geometric"),
         (16, 4, 1, "cyclic_step_1", "linear"),
         (16, 8, 2, "cyclic_step_1", "linear")]


def _sources():
    core = (HERE / 'e22_core.py').read_text()
    census = (HERE / 'e22_census_modal.py').read_text()
    census = re.sub(r'^import modal\s*$', '', census, flags=re.M)
    census = re.sub(r'^app = modal\.App.*$', '', census, flags=re.M)
    census = re.sub(r'^image = .*$', '', census, flags=re.M)
    census = re.sub(r'^@app\.\w+\(.*\)\s*$', '', census, flags=re.M)
    return core, census


@app.function(image=image, cpu=2, memory=3072, timeout=60)
def envelope_cell(payload):
    import sys
    import types
    core_src, census_src, q, spec = payload
    ns = {"__name__": "e22_core", "__file__": "/tmp/a/b/e22_core.py"}
    exec(core_src, ns)
    ns["P"] = q
    mod = types.ModuleType("e22_core")
    mod.__dict__.update(ns)
    sys.modules["e22_core"] = mod
    ns2 = {"__name__": "e22_census", "__file__": "/tmp/a/b/e22_census.py"}
    exec(census_src, ns2)
    ns2["P"] = q
    n, k, sigma, layout, scalar = spec
    cell = ns2["exact_cell"](n, k, sigma, layout, scalar)
    ch = sum(cell.get("class_counts", {}).get(c, 0)
             for c in ("full_petal", "mixed_petal"))
    unc = cell.get("unclassified", 0)
    return {"q": q, "spec": list(spec), "challengers": ch,
            "unclassified": unc, "planted": cell.get("class_counts", {}).get("planted"),
            "kind": cell.get("kind")}


@app.local_entrypoint()
def main():
    core, census = _sources()
    payloads = [(core, census, q, spec) for spec in CELLS for q in QLADDER]
    results = [r for r in envelope_cell.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]
    by_cell = {}
    for r in results:
        by_cell.setdefault(tuple(r["spec"]), []).append(r)
    any_alarm = False
    for spec, rows in sorted(by_cell.items()):
        rows.sort(key=lambda r: r["q"])
        print(f"\n== cell {spec} ==")
        kqs = []
        for r in rows:
            kq = r["challengers"] * r["q"] ** spec[2]
            kqs.append(kq)
            print(f"  q={r['q']:>5}: challengers={r['challengers']:>5} "
                  f"count*q^s={kq:>9} unclassified={r['unclassified']}")
        # envelope check: count*q^sigma should be ~constant (or shrink);
        # alarm = monotone growth by > 3x from the median across the ladder tail
        if len(kqs) >= 5:
            med = sorted(kqs)[len(kqs) // 2]
            grow = kqs[-1] > 3 * max(med, 1) and kqs[-2] > 2 * max(med, 1)
            if grow:
                any_alarm = True
                print("  <-- ENVELOPE ALARM (sustained super-envelope growth)")
    print(f"\nany alarm: {any_alarm}")
    with open("/tmp/f7a2_results.json", "w") as f:
        json.dump(results, f, indent=1)
