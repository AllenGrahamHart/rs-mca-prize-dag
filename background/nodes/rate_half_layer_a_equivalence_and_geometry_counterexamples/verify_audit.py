#!/usr/bin/env python3
"""Independent audit of the (LA-EQ) / geometry-counterexamples node.

Second code path, deliberately different from verify.py:
  - a DETERMINISTIC H1 build at the fresh field q = 577 (no random module):
    fixed supports from mu_32, the per-point incidences found by scanning
    the z-quadratic over the whole field, nullity asserted exactly 1;
  - the generalized fence replayed at a FRESH m = 4 cell over mu_64 at
    q = 193 (the draft verifier ran m = 3 only; m = 4 was banked upstream
    but never locally re-implemented): expected 108 x 80, nullity 8 = 2m;
  - freshly written construction and rank code (column order t-major,
    elimination written independently).

Run: tools/ramguard local -- python3 \
  background/nodes/rate_half_layer_a_equivalence_and_geometry_counterexamples/verify_audit.py
(RAMGUARD_TIMEOUT 300s)
"""


def rank(M, q):
    M = [row[:] for row in M]
    nr, nc = len(M), len(M[0])
    r = 0
    for c in range(nc):
        p = next((i for i in range(r, nr) if M[i][c] % q), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = pow(M[r][c], q - 2, q)
        M[r] = [x * inv % q for x in M[r]]
        for i in range(nr):
            if i != r and M[i][c] % q:
                f = M[i][c]
                M[i] = [(a - f * b) % q for a, b in zip(M[i], M[r])]
        r += 1
    return r


def mu(order, q):
    assert (q - 1) % order == 0
    for cand in range(2, q):
        g = pow(cand, (q - 1) // order, q)
        seen, cur = 1, g
        while cur != 1:
            cur = cur * g % q
            seen += 1
        if seen == order:
            out = [1]
            for _ in range(order - 1):
                out.append(out[-1] * g % q)
            return out
    raise AssertionError("no generator")


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


def nullity_t_major(incidences, degz, degx, q):
    # columns ordered t-major (x-power outer, z-power inner) -- a different
    # column order than verify.py's i-major layout
    E = [[pow(x, t, q) * pow(gm, i, q) % q
          for t in range(degx + 1) for i in range(degz + 1)]
         for gm, x in incidences]
    cols = (degx + 1) * (degz + 1)
    return cols - rank(E, q), cols


# ---- A: deterministic H1 build at q = 577
q = 577
M32 = mu(32, q)
m, rho = 2, 7
built = False
for shift in range(12):
    pts = M32[shift:shift + 13]
    x0 = pts[0]
    Sg, Sh = [x0] + pts[1:7], [x0] + pts[7:13]
    if len(set(Sg) | set(Sh)) != 13:
        continue
    outside = [z for z in range(2, q) if z not in M32]
    g, h = outside[0], outside[1]
    sg, sh = poly_from_roots(Sg, q), poly_from_roots(Sh, q)
    a_, b_ = 1, 1
    C = [(3 * i + shift + 1) % q for i in range(rho + 1)]
    # Q(z,x) = (z-g)(z-h)C(x) + a(z-h)sg(x) - b(z-g)sh(x)
    def Q(z, x):
        return ((z - g) * (z - h) % q * peval(C, x, q)
                + a_ * (z - h) * peval(sg, x, q)
                - b_ * (z - g) * peval(sh, x, q)) % q
    W = sorted(set(Sg) | set(Sh))
    inc = []
    ok = True
    for x in W:
        roots = [z for z in range(q) if Q(z, x) == 0]
        if len(roots) != 2:
            ok = False
            break
        inc.extend((z, x) for z in roots)
    if not ok:
        continue
    assert len(inc) == 26
    nul, cols = nullity_t_major(inc, m, rho, q)
    assert cols == 24
    assert nul == 1, "H1 build at q=577 has nullity %d, want exactly 1" % nul
    built = True
    break
assert built, "no admissible deterministic H1 build found at q=577"

# ---- B: the generalized fence at fresh m = 4, q = 193
mq, q4 = 4, 193
N = 16 * mq
D = mu(N, q4)
rho4 = 4 * mq - 1
img = {}
for x in D:
    img.setdefault(pow(x, 2 * mq, q4), []).append(x)
fibres = sorted(img)
assert len(fibres) == 8, len(fibres)
chosen = fibres[:4]
pool = [x for v in chosen for x in img[v]]
assert len(pool) == 8 * mq
Gamma = []
for v in chosen:
    roots = [gm for gm in range(1, q4) if pow(gm, mq, q4) == v % q4]
    assert len(roots) == mq, (v, len(roots))
    Gamma.extend(roots)
assert len(set(Gamma)) == 4 * mq
spare = next(z for z in range(1, q4)
             if z not in Gamma and pow(z, mq, q4) not in
             [v % q4 for v in chosen])
Gamma = sorted(set(Gamma)) + [spare]
a4 = 7 * mq - 1
hit = False
for start in range(len(pool) - a4 + 1):
    W4 = pool[start:start + a4]
    inc4 = []
    ok = True
    for x in W4:
        rs = [gm for gm in Gamma
              if (pow(gm, mq, q4) - pow(x, 2 * mq, q4)) % q4 == 0]
        if len(rs) != mq:
            ok = False
            break
        inc4.extend((gm, x) for gm in rs)
    if not ok or len(inc4) != mq * a4:
        continue
    nul4, cols4 = nullity_t_major(inc4, mq, rho4, q4)
    assert cols4 == 80 and len(inc4) == 108
    assert nul4 == 2 * mq, "fence m=4 nullity %d, want 8" % nul4
    hit = True
    break
assert hit, "no admissible m=4 fence selection found"

print(
    "RATE_HALF_LAYER_A_EQUIVALENCE_GEOMETRY_AUDIT_PASS "
    "deterministic H1 build q=577 nullity=1 (26x24, excess +2); "
    "fresh fence cell m=4 over mu_64 q=193: 108x80 nullity=8=2m"
)
