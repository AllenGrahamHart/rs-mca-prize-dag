#!/usr/bin/env python3
"""F7-A1 (floor campaign, Modal): complete the canceled pre-registered E22
census as per-cell mapped jobs (<60 s each; the original was one 6 h pooled
job, canceled at 130/135 — not a closure certificate).

FLOOR UNDER ATTACK: ROWWISE-ENVELOPE (non-planted low-slack contributions
obey the certified K_cell/q^sigma envelope at official-convention rows).
The census enumerates words beating 0.9x the planted list and classifies
every hit into the two-column form; pre-registered alarms: UNCLASSIFIED
hits (third class) or envelope-violating counts. The plan, gates, and
classification logic are the ORIGINAL script's, source-shipped verbatim;
only the execution shape changes (per-cell Modal map). Cells that exceed
60 s are flagged TIMEOUT for F7-A1b sharding — reported, never silently
dropped.
"""
import json
import re
from pathlib import Path

import modal

app = modal.App("rs-mca-f7a1-census")
image = modal.Image.debian_slim().pip_install("numpy")

HERE = Path('/home/u2470931/smooth-read-solomin/prize/critical/nodes/'
            'worst_word_challenger_pricing/notes')


def _sources():
    core = (HERE / 'e22_core.py').read_text()
    census = (HERE / 'e22_census_modal.py').read_text()
    # strip modal scaffolding from the census source so workers can exec it
    census = re.sub(r'^import modal\s*$', '', census, flags=re.M)
    census = re.sub(r'^app = modal\.App.*$', '', census, flags=re.M)
    census = re.sub(r'^image = .*$', '', census, flags=re.M)
    census = re.sub(r'^@app\.\w+\(.*\)\s*$', '', census, flags=re.M)
    return core, census


@app.function(image=image, cpu=2, memory=3072, timeout=60)
def one_cell(payload):
    core_src, census_src, spec = payload
    ns = {"__name__": "e22_core", "__file__": "/tmp/e22_core.py"}
    exec(core_src, ns)
    import sys
    import types
    mod = types.ModuleType("e22_core")
    mod.__dict__.update(ns)
    sys.modules["e22_core"] = mod
    ns2 = {"__name__": "e22_census", "__file__": "/tmp/e22_census.py"}
    exec(census_src, ns2)
    return ns2["cell_task"](tuple(spec))


@app.function(image=image, cpu=2, memory=3072, timeout=120)
def gate(payload):
    core_src, census_src = payload
    ns = {"__name__": "e22_core", "__file__": "/tmp/e22_core.py"}
    exec(core_src, ns)
    import sys
    import types
    mod = types.ModuleType("e22_core")
    mod.__dict__.update(ns)
    sys.modules["e22_core"] = mod
    ns2 = {"__name__": "e22_census", "__file__": "/tmp/e22_census.py"}
    exec(census_src, ns2)
    ok, details = ns2["gate_check"]()
    return {"ok": bool(ok), "details": str(details)[:2000],
            "plan": [list(s) for s in ns2["build_plan"]()]}


@app.local_entrypoint()
def main():
    core, census = _sources()
    g = gate.remote((core, census))
    print(f"gate passed: {g['ok']}")
    if not g["ok"]:
        print(g["details"])
        return
    plan = g["plan"]
    print(f"census plan: {len(plan)} cells; dispatching per-cell jobs")
    payloads = [(core, census, spec) for spec in plan]
    done, errs = [], []
    for r in one_cell.map(payloads, return_exceptions=True):
        (done if isinstance(r, dict) else errs).append(r)
    unclassified = [c for c in done
                    if isinstance(c, dict) and c.get("unclassified", c.get("UNCLASSIFIED", 0))]
    print(f"completed {len(done)}/{len(plan)}; timeouts/errors {len(errs)}")
    print(f"cells with UNCLASSIFIED hits: {len(unclassified)}")
    for c in unclassified[:5]:
        print("  ALARM CANDIDATE:", {k: c[k] for k in list(c)[:8]})
    with open("/tmp/f7a1_census.json", "w") as f:
        json.dump({"completed": done, "n_errors": len(errs)}, f, indent=1)
