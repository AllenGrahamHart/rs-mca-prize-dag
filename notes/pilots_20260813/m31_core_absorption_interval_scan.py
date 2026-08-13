#!/usr/bin/env python3
"""Exact fixed-cutoff scan for the M31 common-core absorption compiler."""

from __future__ import annotations

import json
import sys


R, D, K, BUDGET = 1048576, 67448, 6, 16777215
N, M, C = R + K, D + K, K - 1
CUTOFF = 65488


class Reject(ValueError):
    pass


def cap(e: int, h: int) -> int:
    n = N - e
    agreement = M - h
    johnson = agreement * agreement - n * C
    if johnson > 0:
        return n * (agreement - C) // johnson
    gap = -johnson
    balance = 2 * agreement * agreement - n * C
    tangent = (n - agreement) ** 2 - (n - 1) * gap
    if balance < 0 or tangent <= 0:
        raise Reject(f"undefined prefix cap e={e} h={h}")
    return ((n - 1) * n * n * (agreement - C)
            // (agreement * tangent))


def prefix(e: int) -> int:
    values = [0] + [cap(e, h) for h in range(1, CUTOFF + 1)]
    for h in range(CUTOFF - 1, 0, -1):
        values[h] = min(values[h], values[h + 1])
    return sum((values[h] - values[h - 1]) * (e // h)
               for h in range(1, CUTOFF + 1))


def boundary_cap(e: int, h: int) -> int:
    n = N - e
    inside_pair = 2 * h - e
    denominator = inside_pair * inside_pair - e * C
    outside_agreement = M - h
    if (2 * h <= e or inside_pair <= 0 or denominator <= 0 or
            not (n > outside_agreement > C)):
        raise Reject(f"undefined boundary cap e={e} h={h}")
    classes = e * (inside_pair - C) // denominator
    line = (n - C) // (outside_agreement - C)
    return 1 + classes * (line - 1)


def record(e: int) -> dict[str, int | bool]:
    s, residue = divmod(e - K, 3)
    H = e - s - 1
    if H <= CUTOFF:
        raise Reject("empty boundary stack")
    p = prefix(e)
    stack = sum(boundary_cap(e, h) for h in range(CUTOFF + 1, H + 1))
    forcing_charge = p + stack
    top_threshold = BUDGET - forcing_charge + 1
    if top_threshold < 2:
        return {
            "e": e, "residue": residue, "H": H,
            "boundary_layers": H - CUTOFF, "prefix": p,
            "boundary_charge": stack, "forcing_charge": forcing_charge,
            "top_threshold": top_threshold, "paid": False,
            "failure": "no_two_top_anchors",
        }
    if top_threshold > N - M + 1:
        return {
            "e": e, "residue": residue, "H": H,
            "boundary_layers": H - CUTOFF, "prefix": p,
            "boundary_charge": stack, "forcing_charge": forcing_charge,
            "top_threshold": top_threshold, "paid": True,
            "failure": "top_line_impossible",
        }
    core = ((top_threshold * M - N + top_threshold - 2)
            // (top_threshold - 1))
    inside_core = core - C
    sync_start = e - inside_core + K
    low_end = sync_start - 1
    agreement = M - low_end
    n = N - e
    denominator = agreement * agreement - n * C
    if denominator <= 0:
        return {
            "e": e, "residue": residue, "H": H,
            "boundary_layers": H - CUTOFF, "prefix": p,
            "boundary_charge": stack, "forcing_charge": forcing_charge,
            "top_threshold": top_threshold, "core": core,
            "inside_core": inside_core, "sync_start": sync_start,
            "paid": False, "failure": "low_johnson_undefined",
        }
    list_cap = n * (agreement - C) // denominator
    final_bound = e * list_cap + (N - M + 1)
    return {
        "e": e, "residue": residue, "H": H,
        "boundary_layers": H - CUTOFF, "prefix": p,
        "boundary_charge": stack, "forcing_charge": forcing_charge,
        "top_threshold": top_threshold, "core": core,
        "inside_core": inside_core, "sync_start": sync_start,
        "low_agreement": agreement, "low_list_cap": list_cap,
        "final_bound": final_bound, "slack": BUDGET - final_bound,
        "paid": final_bound < BUDGET,
        "failure": "" if final_bound < BUDGET else "final_budget",
    }


def main() -> None:
    global CUTOFF
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 98232
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 98700
    CUTOFF = int(sys.argv[3]) if len(sys.argv) > 3 else CUTOFF
    rows = []
    transitions = []
    previous = None
    scope_wall = None
    for e in range(start, end + 1):
        try:
            row = record(e)
        except Reject as exc:
            scope_wall = {"e": e, "reason": str(exc)}
            break
        rows.append(row)
        state = (row["paid"], row["failure"], row.get("low_list_cap"))
        if state != previous:
            transitions.append(row)
            previous = state
    paid = [row for row in rows if row["paid"]]
    summary = {
        "schema": "m31-core-absorption-interval-scan-v1",
        "range": [start, end],
        "cutoff": CUTOFF,
        "paid_count": len(paid),
        "first_paid": paid[0] if paid else None,
        "last_paid": paid[-1] if paid else None,
        "first_unpaid_after_paid": next(
            (row for row in rows
             if paid and row["e"] > paid[-1]["e"] and not row["paid"]),
            None),
        "transitions": transitions,
        "scope_wall": scope_wall,
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
