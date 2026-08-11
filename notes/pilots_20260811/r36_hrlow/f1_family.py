"""f1_family.py  (r36_hrlow)

Structure of the common-support far-CA pencil family.

Model (anchor 2 conventions):
  D subset F_q, |D| = n, v_x = 1/prod_{y in D, y != x}(x-y),
  y_m = sum_x e(x) v_x x^m,  M_r(y) = (y_{i+j})_{0<=i<rho, 0<=j<=r},
  rho = R-r, R = n-k.
Both syndromes come from errors supported on a common set T, |T| = s,
with e_0 == 1 on T and e_1 = L on T, deg L = d.

Measured per (cell, field, family):
  h_r = rank[M_r(y_0); M_r(y_1)], dim K_0, p*, d*, dim Ann(V)_{p*},
  the two principality tests, the structural slope set and an EXACT
  verification of each structural slope by exhibiting its locator.

Writes: notes/pilots_20260811/r36_hrlow/f1_results.txt   (own dir only)
"""
import sys

OUT = "notes/pilots_20260811/r36_hrlow/f1_results.txt"


def inv(a, q):
    return pow(a % q, q - 2, q)


def rref(M, q):
    M = [row[:] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    r = 0
    piv = []
    for c in range(cols):
        pr = None
        for i in range(r, rows):
            if M[i][c] % q:
                pr = i
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        iv = inv(M[r][c], q)
        M[r] = [(x * iv) % q for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % q:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % q for j in range(cols)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return M, r, piv


def nullity(M, q, cols):
    if not M:
        return cols
    _, rk, _ = rref(M, q)
    return cols - rk


def nullspace(M, q, cols):
    if not M:
        b = []
        for j in range(cols):
            v = [0] * cols
            v[j] = 1
            b.append(v)
        return b
    Mr, rk, piv = rref(M, q)
    free = [c for c in range(cols) if c not in piv]
    out = []
    for f in free:
        v = [0] * cols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-Mr[i][f]) % q
        out.append(v)
    return out


def poly_from_roots(roots, q):
    p = [1]
    for a in roots:
        np_ = [0] * (len(p) + 1)
        for i, c in enumerate(p):
            np_[i + 1] = (np_[i + 1] + c) % q
            np_[i] = (np_[i] - c * a) % q
        p = np_
    return p


def polyeval(p, x, q):
    s = 0
    for c in reversed(p):
        s = (s * x + c) % q
    return s


def make_D(n, q):
    # symmetric point set {+-1,...,+-n/2}: lets a quadratic ratio be made
    # injective (one-sided T) or exactly 2-to-1 (symmetric T) at will.
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


def syndrome(T, ev, v, q, R):
    y = [0] * R
    for x in T:
        c = (ev[x] * v[x]) % q
        xp = 1
        for m in range(R):
            y[m] = (y[m] + c * xp) % q
            xp = (xp * x) % q
    return y


def hankel(y, rho, r, q):
    return [[y[i + j] % q for j in range(r + 1)] for i in range(rho)]


def pstar(H, r, q):
    """p* = min i such that exists P != 0, deg P <= i, P*x^j in K_0 for
    all 0 <= j <= r-i.  Returns (p*, dimAnn, d*, Pmin)."""
    for i in range(0, r + 1):
        rows = []
        for j in range(0, r - i + 1):
            for h in H:
                rows.append([h[t + j] for t in range(i + 1)])
        nb = nullspace(rows, q, i + 1)
        if nb:
            # d* : min degree of a nonzero element of this space
            dstar = None
            for t in range(0, i + 1):
                sub = [row[: t + 1] for row in rows]
                nb2 = nullspace(sub, q, t + 1)
                if nb2:
                    dstar = t
                    Pmin = nb2[0] + [0] * (i - t)
                    break
            return i, len(nb), dstar, Pmin
    return None, 0, None, None


def span_eq(A, B, q, cols):
    """do the row spaces of A and B coincide?"""
    _, ra, _ = rref(A, q) if A else (None, 0, None)
    _, rb, _ = rref(B, q) if B else (None, 0, None)
    if ra != rb:
        return False
    _, rc, _ = rref(A + B, q) if (A or B) else (None, 0, None)
    return rc == ra


def run_cell(n, k, rho, q, fam, w):
    R = n - k
    r = R - rho
    a = n - r
    D = make_D(n, q)
    v = make_v(D, q)
    s, Lc, Tkind = fam["s"], fam["L"], fam["T"]
    pos = [i % q for i in range(1, n // 2 + 1)]
    if Tkind == "one":
        T = pos[:s]
    else:  # symmetric: 1,-1,2,-2,...
        T = []
        i = 1
        while len(T) < s:
            T.append(i % q)
            if len(T) < s:
                T.append((-i) % q)
            i += 1
    assert len(set(T)) == s
    e0 = {x: 1 for x in T}
    e1 = {x: polyeval(Lc, x, q) for x in T}
    if any(e1[x] == 0 for x in T):
        w("  SKIP %s: L vanishes on T" % fam["tag"])
        return None
    d = max(i for i, c in enumerate(Lc) if c % q) if any(c % q for c in Lc) else 0
    y0 = syndrome(T, e0, v, q, R)
    y1 = syndrome(T, e1, v, q, R)
    M0 = hankel(y0, rho, r, q)
    M1 = hankel(y1, rho, r, q)
    H = M0 + M1
    _, hr, _ = rref(H, q)
    K0 = nullspace(H, q, r + 1)
    dimK0 = len(K0)
    ps, dimAnn, ds, Pmin = pstar(H, r, q)
    # principality tests
    pr1 = pr2 = None
    if Pmin is not None:
        Pm = Pmin[:]
        while len(Pm) > 1 and Pm[-1] % q == 0:
            Pm.pop()
        degP = len(Pm) - 1
        for (idx, cap) in ((1, r - ps), (2, r - degP)):
            if cap < 0:
                res = False
            else:
                rowsP = []
                for j in range(cap + 1):
                    vv = [0] * (r + 1)
                    for t2, c in enumerate(Pm):
                        if t2 + j <= r:
                            vv[t2 + j] = c % q
                    rowsP.append(vv)
                res = span_eq(rowsP, K0, q, r + 1)
            if idx == 1:
                pr1 = res
            else:
                pr2 = res
    else:
        degP = None
    # structural slopes: gamma = -1/L(t)
    groups = {}
    for t in T:
        g = (-inv(e1[t], q)) % q
        groups.setdefault(g, []).append(t)
    struct = []
    for g, Z in sorted(groups.items()):
        supp = [x for x in T if x not in Z]
        if len(supp) <= r:
            extra = [x for x in D if x not in T][: r - len(supp)]
            S = supp + extra
            if len(S) != r:
                continue
            sig = poly_from_roots(S, q)
            Hg = [[(M0[i][j] + g * M1[i][j]) % q for j in range(r + 1)]
                  for i in range(rho)]
            ok = all(sum(Hg[i][j] * sig[j] for j in range(r + 1)) % q == 0
                     for i in range(rho))
            struct.append((g, len(Z), len(supp), ok))
    nstruct = len(struct)
    nver = sum(1 for x in struct if x[3])
    nvals = len(groups)
    w("  fam=%-10s s=%d d=%d | h_r=%d (pred %d) dimK0=%d (pred %d) | "
      "p*=%s (pred %s) d*=%s dimAnn=%d degP=%s | princ(p*)=%s princ(degP)=%s"
      % (fam["tag"], s, d, hr, rho + d, dimK0, r + 1 - rho - d,
         ps, max(rho + d, (R + 1 + d) // 2), ds, dimAnn, degP, pr1, pr2))
    w("             #distinct L-values on T = %d ; structural slopes = %d ; "
      "VERIFIED exactly = %d ; ceil((r+1)/d) = %d ; r+1 = %d"
      % (nvals, nstruct, nver, -((-(r + 1)) // max(d, 1)), r + 1))
    return dict(hr=hr, dimK0=dimK0, ps=ps, ds=ds, nstruct=nstruct, nver=nver,
                d=d, s=s, nvals=nvals)


def main():
    lines = []

    def w(t):
        lines.append(t)
        print(t)

    CELLS = [("H1", 20, 10, 2), ("H2", 22, 11, 2), ("H3", 24, 12, 2),
             ("H4", 26, 13, 3), ("H5", 28, 14, 3)]
    FIELDS = [101, 349, 1009, 10007, 65537]
    w("# f1_family.py results — r36_hrlow")
    w("# common-support family: e_0 == 1 on T, e_1 = L on T, d = deg L")
    w("# prediction R2a: h_r = rho+d, dim K_0 = r+1-rho-d")
    w("# prediction R2c: p* = max(rho+d, floor((R+1+d)/2))")
    w("# prediction R2d/e/f: struct slopes = #distinct L-values with fibre")
    w("#   size >= s-r ; <= r+1 always ; = r+1 iff s=r+1 and L injective")
    for tag, n, k, rho in CELLS:
        R = n - k
        r = R - rho
        a = n - r
        w("")
        w("== %s  n=%d k=%d R=%d rho=%d r=%d a=%d | FAITHFUL: 4rho<R %s, "
          "a>R+1 %s, a-1>r %s" % (tag, n, k, R, rho, r, a,
                                  4 * rho < R, a > R + 1, a - 1 > r))
        fams = [
            dict(tag="d1-x", s=r + 1, L=[0, 1], T="one"),
            dict(tag="d1-x+1", s=r + 1, L=[1, 1], T="one"),
            dict(tag="d2-inj", s=r + 1, L=[0, 0, 1], T="one"),
            dict(tag="d2-2to1", s=r + 1, L=[0, 0, 1], T="sym"),
            dict(tag="d2-s+1inj", s=r + 2, L=[0, 0, 1], T="one"),
            dict(tag="d2-s+1sym", s=r + 2, L=[0, 0, 1], T="sym"),
            dict(tag="d1-s+1", s=r + 2, L=[0, 1], T="one"),
            dict(tag="ctrl-s=r", s=r, L=[0, 1], T="one"),
        ]
        if rho >= 3:
            fams.insert(4, dict(tag="d3-cube", s=r + 1, L=[0, 0, 0, 1],
                                T="one"))
        for q in FIELDS:
            w(" -- q=%d  (mu_1 = C(n,r)/q^rho)" % q)
            for fam in fams:
                try:
                    run_cell(n, k, rho, q, fam, w)
                except AssertionError as e:
                    w("  fam=%-10s ASSERT %s" % (fam["tag"], e))
    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("wrote", OUT)


main()
