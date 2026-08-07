#!/usr/bin/env python3
"""MYSTERY-5 diagnosis, round 21: toy measurement of the generator_economy early cap.

Ring: Z[zeta_N] = Z[x]/(x^n + 1), n = N/2, N a 2-power (CATCH-19C: 2-power grids).
Centers: e_1(B) = sum_{i in B} x^i for B a half-size (|B| = N/2) subset of mu_N.
         In Z[x]/(x^n+1) a center is the vector v_j = [j in B] - [j+n in B].

Registered functionals (PREREG R1, R2, R4):
  COLLAPSE(N)  = |F| / #distinct e_1 over the Pro-Brief-F antipodal family
  POW2(d)      = 1 iff |Norm(d)| is a power of 2   (the certifiability test)
  MAXPOW2(N)   = max size of a center set with ALL pairwise differences POW2
  SLOPE/CURV   = discrete first/second differences of the orbit-union size
"""
import itertools
import math
import sys

import numpy as np


# ---------------------------------------------------------------- exact norm
def bareiss_det(mat):
    """Exact integer determinant (fraction-free Gaussian elimination)."""
    m = [row[:] for row in mat]
    n = len(m)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if m[k][k] == 0:
            piv = None
            for r in range(k + 1, n):
                if m[r][k] != 0:
                    piv = r
                    break
            if piv is None:
                return 0
            m[k], m[piv] = m[piv], m[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                m[i][j] = (m[i][j] * m[k][k] - m[i][k] * m[k][j]) // prev
        prev = m[k][k]
    return sign * m[n - 1][n - 1]


def exact_norm(vec, n):
    """Norm_{Q(zeta_N)/Q} of sum vec[j] x^j in Z[x]/(x^n+1): det of mult matrix."""
    mat = [[0] * n for _ in range(n)]
    for j in range(n):          # column j = x^j * vec
        for i in range(n):
            s = i + j
            if s < n:
                mat[s][j] += vec[i]
            else:
                mat[s - n][j] -= vec[i]
    return bareiss_det(mat)


def is_pow2(x):
    x = abs(int(x))
    return x != 0 and (x & (x - 1)) == 0


# ------------------------------------------------------- float POW2 screening
def vandermonde(n):
    """Rows = primitive N-th roots (odd powers), cols = x^j."""
    N = 2 * n
    ks = np.arange(1, N, 2)
    js = np.arange(n)
    ang = 2.0 * np.pi * np.outer(ks, js) / N
    return np.exp(1j * ang)


def pow2_mask(D, n, V):
    """D: (M,n) int array. Returns boolean mask of |Norm| == power of 2."""
    vals = D.astype(np.complex128) @ V.T          # (M, n)
    absv = np.abs(vals)
    zero = (absv < 1e-9).any(axis=1)
    with np.errstate(divide="ignore"):
        logn = np.log2(np.where(absv < 1e-12, 1.0, absv)).sum(axis=1)
    cand = (~zero) & (np.abs(logn - np.round(logn)) < 1e-6)
    out = np.zeros(len(D), dtype=bool)
    idx = np.flatnonzero(cand)
    for i in idx:                                  # exact verification
        out[i] = is_pow2(exact_norm([int(t) for t in D[i]], n))
    return out


# ------------------------------------------------------------------ centers
def all_centers(n):
    """All distinct e_1 of half-size subsets: v in {-1,0,1}^n with #zeros even."""
    out = []
    for v in itertools.product((-1, 0, 1), repeat=n):
        if (n - sum(1 for t in v if t != 0)) % 2 == 0:
            out.append(v)
    return out


def sample_centers(n, k, rng):
    """Uniform-ish sample of valid centers (even number of zero coordinates)."""
    out = set()
    while len(out) < k:
        v = rng.integers(-1, 2, size=n)
        if (n - int(np.count_nonzero(v))) % 2:
            j = int(rng.integers(0, n))
            v[j] = 0 if v[j] != 0 else 1
        if (n - int(np.count_nonzero(v))) % 2 == 0:
            out.add(tuple(int(t) for t in v))
    return list(out)


# ------------------------------------------- R1: Pro-Brief-F family collapse
def r1_collapse(N):
    n = N // 2
    pairs = [(j, j + n) for j in range(n)]        # antipodal pairs of mu_N
    total = 0
    centers = set()
    for s in range(N):
        s1 = (s + 1) % N
        avail = [p for p in pairs if s % n != p[0] % n and s1 % n != p[0] % n]
        assert len(avail) == n - 2, (len(avail), n)
        for T in itertools.combinations(avail, n // 2 - 1):
            vec = [0] * n
            for e in (s, s1):
                if e < n:
                    vec[e] += 1
                else:
                    vec[e - n] -= 1
            for (a, b) in T:                       # x^a + x^{a+n} = 0
                pass
            total += 1
            centers.add(tuple(vec))
    return total, len(centers), math.comb(n - 2, n // 2 - 1)


# ------------------------------------------------ R4: MAXPOW2 via max clique
def max_clique(adj, order):
    """Exact max clique, greedy-coloured branch and bound."""
    best = [0]
    best_set = [[]]

    def expand(R, P):
        if not P:
            if len(R) > best[0]:
                best[0] = len(R)
                best_set[0] = list(R)
            return
        if len(R) + len(P) <= best[0]:
            return
        # greedy colouring bound
        colours = {}
        classes = []
        for v in sorted(P, key=lambda t: -len(adj[t] & P)):
            placed = False
            for ci, cl in enumerate(classes):
                if not (adj[v] & cl):
                    cl.add(v)
                    colours[v] = ci + 1
                    placed = True
                    break
            if not placed:
                classes.append({v})
                colours[v] = len(classes)
        cand = sorted(P, key=lambda t: colours[t])
        for i in range(len(cand) - 1, -1, -1):
            v = cand[i]
            if len(R) + colours[v] <= best[0]:
                return
            expand(R + [v], P & adj[v])
            P = P - {v}

    expand([], set(order))
    return best[0], best_set[0]


def r4_maxpow2(N, verbose=True):
    n = N // 2
    V = vandermonde(n)
    cent = all_centers(n)
    cidx = {c: i for i, c in enumerate(cent)}
    # candidate difference vectors live in {-2..2}^n
    diffs = np.array(list(itertools.product((-2, -1, 0, 1, 2), repeat=n)),
                     dtype=np.int64)
    mask = pow2_mask(diffs, n, V)
    P = [tuple(int(t) for t in d) for d in diffs[mask]]
    if verbose:
        print("  |centers|=%d  |box|=%d  |POW2 connection set P|=%d"
              % (len(cent), len(diffs), len(P)))
    adj = [set() for _ in cent]
    for i, c in enumerate(cent):
        for p in P:
            q = tuple(c[j] + p[j] for j in range(n))
            j = cidx.get(q)
            if j is not None and j != i:
                adj[i].add(j)
    deg = [len(a) for a in adj]
    if verbose:
        print("  POW2 graph: mean degree %.2f  max degree %d"
              % (sum(deg) / len(deg), max(deg)))
    size, clique = max_clique(adj, range(len(cent)))
    return len(cent), len(P), size, [cent[i] for i in clique]


# ------------------------------------- R2: orbit-union growth (E12 replay)
def r2_orbit_growth(N, tmax=8, seed=11):
    n = N // 2
    rng = np.random.default_rng(seed)
    if n <= 8:
        cent = all_centers(n)
        picks = [cent[i] for i in rng.choice(len(cent), size=tmax, replace=False)]
    else:
        picks = sample_centers(n, tmax, rng)

    def orbit(c):
        """{ +/- x^r * c : r } -- the unit orbit inside the ring."""
        o = set()
        cur = list(c)
        for _ in range(N):
            o.add(tuple(cur))
            o.add(tuple(-t for t in cur))
            cur = [-cur[n - 1]] + cur[:n - 1]      # multiply by x
        return o

    u = set()
    sizes = []
    for c in picks:
        u |= orbit(c)
        sizes.append(len(u))
    first = [sizes[i] - sizes[i - 1] for i in range(1, len(sizes))]
    second = [first[i] - first[i - 1] for i in range(1, len(first))]
    return sizes, first, (max(second) if second else 0)


# ------------------------------------------------- base-set norm sanity check
def base_norms(N):
    n = N // 2
    rows = []
    for k in range(1, N):
        vec = [0] * n
        if k < n:
            vec[k] += 1
        else:
            vec[k - n] -= 1
        vec[0] -= 1                                 # x^k - 1
        nm = exact_norm(vec, n)
        rows.append(("x^%d-1" % k, nm, is_pow2(nm)))
    vec = [0] * n
    vec[0] = 1
    vec[1] = 1
    nm = exact_norm(vec, n)                         # 1+x
    rows.append(("1+x", nm, is_pow2(nm)))
    return rows


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"

    if which in ("all", "r1"):
        print("== R1 COLLAPSE (Pro-Brief-F antipodal family) ==")
        for N in (8, 16, 32):
            tot, dis, pad = r1_collapse(N)
            print("  N=%3d  |F|=%d  #distinct e1=%d  COLLAPSE=%d  "
                  "C(n-2,n/2-1)=%d  distinct==N? %s"
                  % (N, tot, dis, tot // dis, pad, dis == N))

    if which in ("all", "bases"):
        print("== BASE NORMS (is every certified base of 2-power norm?) ==")
        for N in (8, 16, 32):
            rows = base_norms(N)
            bad = [r for r in rows if not r[2]]
            print("  N=%3d  bases=%d  all |Norm| a power of 2? %s  "
                  "norms seen=%s"
                  % (N, len(rows), not bad,
                     sorted({abs(r[1]) for r in rows})))
            if bad:
                print("    OFFENDERS:", bad[:5])

    if which in ("all", "r2"):
        print("== R2 ORBIT-UNION GROWTH (E12 replay) ==")
        for N in (8, 16, 32):
            sizes, first, curv = r2_orbit_growth(N)
            print("  N=%3d  U(t)=%s" % (N, sizes))
            print("         SLOPE increments=%s  CURV=%d  (2N=%d)"
                  % (first, curv, 2 * N))

    if which in ("all", "r4"):
        print("== R4 MAXPOW2 (max certifiable family, cyclotomic bases) ==")
        for N in (8, 16):
            nc, npv, size, clique = r4_maxpow2(N)
            print("  N=%3d  |centers|=%d  |P|=%d  MAXPOW2=%d   (N=%d, 2N=%d)"
                  % (N, nc, npv, size, N, 2 * N))
            print("         witness clique: %s" % (clique[:6],))


if __name__ == "__main__":
    main()
