"""Exact orbit count of the norm-preserving group on the box {-2..2}^h.

SELF-CORRECTION: in d1_toy.py I bounded #orbits by 5^h/|G| + 5^{h/2}; the
5^{h/2} term is WRONG in general (an affine index map i -> si+a can have
gcd(s-1,h) fixed points, so cycles can be far from length 2).  Burnside is
computed EXACTLY here instead, so the 13-bit refinement is rigorous.

G = { w -> x^a sigma_s(w) : a in Z/2h, s in (Z/2h)^* },  |G| <= 2h^2.
Each g sends x^i -> eps_i x^{pi(i)}; Fix(g) = product over cycles of
(5 if the sign product round the cycle is +1 else 1).
"""
import math

for h in (8, 16, 32, 64):
    N2 = 2 * h
    seen = {}
    total = 0
    nelem = 0
    for s in range(1, N2, 2):
        if math.gcd(s, N2) != 1:
            continue
        for a in range(N2):
            # basis map
            pi = [0] * h
            eps = [1] * h
            for i in range(h):
                k = (s * i + a) % N2
                if k >= h:
                    k -= h
                    eps[i] = -1
                pi[i] = k
            key = (tuple(pi), tuple(eps))
            if key in seen:
                continue
            seen[key] = 1
            nelem += 1
            # cycle decomposition with sign products
            un = [True] * h
            fix = 1
            for i in range(h):
                if not un[i]:
                    continue
                j = i
                sg = 1
                ln = 0
                while un[j]:
                    un[j] = False
                    sg *= eps[j]
                    j = pi[j]
                    ln += 1
                if sg == 1:
                    fix *= 5
            total += fix
    orbits = total / nelem
    print("h=%3d  |G|=%5d  exact #orbits = 2^%.4f   (5^h/|G| = 2^%.4f, "
          "excess %+.4f bits)"
          % (h, nelem, math.log2(orbits), h * math.log2(5) - math.log2(nelem),
             math.log2(orbits) - (h * math.log2(5) - math.log2(nelem))))
