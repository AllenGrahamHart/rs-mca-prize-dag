#!/usr/bin/env python3
"""Audit full-conductor E30 profile-(2,7) norms with PARI/GP."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e30_profile27_exact_norm_audit.cpp"
ORBITS = HERE / "e30_two_six_odd_light_orbit_result.json"
PRODUCTION = HERE / "e30_profile27_exact_norm_census_result.json"
RESULT = HERE / "e30_profile27_exact_norm_audit_result.json"
REMOTE_SOURCE = "/root/e30_profile27_exact_norm_audit.cpp"
REMOTE_BINARY = "/root/e30_profile27_exact_norm_audit"

app = modal.App("e1-n256-e30-profile27-exact-norm-audit")
image = (
    modal.Image.debian_slim()
    .apt_install("g++", "pari-gp")
    .add_local_file(SOURCE, REMOTE_SOURCE, copy=True)
    .run_commands(f"g++ -O3 -std=c++17 {REMOTE_SOURCE} -o {REMOTE_BINARY}")
)


@app.function(image=image, cpu=1.0, memory=512, timeout=60, max_containers=87)
def run_template(template: int, light: list[int]) -> dict[str, object]:
    import subprocess
    import time

    started = time.monotonic()
    emitted = subprocess.run(
        [REMOTE_BINARY, str(template), *(str(value) for value in light)],
        check=True, capture_output=True, text=True, timeout=20,
    )
    vectors = []
    script = ["x='x;"]
    for line in emitted.stdout.splitlines():
        values = [int(value) for value in line.split()]
        if len(values) != 14:
            raise ValueError("malformed exact-norm audit row")
        positions, coefficients = values[:7], values[7:]
        vectors.append((positions, coefficients))
        polynomial = "+".join(
            f"({coefficient})*x^{exponent}"
            for exponent, coefficient in zip(positions, coefficients, strict=True)
        )
        script.append(f"print(abs(polresultant(x^128+1,{polynomial})));")
    measured = subprocess.run(
        ["gp", "-qf"], input="\n".join(script) + "\n",
        check=True, capture_output=True, text=True, timeout=30,
    )
    norms = [int(line.strip()) for line in measured.stdout.splitlines() if line.strip()]
    if len(norms) != len(vectors) or any(norm == 0 for norm in norms):
        raise ValueError("incomplete or zero PARI norm ledger")
    maximum_norm = max(norms, default=-1)
    maximum_witness = None
    if norms:
        positions, coefficients = vectors[norms.index(maximum_norm)]
        maximum_witness = {"positions": positions, "coefficients": coefficients, "norm": maximum_norm}
    return {
        "complete": True,
        "template": template,
        "light": light,
        "full_conductor_profile_27": len(norms),
        "norm_at_or_above_2_250": sum(norm >= 2**250 for norm in norms),
        "maximum_norm": maximum_norm,
        "maximum_norm_bits": maximum_norm.bit_length() if maximum_norm >= 0 else -1,
        "maximum_witness": maximum_witness,
        "worker_seconds": time.monotonic() - started,
    }


@app.local_entrypoint()
def main() -> None:
    orbit_packet = json.loads(ORBITS.read_text())
    representatives = [row["representative"] for row in orbit_packet["rows"]]
    production = json.loads(PRODUCTION.read_text())
    rows: list[dict[str, object]] = []

    def write_checkpoint(complete: bool) -> tuple[dict[str, object], bool]:
        summary = {}
        if rows:
            summary = {
                "full_conductor_profile_27": sum(int(row["full_conductor_profile_27"]) for row in rows),
                "norm_at_or_above_2_250": sum(int(row["norm_at_or_above_2_250"]) for row in rows),
                "maximum_norm": max(int(row["maximum_norm"]) for row in rows),
                "maximum_norm_bits": max(int(row["maximum_norm_bits"]) for row in rows),
                "worker_seconds": sum(float(row["worker_seconds"]) for row in rows),
            }
        comparable = ("full_conductor_profile_27", "norm_at_or_above_2_250", "maximum_norm", "maximum_norm_bits")
        agreement = complete and all(summary[key] == production["summary"][key] for key in comparable)
        if agreement:
            for left, right in zip(production["rows"], rows):
                agreement = agreement and all(left[key] == right[key] for key in comparable)
        packet = {
            "schema": "e1-e30-profile27-exact-norm-audit-v1",
            "complete": complete,
            "agreement": agreement,
            "completed_templates": len(rows),
            "expected_templates": len(representatives),
            "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "orbits_sha256": hashlib.sha256(ORBITS.read_bytes()).hexdigest(),
            "production_sha256": hashlib.sha256(PRODUCTION.read_bytes()).hexdigest(),
            "summary": summary,
            "rows": rows,
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return summary, agreement

    write_checkpoint(False)
    try:
        for row in run_template.map(range(87), representatives):
            rows.append(row)
            write_checkpoint(False)
    except BaseException:
        print(f"E30_PROFILE27_NORM_AUDIT_INCOMPLETE completed={len(rows)}/87 result={RESULT}")
        raise
    complete = len(rows) == 87 and all(bool(row["complete"]) for row in rows)
    summary, agreement = write_checkpoint(complete)
    print("E30_PROFILE27_EXACT_NORM_AUDIT " + json.dumps(summary, sort_keys=True))
    print(f"E30_PROFILE27_EXACT_NORM_AUDIT_COMPLETE {complete}")
    print(f"E30_PROFILE27_EXACT_NORM_AGREEMENT {agreement}")
    print(f"E30_PROFILE27_EXACT_NORM_AUDIT_RESULT {RESULT}")
