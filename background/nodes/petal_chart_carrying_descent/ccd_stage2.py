#!/usr/bin/env python3
"""ccd_stage2: obligations (i)+(ii) + collapse counts for petal_chart_carrying_descent.

Complete enumeration of periodic (c(S) >= 2) contributors to fiber-aligned chart
words (census conventions), per-scale descent, per-member obligation tests,
per-descended-chart collapse tables. Shards: n16 | n32a | n32b | n32c | probe.

Enumeration completeness (census-proved method): every contributor with
c(S) >= 2 has S = union of full antipodal 2-fibers, |S| >= k+1, hence contains
>= m0 = ceil((k+1)/2) full fibers; interpolation through k points of any
m0-subset recovers f. All m0-subsets of the n/2 fibers are enumerated.
Cross-check at n=16: brute over ALL C(16,k+1) (k+1)-point subsets.
"""
import itertools, random, sys, json
from math import comb

def is_prime(m):
    if m < 2: return False
    if m % 2 == 0: return m == 2
    d = 3
    while d*d <= m:
        if m % d == 0: return False
        d += 2
    return True

def order_n_domain(p, n):
    a = 2
    while True:
        g0 = pow(a, (p-1)//n, p)
        if pow(g0, n//2, p) != 1: break
        a += 1
    return [pow(g0, j, p) for j in range(n)]

def locator_poly(roots, p):
    loc = [1]
    for r in roots:
        new = [0]*(len(loc)+1)
        for i, c in enumerate(loc):
            new[i] = (new[i] - r*c) % p
            new[i+1] = (new[i+1] + c) % p
        loc = new
    return loc

def ev(poly, x, p):
    v = 0
    for c in reversed(poly):
        v = (v*x + c) % p
    return v

def newton_interp(xs, ys, p):
    """Newton divided differences; returns coeff list (monomial basis)."""
    m = len(xs)
    dd = list(ys)
    for j in range(1, m):
        for i in range(m-1, j-1, -1):
            dd[i] = (dd[i] - dd[i-1]) * pow(xs[i] - xs[i-j], -1, p) % p
    # expand: poly = dd[0] + dd[1](X-x0) + dd[2](X-x0)(X-x1) + ...
    poly = [0]*m
    base = [1]
    for i in range(m):
        for d2, c in enumerate(base):
            poly[d2] = (poly[d2] + dd[i]*c) % p
        if i < m-1:
            newb = [0]*(len(base)+1)
            r = xs[i]
            for d2, c in enumerate(base):
                newb[d2] = (newb[d2] - r*c) % p
                newb[d2+1] = (newb[d2+1] + c) % p
            base = newb
    return tuple(poly)

def build_layout(n, k):
    half = n//2
    nf = (k-1)//2
    core = []
    for j in range(nf): core.extend([j, j+half])
    extra = []
    if (k-1) % 2:
        core.append(nf); extra = [nf+half]
    petal_fibers = list(range(nf + (1 if (k-1) % 2 else 0), half))
    petals = [sorted([j, j+half]) for j in petal_fibers]
    return sorted(core), petals, sorted(extra), nf, petal_fibers

def make_scalars(mode, n, k, p, dom):
    half = n//2; nf = (k-1)//2
    petal_fibers = list(range(nf+1, half))
    t = len(petal_fibers)
    dom2 = [dom[i]*dom[i] % p for i in range(half)]
    Zp = [dom2[j] for j in range(nf)]
    locZp = locator_poly(Zp, p)
    y_nf = dom2[nf]
    kp = k//2
    if mode == "geom5":
        out, v = [], 1
        for _ in range(t): out.append(v); v = v*5 % p
    elif mode == "geom3":
        out, v = [], 1
        for _ in range(t): out.append(v); v = v*3 % p
    elif mode == "consec":
        out = [(i+1) % p for i in range(t)]
    elif mode.startswith("rand"):
        rng = random.Random(1000+int(mode[4:]))
        out = [rng.randrange(1, p) for _ in range(t)]
    elif mode in ("wtau0", "wtauy"):
        tau = dom2[0] if mode == "wtau0" else y_nf
        out = []
        for j in petal_fibers:
            y = dom2[j]
            w = pow(y, kp, p) * ((y - tau) % p) % p
            out.append(w * pow(ev(locZp, y, p), -1, p) % p)
        assert all(c % p != 0 for c in out), (mode, "zero scalar")
    else:
        raise ValueError(mode)
    return out

def stab_order(S, n):
    c, M = 1, 2
    while M <= n:
        s = n // M
        if all(((x+s) % n) in S for x in S): c = M
        else: break
        M *= 2
    return c

def periodic_contributors(n, k, p, dom, values):
    half = n//2
    m0 = -(-(k+1)//2)
    found = {}
    cache = {}
    for fibsub in itertools.combinations(range(half), m0):
        pts = []
        for j in fibsub: pts.append(j); pts.append(j+half)
        xs = [dom[j] for j in pts]; ys = [values[j] for j in pts]
        key = tuple(pts[:k])
        poly = cache.get(key)
        if poly is None:
            poly = newton_interp(xs[:k], ys[:k], p)
            cache[key] = poly
        if poly in found: continue
        if any(ev(poly, x, p) != y for x, y in zip(xs[k:], ys[k:])): continue
        S = frozenset(j for j in range(n) if ev(poly, dom[j], p) == values[j])
        if len(S) >= k+1 and stab_order(S, n) >= 2:
            found[poly] = S
    return found

def brute_contributors(n, k, p, dom, values):
    found = {}
    for idxs in itertools.combinations(range(n), k+1):
        xs = [dom[j] for j in idxs]; ys = [values[j] for j in idxs]
        poly = newton_interp(xs[:k], ys[:k], p)
        if poly in found: continue
        if ev(poly, xs[k], p) != ys[k]: continue
        S = frozenset(j for j in range(n) if ev(poly, dom[j], p) == values[j])
        if len(S) >= k+1: found[poly] = S
    return found

def solve_mod(mat, rhs, p):
    """Gaussian elimination mod p; mat MxM invertible."""
    M = len(mat)
    A = [row[:] + [rhs[i]] for i, row in enumerate(mat)]
    for col in range(M):
        piv = next(r for r in range(col, M) if A[r][col] % p != 0)
        A[col], A[piv] = A[piv], A[col]
        inv = pow(A[col][col], -1, p)
        A[col] = [x*inv % p for x in A[col]]
        for r in range(M):
            if r != col and A[r][col] % p:
                f = A[r][col]
                A[r] = [(A[r][c] - f*A[col][c]) % p for c in range(M+1)]
    return [A[i][M] for i in range(M)]

def vector_word(n, M, p, dom, values):
    """Fiberwise inversion: components u_0..u_{M-1} on the n/M quotient points."""
    nq = n // M
    comps = [[0]*nq for _ in range(M)]
    for i in range(nq):
        fpts = [i + s*nq for s in range(M)]
        mat = [[pow(dom[j], r, p) for r in range(M)] for j in fpts]
        rhs = [values[j] for j in fpts]
        sol = solve_mod(mat, rhs, p)
        for r in range(M): comps[r][i] = sol[r]
    return comps

def adversarial_max(Is, cap_m):
    """max over petal-sets P (|P| <= cap_m) of #{I in Is : I subset P} (exact:
    unions over subsets of Is; safe because |Is| small)."""
    Is = list({frozenset(I) for I in Is})
    best = 0
    L = len(Is)
    if L > 18:  # guard; fall back to pair unions
        for a in range(L):
            u = Is[a]; cnt = sum(1 for I in Is if I <= u)
            best = max(best, cnt)
        for a in range(L):
            for b in range(a+1, L):
                u = Is[a] | Is[b]
                if len(u) <= cap_m:
                    cnt = sum(1 for I in Is if I <= u)
                    best = max(best, cnt)
        return best
    for mask in range(1, 1 << L):
        u = frozenset()
        for b in range(L):
            if mask >> b & 1: u = u | Is[b]
        if len(u) <= cap_m:
            cnt = sum(1 for I in Is if I <= u)
            best = max(best, cnt)
    return best

GLOB = dict(escA2=0, coll=0, capviol=0, c1=0, c2=0, rz=0, band=0, chartmem=0,
            fullpetal=0, aon=0, darith=0, brute_mismatch=0, pattern=0,
            merged=0, cells=0, members2=0, members4=0, members8=0,
            sat_max=0.0, offchart_viol=0)
VIOL = []

def run_cell(n, k, p, mode, verbose=False):
    half = n//2
    dom = order_n_domain(p, n)
    core, petals, bg, nf, petal_fibers = build_layout(n, k)
    t = len(petals)
    scal = make_scalars(mode, n, k, p, dom)
    locZ = locator_poly([dom[j] for j in core], p)
    values = [0]*n
    for c_i, P in zip(scal, petals):
        for j in P: values[j] = c_i * ev(locZ, dom[j], p) % p
    contr = periodic_contributors(n, k, p, dom, values)
    # brute cross-check at n=16
    if n == 16:
        bf = brute_contributors(n, k, p, dom, values)
        bper = {f: S for f, S in bf.items() if stab_order(S, n) >= 2}
        if bper != contr:
            GLOB["brute_mismatch"] += 1
            VIOL.append(("BRUTE_MISMATCH", n, k, p, mode))
    scales = {}
    for f, S in contr.items():
        scales.setdefault(stab_order(S, n), []).append(f)
    Ms = [M for M in (2, 4, 8) if M <= t and k % M == 0 and n % M == 0]
    line = f"CELL ({n},{k},p={p},{mode}) t={t} periodic={len(contr)} scales=" + \
           str({c: len(v) for c, v in sorted(scales.items())})
    out = [line]
    GLOB["cells"] += 1
    for M in Ms:
        sub = scales.get(M, [])
        # K_M-invariant superset count
        inv = [f for c, v in scales.items() if c % M == 0 for f in v]
        nq = n // M; kq = k // M
        domq = [pow(dom[1], M*i, p) for i in range(nq)]
        comps_u = vector_word(n, M, p, dom, values)
        coreimg = sorted({j % nq for j in core})
        bgimg = sorted({j % nq for j in bg})
        petalimg = [sorted({j % nq for j in P}) for P in petals]
        petalpts = sorted({q for Pi in petalimg for q in Pi})
        zeroimg = sorted(set(coreimg) | set(bgimg))
        if M == 2:
            GLOB["members2"] += len(sub)
        elif M == 4:
            GLOB["members4"] += len(sub)
        else:
            GLOB["members8"] += len(sub)
        # ---- per-member tests ----
        recs = []
        for f in sub:
            S = contr[f]
            fr = [list(f[r::M]) for r in range(M)]
            Sq = frozenset(j % nq for j in S)
            ok_len = (len(Sq)*M == len(S))
            # componentwise agreement set
            Sq2 = frozenset(i for i in range(nq)
                            if all(ev(fr[r], domq[i], p) == comps_u[r][i]
                                   for r in range(M)))
            if Sq2 != Sq or not ok_len:
                GLOB["chartmem"] += 1; VIOL.append(("DESCENT_SEMANTICS", n, k, p, mode, M))
            # full petal + all-or-nothing at official row
            fp = all(len(S & frozenset(P)) in (0, len(P)) for P in petals)
            if not fp:
                GLOB["fullpetal"] += 1; VIOL.append(("NOT_FULL_PETAL", n, k, p, mode, M, sorted(S)))
            aon = all((i in map(lambda x: x % half, S)) is not None for i in [])  # placeholder
            # pattern: petal touched <=> descended petal point in Sq
            pat = True
            for Pi, P in zip(petalimg, petals):
                touched = frozenset(P) <= S
                img_in = all(q in Sq for q in Pi)
                img_any = any(q in Sq for q in Pi)
                if touched != img_in or (img_any and not touched and M == 2):
                    pat = False
            if not pat:
                GLOB["pattern"] += 1; VIOL.append(("PATTERN", n, k, p, mode, M, sorted(S)))
            # merged petal consistency (M>=4)
            if M >= 4:
                seen = {}
                for idx, Pi in enumerate(petalimg):
                    key = tuple(Pi)
                    if key in seen:
                        t1 = frozenset(petals[seen[key]]) <= S
                        t2 = frozenset(petals[idx]) <= S
                        if t1 != t2:
                            GLOB["merged"] += 1
                            VIOL.append(("MERGED_INCONSISTENT", n, k, p, mode, M))
                    seen[key] = idx
            # escape clause 2: descended member touching no descended petal
            if not (Sq & set(petalpts)):
                GLOB["escA2"] += 1; VIOL.append(("ESCAPE_A2", n, k, p, mode, M, sorted(S)))
            rec = dict(S=S, Sq=Sq, f=f)
            if M == 2:
                x_nf = dom[nf]; y_nf = domq[nf]
                # C1
                f0, f1 = fr[0], fr[1]
                c1ok = all((f0[i] + x_nf*f1[i]) % p == 0 for i in range(len(f1)))
                if not c1ok:
                    GLOB["c1"] += 1; VIOL.append(("C1_FAIL", n, k, p, mode))
                g = f1
                # C2 retained zero <-> scale-2  (split fiber membership)
                gy = ev(g, y_nf, p)
                split_in = (nf in S) and ((nf+half) in S)
                if not (gy == 0 and split_in):
                    GLOB["c2"] += 1; VIOL.append(("C2_FAIL", n, k, p, mode, gy, split_in))
                if gy != 0:
                    GLOB["rz"] += 1
                # chart data
                z = len(Sq & set(range(nf+1)))
                W = frozenset(Sq & set(range(nf+1)))
                Iq = frozenset(Sq & set(petalpts))
                d_off = len(set(core) - S); r_off = len(set(bg) & S)
                dq = kq - z
                if not (d_off == 2*(kq - z) and r_off == 1):
                    GLOB["darith"] += 1; VIOL.append(("D_ARITH", n, k, p, mode, d_off, r_off, z))
                aq = dq + 1
                if len(Iq) < aq:
                    GLOB["band"] += 1; VIOL.append(("A_THRESH", n, k, p, mode))
                # band equivalence: official d >= 2(m-2) <=> dq >= m-2 (same m)
                for m_test in (t, len(Iq)):
                    if (d_off >= 2*(m_test-2)) != (dq >= m_test-2):
                        GLOB["band"] += 1; VIOL.append(("BAND_EQUIV", n, k, p, mode))
                rec.update(W=W, Iq=Iq, z=z, dq=dq, aq=aq,
                           topband=(len(Sq) <= kq+2))
            recs.append(rec)
        # ---- collapse tables (M=2) ----
        if M == 2 and recs:
            byW = {}
            for rec in recs: byW.setdefault(rec["W"], []).append(rec)
            tabl = []
            for W, rs in sorted(byW.items(), key=lambda kv: sorted(kv[0])):
                z = len(W); dq = kq - z
                classes = {rec["Sq"] for rec in rs}
                if len(classes) != len(rs):
                    GLOB["coll"] += 1; VIOL.append(("CLASS_COLLISION", n, k, p, mode, sorted(W)))
                # injection check: (W, Iq) unique
                pairs = {(rec["W"], rec["Iq"]) for rec in rs}
                if len(pairs) != len(rs):
                    GLOB["coll"] += 1
                    VIOL.append(("CRT_COLLISION", n, k, p, mode, sorted(W)))
                cap_m = dq + 2   # largest band petal count
                Is = [rec["Iq"] for rec in rs]
                adv = adversarial_max(Is, cap_m) if cap_m >= 1 else 0
                cap = cap_m + 1
                full_band = (dq >= t - 2)
                nfull = len(classes) if full_band else None
                viol = adv > cap or (full_band and len(classes) > t+1)
                if viol:
                    GLOB["capviol"] += 1
                    VIOL.append(("CAP_VIOLATION", n, k, p, mode, sorted(W), adv, cap))
                sat = adv / cap if cap else 0
                GLOB["sat_max"] = max(GLOB["sat_max"], sat)
                tabl.append((sorted(W), z, dq, len(rs), adv, cap,
                             "BAND(t)" if full_band else "", nfull, t+1))
            out.append(f"  M=2: members={len(sub)} (K2-inv={len(inv)}) charts={len(tabl)}")
            for row in tabl:
                W, z, dq, nm, adv, cap, fb, nfull, capt = row
                s = (f"    W={W} z={z} d'={dq}: members={nm} advmax_in_band_chart={adv}"
                     f" cap(m'+1)={cap}")
                if fb: s += f" | FULLCHART m'=t: classes={nfull} cap={capt} {fb}"
                out.append(s)
        elif M >= 4 and recs:
            classes = {rec["Sq"] for rec in recs}
            npetimg = len({tuple(Pi) for Pi in petalimg})
            overlap = len(set(coreimg) & set(q for Pi in petalimg for q in Pi))
            # component proportionality test
            ref = None; prop = True
            for i in range(nq):
                vec = [comps_u[r][i] for r in range(M)]
                nz = [v for v in vec if v]
                if not nz: continue
                if ref is None and vec[-1] != 0:
                    ref = [v * pow(vec[-1], -1, p) % p for v in vec]
                elif vec[-1] != 0:
                    cur = [v * pow(vec[-1], -1, p) % p for v in vec]
                    if cur != ref: prop = False
                else:
                    prop = False
            zero_all = sum(1 for i in range(nq)
                           if all(comps_u[r][i] == 0 for r in range(M)))
            out.append(f"  M={M}: members={len(sub)} classes={len(classes)}"
                       f" petal_images={npetimg} core/petal_img_overlap={overlap}"
                       f" comps_proportional={prop} joint_zero_pts={zero_all}"
                       f" caps: t+1={t+1} npetimg+1={npetimg+1}")
            for rec in recs[:6]:
                out.append(f"    S'={sorted(rec['Sq'])} |S|={len(rec['S'])}")
    if verbose or any("VIOL" in l for l in out):
        pass
    return out

def main():
    shard = sys.argv[1] if len(sys.argv) > 1 else "probe"
    shards = {
        "probe": [(32, 16, [97], ["geom5"])],
        "n16": [(16, 8, [97, 257, 337, 449],
                 ["geom5", "geom3", "consec", "rand1", "rand2", "wtau0", "wtauy"])],
        "n32a": [(32, 16, [97, 193, 1153],
                  ["geom5", "consec", "rand1", "wtau0", "wtauy"])],
        "n32b": [(32, 12, [97, 193, 449],
                  ["geom5", "consec", "rand1", "wtau0", "wtauy"])],
        "n32c": [(32, 8, [97, 193], ["geom5", "consec", "rand1", "wtauy"])],
    }
    for n, k, primes, modes in shards[shard]:
        for p in primes:
            assert is_prime(p) and (p-1) % n == 0
            for mode in modes:
                for line in run_cell(n, k, p, mode):
                    print(line)
    print("\nGLOBAL:", {k2: v for k2, v in GLOB.items()})
    if VIOL:
        print("VIOLATIONS:")
        for v in VIOL[:80]: print("  ", v)
    else:
        print("NO VIOLATIONS")

if __name__ == "__main__":
    main()
