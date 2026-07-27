#!/usr/bin/env python3
"""Compute exact resultants for full-conductor E32 profile-(4,7) vectors."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e32_profile47_exact_norm_census.cpp"
ORBITS = HERE / "e32_four_odd_light_orbit_result.json"
RESULT = HERE / "e32_profile47_exact_norm_census_result.json"
PILOT_RESULT = HERE / "e32_profile47_exact_norm_census_pilot_result.json"
REMOTE_SOURCE = "/root/e32_profile47_exact_norm_census.cpp"
REMOTE_BINARY = "/root/e32_profile47_exact_norm_census"

app = modal.App("e1-n256-e32-profile47-exact-norm-census")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .pip_install("python-flint")
    .add_local_file(SOURCE, REMOTE_SOURCE, copy=True)
    .run_commands(f"g++ -O3 -std=c++17 {REMOTE_SOURCE} -o {REMOTE_BINARY}")
)


@app.function(image=image, cpu=1.0, memory=512, timeout=60)
def run_template(template: int, light: list[int]) -> dict[str, object]:
    import subprocess
    import time

    from flint import fmpz_poly

    started = time.monotonic()
    completed = subprocess.run(
        [REMOTE_BINARY, str(template), *(str(value) for value in light)],
        check=True,
        capture_output=True,
        text=True,
        timeout=20,
    )
    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    maximum_norm = -1
    maximum_witness: dict[str, object] | None = None
    at_or_above = 0
    count = 0
    for line in completed.stdout.splitlines():
        values = [int(value) for value in line.split()]
        if len(values) != 14:
            raise ValueError("malformed exact-norm census row")
        positions = values[:7]
        coefficients = values[7:]
        dense = [0] * 128
        for exponent, coefficient in zip(positions, coefficients, strict=True):
            dense[exponent] = coefficient
        norm = abs(int(cyclotomic.resultant(fmpz_poly(dense))))
        if norm == 0:
            raise ValueError("zero characteristic-zero norm")
        count += 1
        at_or_above += norm >= 2**250
        if norm > maximum_norm:
            maximum_norm = norm
            maximum_witness = {
                "positions": positions,
                "coefficients": coefficients,
                "norm": norm,
            }
    return {
        "complete": True,
        "template": template,
        "light": light,
        "full_conductor_profile_47": count,
        "norm_at_or_above_2_250": at_or_above,
        "maximum_norm": maximum_norm,
        "maximum_norm_bits": maximum_norm.bit_length() if maximum_norm >= 0 else -1,
        "maximum_witness": maximum_witness,
        "worker_seconds": time.monotonic() - started,
    }


@app.local_entrypoint()
def main(templates: str = "") -> None:
    orbit_packet = json.loads(ORBITS.read_text())
    representatives = [row["representative"] for row in orbit_packet["rows"]]
    selected = (
        [int(value) for value in templates.split(",") if value]
        if templates
        else list(range(len(representatives)))
    )
    if len(set(selected)) != len(selected) or any(
        value < 0 or value >= len(representatives) for value in selected
    ):
        raise ValueError("invalid template selection")
    rows = list(
        run_template.map(selected, [representatives[index] for index in selected])
    )
    packet = {
        "schema": "e1-e32-profile47-exact-norm-census-v1",
        "complete": all(bool(row["complete"]) for row in rows),
        "selected_templates": selected,
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "orbits_sha256": hashlib.sha256(ORBITS.read_bytes()).hexdigest(),
        "summary": {
            "full_conductor_profile_47": sum(
                int(row["full_conductor_profile_47"]) for row in rows
            ),
            "norm_at_or_above_2_250": sum(
                int(row["norm_at_or_above_2_250"]) for row in rows
            ),
            "maximum_norm": max(int(row["maximum_norm"]) for row in rows),
            "maximum_norm_bits": max(int(row["maximum_norm_bits"]) for row in rows),
            "worker_seconds": sum(float(row["worker_seconds"]) for row in rows),
        },
        "rows": rows,
    }
    destination = PILOT_RESULT if templates else RESULT
    destination.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print("E32_PROFILE47_EXACT_NORM_CENSUS " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E32_PROFILE47_EXACT_NORM_RESULT {destination}")
