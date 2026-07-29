"""Bounded route probe for the conductor-256 unit-log L1 minimum.

This is an exploratory floating-point MILP, not a proof certificate.  It uses
the proved exponent box from the E1 character-eigenvalue preflight and fixes
the cyclic/sign symmetry by putting a largest absolute exponent at index 0.
"""

from __future__ import annotations

import json

import modal


APP = modal.App("e1-conductor256-l1-svp-probe")
IMAGE = modal.Image.debian_slim(python_version="3.12").pip_install(
    "numpy==2.3.2",
    "scipy==1.16.1",
    "mpmath==1.3.0",
)


@APP.function(image=IMAGE, cpu=2.0, memory=2048, timeout=280, max_containers=1)
def solve() -> dict[str, object]:
    import mpmath as mp
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, milp

    order = 64
    exponent_bound = 7
    mp.mp.dps = 80

    representatives: list[int] = []
    value = 1
    for _ in range(order):
        representatives.append(min(value, 256 - value))
        value = (5 * value) % 256
    assert len(set(representatives)) == order

    f = [
        2 * mp.log(abs(mp.sin(mp.pi * representative / 256)))
        for representative in representatives
    ]
    convolution = np.array(
        [[float(f[(s + t) % order]) for t in range(order)] for s in range(order)],
        dtype=np.float64,
    )

    # Variables are xi[0:64] (integer) followed by y[0:64] (continuous),
    # where y majorizes the absolute logarithmic embedding.
    variable_count = 2 * order
    objective = np.concatenate((np.zeros(order), np.ones(order)))
    lower = np.concatenate(
        (-exponent_bound * np.ones(order), np.zeros(order))
    )
    upper = np.concatenate(
        (exponent_bound * np.ones(order), np.full(order, np.inf))
    )
    integrality = np.concatenate((np.ones(order), np.zeros(order)))

    rows: list[np.ndarray] = []
    row_lower: list[float] = []
    row_upper: list[float] = []

    # Sum xi=0 is the canonical full-basis parametrization.
    row = np.zeros(variable_count)
    row[:order] = 1
    rows.append(row)
    row_lower.append(0)
    row_upper.append(0)

    # Every nonzero zero-sum vector has, after sign and cyclic shift, a
    # positive largest-absolute coordinate at index zero.
    row = np.zeros(variable_count)
    row[0] = 1
    rows.append(row)
    row_lower.append(1)
    row_upper.append(np.inf)
    for t in range(1, order):
        row = np.zeros(variable_count)
        row[0] = 1
        row[t] = -1
        rows.append(row)
        row_lower.append(0)
        row_upper.append(np.inf)

        row = np.zeros(variable_count)
        row[0] = 1
        row[t] = 1
        rows.append(row)
        row_lower.append(0)
        row_upper.append(np.inf)

    # y_s >= +(T xi)_s and y_s >= -(T xi)_s.
    for s in range(order):
        row = np.zeros(variable_count)
        row[:order] = -convolution[s]
        row[order + s] = 1
        rows.append(row)
        row_lower.append(0)
        row_upper.append(np.inf)

        row = np.zeros(variable_count)
        row[:order] = convolution[s]
        row[order + s] = 1
        rows.append(row)
        row_lower.append(0)
        row_upper.append(np.inf)

    constraints = LinearConstraint(
        np.vstack(rows), np.array(row_lower), np.array(row_upper)
    )
    result = milp(
        c=objective,
        integrality=integrality,
        bounds=Bounds(lower, upper),
        constraints=constraints,
        options={
            "disp": True,
            "mip_rel_gap": 0.0,
            "presolve": True,
            "time_limit": 240.0,
        },
    )

    exponent = None
    recomputed_l1 = None
    if result.x is not None:
        exponent = [int(round(item)) for item in result.x[:order]]
        assert sum(exponent) == 0
        exact_logs = [
            sum(mp.mpf(exponent[t]) * f[(s + t) % order] for t in range(order))
            for s in range(order)
        ]
        recomputed_l1 = mp.fsum(abs(item) for item in exact_logs)

    payload: dict[str, object] = {
        "success": bool(result.success),
        "status": int(result.status),
        "message": str(result.message),
        "objective": None if result.fun is None else float(result.fun),
        "recomputed_l1_70dp": (
            None if recomputed_l1 is None else mp.nstr(recomputed_l1, 70)
        ),
        "mip_dual_bound": (
            None
            if getattr(result, "mip_dual_bound", None) is None
            else float(result.mip_dual_bound)
        ),
        "mip_gap": (
            None if getattr(result, "mip_gap", None) is None else float(result.mip_gap)
        ),
        "mip_node_count": (
            None
            if getattr(result, "mip_node_count", None) is None
            else int(result.mip_node_count)
        ),
        "exponent": exponent,
        "threshold": 77.202,
    }
    print("E1_CONDUCTOR256_L1_SVP_PROBE " + json.dumps(payload, sort_keys=True))
    return payload


@APP.local_entrypoint()
def main() -> None:
    result = solve.remote()
    print(json.dumps(result, indent=2, sort_keys=True))
