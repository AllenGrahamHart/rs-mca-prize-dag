"""D2: does the m=1 T=rho+2 locator pencil come from a REAL column-far
syndrome Hankel pencil, and what is its full (SAT) profile?

Given a line {Q_Z = A + Z B} in P^rho whose totally-split-over-D members are
the T supported locators, a realization is a pair (y_0,y_1) in F^R x F^R with
    M_r(y_0) A = 0,   M_r(y_1) B = 0,   M_r(y_0) B + M_r(y_1) A = 0,
which is exactly  M(Z) Q_Z == 0  as a polynomial identity in Z.  That is
3(R-r) = 15 linear equations on 2R = 16 unknowns, so a nonzero solution
ALWAYS exists at these parameters; the content is whether some solution is
non-degenerate (generic rank exactly rho, column-far, every slope carrying a
FULL-weight-r error).

Then measure (SAT1)-(SAT5): rho, A, e, s, T, u_gamma, O, d_x, the deficit
identity sum_x (m-d_x) = 1+O, w* = min_{g!=g'} |S_g u S_g'|, and w* vs 7m-1
((NEWCAP) falsifier F1).  Stdlib only.
"""
import sys
from itertools import combinations

Q = 17
M = 1
RHO = 4 * M - 1          # 3
N = 16 * M               # 16
R = N // 2               # 8
K = N - R                # 8
RR = RHO                 # r = rho = 3 on the strict row


def inv(a):
    return pow(a % Q, Q - 2, Q)


def poly_from_roots(roots):
    c = [1]
    for r in roots:
        nc = [0] * (len(c) + 1)
        for i, ci in enumerate(c):
            nc[i] = (nc[i] - r * ci) % Q
            nc[i + 1] = (nc[i + 1] + ci) % Q
        c = nc
    return c


def peval(c, x):
    v = 0
    for co in reversed(c):
        v = (v * x + co) % Q
    return v


def rref(rows, ncols):
    rows = [r[:] for r in rows]
    piv, rk = [], 0
    for c in range(ncols):
        p = None
        for i in range(rk, len(rows)):
            if rows[i][c] % Q:
                p = i
                break
        if p is None:
            continue
        rows[rk], rows[p] = rows[p], rows[rk]
        iv = inv(rows[rk][c])
        rows[rk] = [v * iv % Q for v in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][c] % Q:
                f = rows[i][c]
                rows[i] = [(a - f * b) % Q for a, b in zip(rows[i], rows[rk])]
        piv.append(c)
        rk += 1
        if rk == len(rows):
            break
    return rows, piv, rk


def nullspace(rows, ncols):
    if not rows:
        return [[1 if i == j else 0 for i in range(ncols)] for j in range(ncols)]
    rr, piv, rk = rref(rows, ncols)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-rr[i][f]) % Q
        basis.append(v)
    return basis


def rank(rows, ncols):
    return rref(rows, ncols)[2]


def Mr(y):
    """(R-r) x (r+1) Hankel: rows i=0..R-r-1, cols j=0..r"""
    return [[y[i + j] for j in range(RR + 1)] for i in range(R - RR)]


def split_locators_of(mat, D):
    """all monic squarefree degree-r polys with roots in D lying in ker(mat)"""
    ns = nullspace(mat, RR + 1)
    if not ns:
        return []
    out = []
    d = len(ns)
    # enumerate projective points of the kernel
    for coeffs in _proj(d):
        v = [0] * (RR + 1)
        for c, b in zip(coeffs, ns):
            for i in range(RR + 1):
                v[i] = (v[i] + c * b[i]) % Q
        if v[RR] == 0:
            continue
        iv = inv(v[RR])
        v = [a * iv % Q for a in v]
        roots = [x for x in D if peval(v, x) == 0]
        if len(roots) == RR:
            out.append((tuple(v), tuple(sorted(roots))))
    return out


def _proj(d):
    if d == 1:
        yield (1,)
        return
    for lead in range(d):
        for tail in _tuples(d - lead - 1):
            yield tuple([0] * lead + [1] + list(tail))


def _tuples(n):
    if n == 0:
        yield ()
        return
    for t in _tuples(n - 1):
        for a in range(Q):
            yield (a,) + t


def main():
    lines = []

    def out(s):
        print(s)
        lines.append(s)

    D = sorted(pow(3, i, Q) for i in range(16))   # F_17^* = mu_16
    assert len(D) == 16 and 0 not in D
    vx = {}
    for x in D:
        p = 1
        for y in D:
            if y != x:
                p = p * (x - y) % Q
        vx[x] = inv(p)

    out("=== D2: Hankel realization + (SAT) profile, m=1, q=17 ===")
    out(f"D = F_17^* (|D|={len(D)}), k={K}, R={R}, r={RR}, rho_target={RHO}, "
        f"A_target={R + 1 - 2 * RHO}, e_target={M}, 7m-1={7 * M - 1}")
    out("")

    # ---- re-derive every T=5 pencil exhaustively -------------------------
    idx = {x: i for i, x in enumerate(D)}
    triples = list(combinations(D, RHO))
    Pv = {t: [peval(poly_from_roots(t), x) for x in D] for t in triples}
    found = {}
    for i1 in range(len(triples)):
        t1 = triples[i1]
        s1 = set(t1)
        P1 = Pv[t1]
        for i2 in range(i1 + 1, len(triples)):
            t2 = triples[i2]
            if s1 & set(t2):
                continue
            P2 = Pv[t2]
            cnt = {}
            for j, x in enumerate(D):
                if x in s1:
                    v = 0
                elif x in set(t2):
                    v = "INF"
                else:
                    v = (-P1[j] * inv(P2[j])) % Q
                cnt.setdefault(v, []).append(x)
            fam = [tuple(sorted(g)) for g, pts in
                   sorted(cnt.items(), key=str) if len(pts) == RHO
                   for g in [pts]]
            if len(fam) == RHO + 2:
                found[frozenset(fam)] = (t1, t2)
    out(f"distinct T=rho+2=5 locator families (as sets of {RHO}-subsets): "
        f"{len(found)}")
    out("")

    good = 0
    reported = 0
    for fam, (t1, t2) in sorted(found.items(), key=lambda kv: sorted(kv[0])):
        fams = sorted(fam)
        # build the line through P_{t1}, P_{t2}
        A0 = poly_from_roots(t1)
        B0 = poly_from_roots(t2)
        members = {}
        for lam in list(range(Q)) + ["INF"]:
            if lam == "INF":
                v = B0[:]
            else:
                v = [(a + lam * b) % Q for a, b in zip(A0, B0)]
            members[lam] = v
        # pick B = a NON-split member so all split members sit at finite Z
        splitpar = set()
        for lam, v in members.items():
            if v[RHO] == 0:
                continue
            iv = inv(v[RHO])
            w = [a * iv % Q for a in v]
            if len([x for x in D if peval(w, x) == 0]) == RHO:
                splitpar.add(lam)
        nonsplit = [l for l in members if l not in splitpar]
        if not nonsplit:
            continue
        B = members[nonsplit[0]]
        A = members[0] if 0 not in (nonsplit[0],) else members[1]
        # linear system on (y_0,y_1) in F^{2R}
        rows = []
        for i in range(R - RR):
            r1 = [0] * (2 * R)
            r2 = [0] * (2 * R)
            r3 = [0] * (2 * R)
            for j in range(RR + 1):
                r1[i + j] = (r1[i + j] + A[j]) % Q
                r2[R + i + j] = (r2[R + i + j] + B[j]) % Q
                r3[i + j] = (r3[i + j] + B[j]) % Q
                r3[R + i + j] = (r3[R + i + j] + A[j]) % Q
            rows += [r1, r2, r3]
        ns = nullspace(rows, 2 * R)
        ok_here = False
        for sol in ns:
            y0, y1 = sol[:R], sol[R:]
            if not any(y0) and not any(y1):
                continue
            ranks = {}
            for g in range(Q):
                yg = [(a + g * b) % Q for a, b in zip(y0, y1)]
                ranks[g] = rank(Mr(yg), RR + 1)
            rho_meas = max(ranks.values())
            if rho_meas != RHO:
                continue
            # column-far?  common split locator of y0 and y1
            common = set(s for _, s in split_locators_of(Mr(y0), D)) & \
                     set(s for _, s in split_locators_of(Mr(y1), D))
            if common:
                continue
            # supported finite slopes
            sup = {}
            for g in range(Q):
                yg = [(a + g * b) % Q for a, b in zip(y0, y1)]
                sl = split_locators_of(Mr(yg), D)
                if sl:
                    sup[g] = sorted(set(s for _, s in sl))
            if len(sup) != RHO + 2:
                continue
            # full-weight check: y(g) really is a weight-r error on S_g
            fullwt = True
            for g, ss in sup.items():
                if len(ss) != 1:
                    fullwt = False
                    break
                S = ss[0]
                yg = [(a + g * b) % Q for a, b in zip(y0, y1)]
                cols = [[vx[x] * pow(x, j, Q) % Q for x in S] for j in range(R)]
                aug = [cols[j] + [yg[j]] for j in range(R)]
                rr_, piv_, rk_ = rref(aug, RR + 1)
                if RR in piv_:
                    fullwt = False
                    break
                sol_e = [0] * RR
                for i, c in enumerate(piv_):
                    sol_e[c] = rr_[i][RR]
                if any(v == 0 for v in sol_e):
                    fullwt = False
                    break
            if not fullwt:
                continue
            ok_here = True
            good += 1
            if reported < 2:
                reported += 1
                Ssets = {g: sup[g][0] for g in sorted(sup)}
                dx = {x: sum(1 for S in Ssets.values() if x in S) for x in D}
                O = sum(RHO - len(S) for S in Ssets.values())
                deficit = sum(M - dx[x] for x in D)
                ws = min(len(set(Ssets[g]) | set(Ssets[h]))
                         for g, h in combinations(sorted(Ssets), 2))
                out(f"--- REALIZED WITNESS #{reported} ---")
                out(f"  y_0 = {y0}")
                out(f"  y_1 = {y1}")
                out(f"  generic rank rho = {rho_meas}  =>  "
                    f"A = R+1-2rho = {R + 1 - 2 * rho_meas}")
                out(f"  rank multiset over finite slopes: "
                    f"{sorted(set(ranks.values()))}, "
                    f"#slopes with rank<rho = "
                    f"{sum(1 for v in ranks.values() if v < rho_meas)}")
                out(f"  T (finite supported slopes) = {len(sup)} "
                    f"= rho+2 = {RHO + 2}   <-- (SAT3)")
                for g in sorted(Ssets):
                    out(f"    slope {g:2d}: S = {Ssets[g]}  u_gamma = "
                        f"{len(Ssets[g])}")
                out(f"  O = sum(rho-u_gamma) = {O}   (SAT2 needs O <= delta "
                    f"= {M - 1})")
                out(f"  d_x = {[dx[x] for x in D]}  max = {max(dx.values())} "
                    f"(<= e = {M})")
                out(f"  deficit sum_x (m-d_x) = {deficit}  vs  1+O = {1 + O}"
                    f"   (SAT4) {'OK' if deficit == 1 + O else 'FAIL'}")
                out(f"  saturated points (d_x=m): "
                    f"{sum(1 for x in D if dx[x] == M)} "
                    f">= N-(1+O) = {N - (1 + O)}   (SAT5)")
                out(f"  column-far: no common split locator  OK")
                out(f"  w* = min |S_g u S_h| = {ws} ; 7m-1 = {7 * M - 1} ; "
                    f"2rho = {2 * RHO}")
                out(f"  (NEWCAP) F1 fires (w* > 7m-1)? "
                    f"{'YES' if ws > 7 * M - 1 else 'NO'}")
                out(f"  a* = w* = {ws}; CAP(m,a*) = "
                    f"{(N - ws) * M // (R + 1 - ws) if R + 1 - ws > 0 else 'n/a'}")
            break
        if ok_here:
            pass
    out("")
    out("=== SUMMARY ===")
    out(f"  T=rho+2 locator families found (exhaustive): {len(found)}")
    out(f"  of these, families with a NON-DEGENERATE column-far Hankel "
        f"realization at generic rank rho={RHO} (A=3), e=1, s=0: {good}")
    out(f"  (SAT3) REALIZABLE at m=1,q=17: {'YES' if good else 'NO'}")
    with open(sys.argv[1], "w") as f:
        f.write("\n".join(lines) + "\n")


main()
