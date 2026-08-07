#!/usr/bin/env python3
"""D4 -- THE CONE GEOMETRY.  Does a standard lattice tool decide D3's toy
certification, and at what cost against brute force?

Lattice:  Lambda_p = { w in Z^h : w(zeta) = 0 mod p },  zeta of order N' = 2h
in F_p (p = 1 mod N').  Basis rows  (p,0,..,0) and (-zeta^j, .. ,1 at j, ..),
so det Lambda_p = p, dimension h.

Certification question (exactly D3's):  is there w != 0 in Lambda_p with
||w||_inf <= 2 and ||w||_1 <= 2l' ?   ||w||_inf <= 2 implies ||w||_2^2 <= 4h,
so Fincke-Pohst on the ball of radius^2 = min(4h, 4l') is a SUPERSET; the box
and the l_1 budget are applied as extra pruning inside the enumeration.

Everything exact: LLL and the Fincke-Pohst bounds run over Fraction.
FPCOST = enumeration nodes visited.  BFCOST = 5^h (the brute-force box).
"""
import sys
from fractions import Fraction

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from gelib import tower_norm


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def gso(B):
    n = len(B)
    Bs = []
    mu = [[Fraction(0)] * n for _ in range(n)]
    for i in range(n):
        v = [Fraction(x) for x in B[i]]
        for j in range(i):
            mu[i][j] = Fraction(dot([Fraction(x) for x in B[i]], Bs[j]),
                                1) / dot(Bs[j], Bs[j])
            v = [v[k] - mu[i][j] * Bs[j][k] for k in range(n)]
        Bs.append(v)
    return Bs, mu


def lll(B, delta=Fraction(99, 100)):
    B = [list(r) for r in B]
    n = len(B)
    Bs, mu = gso(B)
    k = 1
    while k < n:
        for j in range(k - 1, -1, -1):
            q = mu[k][j]
            r = int(q + Fraction(1, 2)) if q >= 0 else -int(-q + Fraction(1, 2))
            if r:
                B[k] = [B[k][t] - r * B[j][t] for t in range(n)]
                Bs, mu = gso(B)
        if dot(Bs[k], Bs[k]) >= (delta - mu[k][k - 1] ** 2) * dot(Bs[k - 1],
                                                                  Bs[k - 1]):
            k += 1
        else:
            B[k], B[k - 1] = B[k - 1], B[k]
            Bs, mu = gso(B)
            k = max(k - 1, 1)
    return B, Bs, mu


def zeta_of_order(N, p):
    for g in range(2, p):
        c = pow(g, (p - 1) // N, p)
        if pow(c, N // 2, p) == p - 1:
            return c
    return None


def certify(h, p, L, use_lll=True):
    """Enumerate every w != 0 in Lambda_p with ||w||_inf <= 2, ||w||_1 <= L.
    Returns (witnesses, FPCOST)."""
    N = 2 * h
    z = zeta_of_order(N, p)
    assert z is not None
    B = [[0] * h for _ in range(h)]
    B[0][0] = p
    for j in range(1, h):
        B[j][0] = (-pow(z, j, p)) % p
        B[j][j] = 1
    if use_lll:
        B, Bs, mu = lll(B)
    else:
        Bs, mu = gso(B)
    R2 = Fraction(min(4 * h, 2 * L))
    nodes = [0]
    found = []
    x = [0] * h

    def rec(i, partial):
        """partial = sum_{j>i} (x_j + sum_{k>j} mu[k][j] x_k)^2 |b*_j|^2"""
        nodes[0] += 1
        if i < 0:
            w = [0] * h
            for t in range(h):
                if x[t]:
                    for u in range(h):
                        w[u] += x[t] * B[t][u]
            if any(w) and max(abs(t) for t in w) <= 2 and \
               sum(abs(t) for t in w) <= L:
                found.append(tuple(w))
            return
        c = sum(mu[j][i] * x[j] for j in range(i + 1, h))
        rem = R2 - partial
        if rem < 0:
            return
        bi = dot(Bs[i], Bs[i])
        # (x_i + c)^2 * bi <= rem
        lim = rem / bi
        # integer window around -c
        r = 0
        while Fraction((r) ** 2) > lim and r > 0:
            r -= 1
        hi = 0
        while Fraction((hi + 1) ** 2) <= lim:
            hi += 1
        lo_v = -c - hi
        hi_v = -c + hi
        a = -((-lo_v).__floor__()) if False else None
        import math as _m
        start = _m.ceil(lo_v)
        end = _m.floor(hi_v)
        for xi in range(start, end + 1):
            x[i] = xi
            rec(i - 1, partial + (Fraction(xi) + c) ** 2 * bi)
        x[i] = 0

    rec(h - 1, Fraction(0))
    return found, nodes[0]


def main():
    rows = [
        (4, 137, 8, "N'=8, p=137 = TIGHTEMPTY(8): a witness MUST exist"),
        (4, 401, 8, "N'=8, p=401 > TIGHTEMPTY: certified EMPTY"),
        (8, 12289, 6, "N'=16, p=12289, 2l'=6: the banked C-4 anchor"),
        (8, 12289, 16, "N'=16, p=12289, full radius"),
        (8, 463249, 16, "N'=16, p=463249 = TIGHTEMPTY(16): witness MUST exist"),
        (8, 463457, 16, "N'=16, p=463457 > TIGHTEMPTY: certified EMPTY"),
    ]
    print("== D4: Fincke-Pohst on the kernel lattice vs brute force ==")
    print("%-6s %-9s %-5s %-9s %-12s %-14s %-8s" %
          ("h", "p", "2l'", "witnesses", "FPCOST", "BFCOST=5^h", "speedup"))
    for (h, p, L, why) in rows:
        w, nodes = certify(h, p, L)
        bf = 5 ** h
        print("%-6d %-9d %-5d %-9d %-12d %-14d %-8.1fx   %s" %
              (h, p, L, len(w), nodes, bf, bf / nodes, why))
        if w:
            ws = sorted(w)[0]
            print("        witness w = %s   Norm = %d   p | Norm ? %s" %
                  (ws, tower_norm(list(ws)), tower_norm(list(ws)) % p == 0))
    print("\n(FPCOST counts enumeration nodes; BFCOST counts box vectors. Both")
    print(" are exhaustive over the SAME question, so the ratio is honest.)")


if __name__ == "__main__":
    main()
