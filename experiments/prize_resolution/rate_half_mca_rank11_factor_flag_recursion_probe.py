#!/usr/bin/env python3
"""Probe a recursive factor-flag census for the KoalaBear rank-11 lane.

The output is only an arithmetic feasibility study.  A later DAG node must
prove that the proposed bucket recursion preserves disjoint record ownership.
"""

from __future__ import annotations

import json
import math
from math import comb


N = 2_097_152
K = 1_048_576
M = 1_116_048
W = M - K
B_STAR = 274_980_728_111_395_087
FIELD_SIZE = 2_130_706_433**6
TAU = 1_547
A = M - TAU
C0 = 2 * A - N
OUTSIDE = N - A
NEAR = 2 * W
C10 = 106_618_568_137_036_225_644
HIGH = C10 // (TAU + 1)
ANCHOR = OUTSIDE
LOW_BUDGET = B_STAR - NEAR - HIGH - ANCHOR
RANK_ONE_CAP = 8_147_918
S = 10


def falling(x: int, r: int) -> int:
    value = 1
    for i in range(r):
        value *= x - i
    return value


def ordinary_cap(q: int) -> int:
    return comb(N - K + q, q) // comb(A - K + q, q)


M_Q = {q: ordinary_cap(q) for q in range(1, S + 1)}
R_Q = {q: OUTSIDE * M_Q[q] for q in range(1, S + 1)}
R_Q[1] = RANK_ONE_CAP


def bucket_cost(q: int, delta: int) -> int:
    p = S - q
    count = falling(M, p) // (delta**p)
    return count * R_Q[q]


def exact_route_walls() -> dict[str, object]:
    shared = []
    for delta in range(1, C0 + 1):
        charge = bucket_cost(1, delta) + bucket_cost(2, delta)
        if charge <= LOW_BUDGET:
            shared.append((C0 - delta, delta, charge))
    assert shared
    best_shared = max(shared)

    two_rung = {}
    for q in (1, 2):
        best = None
        # At an optimum all available zero-floor resource is spent because
        # both charges are nonincreasing in their respective delta.
        for first in range(1, C0 + 1):
            second = C0 + 1 - first
            charge = bucket_cost(q, first) + bucket_cost(q + 1, second)
            candidate = (charge, first, second)
            if best is None or candidate < best:
                best = candidate
        assert best is not None
        two_rung[f"rank_{q}_start"] = {
            "minimum_charge": best[0],
            "first_delta": best[1],
            "second_delta": best[2],
            "excess_over_low_budget": best[0] - LOW_BUDGET,
        }
    return {
        "shared_one_rung": {
            "maximum_threshold": best_shared[0],
            "delta": best_shared[1],
            "charge": best_shared[2],
            "slack": LOW_BUDGET - best_shared[2],
        },
        "two_rung": two_rung,
    }


def continuous_deltas(terminal_dim: int) -> list[int]:
    qs = list(range(1, terminal_dim))

    def deltas(log_mu: float) -> list[int]:
        mu = math.exp(log_mu)
        out = []
        for q in qs:
            p = S - q
            log_a = math.log(R_Q[q]) + sum(math.log(M - i) for i in range(p))
            d = math.exp((math.log(mu * p) + log_a) / (p + 1))
            out.append(max(1, math.ceil(d)))
        return out

    lo, hi = -200.0, 200.0
    for _ in range(220):
        mid = (lo + hi) / 2
        ds = deltas(mid)
        cost = sum(bucket_cost(q, d) for q, d in zip(qs, ds))
        if cost <= LOW_BUDGET:
            hi = mid
        else:
            lo = mid
    ds = deltas(hi)

    # Spend remaining budget on the cheapest exact one-step decrements.  This
    # improves the residual common-zero floor without claiming global optimality.
    while True:
        cost = sum(bucket_cost(q, d) for q, d in zip(qs, ds))
        candidates = []
        for i, (q, d) in enumerate(zip(qs, ds)):
            if d > 1:
                candidates.append((bucket_cost(q, d - 1) - bucket_cost(q, d), i))
        if not candidates:
            break
        increase, i = min(candidates)
        if cost + increase > LOW_BUDGET:
            break
        ds[i] -= 1
    return ds


def row(terminal_dim: int) -> dict[str, object]:
    qs = list(range(1, terminal_dim))
    ds = continuous_deltas(terminal_dim)
    paid = sum(bucket_cost(q, d) for q, d in zip(qs, ds))
    c = C0
    flags = []
    valid = True
    for q, delta in zip(qs, ds):
        h = c - delta
        valid &= h >= 0
        flags.append(
            {
                "dimension": q,
                "zero_floor": c,
                "threshold": h,
                "delta": delta,
                "space_cap": falling(M, S - q) // delta ** (S - q),
                "bucket_cap": R_Q[q],
                "charge": bucket_cost(q, delta),
            }
        )
        c = h + 1
    return {
        "terminal_dimension": terminal_dim,
        "valid": valid and c >= 1 and paid <= LOW_BUDGET,
        "terminal_common_zero_floor": c,
        "total_delta": sum(ds),
        "paid_low": paid,
        "low_budget": LOW_BUDGET,
        "slack": LOW_BUDGET - paid,
        "flags": flags,
    }


def main() -> None:
    assert A == 1_114_501
    assert C0 == 131_850
    assert HIGH == 68_875_044_016_173_272
    assert LOW_BUDGET == 206_105_684_094_104_220
    assert M_Q[2] == 252
    assert all(M_Q[q] ** 2 < FIELD_SIZE for q in range(1, S + 1))
    print(json.dumps({"event": "caps", "M_q": M_Q, "R_q": R_Q}, sort_keys=True))
    print(json.dumps({"event": "exact_route_walls", **exact_route_walls()}, sort_keys=True))
    for terminal_dim in range(2, S + 1):
        print(json.dumps({"event": "terminal", **row(terminal_dim)}, sort_keys=True))


if __name__ == "__main__":
    main()
