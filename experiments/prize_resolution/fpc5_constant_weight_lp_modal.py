#!/usr/bin/env python3
"""Bounded Modal screen of the Johnson-scheme Delsarte LP."""

from __future__ import annotations

import json

import modal


app = modal.App("rs-mca-fpc5-constant-weight-lp")
image = modal.Image.debian_slim().pip_install("numpy", "scipy")


@app.function(image=image, cpu=2.0, memory=1024, timeout=60)
def screen() -> dict:
    import math
    import time

    import numpy as np
    from scipy.optimize import linprog

    length = 511
    weight = 255
    half_distance = 112
    known_cap = 1751945892004456252745
    variable_scale = 1_000_000.0
    distances = list(range(half_distance, weight + 1))
    deadline = time.monotonic() + 50.0
    rows = []

    for eigenspace in range(1, weight + 1):
        row = []
        for distance in distances:
            value = 0
            limit = min(distance, weight - eigenspace)
            for index in range(limit + 1):
                term = (
                    math.comb(weight - index, weight - distance)
                    * math.comb(weight - eigenspace, index)
                    * math.comb(
                        length - weight + index - eigenspace,
                        index,
                    )
                )
                value += -term if (distance - index) & 1 else term
            valency = math.comb(weight, distance) * math.comb(
                length - weight, distance
            )
            row.append(value / valency)
        rows.append(row)
        if time.monotonic() >= deadline:
            return {
                "status": "partial_matrix",
                "rows_completed": len(rows),
                "rows_required": weight,
                "variables": len(distances),
            }

    matrix = -np.asarray(rows, dtype=float)
    rhs = np.ones(weight, dtype=float)
    objective = -np.ones(len(distances), dtype=float)
    result = linprog(
        objective,
        A_ub=matrix,
        b_ub=rhs / variable_scale,
        bounds=[(0.0, float(known_cap) / variable_scale)] * len(distances),
        method="highs",
        options={"time_limit": max(1.0, deadline - time.monotonic())},
    )
    payload = {
        "status": "solved" if result.success else "solver_failure",
        "solver_status": int(result.status),
        "message": result.message,
        "rows_completed": len(rows),
        "variables": len(distances),
    }
    if result.success:
        optimum = 1.0 - variable_scale * float(result.fun)
        slack = rhs / variable_scale - matrix @ result.x
        payload.update(
            {
                "optimum": optimum,
                "optimum_log2": math.log2(optimum),
                "known_cap_log2": math.log2(known_cap),
                "saving_bits": math.log2(known_cap / optimum),
                "minimum_inequality_slack": float(slack.min()),
                "positive_variables": int(np.count_nonzero(result.x > 1e-7)),
            }
        )
    return payload


@app.local_entrypoint()
def main() -> None:
    print(json.dumps(screen.remote(), sort_keys=True))
