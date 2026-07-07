#!/usr/bin/env python3
"""Falsification probe for dli_prime_weighted_large_block_support.

The old per-profile sup formulation is already refuted.  This script attacks
the corrected U-weighted-average obligation on a concrete central-family model.

For profiles choosing an active ternary domain {-1,0,+1} on S and inactive
domain {0} off S, with profile weight U(S)=3^|S|, the U-weighted average of
rho(S)=q^L B(S)/3^|S| over all S is exactly

    q^L * Pr[A d = 0],

where d_i are independent with Pr[d_i=0]=1/2 and Pr[d_i=+1]=Pr[d_i=-1]=1/4.
This is the weighted object, not the broken sup object.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import time
from typing import Dict, Iterable, List, Sequence, Tuple


RESULT_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "results",
    "dli_weighted_average_probe.json",
)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def factor(n: int) -> Dict[int, int]:
    out: Dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def primitive_root(p: int) -> int:
    assert is_prime(p)
    fac = list(factor(p - 1))
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in fac):
            return g
    raise ValueError(f"no primitive root found for {p}")


def zeta_root(q: int, n: int) -> int:
    if (q - 1) % n != 0:
        raise ValueError(f"n={n} does not divide q-1={q-1}")
    g = primitive_root(q)
    z = pow(g, (q - 1) // n, q)
    assert pow(z, n, q) == 1
    assert n == 1 or pow(z, n // 2, q) != 1
    return z


def section_indices(n: int, count: int, mode: str) -> List[int]:
    h = n // 2
    if count > h:
        raise ValueError(f"count={count} exceeds square-root section size {h}")
    if mode == "prefix":
        return list(range(count))
    if mode == "spread":
        return sorted({(i * h) // count for i in range(count)})
    if mode == "alternating":
        evens = list(range(0, h, 2))
        odds = list(range(1, h, 2))
        return (evens + odds)[:count]
    raise ValueError(f"unknown mode {mode}")


def vector_for_index(zeta: int, q: int, n: int, idx: int, L: int) -> Tuple[int, ...]:
    return tuple(pow(zeta, ((2 * ell + 1) * idx) % n, q) for ell in range(L))


def roll_nd(arr, shifts: Sequence[int], q: int):
    import numpy as np

    out = arr
    for axis, shift in enumerate(shifts):
        shift %= q
        if shift:
            out = np.roll(out, shift, axis=axis)
    return out


def weighted_average_dp(q: int, n: int, L: int, count: int, mode: str) -> Dict[str, object]:
    """Exact floating-probability DP for q^L * Pr[A d = 0]."""
    import numpy as np

    zeta = zeta_root(q, n)
    indices = section_indices(n, count, mode)
    shape = (q,) * L
    dist = np.zeros(shape, dtype=np.float64)
    dist[(0,) * L] = 1.0

    t0 = time.time()
    for idx in indices:
        v = vector_for_index(zeta, q, n, idx, L)
        plus = roll_nd(dist, v, q)
        minus = roll_nd(dist, tuple((-x) % q for x in v), q)
        dist = 0.5 * dist + 0.25 * plus + 0.25 * minus

    prob_zero = float(dist[(0,) * L])
    avg_rho = (q**L) * prob_zero
    logq_avg = math.log(avg_rho, q) if avg_rho > 0 else float("-inf")
    mass_error = abs(float(dist.sum()) - 1.0)
    return {
        "q": q,
        "n": n,
        "L": L,
        "coordinate_count": count,
        "coordinate_mode": mode,
        "state_count": q**L,
        "prob_zero": prob_zero,
        "weighted_average_rho": avg_rho,
        "log_q_weighted_average": logq_avg,
        "log_q_per_L": logq_avg / L,
        "mass_error": mass_error,
        "seconds": time.time() - t0,
    }


def log2_choose(n: int, k: int) -> float:
    if k < 0 or k > n:
        return float("-inf")
    return (
        math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
    ) / math.log(2.0)


def log2_sum(values: Iterable[float]) -> float:
    vals = [v for v in values if math.isfinite(v)]
    if not vals:
        return float("-inf")
    m = max(vals)
    return m + math.log2(sum(2.0 ** (v - m) for v in vals))


def low_mass_entropy_envelope(q_bits: int, alpha_values: Sequence[int], L_values: Sequence[int]):
    rows = []
    for alpha in alpha_values:
        for L in L_values:
            N = alpha * L
            # Zero-skew contribution from all supports |S|<=L in the
            # inactive-or-ternary U-weighted profile family:
            #   q^L * sum_{k<=L} C(N,k) / 4^N.
            log2_low_sum = log2_sum(log2_choose(N, k) for k in range(L + 1))
            log2_contribution = q_bits * L + log2_low_sum - 2 * N
            rows.append(
                {
                    "q_bits": q_bits,
                    "alpha": alpha,
                    "L": L,
                    "N": N,
                    "log2_low_support_count_sum": log2_low_sum,
                    "log_q_zero_skew_low_mass_contribution": log2_contribution / q_bits,
                    "log_q_per_L": log2_contribution / (q_bits * L),
                }
            )
    return rows


def write_result(payload: Dict[str, object]) -> None:
    os.makedirs(os.path.dirname(RESULT_PATH), exist_ok=True)
    tmp = RESULT_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    os.replace(tmp, RESULT_PATH)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seconds", type=float, default=55.0)
    args = ap.parse_args()

    started = time.time()
    payload: Dict[str, object] = {
        "script": os.path.relpath(__file__),
        "started_unix": started,
        "actual_obligation": (
            "corrected dli U-weighted average of rho_j over central profiles; "
            "not the refuted per-profile sup formulation"
        ),
        "weighted_identity": (
            "For inactive/ternary profiles, the U-weighted average equals "
            "q^L * Pr[A d=0] with P(d=0)=1/2 and P(d=+-1)=1/4."
        ),
        "dp_rows": [],
        "low_mass_entropy_envelope": [],
        "completed": False,
    }
    write_result(payload)

    rows = [
        # Small exceptional row: visible algebraic relations, but average should
        # not show growing exponent.
        (17, 16, 1, 8, "prefix"),
        # Full section rows at increasing scale and inert-ish small primes.
        (97, 32, 1, 16, "prefix"),
        (193, 64, 2, 32, "prefix"),
        (257, 256, 2, 32, "prefix"),
        (257, 256, 2, 64, "prefix"),
        (257, 256, 2, 128, "prefix"),
        # Same full section but spread ordering: should be identical in content
        # only if no prefix artifact is present.
        (257, 256, 2, 128, "spread"),
        # Prize-shaped ratio N=256L for the L=1 toy.
        (7681, 512, 1, 256, "prefix"),
    ]
    for row in rows:
        if time.time() - started > args.seconds:
            payload["timeout_after_row"] = row
            write_result(payload)
            return
        result = weighted_average_dp(*row)
        payload["dp_rows"].append(result)
        write_result(payload)

    payload["low_mass_entropy_envelope"] = low_mass_entropy_envelope(
        q_bits=256,
        alpha_values=[16, 32, 64, 128, 256],
        L_values=[1, 2, 4, 8, 16],
    )
    payload["completed"] = True
    payload["elapsed_seconds"] = time.time() - started
    write_result(payload)


if __name__ == "__main__":
    main()
