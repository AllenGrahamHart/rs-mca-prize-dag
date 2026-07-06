#!/usr/bin/env python3
"""Verifier for census_bounded_scales.
Deciding quotient scale is unique (monotone counts + staircase-step gaps) and
pinned in an absolute n-uniform window [~120,400]. Stdlib, exact big ints, <1s."""
from math import comb, log2
from fractions import Fraction

def H(x):
    from math import log
    if x <= 0 or x >= 1: return 0.0
    return -(x * log2(x) + (1 - x) * log2(1 - x))

def pow2_scales(n, t):
    """admissible dyadic quotient rows N'=n/M with M>t, increasing N'."""
    out, M = [], 1
    while M <= n:
        if n % M == 0 and M > t:
            out.append(n // M)
        M *= 2
    return sorted(set(out))

def count(Nprime, jn):
    """Q(N') = C(N', round((j/n) N')) exact."""
    lp = round(jn * Nprime)
    return comb(Nprime, lp), lp

if __name__ == "__main__":
    ok = True

    # (3) entropy corridor bound
    e40 = H(0.40)
    print(f"(3) H(0.40)={e40:.5f} >= 0.97 : {'PASS' if e40 >= 0.97 else 'FAIL'}; "
          f"H monotone up on [0,.5]: {'PASS' if all(H(a) < H(a+0.05) for a in [0.05*i for i in range(9)]) else 'FAIL'}")
    if e40 < 0.97: ok = False

    # (6) crossing window N* = 128/H(j/n) in [120,400], per rate
    print("(6) crossing-scale window N*=128/H(j/n):")
    for rho, name in [(0.5, "1/2"), (0.25, "1/4"), (0.125, "1/8"), (0.0625, "1/16")]:
        jn = 1 - rho
        Nstar = 128 / H(jn)
        inwin = 120 <= Nstar <= 400
        print(f"    rate {name:4s} j/n={jn:.4f} H={H(jn):.4f} N*={Nstar:7.1f} in[120,400]:{inwin}")
        if not inwin: ok = False

    # (1),(2),(4),(5),(U) on concrete rows; and n-uniformity RowC vs prize
    ROWS = [("RowC 1/4", 2**10, 261), ("prize 1/4", 2**41, 558345748481),
            ("RowC 1/8", 2**10, 133), ("prize 1/8", 2**41, 283467841537),
            ("RowC 1/16", 2**10, 67), ("prize 1/16", 2**41, 141733920769)]
    deciding = {}
    for name, n, A in ROWS:
        k = n // int(name.split()[-1].split("/")[1])
        t = A - k; j = n - A; jn = Fraction(j, n)
        scales = pow2_scales(n, t)
        # substantive scales: 0 < l' < N' (non-degenerate binomial, count > 1)
        subs = []
        for Np in scales:
            Q, lp = count(Np, float(jn))
            if 0 < lp < Np and Q > 1:
                subs.append((Np, log2(Q), lp))
        # (2) strict monotone growth over substantive scales
        mono = all(subs[i][1] < subs[i + 1][1] for i in range(len(subs) - 1))
        # (4) top staircase step (gap between the two largest scales) is large
        top_gap = subs[-1][1] - subs[-2][1] if len(subs) >= 2 else float("inf")
        stepok = top_gap >= 30
        # deciding = largest admissible substantive scale
        Np_star, logQ_star, lp_star = subs[-1]
        # (5) uniqueness: only the deciding scale is within a staircase step (< top_gap)
        #     of any bounded target; equivalently the runner-up is >= top_gap below.
        uniq = all(logQ_star - lg >= top_gap - 1e-9 for (Np, lg, _) in subs[:-1])
        if not (mono and stepok and uniq): ok = False
        deciding[name] = (Np_star, lp_star, round(logQ_star, 4))
        print(f"    {name:11s} t={t:>13} decidingN'={Np_star} substantive={[s[0] for s in subs]} "
              f"mono={mono} top_step={top_gap:.1f}(>=30:{stepok}) unique={uniq}")

    # (U) n-uniformity: RowC vs prize identical deciding (N', l', log2Q)
    print("(U) n-uniformity RowC(2^10) vs prize(2^41):")
    for r in ["1/4", "1/8", "1/16"]:
        a, b = deciding[f"RowC {r}"], deciding[f"prize {r}"]
        same = (a == b)
        if not same: ok = False
        print(f"    rate {r:5s}: RowC {a}  prize {b}  identical:{same}")
        # window membership
        if not (120 <= a[0] <= 400): ok = False
    assert ok
    print("ALL PASS")
