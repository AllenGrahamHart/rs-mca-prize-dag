#!/usr/bin/env python3
"""sjb_n64_fiber_demo: EXACT complete e1-fiber distribution at the QRL-MODAL-1
model-grid cell (n = 256, M = 4, n' = 64, k' = 32, rho = 1/2, q = 65537).

q = 65537 is prime, q ≡ 1 (mod 256) and q >= n^2 = 65536 — the exact field-floor
shape of the minted claim ((Mn')^2), at the pre-registered falsification-probe
grid (QRL-MODAL-1: model rows n in {256,512,1024}, n' = 64, first primes >= n^2).

Computes, for the explicit word family W_tau = X^33 - tau X^32 on the order-64
subgroup D of F_q^*, the EXACT complete aperiodic exact-agreement-33 list size
for EVERY tau simultaneously:  L_P(W_tau, 33) = #{S ⊆ D : |S| = 33, e1(S) = tau}
(bijection validated exhaustively in sjb_semantics_tiny.py; cross-validated here
against brute force at (n'=16, q=257)).

DP: counts[s][r] = #subsets of processed prefix with size s and sum r (mod q).
int64 is safe: every entry <= C(64,32) = 1,832,624,140,942,590,534 < 2^63.

Compare: minted cap min((63/128)*64^6, (q-3*64)/2) = min(33,822,867,456, 32,672)
and QRL-MODAL-1's pre-registered expectation max L_P(k'+1) <= 2n' = 128.
"""
import sys
from math import comb
import numpy as np

FAILS = 0
def check(label, cond):
    global FAILS
    print(f"[{'PASS' if cond else 'FAIL'}] {label}")
    if not cond:
        FAILS += 1

def subgroup(q, order, gen_base):
    h = pow(gen_base, (q - 1) // order, q)
    D = [pow(h, i, q) for i in range(order)]
    assert len(set(D)) == order, "not a full order subgroup"
    return D

def fiber_distribution(D, size, q):
    """exact counts[s][r] via int64 DP; returns the row for `size`."""
    counts = np.zeros((size + 1, q), dtype=np.int64)
    counts[0][0] = 1
    for x in D:
        # process element x: new[s] = old[s] + roll(old[s-1], x)
        for s in range(size, 0, -1):
            counts[s] += np.roll(counts[s - 1], x)
    return counts[size]

# ---- cross-validation at (n'=16, k'=8, q=257): DP vs brute-force subsets ----
q_s, np_s, a_s = 257, 16, 9
D_s = subgroup(q_s, np_s, 3)  # 3 is a primitive root of 257
row = fiber_distribution(D_s, a_s, q_s)
import itertools
brute = np.zeros(q_s, dtype=np.int64)
for S in itertools.combinations(D_s, a_s):
    brute[sum(S) % q_s] += 1
check("cross-validation (n'=16, q=257): DP fiber distribution == brute force over all C(16,9)=11440 subsets",
      bool((row == brute).all()) and int(row.sum()) == comb(16, 9))

# ---- the QRL-MODAL-1 grid cell ----
q, NP, KP = 65537, 64, 32
A = KP + 1
D = subgroup(q, NP, 3)  # 3 is a primitive root of F_65537
row = fiber_distribution(D, A, q)
total = int(row.sum())
C = comb(NP, A)
mx, mn = int(row.max()), int(row.min())
tau_star = int(row.argmax())
mean = C / q
cap6 = (63 * NP**6) // 128
capq = (q - 3 * NP) // 2
print(f"\nn'=64, k'=32, a=33, q=65537 (n=256, M=4; q >= n^2 = 65536, q == 1 mod 256)")
print(f"  total subsets C(64,33) = {C}")
print(f"  DP total                = {total}")
print(f"  fiber stats: min {mn}, max {mx} (tau* = {tau_star}), mean C/q = {mean:.6g}")
print(f"  minted caps: (63/128)n'^6 = {cap6},  (q-3n')/2 = {capq}")
print(f"  QRL-MODAL-1 pre-registered expectation: max L_P(k'+1) <= 2n' = {2*NP}")
check("EXACTNESS: DP total == C(64,33)", total == C)
check(f"pigeonhole floor realized: max fiber {mx} >= ceil(C/q) = {-(-C // q)}", mx >= -(-C // q))
check(f"REFUTES (q-3n')/2 branch: max fiber / capq = {mx // capq}x", mx > capq)
check(f"REFUTES (63/128)n'^6 branch at this q: max fiber / cap6 = {mx / cap6:.1f}x", mx > cap6)
check(f"REFUTES QRL-MODAL-1 expectation by {mx // (2*NP)}x (its enumerator counts constructed classes only)",
      mx > 2 * NP)
check(f"CONCENTRATION (supports the equidistribution upgrade): min fiber {mn} > 0.99 * mean",
      mn > 0.99 * mean)

# ---- explicit witness: one (word, codeword, support) triple verified in vivo ----
# find one 33-subset S with e1(S) = tau*: random search (hit rate ~ 1/65537... but
# fibers are dense: expected hits/trial = fiber/C ~ 1/q; do a smarter greedy walk:
# start random, swap elements to adjust the sum until it equals tau*.
import random
rng = random.Random(64)
S = set(rng.sample(D, A))
rest = [x for x in D if x not in S]
for _ in range(200000):
    cur = sum(S) % q
    if cur == tau_star:
        break
    i = rng.randrange(A)
    j = rng.randrange(NP - A)
    Sl = sorted(S)
    a_el, b_el = Sl[i], rest[j]
    new = (cur - a_el + b_el) % q
    # greedy: accept if it moves sum closer to tau* in Z_q distance, sometimes anyway
    d_old = min((cur - tau_star) % q, (tau_star - cur) % q)
    d_new = min((new - tau_star) % q, (tau_star - new) % q)
    if d_new <= d_old or rng.random() < 0.1:
        S.remove(a_el); S.add(b_el)
        rest[j] = a_el
found = (sum(S) % q == tau_star) and len(S) == A
check("witness support S found: |S| = 33, e1(S) = tau*", found)
if found:
    # build c = W_{tau*} - L_S and verify everything end to end
    L = [1]  # monic locator, low->high after reversal handling: build product (X - s)
    for s_el in S:
        L = [(-s_el * L[0]) % q] + [(L[i - 1] - s_el * L[i]) % q for i in range(1, len(L))] + [1]
        L[-1] = 1  # keep monic
    # W = X^33 - tau* X^32  ->  c = W - L_S has coeffs: -(L minus X^33 term), with X^32 coeff -tau* - (-e1) = 0
    ccoef = [(-L[i]) % q for i in range(len(L) - 1)]  # subtract everything below X^33
    ccoef[32] = (ccoef[32] - tau_star) % q
    check("degree drop: coeff of X^32 in c vanishes (deg c < 32... i.e. < k')", ccoef[32] == 0)
    cc = ccoef[:32]
    def ev(co, x):
        acc = 0
        for coefc in reversed(co):
            acc = (acc * x + coefc) % q
        return acc
    agr = {x for x in D if ev(cc, x) == (pow(x, 33, q) - tau_star * pow(x, 32, q)) % q}
    check("in-vivo: exact agreement support of the explicit codeword == S (size 33, aperiodic-odd)",
          agr == S and len(agr) == 33)

print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECKS FAILED")
sys.exit(0 if FAILS == 0 else 1)
