#!/usr/bin/env python3
# r37_urand run 1: exhaustive far-CA census with the T_fib/T_sym/T_rand split
# and the codeword-side (U-rand) analysis.  Stdlib only.  Fresh implementation
# against the anchors' conventions:
#   v_x = 1/prod_{y!=x}(x-y),  y_m = sum_x e(x) v_x x^m  (m = 0..R-1),
#   M_r(y) = (y_{i+j})_{0<=i<rho, 0<=j<=r},  locator sigma = prod_{x in S}(X-x),
#   low-to-high coefficient order.  Bad slope <=> (M_0 + gamma M_1) sigma = 0
#   for a SPLIT sigma of degree exactly r.  Column-far <=> no sigma with
#   M_0 sigma = M_1 sigma = 0.
# RESULTS FILE IS OPENED IN APPEND MODE (round-36 rule).  Never pipe through head.

import sys
from math import comb, log2

OUT = "notes/pilots_20260811/r37_urand/g1_results.txt"
FH = open(OUT, "a")          # APPEND, never "w"


def emit(s):
    FH.write(s + "\n")
    FH.flush()
    print(s)


def inv(a, q):
    return pow(a % q, q - 2, q)


def build_domain(m, q, negclosed):
    """negclosed: D = {+-1,...,+-m}, indices paired (2i,2i+1).  else D={1..2m}."""
    if negclosed:
        D = []
        for i in range(1, m + 1):
            D.append(i % q)
            D.append((-i) % q)
        partner = [j ^ 1 for j in range(2 * m)]
    else:
        D = [(i % q) for i in range(1, 2 * m + 1)]
        partner = [None] * (2 * m)
    return D, partner


def vvals(D, q):
    n = len(D)
    v = []
    for i in range(n):
        p = 1
        for j in range(n):
            if j != i:
                p = (p * (D[i] - D[j])) % q
        v.append(inv(p, q))
    return v


def syndromes(D, v, Tidx, e, R, q):
    """y_m = sum_{x in T} e(x) v_x x^m, m = 0..R-1."""
    y = [0] * R
    for idx in Tidx:
        x = D[idx]
        coef = (e[idx] * v[idx]) % q
        xp = 1
        for m in range(R):
            y[m] = (y[m] + coef * xp) % q
            xp = (xp * x) % q
    return y


def sweep(D, y0, y1, rho, r, q, Wset, partner):
    """Exhaustive sweep of every r-subset of D.  Returns
       slopes: gamma -> [fib, even, min_t, rep_S(tuple), n_loc],
       n_close (common locators), n_leaves, n_inc (incidences)."""
    n = len(D)
    y0s = [tuple(y0[i:i + r + 1]) for i in range(rho)]
    y1s = [tuple(y1[i:i + r + 1]) for i in range(rho)]
    slopes = {}
    stats = [0, 0, 0]          # close, leaves, incidences
    negcl = partner[0] is not None

    def rec(start, depth, poly, chosen):
        if depth == r:
            stats[1] += 1
            uv = [sum(a * b for a, b in zip(y0s[i], poly)) % q for i in range(rho)]
            wv = [sum(a * b for a, b in zip(y1s[i], poly)) % q for i in range(rho)]
            nzu = any(uv)
            nzw = any(wv)
            if not nzu and not nzw:
                stats[0] += 1
                return
            if not nzw:
                return                      # u != 0, w = 0 : no gamma
            piv = next(i for i in range(rho) if wv[i])
            g = (-uv[piv] * inv(wv[piv], q)) % q
            for i in range(rho):
                if (uv[i] + g * wv[i]) % q:
                    return
            stats[2] += 1
            S = tuple(chosen)
            Sset = set(S)
            fib = Sset <= Wset
            if negcl:
                ev = all((idx ^ 1) in Sset for idx in S)
            else:
                ev = False
            t = len(Sset - Wset)
            rec0 = slopes.get(g)
            if rec0 is None:
                slopes[g] = [fib, ev, t, S, 1]
            else:
                rec0[0] = rec0[0] or fib
                rec0[1] = rec0[1] or ev
                if t < rec0[2]:
                    rec0[2] = t
                    if not rec0[0]:
                        rec0[3] = S
                rec0[4] += 1
            return
        hi = n - (r - depth)
        for i in range(start, hi + 1):
            x = D[i]
            np_ = [0] * (depth + 2)
            for j in range(depth + 1):
                c = poly[j]
                if c:
                    np_[j + 1] = (np_[j + 1] + c) % q
                    np_[j] = (np_[j] - x * c) % q
            chosen.append(i)
            rec(i + 1, depth + 1, np_, chosen)
            chosen.pop()

    rec(0, 0, [1], [])
    return slopes, stats


def solve_error(D, v, S, z, R, q):
    """unique u supported on S with syn(u) = z (|S| <= R, MDS => injective).
       Returns dict idx->value, or None if inconsistent."""
    cols = list(S)
    rows = []
    for m in range(R):
        row = []
        for idx in cols:
            row.append(pow(D[idx], m, q) * v[idx] % q)
        row.append(z[m] % q)
        rows.append(row)
    nc = len(cols)
    piv_of = []
    rr = 0
    for c in range(nc):
        p = None
        for i in range(rr, R):
            if rows[i][c]:
                p = i
                break
        if p is None:
            continue
        rows[rr], rows[p] = rows[p], rows[rr]
        ivv = inv(rows[rr][c], q)
        rows[rr] = [(a * ivv) % q for a in rows[rr]]
        for i in range(R):
            if i != rr and rows[i][c]:
                f = rows[i][c]
                rows[i] = [(a - f * b) % q for a, b in zip(rows[i], rows[rr])]
        piv_of.append(c)
        rr += 1
    for i in range(rr, R):
        if rows[i][nc]:
            return None
    sol = [0] * nc
    for i, c in enumerate(piv_of):
        sol[c] = rows[i][nc]
    return {cols[i]: sol[i] for i in range(nc)}


def analyse_codeword(D, v, S, g, y0, y1, Widx, e0, e1, R, q, n):
    """u = h_gamma + c, c in C.  Return (wt_c, |supp(c) cap W|, syn0ok, t)."""
    z = [(y0[m] + g * y1[m]) % q for m in range(R)]
    u = solve_error(D, v, S, z, R, q)
    if u is None:
        return None
    full = [0] * n
    for idx, val in u.items():
        full[idx] = val % q
    h = [0] * n
    for idx in Widx:
        h[idx] = (e0[idx] + g * e1[idx]) % q
    c = [(full[i] - h[i]) % q for i in range(n)]
    wt = sum(1 for a in c if a)
    inW = sum(1 for i in Widx if c[i])
    # verify syn(c) = 0
    ok = True
    for m in range(R):
        s = 0
        for i in range(n):
            if c[i]:
                s += c[i] * v[i] % q * pow(D[i], m, q)
        if s % q:
            ok = False
            break
    t = len(set(S) - set(Widx))
    return (wt, inW, ok, t, sum(1 for a in full if a))


def run_cell(tag, m, k, rho, negclosed, dexp, qs, maxcw=30):
    n = 2 * m
    R = n - k
    r = R - rho
    a = n - r
    faithful = (4 * rho < R) and (a > R + 1) and (a - 1 > r)
    emit("")
    emit("=" * 78)
    emit("CELL %s  n=%d k=%d R=%d rho=%d r=%d a=%d m=%d  D=%s  e1=x^%d"
         % (tag, n, k, R, rho, r, a, m,
            "negclosed{+-1..+-%d}" % m if negclosed else "{1..%d}" % n, dexp))
    emit("FAITHFUL 4rho<R=%s a>R+1=%s a-1>r=%s  -> %s"
         % (4 * rho < R, a > R + 1, a - 1 > r, "FAITHFUL" if faithful else "NOT FAITHFUL"))
    emit("C(n,r)=%d   log2 C(n,r)=%.4f" % (comb(n, r), log2(comb(n, r))))
    if not faithful:
        emit("SKIPPED (faithfulness gate)")
        return
    for q in qs:
        D, partner = build_domain(m, q, negclosed)
        v = vvals(D, q)
        # T = one-sided support of size r+1 : the first r+1 POSITIVE elements
        if negclosed:
            Tidx = [2 * i for i in range(r + 1)]          # 1,2,...,r+1
        else:
            Tidx = [i for i in range(r + 1)]
        e0 = [0] * n
        e1 = [0] * n
        for idx in Tidx:
            e0[idx] = 1
            e1[idx] = pow(D[idx], dexp, q)
        y0 = syndromes(D, v, Tidx, e0, R, q)
        y1 = syndromes(D, v, Tidx, e1, R, q)
        Wset = set(Tidx)
        slopes, stats = sweep(D, y0, y1, rho, r, q, Wset, partner)
        mu1 = comb(n, r) / (q ** rho)
        T = len(slopes)
        Tf = sum(1 for s in slopes.values() if s[0])
        Ts = sum(1 for s in slopes.values() if (not s[0]) and s[1])
        Tr = sum(1 for s in slopes.values() if (not s[0]) and (not s[1]))
        far = (stats[0] == 0)
        emit("-" * 74)
        emit("q=%d  mu_1=%.6g  q*mu_1=%.6g  leaves=%d  incidences=%d  "
             "common_locators=%d  COLUMN-%s"
             % (q, mu1, q * mu1, stats[1], stats[2], stats[0],
                "FAR" if far else "CLOSE"))
        emit("  T=%d   T_fib=%d   T_sym=%d   T_rand=%d   (r+1=%d)"
             % (T, Tf, Ts, Tr, r + 1))
        # null for the codeword-mediated population
        emit("  null: E[incidences] = C(n,r)*q^(1-rho) = %.6g" % (comb(n, r) * q ** (1 - rho)))
        if not far:
            emit("  ROW EXCLUDED FROM CONCLUSIONS (column-close)")
        # spend histogram over non-fib slopes
        hist = {}
        for g, s in slopes.items():
            if not s[0]:
                hist[s[2]] = hist.get(s[2], 0) + 1
        if hist:
            emit("  spend t=|S\\W| histogram over non-fib slopes (min t per slope): "
                 + " ".join("t=%d:%d" % (kk, hist[kk]) for kk in sorted(hist)))
        emit("  FENCE-1 check: rho+1-f = %d  (f=|W|-r=%d) ; min t over non-fib slopes = %s"
             % (rho + 1 - (len(Tidx) - r), len(Tidx) - r,
                min(hist) if hist else "n/a"))
        # codeword analysis on non-fib slopes
        nshow = 0
        viol = 0
        minwt_hits = 0
        cw_rows = 0
        for g, s in sorted(slopes.items()):
            if s[0]:
                continue
            if nshow >= maxcw:
                break
            res = analyse_codeword(D, v, s[3], g, y0, y1, Tidx, e0, e1, R, q, n)
            if res is None:
                emit("    slope %d : NO ERROR ON REP LOCATOR (inconsistent) -- INVESTIGATE" % g)
                continue
            wt, inW, ok, t, wu = res
            cw_rows += 1
            if wt < R + 1:
                viol += 1
            if wt == R + 1:
                minwt_hits += 1
            nshow += 1
            emit("    slope=%d %s t=%d wt(u)=%d wt(c)=%d |supp(c)^W|=%d/%d "
                 "syn(c)=0:%s  wt(c)>=R+1:%s  minwt:%s  W<=supp(c):%s"
                 % (g, "SYM" if s[1] else "RAND", t, wu, wt, inW, len(Tidx), ok,
                    wt >= R + 1, wt == R + 1, inW == len(Tidx)))
        emit("  codeword rows analysed=%d  MDS violations (wt(c)<R+1)=%d  "
             "minimum-weight c=%d" % (cw_rows, viol, minwt_hits))


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    emit("")
    emit("################ RUN g1_census.py  arg=%s ################" % which)
    QS6 = [101, 349, 1009, 10007, 65537, 999983]
    if which in ("all", "c1"):
        # C1 : n=20 k=10 R=10 rho=2 r=8 a=12  (anchor 1's H1 shape), negation-closed
        run_cell("C1/F1 (LB1, d=1)", 10, 10, 2, True, 1, QS6)
        run_cell("C1/F2 (d2-inj)", 10, 10, 2, True, 2, QS6)
        # K1 control: same shape, NON negation-closed domain {1..20}
        run_cell("K1/F2 control (D={1..20})", 10, 10, 2, False, 2, [65537, 999983])
        run_cell("K1/F1 control (D={1..20})", 10, 10, 2, False, 1, [65537, 999983])
    if which in ("all", "c2"):
        # C2 : n=24 k=12 R=12 rho=2 r=10 a=14  second shape
        run_cell("C2/F1 (LB1, d=1)", 12, 12, 2, True, 1, [10007, 65537])
        run_cell("C2/F2 (d2-inj)", 12, 12, 2, True, 2, [10007, 65537])
    emit("################ END RUN g1_census.py ################")


main()
FH.close()
