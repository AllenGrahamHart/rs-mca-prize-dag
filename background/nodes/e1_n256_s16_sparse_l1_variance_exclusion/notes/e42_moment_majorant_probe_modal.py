#!/usr/bin/env python3
"""Probe cubic logarithmic majorants for the V=84 endpoint."""

from __future__ import annotations

import modal


app = modal.App("e1-n256-e42-moment-majorant-probe")
image = modal.Image.debian_slim().pip_install("numpy", "scipy")


@app.function(image=image, cpu=1.0, memory=512, timeout=60)
def optimize() -> dict[str, object]:
    import math

    import numpy as np
    from scipy.optimize import linprog

    linear = np.linspace(0.02, 64.0, 30000)
    logarithmic = np.geomspace(1.0e-12, 0.02, 3000, endpoint=False)
    y = np.unique(np.concatenate((logarithmic, linear, np.array([16.0]))))
    x = y - 16.0
    design = np.column_stack((np.ones_like(x), x, x * x, x * x * x))
    target = math.log(16.0) - 3.0 * math.log(2.0) / 32.0
    rows = []

    for third_moment_cap in (
        600,
        900,
        1200,
        1278,
        1300,
        1500,
        1800,
        2400,
        3000,
        3200,
        3400,
        3600,
        3700,
        3750,
        3800,
        3876,
        4000,
        4032,
    ):
        objective = np.array([1.0, 0.0, 84.0, float(third_moment_cap)])
        result = linprog(
            objective,
            A_ub=-design,
            b_ub=-np.log(y),
            bounds=((None, None), (None, None), (None, None), (0.0, None)),
            method="highs",
        )
        if not result.success:
            rows.append(
                {
                    "third_moment_cap": third_moment_cap,
                    "success": False,
                    "message": result.message,
                }
            )
            continue
        coefficients = result.x
        residual = design @ coefficients - np.log(y)
        rows.append(
            {
                "third_moment_cap": third_moment_cap,
                "success": True,
                "coefficients_x_basis": coefficients.tolist(),
                "average_log_upper": float(result.fun),
                "target": target,
                "target_margin": target - float(result.fun),
                "grid_minimum_residual": float(residual.min()),
                "active_grid_y": y[np.argsort(residual)[:8]].tolist(),
            }
        )

    return {
        "complete": True,
        "grid_points": int(y.size),
        "variance": 84,
        "support_ceiling": 64,
        "rows": rows,
    }


@app.local_entrypoint()
def main() -> None:
    print("E1_N256_E42_MOMENT_MAJORANT_PROBE " + repr(optimize.remote()))
