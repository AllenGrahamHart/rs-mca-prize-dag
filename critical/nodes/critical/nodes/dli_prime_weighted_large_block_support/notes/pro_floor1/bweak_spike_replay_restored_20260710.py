#!/usr/bin/env python3
"""AMBER-AUDIT: independent replay of the SURVIVAL +4 record (Pro floor-window 1):
the single K = 16.0003 concentration spike at N=64, w=5, q=15249281
(claimed: 256 weight-5 vanishers = 2 negacyclic orbits; Poisson-accident).
The banked artifact pro_floor1/bweak_local_verifier.py is an EMPTY PLACEHOLDER,
so this reconstructs the check from the FALSIFICATION_GOAL.md description:
  K = count * q / (2^w * C(N,w)) on the cyclotomic vanisher projection,
  vanishers = signed weight-5 ternary P with P(omega) == 0 mod q,
  omega = g^((q-1)/(2N)) mod q, g = smallest primitive root, z^N = -1 frame.
"""
import itertools, math
import numpy as np
import sympy

q = 15249281
NP, N, w = 128, 64, 5

assert sympy.isprime(q), "q not prime"
assert (q - 1) % NP == 0, "q != 1 mod 2N"
g = int(sympy.primitive_root(q))
omega = pow(g, (q - 1) // NP, q)
# order exactly 2N = 128
assert pow(omega, NP, q) == 1 and pow(omega, N, q) == q - 1
print(f"q={q} prime, g={g}, omega={omega}, ord(omega)=128 (omega^64 = -1)  PASS")

xs = np.array([pow(omega, e, q) for e in range(N)], dtype=np.int64)

# sign patterns with eps_0 = +1 (global sign counted x2 at the end)
signs = np.array(list(itertools.product([1, -1], repeat=w - 1)), dtype=np.int64)
signs = np.hstack([np.ones((signs.shape[0], 1), dtype=np.int64), signs])  # 16 x 5

count = 0
CH = 400_000
buf = []
n_supports = 0
for comb in itertools.combinations(range(N), w):
    buf.append(comb)
    if len(buf) == CH:
        idx = np.array(buf, dtype=np.int64); buf = []
        vals = xs[idx]                       # CH x 5
        sums = vals @ signs.T % q            # CH x 16
        count += int((sums == 0).sum())
        n_supports += idx.shape[0]
if buf:
    idx = np.array(buf, dtype=np.int64)
    vals = xs[idx]
    sums = vals @ signs.T % q
    count += int((sums == 0).sum())
    n_supports += idx.shape[0]

total_signed = 2 * count   # global sign
CNw = math.comb(N, w)
assert n_supports == CNw
K = total_signed * q / (2**w * CNw)
lam_orbit = 2**w * CNw / q / (2 * NP)  # expected orbits (orbit size 2N=128... using 2*NP? no)
print(f"supports = {n_supports} = C(64,5); signed vanishers = {total_signed} (claimed 256)")
print(f"K = {total_signed} * q / (2^5 * C(64,5)) = {K:.6f} (claimed 16.0003)")
print("PASS" if (total_signed == 256 and abs(K - 16.0003) < 5e-4) else "FAIL")
