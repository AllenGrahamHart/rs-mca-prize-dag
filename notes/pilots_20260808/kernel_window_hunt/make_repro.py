#!/usr/bin/env python3
"""Emit repro_witness.py: a STANDALONE checker with literal constants and
ZERO imports from this pilot's library (PREREG P5.6)."""
import json
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else "best_witness"
DST = sys.argv[2] if len(sys.argv) > 2 else "repro_witness"
BW = json.load(open("notes/pilots_20260808/kernel_window_hunt/state/%s.json" % SRC))
w = BW["w"]
p = int(BW["p"])

TPL = '''#!/usr/bin/env python3
"""STANDALONE reproduction of the round-24 kernel_window_hunt witness.

Imports NOTHING but `random` (for Miller-Rabin bases).  Re-derives every claim
from the two literal constants below.  Run:

    tools/ramguard tiny -- python3 notes/pilots_20260808/kernel_window_hunt/repro_witness.py
"""
import random

# ---------------------------------------------------------------- CONSTANTS
W = %(w)r

P = %(p)d

H = len(W)          # folded dimension
NPRIME = 2 * H      # quotient order N'
SMAX = 4 * (H - 1) + 1        # largest sum w_i^2 with an odd coordinate
CEIL = SMAX ** (H // 2)       # the odd-case AM-GM ceiling (253^32 at H=64)


# ------------------------------------------------- exact norm, from scratch
def negasq(a):
    """Square in Z[y]/(y^m + 1), m = len(a)."""
    m = len(a)
    c = [0] * m
    for i in range(m):
        if a[i] == 0:
            continue
        for j in range(m):
            if a[j] == 0:
                continue
            s = i + j
            if s < m:
                c[s] += a[i] * a[j]
            else:
                c[s - m] -= a[i] * a[j]
    return c


def norm(w):
    """Norm_{Q(zeta_2h)/Q}(sum w_i x^i) by the 2-adic tower.  Exact integers."""
    n = len(w)
    while n > 1:
        m = n >> 1
        A, B = negasq(w[0::2]), negasq(w[1::2])
        u = [A[0] + B[m - 1]]
        for i in range(1, m):
            u.append(A[i] - B[i - 1])
        w, n = u, m
    return w[0]


# --------------------------------------------------------------- primality
def mr(n, a):
    d, s = n - 1, 0
    while d %% 2 == 0:
        d //= 2
        s += 1
    x = pow(a, d, n)
    if x in (1, n - 1):
        return True
    for _ in range(s - 1):
        x = x * x %% n
        if x == n - 1:
            return True
    return False


def jacobi(a, n):
    a %%= n
    r = 1
    while a:
        while a %% 2 == 0:
            a //= 2
            if n %% 8 in (3, 5):
                r = -r
        a, n = n, a
        if a %% 4 == 3 and n %% 4 == 3:
            r = -r
        a %%= n
    return r if n == 1 else 0


def strong_lucas(n):
    D = 5
    while jacobi(D, n) != -1:
        D = -(D + 2) if D > 0 else -(D - 2)
    P_, Q = 1, (1 - D) // 4
    d, s = n + 1, 0
    while d %% 2 == 0:
        d //= 2
        s += 1
    U, V, Qk = 1, P_ %% n, Q %% n
    for bit in bin(d)[3:]:
        U, V = U * V %% n, (V * V - 2 * Qk) %% n
        Qk = Qk * Qk %% n
        if bit == "1":
            U, V = (P_ * U + V), (D * U + P_ * V)
            if U %% 2:
                U += n
            if V %% 2:
                V += n
            U, V = (U >> 1) %% n, (V >> 1) %% n
            Qk = Qk * Q %% n
    if U == 0 or V == 0:
        return True
    for _ in range(s - 1):
        V = (V * V - 2 * Qk) %% n
        if V == 0:
            return True
        Qk = Qk * Qk %% n
    return False


# ------------------------------------------------------------------ checks
def main():
    ok = True

    def ck(name, cond, extra=""):
        nonlocal ok
        ok = ok and bool(cond)
        print(("PASS " if cond else "FAIL ") + name + ("  " + extra if extra else ""))

    ck("w is a nonzero vector in {-2..2}^H",
       len(W) == H and any(W) and all(-2 <= t <= 2 for t in W))
    l1 = sum(abs(t) for t in W)
    ck("||w||_1 = %%d <= 2l' = %%d (full N' radius)" %% (l1, NPRIME), l1 <= NPRIME)
    ck("S = sum w_i^2 = %%d <= %%d (odd-coordinate case of the AM-GM bound)"
       %% (sum(t * t for t in W), SMAX), sum(t * t for t in W) <= SMAX)

    N = abs(norm(W))
    ck("Norm(w) has %%d bits" %% N.bit_length(), N.bit_length() > 0)
    ck("|Norm(w)| <= S^(H/2) (AM-GM / Parseval ceiling)",
       N <= sum(t * t for t in W) ** (H // 2))
    ck("P divides Norm(w)", N %% P == 0, "cofactor = %%d" %% (N // P))

    ck("P = 1 mod N' (a primitive N'-th root exists in F_P)", P %% NPRIME == 1)
    ck("P < 2^256 (spec field cap |F| < 2^256)", P < 2 ** 256)
    ck("P <= (4(H-1)+1)^(H/2) (the odd-case norm ceiling; = 253^32 at H=64, "
       "the PROVED high-field emptiness threshold)", P <= CEIL)
    v2 = ((P - 1) & -(P - 1)).bit_length() - 1
    print("     v2(P-1) = %%d  -> the largest power-of-two smooth domain is n = 2^%%d"
          %% (v2, v2))

    prp = mr(P, 2) and strong_lucas(P)
    rng = random.Random(20260808)
    for _ in range(64):
        prp = prp and mr(P, rng.randrange(2, P - 1))
    ck("P is a BPSW + 64-round Miller-Rabin PROBABLE PRIME (not a proof)", prp)

    # kernel membership: rho of exact order 128, and an odd s with w(rho^s) = 0
    e = (P - 1) // NPRIME
    rho = None
    for g in range(2, 500):
        r = pow(g, e, P)
        if pow(r, NPRIME // 2, P) == P - 1:
            rho = r
            break
    ck("found rho with rho^(N'/2) = -1 mod P (exact order N')", rho is not None)
    hit = None
    for s in range(1, NPRIME, 2):
        rs = pow(rho, s, P)
        acc, cur = 0, 1
        for j in range(H):
            acc = (acc + W[j] * cur) %% P
            cur = cur * rs %% P
        if acc %% P == 0:
            hit = s
            break
    ck("sum_j w_j (rho^s)^j = 0 mod P for an odd s", hit is not None,
       "s = %%s" %% hit)

    # the ternary lift: v in {-1,0,1}^128 with v_i - v_{i+64} = w_i
    v = [0] * NPRIME
    for i, t in enumerate(W):
        if t == 2:
            v[i], v[i + H] = 1, -1
        elif t == -2:
            v[i], v[i + H] = -1, 1
        elif t == 1:
            v[i] = 1
        elif t == -1:
            v[i] = -1
    zeta = pow(rho, hit, P)
    acc, cur = 0, 1
    for j in range(NPRIME):
        acc = (acc + v[j] * cur) %% P
        cur = cur * zeta %% P
    ck("the ternary lift v in {-1,0,1}^N' satisfies sum_j v_j zeta^j = 0 mod P",
       acc %% P == 0)
    ck("supp(v) = ||w||_1 = %%d" %% l1, sum(1 for t in v if t) == l1)
    ck("v is NON-CYCLOTOMIC (v_i != v_{i+H} for some i)",
       any(v[i] != v[i + H] for i in range(H)))

    print()
    print("WITNESS_REPRO %%s" %% ("PASS" if ok else "FAIL"))
    print("A non-cyclotomic ternary kernel vector exists at the admissible row")
    print("prime P (%%d bits, P = 1 mod %%d, P < 2^256)." %% (P.bit_length(), NPRIME))


main()
'''

open("notes/pilots_20260808/kernel_window_hunt/%s.py" % DST, "w").write(
    TPL % {"w": w, "p": p})
print("wrote %s.py for p =" % DST, p, "(%d bits)" % p.bit_length())
