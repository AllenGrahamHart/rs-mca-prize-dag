#!/usr/bin/env python3
"""c36r independent replay: demo rows, all cluster identities, exact compilers.

Written from the statements alone (not from Codex's verify.py code).
Exact integer/Fraction arithmetic throughout.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction

ROWS = ((97, 32), (4289, 64), (7937, 64))
EXPECTED = {  # (N_3to1, identity fiber I, overlap max on quotient support)
    (97, 32): (9692, 12, 14),
    (4289, 64): (3639, 0, 6),
    (7937, 64): (5765, 12, 14),
}


def factorize(m: int) -> list[int]:
    out, d = [], 2
    while d * d <= m:
        if m % d == 0:
            out.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out


def subgroup(p: int, n: int) -> list[int]:
    assert (p - 1) % n == 0
    fac = factorize(p - 1)
    g = next(c for c in range(2, p)
             if all(pow(c, (p - 1) // q, p) != 1 for q in fac))
    h = pow(g, (p - 1) // n, p)
    # order check
    for q in factorize(n):
        assert pow(h, n // q, p) != 1
    H = []
    x = 1
    for _ in range(n):
        H.append(x)
        x = x * h % p
    assert x == 1 and len(set(H)) == n
    return H


def replay_row(p: int, n: int) -> None:
    H = subgroup(p, n)
    Hset = set(H)
    A = [(1 - x) % p for x in H if x != 1]
    assert len(A) == n - 1 and 0 not in A

    P: Counter[int] = Counter()
    R: Counter[int] = Counter()
    D: Counter[int] = Counter()
    for a in A:
        D[a * a % p] += 1
        inv_a = pow(a, p - 2, p)
        for b in A:
            P[a * b % p] += 1
            R[b * inv_a % p] += 1  # d/c = t with c=a, d=b

    # --- base identities (M1/M2/M4 shape) ---
    N = sum(cnt * R[t] for t, cnt in P.items())
    N_direct = sum(1 for a1 in A for a2 in A for a3 in A
                   if (a1 * a2 * a3) % p in set(A)) if n <= 64 else None
    if N_direct is not None:
        assert N == N_direct, (p, n, N, N_direct)
    I_oneshift = sum(1 for u in H if (1 - u) % p in Hset)  # #{u,v in H: u+v=1}
    assert P[1] == I_oneshift, (p, n, P[1], I_oneshift)
    assert R[1] == n - 1
    assert sum(R.values()) - R[1] == (n - 1) * (n - 2)
    assert sum(P.values()) == (n - 1) ** 2
    overlap_max = max((P[t] for t in R if t != 1 and R[t] > 0), default=0)
    exp = EXPECTED[(p, n)]
    assert (N, P[1], overlap_max) == exp, (p, n, N, P[1], overlap_max, exp)

    # --- weighted excess, factorial and non-swap moments ---
    X35 = sum(max(P[t] - 35, 0) * R[t] for t in R if t != 1)
    M21 = sum(P[t] * (P[t] - 1) * R[t] for t in R if t != 1)
    Sns = sum((P[t] * (P[t] - 2) + D[t]) * R[t] for t in R if t != 1)
    Sswap = sum((P[t] - D[t]) * R[t] for t in R if t != 1)
    assert M21 == Sns + Sswap  # swap decomposition
    assert 138 * X35 <= M21
    assert 136 * X35 <= Sns
    # direct S_ns via ordered non-equal non-swap pairs of product reps
    reps: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for a in A:
        for b in A:
            reps[a * b % p].append((a, b))
    Sns_direct = 0
    for t, lst in reps.items():
        if t == 1:
            continue
        cnt = sum(1 for r1 in lst for r2 in lst
                  if r2 != r1 and r2 != (r1[1], r1[0]))
        Sns_direct += cnt * R[t]
    assert Sns_direct == Sns, (p, n, Sns_direct, Sns)
    # multiplier (lambda,a,b,c) parameterization of S_ns
    Aset = set(A)
    Sns_mult = 0
    for lam in range(2, p):
        lam_inv = pow(lam, p - 2, p)
        for a in A:
            la = lam * a % p
            if la not in Aset:
                continue
            for b in A:
                if a * b % p == 1 or b * pow(a, p - 2, p) % p == lam:
                    continue
                if b * lam_inv % p not in Aset:
                    continue
                ab = a * b % p
                for c in A:
                    if ab * c % p in Aset:
                        Sns_mult += 1
    assert Sns_mult == Sns, (p, n, Sns_mult, Sns)

    # --- quotient block identity ---
    # dlog table
    fac = factorize(p - 1)
    g = next(c for c in range(2, p)
             if all(pow(c, (p - 1) // q, p) != 1 for q in fac))
    dlog = {}
    x = 1
    for e in range(p - 1):
        dlog[x] = e
        x = x * g % p
    idx = (p - 1) // n
    blocks: dict[tuple[int, int], list[int]] = defaultdict(list)
    for t in range(2, p):
        u = pow((1 - t) % p, p - 2, p)
        v = (-t * u) % p
        assert (u + v) % p == 1
        blocks[(dlog[u] % idx, dlog[v] % idx)].append(t)
    tot = 0
    for members in blocks.values():
        m = len(members)
        for t in members:
            assert R[t] == m - 1, (p, n, t, R[t], m)
        tot += m * (m - 1)
    assert tot == (n - 1) * (n - 2)

    # --- PGL2 pair identities ---
    for t in range(2, p):
        I_inv = sum(1 for x_ in H if x_ != 1
                    and (1 + t * pow(x_ - 1, p - 2, p)) % p in Hset)
        I_aff = sum(1 for z in H if (1 + t * (z - 1)) % p in Hset)
        assert P[t] == I_inv, (p, n, t, P[t], I_inv)
        assert R[t] == I_aff - 1, (p, n, t, R[t], I_aff)

    print(f"row ({p},{n}): N={N} I={P[1]} overlap_max={overlap_max} "
          f"X35={X35} M21={M21} Sns={Sns} Sswap={Sswap} blocks=OK pgl2=OK")


def icbrt(m: int) -> int:
    r = round(m ** (1 / 3))
    while r ** 3 > m:
        r -= 1
    while (r + 1) ** 3 <= m:
        r += 1
    return r


def compilers() -> None:
    # Exact rational upper bound rhat >= n^(1/3), rhat^3 >= n, error < 2^-30
    for s in range(13, 42):
        n = 1 << s
        # rhat = ceil(n^(1/3) * 2^30) / 2^30 via integer cube search
        scale = 1 << 30
        lo = icbrt(n * scale**3)
        rhat = Fraction(lo + 1, scale)
        assert rhat**3 > n
        lhs_rad = 4 * rhat**2 * (n - 1) + 16 * n * rhat  # >= 4n^(2/3)(n-1)+16n^(4/3)
        G = Fraction(36 * n**2) - Fraction(n, 2) - 35 * (n - 1) * (n - 2) \
            - Fraction(n**2, 2)
        assert lhs_rad < G, (s, "weighted compiler FULL exact")
        # pointwise (M35) compiler: without the n^2/2 allowance
        G_pt = G + Fraction(n**2, 2)
        assert lhs_rad < G_pt, (s, "pointwise compiler")
        # mutations
        G_cap36 = Fraction(36 * n**2) - Fraction(n, 2) - 36 * (n - 1) * (n - 2) \
            - Fraction(n**2, 2)
        assert not (lhs_rad < G_cap36), (s, "cap-36 mutation must fail")
        # Codex's mutation semantics: with the (6/25)n^2 radical BUDGET on the
        # left, a 4n^2/5 excess allowance must overflow the target.
        budget_lhs = 35 * (n - 1) * (n - 2) + Fraction(6 * n**2, 25) \
            + Fraction(4 * n**2, 5)
        assert budget_lhs >= Fraction(36 * n**2) - Fraction(n, 2), \
            (s, "4n^2/5 budget-mutation must fail")
        # True-statement room with EXACT radicals (observation, not control):
        true_room = Fraction(36 * n**2) - Fraction(n, 2) \
            - 35 * (n - 1) * (n - 2) - lhs_rad
        if s == 13:
            print(f"  true allowance at s=13: {float(true_room/n**2):.4f} n^2 "
                  "(n^2/2 claimed; 4n^2/5 mutation only fails under the "
                  "(6/25)n^2 budget, not against exact radicals for s>=14)")
        # their radical-budget route, independently: cube comparisons
        assert 125 * 64 * n**5 <= n**6 and 15625 * 4096 * n**4 <= n**6, s

    # FM69 compiler: 138*(m-35)_+ <= m(m-1), sharp; 139 fails
    for m in range(0, 2000):
        assert 138 * max(m - 35, 0) <= m * (m - 1)
    assert any(139 * max(m - 35, 0) > m * (m - 1) for m in (69, 70))
    # symbolic: m>=36 -> m(m-1)-138(m-35) = (m-69)(m-70)
    for m in range(36, 500):
        assert m * (m - 1) - 138 * (m - 35) == (m - 69) * (m - 70)
    assert Fraction(69, 138) == Fraction(1, 2)

    # non-swap compiler: 136*(m-35)_+ <= m(m-2)+d for feasible (m,d); 137 fails
    for m in range(0, 2000):
        for d in range(0, 3):
            if d <= m and d % 2 == m % 2:
                assert 136 * max(m - 35, 0) <= m * (m - 2) + d, (m, d)
    assert 137 * (68 - 35) > 68 * 66  # mutation
    for m in range(36, 500):
        assert m * (m - 2) - 136 * (m - 35) == (m - 68) * (m - 70)
    assert Fraction(68, 136) == Fraction(1, 2)

    # paired compiler: I_inv + 2*I_aff <= 39 and I_aff >= 2 -> I_inv <= 35
    for I_aff in range(2, 40):
        for I_inv in range(0, 40):
            if I_inv + 2 * I_aff <= 39:
                assert I_inv <= 35
    # threshold-40 mutation admits I_inv=36
    assert 36 + 2 * 2 <= 40
    print("compilers: weighted(full-exact)+pointwise+FM69+nonswap+paired OK; "
          "mutations cap36/4n2:5/139/137/threshold40 all detected")


def main() -> None:
    compilers()
    for p, n in ROWS:
        replay_row(p, n)
    print("C36R_DEMO_REPLAY_PASS")


if __name__ == "__main__":
    main()
