#!/usr/bin/env python3
"""Verifier for dyadic_profile_evaluation.
Exact divisor-count of the quotient profile Q_M = C(n/M-1, floor(A/M)) and the
dihedral companion D_M on 2-power domains, at the four rates. Reproduces the
banked QA.22 numbers exactly, and checks first-scale dominance + n-uniformity.
Stdlib only (math.comb, exact big ints); runs <1s."""
from math import comb, log2

def pow2_divisors(n):
    ds, M = [], 1
    while M <= n:
        if n % M == 0: ds.append(M)
        M *= 2
    return ds

def profile(n, k, A):
    t = A - k
    terms = []
    for M in pow2_divisors(n):
        if M > t:
            N, h = n // M, A // M
            if 0 <= h <= N - 1:
                terms.append((M, N, h, comb(N - 1, h)))
    return terms  # ordered by increasing M = decreasing N

def D_M(N, h, b):
    pairs = (N - 2) // 2
    fixed = 2 if b == 0 else 1
    tot = 0
    for f in range(fixed + 1):
        rem = h - f
        if rem >= 0 and rem % 2 == 0:
            p = rem // 2
            if 0 <= p <= pairs:
                tot += comb(fixed, f) * comb(pairs, p)
    return tot

ROWS = [
    ("pinned 1/2", 512, 256, 507),
    ("RowC 1/4", 2**10, 2**8, 261),
    ("RowC 1/8", 2**10, 2**7, 133),
    ("RowC 1/16", 2**10, 2**6, 67),
    ("prize 1/4", 2**41, 2**39, 558345748481),
    ("prize 1/8", 2**41, 2**38, 283467841537),
    ("prize 1/16", 2**41, 2**37, 141733920769),
]
# banked QA.22 targets (deciding-scale log2 Q_M, log2 D_M) by rate
QA22_Q = {"1/4": 99.8063, "1/8": 66.1465, "1/16": 82.9664}
QA22_D = {"1/4": 48.3804, "1/8": 31.8508, "1/16": 40.2857}

def rate_of(name): return name.split()[-1]

if __name__ == "__main__":
    prof = {}
    ok = True
    print(f"{'row':12s} {'t':>13} {'M*':>13} {'N*':>4} {'h':>3} {'log2Q_M*':>10} {'log2Qsum':>9} {'log2D_M*':>9}")
    for name, n, k, A in ROWS:
        ts = profile(n, k, A)
        if not ts or ts[0][3] <= 1:
            print(f"{name:12s} {A-k:>13} {'--':>13}  (trivial profile; parity-killed)  ")
            prof[name] = ("trivial",)
            continue
        M, N, h, Qm = ts[0]
        Qsum = sum(x[3] for x in ts)
        b = A - h * M
        Dm = D_M(N, h, b)
        lQ, lS, lD = log2(Qm), log2(Qsum), log2(Dm) if Dm > 0 else float("nan")
        print(f"{name:12s} {A-k:>13} {M:>13} {N:>4} {h:>3} {lQ:>10.4f} {lS:>9.4f} {lD:>9.4f}")
        prof[name] = (N, h, round(lQ, 4), round(lD, 4))
        r = rate_of(name)
        # (a) match QA.22
        if r in QA22_Q:
            if abs(lQ - QA22_Q[r]) > 5e-4: ok = False; print("   FAIL Q vs QA22")
            if abs(lD - QA22_D[r]) > 5e-4: ok = False; print("   FAIL D vs QA22")
        # (b) first-scale dominance: sum == top term to 6 dp
        if abs(lS - lQ) > 1e-6: ok = False; print("   FAIL first-scale dominance")

    # (c) n-uniformity: RowC vs prize identical (N, h, log2Q, log2D)
    for r in ["1/4", "1/8", "1/16"]:
        a, b = prof[f"RowC {r}"], prof[f"prize {r}"]
        if a != b: ok = False; print(f"   FAIL n-uniformity at rate {r}: {a} != {b}")
    print("n-uniformity RowC(n=2^10) == prize(n=2^41):",
          all(prof[f"RowC {r}"] == prof[f"prize {r}"] for r in ["1/4", "1/8", "1/16"]))
    # (d) rate 1/2 trivial
    print("rate 1/2 profile trivial:", prof["pinned 1/2"] == ("trivial",))
    assert ok and prof["pinned 1/2"] == ("trivial",)
    print("ALL PASS")
