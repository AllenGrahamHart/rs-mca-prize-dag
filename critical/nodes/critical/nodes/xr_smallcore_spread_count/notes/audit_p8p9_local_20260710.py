#!/usr/bin/env python3
"""Local (non-Modal) exact replay of the F5 bookkeeping instruments consumed by
the proposed xr_smallcore amber assembly, plus the elementary lemmas the
assembly labels PROVED.

Row: D = first n nonzero elements of F_q, q=97 prime; codewords = deg<k polys.
Official shape: k = n/2, A = k+2 (t=2) as in the shipped Modal replays
(f5_p8_lineray_saturation_modal.py, f5_p9_wcollision_pair_moment_modal.py),
plus a t=3 variant as an off-boundary control for the general-t claims.

Checks (all exact integer/field arithmetic):
  I1  per-word saturation identity   Cen(U_z; m) = sum_c C(s_c, m)
  I2  line identity                  sum_z Cen(U_z; m) = sum_rays C(s,m)
  I3  W-scan corollary               sum_{|W|=k} #rays through W = sum_rays C(s,k)
  T1  pair-moment identity           sum_W C(mult(W),2) = sum_{cross pairs} C(J,k)
  T2  fiber structure                supp ^ supp' == JointAgr(f,g) exactly
  T3  regroup                        moment = sum_(f,g) C(L,2)*C(J,k), L recomputed
  T4  pencil collapse                mult(W) == L(P_W, Q_W) for every k-set W
  F1  rung-2b two-slope forcing      exhaustive: every distinct-slope ray pair
                                     with |core| >= k+1 forces (u,v)|core to a
                                     codeword pair (and validity: if v|core is a
                                     deg<k restriction the pair-tangent event is
                                     visible as joint agreement)
  S1  sunflower cap                  per-W ray multiplicity <= (n-k)/(t-d) with
                                     d = #pencil-degenerate points of W
  H1  high-core counting implication #high-core rays <= 2 * sum_W C(mult,2)
                                     (the assembly step consuming predicate P-A)

Rays here: (z, c) with s_{z,c} = |{x: U_z(x)=c(x)}| >= A (raw rays, as in the
shipped P9 replay; strips are applied only where a check says so).
"""
import itertools, random
random.seed(20260710)

q = 97
def inv(a): return pow(a, q-2, q)

def interp_coeffs(xs, ys, k):
    """Return coefficients (len k) of the unique deg<k poly through the k
    points (xs, ys), via Lagrange, reduced mod q. len(xs) == k."""
    coeff = [0]*k
    for i in range(k):
        # numerator poly prod_{j!=i}(X - x_j)
        num = [1]
        for j in range(k):
            if j == i: continue
            num = polymul(num, [(-xs[j]) % q, 1])
        den = 1
        for j in range(k):
            if j == i: continue
            den = den * ((xs[i]-xs[j]) % q) % q
        w = ys[i]*inv(den) % q
        for d_ in range(len(num)):
            coeff[d_] = (coeff[d_] + w*num[d_]) % q
    return tuple(coeff)

def polymul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i+j] = (out[i+j] + ai*bj) % q
    return out

def evalp(c, x):
    r = 0
    for co in reversed(c):
        r = (r*x + co) % q
    return r

FAILS = []
def chk(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + (f"  [{detail}]" if detail else ""))
    if not ok: FAILS.append(label)

def run_row(n, k, t, pairs_spec):
    A = k + t
    D = list(range(1, n+1))
    print(f"\n== row n={n}, k={k}, t={t}, A={A}, q={q} ==")
    Wsets = list(itertools.combinations(range(n), k))
    for name, (u, v) in pairs_spec:
        # rays via W-scan: every support of size >= A contains a k-set
        rays = {}
        for z in range(q):
            Uz = [(u[i] + z*v[i]) % q for i in range(n)]
            seen = set()
            for W in Wsets:
                c = interp_coeffs([D[i] for i in W], [Uz[i] for i in W], k)
                if c in seen: continue
                seen.add(c)
                s = sum(1 for i in range(n) if evalp(c, D[i]) == Uz[i])
                if s >= A:
                    supp = frozenset(i for i in range(n) if evalp(c, D[i]) == Uz[i])
                    rays[(z, c)] = supp
        raylist = list(rays.items())
        # I1/I2: censuses. Cen(U_z; m) = #{|T|=m : U_z|_T extends to a codeword}
        m = A
        lhs_line = 0
        i1_ok = True
        for z in range(q):
            Uz = [(u[i] + z*v[i]) % q for i in range(n)]
            cen = 0
            for T in itertools.combinations(range(n), m):
                c = interp_coeffs([D[i] for i in T[:k]], [Uz[i] for i in T[:k]], k)
                if all(evalp(c, D[i]) == Uz[i] for i in T[k:]):
                    cen += 1
            rhs = sum(comb(len(s), m) for (zz, c), s in rays.items() if zz == z)
            if cen != rhs: i1_ok = False
            lhs_line += cen
        chk(f"{name}: I1 per-word saturation identity at m={m} (all {q} words)", i1_ok)
        rhs_line = sum(comb(len(s), m) for s in rays.values())
        chk(f"{name}: I2 line identity", lhs_line == rhs_line,
            f"{lhs_line}=={rhs_line}")
        # I3 + mult(W)
        mult = {}
        for (z, c), s in rays.items():
            for W in itertools.combinations(sorted(s), k):
                mult[W] = mult.get(W, 0) + 1
        lhs3 = sum(mult.values())
        rhs3 = sum(comb(len(s), k) for s in rays.values())
        chk(f"{name}: I3 W-scan corollary", lhs3 == rhs3, f"{lhs3}=={rhs3}")
        # T1
        lhsT1 = sum(comb(mm, 2) for mm in mult.values())
        rhsT1 = 0
        cross = []
        for a in range(len(raylist)):
            for b in range(a+1, len(raylist)):
                (z1, c1), s1 = raylist[a]
                (z2, c2), s2 = raylist[b]
                if z1 == z2: continue
                J = len(s1 & s2)
                cross.append((a, b, J))
                if J >= k: rhsT1 += comb(J, k)
        chk(f"{name}: T1 pair-moment identity", lhsT1 == rhsT1,
            f"{lhsT1}=={rhsT1}")
        # T2 on every cross pair with J >= 1
        t2_ok = True
        for a, b, J in cross:
            (z1, c1), s1 = raylist[a]
            (z2, c2), s2 = raylist[b]
            dz = (z1 - z2) % q
            g = tuple((c1[i]-c2[i]) * inv(dz) % q for i in range(k))
            f = tuple((c1[i] - z1*g[i]) % q for i in range(k))
            ja = frozenset(i for i in range(n)
                           if evalp(f, D[i]) == u[i] and evalp(g, D[i]) == v[i])
            if ja != (s1 & s2): t2_ok = False
        chk(f"{name}: T2 fiber structure (all {len(cross)} cross pairs)", t2_ok)
        # T3: regroup by (f,g) fibers; L recomputed independently as the number
        # of slopes z such that (z, f + z*g) is a ray of (u,v)
        fibers = {}
        for a, b, J in cross:
            if J < k: continue
            (z1, c1), s1 = raylist[a]
            (z2, c2), s2 = raylist[b]
            dz = (z1 - z2) % q
            g = tuple((c1[i]-c2[i]) * inv(dz) % q for i in range(k))
            f = tuple((c1[i] - z1*g[i]) % q for i in range(k))
            fibers.setdefault((f, g), []).append((a, b))
        rhsT3 = 0
        t3_ok = True
        for (f, g), plist in fibers.items():
            L = 0
            for z in range(q):
                c = tuple((f[i] + z*g[i]) % q for i in range(k))
                if (z, c) in rays: L += 1
            ja = frozenset(i for i in range(n)
                           if evalp(f, D[i]) == u[i] and evalp(g, D[i]) == v[i])
            J = len(ja)
            if len(plist) != comb(L, 2): t3_ok = False
            rhsT3 += comb(L, 2) * comb(J, k)
        chk(f"{name}: T3 regroup (per-fiber pair count = C(L,2))", t3_ok)
        chk(f"{name}: T3 regroup total equals T1", rhsT3 == lhsT1,
            f"{rhsT3}=={lhsT1}")
        # T4: mult(W) == L(P_W, Q_W) for EVERY k-set W (incl. mult 0)
        t4_ok = True
        for W in Wsets:
            P = interp_coeffs([D[i] for i in W], [u[i] for i in W], k)
            Q = interp_coeffs([D[i] for i in W], [v[i] for i in W], k)
            L = 0
            for z in range(q):
                c = tuple((P[i] + z*Q[i]) % q for i in range(k))
                if (z, c) in rays:
                    # sanity: the pencil ray necessarily passes through W
                    assert set(W) <= rays[(z, c)]
                    L += 1
            if L != mult.get(W, 0): t4_ok = False
        chk(f"{name}: T4 mult(W) == L(P_W,Q_W) for all C({n},{k}) k-sets", t4_ok)
        # F1: exhaustive rung-2b forcing on cross pairs with core >= k+1
        f1_ok = True
        n_forced = 0
        for a, b, J in cross:
            if J < k+1: continue
            n_forced += 1
            (z1, c1), s1 = raylist[a]
            (z2, c2), s2 = raylist[b]
            core = sorted(s1 & s2)
            dz = (z1 - z2) % q
            gv = tuple((c1[i]-c2[i]) * inv(dz) % q for i in range(k))
            fu = tuple((c1[i] - z1*gv[i]) % q for i in range(k))
            if not all(evalp(fu, D[i]) == u[i] and evalp(gv, D[i]) == v[i]
                       for i in core):
                f1_ok = False
        chk(f"{name}: F1 rung-2b forcing on all core>=k+1 cross pairs",
            f1_ok, f"{n_forced} forced pairs")
        # S1: sunflower cap per W: mult(W) <= (n-k)/(t-d), d = #degenerate pts
        s1_ok = True
        worst = 0
        for W, mm in mult.items():
            if mm < 2: continue
            P = interp_coeffs([D[i] for i in W], [u[i] for i in W], k)
            Q = interp_coeffs([D[i] for i in W], [v[i] for i in W], k)
            d_ = sum(1 for i in range(n) if i not in W
                     and evalp(Q, D[i]) == v[i] and evalp(P, D[i]) == u[i])
            if t - d_ <= 0:  # tangent event; cap not claimed (charged to strip)
                continue
            cap = (n - k) // (t - d_)
            worst = max(worst, mm)
            if mm > cap: s1_ok = False
        chk(f"{name}: S1 sunflower cap mult(W) <= (n-k)/(t-d) on non-tangent W",
            s1_ok, f"max mult={worst}, cap(n-k)/t={(n-k)//t}")
        # H1: high-core counting implication (assembly step 5)
        # high-core rays: rays sharing >= k core with another DISTINCT-slope ray
        hc = set()
        for a, b, J in cross:
            if J >= k:
                hc.add(a); hc.add(b)
        moment = lhsT1
        chk(f"{name}: H1 #high-core rays <= 2 * moment",
            len(hc) <= 2*moment, f"{len(hc)} <= 2*{moment}")

from math import comb

def mk_pair(n, kind, k):
    if kind == "random":
        return ([random.randrange(q) for _ in range(n)],
                [random.randrange(1, q) for _ in range(n)])
    if kind == "nearpencil":
        c0 = [random.randrange(q) for _ in range(k)]
        w0 = [random.randrange(q) for _ in range(k)]
        z0 = random.randrange(1, q)
        D = list(range(1, n+1))
        u = [(evalp(tuple(c0), D[i]) + z0*evalp(tuple(w0), D[i])) % q for i in range(n)]
        v = [evalp(tuple(w0), D[i]) % q for i in range(n)]
        for _ in range(3):  # r=3 perturbation
            i = random.randrange(n)
            u[i] = (u[i] + random.randrange(1, q)) % q
            j = random.randrange(n)
            v[j] = (v[j] + random.randrange(1, q)) % q
        v = [vv if vv != 0 else 1 for vv in v]
        return u, v
    raise ValueError

# t=2 boundary row (the shipped replays' shape) and a t=3 control
n1, k1 = 12, 6
pairs1 = [(f"rand{i}", mk_pair(n1, "random", k1)) for i in range(3)] + \
         [(f"np{i}", mk_pair(n1, "nearpencil", k1)) for i in range(2)]
run_row(n1, k1, 2, pairs1)

n2, k2 = 10, 4
pairs2 = [(f"rand{i}", mk_pair(n2, "random", k2)) for i in range(2)] + \
         [(f"np{i}", mk_pair(n2, "nearpencil", k2)) for i in range(1)]
run_row(n2, k2, 3, pairs2)   # t=3: general-t control for T1-T3/F1/S1/H1

print()
print("FAILS:", len(FAILS))
print("XR_P8P9_LOCAL_" + ("PASS" if not FAILS else "FAIL"))
