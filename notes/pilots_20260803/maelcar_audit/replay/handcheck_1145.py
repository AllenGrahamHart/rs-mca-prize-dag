#!/usr/bin/env python3
"""Independent hand-checks of load-bearing structural claims in maelcar PR #1145.

None of these re-run the author's C++ census. They check claims that the
author's own Python auditors do NOT check, using only the recorded data.
"""
from itertools import combinations
from math import comb, gcd
from collections import Counter

ELL = 11
ok = lambda b: "PASS" if b else "**FAIL**"

print("== C1. support dichotomy: 252 = 250 (gcd 1) + 2 (gcd 2) ==")
g = Counter()
for A in combinations(range(1, 11), 5):
    g[gcd(*[a - A[0] for a in A[1:]])] += 1
print("   histogram", dict(g), ok(g == Counter({1: 250, 2: 2})))
par = [A for A in combinations(range(1, 11), 5)
       if gcd(*[a - A[0] for a in A[1:]]) == 2]
print("   gcd-2 supports", par,
      ok(sorted(par) == [(1, 3, 5, 7, 9), (2, 4, 6, 8, 10)]))

print("\n== C2. AGL(1,11) orbit count on 6-subsets of Z/11 (note claims 6 reps) ==")
subsets = [frozenset(s) for s in combinations(range(ELL), 6)]
seen, orbits = set(), 0
for S in subsets:
    if S in seen:
        continue
    orbits += 1
    for a in range(1, ELL):
        for b in range(ELL):
            seen.add(frozenset((a * x + b) % ELL for x in S))
print(f"   C(11,6)={comb(11,6)}  orbits={orbits}", ok(orbits == 6))

print("\n== C3. recorded 6x6 norm table -> primes = 1 mod 11 ==")
table = [[1, 1, 1, 1, 1, 1],
         [1, 23, 67, 23, 1, 243],
         [1, 67, 419, 23, 1, 1],
         [1, 23, 23, 199, 1, 3125],
         [1, 1, 1, 1, 529, 1024],
         [1, 243, 1, 3125, 1024, 243]]


def primes(n):
    out, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            out.add(d)
            n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


allp = set().union(*(primes(v) for row in table for v in row if v > 1))
one_mod_11 = sorted(p for p in allp if p % ELL == 1)
print("   all prime divisors ", sorted(allp))
print("   those = 1 mod 11   ", one_mod_11, ok(one_mod_11 == [23, 67, 199, 419]))
for p in [23, 67, 199, 419]:
    q = (p - 1) // ELL
    print(f"   p={p:3d}  q=(p-1)/11={q:2d}  q>=11? {q >= ELL}"
          f"   -> {'usable' if q >= ELL else 'excluded (too few labels)'}")

print("\n== C4. census enumeration law  rows = 252*(C(11,4)*q + 60) ==")
for p, q, rows, exact in [(199, 18, 1512000, 1474200),
                          (331, 30, 2509920, 2472120),
                          (419, 38, 3175200, 3137400)]:
    pred = 252 * (comb(11, 4) * q + 60)
    print(f"   p={p:4d} q={q:2d} rows={rows:8d} pred={pred:8d} {ok(rows==pred)}"
          f"   degenerate={rows-exact}")
print("   degenerate count constant across primes",
      ok(len({1512000-1474200, 2509920-2472120, 3175200-3137400}) == 1))

print("\n== C5. S_6 of the recorded six-fibre states (note prints 'S_6 = 20') ==")
for p, hist in [(199, {1: 9, 2: 8, 6: 1}), (419, {1: 32, 2: 5, 6: 1})]:
    vals = sorted([v for v, c in hist.items() for _ in range(c)], reverse=True)
    q = (p - 1) // ELL
    print(f"   p={p:3d} labels={len(vals)} (q={q} {ok(len(vals)==q)}) "
          f"S_6={sum(vals[:6])}  <=20 {ok(sum(vals[:6])<=20)}")
print("   -> six-fibre states have S_6 = 16, NOT 20; the '20' in note SS3 is the")
print("      census envelope at that prime, achieved by a DIFFERENT state.")

print("\n== C6. envelope monotonicity: (20,22,24,27) needs distinct maximisers ==")
d = [20, 22, 24, 27]
inc = [d[0]] + [d[i] - d[i-1] for i in range(1, 4)]
print("   S_6..S_9 =", d, " increments", inc[1:])
print("   increments non-increasing?", inc[1:] == sorted(inc[1:], reverse=True),
      "-> False means NO single state attains all four; envelope reading forced.")
named = {5: 2, 3: 2, 2: 4, 1: 22}
v = sorted([x for x, c in named.items() for _ in range(c)], reverse=True)
print(f"   note SS1 witness 5^2 3^2 2^4 1^22 gives "
      f"(S6..S9)=({sum(v[:6])},{sum(v[:7])},{sum(v[:8])},{sum(v[:9])})"
      f" -> matches (20,22,24,-) but S_9=25 != 27, as expected.")
