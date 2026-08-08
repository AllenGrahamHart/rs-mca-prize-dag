#!/usr/bin/env python3
"""NORMRES — the 2-adic residue law of box norms, and what it does to v2(p-1).
Measured, not assumed.  This decides whether the forward hunt can ever reach a
DEPLOYED-scale row (which needs v2(p-1) >= 41)."""
import random
import sys
from collections import Counter
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K

rng = random.Random(20260808)
H = 64
M = 4000


def v2(n):
    return (n & -n).bit_length() - 1


def report(name, gen):
    c256, c512, vs, vodd = Counter(), Counter(), Counter(), Counter()
    for _ in range(M):
        w = gen()
        n = abs(K.tower_norm(w))
        if n % 2 == 0:
            continue
        c256[n % 256] += 1
        c512[n % 512] += 1
        vs[v2(n - 1)] += 1
        if n % 128 == 1:
            vodd[v2(n - 1)] += 1
    print("%-28s  N mod 256: %s" % (name, dict(sorted(c256.items()))))
    print("%-28s  v2(N-1) overall: %s" % ("", dict(sorted(vs.items()))))
    print("%-28s  v2(N-1) | N=1 mod 128: %s" % ("", dict(sorted(vodd.items()))))


report("FAM-B  (nodd=1, S=253)", lambda: K.fam_B(H, rng))
report("FAM-C  (nodd=3, S=247)", lambda: K.fam_C(H, rng, 3))
report("nodd=5", lambda: K.fam_C(H, rng, 5))
report("nodd=7", lambda: K.fam_C(H, rng, 7))
report("nodd=1 at index 0 only", lambda: [rng.choice((-1, 1))] +
       [rng.choice((-2, 2)) for _ in range(H - 1)])
report("sparse s=27 (+-1)", lambda: K.fam_S(H, rng, 27))
report("sparse s=13 (+-1)", lambda: K.fam_S(H, rng, 13))
report("uniform box (odd norms)", lambda: K.fam_A(H, rng))

# the exact algebraic prediction: N = a^64 + 64 a^63 (w_0 - a) + ... ?
print("\ncheck N vs a^64 mod 512, a = w(1):")
c = Counter()
for _ in range(2000):
    w = K.fam_B(H, rng)
    n = abs(K.tower_norm(w))
    if n % 2 == 0:
        continue
    a = sum(w)
    c[(n - pow(a, 64, 512)) % 512] += 1
print(dict(sorted(c.items())))
