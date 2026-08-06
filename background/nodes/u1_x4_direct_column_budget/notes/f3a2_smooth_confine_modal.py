#!/usr/bin/env python3
"""F3-A1 (floor campaign, Modal): boundary-row sweep for the u1_x4 n^3
direct-column floor — the existing probe's rows re-run per-row on Modal
with FULL anchor windows (the local run was 60s-capped with sliced
windows), plus an extended boundary-prime grid (the node's own attack
surface: boundary p ≡ 1 mod n rows are where hn/n^2 trophies can fail).

FLOOR: fully-stripped primitive active-core residue <= n^3 at official
corridor rows. Pre-registered falsifier: a certified row/slice with more
than n^3 post-strip non-toral primitive trades. Alarm metric = the probe's
own direct_n3 flag; positive control (n16 h4 p17: 60 trades detected)
must fire for the run to count (instrument gate).
"""
import json
from pathlib import Path

import modal

app = modal.App("rs-mca-f3a2-smooth-confine")
image = modal.Image.debian_slim()


def _src():
    return Path('/home/u2470931/smooth-read-solomin/prize/experiments/'
                'u1_x4_active_core_budget_probe.py').read_text()


@app.function(image=image, cpu=2, memory=3072, timeout=60)
def probe_row(payload):
    import time
    src, row = payload
    ns = {"__name__": "u1probe", "__file__": "/tmp/a/b/u1probe.py"}
    exec(src, ns)
    deadline = time.monotonic() + 50.0
    out = ns["anchored_mitm"](dict(row), deadline)
    slim = {k: out.get(k) for k in
            ("name", "n", "h", "p", "anchored_nontoral_trades",
             "direct_n3_budget", "direct_n3_exceeded", "old_n2_budget",
             "partial", "anchors_checked", "trades_found") if k in out}
    slim["row"] = row
    return slim


@app.local_entrypoint()
def main():
    src = _src()
    ns = {"__name__": "u1probe", "__file__": "/tmp/a/b/u1probe.py"}
    exec(src, ns)
    npm = ns["next_prime_1mod"]
    rows = [
        {"name": "GATE_exceptional_n16_h4_p17", "n": 16, "h": 4, "p": 17, "W": 16},
        # F3-A2: adversarially SMOOTH q (rich subgroup structure) at n=32, full windows
        {"name": "smooth_n32_h6_p40961", "n": 32, "h": 6, "p": 40961, "W": 32},
        {"name": "smooth_n32_h7_p40961", "n": 32, "h": 7, "p": 40961, "W": 32},
        {"name": "smooth_n32_h6_p61441", "n": 32, "h": 6, "p": 61441, "W": 32},
        {"name": "smooth_n32_h7_p61441", "n": 32, "h": 7, "p": 61441, "W": 32},
        {"name": "smooth_n32_h6_p65537", "n": 32, "h": 6, "p": 65537, "W": 32},
        {"name": "smooth_n32_h7_p65537", "n": 32, "h": 7, "p": 65537, "W": 32},
        # F3 third family: exceptional-regime CONFINEMENT at n=16 (small fields
        # where the known exceptional control lives; floor regime is q >= n^2)
        {"name": "confine_n16_h4_p97", "n": 16, "h": 4, "p": 97, "W": 16},
        {"name": "confine_n16_h5_p97", "n": 16, "h": 5, "p": 97, "W": 16},
        {"name": "confine_n16_h4_p113", "n": 16, "h": 4, "p": 113, "W": 16},
        {"name": "confine_n16_h5_p113", "n": 16, "h": 5, "p": 113, "W": 16},
        {"name": "confine_n16_h4_p241", "n": 16, "h": 4, "p": 241, "W": 16},
        {"name": "confine_n16_h5_p241", "n": 16, "h": 5, "p": 241, "W": 16},
        {"name": "confine_n16_h4_p337", "n": 16, "h": 4, "p": 337, "W": 16},
    ]
    payloads = [(src, r) for r in rows]
    results = [r for r in probe_row.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]
    gate = next((r for r in results if r["row"]["name"].startswith("GATE")), None)
    gate_trades = (gate or {}).get("anchored_nontoral_trades",
                                   (gate or {}).get("trades_found"))
    print(f"instrument gate (expect ~60 nontoral at n16/h4/p17): {gate_trades}")
    alarms = []
    for r in results:
        exceeded = r.get("direct_n3_exceeded")
        flag = "  <-- N3 ALARM" if exceeded else ""
        print(f"{r['row']['name']:>28}: trades={r.get('anchored_nontoral_trades', r.get('trades_found'))} "
              f"budget={r.get('direct_n3_budget')} partial={r.get('partial')}{flag}")
        if exceeded:
            alarms.append(r)
    print(f"\nrows completed {len(results)}/{len(rows)}; N3 alarms: {len(alarms)}")
    with open("/tmp/f3a1_results.json", "w") as f:
        json.dump(results, f, indent=1)
