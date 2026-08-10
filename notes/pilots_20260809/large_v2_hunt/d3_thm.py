#!/usr/bin/env python3
"""D3 - the two laws, tested as IDENTITIES (arbitrary integer coefficients,
several h), not just on the box.

LAW 1 (NORMLAW, elementary proof).  Norm(w) > 0, and every odd prime p with
p^e || Norm(w) has f = ord(p mod 2h) dividing e with p^f = 1 mod 2h; hence
Norm(w) = 1 mod 2h whenever Norm(w) is odd.

LAW 2 (NEW, the v_2(Norm-1) refinement).  For v in Z[x]/(x^h+1), h a power
of 2 >= 2,
        Norm(1 + 2v)  =  1 + 2h * v_{h/2}   (mod 4h).
Proof: Newton's identities with p_k = Tr(v^k) = h*(v^k)_0 give
2c_1 = 2h v_0, 4c_2 = 2h^2 v_0^2 - 2h (v^2)_0 = -2h (v^2)_0 mod 4h, and
v_2(2^k c_k) >= log2(4h) for k >= 3; then
v_0 - (v^2)_0 = v_0 - v_0^2 + v_{h/2}^2 + 2(...) = v_{h/2} mod 2.
COROLLARY: v_2(Norm(1+2v) - 1) >= log2(4h)  <=>  v_{h/2} even.
"""
import random
import sys
sys.path.insert(0, "notes/pilots_20260807/ge_floor_falsifier")
from gelib import tower_norm  # noqa: E402

rng = random.Random(20260809)
print("LAW 2 as an identity: Norm(1+2v) = 1 + 2h*v_{h/2} mod 4h")
for h in (2, 4, 8, 16, 32, 64):
    bad = 0
    badc = 0
    T = 4000 if h <= 16 else 600
    for _ in range(T):
        v = [rng.randrange(-9, 10) for _ in range(h)]
        w = [2 * t for t in v]
        w[0] += 1
        n = tower_norm(w)
        if n == 0 or n % 2 == 0:
            continue
        if n % (4 * h) != (1 + 2 * h * v[h // 2]) % (4 * h):
            bad += 1
        ge = ((n - 1) % (4 * h) == 0)
        if ge != (v[h // 2] % 2 == 0):
            badc += 1
    print("   h=%3d  (2h=%4d, 4h=%4d)  violations of LAW 2: %d/%d   "
          "corollary violations: %d" % (h, 2 * h, 4 * h, bad, T, badc))

print("\nLAW 1 on random NON-box vectors (large coefficients):")
for h in (8, 16, 32, 64):
    bad = tot = 0
    for _ in range(600):
        w = [rng.randrange(-40, 41) for _ in range(h)]
        n = tower_norm(w)
        if n == 0 or n % 2 == 0:
            continue
        tot += 1
        if n % (2 * h) != 1:
            bad += 1
    print("   h=%3d  odd norms %d, violations of Norm = 1 mod 2h: %d"
          % (h, tot, bad))

print("\nGeneralised criterion for the BOX, nodd = 1 at position j:")
print("   w = eps*x^j + 2u  =>  v = eps*u*x^{-j}, v_{h/2} = +-u_{(j+h/2) mod h}")
h = 64
bad = 0
for _ in range(3000):
    j = rng.randrange(h)
    w = [rng.choice((-2, -1, 0, 1, 2)) for _ in range(h)]
    for i in range(h):
        if w[i] % 2 and i != j:
            w[i] *= 2 if w[i] in (-1, 1) else 1
            if w[i] % 2:
                w[i] = 2
    w[j] = rng.choice((-1, 1))
    if sum(1 for t in w if t % 2) != 1:
        continue
    n = tower_norm(w)
    if n == 0 or n % 2 == 0:
        continue
    ge8 = ((n - 1) % 256 == 0)
    pred = (w[(j + h // 2) % h] == 0)
    if ge8 != pred:
        bad += 1
print("   violations of  [v_2(Norm-1) >= 8  <=>  w_{(j+32) mod 64} = 0] : %d/3000"
      % bad)
