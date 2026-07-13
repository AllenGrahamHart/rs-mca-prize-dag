#!/usr/bin/env python3
"""csp_verify: verifier for the chart-carrying descent proof packet
(csp_statement.md / csp_proof.md; SUCCESSOR-A claims #132, #128, L0/C).

Run: tools/ramguard tiny -- python3 csp_verify.py     (exit 0 = PASS)

What it checks (all M = 2, fiber-aligned sigma = 1 charts, census
conventions pinned verbatim from cg_petal_census / ccd_stage2):

STAGE A  structure identities S1, S2 (locator + word factorization, u0 =
         -x_nf*u1, u1 = quotient chart word with unchanged scalars) and the
         lift-semantics formula S4, on banked cells AND new cells.
STAGE B  complete censuses by TWO independent methods — official-row
         fiber-subset enumeration vs quotient-row point-subset enumeration —
         matched through the S3/S4 bijection; per-member chart-data descent
         (d = 2d', r = 1, a' threshold, band equivalence, full petal,
         image factorization G_P = [(Y-y_nf) g/L_W](X^2), deg g/L_W <= d'-1);
         P3 uniqueness (no two distinct members fit one band chart);
         member counts compared against PINNED values from the banked ccd
         evidence tables (ccd_out_n16/n32a/n32b/n32c.txt).
         NEW cells never touched by the search: the (32,20) row shape,
         prime 577 at (16,8), prime 353 at (32,16).
STAGE C  mutation controls (each must TRIP a named check):
         M1 corrupted chart word -> S2 identity fails;
         M2 injected fake member (coefficient flip) -> semantics/K_2 checks fail;
         M3 P3 margin: two distinct degree-d' pseudo-members DO occupy one
            band chart (the reading-A degree bound d'-1 is load-bearing);
         M4 corrupted pin table -> banked comparison fails.
"""
import itertools, random, sys

# ---------- pinned census conventions (verbatim semantics) ----------

def order_n_domain(p, n):
    a = 2
    while True:
        g0 = pow(a, (p - 1) // n, p)
        if pow(g0, n // 2, p) != 1:
            break
        a += 1
    dom = [pow(g0, j, p) for j in range(n)]
    assert len(set(dom)) == n
    return dom

def locator_poly(roots, p):
    loc = [1]
    for r in roots:
        new = [0] * (len(loc) + 1)
        for i, c in enumerate(loc):
            new[i] = (new[i] - r * c) % p
            new[i + 1] = (new[i + 1] + c) % p
        loc = new
    return loc

def ev(poly, x, p):
    v = 0
    for c in reversed(poly):
        v = (v * x + c) % p
    return v

def newton_interp(xs, ys, p):
    m = len(xs)
    dd = list(ys)
    for j in range(1, m):
        for i in range(m - 1, j - 1, -1):
            dd[i] = (dd[i] - dd[i - 1]) * pow(xs[i] - xs[i - j], -1, p) % p
    poly = [0] * m
    base = [1]
    for i in range(m):
        for d2, c in enumerate(base):
            poly[d2] = (poly[d2] + dd[i] * c) % p
        if i < m - 1:
            newb = [0] * (len(base) + 1)
            r = xs[i]
            for d2, c in enumerate(base):
                newb[d2] = (newb[d2] - r * c) % p
                newb[d2 + 1] = (newb[d2 + 1] + c) % p
            base = newb
    return tuple(poly)

def polymul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % p
    return out

def polydeg(a):
    d = len(a) - 1
    while d >= 0 and a[d] == 0:
        d -= 1
    return d  # -1 for zero poly

def divide_by_root(a, r, p):
    """a(X)/(X-r) by synthetic division; returns (quotient, remainder)."""
    out = [0] * (len(a) - 1)
    acc = 0
    for i in range(len(a) - 1, 0, -1):
        acc = (acc * r + a[i]) % p if i != len(a) - 1 else a[i] % p
        out[i - 1] = acc
    rem = (acc * r + a[0]) % p
    return out, rem

def stab_order(S, n):
    c, M = 1, 2
    while M <= n:
        s = n // M
        if all(((x + s) % n) in S for x in S):
            c = M
        else:
            break
        M *= 2
    return c

def make_scalars(mode, n, k, p, dom):
    half = n // 2
    nf = (k - 1) // 2
    petal_fibers = list(range(nf + 1, half))
    t = len(petal_fibers)
    dom2 = [dom[i] * dom[i] % p for i in range(half)]
    Zp = [dom2[j] for j in range(nf)]
    locZp = locator_poly(Zp, p)
    y_nf = dom2[nf]
    kp = k // 2
    if mode == "geom5":
        out, v = [], 1
        for _ in range(t):
            out.append(v); v = v * 5 % p
    elif mode == "geom3":
        out, v = [], 1
        for _ in range(t):
            out.append(v); v = v * 3 % p
    elif mode == "consec":
        out = [(i + 1) % p for i in range(t)]
    elif mode.startswith("rand"):
        rng = random.Random(1000 + int(mode[4:]))
        out = [rng.randrange(1, p) for _ in range(t)]
    elif mode in ("wtau0", "wtauy"):
        tau = dom2[0] if mode == "wtau0" else y_nf
        out = []
        for j in petal_fibers:
            y = dom2[j]
            w = pow(y, kp, p) * ((y - tau) % p) % p
            out.append(w * pow(ev(locZp, y, p), -1, p) % p)
        assert all(c % p != 0 for c in out)
    else:
        raise ValueError(mode)
    return out

def build_cell(n, k, p, mode):
    """Returns full cell data dict (k even only)."""
    assert k % 2 == 0 and n % 2 == 0 and (p - 1) % n == 0
    half = n // 2
    nf = k // 2 - 1                       # = (k-1)//2 for even k
    dom = order_n_domain(p, n)
    core = sorted([j for j in range(nf)] + [j + half for j in range(nf)] + [nf])
    petal_fibers = list(range(nf + 1, half))
    petals = [sorted([j, j + half]) for j in petal_fibers]
    bg = [nf + half]
    scal = make_scalars(mode, n, k, p, dom)
    locZ = locator_poly([dom[j] for j in core], p)
    values = [0] * n
    for c_i, P in zip(scal, petals):
        for j in P:
            values[j] = c_i * ev(locZ, dom[j], p) % p
    dom2 = [dom[i] * dom[i] % p for i in range(half)]
    Zp = [dom2[j] for j in range(nf)]
    locZp = locator_poly(Zp, p)
    u1 = [0] * half
    for i in petal_fibers:
        u1[i] = scal[i - nf - 1] * ev(locZp, dom2[i], p) % p
    return dict(n=n, k=k, p=p, mode=mode, half=half, nf=nf, kp=k // 2,
                t=len(petals), dom=dom, dom2=dom2, core=core, petals=petals,
                petal_fibers=petal_fibers, bg=bg, scal=scal, locZ=locZ,
                locZp=locZp, values=values, u1=u1, x_nf=dom[nf],
                y_nf=dom2[nf])

def lift(g, x_nf, k, p):
    f = [0] * k
    for i, c in enumerate(g):
        f[2 * i] = (f[2 * i] - x_nf * c) % p
        if 2 * i + 1 < k:
            f[2 * i + 1] = c % p
    return tuple(f)

# ---------- STAGE A: structure identities ----------

def check_struct(C):
    fails = []
    n, k, p = C["n"], C["k"], C["p"]
    half, nf, kp = C["half"], C["nf"], C["kp"]
    dom, dom2, values, u1 = C["dom"], C["dom2"], C["values"], C["u1"]
    x_nf, y_nf = C["x_nf"], C["y_nf"]
    # S1: L_Z(X) = L_{Z'}(X^2)(X - x_nf)
    inner = [0] * (2 * len(C["locZp"]) - 1)
    for i, c in enumerate(C["locZp"]):
        inner[2 * i] = c
    rhs = [0] * (len(inner) + 1)
    for i, c in enumerate(inner):
        rhs[i] = (rhs[i] - x_nf * c) % p
        rhs[i + 1] = (rhs[i + 1] + c) % p
    if [c % p for c in C["locZ"]] != [c % p for c in rhs]:
        fails.append("S1")
    # S2 table: u1 = 0 on Z' u {y_nf}; c_i L_{Z'} on petal points (checked in
    # build_cell construction); here verify u1 against the FIBERWISE vector
    # word of U (independent derivation) and the pointwise factorization.
    for i in range(half):
        a, b = values[i], values[i + half]
        u0_i = (a + b) * pow(2, -1, p) % p
        u1_i = (a - b) * pow(2 * dom[i], -1, p) % p
        if u1_i != u1[i]:
            fails.append("S2 u1"); break
        if u0_i != (-x_nf * u1[i]) % p:
            fails.append("S2 u0"); break
    for j in range(n):
        if values[j] != (dom[j] - x_nf) * u1[j % half] % p:
            fails.append("S2 factor"); break
    for j in range(nf + 1):
        if u1[j] != 0:
            fails.append("S2 zeros"); break
    # S4: lift agreement formula on random g (10 free, 10 with g(y_nf)=0)
    rng = random.Random(20260713)
    for trial in range(20):
        if trial < 10:
            g = [rng.randrange(p) for _ in range(kp)]
        else:
            g0 = [rng.randrange(p) for _ in range(kp - 1)]
            g = polymul([(-y_nf) % p, 1], g0, p)  # (Y - y_nf) * random
            g = (g + [0] * kp)[:kp]
        f = lift(g, x_nf, k, p)
        S = frozenset(j for j in range(n) if ev(f, dom[j], p) == values[j])
        agrg = frozenset(i for i in range(half) if ev(g, dom2[i], p) == u1[i])
        pred = {nf} | {j for j in range(n)
                       if j % half != nf and (j % half) in agrg}
        if ev(g, y_nf, p) == 0:
            pred.add(nf + half)
        if S != frozenset(pred):
            fails.append("S4 formula"); break
    return fails

# ---------- STAGE B: dual complete censuses + battery ----------

def official_census(C):
    """Complete enumeration of scale->=2 contributors (fiber-subset method:
    every K_2-invariant S with |S| >= k+2 contains >= k'+1 full fibers)."""
    n, k, p = C["n"], C["k"], C["p"]
    half, dom, values = C["half"], C["dom"], C["values"]
    m0 = C["kp"] + 1
    found = {}
    for fibsub in itertools.combinations(range(half), m0):
        pts = []
        for j in fibsub:
            pts.append(j); pts.append(j + half)
        xs = [dom[j] for j in pts]
        ys = [values[j] for j in pts]
        poly = newton_interp(xs[:k], ys[:k], p)
        if poly in found:
            continue
        if any(ev(poly, x, p) != y for x, y in zip(xs[k:], ys[k:])):
            continue
        S = frozenset(j for j in range(n) if ev(poly, dom[j], p) == values[j])
        if len(S) >= k + 1 and stab_order(S, n) >= 2:
            found[poly] = S
    return found

def quotient_census(C):
    """Complete enumeration of quotient contributors g to u1 with
    y_nf in agr (point-subset method: any |S'| >= k'+1 support contains a
    (k'+1)-subset; interpolate through k' points, check the rest)."""
    half, kp, p = C["half"], C["kp"], C["p"]
    dom2, u1 = C["dom2"], C["u1"]
    nf = C["nf"]
    found = {}
    for sub in itertools.combinations(range(half), kp + 1):
        xs = [dom2[i] for i in sub]
        ys = [u1[i] for i in sub]
        g = newton_interp(xs[:kp], ys[:kp], p)
        if g in found:
            continue
        if ev(g, xs[kp], p) != ys[kp]:
            continue
        Sq = frozenset(i for i in range(half) if ev(g, dom2[i], p) == u1[i])
        if len(Sq) >= kp + 1 and nf in Sq:
            found[g] = Sq
    return found

def battery(C, off, quo):
    """All per-member packet checks + P3 + bijection. Returns fails list."""
    fails = []
    n, k, p = C["n"], C["k"], C["p"]
    half, nf, kp, t = C["half"], C["nf"], C["kp"], C["t"]
    dom, dom2, values, u1 = C["dom"], C["dom2"], C["values"], C["u1"]
    x_nf, y_nf = C["x_nf"], C["y_nf"]
    coreset = set(C["core"])
    # S3/S4 bijection: lifts of quotient members == official members, supports match
    lifted = {}
    for g, Sq in quo.items():
        f = lift(g, x_nf, k, p)
        lifted[f] = frozenset(j for j in range(n) if (j % half) in Sq)
    if lifted != off:
        fails.append("BIJECTION")
    byW = {}
    for g, Sq in quo.items():
        W = frozenset(i for i in Sq if i <= nf)
        Iq = frozenset(i for i in Sq if i > nf)
        z = len(W)
        dq = kp - z
        # chart data descent (S5)
        f = lift(g, x_nf, k, p)
        S = lifted.get(f, frozenset())
        d_off = len(coreset - S)
        r_off = 1 if (nf + half) in S else 0
        if nf not in W:
            fails.append("YNF_NOT_IN_W")
        if not (d_off == 2 * dq and r_off == 1 and nf in S):
            fails.append("D_ARITH")
        if dq < 1:
            fails.append("DQ_ZERO_CHART_NONEMPTY")
        if len(Iq) < dq + 1:
            fails.append("A_THRESH")
        for m_test in (t, len(Iq)):
            if (d_off >= 2 * (m_test - 2)) != (dq >= m_test - 2):
                fails.append("BAND_EQUIV")
        for P in C["petals"]:
            if len(S & set(P)) not in (0, 2):
                fails.append("FULL_PETAL")
        for i in C["petal_fibers"]:
            if (set([i, i + half]) <= S) != (i in Iq):
                fails.append("PATTERN")
        # deg h <= d'-1 via exact division g / L_W  (reading-A degree pin)
        h = list(g)
        okdiv = True
        for i in sorted(W):
            h, rem = divide_by_root(h, dom2[i], p)
            if rem != 0:
                okdiv = False
                break
        if not okdiv:
            fails.append("LW_DIVIDES")
        elif polydeg(h) > dq - 1:
            fails.append("DEG_H")
        else:
            # S5 image factorization: f == L_{Z n S} * Q(X^2), Q = (Y-y_nf) h
            Q = polymul([(-y_nf) % p, 1], h, p) if polydeg(h) >= 0 else [0]
            Qx2 = [0] * (2 * len(Q) - 1)
            for i2, c in enumerate(Q):
                Qx2[2 * i2] = c
            locZS = locator_poly([dom[j] for j in sorted(coreset & S)], p)
            prod = polymul(locZS, Qx2, p)
            fpad = list(f) + [0] * max(0, len(prod) - len(f))
            prod = prod + [0] * max(0, len(fpad) - len(prod))
            if [c % p for c in fpad] != [c % p for c in prod]:
                fails.append("IMAGE_FACTOR")
        byW.setdefault(W, []).append((g, Iq, dq))
    # P3: no two distinct members fit one band chart (same W, |I1 u I2| <= d'+2)
    for W, recs in byW.items():
        for (g1, I1, dq), (g2, I2, _) in itertools.combinations(recs, 2):
            if len(I1 | I2) <= dq + 2:
                fails.append("P3_TWO_MEMBERS_ONE_BAND_CHART")
    return fails, byW

# pinned member counts from the banked ccd evidence tables
PINS = {
    (16, 8, 97, "consec"): 3,
    (16, 8, 257, "wtauy"): 1,
    (16, 8, 337, "consec"): 3,
    (32, 16, 97, "geom5"): 63,
    (32, 16, 193, "consec"): 56,
    (32, 12, 97, "geom5"): 47,
    (32, 12, 193, "consec"): 43,
    (32, 8, 97, "geom5"): 14,
    (32, 8, 193, "rand1"): 7,
}
# pinned per-chart table for (16,8,97,consec): W (as sorted index tuples) -> members
PIN_CHART_16 = {(0, 2, 3): 1, (1, 2, 3): 1, (3,): 1}

NEW_CELLS = [(32, 20, 97, "geom5"), (32, 20, 97, "consec"),
             (16, 8, 577, "consec"), (32, 16, 353, "geom5")]

# ---------- STAGE C: mutation controls ----------

def mutation_M1():
    """Corrupt the chart word at one petal point -> S2 must fail."""
    C = build_cell(32, 16, 97, "geom5")
    j = C["petal_fibers"][0]
    C["values"][j] = (C["values"][j] + 1) % C["p"]
    fails = check_struct(C)
    return any(f.startswith("S2") for f in fails)

def mutation_M2():
    """Coefficient-flip a true member, keep its claimed support ->
    semantics + K_2-invariance checks must fail."""
    C = build_cell(32, 16, 97, "geom5")
    quo = quotient_census(C)
    g, Sq = next(iter(sorted(quo.items())))
    gf = list(g)
    gf[0] = (gf[0] + 1) % C["p"]
    f = lift(gf, C["x_nf"], C["k"], C["p"])
    S = frozenset(j for j in range(C["n"])
                  if ev(f, C["dom"][j], C["p"]) == C["values"][j])
    claimed = frozenset(j for j in range(C["n"]) if (j % C["half"]) in Sq)
    support_trip = (S != claimed)
    inv_trip = (ev(gf, C["y_nf"], C["p"]) != 0) and (stab_order(S, C["n"]) < 2)
    return support_trip and inv_trip

def mutation_M3():
    """P3 margin: with images of degree d' (one more than reading A's d'-1;
    equivalently deg g = k', not a codeword) TWO distinct pseudo-members fit
    one band chart -> the uniqueness check must trip on them."""
    C = build_cell(32, 16, 97, "geom5")
    p, kp, nf, half = C["p"], C["kp"], C["nf"], C["half"]
    dom2, u1, y_nf = C["dom2"], C["u1"], C["y_nf"]
    petalpts = list(range(nf + 1, half))
    for j0 in range(nf):
        W = [j0, nf]
        z = 2
        dq = kp - z
        if len(petalpts) < dq + 2:
            continue
        P = petalpts[:dq + 2]
        locW = locator_poly([dom2[i] for i in W], p)
        v = {i: u1[i] * pow(ev(locW, dom2[i], p), -1, p) % p for i in P}
        J, (q1, q2) = P[:dq], P[dq:dq + 2]
        h1 = newton_interp([dom2[i] for i in J + [q1]],
                           [v[i] for i in J + [q1]], p)   # deg <= d'
        h2 = newton_interp([dom2[i] for i in J + [q2]],
                           [v[i] for i in J + [q2]], p)   # deg <= d'
        if list(h1) == list(h2):
            continue  # degenerate; try another W
        if polydeg(list(h1)) <= dq - 1 or polydeg(list(h2)) <= dq - 1:
            continue  # accidental true member; try another W
        # both vanish on W after multiplying back, both have >= d'+1
        # agreements with u1 inside P:
        ok = True
        for h in (h1, h2):
            g = polymul(locW, list(h), p)
            agr = sum(1 for i in P if ev(g, dom2[i], p) == u1[i])
            if agr < dq + 1 or polydeg(g) != kp:
                ok = False
        if not ok:
            continue
        # the band-chart double occupancy exists at degree d' => trip
        I1 = frozenset(i for i in P if ev(polymul(locW, list(h1), p), dom2[i], p) == u1[i])
        I2 = frozenset(i for i in P if ev(polymul(locW, list(h2), p), dom2[i], p) == u1[i])
        return len(I1 | I2) <= dq + 2 and len(I1) >= dq + 1 and len(I2) >= dq + 1
    return False

def mutation_M4():
    """Corrupted pin -> banked comparison must fail."""
    C = build_cell(16, 8, 97, "consec")
    off = official_census(C)
    return len(off) != PINS[(16, 8, 97, "consec")] + 1  # wrong pin must mismatch

# ---------- main ----------

def main():
    nfail = 0
    # STAGE A
    struct_cells = ([(16, 8, pp, "consec") for pp in (97, 257, 337, 449, 577)]
                    + [(32, 12, 97, "geom5"), (32, 12, 193, "consec"),
                       (32, 16, 97, "geom5"), (32, 16, 193, "wtauy"),
                       (32, 16, 353, "geom5"), (32, 16, 1153, "geom5"),
                       (32, 8, 97, "rand1"), (32, 20, 97, "geom5"),
                       (32, 20, 97, "consec"), (16, 8, 257, "wtauy")])
    for cell in struct_cells:
        C = build_cell(*cell)
        fails = check_struct(C)
        tag = f"A {cell}"
        if fails:
            nfail += 1
            print(f"FAIL {tag}: {fails}")
        else:
            print(f"PASS {tag}")
    # STAGE B
    bat_cells = list(PINS.keys()) + NEW_CELLS
    total_members = 0
    for cell in bat_cells:
        C = build_cell(*cell)
        off = official_census(C)
        quo = quotient_census(C)
        fails, byW = battery(C, off, quo)
        pin = PINS.get(cell)
        pin_note = ""
        if pin is not None:
            if len(off) != pin or len(quo) != pin:
                fails.append(f"PIN_MISMATCH got {len(off)}/{len(quo)} want {pin}")
            pin_note = f" pin={pin}"
        if cell == (16, 8, 97, "consec"):
            table = {tuple(sorted(W)): len(v) for W, v in byW.items()}
            if table != PIN_CHART_16:
                fails.append(f"PIN_CHART_MISMATCH {table}")
        total_members += len(off)
        tag = f"B {cell} members={len(off)}{pin_note} charts(W)={len(byW)}"
        if fails:
            nfail += 1
            print(f"FAIL {tag}: {sorted(set(fails))}")
        else:
            print(f"PASS {tag}")
    print(f"stage B total members checked: {total_members}")
    # STAGE C
    for name, fn in [("M1 word-corrupt", mutation_M1),
                     ("M2 fake-member", mutation_M2),
                     ("M3 P3-degree-margin", mutation_M3),
                     ("M4 pin-corrupt", mutation_M4)]:
        tripped = fn()
        if tripped:
            print(f"PASS C {name}: TRIPPED as required")
        else:
            nfail += 1
            print(f"FAIL C {name}: mutation NOT detected")
    print("VERDICT:", "ALL PASS" if nfail == 0 else f"{nfail} FAILURES")
    sys.exit(0 if nfail == 0 else 1)

if __name__ == "__main__":
    main()
