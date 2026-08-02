#!/usr/bin/env python3
"""Exact norms Norm(f) = Res(f, x^N + 1) for ternary f, and the symmetry group.

DEFINITIONS (taken verbatim from notes/pilots_20260802/c1_doubling_orbits, NOT guessed)
-------------------------------------------------------------------------------------
2N is a power of two, N = 2N/2.  omega has exact multiplicative order 2N in F_q.
The C1 half-section is 1, omega, ..., omega^(N-1) -- so a relation vector has
exactly N = (2N)/2 entries.

  * ADMISSIBLE PRIME:  q prime with  q = 1 (mod 2N).   [low_weight_router.py:
    `if p % args.twoN == 1`]
  * TERNARY WEIGHT-w RELATION for q: d in {-1,0,1}^N with exactly w nonzero
    entries and  sum_i d_i omega^i = 0 (mod q).  Equivalently f(x) = sum d_i x^i
    (deg < N) has f(omega) = 0 in F_q.
  * ROUTER:  q carries a weight-w relation  <=>  q | Norm(f) for some ternary f
    of weight w, where
        Norm(f) := Res(f(x), x^N + 1) = prod_{j odd, 0<j<2N} f(zeta_{2N}^j)
              = det( multiplication-by-f on Z[x]/(x^N+1) ),
    an exact integer INDEPENDENT of q.

Two facts used throughout (both proved in the report):
  (P) Norm(f) = prod over the N/2 complex-conjugate pairs of |f(zeta^j)|^2 >= 0,
      so the resultant is NON-NEGATIVE; |Norm| = Norm.
  (AM-GM)  sum_{j odd} |f(zeta^j)|^2 = N * ||f||_2^2 = N*w  (negacyclic Parseval),
      so by AM-GM  Norm(f) <= w^(N/2).   <-- a hard a-priori ceiling.

SYMMETRY GROUP (norm-preserving, weight-preserving)
---------------------------------------------------
  U   = { +- x^i : 0 <= i < N }              (order 2N)  "negation + rotation by units"
        Norm(x) = zeta^(1+3+...+(2N-1)) = zeta^(N^2) = 1 and Norm(-f) = (-1)^N Norm(f)
        = Norm(f) for N even, so U preserves Norm EXACTLY.
        Z[x]/(x^N+1) = Z[zeta_2N] is a domain (x^N+1 irreducible for 2N a 2-power),
        so U acts FREELY on nonzero f: every U-orbit has size exactly 2N.
        This is the prior pilot's orbit notion (structure_checks.py / scaling_transfer.py
        divide the weight profile N_w by 2N).
  Gal = { x -> x^u : u in (Z/2N)^* }         (order phi(2N) = N)
        permutes the conjugates, so preserves Norm exactly; it is a signed
        permutation of the monomial basis, so preserves ternariness and weight.
  G   = < U, Gal >  (order 2N * phi(2N) = 2N^2 when 2N is a 2-power).
        Gal does NOT act freely, so G-orbit counts need Burnside.

IMPLEMENTATION
--------------
Fast norm by the field-norm (Falcon/NTRU) descent:
    f(x) = fe(x^2) + x*fo(x^2)  =>  f(x)f(-x) = g(x^2),  g(y) = fe(y)^2 - y*fo(y)^2
    Norm_N(f) = Norm_{N/2}(g),   Norm_1(h) = h_0   (ring Z[y]/(y+1), y = -1).
Vectorised over a batch with numpy int64.  Overflow analysis for N = 16 (all
polynomials ternary): level coefficient bounds 1 -> 16 -> 2048 -> 1.68e7 ->
5.6e14, all far below 2^63.  For N = 32 use the CRT variant (two 31-bit primes).

Cross-checked against a fraction-free Bareiss determinant of the negacyclic
multiplication matrix (the prior pilot's `norm_mod_xN_plus_1`).
"""

from __future__ import annotations

import numpy as np

# --------------------------------------------------------------- reference ---


def norm_bareiss(d: list[int]) -> int:
    """Res(f, x^N+1) via fraction-free Gaussian elimination -- prior pilot's code."""
    n = len(d)
    M = [[0] * n for _ in range(n)]
    for j in range(n):
        for i, c in enumerate(d):
            k = i + j
            M[k % n][j] += c * (-1 if k >= n else 1)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            for r in range(k + 1, n):
                if M[r][k]:
                    M[k], M[r] = M[r], M[k]
                    sign = -sign
                    break
            else:
                return 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
            M[i][k] = 0
        prev = M[k][k]
    return sign * M[n - 1][n - 1]


def norm_descent_py(d) -> int:
    """Exact Python-int field-norm descent (no overflow, any N a power of two)."""
    a = list(d)
    M = len(a)
    while M > 1:
        fe = a[0::2]
        fo = a[1::2]
        h = M // 2
        s_e = [0] * h
        s_o = [0] * h
        for i in range(h):
            for j in range(h):
                k = i + j
                if k < h:
                    s_e[k] += fe[i] * fe[j]
                    s_o[k] += fo[i] * fo[j]
                else:
                    s_e[k - h] -= fe[i] * fe[j]
                    s_o[k - h] -= fo[i] * fo[j]
        # g = s_e - y * s_o  in Z[y]/(y^h + 1);  (y*s_o)_0 = -s_o[h-1]
        g = [0] * h
        g[0] = s_e[0] + s_o[h - 1]
        for k in range(1, h):
            g[k] = s_e[k] - s_o[k - 1]
        a = g
        M = h
    return a[0]


# ------------------------------------------------------------ vectorised -----


def _negacyclic_square(a: np.ndarray) -> np.ndarray:
    """a: (B, M) int64 -> a*a mod (y^M + 1), shape (B, M)."""
    B, M = a.shape
    out = np.zeros((B, M), dtype=np.int64)
    for i in range(M):
        ai = a[:, i]
        for j in range(M):
            k = i + j
            if k < M:
                out[:, k] += ai * a[:, j]
            else:
                out[:, k - M] -= ai * a[:, j]
    return out


def norm_batch_int64(d: np.ndarray) -> np.ndarray:
    """d: (B, N) int64, N a power of two -> (B,) exact Norm(f) as int64.

    Safe (no overflow) for N <= 16 with ternary input; see module docstring.
    """
    a = d.astype(np.int64)
    M = a.shape[1]
    while M > 1:
        h = M // 2
        se = _negacyclic_square(np.ascontiguousarray(a[:, 0::2]))
        so = _negacyclic_square(np.ascontiguousarray(a[:, 1::2]))
        g = np.empty((a.shape[0], h), dtype=np.int64)
        g[:, 0] = se[:, 0] + so[:, h - 1]
        if h > 1:
            g[:, 1:] = se[:, 1:] - so[:, : h - 1]
        a = g
        M = h
    return a[:, 0]


def _negacyclic_square_mod(a: np.ndarray, p: int) -> np.ndarray:
    B, M = a.shape
    out = np.zeros((B, M), dtype=np.int64)
    for i in range(M):
        ai = a[:, i]
        for j in range(M):
            k = i + j
            t = (ai * a[:, j]) % p
            if k < M:
                out[:, k] = (out[:, k] + t) % p
            else:
                out[:, k - M] = (out[:, k - M] - t) % p
    return out


def norm_batch_mod(d: np.ndarray, p: int) -> np.ndarray:
    a = d.astype(np.int64) % p
    M = a.shape[1]
    while M > 1:
        h = M // 2
        se = _negacyclic_square_mod(np.ascontiguousarray(a[:, 0::2]), p)
        so = _negacyclic_square_mod(np.ascontiguousarray(a[:, 1::2]), p)
        g = np.empty((a.shape[0], h), dtype=np.int64)
        g[:, 0] = (se[:, 0] + so[:, h - 1]) % p
        if h > 1:
            g[:, 1:] = (se[:, 1:] - so[:, : h - 1]) % p
        a = g
        M = h
    return a[:, 0]


P1 = 2147483647   # 2^31 - 1, prime
P2 = 2147483629   # prime
_INV = pow(P1, -1, P2)


def norm_batch_crt(d: np.ndarray) -> np.ndarray:
    """Exact Norm as int64 via 2-prime CRT.  Valid while 0 <= Norm < P1*P2 = 4.61e18.

    Norm(f) >= 0 always (fact (P)), and Norm <= w^(N/2) (AM-GM), so this is exact
    for every case we use it on (N = 32, w <= 8: 8^16 = 2.8e14).
    """
    a1 = norm_batch_mod(d, P1)
    a2 = norm_batch_mod(d, P2)
    t = ((a2 - a1) % P2) * _INV % P2
    return a1 + P1 * t


# --- fast variant: three ~2^20 primes with delayed reduction inside the square --

Q1, Q2, Q3 = 1048573, 1048571, 1048559      # primes just below 2^20
_QINV12 = pow(Q1, -1, Q2)
_QINV123 = pow(Q1 * Q2, -1, Q3)
_Q12 = Q1 * Q2                               # ~1.1e12
# Q1*Q2*Q3 = 1.1525e18 < 2^63; a coefficient sum is < 32 * (2^20)^2 = 2^45.


def _negsq_mod_fast(a: np.ndarray, p: int) -> np.ndarray:
    B, M = a.shape
    acc = np.zeros((B, M), dtype=np.int64)
    for i in range(M):
        ai = a[:, i]
        for j in range(M):
            k = i + j
            if k < M:
                acc[:, k] += ai * a[:, j]
            else:
                acc[:, k - M] -= ai * a[:, j]
    return acc % p


def norm_batch_mod_fast(d: np.ndarray, p: int) -> np.ndarray:
    a = d.astype(np.int64) % p
    M = a.shape[1]
    while M > 1:
        h = M // 2
        se = _negsq_mod_fast(np.ascontiguousarray(a[:, 0::2]), p)
        so = _negsq_mod_fast(np.ascontiguousarray(a[:, 1::2]), p)
        g = np.empty((a.shape[0], h), dtype=np.int64)
        g[:, 0] = (se[:, 0] + so[:, h - 1]) % p
        if h > 1:
            g[:, 1:] = (se[:, 1:] - so[:, : h - 1]) % p
        a = g
        M = h
    return a[:, 0]


def norm_batch_crt3(d: np.ndarray) -> np.ndarray:
    """Exact Norm as int64 via 3-prime CRT (Garner).  Valid for 0 <= Norm < 1.15e18."""
    a1 = norm_batch_mod_fast(d, Q1)
    a2 = norm_batch_mod_fast(d, Q2)
    a3 = norm_batch_mod_fast(d, Q3)
    t1 = ((a2 - a1) % Q2) * _QINV12 % Q2
    x = a1 + Q1 * t1                                   # < 1.1e12
    t2 = ((a3 - x) % Q3) * _QINV123 % Q3
    return x + _Q12 * t2


# ------------------------------------------------------- symmetry group ------


def signed_perm_neg(N: int):
    """f -> -f  as (perm, sign) with  d'_{perm[i]} = sign[i] * d_i."""
    return list(range(N)), [-1] * N


def signed_perm_rot(N: int):
    """f -> x*f  in Z[x]/(x^N+1)."""
    perm = [(i + 1) % N for i in range(N)]
    sign = [1] * N
    sign[N - 1] = -1          # x * x^(N-1) = x^N = -1
    return perm, sign


def signed_perm_gal(N: int, u: int):
    """f -> f(x^u), u odd, in Z[x]/(x^N+1)."""
    twoN = 2 * N
    perm = [0] * N
    sign = [1] * N
    for i in range(N):
        e = (u * i) % twoN
        if e >= N:
            perm[i] = e - N
            sign[i] = -1
        else:
            perm[i] = e
            sign[i] = 1
    return perm, sign


def compose(g2, g1):
    """apply g1 then g2."""
    p1, s1 = g1
    p2, s2 = g2
    N = len(p1)
    p = [0] * N
    s = [0] * N
    for i in range(N):
        j = p1[i]
        p[i] = p2[j]
        s[i] = s1[i] * s2[j]
    return p, s


def _key(g):
    return (tuple(g[0]), tuple(g[1]))


def close_group(gens, N):
    ident = (list(range(N)), [1] * N)
    seen = {_key(ident): ident}
    frontier = [ident]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                c = compose(h, g)
                k = _key(c)
                if k not in seen:
                    seen[k] = c
                    nxt.append(c)
        frontier = nxt
    return list(seen.values())


def group_U(N):
    return close_group([signed_perm_neg(N), signed_perm_rot(N)], N)


def group_G(N):
    gens = [signed_perm_neg(N), signed_perm_rot(N)]
    twoN = 2 * N
    for u in range(3, twoN, 2):
        gens.append(signed_perm_gal(N, u))
    return close_group(gens, N)


def fix_polynomial(g, N):
    """Weight generating polynomial of Fix(g) on ternary vectors: list c[w].

    A vector d is fixed by the signed permutation (perm, sign) iff on every cycle
    of perm the entries propagate consistently; a cycle whose sign product is -1
    forces all its entries to 0, a cycle of length L with sign product +1
    contributes (1 + 2 z^L).
    """
    perm, sign = g
    seen = [False] * N
    poly = [0] * (N + 1)
    poly[0] = 1
    for start in range(N):
        if seen[start]:
            continue
        cyc = []
        i = start
        sp = 1
        while not seen[i]:
            seen[i] = True
            cyc.append(i)
            sp *= sign[i]
            i = perm[i]
        L = len(cyc)
        if sp == 1:
            new = [0] * (N + 1)
            for w in range(N + 1):
                if poly[w]:
                    new[w] += poly[w]
                    if w + L <= N:
                        new[w + L] += 2 * poly[w]
            poly = new
        # sp == -1: factor is 1, nothing to do
    return poly


def burnside_orbit_counts(grp, N):
    """Exact number of orbits of `grp` on ternary vectors of each weight w."""
    tot = [0] * (N + 1)
    for g in grp:
        f = fix_polynomial(g, N)
        for w in range(N + 1):
            tot[w] += f[w]
    n = len(grp)
    assert all(t % n == 0 for t in tot), "Burnside sum not divisible by |G|"
    return [t // n for t in tot]


if __name__ == "__main__":
    import json
    import random
    from itertools import product as iproduct

    report = {"selftest": []}

    # 1. descent vs Bareiss on every ternary f for N = 4 and N = 8, and random N = 16
    for N in (4, 8):
        bad = 0
        mx = 0
        for d in iproduct((-1, 0, 1), repeat=N):
            a = norm_bareiss(list(d))
            b = norm_descent_py(list(d))
            if a != b:
                bad += 1
            mx = max(mx, abs(a))
        report["selftest"].append(
            {"N": N, "exhaustive": True, "mismatches": bad, "max_abs_norm": str(mx)})
        assert bad == 0

    rng = random.Random(20260802)
    # N = 32 is only ever used at low weight (w <= 8), where AM-GM gives
    # Norm <= 8^16 = 2.8e14 < P1*P2, so the CRT recovery is exact; sample there.
    for N, wcap in ((16, 16), (32, 8)):
        bad = 0
        rows = []
        for _ in range(200):
            d = [0] * N
            w = rng.randint(1, wcap)
            for p in rng.sample(range(N), w):
                d[p] = rng.choice((-1, 1))
            rows.append(d)
            if norm_bareiss(d) != norm_descent_py(d):
                bad += 1
        arr = np.array(rows, dtype=np.int64)
        v_crt = norm_batch_crt(arr)
        ok_crt = all(int(v_crt[i]) == norm_descent_py(rows[i]) for i in range(len(rows)))
        entry = {"N": N, "random_samples": len(rows), "bareiss_vs_descent_mismatches": bad,
                 "crt_batch_matches": bool(ok_crt)}
        if N == 16:
            v64 = norm_batch_int64(arr)
            entry["int64_batch_matches"] = bool(
                all(int(v64[i]) == norm_descent_py(rows[i]) for i in range(len(rows))))
        report["selftest"].append(entry)
        assert bad == 0 and ok_crt

    # 2. non-negativity of the resultant (fact (P)) on all of N = 8
    negs = sum(1 for d in iproduct((-1, 0, 1), repeat=8) if norm_bareiss(list(d)) < 0)
    report["resultant_negative_count_N8"] = negs

    # 3. reproduce the prior pilot's q = 70529 weight-7 certificate
    w7 = [1, -1, 1, -1, 0, 1, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0]
    report["prior_pilot_70529_certificate"] = {
        "f": w7, "norm_bareiss": str(norm_bareiss(w7)),
        "norm_descent": str(norm_descent_py(w7)),
        "norm_batch_int64": str(int(norm_batch_int64(np.array([w7], dtype=np.int64))[0])),
    }

    # 4. group orders
    report["group_orders"] = {
        str(N): {"|U|": len(group_U(N)), "|G|": len(group_G(N))} for N in (4, 8, 16, 32)}

    print(json.dumps(report, indent=1))
