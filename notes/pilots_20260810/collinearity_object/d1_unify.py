"""D1/D2: ONE object, both functionals, same cells.

Unified object (R0/R1 of the PREREG):

    D  = order-N multiplicative subgroup of F_q^*,  V subset D, a=|V|
    L_T = [ sigma_T(x) ]_{x in V}                     (direct locator, ssparse)
    P_S = [ 1/(sigma'_V(x) sigma_S(x)) ]_{x in V}     (reciprocal, apolar)

(U1)  P_S = diag(x/N) . L_{(D\\V)\\S}     -- tested here (P3).

Measured functionals: F_COLL (max collinear), STRUCT3/SPOR3 (apolar's
triple census, recovered exactly from the line census), the moving degree
k, the counting profile d_x, and RIG = a-1-2s.

Stdlib only.  Run under tools/ramguard.
"""
import itertools
import random
import sys
from math import comb


def say(s=""):
    print(str(s), flush=True)


def subgroup(n, q):
    """ffield.subgroup convention: [h^0, h^1, ...] (ssparse ordering)."""
    assert (q - 1) % n == 0
    fac, m, d = set(), q - 1, 2
    while d * d <= m:
        while m % d == 0:
            fac.add(d)
            m //= d
        d += 1
    if m > 1:
        fac.add(m)
    g = 2
    while any(pow(g, (q - 1) // p, q) == 1 for p in fac):
        g += 1
    h = pow(g, (q - 1) // n, q)
    return [pow(h, i, q) for i in range(n)]


class Inv:
    def __init__(self, q):
        self.q = q
        self.c = {}

    def __call__(self, x):
        v = self.c.get(x)
        if v is None:
            v = pow(x, self.q - 2, self.q)
            self.c[x] = v
        return v


def sigma_prime(V, q):
    out = {}
    for x in V:
        p = 1
        for y in V:
            if y != x:
                p = p * (x - y) % q
        out[x] = p
    return out


def norm(v, q, inv):
    for c in v:
        if c:
            iv = inv(c)
            return tuple(t * iv % q for t in v)
    return None


def pointP(S, V, spv, q, inv):
    """P_S = [1/(sigma'_V(x) sigma_S(x))] == [prod_{y!=x} w_y], w nonzero."""
    w = []
    for x in V:
        t = spv[x]
        for y in S:
            t = t * (x - y) % q
        w.append(t % q)
    a = len(V)
    pre = [1] * (a + 1)
    for i in range(a):
        pre[i + 1] = pre[i] * w[i] % q
    suf = [1] * (a + 1)
    for i in range(a - 1, -1, -1):
        suf[i] = suf[i + 1] * w[i] % q
    return norm([pre[i] * suf[i + 1] % q for i in range(a)], q, inv)


def pointL(T, V, q, inv):
    return norm([_sig(T, x, q) for x in V], q, inv)


def _sig(T, x, q):
    t = 1
    for y in T:
        t = t * (x - y) % q
    return t


def plucker(u, v, q, a, inv):
    m = []
    for i in range(a):
        ui, vi = u[i], v[i]
        for j in range(i + 1, a):
            m.append((ui * v[j] - u[j] * vi) % q)
    return norm(m, q, inv)


def line_census(P, q, a, inv):
    """returns (F_COLL, lines) with lines = [(pt_index_tuple)] for every
    projective line carrying >= 3 of the DISTINCT points P."""
    M = len(P)
    best, lines = min(M, 2), []
    for i in range(M):
        d = {}
        Pi = P[i]
        for j in range(i + 1, M):
            k = plucker(Pi, P[j], q, a, inv)
            g = d.get(k)
            if g is None:
                d[k] = [j]
            else:
                g.append(j)
        for k, g in d.items():
            if len(g) >= 2:
                lines.append((i,) + tuple(g))
                if len(g) + 1 > best:
                    best = len(g) + 1
    return best, lines


def all_collinear(P, q):
    a = len(P[0])
    for i in range(a):
        for j in range(i + 1, a):
            det = (P[0][i] * P[1][j] - P[0][j] * P[1][i]) % q
            if det:
                iv = pow(det, q - 2, q)
                for p in P[2:]:
                    al = (p[i] * P[1][j] - p[j] * P[1][i]) % q * iv % q
                    be = (P[0][i] * p[j] - P[0][j] * p[i]) % q * iv % q
                    for t in range(a):
                        if (al * P[0][t] + be * P[1][t] - p[t]) % q:
                            return False
                return True
    return False


def classify(fam, s, q):
    """fam = list of S-tuples on one line.  Returns a dict of invariants."""
    Ss = [frozenset(S) for S in fam]
    M = len(Ss)
    G = Ss[0] | Ss[1]
    I = Ss[0] & Ss[1]
    k = s - len(I)
    inside = all(S <= G for S in Ss)
    comps = [G - S for S in Ss]
    disj = True
    seen = set()
    for c in comps:
        if c & seen:
            disj = False
        seen |= c
    U = set()
    for S in Ss:
        U |= S
    cnt = {}
    for S in Ss:
        for x in S:
            cnt[x] = cnt.get(x, 0) + 1
    inter = set(Ss[0])
    for S in Ss[1:]:
        inter &= S
    return dict(M=M, k=k, Gsz=len(G), Usz=len(U), inside=inside,
                fibres_disjoint=disj, fibre_sizes=sorted({len(c) for c in comps}),
                dmax=max(cnt.values()), inter=len(inter),
                label=("k1-PENCIL" if len(U) == s + 1 else
                       ("k%d-FIBRE" % k if (inside and disj) else "OTHER")))


def cell(q, N, a, s, Vidx=None, verbose=True, tag=""):
    inv = Inv(q)
    D = subgroup(N, q)
    V = [D[i] for i in (Vidx if Vidx is not None else range(a))]
    rest = [x for x in D if x not in V]
    assert len(rest) == N - a
    spv = sigma_prime(V, q)
    subs = list(itertools.combinations(rest, s))
    pt2S, order = {}, []
    for S in subs:
        p = pointP(S, V, spv, q, inv)
        g = pt2S.get(p)
        if g is None:
            pt2S[p] = [S]
            order.append(p)
        else:
            g.append(S)
    P = order
    F, lines = line_census(P, q, a, inv)
    nS = len(subs)
    st3 = sp3 = 0
    best = None
    fams = {}
    for ln in lines:
        fam = [pt2S[P[i]][0] for i in ln]
        c = classify(fam, s, q)
        fams[c["label"]] = fams.get(c["label"], 0) + 1
        tr = comb(len(ln), 3)
        if c["Usz"] <= s + 1:
            st3 += tr
        else:
            sp3 += tr
        if best is None or len(ln) > len(best[0]):
            best = (ln, c, fam)
    rig = a - 1 - 2 * s
    if verbose:
        say("  %-18s q=%-6d N=%-3d a=%-3d s=%-2d t=%-3d RIG=%-4d #S=%-6d "
            "#pts=%-6d F_COLL=%-5d s+1=%-3d ST3=%-8d SP3=%-8d"
            % (tag, q, N, a, s, N - a - s, rig, nS, len(P), F, s + 1, st3, sp3))
        if best is not None:
            c = best[1]
            say("        max family: M=%d %s k=%d |G|=%d |U|=%d inside=%s "
                "disj=%s fibres=%s dmax=%d |cap S_i|=%d"
                % (c["M"], c["label"], c["k"], c["Gsz"], c["Usz"], c["inside"],
                   c["fibres_disjoint"], c["fibre_sizes"], c["dmax"], c["inter"]))
            say("        line families by label: %s" % sorted(fams.items()))
    return dict(F=F, nS=nS, npts=len(P), st3=st3, sp3=sp3, rig=rig, best=best)


# ------------------------------------------------------------------ P3 (U1)
def test_U1(qs, Ns, trials=256):
    say("=== P3 : the UNIFICATION IDENTITY (U1) "
        "P_S = diag(x/N) . L_{(D\\V)\\S} ===")
    random.seed(20260810)
    ok = bad = 0
    for q in qs:
        for N in Ns:
            if (q - 1) % N:
                continue
            inv = Inv(q)
            D = subgroup(N, q)
            for _ in range(trials):
                a = random.randint(2, min(8, N - 3))
                V = random.sample(D, a)
                rest = [x for x in D if x not in V]
                s = random.randint(1, len(rest) - 1)
                S = random.sample(rest, s)
                T = [x for x in rest if x not in S]
                spv = sigma_prime(V, q)
                lhs = pointP(tuple(S), V, spv, q, inv)
                raw = [_sig(T, x, q) * x % q * inv(N % q) % q for x in V]
                rhs = norm(raw, q, inv)
                if lhs == rhs:
                    ok += 1
                else:
                    bad += 1
            say("  q=%-6d N=%-3d : %d/%d identical" % (q, N, ok, ok + bad))
    say("  TOTAL %d ok, %d FAILURES" % (ok, bad))
    say()


# --------------------------------------------------------- P8 (fence, q=17)
def test_fence():
    say("=== P8 : the m=1 fence at q=17 -- the BOUNDARY term ===")
    q = 17
    W = [1, 2, 3, 5, 7, 11]
    Ss = [(9, 12, 13), (4, 6, 16), (8, 10, 15)]
    s, a = 3, 6
    say("  a=%d s=%d 2s=%d a-1=%d  RIG=%d  (rigid needs RIG>=0)"
        % (a, s, 2 * s, a - 1, a - 1 - 2 * s))
    say("  pairwise intersections: %s"
        % [len(set(Ss[i]) & set(Ss[j])) for i, j in ((0, 1), (0, 2), (1, 2))])

    def poly(R):
        p = [1]
        for r in R:
            n = [0] * (len(p) + 1)
            for i, c in enumerate(p):
                n[i] = (n[i] - c * r) % q
                n[i + 1] = (n[i + 1] + c) % q
            p = n
        return p

    def mul(p1, p2):
        out = [0] * (len(p1) + len(p2) - 1)
        for i, c in enumerate(p1):
            if c:
                for j, d in enumerate(p2):
                    out[i + j] = (out[i + j] + c * d) % q
        return out

    def add(p1, p2, c1=1, c2=1):
        n = max(len(p1), len(p2))
        return [((p1[i] if i < len(p1) else 0) * c1
                 + (p2[i] if i < len(p2) else 0) * c2) % q for i in range(n)]

    s1, s2, s3 = poly(Ss[0]), poly(Ss[1]), poly(Ss[2])
    sW = poly(W)
    inv = Inv(q)
    spv = sigma_prime(W, q)
    Pn = [pointP(S, W, spv, q, inv) for S in Ss]
    say("  normalised points collinear : %s"
        % all_collinear(Pn, q))
    # CORRECTION (self-caught): the polynomial identity needs the
    # coefficients in the UNNORMALISED basis v_i = [1/sigma_{S_i}(x)].
    v = [[inv(_sig(S, x, q)) for x in W] for S in Ss]
    al = be = None
    for i in range(6):
        for j in range(i + 1, 6):
            det = (v[0][i] * v[1][j] - v[0][j] * v[1][i]) % q
            if det:
                iv = inv(det)
                al = (v[2][i] * v[1][j] - v[2][j] * v[1][i]) % q * iv % q
                be = (v[0][i] * v[2][j] - v[0][j] * v[2][i]) % q * iv % q
                break
        if al is not None:
            break
    resid = max((al * v[0][t] + be * v[1][t] - v[2][t]) % q for t in range(6))
    say("  1/sigma_S3 = %d/sigma_S1 + %d/sigma_S2 on W (max residual %d)"
        % (al, be, resid))
    say("  alpha+beta = %d  (identity would force D = (1-(al+be)) sigma_W)"
        % ((al + be) % q))
    lhs = mul(s1, s2)
    rhs = mul(s3, add(mul([al], s2), mul([be], s1)))
    dif = add(lhs, rhs, 1, q - 1)
    while dif and dif[-1] == 0:
        dif.pop()
    say("  deg(sigma_S1 sigma_S2) = %d ; deg sigma_W = %d ; a = %d"
        % (len(lhs) - 1, len(sW) - 1, a))
    say("  D := s1*s2 - s3*(al*s2 + be*s1) = %s (deg %d)"
        % (dif, len(dif) - 1))
    c = None
    if len(dif) == len(sW):
        c = dif[-1]
        chk = add(dif, mul([c], sW), 1, q - 1)
        while chk and chk[-1] == 0:
            chk.pop()
        say("  D == c*sigma_W with c = %d : %s   (c != 0 : %s)"
            % (c, chk == [], c != 0))
    else:
        say("  D is NOT of degree a -- registered prediction P8 FAILS")
    say()


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"

    if mode in ("all", "u1"):
        test_U1([97, 65537], [16, 32], trials=256)
        test_fence()

    if mode in ("all", "n16"):
        say("=== D1 : the |V| ladder at N=16 (t = 16-a-s) ===")
        say("  [C1-C4 floppy/boundary (ssparse's and apolar's cells); "
            "C5-C8 rigid]")
        for q in (17, 97, 65537):
            for (a, s) in ((3, 6), (4, 5), (5, 4), (6, 3), (8, 4),
                           (7, 3), (8, 3), (9, 4), (10, 4)):
                cell(q, 16, a, s, tag="N16")
            say()

    if mode in ("all", "p4"):
        say("=== P4 : ssparse's exact cell, reciprocal side "
            "(N=16,a=3,s=6, first 3 rotation classes) ===")
        for q in (17, 97, 65537):
            best = 0
            for E in ((0, 1, 2), (0, 1, 3), (0, 1, 4)):
                r = cell(q, 16, 3, 6, Vidx=E, verbose=False, tag="")
                say("    E=%s q=%-6d F_COLL=%d  (#pts=%d)"
                    % (str(E), q, r["F"], r["npts"]))
                best = max(best, r["F"])
            say("    MAX over the three classes at q=%-6d : %d" % (q, best))
        say()

    if mode in ("all", "n32"):
        say("=== D1 : N=32 cells ===")
        for q in (97, 65537):
            for (a, s) in ((3, 2), (5, 2), (7, 3), (8, 3), (11, 3)):
                cell(q, 32, a, s, tag="N32")
            say()
    say("=== END d1_unify ===")
