#!/usr/bin/env python3
"""ccd_stage3: n=64 rows + config-census (proved lift reduction) + M=4 boundary
plant + uniqueness mutation control, for petal_chart_carrying_descent.

Subcommands:
  fib64k8 <p>       fiber-complete (64,8,p) x [geom5,consec,rand1] + cfg cross-check
  cfg <n> <k> <p> <modes,> <zmax>   config-census at quotient row, lift, battery
  plant4 <n> <k> <p>                scale-4 plant + full-cell battery (n<=32) or
                                    member-level battery (n=64)
  unique2                            two-members-in-one-band-chart infeasibility

Config-census completeness: by P1 (proved lift form, in-vivo 1221/1221), every
scale->=2 member is f=(X-x_nf)g(X^2) with deg g<k'=k/2, g(y_nf)=0,
|agr(g,u_1)|>=k'+1. g factors L_W h, W = zero-region agreements (y_nf in W),
deg h <= k'-1-|W|; h is determined by any (k'-|W|)-subset of its petal
agreements (|I'| >= k'+1-|W| > k'-|W|). Enumerating all W (|W| <= zmax) and all
defining petal subsets covers every member with z <= zmax exactly.
"""
import itertools, random, sys
from math import comb

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
    m = len(xs)
    dd = list(ys)
    for j in range(1, m):
        for i in range(m-1, j-1, -1):
            dd[i] = (dd[i] - dd[i-1]) * pow(xs[i] - xs[i-j], -1, p) % p
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

def polymul(a, b, p):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i+j] = (out[i+j] + x*y) % p
    return out

def stab_order(S, n):
    c, M = 1, 2
    while M <= n:
        s = n // M
        if all(((x+s) % n) in S for x in S): c = M
        else: break
        M *= 2
    return c

def build_word(n, k, p, dom, scal):
    half = n//2; nf = (k-1)//2
    core = []
    for j in range(nf): core.extend([j, j+half])
    core.append(nf)
    petal_fibers = list(range(nf+1, half))
    petals = [sorted([j, j+half]) for j in petal_fibers]
    locZ = locator_poly([dom[j] for j in sorted(core)], p)
    values = [0]*n
    for c_i, P in zip(scal, petals):
        for j in P: values[j] = c_i * ev(locZ, dom[j], p) % p
    return values, sorted(core), petals, [nf+half], nf, locZ

def make_scalars(mode, n, k, p, dom):
    half = n//2; nf = (k-1)//2
    petal_fibers = list(range(nf+1, half))
    t = len(petal_fibers)
    dom2 = [dom[i]*dom[i] % p for i in range(half)]
    Zp = [dom2[j] for j in range(nf)]
    locZp = locator_poly(Zp, p); y_nf = dom2[nf]; kp = k//2
    if mode == "geom5":
        out, v = [], 1
        for _ in range(t): out.append(v); v = v*5 % p
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
        assert all(c % p for c in out)
    else:
        raise ValueError(mode)
    return out

def quotient_data(n, k, p, dom):
    half = n//2; nf = (k-1)//2; kp = k//2
    dom2 = [dom[i]*dom[i] % p for i in range(half)]
    Zp = [dom2[j] for j in range(nf)]
    locZp = locator_poly(Zp, p)
    return half, nf, kp, dom2, Zp, locZp, dom2[nf]

def u1_of_word(n, p, dom, values):
    half = n//2
    u1 = [0]*half
    inv2 = pow(2, -1, p)
    for i in range(half):
        x = dom[i]
        u1[i] = (values[i]-values[i+half]) * pow(2*x, -1, p) % p
    return u1

def lift(g, x_nf, k, p):
    """f = (X - x_nf) g(X^2), coeffs deg < k."""
    f = [0]*k
    for i, c in enumerate(g):
        f[2*i] = (f[2*i] - x_nf*c) % p
        if 2*i+1 < k: f[2*i+1] = c % p
    return tuple(f)

def config_census(nq, kq, p, domq, u1v, zmax, zmin=1):
    """members: g -> frozenset agr. zero-region = {0..kq-1}, y_nf index kq-1.
    Works in h-space: g = L_W h; agr = W u {petal q: h(q)=vs[q]}
    u {zero i not in W: h(i)=0}."""
    nfq = kq-1
    petalpts = list(range(kq, nq))
    members = {}
    zmax = min(zmax, kq-1)
    ncand = 0
    need = kq+1
    for z in range(zmin, zmax+1):
        for Wrest in itertools.combinations(range(nfq), z-1):
            W = list(Wrest) + [nfq]
            Wset = set(W)
            locW = locator_poly([domq[i] for i in W], p)
            nun = kq - z
            if nun <= 0: continue
            vs = {}
            for i in petalpts:
                vs[i] = u1v[i] * pow(ev(locW, domq[i], p), -1, p) % p
            zfree = [i for i in range(kq) if i not in Wset]
            xpet = {i: domq[i] for i in petalpts}
            for I0 in itertools.combinations(petalpts, nun):
                ncand += 1
                xs = [xpet[i] for i in I0]; ys = [vs[i] for i in I0]
                h = newton_interp(xs, ys, p)
                cnt = z; agrset = list(W)
                rem = len(petalpts) + len(zfree)
                dead = False
                for i in petalpts:
                    if ev(h, xpet[i], p) == vs[i]:
                        cnt += 1; agrset.append(i)
                    rem -= 1
                    if cnt + rem < need: dead = True; break
                if dead: continue
                for i in zfree:
                    if ev(h, domq[i], p) == 0:
                        cnt += 1; agrset.append(i)
                    rem -= 1
                    if cnt + rem < need: dead = True; break
                if dead or cnt < need: continue
                g = tuple(c % p for c in polymul(locW, list(h), p))
                g = tuple(list(g) + [0]*(kq-len(g)))[:kq]
                if g not in members:
                    members[g] = frozenset(agrset)
    return members, ncand

def battery_m2(n, k, p, dom, values, petals, nf, members_g, tag):
    """obligation battery on quotient members g (scale->=2 lifts)."""
    half = n//2; kp = k//2
    x_nf = dom[nf]
    viol = []
    dom2 = [dom[i]*dom[i] % p for i in range(half)]
    petalpts = set(range(nf+1, half))
    byW = {}
    n4 = 0
    for g, Sq in members_g.items():
        f = lift(g, x_nf, k, p)
        S = frozenset(j for j in range(n) if ev(f, dom[j], p) == values[j])
        if frozenset(j % half for j in S) != Sq or len(S) != 2*len(Sq):
            viol.append(("LIFT_SEMANTICS", tag))
        st = stab_order(S, n)
        if st == 4: n4 += 1
        # full petal + pattern + escape
        for P in petals:
            if len(S & frozenset(P)) not in (0, 2): viol.append(("NOT_FULL_PETAL", tag))
        if not (Sq & petalpts): viol.append(("ESCAPE_A2", tag, sorted(Sq)))
        W = frozenset(Sq & set(range(nf+1)))
        Iq = frozenset(Sq & petalpts)
        z = len(W); dq = kp - z
        if len(Iq) < dq+1: viol.append(("A_THRESH", tag))
        byW.setdefault(W, []).append((g, Sq, Iq))
    # per-chart adversarial max
    worst = 0; capv = 0; bigW = 0
    rngs = random.Random(3)
    for W, rs in byW.items():
        z = len(W); dq = kp - z; cap_m = dq + 2
        Is = list({Iq for _, _, Iq in rs})
        best = 1 if Is else 0
        L = len(Is)
        if L <= 16:
            for mask in range(1, 1 << L):
                u = frozenset()
                for b in range(L):
                    if mask >> b & 1: u = u | Is[b]
                if len(u) <= cap_m:
                    best = max(best, sum(1 for I in Is if I <= u))
        elif L <= 400:
            for a in range(L):
                for b in range(a+1, L):
                    u = Is[a] | Is[b]
                    if len(u) <= cap_m:
                        best = max(best, sum(1 for I in Is if I <= u))
        else:
            bigW += 1   # P3-proof regime; sampled pair verification
            for _ in range(4000):
                a, b = rngs.randrange(L), rngs.randrange(L)
                if a != b and len(Is[a] | Is[b]) <= cap_m:
                    best = max(best, 2)
        worst = max(worst, best)
        if best > cap_m + 1: capv += 1
    topband = sum(1 for g, Sq in members_g.items() if len(Sq) <= kp+2)
    print(f"  {tag}: members={len(members_g)} charts={len(byW)} scale4={n4}"
          f" topband={topband} max_members_per_band_chart={worst} capviol={capv}"
          f" bigW_P3_sampled={bigW} viol={len(viol)}")
    for v in viol[:10]: print("    VIOL", v)
    return viol, byW

def battery_m4(n, k, p, dom, values, petals, nf, f, S, tag):
    """M=4 descent battery on one official member f with 4-invariant S."""
    M = 4; nq = n//M; kq = k//M
    domq = [pow(dom[1], M*i, p) for i in range(nq)]
    # vector word by 4x4 fiberwise solve
    comps = []
    for i in range(nq):
        fpts = [i + s*nq for s in range(M)]
        mat = [[pow(dom[j], r, p) for r in range(M)] for j in fpts]
        rhs = [values[j] for j in fpts]
        A = [row[:] + [rhs[ii]] for ii, row in enumerate(mat)]
        Mm = M
        for col in range(Mm):
            piv = next(r for r in range(col, Mm) if A[r][col] % p)
            A[col], A[piv] = A[piv], A[col]
            inv = pow(A[col][col], -1, p)
            A[col] = [x*inv % p for x in A[col]]
            for r in range(Mm):
                if r != col and A[r][col] % p:
                    fq = A[r][col]
                    A[r] = [(A[r][c] - fq*A[col][c]) % p for c in range(Mm+1)]
        comps.append([A[r][Mm] for r in range(M)])
    fr = [list(f[r::M]) for r in range(M)]
    Sq = frozenset(j % nq for j in S)
    ok = (len(Sq)*M == len(S))
    Sq2 = frozenset(i for i in range(nq)
                    if all(ev(fr[r], domq[i], p) == comps[i][r] for r in range(M)))
    core_img = sorted({j % nq for j in range(nf)} | {j % nq for j in range(n//2, n//2+nf)} |
                      {jj % nq for jj in [j for j in range(nf)]})
    # official core exponents: full fibers {j, j+n/2}, j<nf, plus nf
    core_exps = [j for j in range(nf)] + [j+n//2 for j in range(nf)] + [nf]
    core_img = sorted({j % nq for j in core_exps})
    split_img = nf % nq
    pet_imgs = [sorted({j % nq for j in P}) for P in petals]
    pet_pts = sorted({q for Pi in pet_imgs for q in Pi})
    merged = {}
    inc = 0
    for idx, Pi in enumerate(pet_imgs):
        merged.setdefault(tuple(Pi), []).append(idx)
    for key, idxs in merged.items():
        touch = {frozenset(petals[i]) <= S for i in idxs}
        if len(touch) > 1: inc += 1
    escape = not (Sq & set(pet_pts))
    # proportionality of components on nonzero pts
    prop = True; ref = None
    for i in range(nq):
        vec = comps[i]
        if vec[-1] != 0:
            cur = [v * pow(vec[-1], -1, p) % p for v in vec]
            if ref is None: ref = cur
            elif cur != ref: prop = False
        elif any(vec): prop = False
    jz = sum(1 for i in range(nq) if not any(comps[i]))
    print(f"  {tag}: |S|={len(S)} |S''|={len(Sq)} semantic_ok={Sq2 == Sq and ok}"
          f" escape_clause2={escape} merged_petal_groups={sum(1 for v in merged.values() if len(v) > 1)}"
          f" merged_inconsistent={inc} core_img={len(core_img)} petal_img_pts={len(pet_pts)}"
          f" overlap={len(set(core_img) & set(pet_pts))} comps_proportional={prop}"
          f" joint_zero_pts={jz} (chart-form would need ~{kq})")
    return escape, inc

def cmd_fib64k8(p):
    n, k = 64, 8
    dom = order_n_domain(p, n)
    for mode in ["geom5", "consec", "rand1"]:
        scal = make_scalars(mode, n, k, p, dom)
        values, core, petals, bg, nf, locZ = build_word(n, k, p, dom, scal)
        # fiber-complete
        half = n//2; m0 = -(-(k+1)//2)
        found = {}
        cache = {}
        for fibsub in itertools.combinations(range(half), m0):
            pts = []
            for j in fibsub: pts.append(j); pts.append(j+half)
            xs = [dom[j] for j in pts]; ys = [values[j] for j in pts]
            key = tuple(pts[:k])
            poly = cache.get(key)
            if poly is None:
                poly = newton_interp(xs[:k], ys[:k], p); cache[key] = poly
            if poly in found: continue
            if any(ev(poly, x, p) != y for x, y in zip(xs[k:], ys[k:])): continue
            S = frozenset(j for j in range(n) if ev(poly, dom[j], p) == values[j])
            if len(S) >= k+1 and stab_order(S, n) >= 2: found[poly] = S
        # config census (complete: zmax = k'-1 = 3)
        u1v = u1_of_word(n, p, dom, values)
        domq = [dom[i]*dom[i] % p for i in range(half)]
        mem, ncand = config_census(half, k//2, p, domq, u1v, k//2-1)
        lifted = {lift(g, dom[nf], k, p) for g in mem}
        match = (lifted == set(found))
        scales = {}
        for f, S in found.items(): scales.setdefault(stab_order(S, n), []).append(f)
        print(f"CELL (64,8,p={p},{mode}) fiber_complete={len(found)}"
              f" cfg_complete={len(mem)} METHODS_MATCH={match}"
              f" scales={ {c: len(v) for c, v in sorted(scales.items())} } cands={ncand}")
        battery_m2(n, k, p, dom, values, petals, nf, mem, f"(64,8,{p},{mode}) M=2")
        for st in (4, 8):
            for f in scales.get(st, []):
                if st == 4:
                    battery_m4(n, k, p, dom, values, petals, nf, f, found[f],
                               f"(64,8,{p},{mode}) natural scale-4 M=4")

def cmd_cfg(n, k, p, modes, zmax, zmin=1):
    dom = order_n_domain(p, n)
    half = n//2; nf = (k-1)//2
    for mode in modes:
        scal = make_scalars(mode, n, k, p, dom)
        values, core, petals, bg, nf, locZ = build_word(n, k, p, dom, scal)
        u1v = u1_of_word(n, p, dom, values)
        domq = [dom[i]*dom[i] % p for i in range(half)]
        mem, ncand = config_census(half, k//2, p, domq, u1v, zmax, zmin)
        zs = {}
        for g, agr in mem.items():
            z = len(agr & set(range(k//2)))
            zs[z] = zs.get(z, 0) + 1
        print(f"CELL ({n},{k},p={p},{mode}) cfg_members({zmin}<=z<={zmax})={len(mem)}"
              f" by_z={dict(sorted(zs.items()))} cands={ncand}")
        battery_m2(n, k, p, dom, values, petals, nf, mem, f"({n},{k},{p},{mode}) M=2")
        # natural scale-4 among lifts:
        x_nf = dom[nf]
        for g, Sq in mem.items():
            if stab_order(Sq, half) >= 2:  # S' 2-invariant => official scale 4
                f = lift(g, x_nf, k, p)
                S = frozenset(j for j in range(n) if ev(f, dom[j], p) == values[j])
                battery_m4(n, k, p, dom, values, petals, nf, f, S,
                           f"({n},{k},{p},{mode}) natural scale-4 M=4")

def cmd_plant4(n, k, p, seed=5):
    rng = random.Random(seed)
    dom = order_n_domain(p, n)
    half = n//2; nf = (k-1)//2; kp = k//2
    dom2 = [dom[i]*dom[i] % p for i in range(half)]
    Zp = [dom2[j] for j in range(nf)]; locZp = locator_poly(Zp, p)
    # quotient 2-fibers {i, i+half/2}; zero-region {0..kp-1}; want S' = union of
    # fibers over W_fib (i and i+nq2 both in S'), y_nf index = nf = kp-1.
    nq2 = half//2
    nfib = (kp+1)//2 + 1  # enough fibers: 2*nfib >= kp+2
    while 2*nfib < kp+2: nfib += 1
    for attempt in range(200):
        Wf = [nf] + rng.sample(range(nf), nfib-1)
        W = sorted(Wf)
        locW = locator_poly([dom2[i] for i in W], p)
        hdeg = kp-1-nfib
        if hdeg < 0: print("plant infeasible: hdeg<0"); return
        h = [rng.randrange(p) for _ in range(hdeg+1)]
        if not any(h): continue
        g = tuple(c % p for c in polymul(locW, h, p))
        g = tuple(list(g) + [0]*(kp-len(g)))[:kp]
        # partners i+nq2 must be petal points (>= kp) and g nonzero there
        partners = [i + nq2 for i in W]
        if any(q < kp for q in partners): continue
        if any(ev(g, dom2[q], p) == 0 for q in partners): continue
        # scalars: petal fiber q (kp <= q < half): c_q = g(y_q)/L_{Z'}(y_q) for
        # planted partners; random elsewhere
        scal = []
        for q in range(kp, half):
            if q in partners:
                scal.append(ev(g, dom2[q], p) * pow(ev(locZp, dom2[q], p), -1, p) % p)
            else:
                scal.append(rng.randrange(1, p))
        values, core, petals, bg, nf2, locZ = build_word(n, k, p, dom, scal)
        u1v = u1_of_word(n, p, dom, values)
        agr = frozenset(i for i in range(half) if ev(g, dom2[i], p) == u1v[i])
        if len(agr) < kp+1: continue
        if stab_order(agr, half) < 2: continue
        f = lift(g, dom[nf], k, p)
        S = frozenset(j for j in range(n) if ev(f, dom[j], p) == values[j])
        st = stab_order(S, n)
        if st != 4: continue
        print(f"PLANTED scale-4 member at ({n},{k},p={p}) attempt={attempt}"
              f" |S|={len(S)} S'={sorted(agr)}")
        battery_m4(n, k, p, dom, values, petals, nf, f, S,
                   f"({n},{k},{p},planted) M=4")
        # full battery on the planted word (complete cfg census up to z limit)
        zmax = kp-1 if n <= 32 else 3
        mem, ncand = config_census(half, kp, p, dom2, u1v, zmax)
        print(f"  planted-word cfg census (z<={zmax}): members={len(mem)}")
        battery_m2(n, k, p, dom, values, petals, nf, mem,
                   f"({n},{k},{p},planted) M=2")
        # scale-4 class count per chart reading at M=4
        s4 = [(g2, Sq) for g2, Sq in mem.items() if stab_order(Sq, half) >= 2]
        print(f"  scale-4 members among census: {len(s4)}")
        s4cls = set()
        for g2, Sq in s4:
            f2 = lift(g2, dom[nf], k, p)
            S2 = frozenset(j for j in range(n) if ev(f2, dom[j], p) == values[j])
            s4cls.add(frozenset(j % (n//4) for j in S2))
        t = len(petals)
        print(f"  scale-4 distinct M=4 classes={len(s4cls)} vs t+1={t+1}")
        return
    print(f"plant4({n},{k},{p}): no planted scale-4 member in 200 attempts")

def cmd_unique2():
    n, k, p = 32, 16, 97
    dom = order_n_domain(p, n)
    half, nf, kp, dom2, Zp, locZp, y_nf = quotient_data(n, k, p, dom)
    rng = random.Random(11)
    petalpts = list(range(kp, half))
    trials = 0; contradictions = 0
    for trial in range(50):
        Wrest = rng.sample(range(nf), 1)
        W = sorted(Wrest + [nf])          # z = 2, d' = kp-2, cap_m = kp
        locW = locator_poly([dom2[i] for i in W], p)
        P = petalpts[:]                    # m' = kp = d'+2: max band chart
        q1, q2 = rng.sample(P, 2)
        I1 = [q for q in P if q != q1]; I2 = [q for q in P if q != q2]
        h1 = [rng.randrange(p) for _ in range(kp-2)]  # deg <= d'-1 = kp-3
        # h1 defines c-values on I1; h2 must match c-values on I1 cap I2
        shared = [q for q in I1 if q in I2]
        xs = [dom2[q] for q in shared]
        ys = [ev(h1, x, p) for x in xs]
        # h2 interpolates >= kp-2 shared values with deg <= kp-3: determined by
        # any kp-2 of them; check it equals h1 (kp-2 points determine deg kp-3)
        h2 = list(newton_interp(xs[:kp-2], ys[:kp-2], p))
        h2 += [0]*(kp-2-len(h2))
        h1p = h1 + [0]*(kp-2-len(h1))
        trials += 1
        if [c % p for c in h2] == [c % p for c in h1p]:
            contradictions += 1
    print(f"unique2: {trials} attempts to place 2 distinct members in one max-band"
          f" chart; forced h2==h1 in {contradictions}/{trials}"
          f" (P3 uniqueness confirmed: no two distinct members share a band chart)")

def main():
    cmd = sys.argv[1]
    if cmd == "fib64k8":
        cmd_fib64k8(int(sys.argv[2]))
    elif cmd == "cfg":
        n, k, p = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
        modes = sys.argv[5].split(",")
        zmax = int(sys.argv[6])
        zmin = int(sys.argv[7]) if len(sys.argv) > 7 else 1
        cmd_cfg(n, k, p, modes, zmax, zmin)
    elif cmd == "plant4":
        cmd_plant4(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif cmd == "unique2":
        cmd_unique2()

if __name__ == "__main__":
    main()
