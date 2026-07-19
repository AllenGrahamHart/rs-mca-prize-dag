#!/usr/bin/env python3
"""LOCAL grounding (ramguard tiny): verify E = q^L*A_total/4^N reproduces the
recorded M2 E-1, and cross-check against the banked M1 V_orbits identity.
Small rows only (grid <= q^2 for q<=7937). READ-ONLY on repo."""
from __future__ import annotations
import json
from fractions import Fraction
import numpy as np

REPO = "/home/u2470931/smooth-read-solomin/prize"
M1 = json.load(open(f"{REPO}/critical/nodes/dli_prime_weighted_large_block_support/notes/m1_dli_m1_results.json"))
M2 = json.load(open(f"{REPO}/critical/nodes/dli_prime_weighted_large_block_support/notes/m2_c1prime_level_scaled_results.json"))
N = 32
NPRIME = 2 * N  # 64


def least_primitive_root(q):
    x, d, fac = q - 1, 2, []
    while d * d <= x:
        while x % d == 0:
            fac.append(d); x //= d
        d += 1
    if x > 1:
        fac.append(x)
    fac = sorted(set(fac))
    return next(c for c in range(2, q)
                if all(pow(c, (q - 1) // r, q) != 1 for r in fac))


def zeta_of(q):
    assert (q - 1) % NPRIME == 0
    z = pow(least_primitive_root(q), (q - 1) // NPRIME, q)
    assert pow(z, NPRIME, q) == 1 and pow(z, NPRIME // 2, q) != 1
    return z


def a_total(q, L):
    """Exact integer A_total = # signed odd-null fused states, DP over (q,)^L."""
    z = zeta_of(q)
    dp = np.zeros((q,) * L, dtype=np.int64)
    dp[(0,) * L] = 1
    axes = tuple(range(L))
    for i in range(N):
        vp = tuple(pow(z, ((2 * ell - 1) * i) % NPRIME, q) for ell in range(1, L + 1))
        vm = tuple((q - x) % q for x in vp)
        new = 2 * dp + np.roll(dp, vp, axis=axes) + np.roll(dp, vm, axis=axes)
        assert int(new.max()) < (1 << 62), "int64 headroom guard"
        dp = new
    return int(dp[(0,) * L])


def e_from_atotal(q, L):
    return Fraction(q ** L * a_total(q, L), 4 ** N)


def e_from_vorbits(row):
    q = row["q"]; L = (row["t"] + 1) // 2
    assert not row["suborbit_flags"]
    w = Fraction(1, 1)
    for wt, cnt in row["V_orbits"].items():
        w += Fraction(int(cnt) * 2 * N, 2 ** int(wt))
    return Fraction(q ** L, 2 ** N) * w, L


src = {((r["t"] + 1) // 2, r["q"]): r for r in M1["rows"]}
ok = True
for m2row in M2["rows"]:
    L, q = m2row["level"], m2row["q"]
    rec = Fraction(*m2row["E_minus_1"])
    e_at = e_from_atotal(q, L) - 1
    e_v, _ = e_from_vorbits(src[(L, q)])
    e_v -= 1
    match = (e_at == rec == e_v)
    ok &= match
    print(f"L={L} q={q:>5}: E-1 recorded={float(rec):.6e}  "
          f"A_total_formula={'MATCH' if e_at==rec else 'MISMATCH'}  "
          f"V_orbits={'MATCH' if e_v==rec else 'MISMATCH'}  "
          f"(E-1)/r={float(rec/Fraction(q**L,2**N)):.4f}")

assert ok, "GROUNDING FAILED: E formula disagreement"
print("\nGROUNDING PASS: E = q^L*A_total/4^N == recorded E-1 == V_orbits identity, all 12 rows")
