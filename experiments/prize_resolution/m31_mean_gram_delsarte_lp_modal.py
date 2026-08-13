#!/usr/bin/env python3
"""Bounded Modal Delsarte screen for the first unpaid M31 support."""

from __future__ import annotations

import json

import modal


app = modal.App("rs-mca-m31-mean-gram-delsarte")
image = modal.Image.debian_slim().pip_install("numpy", "scipy")


@app.function(image=image, cpu=2.0, memory=1024, timeout=240)
def screen() -> dict:
    import math
    import time
    from fractions import Fraction

    import numpy as np
    from scipy.optimize import linprog

    length = 983127
    weight = 1999
    overlap = 5
    known_cap = 16203700
    payment_cap = 15860792
    distances = list(range(weight - overlap, weight + 1))
    deadline = time.monotonic() + 220.0
    rows = []

    for eigenspace in range(1, weight + 1):
        row = []
        for distance in distances:
            support_complement = weight - distance
            limit = min(distance, weight - eigenspace)
            term = math.comb(weight, support_complement)
            value = -term if distance & 1 else term
            background = length - weight - eigenspace
            for index in range(limit):
                numerator = (
                    (weight - index - support_complement)
                    * (weight - eigenspace - index)
                    * (background + index + 1)
                )
                denominator = (weight - index) * (index + 1) ** 2
                term = term * numerator // denominator
                value = value - term if (distance - index - 1) & 1 else value + term
            valency = math.comb(weight, distance) * math.comb(
                length - weight, distance
            )
            row.append(float(Fraction(value, valency)))
        rows.append(row)
        if time.monotonic() >= deadline:
            break

    matrix = -np.asarray(rows, dtype=float)
    rhs = np.ones(len(rows), dtype=float)
    objective = -np.ones(len(distances), dtype=float)
    result = linprog(
        objective,
        A_ub=matrix,
        b_ub=rhs,
        bounds=[(0.0, float(known_cap - 1))] * len(distances),
        method="highs",
        options={"time_limit": max(1.0, deadline - time.monotonic())},
    )
    payload = {
        "status": "solved" if result.success else "solver_failure",
        "matrix_status": "full" if len(rows) == weight else "partial",
        "rows_completed": len(rows),
        "rows_required": weight,
        "variables": len(distances),
        "solver_status": int(result.status),
        "message": result.message,
        "known_cap": known_cap,
        "payment_cap": payment_cap,
    }
    if result.success:
        optimum = 1.0 - float(result.fun)
        slack = rhs - matrix @ result.x
        payload.update(
            {
                "optimum": optimum,
                "improves_known_cap": optimum < known_cap,
                "payment_signal": optimum <= payment_cap,
                "minimum_inequality_slack": float(slack.min()),
                "positive_variables": int(np.count_nonzero(result.x > 1e-8)),
            }
        )
    return payload


@app.local_entrypoint()
def main() -> None:
    print(json.dumps(screen.remote(), sort_keys=True))
