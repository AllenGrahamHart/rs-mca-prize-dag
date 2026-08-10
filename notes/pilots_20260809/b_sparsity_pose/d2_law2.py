"""D2 — LAW 2 for general w (named gap 1).

s(w) := ((Norm(w)-1)/(2h)) mod 2   for odd Norm(w)   [LAW 1 makes this legal]

Registered chain (PREREG R3):
  P1  s is a homomorphism: s(w1 w2) = s(w1) + s(w2)
  P2  s(w) = sigma(u) + (u^{-1} z)_{h/2},  u = w mod 2, z = ((w-uhat)/2) mod 2
  P2' consequently s(w) depends only on w mod 4
  P3  GUESS-G: sigma(u) = #{i<j : u_i=u_j=1, i+j = h/2 mod h} mod 2

F_2[x]/(x^h+1) = F_2[x]/(x^h-1): reduction is CYCLIC over F_2.  Units are the
u with u(1)=1; u^{-1} = prod_{j<k} u(x^{2^j}) for 2^k >= h.
"""
import random, itertools, math

random.seed(20260809)


def negmul(a, b, h):
    c = [0] * h
    for i in range(h):
        ai = a[i]
        if not ai:
            continue
        for j in range(h):
            bj = b[j]
            if not bj:
                continue
            k = i + j
            if k < h:
                c[k] += ai * bj
            else:
                c[k - h] -= ai * bj
    return c


def tower_norm(w):
    w = list(w)
    h = len(w)
    while h > 1:
        wm = [w[i] if i % 2 == 0 else -w[i] for i in range(h)]
        p = negmul(w, wm, h)
        w = [p[2 * i] for i in range(h // 2)]
        h //= 2
    return w[0]


def s_of(w):
    h = len(w)
    N = tower_norm(w)
    assert N % 2 == 1, "even norm"
    assert (N - 1) % (2 * h) == 0, "LAW 1 violated"
    return ((N - 1) // (2 * h)) % 2


# ---- F_2[x]/(x^h-1) as bitmasks
def f2mul(a, b, h):
    c = 0
    for i in range(h):
        if (a >> i) & 1:
            c ^= ((b << i) | (b >> (h - i))) & ((1 << h) - 1)
    return c


def f2frob(a, h, e):
    """a(x^{2^e}) mod x^h-1"""
    r = 0
    m = pow(2, e, h) if h else 0
    for i in range(h):
        if (a >> i) & 1:
            r ^= 1 << ((i * pow(2, e)) % h)
    return r


def f2inv(a, h):
    k = 1
    while (1 << k) < h:
        k += 1
    r = 1
    for j in range(k):
        r = f2mul(r, f2frob(a, h, j), h)
    assert f2mul(r, a, h) == 1
    return r


def bits(v):
    return [(v >> i) & 1 for i in range(v.bit_length())]


def guessG(u, h):
    """#{i<j : u_i=u_j=1, i+j = h/2 mod h} mod 2"""
    idx = [i for i in range(h) if (u >> i) & 1]
    c = 0
    for a in range(len(idx)):
        for b in range(a + 1, len(idx)):
            if (idx[a] + idx[b] - h // 2) % h == 0:
                c ^= 1
    return c


def decomp(w):
    h = len(w)
    u = 0
    for i in range(h):
        if w[i] % 2:
            u |= 1 << i
    uhat = [(w[i] % 2) for i in range(h)]
    z = 0
    for i in range(h):
        t = (w[i] - uhat[i]) // 2
        if t % 2:
            z |= 1 << i
    return u, uhat, z


def sigma(u, h):
    return s_of([(u >> i) & 1 for i in range(h)])


print("=== P1: homomorphism  s(w1 w2) = s(w1)+s(w2) ===")
for h in (4, 8, 16, 32):
    bad = n = 0
    while n < (400 if h <= 16 else 120):
        w1 = [random.randint(-4, 4) for _ in range(h)]
        w2 = [random.randint(-4, 4) for _ in range(h)]
        if sum(w1) % 2 == 0 or sum(w2) % 2 == 0:
            continue
        n += 1
        pr = negmul(w1, w2, h)
        if s_of(pr) != (s_of(w1) ^ s_of(w2)):
            bad += 1
    print("  h=%2d  %4d products, violations %d" % (h, n, bad))

print("=== P2 / P2': the reduction, and dependence on w mod 4 only ===")
for h in (4, 8, 16, 32, 64):
    bad2 = bad2p = n = 0
    lim = 300 if h <= 16 else (120 if h == 32 else 40)
    while n < lim:
        w = [random.randint(-5, 5) for _ in range(h)]
        if sum(w) % 2 == 0:
            continue
        n += 1
        u, uhat, z = decomp(w)
        lhs = s_of(w)
        rhs = sigma(u, h) ^ ((f2mul(f2inv(u, h), z, h) >> (h // 2)) & 1)
        if lhs != rhs:
            bad2 += 1
        w4 = [w[i] + 4 * random.randint(-3, 3) for i in range(h)]
        if s_of(w4) != lhs:
            bad2p += 1
    print("  h=%2d  %4d samples: P2 violations %d ; P2' (mod-4) violations %d"
          % (h, n, bad2, bad2p))

print("=== P3: GUESS-G for sigma(u) ===")
for h in (4, 8, 16):
    bad = tot = 0
    rows = []
    for u in range(1 << h):
        if bin(u).count("1") % 2 == 0:
            continue
        tot += 1
        sg = sigma(u, h)
        gg = guessG(u, h)
        if sg != gg:
            bad += 1
            if len(rows) < 6:
                rows.append((u, [(u >> i) & 1 for i in range(h)], sg, gg))
    print("  h=%2d  exhaustive odd-weight u: %d, GUESS-G violations %d" % (h, tot, bad))
    for r in rows:
        print("        u=%s sigma=%d guess=%d" % (r[1], r[2], r[3]))
    if h == 8 and bad:
        # tabulate sigma by weight for the fit
        byw = {}
        for u in range(1 << h):
            if bin(u).count("1") % 2 == 0:
                continue
            byw.setdefault(bin(u).count("1"), []).append((u, sigma(u, h)))
        for wt in sorted(byw):
            ones = sum(v for _, v in byw[wt])
            print("        weight %d: %d vectors, sigma=1 for %d" % (wt, len(byw[wt]), ones))
