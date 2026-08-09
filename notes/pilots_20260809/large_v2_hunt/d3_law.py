#!/usr/bin/env python3
"""D3 - THE 2-ADIC LAW OF v_2(Norm(w) - 1), tested by exact measurement.

Derivation (Newton's identities + Tr(z) = h*z_0 on Z[x]/(x^h+1)):
for w with EXACTLY ONE odd coordinate at position j, w = eps*x^j + 2u with
u in {-1,0,1}^h, u_j = 0.  Then Norm(w) = Norm(1 + 2v), v = eps*u*x^{-j},
v_0 = 0, and
      Norm(1+2v) = 1 + 128*(v_0 - (v^2)_0)  mod 256
with (v^2)_0 = v_0^2 - v_{h/2}^2 - 2*sum_{0<i<h/2} v_i v_{h-i}, so
      v_2(Norm(w) - 1) >= 8   <==>   u_{(j + h/2) mod h} = 0
      i.e.                            w_{(j + h/2) mod h} = 0.
FAM-B has no zero coordinate, so the prediction is v_2 == 7 IDENTICALLY.
"""
import random
import sys
from collections import Counter
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K  # noqa: E402

H = 64
rng = random.Random(20260809)


def v2(n):
    return (n & -n).bit_length() - 1


def mk_zero(rng, at_j32):
    """nodd = 1 at position j; exactly one ZERO coordinate, placed either at
    j+32 (predicted v2 >= 8) or at a position != j, j+32 (predicted v2 = 7)."""
    j = rng.randrange(H)
    w = [rng.choice((-2, 2)) for _ in range(H)]
    w[j] = rng.choice((-1, 1))
    if at_j32:
        w[(j + H // 2) % H] = 0
    else:
        while True:
            z = rng.randrange(H)
            if z != j and z != (j + H // 2) % H:
                break
        w[z] = 0
    return w


def prof(name, gen, M=3000):
    c = Counter()
    split = Counter()
    for _ in range(M):
        w = gen()
        n = abs(K.tower_norm(w))
        if n == 0 or n % 2 == 0:
            continue
        g = v2(n - 1)
        c[g] += 1
        odd = [i for i in range(H) if w[i] % 2]
        if len(odd) == 1:
            j = odd[0]
            split[(w[(j + H // 2) % H] == 0, g >= 8)] += 1
    print("%-32s v2(Norm-1): %s" % (name, dict(sorted(c.items()))))
    if split:
        print("%-32s   (w_{j+32}==0, v2>=8) -> %s"
              % ("", dict(sorted(split.items()))))


prof("FAM-B nodd=1 no zeros", lambda: K.fam_B(H, rng))
prof("nodd=1, ZERO at j+32", lambda: mk_zero(rng, True))
prof("nodd=1, ZERO elsewhere", lambda: mk_zero(rng, False))
prof("FAM-C nodd=3", lambda: K.fam_C(H, rng, 3))
prof("nodd=5", lambda: K.fam_C(H, rng, 5))
prof("sparse s=27 (+-1)", lambda: K.fam_S(H, rng, 27))
prof("uniform box FAM-A", lambda: K.fam_A(H, rng))
