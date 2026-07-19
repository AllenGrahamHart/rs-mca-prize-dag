#!/usr/bin/env python3
"""sjb_semantics_tiny: EXHAUSTIVE validation of every definitional step of the
refutation argument at (n'=8, k'=4, q=17) — small enough to enumerate ALL q^{k'}
= 83,521 codewords per word.

Validates:
  V1 (bijection): for EVERY tau in F_17, the exact-agreement-(k'+1) list of the
     word W_tau = X^{k'+1} - tau X^{k'} (computed by brute force over all
     codewords) EQUALS the e1-fiber #{S : |S| = k'+1, sum(S) = tau} (computed by
     brute force over all C(8,5) = 56 subsets), and every listed support is
     exactly the corresponding S.
  V2 (aperiodicity for free): every counted support (odd size 5) is aperiodic
     under the rotation action of Z_8 on the subgroup domain.
  V3 (pigeonhole): sum_tau fiber(tau) == C(8,5); max_tau fiber >= ceil(C(8,5)/17).
  V4 (averaging identity): over ALL words it holds exactly by algebra; here,
     sampled mean of the exact-agreement-5 count over random words matches
     C(8,5) * (q-1)^3 / q^4 = 2.746 within sampling error.
  V5 (mass identity, definitional mutation control): for random words,
     sum over codewords with agreement >= k' of C(A_c, k') == C(8,4) = 70, exactly.
"""
import itertools, random, sys
from math import comb

q = 17
NP, KP = 8, 4          # n', k'
A = KP + 1             # the P1-OWN cell
# order-8 subgroup of F_17^*: powers of 2
g = 2
D = []
x = 1
for _ in range(NP):
    x = x * g % q if D else 1
    D.append(x)
# rebuild cleanly
D = [pow(g, i, q) for i in range(NP)]
assert len(set(D)) == NP and pow(g, NP, q) == 1

FAILS = 0
def check(label, cond):
    global FAILS
    print(f"[{'PASS' if cond else 'FAIL'}] {label}")
    if not cond:
        FAILS += 1

def poly_eval(coeffs, x):  # coeffs low->high
    acc = 0
    for c in reversed(coeffs):
        acc = (acc * x + c) % q
    return acc

def exact_support(cw_vals, word_vals):
    return frozenset(i for i in range(NP) if cw_vals[i] == word_vals[i])

def aperiodic(support_idx):
    """support given as index set in Z_8 (positions in D = subgroup order); the
    rotation action is index shift mod 8."""
    for sh in range(1, NP):
        if NP % sh == 0 or True:  # check all nontrivial rotations; stabilizer nontrivial iff invariant under some sh != 0
            pass
    for sh in range(1, NP):
        if frozenset((i + sh) % NP for i in support_idx) == support_idx:
            return False
    return True

# all codewords as value vectors, keyed by coefficient tuple
print(f"domain D (order-8 subgroup of F_17^*): {D}")
codewords = {}
for coeffs in itertools.product(range(q), repeat=KP):
    codewords[coeffs] = tuple(poly_eval(coeffs, x) for x in D)
print(f"enumerated ALL {len(codewords)} codewords (deg < {KP})")

# V1 + V2 + V3
subsets = list(itertools.combinations(range(NP), A))
fibers = {}
for S in subsets:
    tau = sum(D[i] for i in S) % q
    fibers.setdefault(tau, []).append(frozenset(S))

all_v1 = True
all_v2 = True
for tau in range(q):
    wvals = tuple((pow(x, A, q) - tau * pow(x, KP, q)) % q for x in D)
    listed = {}
    for coeffs, cvals in codewords.items():
        E = exact_support(cvals, wvals)
        if len(E) == A:
            listed[coeffs] = E
    fib = set(fibers.get(tau, []))
    got = set(listed.values())
    if got != fib or len(listed) != len(fib):
        all_v1 = False
        print(f"  MISMATCH tau={tau}: brute list {len(listed)} supports {len(got)} vs fiber {len(fib)}")
    if not all(aperiodic(E) for E in listed.values()):
        all_v2 = False
check("V1: for ALL 17 tau, exact-agreement-5 list == e1-fiber (bijection, support-exact)", all_v1)
check("V2: every counted support aperiodic (odd size => free aperiodicity)", all_v2)
tot = sum(len(v) for v in fibers.values())
mx = max(len(fibers.get(t, [])) for t in range(q))
check(f"V3: sum_tau fiber = {tot} == C(8,5) = {comb(8,5)}; max fiber = {mx} >= ceil(C/q) = {-(-comb(8,5)//q)}",
      tot == comb(8, 5) and mx >= -(-comb(8, 5) // q))

# V4: sampled averaging identity
rng = random.Random(20260713)
NW = 400
tot_count = 0
for _ in range(NW):
    wvals = tuple(rng.randrange(q) for _ in range(NP))
    cnt = 0
    for cvals in codewords.values():
        if len(exact_support(cvals, wvals)) == A:
            cnt += 1
    tot_count += cnt
mean = tot_count / NW
pred = comb(NP, A) * (q - 1) ** (NP - A) / q ** (NP - KP)
check(f"V4: sampled mean {mean:.3f} vs exact-average prediction {pred:.3f} (|diff| < 0.35)",
      abs(mean - pred) < 0.35)

# V5: mass identity per word (exact)
ok = True
for _ in range(25):
    wvals = tuple(rng.randrange(q) for _ in range(NP))
    mass = 0
    for cvals in codewords.values():
        Ac = sum(1 for i in range(NP) if cvals[i] == wvals[i])
        if Ac >= KP:
            mass += comb(Ac, KP)
    if mass != comb(NP, KP):
        ok = False
check(f"V5: mass identity sum_c C(A_c,{KP}) == C(8,4) = 70 EXACT on 25 random words", ok)

print("ALL CHECKS PASS" if FAILS == 0 else f"{FAILS} CHECKS FAILED")
sys.exit(0 if FAILS == 0 else 1)
