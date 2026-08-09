"""D2 continued — determine sigma(u) exactly.

GUESS-G (P3) is REFUTED.  sigma is a Boolean function of the (x+1)-adic
coordinates: write u = sum_k a_k y^k, y = x+1 over F_2, a_0 = 1 forced by
u(1)=1, so sigma is a Boolean function of (a_1..a_{h-1}).  Compute its exact
algebraic normal form by the Moebius transform at h=4,8,16 and read the
pattern; then test the conjectured general form out-of-sample at h=32,64.
"""
import sys

sys.setrecursionlimit(10000)


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
    return ((N - 1) // (2 * h)) % 2


def u_from_a(a, h):
    """a is an int bitmask over k=0..h-1 (bit0 = a_0); returns u bitmask."""
    u = 0
    for k in range(h):
        if (a >> k) & 1:
            # y^k = (x+1)^k : coefficients C(k,i) mod 2
            for i in range(k + 1):
                # C(k,i) mod 2 = 1 iff (i & ~k) == 0  (Lucas)
                if (i & ~k) == 0:
                    u ^= 1 << i
    return u


for h in (4, 8, 16):
    n = h - 1                       # free variables a_1..a_{h-1}
    tt = [0] * (1 << n)
    for m in range(1 << n):
        a = 1 | (m << 1)
        u = u_from_a(a, h)
        tt[m] = s_of([(u >> i) & 1 for i in range(h)])
    # Moebius transform -> ANF
    anf = tt[:]
    step = 1
    while step < (1 << n):
        for i in range(1 << n):
            if i & step:
                anf[i] ^= anf[i ^ step]
        step <<= 1
    terms = [m for m in range(1 << n) if anf[m]]
    print("h=%2d : sigma has %d ANF terms; degree %d"
          % (h, len(terms), max((bin(m).count('1') for m in terms), default=0)))
    for m in sorted(terms, key=lambda t: (bin(t).count('1'), t)):
        ks = [k + 1 for k in range(n) if (m >> k) & 1]
        print("      a_%s" % "*a_".join(map(str, ks)))
