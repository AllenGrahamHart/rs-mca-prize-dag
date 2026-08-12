#!/usr/bin/env python3
"""(LA-EQ) geometry: the H1 and H1+H2 nullity-1 families, and the
generalized fence Z^m - X^{2m} at a fresh m.

Source: critical/nodes/rate_half_band_crossing_location/statement.md
        L4270-4345 (Round-36 (LA-EQ) addendum, round 36 bank 1).
Prior art (cross-pointer, NOT re-claimed here): the m = 2 member of the
        generalized fence is the PROVED node
        background/nodes/rate_half_layer_a_saturation_count_route_fence,
        whose coordinator addendum (statement.md:73-89) already records the
        Z^m - X^{2m} generalization.

Checks
  A. THE H1 RUNG IS CONSTRUCTIVELY FALSE.  The closed form
     Q = (Z-g)(Z-h)C(X) + a(Z-h)sigma_g(X) - b(Z-g)sigma_h(X)
     satisfies H1 by construction (two degree-rho supports split over mu_32,
     |S_g ^ S_h| = m-1 = 1, a = 7m-1 = 13 saturated points).  Every
     admissible build has layer-A nullity exactly 1 -- so positive count
     excess 3m^2-5m = +2 does NOT force full rank.
  B. THE H1+H2 RUNG IS CONSTRUCTIVELY FALSE.  Prescribing the five merged
     second slopes makes the merge conditions LINEAR in C; the system is
     10 equations on 9 unknowns (C's 8 coefficients and the scalar a), so
     solvability is ONE scalar condition, solved here by scanning the fifth
     target slope.  The exhibit has supports [7,7,2,2,2,2,2,1,1],
     T = 9 = rho+2 exactly, max pair-intersection 1, and nullity 1.
  C. THE FENCE IS AN INFINITE FAMILY, verified at a FRESH m = 3:
     Q_0 = Z^3 - X^6, W inside 4 fibres of x -> x^6 on mu_48, Gamma = the
     12 cube roots + one spare; a = 20 = 7m-1 saturated, nullity EXACTLY
     2m = 6.

Helpers DUPLICATED; nothing imported.  Stdlib only.
Run: tools/ramguard local -- python3 <this file>   (RAMGUARD_TIMEOUT 300s)
"""

import random

FAIL = []


def bad(m):
    FAIL.append(m)


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
        iv = pow(M[r][c], q - 2, q)
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


def rank(M, q):
    return rref(M, q)[1] if M else 0


def solve_affine(A, b, q):
    """one solution of A z = b, or None."""
    rows, cols = len(A), len(A[0])
    M = [A[i][:] + [b[i] % q] for i in range(rows)]
    Mr, rk, piv = rref(M, q)
    if piv and piv[-1] == cols:
        return None
    z = [0] * cols
    for i, c in enumerate(piv):
        z[c] = Mr[i][cols] % q
    for i in range(rows):
        if sum(A[i][j] * z[j] for j in range(cols)) % q != b[i] % q:
            return None
    return z


def poly_from_roots(roots, q):
    p = [1]
    for a in roots:
        np_ = [0] * (len(p) + 1)
        for i, c in enumerate(p):
            np_[i + 1] = (np_[i + 1] + c) % q
            np_[i] = (np_[i] - c * a) % q
        p = np_
    return p


def peval(p, x, q):
    s = 0
    for c in reversed(p):
        s = (s * x + c) % q
    return s


def mu(order, q):
    """the group of order-dividing-`order` roots of unity in F_q."""
    assert (q - 1) % order == 0
    gen = None
    for cand in range(2, q):
        seen = pow(cand, (q - 1) // order, q)
        ordr = 1
        cur = seen
        while cur != 1:
            cur = cur * seen % q
            ordr += 1
        if ordr == order:
            gen = seen
            break
    assert gen is not None
    out = [1]
    for _ in range(order - 1):
        out.append(out[-1] * gen % q)
    assert len(set(out)) == order
    return out


def layer_a_nullity(incidences, degz, degx, q):
    """E_I[(gamma,x),(i,t)] = gamma^i x^t, 0<=i<=degz, 0<=t<=degx."""
    E = [[pow(gm, i, q) * pow(x, t, q) % q
          for i in range(degz + 1) for t in range(degx + 1)]
         for gm, x in incidences]
    cols = (degz + 1) * (degx + 1)
    return cols - rank(E, q), cols


# ================================================== A/B: the H1(+H2) families
def build_h1h2(q, seed):
    """Return an H1+H2 exhibit or None."""
    rng = random.Random(seed)
    M32 = mu(32, q)
    m = 2
    rho = 4 * m - 1                     # 7
    for _attempt in range(60):
        pts = rng.sample(M32, 13)
        x0 = pts[0]                     # the shared point
        Sg = [x0] + pts[1:7]
        Sh = [x0] + pts[7:13]
        Wpts = sorted(set(Sg) | set(Sh))
        if len(Wpts) != 7 * m - 1:
            continue
        outside = [z for z in range(q) if z not in M32]
        g, h = rng.sample(outside, 2)
        sg = poly_from_roots(Sg, q)
        sh = poly_from_roots(Sh, q)
        gonly = [x for x in Sg if x != x0]
        honly = [x for x in Sh if x != x0]
        # five CROSS pairs (one point from each side) => every new slope has
        # exactly one point in S_g and one in S_h: pair-intersections <= 1.
        pairs = list(zip(gonly[:5], honly[:5]))
        single_g, single_h = gonly[5], honly[5]
        b = 1
        # Unknowns: C_0..C_7 (8) and a (1).  Conditions: C(x1_i)(tau_i - h) =
        # b*sigma_h(x1_i) and C(x2_i)(g - tau_i) = a*sigma_g(x2_i), i = 1..5.
        for tau5 in range(q):
            taus = [(3 + 7 * i) % q for i in range(4)] + [tau5]
            if len(set(taus)) != 5:
                continue
            if any(t in (g, h) for t in taus):
                continue
            A = []
            rhs = []
            ok = True
            for (x1, x2), tau in zip(pairs, taus):
                row = [pow(x1, t, q) * ((tau - h) % q) % q for t in range(8)]
                row.append(0)
                A.append(row)
                rhs.append(b * peval(sh, x1, q) % q)
                row2 = [pow(x2, t, q) * ((g - tau) % q) % q for t in range(8)]
                row2.append((-peval(sg, x2, q)) % q)
                A.append(row2)
                rhs.append(0)
            if not ok:
                continue
            z = solve_affine(A, rhs, q)
            if z is None:
                continue
            C = z[:8]
            a = z[8]
            if a % q == 0 or all(c % q == 0 for c in C):
                continue
            if any(peval(C, x, q) == 0 for x in Wpts):
                continue
            # induced second slopes
            slopes = {}
            for x in gonly:
                s2 = (h + b * peval(sh, x, q) * pow(peval(C, x, q), q - 2, q)) % q
                slopes.setdefault(s2, []).append(x)
            for x in honly:
                s2 = (g - a * peval(sg, x, q) * pow(peval(C, x, q), q - 2, q)) % q
                slopes.setdefault(s2, []).append(x)
            supports = {g: set(Sg), h: set(Sh)}
            clash = False
            for s2, xs in slopes.items():
                if s2 in (g, h):
                    clash = True
                    break
                supports[s2] = set(xs)
            if clash:
                continue
            prof = sorted((len(v) for v in supports.values()), reverse=True)
            if prof != [7, 7, 2, 2, 2, 2, 2, 1, 1]:
                continue
            if len(supports) != rho + 2:
                continue
            keys = list(supports)
            maxint = max(len(supports[keys[i]] & supports[keys[j]])
                         for i in range(len(keys))
                         for j in range(i + 1, len(keys)))
            if maxint != m - 1:
                continue
            inc = []
            for s2, S in supports.items():
                for x in S:
                    inc.append((s2, x))
            if len(inc) != 26:
                continue
            nul, cols = layer_a_nullity(inc, m, rho, q)
            return dict(q=q, Sg=Sg, Sh=Sh, g=g, h=h, C=C, a=a, b=b,
                        prof=prof, T=len(supports), maxint=maxint,
                        nullity=nul, cols=cols, rows=len(inc),
                        excess=len(inc) - cols)
    return None


def h1_census(q, seed, draws):
    """random admissible H1 builds: layer-A nullity must be exactly 1."""
    rng = random.Random(seed)
    M32 = mu(32, q)
    m, rho = 2, 7
    ok = 0
    for _ in range(draws):
        pts = rng.sample(M32, 13)
        x0 = pts[0]
        Sg = [x0] + pts[1:7]
        Sh = [x0] + pts[7:13]
        outside = [z for z in range(q) if z not in M32]
        g, h = rng.sample(outside, 2)
        sg = poly_from_roots(Sg, q)
        sh = poly_from_roots(Sh, q)
        C = [rng.randrange(q) for _ in range(8)]
        if any(peval(C, x, q) == 0 for x in set(Sg) | set(Sh)):
            continue
        a = rng.randrange(1, q)
        b = rng.randrange(1, q)
        supports = {g: set(Sg), h: set(Sh)}
        clash = False
        for x in Sg:
            if x == x0:
                continue
            s2 = (h + b * peval(sh, x, q) * pow(peval(C, x, q), q - 2, q)) % q
            if s2 in (g, h):
                clash = True
                break
            supports.setdefault(s2, set()).add(x)
        if clash:
            continue
        for x in Sh:
            if x == x0:
                continue
            s2 = (g - a * peval(sg, x, q) * pow(peval(C, x, q), q - 2, q)) % q
            if s2 in (g, h):
                clash = True
                break
            supports.setdefault(s2, set()).add(x)
        if clash:
            continue
        inc = [(s2, x) for s2, S in supports.items() for x in S]
        if len(inc) != 26:
            continue
        nul, _ = layer_a_nullity(inc, m, rho, q)
        if nul != 1:
            bad("H1 build at q=%d has nullity %d, want 1" % (q, nul))
        else:
            ok += 1
    return ok


# ============================================ C: the generalized fence at m=3
def fence_cell(m, q):
    N = 16 * m
    D = mu(N, q)
    rho = 4 * m - 1
    img = {}
    for x in D:
        img.setdefault(pow(x, 2 * m, q), []).append(x)
    fibres = sorted(img)
    if len(fibres) != 8:
        bad("fence m=%d: image size %d, want 8" % (m, len(fibres)))
        return None
    chosen = fibres[:4]
    pool = [x for v in chosen for x in img[v]]
    if len(pool) != 8 * m:
        bad("fence m=%d: 4 fibres give %d points, want %d"
            % (m, len(pool), 8 * m))
        return None
    # Gamma = the 4m m-th roots of the four fibre values, plus one spare
    Gamma = []
    for v in chosen:
        roots = [gm for gm in range(1, q) if pow(gm, m, q) == v % q]
        if len(roots) != m:
            bad("fence m=%d: value %d has %d m-th roots, want %d"
                % (m, v, len(roots), m))
            return None
        Gamma.extend(roots)
    if len(set(Gamma)) != 4 * m:
        bad("fence m=%d: |Gamma| = %d, want 4m" % (m, len(set(Gamma))))
        return None
    spare = next(z for z in range(1, q)
                 if z not in Gamma and pow(z, m, q) not in
                 [v % q for v in chosen])
    Gamma = sorted(set(Gamma)) + [spare]
    a = 7 * m - 1
    for start in range(len(pool) - a + 1):
        W = pool[start:start + a]
        inc = []
        okw = True
        for x in W:
            rs = [gm for gm in Gamma if (pow(gm, m, q) - pow(x, 2 * m, q)) % q == 0]
            if len(rs) != m:
                okw = False
                break
            inc.extend((gm, x) for gm in rs)
        if not okw:
            continue
        if len(inc) != m * a:
            continue
        nul, cols = layer_a_nullity(inc, m, rho, q)
        if nul == 2 * m:
            return dict(m=m, q=q, N=N, rho=rho, a=a, T=len(Gamma),
                        rows=len(inc), cols=cols, nullity=nul,
                        rank=cols - nul, excess=3 * m * m - 5 * m)
    bad("fence m=%d q=%d: no %d-point selection reached nullity 2m = %d"
        % (m, q, a, 2 * m))
    return None


# ===================================================================== main
h1_ok_97 = h1_census(97, 3701, 60)
h1_ok_193 = h1_census(193, 3702, 40)
if h1_ok_97 == 0 or h1_ok_193 == 0:
    bad("no admissible H1 builds were produced at one of the fields")

ex = build_h1h2(97, 3703)
if ex is None:
    bad("no H1+H2 exhibit found at q=97")
else:
    if ex["nullity"] != 1:
        bad("H1+H2 exhibit nullity %d, want 1" % ex["nullity"])
    if ex["excess"] != 2:
        bad("H1+H2 exhibit count excess %d, want 3m^2-5m = 2" % ex["excess"])

fen = fence_cell(3, 97)
if fen is not None:
    if fen["nullity"] != 6 or fen["rank"] != 42:
        bad("fence m=3 nullity/rank = %d/%d, want 6/42"
            % (fen["nullity"], fen["rank"]))
    if fen["rows"] != 60 or fen["cols"] != 48:
        bad("fence m=3 shape %dx%d, want 60x48" % (fen["rows"], fen["cols"]))
    if fen["excess"] != 3 * 9 - 5 * 3:
        bad("fence m=3 count excess wrong")

if FAIL:
    for m in FAIL:
        print("FAIL " + m)
    raise SystemExit(1)
print("LA_EQ_GEOMETRY_COUNTEREXAMPLES_PASS H1 nullity-1 on %d/%d (q=97) and "
      "%d/%d (q=193) admissible builds; H1+H2 exhibit q=97 profile=%s T=%d "
      "maxpairint=%d rows=%d cols=24 excess=+%d nullity=%d; generalized "
      "fence m=3 over mu_%d: a=%d T=%d %dx%d rank=%d nullity=%d=2m with "
      "count excess +%d"
      % (h1_ok_97, h1_ok_97, h1_ok_193, h1_ok_193, ex["prof"], ex["T"],
         ex["maxint"], ex["rows"], ex["excess"], ex["nullity"], fen["N"],
         fen["a"], fen["T"], fen["rows"], fen["cols"], fen["rank"],
         fen["nullity"], fen["excess"]))
