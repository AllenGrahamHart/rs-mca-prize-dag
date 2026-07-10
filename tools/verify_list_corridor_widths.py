#!/usr/bin/env python3
"""Verify the list_corridor_widths compute packet.

This is the list-side analogue of the corridor-width arithmetic in the MCA
corridor-eater packet.  It recomputes the width table from the banked formulas:

  unsafe reserve = H(rho) / 128
  safe reserve   = tau_star(rho, log2_q=256)
  grid step      = 2^-9, except 2^-10 at rate 1/16

No search or external data is used.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TABLE = ROOT / "critical" / "nodes" / "list_corridor_widths" / "list_corridor_widths_table.json"
LGQ = 256.0
TOL = 5e-12


def lg(x: float) -> float:
    return math.log2(x)


def H(x: float) -> float:
    return -x * lg(x) - (1 - x) * lg(1 - x) if 0 < x < 1 else 0.0


def tau_star(rho: float, lgq: float = LGQ) -> float:
    lo, hi = 1e-12, 1 - rho - 1e-12
    for _ in range(300):
        mid = (lo + hi) / 2
        if mid * lgq - H(rho + mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def rate_value(label: str) -> float:
    num, den = label.split("/")
    return int(num) / int(den)


def cap_exp(rho: float) -> int:
    return 10 if abs(rho - 1 / 16) < 1e-15 else 9


def compute_row(rate: str) -> dict[str, float | str]:
    rho = rate_value(rate)
    eta = 2.0 ** -cap_exp(rho)
    h = H(rho)
    unsafe = h / 128.0
    safe = tau_star(rho)
    dyadic_hi = h / 256.0
    return {
        "rate": rate,
        "H_rho": h,
        "eta": eta,
        "unsafe_reserve_H_over_128": unsafe,
        "safe_reserve_tau_star": safe,
        "dyadic_hi_reserve_H_over_256": dyadic_hi,
        "unsafe_delta": 1 - rho - unsafe,
        "safe_delta": 1 - rho - safe,
        "dyadic_hi_delta": 1 - rho - dyadic_hi,
        "W_list": (unsafe - safe) / eta,
        "dyadic_window_width": (unsafe - dyadic_hi) / eta,
        "tau_star_minus_H_over_256_in_grid_steps": (safe - dyadic_hi) / eta,
    }


def close(a: float, b: float) -> bool:
    return abs(a - b) <= TOL


def main() -> None:
    errors: list[str] = []
    table = json.loads(TABLE.read_text())
    if table.get("node") != "list_corridor_widths":
        errors.append("node field mismatch")
    if table.get("log2_q") != 256:
        errors.append("log2_q must be 256")
    if table.get("units") != "cap-grid steps eta":
        errors.append("unexpected units")

    rows = table.get("rows", [])
    if [r.get("rate") for r in rows] != ["1/4", "1/8", "1/16"]:
        errors.append("rows must be exactly clean rates 1/4, 1/8, 1/16")

    for row in rows:
        rate = row["rate"]
        got = compute_row(rate)
        for key, val in got.items():
            if key == "rate":
                continue
            if not close(float(row[key]), float(val)):
                errors.append(
                    f"{rate} {key}: table={row[key]!r} recomputed={val!r}"
                )
        if float(row["W_list"]) <= 1.0:
            errors.append(f"{rate} W_list should exceed one grid step")
        if float(row["tau_star_minus_H_over_256_in_grid_steps"]) >= 0.025:
            errors.append(f"{rate} tau_star drift from H/256 exceeds audit bound")

    if errors:
        print("FAIL list_corridor_widths verifier")
        for err in errors:
            print(" -", err)
        raise SystemExit(1)

    print("PASS list_corridor_widths")
    for row in rows:
        print(f"{row['rate']}: W_list={row['W_list']:.12f}")


if __name__ == "__main__":
    main()
