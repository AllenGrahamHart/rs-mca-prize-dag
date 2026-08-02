#!/usr/bin/env python3
"""Lift the sole nonunit cell-3 exceptional common algebra over F_p."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
CHARTS = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_exceptional_common_charts_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_exceptional_point_lift_result.json"
REMOTE_CHARTS = "/root/cell3_exceptional_common_charts.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell3-exceptional-point-lift")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(CHARTS, REMOTE_CHARTS)
)


@app.function(image=image, cpu=1.0, memory=1024, timeout=60)
def lift_point():
    import sympy as sp

    payload_bytes = Path(REMOTE_CHARTS).read_bytes()
    rows = json.loads(payload_bytes)["rows"]
    survivors = [row for row in rows if row["status"] == "COMPLETE"
                 and row.get("unit") is False]
    if len(survivors) != 1 or survivors[0]["t"] != 1288361599:
        raise RuntimeError("unexpected exceptional survivor")
    trace = 891442763
    discriminant = (trace*trace - 4) % PRIME
    roots_discriminant = sorted(
        int(value) % PRIME
        for value in sp.sqrt_mod(discriminant, PRIME, all_roots=True)
    )
    inverse_two = pow(2, -1, PRIME)
    b_roots = sorted({
        ((trace + value)*inverse_two) % PRIME
        for value in roots_discriminant
    })
    points = [
        {
            "t": 1288361599,
            "r": 700051530,
            "b": b_value,
            "c": (736842529*b_value + 915102487) % PRIME,
        }
        for b_value in b_roots
    ]
    return {
        "status": "COMPLETE",
        "field": PRIME,
        "source_charts_sha256": hashlib.sha256(payload_bytes).hexdigest(),
        "quadratic": "b^2-891442763*b+1",
        "discriminant": discriminant,
        "legendre": pow(discriminant, (PRIME-1)//2, PRIME),
        "discriminant_roots": roots_discriminant,
        "b_roots": b_roots,
        "deployed_points": points,
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell3-exceptional-point-lift-v1",
        "scope": (
            "Exact deployed-field lift of the sole nonunit exceptional common "
            "algebra; no outside, orbit, or Prize claim."
        ),
        "result": lift_point.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "status": output["result"].get("status"),
        "legendre": output["result"].get("legendre"),
        "b_roots": output["result"].get("b_roots"),
        "deployed_points": output["result"].get("deployed_points"),
    }, sort_keys=True))
