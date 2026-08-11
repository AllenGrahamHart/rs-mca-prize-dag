#!/usr/bin/env python3
"""e1_forced_fixed.py -- rh_moving_kernel (round 33), D1.

Round 32's R-MOVING premise: in the wide regime the generic kernel of the
syndrome Hankel pencil is a 2-generated apolar truncation; the kernel splits
as m_P = r+1-p shifts of P and m_Q = r+p-R shifts of Q'; "since the two
multiplicities sum to 2r+1-R while their weighted Kronecker sum is <= rho,
AT LEAST ONE GENERATOR IS FORCED FIXED".

This tests the conclusion directly.  For each column-far plane:
  rho    = generic rank of M(Z)                       (r+1-rho = dim ker)
  h_r    = rank of the stacked [M_r(y_0); M_r(y_1)]   (r+1-h_r = dim K_0)
  p_gen  = min i with ker cat_i(y_gamma) != 0 at a generic gamma
           (= degree of the LOW apolar generator of Phi_gamma)
  p_star = min i with ker [cat_i(y_0); cat_i(y_1)] != 0
           (= min degree of a COMMON apolar form of the pencil)
P is fixed  <=>  p_star == p_gen  (and then P = P_star).
Q' is fixed <=>  R+1-p_gen appears as a common apolar degree with the
           right multiplicity; we test it as dim K_0 >= m_Q with a common
           form of degree R+1-p_gen.

Naive round-32 prediction: m_P > rho  ==>  P fixed;  m_Q > rho ==> Q' fixed.

Stdlib only.  Run under: tools/ramguard local -- python3 <this>
"""
import itertools
import random
import time

T0 = time.time()
OUT = "notes/pilots_20260811/rh_moving_kernel/e1_forced_fixed_results.txt"
LINES = []


def emit(s):
    LINES.append(s)
    with open(OUT, "w") as fh:
        fh.write("\n".join(LINES) + "\n")


def inv(x, q):
    return pow(x, q - 2, q)


def build(n, k, q):
    """RS[F_q, D={0..n-1}, k]: R = n-k, dual basis v_x, syndrome rows."""
    R = n - k
    D = list(range(n))
    v = []
    for x in D:
        p = 1
        for y in D:
            if y != x:
                p = p * (x - y) % q
        v.append(inv(p, q))
    return R, D, v


def syn(f, D, v, R, q):
    """y_m = sum_x f(x) v_x x^m, m = 0..R-1."""
    return [sum(f[i] * v[i] % q * pow(D[i], m, q) for i in range(len(D))) % q
            for m in range(R)]


def rref(M, q):
    M = [row[:] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    piv = []
    rk = 0
    for c in range(cols):
        p = None
        for i in range(rk, rows):
            if M[i][c]:
                p = i
                break
        if p is None:
            continue
        M[rk], M[p] = M[p], M[rk]
        iv = inv(M[rk][c], q)
        M[rk] = [x * iv % q for x in M[rk]]
        for i in range(rows):
            if i != rk and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[rk][j]) % q for j in range(cols)]
        piv.append(c)
        rk += 1
    return M[:rk], piv


def nullspace(M, q):
    if not M:
        return []
    Rm, piv = rref(M, q)
    cols = len(M[0])
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        vv = [0] * cols
        vv[f] = 1
        for i, c in enumerate(piv):
            vv[c] = (-Rm[i][f]) % q
        basis.append(vv)
    return basis


def cat(y, R, i):
    """degree-i catalecticant of the degree-(R-1) form with coeffs y."""
    return [[y[a + b] for b in range(i + 1)] for a in range(R - i)]


def rank(M, q):
    if not M:
        return 0
    return len(rref(M, q)[0])


def norml(v, q):
    """normalise a nonzero vector: first nonzero entry = 1."""
    for x in v:
        if x:
            iv = inv(x, q)
            return tuple(t * iv % q for t in v)
    return tuple(v)


def locators(n, r, D, q):
    out = []
    for X in itertools.combinations(range(n), r):
        c = [1]
        for j in X:
            c = [0] + c
            for i in range(len(c) - 1):
                c[i] = (c[i] - D[j] * c[i + 1]) % q
        out.append((X, c + [0] * (r + 1 - len(c))))
    return out


def in_span(vec, basisrref, piv, q):
    w = vec[:]
    for i, p in enumerate(piv):
        if w[p]:
            f = w[p]
            w = [(w[j] - f * basisrref[i][j]) % q for j in range(len(w))]
    return not any(w)


def analyse(y0, y1, n, k, a, q, D, LOC):
    R = n - k
    r = n - a
    # generic rank rho and h_r
    ranks = {}
    for g in range(q):
        yg = [(y0[m] + g * y1[m]) % q for m in range(R)]
        ranks[g] = rank(cat(yg, R, r), q)
    rho = max(ranks.values())
    st = cat(y0, R, r) + cat(y1, R, r)
    h_r = rank(st, q)
    K0 = nullspace(st, q)
    dimK0 = len(K0)
    # column-far test: K0 carries no domain split locator
    if K0:
        Kr, Kp = rref([v[:] for v in K0], q)
        for (X, c) in LOC:
            if in_span(c, Kr, Kp, q):
                return None  # column-CLOSE
    # p_gen at a generic slope; p_star for the pencil
    p_gen = None
    gens = {}
    for g in range(q):
        yg = [(y0[m] + g * y1[m]) % q for m in range(R)]
        if rank(cat(yg, R, r), q) != rho:
            continue                      # rank-drop slope, skip
        for i in range(1, R + 1):
            ns = nullspace(cat(yg, R, i), q)
            if ns:
                gens[g] = (i, norml(ns[0], q) if len(ns) == 1 else None)
                break
    if not gens:
        return None
    degs = [d for (d, _) in gens.values()]
    p_gen = min(degs)
    p_star = None
    for i in range(1, R + 1):
        if rank(cat(y0, R, i) + cat(y1, R, i), q) < i + 1:
            p_star = i
            break
    m_P = r + 1 - p_gen
    m_Q = r + p_gen - R
    # is the low generator actually fixed?
    lowgens = set(v for (d, v) in gens.values() if d == p_gen and v is not None)
    P_fixed = (len(lowgens) == 1) and (p_star == p_gen)
    # bad slopes
    T = 0
    for g in range(q):
        yg = [(y0[m] + g * y1[m]) % q for m in range(R)]
        ns = nullspace(cat(yg, R, r), q)
        if not ns:
            continue
        Nr, Np = rref([v[:] for v in ns], q)
        for (X, c) in LOC:
            if in_span(c, Nr, Np, q):
                T += 1
                break
    return dict(rho=rho, h_r=h_r, dimK0=dimK0, p_gen=p_gen, p_star=p_star,
                m_P=m_P, m_Q=m_Q, P_fixed=P_fixed, T=T,
                ndistinct_low=len(lowgens))


def run(n, k, a, q, trials, seed=7):
    random.seed(seed)
    R, D, v = build(n, k, q)
    r = n - a
    LOC = locators(n, r, D, q)
    emit("== cell n=%d k=%d a=%d r=%d R=%d q=%d  (r+1-2(R-r)=%d) =="
         % (n, k, a, r, R, q, r + 1 - 2 * (R - r)))
    stats = {}
    nf = 0
    for _ in range(trials):
        f0 = [random.randrange(q) for _ in range(n)]
        f1 = [random.randrange(q) for _ in range(n)]
        y0 = syn(f0, D, v, R, q)
        y1 = syn(f1, D, v, R, q)
        res = analyse(y0, y1, n, k, a, q, D, LOC)
        if res is None:
            continue
        nf += 1
        key = (res["rho"], res["h_r"], res["dimK0"], res["p_gen"],
               res["p_star"], res["m_P"], res["m_Q"], res["P_fixed"])
        st = stats.setdefault(key, [0, 0, 0])
        st[0] += 1
        st[1] = max(st[1], res["T"])
        st[2] += res["ndistinct_low"]
    emit("column-far planes analysed: %d / %d" % (nf, trials))
    emit("rho h_r dimK0 p_gen p* m_P m_Q P_fixed | count maxT  naive-says-P-fixed")
    for key in sorted(stats):
        rho, h_r, dK, pg, ps, mP, mQ, pf = key
        cnt, mT, _ = stats[key]
        emit("%3d %3d %5d %5d %2d %3d %3d %7s | %5d %4d  %s"
             % (rho, h_r, dK, pg, ps, mP, mQ, pf, cnt, mT,
                "YES" if mP > rho else "no"))
    emit("")


if __name__ == "__main__":
    for (n, k, a, q, t) in [(11, 3, 5, 13, 60), (10, 2, 4, 11, 60),
                            (11, 2, 4, 13, 40), (12, 3, 5, 13, 25),
                            (9, 2, 4, 11, 60), (7, 2, 4, 11, 60)]:
        run(n, k, a, q, t)
    emit("wall %.1fs" % (time.time() - T0))
