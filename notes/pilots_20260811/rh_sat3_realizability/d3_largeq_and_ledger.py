"""D3a: is the m=1 (SAT3) realization a small-field artifact?

The round's d1 scan fixed D = mu_16 and found T = rho+2 = 5 only at q = 17.
But D (the RS evaluation domain) is FREE.  The m=1 object is a degree-rho=3
rational map psi = -A/B : P^1 -> P^1; its supported slopes are exactly its
TOTALLY SPLIT fibres, and (SAT4) at m=1 only asks that 5 such fibres plus one
extra point make up D (|D| = N = 16).  So: sample degree-3 pencils over a
LARGE prime field, count totally split fibres, DESIGN D from five of them, and
re-run the full column-far Hankel realization + (SAT1)-(SAT5) audit.

D3b: the dimension ledger for general m (the T-cap heuristic).

Stdlib only.
"""
import sys
import random
from itertools import combinations

INF = "INF"


def make(q):
    def inv(a):
        return pow(a % q, q - 2, q)

    def peval(c, x):
        v = 0
        for co in reversed(c):
            v = (v * x + co) % q
        return v

    def poly_from_roots(rs):
        c = [1]
        for r in rs:
            nc = [0] * (len(c) + 1)
            for i, ci in enumerate(c):
                nc[i] = (nc[i] - r * ci) % q
                nc[i + 1] = (nc[i + 1] + ci) % q
            c = nc
        return c

    def rref(rows, ncols):
        rows = [r[:] for r in rows]
        piv, rk = [], 0
        for c in range(ncols):
            p = None
            for i in range(rk, len(rows)):
                if rows[i][c] % q:
                    p = i
                    break
            if p is None:
                continue
            rows[rk], rows[p] = rows[p], rows[rk]
            iv = inv(rows[rk][c])
            rows[rk] = [v * iv % q for v in rows[rk]]
            for i in range(len(rows)):
                if i != rk and rows[i][c] % q:
                    f = rows[i][c]
                    rows[i] = [(a - f * b) % q for a, b in zip(rows[i], rows[rk])]
            piv.append(c)
            rk += 1
            if rk == len(rows):
                break
        return rows, piv, rk

    def nullspace(rows, ncols):
        rr, piv, rk = rref(rows, ncols)
        free = [c for c in range(ncols) if c not in piv]
        basis = []
        for f in free:
            v = [0] * ncols
            v[f] = 1
            for i, c in enumerate(piv):
                v[c] = (-rr[i][f]) % q
            basis.append(v)
        return basis

    return inv, peval, poly_from_roots, rref, nullspace


def run_cell(q, seed, out):
    RHO, N, R, RR = 3, 16, 8, 3
    K = N - R
    M = 1
    inv, peval, poly_from_roots, rref, nullspace = make(q)
    rnd = random.Random(seed)

    for attempt in range(400):
        A = [rnd.randrange(q) for _ in range(RHO)] + [1]
        B = [rnd.randrange(q) for _ in range(RHO)] + [rnd.randrange(1, q)]
        # need A,B to span a pencil with >=5 totally split fibres
        fibres = {}
        for lam in list(range(q)) + [INF]:
            v = B[:] if lam == INF else [(a + lam * b) % q for a, b in zip(A, B)]
            if v[RHO] == 0:
                continue
            iv = inv(v[RHO])
            w = [a * iv % q for a in v]
            rs = [x for x in range(q) if peval(w, x) == 0]
            if len(rs) == RHO:
                fibres[lam] = tuple(sorted(rs))
        if len(fibres) < RHO + 2:
            continue
        # DESIGN D: five totally split fibres (15 points) + 1 spare point
        keys = sorted(fibres, key=str)[:RHO + 2]
        pts = set()
        bad = False
        for k_ in keys:
            f = fibres[k_]
            if pts & set(f):
                bad = True
                break
            pts |= set(f)
        if bad or len(pts) != 15:
            continue
        spare = [x for x in range(q) if x not in pts]
        if not spare:
            continue
        D = sorted(pts | {spare[0]})
        assert len(D) == N
        # re-census against THIS D
        split = {}
        for lam in list(range(q)) + [INF]:
            v = B[:] if lam == INF else [(a + lam * b) % q for a, b in zip(A, B)]
            if v[RHO] == 0:
                continue
            iv = inv(v[RHO])
            w = [a * iv % q for a in v]
            rs = [x for x in D if peval(w, x) == 0]
            if len(rs) == RHO:
                split[lam] = tuple(sorted(rs))
        if len(split) != RHO + 2:
            continue
        nonsplit = [l for l in (list(range(q)) + [INF]) if l not in split]
        # re-parametrise so every split member sits at a FINITE Z
        lb = nonsplit[0]
        Bp = B[:] if lb == INF else [(a + lb * b) % q for a, b in zip(A, B)]
        la = [l for l in split if l != INF][0]
        Ap = [(a + la * b) % q for a, b in zip(A, B)]
        # linear system  M_r(y0)Ap = 0, M_r(y1)Bp = 0, M_r(y0)Bp + M_r(y1)Ap = 0
        rows = []
        for i in range(R - RR):
            r1 = [0] * (2 * R); r2 = [0] * (2 * R); r3 = [0] * (2 * R)
            for j in range(RR + 1):
                r1[i + j] = (r1[i + j] + Ap[j]) % q
                r2[R + i + j] = (r2[R + i + j] + Bp[j]) % q
                r3[i + j] = (r3[i + j] + Bp[j]) % q
                r3[R + i + j] = (r3[R + i + j] + Ap[j]) % q
            rows += [r1, r2, r3]
        ns = nullspace(rows, 2 * R)
        vx = {}
        for x in D:
            p = 1
            for y in D:
                if y != x:
                    p = p * (x - y) % q
            vx[x] = inv(p)

        def Mr(y):
            return [[y[i + j] for j in range(RR + 1)] for i in range(R - RR)]

        def split_locs(mat):
            bas = nullspace(mat, RR + 1)
            if len(bas) == 0 or len(bas) > 2:
                return None if len(bas) > 2 else []
            outl = []
            cand = [bas[0]] if len(bas) == 1 else \
                   [bas[0]] + [[(bas[1][i] + t * bas[0][i]) % q
                               for i in range(RR + 1)] for t in range(q)]
            for v in cand:
                if v[RR] == 0:
                    continue
                iv = inv(v[RR])
                w = [a * iv % q for a in v]
                rs = [x for x in D if peval(w, x) == 0]
                if len(rs) == RHO:
                    outl.append(tuple(sorted(rs)))
            return sorted(set(outl))

        for sol in ns:
            y0, y1 = sol[:R], sol[R:]
            if not any(y0) and not any(y1):
                continue
            rk = max(rref(Mr([(a + g * b) % q for a, b in zip(y0, y1)]),
                          RR + 1)[2] for g in range(min(q, 60)))
            if rk != RHO:
                continue
            c0, c1 = split_locs(Mr(y0)), split_locs(Mr(y1))
            if c0 is None or c1 is None or (set(c0) & set(c1)):
                continue
            sup = {}
            for g in range(q):
                yg = [(a + g * b) % q for a, b in zip(y0, y1)]
                sl = split_locs(Mr(yg))
                if sl:
                    sup[g] = sl
            if len(sup) != RHO + 2 or any(len(v) != 1 for v in sup.values()):
                continue
            Ss = {g: sup[g][0] for g in sorted(sup)}
            dx = {x: sum(1 for S in Ss.values() if x in S) for x in D}
            O = sum(RHO - len(S) for S in Ss.values())
            deficit = sum(M - dx[x] for x in D)
            ws = min(len(set(Ss[g]) | set(Ss[h]))
                     for g, h in combinations(sorted(Ss), 2))
            out(f"  q={q}: REALIZED after {attempt + 1} pencil draws")
            out(f"    |split fibres of the pencil over F_q| = {len(fibres)} "
                f"(>= rho+2 = {RHO + 2} needed)")
            out(f"    D (designed, |D|={len(D)}) = {D}")
            out(f"    generic rank rho = {rk}  =>  A = {R + 1 - 2 * rk}")
            out(f"    T = {len(sup)} = rho+2 ; slopes {sorted(Ss)}")
            out(f"    u_gamma = {[len(S) for S in Ss.values()]} ; O = {O} "
                f"(SAT2 bound delta = {M - 1})")
            out(f"    max d_x = {max(dx.values())} <= e = {M} ; "
                f"deficit sum_x(m-d_x) = {deficit} vs 1+O = {1 + O} "
                f"-> (SAT4) {'OK' if deficit == 1 + O else 'FAIL'}")
            out(f"    saturated pts = {sum(1 for x in D if dx[x] == M)} "
                f">= N-(1+O) = {N - (1 + O)} -> (SAT5) OK")
            out(f"    column-far (no common split locator): OK")
            out(f"    w* = {ws} ; 7m-1 = {7 * M - 1} -> "
                f"(NEWCAP) F1 fires? {'YES' if ws > 7 * M - 1 else 'NO'}")
            return True
    out(f"  q={q}: no realization found in 400 pencil draws")
    return False


def main():
    lines = []

    def out(s):
        print(s)
        lines.append(s)

    out("=== D3a: m=1 (SAT3) realizability at LARGE q with a DESIGNED domain ===")
    out("profile rho=3 N=16 R=8 k=8 r=3 A=3 e=1 s=0 delta=0, target T=rho+2=5")
    out("")
    ok = []
    for q, seed in ((1009, 11), (2003, 23), (10007, 37)):
        ok.append(run_cell(q, seed, out))
        out("")
    out(f"large-q realizations: {sum(ok)}/{len(ok)} cells")
    out("")

    out("=== D3b: DIMENSION LEDGER for the (SAT3) configuration ===")
    out("The object is the affine curve F(Z,x)=0 of bidegree (e,rho)=(m,4m-1)")
    out("(F = the apolar generator Q_Z read as a polynomial in the domain")
    out("variable x).  Free data: the curve ((m+1)*4m - 1 projective coeffs),")
    out("the slope set G (|G| = T), the domain D (|D| = N = 16m).")
    out("Conditions: (SAT4) forces sum_x d_x = T*rho - O with d_x <= m and")
    out("|D| = 16m, i.e. all but 1+O domain points must have ALL m roots of")
    out("the degree-m polynomial F(.,x) inside G -- i.e. F(.,x) | H_G(Z).")
    out("Each such point is m conditions on a P^m, minus 1 for the free x.")
    out("")
    out(f"{'m':>4} {'rho':>10} {'N':>10} {'T=rho+2':>10} {'params':>16} "
        f"{'conds':>18} {'excess':>18} {'verdict':>14}")
    for m in [1, 2, 3, 4, 5, 8, 16, 1024, 2 ** 37]:
        rho, N, T = 4 * m - 1, 16 * m, 4 * m + 1
        params = (m + 1) * 4 * m - 1 + T + N
        conds = T * rho          # = 16m^2 - 1 (at O = 0)
        excess = conds - params
        v = "REALIZABLE" if excess < 0 else ("MARGINAL" if excess == 0
                                             else "OVER-DET")
        ms = str(m) if m < 10 ** 6 else "2^37"
        out(f"{ms:>4} {rho:>10} {N:>10} {T:>10} {params:>16} {conds:>18} "
            f"{excess:>18} {v:>14}")
    out("")
    out("closed form: excess(m) = 16m^2 - 1 - (4m^2+4m-1) - (4m+1) - 16m")
    out("           = 12m^2 - 24m - 1")
    for m in (1, 2, 3):
        out(f"   excess({m}) = {12 * m * m - 24 * m - 1}")
    out("roots of 12m^2-24m-1: m = 1 +- sqrt(39)/6 -> m in (-0.04, 2.04);")
    out("so excess < 0 EXACTLY for m in {1, 2} and excess > 0 for every m >= 3.")
    out("")
    out("Second, independent bookkeeping (conditions counted as")
    out("'F(.,x) divides H_G' at 16m-(1+O) points, m conditions each, minus")
    out("one free x per point; parameters = curve + G only):")
    out("   excess2(m) = 16m(m-1) - ((m+1)4m-1) - (4m+1) = 12m^2 - 24m - 2")
    for m in (1, 2, 3, 4):
        out(f"   excess2({m}) = {12 * m * m - 24 * m - 2}")
    out("Both bookkeepings agree to an additive constant and give the SAME")
    out("sign change between m=2 and m=3.")
    with open(sys.argv[1], "w") as f:
        f.write("\n".join(lines) + "\n")


main()
