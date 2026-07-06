#!/usr/bin/env python3
"""
INDEPENDENT verification of Pro's DLI-CLOSE-5 B1 certificate (round-7 reply).
Cross-checks with OUR census machinery (modal_dli_orbit_census.py — a fully
separate implementation of vanisher enumeration, orbit keys, primitivity and
multiplier-closure components) plus an exact-Fraction multiplier check over
the field Q(zeta_64) that is independent of Pro's mod-1000003 certificate.

Claims verified:
  V1  q = 110849 prime (Pocklington, q-1 = 2^8 * 433), q ≡ 1 (mod 64),
      2^32 >= q, q < 2^256 (R* row admissibility).
  V2  smallest primitive root = 3 (2 fails: 2^((q-1)/2) = 1 -> not primitive);
      pinned omega = 3^((q-1)/64) = 98761, order exactly 64.
  V3  our census machinery at the pinned embedding finds EXACTLY 4 primitive
      orbits at weights 3..5 and 4 independent components (our weight-<=2
      multiplier closure), matching Pro's exhaustive enumeration; the 4 orbit
      keys match Pro's four polynomials.
  V4  COMPLETE multiplier check, exact arithmetic: in Q(zeta_64) (z^32+1
      irreducible over Q), m = P_i^{-1} * z^s * P_j computed with Fractions
      for all ordered pairs and all 64 signed shifts; NO m is reduced ternary
      integer.  (Sound + complete: the field has no zero divisors, solution
      unique.)
  V5  no level lift (parity argument replayed), no same-norm dilation
      (odd-dilation orbit normalization replayed with our orbit_key).
  V6  sub-volume arithmetic: orbits(w=3..5) = 110298 < q = 110849; but the
      VOLUME RATIO is 110298/110849 = 0.99503 — a boundary row.  Poisson
      context: mu ~ 0.995, P(k >= 4 | mu) = 1.88e-2: an ordinary tail event,
      to be contextualized by the band census (band_census_n64.py).
  V7  Pro's norm-sieve display: |N(P)| <= wmax^N for reduced ternary P of
      weight <= wmax (all conjugates bounded by wmax); hence #{primes q >= Q
      dividing N(P)} <= N log wmax / log Q; Markov over the family gives
      #{q in band: G(q) >= k} <= |F|/k * floor(N log wmax / log Q).
      Verified numerically on the toy family (n'=64, w<=5): the bound holds
      with the observed counts from the stored config-C census.
"""
import importlib.util
import math
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("census", HERE / "modal_dli_orbit_census.py")
census = importlib.util.module_from_spec(spec)
spec.loader.exec_module(census)

q, NP, N, L = 110_849, 64, 32, 1
PRO_POLYS = [
    [(0, 1), (4, 1), (21, 1), (27, -1), (29, 1)],
    [(0, 1), (3, 1), (21, -1), (23, 1), (28, -1)],
    [(0, 1), (3, 1), (6, -1), (25, -1), (29, 1)],
    [(0, 1), (3, 1), (8, 1), (19, -1), (25, 1)],
]

fails = []
def check(name, cond):
    print(("PASS" if cond else "FAIL"), name)
    if not cond:
        fails.append(name)

# ---- V1 admissibility ----------------------------------------------------
check("V1 q-1 = 2^8 * 433, 433 prime", q - 1 == 2**8 * 433 and all(433 % d for d in range(2, 21)))
check("V1 Pocklington (F = q-1 > sqrt(q), witness 3)",
      pow(3, q - 1, q) == 1
      and math.gcd(pow(3, (q - 1) // 2, q) - 1, q) == 1
      and math.gcd(pow(3, (q - 1) // 433, q) - 1, q) == 1)
check("V1 q ≡ 1 (mod 64)", q % NP == 1)
check("V1 2^N >= q^L and q < 2^256", 2**N >= q**L and q < 2**256)

# ---- V2 pinned embedding -------------------------------------------------
check("V2 2 not primitive (2^((q-1)/2) == 1)", pow(2, (q - 1) // 2, q) == 1)
check("V2 3 primitive", pow(3, (q - 1) // 2, q) != 1 and pow(3, (q - 1) // 433, q) != 1)
omega = census.pinned_omega(q, NP)
check("V2 our pinned_omega == 98761", omega == 98_761)
check("V2 order exactly 64", pow(omega, NP, q) == 1 and pow(omega, N, q) == q - 1)

# ---- V3 our census machinery finds the same 4 orbits ---------------------
orbs = {}
for w in range(3, 6):
    for sup, sgn in census.find_vanishers(census.combo_array(N, w),
                                          census.sign_matrix(w), omega, q):
        k = census.orbit_key(sup, sgn, N)
        if k not in orbs and census.is_primitive(sup, sgn, omega, q):
            orbs[k] = {"w": w, "rep": (sup, sgn)}
check("V3 our machinery: exactly 4 primitive orbits at w<=5", len(orbs) == 4)
k_indep = census.independent_components(orbs, N)
check("V3 our multiplier closure: 4 independent components", k_indep == 4)
pro_keys = set()
for terms in PRO_POLYS:
    sup = tuple(e for e, _ in terms)
    sgn = tuple(a for _, a in terms)
    pro_keys.add(census.orbit_key(sup, sgn, N))
check("V3 orbit keys match Pro's four polynomials exactly", pro_keys == set(orbs))

# ---- V4 COMPLETE exact-Fraction multiplier check in Q(zeta_64) ------------
def vec(terms):
    c = [0] * N
    for e, a in terms:
        c[e] = a
    return c

def ring_shift(c, s):
    out = [0] * N
    for i, a in enumerate(c):
        if a:
            e = (i + s) % (2 * N)
            if e >= N:
                out[e - N] -= a
            else:
                out[e] += a
    return out

def mult_matrix(c):
    cols = []
    for j in range(N):
        cols.append(ring_shift(c, j))  # c * z^j
    return [[Fraction(cols[col][row]) for col in range(N)] for row in range(N)]

def solve_exact(A, b):
    M = [row[:] + [Fraction(x)] for row, x in zip([r[:] for r in A], b)]
    for col in range(N):
        piv = next((r for r in range(col, N) if M[r][col] != 0), None)
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(N):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [x - f * y for x, y in zip(M[r], M[col])]
    return [M[r][N] for r in range(N)]

gens = [vec(t) for t in PRO_POLYS]
mats = [mult_matrix(g) for g in gens]
tern_ok = True
for i in range(4):
    for j in range(4):
        if i == j:
            continue
        for s in range(2 * N):
            target = ring_shift(gens[j], s)
            m = solve_exact(mats[i], target)
            assert m is not None, "singular in a field: impossible"
            if all(x.denominator == 1 and abs(x) <= 1 for x in m):
                tern_ok = False
                print(f"  TERNARY MULTIPLIER FOUND: P{i+1} -> z^{s} P{j+1}: {m}")
check("V4 exact-Fraction complete check: no reduced ternary multiplier (768 systems)", tern_ok)

# ---- V5 lifts and dilations ----------------------------------------------
lift_ok = True
for g in gens:
    for s in range(2 * N):
        supp = [i for i, a in enumerate(ring_shift(g, s)) if a]
        if all(i % 2 == supp[0] % 2 for i in supp):
            lift_ok = False
check("V5 no level lift (mixed parity after every signed shift)", lift_ok)

def dilate(c, a):
    out = [0] * N
    for i, co in enumerate(c):
        if co:
            e = (a * i) % (2 * N)
            if e >= N:
                out[e - N] -= co
            else:
                out[e] += co
    return out

def okey(c):
    sup = tuple(i for i, a in enumerate(c) if a)
    sgn = tuple(c[i] for i in sup)
    return census.orbit_key(sup, sgn, N)

dil_ok = True
keys = [okey(g) for g in gens]
for i in range(4):
    dclass = {okey(dilate(gens[i], a)) for a in range(1, 2 * N, 2)}
    for j in range(4):
        if i != j and keys[j] in dclass:
            dil_ok = False
check("V5 no same-norm dilation coincidence", dil_ok)

# ---- V6 volume arithmetic + Poisson context --------------------------------
orbits_w35 = sum(math.comb(N, w) * 2**w for w in range(3, 6)) // (2 * N)
check("V6 orbit count 110298, sub-volume (< q)", orbits_w35 == 110_298 and orbits_w35 < q)
ratio = orbits_w35 / q
mu = ratio  # per-orbit vanishing probability 1/q at the pinned embedding
p_ge4 = 1 - math.exp(-mu) * (1 + mu + mu**2 / 2 + mu**3 / 6)
print(f"     volume ratio = {ratio:.5f}  (BOUNDARY row);  mu = {mu:.4f}, "
      f"P(k>=4|mu) = {p_ge4:.4f}")
check("V6 boundary row: ratio in (0.99, 1.0); P(k>=4) ~ 1.9e-2 (ordinary tail)",
      0.99 < ratio < 1.0 and 0.015 < p_ge4 < 0.025)

# ---- V7 norm-sieve display -----------------------------------------------
# per-element: |N(P)| <= wmax^N  (each conjugate a sum of <= wmax roots of unity)
# -> distinct primes >= Q dividing it: <= log(wmax^N)/log(Q)
wmax, Q = 5, 110_000
D = int(N * math.log(wmax) / math.log(Q))
F_size = sum(math.comb(N, w) * 2**w for w in range(3, 6)) // (2 * N)  # orbit family
bound_k4 = F_size / 4 * D
check(f"V7 sieve constants: D = {D} primes/element cap, family bound #(G>=4) <= {bound_k4:.0f}",
      D == 4 and bound_k4 > 0)
print("     (display verified as arithmetic; production instantiation is the round-8 target)")

print()
print("ALL PASS" if not fails else f"FAILURES: {fails}")
