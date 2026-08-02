#!/usr/bin/env python3
"""Exact checks on the two degenerate frequency lines and the k = p mode.

Run:  tools/ramguard local -- python3 \
        notes/pilots_20260802/f2_carry_reachability/resonance.py

(1) c in F_p (Frobenius-fixed line):  delta_i = 0 for every pair, the
    carry is a constant, and EVERY mode multiplier is M_i(k) = +-2a_i,
    i.e. contraction is identically zero.  The orientation is invisible.
(2) c in the trace-zero line (the other Frobenius eigenline):
    s_i(-1) = p - s_i(+1) exactly, every delta is ODD, and the mode
    k = p carries contraction EXACTLY zero on every pair -- a genuine
    algebraic resonance owner for the carry-DFT route.
(3) generic c: the k = p mode contracts a pair iff f(s+) != f(s-) with
    f(s) = s + [2s > p] mod 2; measured frequency ~ 1/2.
(4) census of DISTINCT delta values mod p, which is the hypothesis of the
    Olson / Dias da Silva-Hamidoune subset-sum bound used for the
    unconditional >= p state floor.
"""

from __future__ import annotations

import json
import math
import os
import random
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from f2model import (  # noqa: E402
    Fp2, deltas, divisors, half_flag, is_prime, pair_reps, residues,
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results")


def f_parity(p: int, s: int) -> int:
    return (s + half_flag(p, s)) % 2


def admissible(p: int) -> list[int]:
    return [n for n in divisors(p * p - 1)
            if n % 2 == 0 and (p - 1) % n != 0]


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    primes = [q for q in range(7, 300) if is_prime(q)]
    fp_rows = 0
    tz_rows = 0
    gen_frac = []
    distinct_rows = []
    for p in primes:
        F = Fp2.make(p)
        rng = random.Random(31337 + p)
        for n in admissible(p)[-2:]:
            mu = F.subgroup(n)
            reps = pair_reps(F, mu)
            if not reps:
                continue
            # (1) Frobenius-fixed line
            for a in (1, 2, rng.randrange(1, p)):
                c = (a % p, 0)
                if c == (0, 0):
                    continue
                for y in reps:
                    sp, sm = residues(F, c, y)
                    assert sp == sm, f"c in F_p must give s+ = s- (p={p})"
                assert all(d == 0 for d in deltas(F, c, reps))
                fp_rows += 1
            # (2) trace-zero line
            for b in (1, 2, rng.randrange(1, p)):
                c = (0, b % p)
                if c == (0, 0):
                    continue
                for y in reps:
                    sp, sm = residues(F, c, y)
                    assert sp != 0 and sm == p - sp, \
                        f"trace-zero conjugate reflection (p={p})"
                    assert (sp - sm) % 2 == 1, "trace-zero delta odd"
                    assert f_parity(p, sp) == f_parity(p, sm), \
                        "k=p mode must not contract on the trace-zero line"
                tz_rows += 1
            # (3) generic c
            for _ in range(3):
                c = (rng.randrange(1, p), rng.randrange(1, p))
                hit = 0
                for y in reps:
                    sp, sm = residues(F, c, y)
                    if f_parity(p, sp) != f_parity(p, sm):
                        hit += 1
                gen_frac.append(hit / len(reps))
            # (4) distinct deltas mod p
            for _ in range(2):
                c = (rng.randrange(1, p), rng.randrange(1, p))
                ds = deltas(F, c, reps)
                dp = {d % p for d in ds}
                assert 0 not in dp, "no zero delta for c outside F_p"
                distinct_rows.append({
                    "p": p, "n": n, "m": len(reps), "distinct_mod_p": len(dp),
                    "sqrt_2p": math.isqrt(2 * p) + 1,
                    "eh_saturates": len(dp) * (len(dp) + 1) // 2 + 1 >= p,
                })
    print(f"F2A2_R1_FIXED_LINE_PASS   c in F_p rows checked = {fp_rows} "
          "(delta == 0 on every pair, every mode dead)")
    print(f"F2A2_R2_TRACE_ZERO_PASS   c trace-zero rows checked = {tz_rows} "
          "(s- = p - s+, delta odd, k=p contraction identically zero)")
    print(f"F2A2_R3_GENERIC_KP        fraction of pairs contracted at k=p: "
          f"min={min(gen_frac):.3f} median={statistics.median(gen_frac):.3f} "
          f"max={max(gen_frac):.3f}  (samples={len(gen_frac)})")
    sat = sum(1 for r in distinct_rows if r["eh_saturates"])
    big = [r for r in distinct_rows if r["m"] >= 2 * r["sqrt_2p"]]
    bigsat = sum(1 for r in big if r["eh_saturates"])
    print(f"F2A2_R4_DISTINCT          rows={len(distinct_rows)}; "
          f"Olson/EH bound already forces Z/p on {sat} of them; "
          f"on rows with m >= 2*sqrt(2p): {bigsat}/{len(big)}")
    ratio = [r["distinct_mod_p"] / r["m"] for r in distinct_rows]
    print(f"                          distinct(delta mod p)/m: "
          f"min={min(ratio):.3f} median={statistics.median(ratio):.3f}")
    with open(os.path.join(OUT, "resonance.json"), "w") as f:
        json.dump({"fixed_line_rows": fp_rows, "trace_zero_rows": tz_rows,
                   "generic_kp_contracted_fraction": {
                       "min": min(gen_frac),
                       "median": statistics.median(gen_frac),
                       "max": max(gen_frac)},
                   "distinct_rows": distinct_rows[:200]}, f, indent=1)
    print("F2A2_RESONANCE_ALL_PASS")


if __name__ == "__main__":
    main()
