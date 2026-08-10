"""D2: the COMPLETE structured-family census, graded by moving degree k,
with counting-layer status per family; and the RIG sweep that locates the
rigid/floppy transition.

For a collinear family {P_{S_1},...,P_{S_M}} put G = union S_i and
psi_i = sigma_{G\\S_i} (the COMPLEMENTARY locator).  Registered invariant:

    pdim := dim span{ psi_i }        (2 <=> the family is a PENCIL)
    k    := |G| - s                  (the moving degree)

R2 predicts: RIG = a-1-2s >= 0  ==>  pdim = 2 for EVERY family,
S_i subset S_1 u S_2, the psi_i are disjoint fibres of a degree-k map,
and hence M <= 1 + s/k <= s+1.  Counting-layer status: d_x = M on
cap S_i (if nonempty) else d_x = M-1 on G; so no family beats e+1.

Stdlib only.  Run under tools/ramguard.
"""
import itertools
import random
import sys
from math import comb

from d1_unify import (subgroup, sigma_prime, pointP, plucker, line_census,
                      Inv, say)


def poly_from_roots(R, q):
    p = [1]
    for r in R:
        n = [0] * (len(p) + 1)
        for i, c in enumerate(p):
            n[i] = (n[i] - c * r) % q
            n[i + 1] = (n[i + 1] + c) % q
        p = n
    return p


def rank(rows, ncols, q):
    M = [r[:] + [0] * (ncols - len(r)) for r in rows]
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, len(M)):
            if M[i][c]:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][c], q - 2, q)
        M[r] = [(v * iv) % q for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(x - f * y) % q for x, y in zip(M[i], M[r])]
        r += 1
        if r == len(M):
            break
    return r


def family_stats(fam, s, q):
    Ss = [frozenset(S) for S in fam]
    M = len(Ss)
    G = set()
    for S in Ss:
        G |= S
    k = len(G) - s
    psis = [poly_from_roots(sorted(G - S), q) for S in Ss]
    pdim = rank(psis, k + 1, q)
    cnt = {}
    for S in Ss:
        for x in S:
            cnt[x] = cnt.get(x, 0) + 1
    inter = set(Ss[0])
    for S in Ss[1:]:
        inter &= S
    fib = [tuple(sorted(G - S)) for S in Ss]
    seen, disj = set(), True
    for f in fib:
        if set(f) & seen:
            disj = False
        seen |= set(f)
    # Galois test for k=2 fibres: constant product (dihedral / twin coset)
    gal = ""
    if k == 2 and all(len(f) == 2 for f in fib):
        prods = {f[0] * f[1] % q for f in fib}
        sums = {(f[0] + f[1]) % q for f in fib}
        if len(prods) == 1:
            gal = "DIHEDRAL(uv=%d)" % prods.pop()
        elif sums == {0}:
            gal = "COSET(mu_2)"
        else:
            gal = "non-Galois"
    return dict(M=M, k=k, pdim=pdim, dmax=max(cnt.values()), inter=len(inter),
                disj=disj, gal=gal, Gsz=len(G))


def census(q, N, a, s, Vidx=None, tag="", show=True):
    inv = Inv(q)
    D = subgroup(N, q)
    V = [D[i] for i in (Vidx if Vidx is not None else range(a))]
    rest = [x for x in D if x not in V]
    spv = sigma_prime(V, q)
    pt2S, P = {}, []
    for S in itertools.combinations(rest, s):
        p = pointP(S, V, spv, q, inv)
        if p in pt2S:
            pt2S[p].append(S)
        else:
            pt2S[p] = [S]
            P.append(p)
    F, lines = line_census(P, q, a, inv)
    byk, spor, galtab = {}, [], {}
    viol_bound = viol_count = 0
    for ln in lines:
        fam = [pt2S[P[i]][0] for i in ln]
        st = family_stats(fam, s, q)
        key = st["k"]
        rec = byk.setdefault(key, dict(n=0, Mmax=0, dmaxmax=0))
        rec["n"] += 1
        rec["Mmax"] = max(rec["Mmax"], st["M"])
        rec["dmaxmax"] = max(rec["dmaxmax"], st["dmax"])
        if st["pdim"] != 2:
            spor.append(st)
        else:
            if st["M"] * st["k"] > st["Gsz"]:
                viol_bound += 1
        if st["dmax"] not in (st["M"], st["M"] - 1):
            viol_count += 1
        if st["gal"]:
            galtab[st["gal"]] = galtab.get(st["gal"], 0) + 1
    rig = a - 1 - 2 * s
    smax = max([x["M"] for x in spor], default=0)
    if show:
        say("  %-5s q=%-6d N=%-3d a=%-3d s=%-2d RIG=%-4d #pts=%-6d "
            "F_COLL=%-4d s+1=%-3d | pencil-lines=%-7d NON-PENCIL(pdim>2)=%-6d "
            "maxM(non-pencil)=%-4d | M*k>|G| viol=%d  d_x-law viol=%d"
            % (tag, q, N, a, s, rig, len(P), F, s + 1,
               sum(r["n"] for r in byk.values()) - len(spor), len(spor),
               smax, viol_bound, viol_count))
        if byk:
            say("        by moving degree k: %s"
                % "  ".join("k=%d:{n=%d,Mmax=%d,dmax=%d,bound 1+s/k=%.1f}"
                            % (k, r["n"], r["Mmax"], r["dmaxmax"], 1 + s / k)
                            for k, r in sorted(byk.items())))
        if galtab:
            say("        k=2 fibre types: %s" % sorted(galtab.items()))
    return dict(F=F, rig=rig, npts=len(P), nspor=len(spor), smax=smax,
                byk=byk, viol_bound=viol_bound, viol_count=viol_count)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "sweep"

    if mode == "sweep":
        say("=== D2 : RIG SWEEP -- F_COLL vs RIG = a-1-2s (N=16, two fields) ===")
        say("    R2 predicts F_COLL = s+1 and ZERO non-pencil families "
            "for RIG >= 0")
        tot_v = 0
        for q in (97, 65537):
            for s in (2, 3, 4, 5):
                for a in range(3, min(2 * s + 4, 16 - s) + 1):
                    if comb(16 - a, s) < 3:
                        continue
                    r = census(q, 16, a, s, tag="S%d" % s)
                    tot_v += r["viol_bound"] + r["viol_count"]
            say()
        say("  TOTAL structure-theorem violations across the sweep: %d" % tot_v)
        say()

    if mode == "n32":
        say("=== D2 : N=32 census (two fields) ===")
        for q in (97, 65537):
            for (a, s) in ((3, 2), (5, 2), (6, 2), (7, 3), (8, 3)):
                census(q, 32, a, s, tag="N32")
            say()

    if mode == "decay":
        say("=== D2/D3 : the NON-PENCIL (true sporadic) count vs q at the "
            "boundary RIG=-1 and RIG=-2, random V ===")
        say("    (a,s) = (6,3) is apolar's m=1 cell [RIG=-1]; "
            "(8,4) [RIG=-1]; (7,4) [RIG=-2]")
        for (a, s) in ((6, 3), (8, 4), (7, 4)):
            say("  --- N=16 a=%d s=%d RIG=%d ---" % (a, s, a - 1 - 2 * s))
            for q in (17, 97, 113, 193, 241, 65537):
                if (q - 1) % 16:
                    continue
                random.seed(20260810)
                D = subgroup(16, q)
                tot = totmax = 0
                nV = 8
                for _ in range(nV):
                    idx = sorted(random.sample(range(16), a))
                    r = census(q, 16, a, s, Vidx=idx, show=False)
                    tot += r["nspor"]
                    totmax = max(totmax, r["smax"])
                say("     q=%-6d  mean non-pencil lines per V = %8.4f   "
                    "max non-pencil family = %d   (%d random V)"
                    % (q, tot / nV, totmax, nV))
        say()
    say("=== END d2_census ===")
