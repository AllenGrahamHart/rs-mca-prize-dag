#!/usr/bin/env python3
"""Probe the all-corank projective-paving kernel capacity on Modal."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
RESULT = HERE / "rate_half_mca_rank11_kernel_projective_paving_probe_result.json"

app = modal.App("rate-half-mca-rank11-kernel-projective-paving-probe")
image = modal.Image.debian_slim().pip_install("scipy==1.16.1")

N_OFFSET = 1048576
M_OFFSET = 67472
RESIDUAL = 274980728111260126
SAMPLES = (
    377673,
    377674,
    568338,
    568339,
    796598,
    796599,
    850000,
    900000,
    950000,
    1000000,
    1048576,
)


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def projective_record_cap(dimension: int) -> int:
    n = N_OFFSET + dimension
    m = M_OFFSET + dimension
    bases = (dimension + 1) * falling(m - 1, dimension)
    return falling(n, dimension + 1) // bases


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def effective_record_cap(kprime: int, dimension: int, projective_caps: list[int]) -> int:
    if dimension == 1:
        return projective_caps[0]
    shortened = kprime - 10 + dimension
    unshortened = Fraction(
        falling(N_OFFSET + shortened, dimension + 1),
        (M_OFFSET + shortened) * rising(M_OFFSET + 1, dimension - 1),
    )
    near_complete = Fraction(
        falling(N_OFFSET + dimension + 1, dimension + 1),
        (M_OFFSET + dimension + 1) * rising(M_OFFSET + 1, dimension - 1),
    )
    cap = int(max(
        unshortened,
        near_complete,
        projective_caps[dimension - 1],
    ))
    if dimension == 9:
        cap = min(cap, 61871313426630599)
    return cap


def cap_data(kprime: int, projective_caps: list[int]) -> tuple[list[Fraction], list[int], list[str]]:
    nprime = N_OFFSET + kprime
    mprime = M_OFFSET + kprime
    caps = []
    records = []
    branches = []
    for dimension in range(1, 10):
        record = effective_record_cap(kprime, dimension, projective_caps)
        extension = comb(kprime - 10, dimension + 1)
        ambient = Fraction(
            comb(nprime, 10 - dimension)
            * record
            * extension
            // (dimension + 2),
            RESIDUAL,
        )
        support = Fraction(
            comb(mprime, 10 - dimension) * extension // (dimension + 2)
        )
        caps.append(min(ambient, support))
        records.append(record)
        branches.append("ambient" if ambient <= support else "record")
    return caps, records, branches


def raising(kprime: int, step: int, source: int) -> Fraction:
    return Fraction(
        comb(source + 2, step) * comb(M_OFFSET + source, step),
        comb(kprime - source - 11 + step, step),
    )


def multiplicity(step: int, source: int) -> int:
    return comb(9 - source + step, step)


def solve_sample(kprime: int, record_caps: list[int]) -> dict[str, object]:
    import numpy as np
    from scipy.optimize import linprog

    caps, effective_caps, branches = cap_data(kprime, record_caps)
    objective_scale = max(caps)
    c = -np.array([float(cap / objective_scale) for cap in caps])
    rows: list[list[float]] = []
    bounds: list[float] = []
    names: list[str] = []

    mprime = M_OFFSET + kprime
    shadow_budget = comb(mprime, 9)
    shadow = [
        Fraction(comb(dimension + 2, 2), comb(kprime - dimension - 9, 2))
        for dimension in range(1, 10)
    ]
    rows.append([float(shadow[i] * caps[i] / shadow_budget) for i in range(9)])
    bounds.append(1.0)
    names.append("shadow")

    e0 = comb(mprime - 9, 2)
    containment_budget = e0 * comb(mprime, 9)
    containment = [
        52 + Fraction(3 * e0, comb(kprime - 10, 2)),
        55 + Fraction(6 * comb(67474, 2), comb(kprime - 11, 2)),
        *[Fraction(55) for _ in range(7)],
    ]
    rows.append(
        [
            float(containment[i] * caps[i] / containment_budget)
            for i in range(9)
        ]
    )
    bounds.append(1.0)
    names.append("containment")

    for step in range(2, 9):
        for source in range(step + 1, 10):
            target = source - step
            row = [0.0 for _ in range(9)]
            row[source - 1] = float(
                raising(kprime, step, source)
                * caps[source - 1]
                / (multiplicity(step, source) * caps[target - 1])
            )
            row[target - 1] = -1.0
            rows.append(row)
            bounds.append(0.0)
            names.append(f"hierarchy_{step}_{source}")

    solution = linprog(
        c,
        A_ub=np.array(rows),
        b_ub=np.array(bounds),
        bounds=[(0.0, 1.0) for _ in range(9)],
        method="highs",
    )
    if not solution.success:
        raise RuntimeError(solution.message)

    y = solution.x
    allocation = [float(caps[i]) * float(y[i]) for i in range(9)]
    optimum = sum(allocation)
    demand = float(Fraction(495405467 * comb(mprime, 11), 10**9))
    slacks = np.array(bounds) - np.array(rows) @ y
    return {
        "kprime": kprime,
        "closed": demand > optimum,
        "demand_over_capacity": demand / optimum,
        "active_caps": [i + 1 for i, value in enumerate(y) if abs(value - 1.0) <= 1e-7],
        "positive_coranks": [i + 1 for i, value in enumerate(y) if value >= 1e-10],
        "active_rows": [names[i] for i, slack in enumerate(slacks) if abs(slack) <= 1e-7],
        "effective_record_caps": effective_caps,
        "individual_cap_branches": branches,
        "scaled_allocation": [float(value) for value in y],
    }


@app.function(image=image, cpu=1.0, memory=512, timeout=60, max_containers=1)
def probe() -> dict[str, object]:
    record_caps = [projective_record_cap(dimension) for dimension in range(1, 10)]
    left, right = 377673, 523405
    while left < right:
        middle = (left + right + 1) // 2
        if solve_sample(middle, record_caps)["closed"]:
            left = middle
        else:
            right = middle - 1
    return {
        "schema": "rate-half-mca-rank11-kernel-projective-paving-probe-v1",
        "record_caps": record_caps,
        "frontier": [
            solve_sample(left, record_caps),
            solve_sample(left + 1, record_caps),
        ],
        "samples": [solve_sample(kprime, record_caps) for kprime in SAMPLES],
    }


@app.local_entrypoint()
def main() -> None:
    RESULT.write_text(json.dumps({"complete": False}, indent=2) + "\n")
    try:
        payload = probe.remote()
    except BaseException as error:
        RESULT.write_text(
            json.dumps(
                {"complete": False, "error": f"{type(error).__name__}: {error}"},
                indent=2,
            )
            + "\n"
        )
        raise
    payload["complete"] = True
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))
    print(f"RESULT {RESULT}")


if __name__ == "__main__":
    main()
