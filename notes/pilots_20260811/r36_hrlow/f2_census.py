"""f2_census.py  (r36_hrlow)   usage: f2_census.py CELL

EXACT bad-slope census for the common-support far-CA pencils.

Sweeps every monic squarefree degree-r split locator sigma (root set
S subset D, |S| = r) exactly once.  For a locator sigma put
  u = M_r(y_0) sigma,  w = M_r(y_1) sigma.
sigma lies in ker(M_0 + gamma M_1) iff u + gamma w = 0, which pins at
most ONE gamma; u = w = 0 means sigma is a COMMON split locator, i.e.
the pair is column-CLOSE.  So one sweep yields, exactly:
  * column-far / column-close,
  * the exact total bad-slope count T,
  * the split T = T_struct + T_acc against the predicted structural
    set {gamma : |supp(e_0 + gamma e_1)| <= r}.

Writes: notes/pilots_20260811/r36_hrlow/f2_results_<CELL>.txt (own dir)
"""
import sys

CELL = sys.argv[1] if len(sys.argv) > 1 else "H1"
OUT = "notes/pilots_20260811/r36_hrlow/f2_results_%s.txt" % CELL

CELLS = {"H1": (20, 10, 2, [101, 349, 1009, 10007, 65537]),
         "H2": (22, 11, 2, [101, 65537]),
         "H3": (24, 12, 2, [101])}


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


def build_fams(n, k, rho, q, D, v):
    R = n - k
    r = R - rho
    pos_pts = [i % q for i in range(1, n // 2 + 1)]

    def Tset(kind, s):
        if kind == "one":
            return pos_pts[:s]
        T = []
        i = 1
        while len(T) < s:
            T.append(i % q)
            if len(T) < s:
                T.append((-i) % q)
            i += 1
        return T

    specs = [("d1-x", r + 1, [0, 1], "one"),
             ("d2-inj", r + 1, [0, 0, 1], "one"),
             ("d2-2to1", r + 1, [0, 0, 1], "sym"),
             ("d2-s+1inj", r + 2, [0, 0, 1], "one"),
             ("d2-s+1sym", r + 2, [0, 0, 1], "sym"),
             ("ctrl-s=r", r, [0, 1], "one")]
    if rho >= 3:
        specs.insert(3, ("d3-cube", r + 1, [0, 0, 0, 1], "one"))
    fams = []
    idx = {x: i for i, x in enumerate(D)}
    for tag, s, Lc, kind in specs:
        T = Tset(kind, s)
        e0 = {x: 1 for x in T}
        e1 = {x: polyeval(Lc, x, q) for x in T}
        if any(e1[x] == 0 for x in T):
            continue
        d = max(i for i, c in enumerate(Lc) if c % q)
        pos = [idx[x] for x in T]
        C0 = []
        C1 = []
        for i in range(rho):
            C0.append([(e0[x] * v[x] * pow(x, i, q)) % q for x in T])
            C1.append([(e1[x] * v[x] * pow(x, i, q)) % q for x in T])
        # predicted structural slopes
        groups = {}
        for x in T:
            g = (-inv(e1[x], q)) % q
            groups.setdefault(g, []).append(x)
        struct = set(g for g, Z in groups.items() if s - len(Z) <= r)
        fams.append(dict(tag=tag, s=s, d=d, pos=pos, c0=C0, c1=C1,
                         struct=struct, T=T, gam=set(), common=0))
    return fams


def run(cell, w):
    n, k, rho, fields = CELLS[cell]
    R = n - k
    r = R - rho
    a = n - r
    w("== %s n=%d k=%d R=%d rho=%d r=%d a=%d | FAITHFUL 4rho<R %s a>R+1 %s "
      "a-1>r %s" % (cell, n, k, R, rho, r, a, 4 * rho < R, a > R + 1,
                    a - 1 > r))
    from math import comb
    for q in fields:
        D = make_D(n, q)
        v = make_v(D, q)
        fams = build_fams(n, k, rho, q, D, v)
        mu1 = comb(n, r) / float(q) ** rho
        nD = len(D)

        def leaf(val):
            for fam in fams:
                pos = fam['pos']
                C0 = fam['c0']
                C1 = fam['c1']
                r0 = C0[0]
                r1 = C1[0]
                u0 = 0
                w0 = 0
                for t in range(len(pos)):
                    vv = val[pos[t]]
                    if vv:
                        u0 += r0[t] * vv
                        w0 += r1[t] * vv
                u0 %= q
                w0 %= q
                if w0 == 0 and u0 != 0:
                    continue
                U = [u0]
                W = [w0]
                for i in range(1, rho):
                    ai = C0[i]
                    bi = C1[i]
                    su = 0
                    sw = 0
                    for t in range(len(pos)):
                        vv = val[pos[t]]
                        if vv:
                            su += ai[t] * vv
                            sw += bi[t] * vv
                    U.append(su % q)
                    W.append(sw % q)
                if all(x == 0 for x in W):
                    if all(x == 0 for x in U):
                        fam['common'] += 1
                    continue
                j = next(i for i in range(rho) if W[i])
                g = (-U[j] * inv(W[j], q)) % q
                if all((U[i] + g * W[i]) % q == 0 for i in range(rho)):
                    fam['gam'].add(g)

        def rec(start, depth, val):
            if depth == r:
                leaf(val)
                return
            for idx in range(start, nD - (r - depth) + 1):
                x = D[idx]
                nv = [(val[j] * (D[j] - x)) % q for j in range(nD)]
                rec(idx + 1, depth + 1, nv)

        sys.setrecursionlimit(10000)
        rec(0, 0, [1] * nD)
        w(" -- q=%d  mu_1=C(n,r)/q^rho=%.6g   q*mu_1=%.4g   "
          "1-exp(-mu_1)=%.6f" % (q, mu1, q * mu1,
                                 1.0 - pow(2.718281828459045, -mu1)))
        for fam in fams:
            G = fam['gam']
            st = fam['struct'] & G
            acc = G - fam['struct']
            miss = fam['struct'] - G
            w("   %-10s s=%2d d=%d | column-%s (common locators=%d) | "
              "T=%3d  T_struct=%3d  T_acc=%3d  predicted_struct=%3d "
              "missing=%d | r+1=%d  T/q=%.6f" %
              (fam['tag'], fam['s'], fam['d'],
               "CLOSE" if fam['common'] else "far", fam['common'],
               len(G), len(st), len(acc), len(fam['struct']), len(miss),
               r + 1, len(G) / float(q)))


def main():
    lines = []

    def w(t):
        lines.append(t)
        print(t)
        sys.stdout.flush()

    w("# f2_census.py — exact bad-slope census, cell %s" % CELL)
    run(CELL, w)
    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("wrote", OUT)


main()
