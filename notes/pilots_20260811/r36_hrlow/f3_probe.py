"""f3_probe.py  (r36_hrlow)

Three probes.

A. THE d=2 EXCESS.  f2 found, at H1, that the h_r = rho+2 families keep
   ~90 bad slopes at q = 65537 where the first moment predicts ~1.9.
   Re-run the exact census at a much larger field and histogram
   |S cap T| over every (locator, slope) incidence, to see whether the
   excess is a field-size-independent structural set and what shape its
   locators have.

B. THE GENERAL CLASSIFICATION.  For RANDOM column-far pencils: take two
   bad slopes gamma_1 != gamma_2 with locators S_1, S_2, solve for the
   weight-<=r errors u_1, u_2, rebuild
      e_0 = (gamma_2 u_1 - gamma_1 u_2)/(gamma_2-gamma_1),
      e_1 = (u_1-u_2)/(gamma_1-gamma_2),
   VERIFY syn(e_0) = y_0 and syn(e_1) = y_1 (the common-support theorem),
   then measure W = supp(e_0) u supp(e_1), f = |W|-r, the structural
   slope count and the cap floor((r+f)/f).

C. THE GENERAL h_r LAW: h_r for (s, deg e_0, deg e_1) off the s = r+1,
   e_0 == 1 diagonal.

Writes: notes/pilots_20260811/r36_hrlow/f3_results.txt   (own dir)
"""
import sys

OUT = "notes/pilots_20260811/r36_hrlow/f3_results.txt"


def inv(a, q):
    return pow(a % q, q - 2, q)


def make_D(n, q):
    m = n // 2
    D = []
    for i in range(1, m + 1):
        D.append(i % q)
        D.append((-i) % q)
    assert len(set(D)) == n
    return D


def make_v(D, q):
    v = {}
    for x in D:
        pr = 1
        for y in D:
            if y != x:
                pr = (pr * (x - y)) % q
        v[x] = inv(pr, q)
    return v


def polyeval(p, x, q):
    s = 0
    for c in reversed(p):
        s = (s * x + c) % q
    return s


def syn_of(ev, D, v, q, R):
    y = [0] * R
    for x in D:
        e = ev.get(x, 0) % q
        if not e:
            continue
        c = (e * v[x]) % q
        xp = 1
        for m in range(R):
            y[m] = (y[m] + c * xp) % q
            xp = (xp * x) % q
    return y


def hank(y, rho, r, q):
    return [[y[i + j] % q for j in range(r + 1)] for i in range(rho)]


def rref(M, q):
    M = [row[:] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    rk = 0
    piv = []
    for c in range(cols):
        pr = None
        for i in range(rk, rows):
            if M[i][c] % q:
                pr = i
                break
        if pr is None:
            continue
        M[rk], M[pr] = M[pr], M[rk]
        iv = inv(M[rk][c], q)
        M[rk] = [(x * iv) % q for x in M[rk]]
        for i in range(rows):
            if i != rk and M[i][c] % q:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[rk][j]) % q for j in range(cols)]
        piv.append(c)
        rk += 1
        if rk == rows:
            break
    return M, rk, piv


def solve(A, b, q):
    """one solution of A z = b, or None"""
    rows = len(A)
    cols = len(A[0])
    M = [A[i][:] + [b[i]] for i in range(rows)]
    Mr, rk, piv = rref(M, q)
    for i in range(rk):
        pass
    # inconsistency: a pivot in the last column
    if piv and piv[-1] == cols:
        return None
    z = [0] * cols
    for i, c in enumerate(piv):
        z[c] = Mr[i][cols] % q
    # check
    for i in range(rows):
        if sum(A[i][j] * z[j] for j in range(cols)) % q != b[i] % q:
            return None
    return z


def sweep(n, r, D, q, objs, want_hist=False):
    """DFS over all r-subsets of D; objs = list of dicts with M0,M1.
    Fills obj['gam'] (slope -> a witnessing locator) and obj['common']."""
    nD = len(D)
    rho = len(objs[0]['M0'])

    def leaf(sig, S):
        for ob in objs:
            M0 = ob['M0']
            M1 = ob['M1']
            a0 = M0[0]
            b0 = M1[0]
            u0 = 0
            w0 = 0
            for j in range(r + 1):
                sj = sig[j]
                if sj:
                    u0 += a0[j] * sj
                    w0 += b0[j] * sj
            u0 %= q
            w0 %= q
            if w0 == 0 and u0 != 0:
                continue
            U = [u0]
            W = [w0]
            for i in range(1, rho):
                ai = M0[i]
                bi = M1[i]
                su = 0
                sw = 0
                for j in range(r + 1):
                    sj = sig[j]
                    if sj:
                        su += ai[j] * sj
                        sw += bi[j] * sj
                U.append(su % q)
                W.append(sw % q)
            if all(x == 0 for x in W):
                if all(x == 0 for x in U):
                    ob['common'] += 1
                continue
            jj = next(i for i in range(rho) if W[i])
            g = (-U[jj] * inv(W[jj], q)) % q
            if all((U[i] + g * W[i]) % q == 0 for i in range(rho)):
                if g not in ob['gam']:
                    ob['gam'][g] = list(S)
                if want_hist:
                    tt = ob.get('Tset')
                    if tt is not None:
                        ob['hist'][len(tt & set(S))] += 1

    def rec(start, depth, sig, S):
        if depth == r:
            leaf(sig, S)
            return
        for idx in range(start, nD - (r - depth) + 1):
            x = D[idx]
            ns = [0] * (r + 1)
            for j in range(depth + 1):
                c = sig[j]
                if c:
                    ns[j + 1] = (ns[j + 1] + c) % q
                    ns[j] = (ns[j] - c * x) % q
            S.append(x)
            rec(idx + 1, depth + 1, ns, S)
            S.pop()

    sys.setrecursionlimit(10000)
    sig0 = [0] * (r + 1)
    sig0[0] = 1
    rec(0, 0, sig0, [])


def main():
    lines = []

    def w(t):
        lines.append(t)
        print(t)
        sys.stdout.flush()

    from math import comb
    n, k, rho = 20, 10, 2
    R = n - k
    r = R - rho
    a = n - r
    w("# f3_probe.py — r36_hrlow")
    w("# cell H1 n=20 k=10 R=10 rho=2 r=8 a=12 | FAITHFUL 4rho<R %s "
      "a>R+1 %s a-1>r %s" % (4 * rho < R, a > R + 1, a - 1 > r))

    # ---------- A: the d=2 excess at a large field ----------
    w("")
    w("== A. the h_r=rho+2 excess, exact census + |S cap T| histogram")
    for q in (65537, 999983):
        D = make_D(n, q)
        v = make_v(D, q)
        pos = [i % q for i in range(1, n // 2 + 1)]
        specs = [("d1-x", r + 1, [0, 1], "one"),
                 ("d2-inj", r + 1, [0, 0, 1], "one"),
                 ("d2-2to1", r + 1, [0, 0, 1], "sym"),
                 ("d3-cube", r + 1, [0, 0, 0, 1], "one")]
        objs = []
        for tag, s, Lc, kind in specs:
            if kind == "one":
                T = pos[:s]
            else:
                T = []
                i = 1
                while len(T) < s:
                    T.append(i % q)
                    if len(T) < s:
                        T.append((-i) % q)
                    i += 1
            e0 = {x: 1 for x in T}
            e1 = {x: polyeval(Lc, x, q) for x in T}
            y0 = syn_of(e0, D, v, q, R)
            y1 = syn_of(e1, D, v, q, R)
            M0 = hank(y0, rho, r, q)
            M1 = hank(y1, rho, r, q)
            _, hr, _ = rref(M0 + M1, q)
            groups = {}
            for x in T:
                groups.setdefault((-inv(e1[x], q)) % q, []).append(x)
            st = set(g for g, Z in groups.items() if s - len(Z) <= r)
            objs.append(dict(tag=tag, M0=M0, M1=M1, gam={}, common=0,
                             Tset=set(T), hist=[0] * (r + 2), struct=st,
                             hr=hr, d=max(i for i, c in enumerate(Lc)
                                          if c % q)))
        sweep(n, r, D, q, objs, want_hist=True)
        mu1 = comb(n, r) / float(q) ** rho
        w(" -- q=%d  mu_1=%.6g  moment E[T_acc] ~ C(n,r)/q = %.4g" %
          (q, mu1, comb(n, r) / float(q)))
        for ob in objs:
            G = set(ob['gam'])
            acc = G - ob['struct']
            w("   %-9s d=%d h_r=%d(=rho+d %s) | column-%s | T=%3d "
              "T_struct=%2d T_acc=%3d | r+1=%d" %
              (ob['tag'], ob['d'], ob['hr'], ob['hr'] == rho + ob['d'],
               "CLOSE" if ob['common'] else "far", len(G),
               len(G & ob['struct']), len(acc), r + 1))
            w("        |S cap T| histogram over (locator,slope) "
              "incidences: %s" % ob['hist'])
            if acc:
                sub = sorted(acc)[:6]
                for g in sub:
                    S = ob['gam'][g]
                    w("        acc slope %d : |S cap T|=%d  S=%s" %
                      (g, len(ob['Tset'] & set(S)), sorted(S)))

    # ---------- B: general classification on RANDOM pencils ----------
    w("")
    w("== B. random pencils: common-support reconstruction + the "
      "T_struct <= floor((r+f)/f) cap")
    seed = 20260811
    for q in (349, 1009):
        D = make_D(n, q)
        v = make_v(D, q)
        objs = []
        for t in range(6):
            y0 = []
            y1 = []
            for m in range(R):
                seed = (1103515245 * seed + 12345) % (1 << 31)
                y0.append(seed % q)
                seed = (1103515245 * seed + 12345) % (1 << 31)
                y1.append(seed % q)
            M0 = hank(y0, rho, r, q)
            M1 = hank(y1, rho, r, q)
            _, hr, _ = rref(M0 + M1, q)
            objs.append(dict(tag="rnd%d" % t, M0=M0, M1=M1, gam={},
                             common=0, hr=hr, y0=y0, y1=y1))
        sweep(n, r, D, q, objs)
        w(" -- q=%d" % q)
        for ob in objs:
            G = sorted(ob['gam'])
            if ob['common'] or len(G) < 2:
                w("   %-6s h_r=%d column-%s T=%d — skipped" %
                  (ob['tag'], ob['hr'], "CLOSE" if ob['common'] else "far",
                   len(G)))
                continue
            g1, g2 = G[0], G[1]
            us = []
            ok = True
            for g in (g1, g2):
                S = ob['gam'][g]
                A = [[(v[x] * pow(x, m, q)) % q for x in S]
                     for m in range(R)]
                b = [(ob['y0'][m] + g * ob['y1'][m]) % q for m in range(R)]
                z = solve(A, b, q)
                if z is None:
                    ok = False
                    break
                us.append({S[i]: z[i] for i in range(len(S))})
            if not ok:
                w("   %-6s locator solve failed" % ob['tag'])
                continue
            dg = (g2 - g1) % q
            idg = inv(dg, q)
            e0 = {}
            e1 = {}
            for x in D:
                a1 = us[0].get(x, 0)
                a2 = us[1].get(x, 0)
                e0[x] = ((g2 * a1 - g1 * a2) * idg) % q
                e1[x] = ((a2 - a1) * idg) % q
            ok0 = syn_of(e0, D, v, q, R) == [c % q for c in ob['y0']]
            ok1 = syn_of(e1, D, v, q, R) == [c % q for c in ob['y1']]
            W = set(x for x in D if e0[x] or e1[x])
            f = len(W) - r
            struct = set()
            for g in range(q):
                cnt = 0
                for x in W:
                    if (e0[x] + g * e1[x]) % q:
                        cnt += 1
                        if cnt > r:
                            break
                if cnt <= r:
                    struct.add(g)
            cap = (r + f) // f if f > 0 else -1
            w("   %-6s h_r=%d col-far T=%3d | recon syn(e_0)=y_0 %s "
              "syn(e_1)=y_1 %s | |W|=%d f=%d | T_struct=%d cap=%d "
              "cap_ok=%s | T_acc=%d" %
              (ob['tag'], ob['hr'], len(G), ok0, ok1, len(W), f,
               len(struct & set(G)), cap, len(struct & set(G)) <= cap,
               len(set(G) - struct)))

    # ---------- C: general h_r law ----------
    w("")
    w("== C. h_r off the (s=r+1, e_0==1) diagonal   [pred h_r=rho+d only "
      "claimed for s=r+1, e_0 nonvanishing]")
    for q in (1009, 10007):
        D = make_D(n, q)
        v = make_v(D, q)
        pos = [i % q for i in range(1, n // 2 + 1)]
        w(" -- q=%d" % q)
        for s in (r + 1, r + 2, r + 3, r + 4, 2 * r):
            if s > n:
                continue
            T = pos[:s] if s <= n // 2 else (pos + [(-i) % q for i in
                                                    range(1, n // 2 + 1)])[:s]
            for A in ([1], [0, 1], [1, 1, 1]):
                for B in ([0, 1], [0, 0, 1], [0, 0, 0, 1], [1, 2, 3, 4, 5]):
                    e0 = {x: polyeval(A, x, q) for x in T}
                    e1 = {x: polyeval(B, x, q) for x in T}
                    if all(e0[x] == 0 for x in T):
                        continue
                    supp = [x for x in T if e0[x] or e1[x]]
                    y0 = syn_of(e0, D, v, q, R)
                    y1 = syn_of(e1, D, v, q, R)
                    _, hr, _ = rref(hank(y0, rho, r, q) +
                                    hank(y1, rho, r, q), q)
                    dA = max(i for i, c in enumerate(A) if c % q)
                    dB = max(i for i, c in enumerate(B) if c % q)
                    w("   s=%2d |supp|=%2d degA=%d degB=%d -> h_r=%d "
                      "dimK0=%d  (rho+max(dA,dB)=%d, 2rho=%d)" %
                      (s, len(supp), dA, dB, hr, r + 1 - hr,
                       rho + max(dA, dB), 2 * rho))

    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("wrote", OUT)


main()
