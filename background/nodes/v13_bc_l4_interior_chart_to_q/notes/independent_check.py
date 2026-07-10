#!/usr/bin/env python3
"""INDEPENDENT proof-read verifier for cap25_v13_bc_l4_interior_chart_to_q.md.

Written from scratch (does not reuse the upstream verifier's code paths):
  - census test uses the FULL-DEGREE Lagrange interpolant (deg <= m-1) and a
    degree threshold, instead of upstream's fit-on-first-K-points method;
  - line-for-RS[k] / line-for-RS[K] use the pole-free degree characterization
    deg I_T < K  /  deg I_T <= K (proved equivalent in the log), so agreement
    with upstream's pole-system counts cross-validates the equivalence;
  - L4 table recomputed with a 400-bit-shift log2 (abs err ~3e-16);
  - adds checks the upstream verifier does NOT run: the F_7 exact-p instance,
    exact integer pigeonhole ceil == 9237104, exact ceil(C(n,m')/p^4217)==1,
    the anticode==K-subset-bound identity, 2t+1==w+1 packing feasibility,
    the 901x term ratio / 1.00111 top-term dominance / 2106x overcount /
    103799.20 dropped-figure reconstruction, and the section-4 honest-scope
    toy evidence (row-B even rays => base-valued zeta; row-A odd parts).

Pre-registered criteria: every gate is CONFIRM/REFUTE; any REFUTE falsifies
the corresponding note claim. Exact arithmetic everywhere except float log2
pins (tolerance stated per gate, always >= 100x the method error).
"""
import math, itertools
from math import comb
from fractions import Fraction

FAIL = []
def gate(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAIL.append(name)

def l2(N):
    if N <= 0: raise ValueError
    s = max(0, N.bit_length() - 400)
    return s + math.log2(N >> s) if s else math.log2(N)

# ======================================================================
# I1: L4 exact table, independent recomputation
# ======================================================================
print("=== I1: L4 exact table ===")
n, K, m = 131072, 65537, 69753
k = K - 1
w = m - K
p = 2**31 - 2**24 + 1
d1 = w + 2
mp = k + d1
q = p**6
gate("fixture: n=2^17", n == 2**17)
gate("fixture: K=2^16+1", K == 2**16 + 1)
gate("fixture: w=4216", w == 4216)
gate("fixture: p=2130706433", p == 2130706433)
gate("fixture: d1=4218, m'=69754=m+1, e=1", d1 == 4218 and mp == 69754 and mp - m == 1)
gate("fixture: d1-1 = w+1 = 4217", d1 - 1 == w + 1 == 4217)
gate("fixture: gcd(m,n)=1 (m odd, n=2^17)", math.gcd(m, n) == 1 and m % 2 == 1)
gate("fixture: n | p-1 (D exists as mult. coset size n)", (p - 1) % n == 0)

Cnm = comb(n, m); Cnmp = comb(n, mp)
lp = l2(p); l2Cnm = l2(Cnm)
gate("log2 p == 30.988684687 (9dp)", abs(lp - 30.988684687) < 5e-10, f"{lp:.9f}")
heur = l2Cnm - w * lp
gate("heuristic log2(C(n,m)/p^w) == 23.139009074 (== #361 a_4, 9dp)",
     abs(heur - 23.139009074) < 2e-9, f"{heur:.9f}")
# exact integer pigeonhole ceiling; #369 boundary-row 'ceil fiber floor' = 9237104
pig, rem = divmod(Cnm, p**w)
pig += (1 if rem else 0)
gate("EXACT pigeonhole ceil(C(n,m)/p^w) == 9237104 (#369 row d1=4217)", pig == 9237104, str(pig))
gate("ceil vs a_4 differ below print precision", abs(l2(pig) - heur) < 1e-6,
     f"log2(ceil)={l2(pig):.9f}")
# planted density and M_B(4218): EXACT ceil
gate("EXACT 1 <= C(n,m') < p^(d1-1)  => ceil density = 1", 1 <= Cnmp < p**(d1 - 1))
dens = l2(Cnmp) - (d1 - 1) * lp
gate("planted density == -8.035617 (6dp)", abs(dens - (-8.035617)) < 5e-7, f"{dens:.6f}")
MB = comb(mp, m) * 1
gate("M_B(4218) == 69754 == m+1 == C(m',m)", MB == 69754 == m + 1)
gate("log2 M_B == 16.089988 (#369 col)", abs(l2(MB) - 16.089988) < 5e-7, f"{l2(MB):.6f}")
gate("K-1 == 65536", K - 1 == 65536)
# rigidity/packing: t = floor(w/2); disjointness needs min sep >= 2t+1; rigidity gives w+1
t = w // 2
gate("packing feasibility: 2t+1 == w+1 (rigidity exactly meets Johnson radius)", 2 * t + 1 == w + 1)
Vt = sum(comb(m, i) * comb(n - m, i) for i in range(t + 1))
top = comb(m, t) * comb(n - m, t)
pack_full = l2Cnm - l2(Vt)
pack_one = l2Cnm - l2(top)
gate("packing full-ball == 103810.2369 (4dp)", abs(pack_full - 103810.2369) < 5e-4, f"{pack_full:.4f}")
gate("packing one-term == 103810.2385 (4dp)", abs(pack_one - 103810.2385) < 5e-4, f"{pack_one:.4f}")
gate("full-ball vs one-term differ only in 4th decimal (<0.01)", abs(pack_full - pack_one) < 0.01)
ratio_t = Fraction(comb(m, t) * comb(n - m, t), comb(m, t - 1) * comb(n - m, t - 1))
gate("term(t)/term(t-1) ~ 901", abs(float(ratio_t) - 901) < 1.0, f"{float(ratio_t):.2f}")
gate("V_t/top == 1.00111 (5dp)", abs(Vt / top - 1.00111) < 5e-6, f"{Vt/top:.5f}")
gate("(t+1)*top over-counts V_t by ~2106x", abs((t + 1) * top / Vt - 2106) < 2, f"{(t+1)*top/Vt:.1f}")
dropped = l2Cnm - l2((t + 1) * top)
gate("dropped draft figure reconstructed == 103799.20", abs(dropped - 103799.20) < 5e-3, f"{dropped:.4f}")
gate("dropped figure UNDER-states true ceiling (not a valid upper bound)", dropped < pack_full)
# anticode == 'every K-subset in <=1 member' bound, exact identity
gate("EXACT n-m+w == n-K (anticode arg identity)", n - m + w == n - K)
gate("EXACT C(n,m)*C(m,K) == C(n,K)*C(n-m+w,w)  [anticode = K-subset double count]",
     comb(n, m) * comb(m, K) == comb(n, K) * comb(n - m + w, w))
anti = l2Cnm - l2(comb(n - m + w, w))
gate("anticode == 108108.04 (2dp)", abs(anti - 108108.04) < 5e-3, f"{anti:.4f}")
gate("packing < anticode", pack_one < anti)
# depth-(w+1) reduction route: t' = floor((w+1)/2) = t (w even); within-fiber sep >= w+2 >= 2t'+1
tp = (w + 1) // 2
gate("t' == t (w even) and w+2 >= 2t'+1 (in-fiber packing feasible)", tp == t and w + 2 >= 2 * tp + 1)
red = lp + l2Cnm - l2(Vt)
gate("reduction+packing == 103841.23 (2dp)", abs(red - 103841.23) < 5e-3, f"{red:.4f}")
gate("reduction - direct == log2 p (pays |B| factor, ~31 bits)", abs((red - pack_full) - lp) < 1e-9)
thr = l2((q - p) // (K - 1) + 1)
gate("distinct-slope threshold == 169.93 (2dp)", abs(thr - 169.93) < 5e-3, f"{thr:.4f}")
rayf = heur - l2(m + 1)
gate("ray floor == 7.05 (heuristic - log2(m+1))", abs(rayf - 7.05) < 5e-3, f"{rayf:.4f}")
gate("slope floor == 6.05 (ray floor - 1)", abs((rayf - 1) - 6.05) < 5e-3)
gate("gap packing-heuristic ~ 103787 bits", abs((pack_one - heur) - 103787.10) < 5e-2,
     f"{pack_one-heur:.2f}")
coll = math.log2(0.5) + 2 * heur + math.log2(K - 1) - l2(q - p)
gate("collisions at heuristic N == -124.65 (2dp)", abs(coll - (-124.65)) < 5e-3, f"{coll:.4f}")
gate("c.2 arithmetic: K=65537 < n-2w = 122640", K < n - 2 * w == 122640)
l4K = l2Cnm - (w - 1) * lp
gate("line-for-RS[K] heuristic == 54.127694 == log2 p + 23.139009", abs(l4K - 54.127694) < 5e-7
     and abs(l4K - (lp + heur)) < 1e-9, f"{l4K:.6f}")
# Lemma A2 degree bookkeeping, symbolic-exact at fixture values
gate("Lemma A2: m'-(d1-1)-1 == K-1 < m", mp - (d1 - 1) - 1 == K - 1 and K - 1 < m)
gate("rigidity: m-(K-1) == w+1", m - (K - 1) == w + 1)
gate("lattice: d1+d2 == n-K+1 with d2=deg S=n-m'", d1 + (n - mp) == n - K + 1 and n - mp == 61318)
gate("lattice: omega=n-m => omega-d1==57101 and omega-d2==1 (deg B<=1 forced)",
     (n - m) - d1 == 57101 and (n - m) - (n - mp) == 1)

# ======================================================================
# shared exact GF(p) polynomial helpers (fresh implementations)
# ======================================================================
def pmul(a, b, P):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % P
    while len(r) > 1 and r[-1] == 0: r.pop()
    return r

def norm(a):
    a = [x for x in a]
    while len(a) > 1 and a[-1] == 0: a.pop()
    return a

def pev(a, x, P):
    r = 0
    for c in reversed(a): r = (r * x + c) % P
    return r

def newton_interp(xs, ys, P):
    nn = len(xs)
    dd = list(ys)
    for j in range(1, nn):
        for i in range(nn - 1, j - 1, -1):
            dd[i] = (dd[i] - dd[i - 1]) * pow((xs[i] - xs[i - j]) % P, P - 2, P) % P
    poly = [dd[nn - 1] % P]
    for i in range(nn - 2, -1, -1):
        poly = pmul(poly, [(-xs[i]) % P, 1], P)
        poly[0] = (poly[0] + dd[i]) % P
    return norm(poly)

def ell_of(T, P):
    r = [1]
    for x in T: r = pmul(r, [(-x) % P, 1], P)
    return r

def rank_mod(rows, P):
    M = [r[:] for r in rows]
    nr = len(M); nc = len(M[0]) if M else 0
    rk = 0
    for c in range(nc):
        piv = next((i for i in range(rk, nr) if M[i][c] % P), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        inv = pow(M[rk][c], P - 2, P)
        M[rk] = [(x * inv) % P for x in M[rk]]
        for i in range(nr):
            if i != rk and M[i][c] % P:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[rk][j]) % P for j in range(nc)]
        rk += 1
    return rk

def module_d1_indep(U, Kk, nn, beta, P, dmax):
    """min d with nonzero (W,N), deg W<=d, deg N<=d+Kk-1, W*U==N mod X^nn-beta."""
    for d_ in range(dmax + 1):
        cols = []
        for i in range(d_ + 1):                      # column for w_i: X^i*U reduced
            prod = [0] * i + list(U)
            prod = [x % P for x in prod]
            while len(prod) > nn:
                c0 = prod.pop()
                if c0:
                    sh = len(prod) - nn
                    prod[sh] = (prod[sh] + c0 * beta) % P
            v = [0] * nn
            for idx, x in enumerate(prod): v[idx] = x % P
            cols.append(v)
        for j_ in range(d_ + Kk):                    # column for -n_j
            v = [0] * nn
            v[j_] = P - 1
            cols.append(v)
        rows = [[cols[c][r] for c in range(len(cols))] for r in range(nn)]
        if rank_mod(rows, P) < len(cols):
            return d_
    return None

# ======================================================================
# I2: toy rows A/B, fully independent enumeration
# ======================================================================
def run_row(label, P, nn, Kk, mm, ww, d1_, mp_, zst, expect):
    print(f"=== I2: toy row {label} (p={P},n={nn},K={Kk},m={mm},w={ww},m'={mp_},z*={zst}) ===")
    D = sorted(x for x in range(1, P) if pow(x, nn, P) == 1)
    assert len(D) == nn
    Dset = set(D)
    U = [0] * (mp_ + 1); U[mp_] = 1
    for h, z in enumerate(zst, 1): U[mp_ - h] = z % P
    U = norm(U)
    gate(f"{label}: U has no coefficient below X^K", all(c == 0 for c in U[:Kk]))

    valid, fib, mismatch, facmm = [], {}, 0, 0
    rays = {}
    strata = {"planted": 0, "primitive": 0, "degenerate": 0}
    for T in itertools.combinations(D, mm):
        ell = ell_of(T, P)
        a = [ell[mm - i] % P if 0 <= mm - i < len(ell) else 0 for i in range(ww + 2)]
        fib.setdefault(tuple(a[1:ww + 2]), 0)
        fib[tuple(a[1:ww + 2])] += 1
        r = (a[1] - zst[0]) % P
        tw = all((a[j] - r * a[j - 1] - zst[j - 1]) % P == 0 for j in range(2, ww + 2))
        I = newton_interp(list(T), [pev(U, x, P) for x in T], P)     # deg <= m-1
        di = len(norm(I)) - 1 if norm(I) != [0] else -1
        direct = di < Kk
        if tw != direct:
            mismatch += 1
            continue
        if not tw: continue
        Psi = [( (U[i] if i < len(U) else 0) - (I[i] if i < len(I) else 0)) % P
               for i in range(max(len(U), len(I)))]
        Psi = norm(Psi)
        closed = pmul(ell, [(-r) % P, 1], P)
        if closed != Psi: facmm += 1
        S = tuple(x for x in D if pev(Psi, x, P) == 0)
        if r in Dset and r not in T: strata["planted"] += 1
        elif r not in Dset: strata["primitive"] += 1
        else: strata["degenerate"] += 1
        valid.append((tuple(T), a[1]))
        rays.setdefault(S, {"Psi": Psi, "mem": set()})["mem"].add(tuple(T))

    Cen = len(valid)
    gate(f"{label}: census(full-interpolant) == twisted on ALL {comb(nn,mm)} subsets (0 mismatch)",
         mismatch == 0)
    gate(f"{label}: Psi == ell_T*(X-r) exactly for every valid T (0 mismatch)", facmm == 0)
    gate(f"{label}: Cen == {expect['Cen']}", Cen == expect["Cen"], str(Cen))
    gate(f"{label}: rays == {expect['rays']}", len(rays) == expect["rays"], str(len(rays)))
    # Theorem
    def theta(s):
        r_ = (s - zst[0]) % P
        ph = [s % P]
        for j in range(2, ww + 2): ph.append((zst[j - 1] + r_ * ph[-1]) % P)
        return tuple(ph)
    sfib = sum(fib.get(theta(s), 0) for s in range(P))
    gate(f"{label}: THEOREM sum_s |Fib_(w+1)(theta(s))| == Cen", sfib == Cen, f"{sfib} vs {Cen}")
    mx = max(fib.values())
    gate(f"{label}: max fiber == {expect['maxf']}", mx == expect["maxf"], str(mx))
    gate(f"{label}: COROLLARY rays <= Cen <= p*maxfiber", len(rays) <= Cen <= P * mx)
    # saturation
    sat = sum(comb(len(S), mm) for S in rays)
    gate(f"{label}: SATURATION Cen == sum C(rt_D,m)", sat == Cen, f"{sat} vs {Cen}")
    memok = all(r_["mem"] == set(itertools.combinations(S, mm)) for S, r_ in rays.items())
    gate(f"{label}: per-ray members == all m-subsets of S_Psi", memok)
    gate(f"{label}: strata all planted == {expect['Cen']}",
         strata["planted"] == expect["Cen"] and strata["primitive"] == 0 and strata["degenerate"] == 0,
         str(strata))
    # rigidity + collision caps
    keys = list(rays)
    seps, degs = [], []
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            Ti = next(iter(rays[keys[i]]["mem"])); Tj = next(iter(rays[keys[j]]["mem"]))
            seps.append(len(set(Ti) - set(Tj)))
            dif = norm([(x - y) % P for x, y in itertools.zip_longest(
                rays[keys[i]]["Psi"], rays[keys[j]]["Psi"], fillvalue=0)])
            degs.append(len(dif) - 1)
    gate(f"{label}: RIGIDITY min|T\\T'| == w+1 == {ww+1}", min(seps) == ww + 1, str(min(seps)))
    gate(f"{label}: COLLISION max deg(Psi-Psi') == K-1 == {Kk-1} (cap attained)",
         max(degs) == Kk - 1, str(max(degs)))
    # module d1
    dfound = module_d1_indep(U, Kk, nn, 1, P, ww + 4)
    gate(f"{label}: module d1(U) == w+2 == {ww+2}", dfound == ww + 2, str(dfound))
    # planted bijection
    mpfib = set()
    for Mp in itertools.combinations(D, mp_):
        ee = ell_of(Mp, P)
        if all(ee[mp_ - h] % P == zst[h - 1] % P for h in range(1, d1_)):
            mpfib.add(Mp)
    planted_rays = set(S for S in rays if len(S) == mp_)
    gate(f"{label}: planted rays <-> prefix-z* m'-subsets (bijection, {expect['praw']})",
         planted_rays == mpfib and len(mpfib) == expect["praw"],
         f"{len(planted_rays)} vs {len(mpfib)}")
    # convention pin via pole-free degree characterization
    lk = lK = 0
    census_set = set(v[0] for v in valid)
    lk_set, lK_set = set(), set()
    for T in itertools.combinations(D, mm):
        I = newton_interp(list(T), [pev(U, x, P) for x in T], P)
        dI = len(norm(I)) - 1 if norm(I) != [0] else -1
        if dI < Kk: lk_set.add(T)
        if dI <= Kk: lK_set.add(T)
    gate(f"{label}: line-for-RS[k] == word census (== {expect['Cen']})",
         lk_set == census_set and len(lk_set) == expect["Cen"])
    gate(f"{label}: |line-for-RS[K]| == {expect['lineK']} and census strict subset",
         len(lK_set) == expect["lineK"] and census_set < lK_set, str(len(lK_set)))
    return rays, U, D

raysA, UA, DA = run_row("A", 97, 16, 4, 6, 2, 4, 7, [96, 1, 96],
                        dict(Cen=21, rays=3, maxf=3, praw=3, lineK=105))
raysB, UB, DB = run_row("B", 97, 16, 5, 7, 2, 4, 8, [0, 0, 0],
                        dict(Cen=48, rays=6, maxf=3, praw=6, lineK=144))

# ======================================================================
# I3: F_7 instance (upstream verifier does NOT run this; note cites D2 toy)
# ======================================================================
print("=== I3: F_7 exact-p convention instance ===")
P7 = 7; D7 = list(range(1, 7)); m7, K7, mp7 = 4, 2, 5
tot_cen = tot_lK = 0
subset_ok = True
for z1 in range(7):
    for z2 in range(7):
        for z3 in range(7):
            U7 = [0, 0, z3, z2, z1, 1]
            cs, ls = set(), set()
            for T in itertools.combinations(D7, m7):
                I = newton_interp(list(T), [pev(U7, x, P7) for x in T], P7)
                dI = len(norm(I)) - 1 if norm(I) != [0] else -1
                if dI < K7: cs.add(T)
                if dI <= K7: ls.add(T)
            tot_cen += len(cs); tot_lK += len(ls)
            if not cs.issubset(ls): subset_ok = False
gate("F_7: total census over all 343 prefixes == 105  (avg == 15/7^2 exactly)",
     tot_cen == 105 and Fraction(tot_cen, 343) == Fraction(15, 49), str(tot_cen))
gate("F_7: total line-for-RS[K] == 735  (avg == 15/7 exactly)",
     tot_lK == 735 and Fraction(tot_lK, 343) == Fraction(15, 7), str(tot_lK))
gate("F_7: ratio EXACTLY p == 7", Fraction(tot_lK, tot_cen) == 7)
gate("F_7: census subset of RS[K]-line on every prefix", subset_ok)

# ======================================================================
# I4: section-4 honest-scope toy evidence (zeta base/extension-valued)
# ======================================================================
print("=== I4: honest-scope evidence (per-slope zeta membership) ===")
# Row B: all rays Psi even (supports negation-closed) => zeta=(U-Psi)(alpha) in B
# whenever alpha^2 in B (U-Psi even, deg<=K-1).
evenB = all(all(c == 0 for i, c in enumerate(r_["Psi"]) if i % 2 == 1) for r_ in raysB.values())
negcl = all(set((-x) % 97 for x in S) == set(S) for S in raysB)
gate("row B: every ray Psi is an EVEN polynomial (supports negation-closed)",
     evenB and negcl)
gate("row B: hence zeta base-valued at any alpha with alpha^2 in B (num_ext_valued == 0)", evenB)
# Row A: Delta = U - Psi (deg<=K-1=3); zeta at alpha=sqrt(g) is in B iff odd part
# of Delta vanishes at g. Check over ALL quadratic non-residues g.
odd_ok_all_g = True
nonres = [g for g in range(1, 97) if pow(g, 48, 97) == 96]
for r_ in raysA.values():
    Dlt = norm([((UA[i] if i < len(UA) else 0) - (r_["Psi"][i] if i < len(r_["Psi"]) else 0)) % 97
                for i in range(max(len(UA), len(r_["Psi"])))])
    d1c = Dlt[1] if len(Dlt) > 1 else 0
    d3c = Dlt[3] if len(Dlt) > 3 else 0
    for g in nonres:
        if (d1c + d3c * g) % 97 == 0:
            odd_ok_all_g = False
gate("row A: every ray zeta EXTENSION-valued at alpha=sqrt(g) for ALL 48 non-residues g",
     odd_ok_all_g, f"rays={len(raysA)}, per-support values=21")

print(f"\n=== RESULT: {'ALL PASS' if not FAIL else 'FAILURES: ' + str(FAIL)} ===")
