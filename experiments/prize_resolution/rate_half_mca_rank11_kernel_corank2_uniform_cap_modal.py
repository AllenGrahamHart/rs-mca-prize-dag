#!/usr/bin/env python3
"""Audit the proposed uniform corank-two projective cap on Modal."""

from __future__ import annotations

import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
RESULT = HERE / "rate_half_mca_rank11_kernel_corank2_uniform_cap_result.json"

app = modal.App("rate-half-mca-rank11-kernel-corank2-uniform-cap")
image = modal.Image.debian_slim()

R = 1048576
W = 67472
T_MAX = R - 10
TARGET_CAP = 84416263


def row(t: int) -> dict[str, int]:
    resource = (R + t) * (R + t + 1) * (R + t + 2)
    ordered_basis_floor = 3 * W * (W + t + 1)
    cap, remainder = divmod(resource, ordered_basis_floor)
    return {
        "t": t,
        "resource": resource,
        "ordered_basis_floor": ordered_basis_floor,
        "record_cap": cap,
        "division_remainder": remainder,
        "next_integer_gap": (TARGET_CAP + 1) * ordered_basis_floor - resource,
        "ratio_step_sign": 2 * t + 3 * W + 3 - R,
    }


@app.function(image=image, cpu=1.0, memory=512, timeout=60, max_containers=1)
def audit() -> dict[str, object]:
    maximum = (-1, -1)
    first_excess: dict[str, int] | None = None
    for t in range(T_MAX + 1):
        current = row(t)
        candidate = (current["record_cap"], -t)
        if candidate > maximum:
            maximum = candidate
        if current["record_cap"] > TARGET_CAP and first_excess is None:
            first_excess = current

    turn_floor = (R - 3 * W - 3) // 2
    return {
        "schema": "rate-half-mca-rank11-kernel-corank2-uniform-cap-v1",
        "complete": True,
        "parameters": {
            "R": R,
            "w": W,
            "t_minimum": 0,
            "t_maximum": T_MAX,
            "target_cap": TARGET_CAP,
        },
        "rows": {
            "complete": row(0),
            "adjacent": row(1),
            "turn_left": row(turn_floor),
            "turn_right": row(turn_floor + 1),
            "official_endpoint": row(T_MAX),
        },
        "scan": {
            "checked_rows": T_MAX + 1,
            "maximum_record_cap": maximum[0],
            "first_maximizer": -maximum[1],
            "first_excess": first_excess,
        },
    }


@app.local_entrypoint()
def main() -> None:
    RESULT.write_text(json.dumps({"complete": False}, indent=2) + "\n")
    try:
        payload = audit.remote()
    except BaseException as error:
        RESULT.write_text(
            json.dumps(
                {"complete": False, "error": f"{type(error).__name__}: {error}"},
                indent=2,
            )
            + "\n"
        )
        raise
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))
    print(f"RESULT {RESULT}")


if __name__ == "__main__":
    main()
