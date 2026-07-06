#!/usr/bin/env python3
"""ROUND S2 (self-tennis), REFUTE CHAIR: audit of the pinned "analytic
alternative" for the R-bound, plus the moment-transfer identity.

CLAIM UNDER ATTACK (pinned file, proof-architecture section (c) ALTERNATIVE):
  "for every lambda != 0: sum_y log2 cos^2(pi a_y(lambda)/q)
       <= -(256+delta)*L + O(log q)"
  — justified there by 'the circle average of log2 cos^2 is exactly -2, so
  the requirement is HALF of typical: a 100% margin'.

ATTACK 1 (iid tail — the margin is a mirage): under the random model
(a_y/q iid uniform), the tail P(T >= 2^-N(1+delta)) with
T = prod_y cos^2 is NOT ~2^-N; fractional-moment Markov with s = 1/2 gives
  P(T >= 2^-N) <= (E|cos(pi U)| * 2^(1/2))^N = (0.9003...)^N = 2^-0.1515 N,
so ~ q^L * 2^-0.1515 N = 2^(255-38.8)L frequencies are EXPECTED to violate
the per-lambda display. Monte Carlo confirms the tail scale. The correct
target is the DYADIC COUNT form, never per-lambda.

ATTACK 2 (real row): exhaustive lambda-scan of a balanced toy row
(q = 66161, n' = 64, N = 32, L = 1... chosen q ≡ 1 mod 64, q ~ 2^N/65 —
wait, balanced needs q ~ 2^32; local exhaustive scan needs q small; we use
q = 66177? — we instead scan q = 65089 (q ≡ 1 mod 64, q < 2^32) — the point
of this attack is only the SHAPE of the dyadic histogram vs iid, which is
q-scale-free) — count #{lambda : T(lambda) >= 2^-j} for dyadic j and compare
to the iid prediction q * P_iid(T >= 2^-j) (estimated by Monte Carlo).
K(j) := observed/predicted is the honest near-peak constant.

PROVER LEMMA (moment transfer — exact identity, verified here numerically):
  sum_{lambda in F_q^L} T(lambda)^s
    = 4^{-sN} q^L sum_{k in [-s..s]^N, A k ≡ 0 mod q} prod_y C(2s, s+k_y)
  for integer s >= 1: the s-th moment of the Fourier weight IS a weighted
  (2s+1)-ary kernel count. (s = 1 is the D3=D2 identity already pinned.)
  Verified exactly at a small row for s = 1, 2 by computing both sides.
CONSEQUENCE: every dyadic near-peak count is controlled by higher-alphabet
kernel counting and vice versa — A2/R and zone-(b) are ONE leaf in different
alphabets; there is no purely-analytic escape. (The 'analytic route' can at
best transfer the problem, not solve it.)
"""
import math
import random
import numpy as np

fails = []
def check(name, cond):
    print(("PASS" if cond else "FAIL"), name)
    if not cond:
        fails.append(name)

# ---------- ATTACK 1: iid tail ----------
# exact s=1/2 Markov constant: E|cos(pi U)| = 2/pi
c_half = (2 / math.pi) * math.sqrt(2.0)
print(f"s=1/2 Markov: P(T >= 2^-N) <= ({c_half:.6f})^N = 2^(-{-math.log2(c_half):.4f} N)")
check("ATTACK 1a: Markov constant < 1 (tail is 2^-0.152N, NOT 2^-N)",
      0.89 < c_half < 0.91)

# Monte Carlo at N = 256: estimate P(T >= 2^-N(1+delta)) via importance-free
# log-sum sampling (the event is rare-ish but 2^-39 at N=256 is too rare to
# hit directly; sample at N = 64 where 2^-0.1515*64 = 2^-9.7 and check scale)
rng = np.random.default_rng(715)
N_mc, trials = 64, 4_000_000
u = rng.random((trials, N_mc))
logT = np.log2(np.cos(np.pi * u) ** 2 + 1e-300).sum(axis=1)
p_emp = float((logT >= -N_mc).mean())
p_markov = c_half ** N_mc
print(f"Monte Carlo N={N_mc}: P(T >= 2^-N) = {p_emp:.3e}, Markov cap {p_markov:.3e}")
check("ATTACK 1b: empirical tail within [2^-14, 2^-9] at N=64 "
      "(fat tail confirmed; per-coordinate rate ~0.16-0.21, far from 1)",
      2**-14 <= p_emp <= 2**-9)
rate = -math.log2(p_emp) / N_mc
print(f"  empirical per-coordinate rate I = {rate:.4f}  (the display needs I >= ~1)")
check("ATTACK 1c: rate << 1 => per-lambda display FALSE in the random model",
      rate < 0.35)
# expected violator count at production L=1: q ~ 2^255, N = 256
viol_log2 = 255 - rate * 256
print(f"  => expected # violating lambda at production L=1: 2^{viol_log2:.0f}")
check("ATTACK 1d: expected violators astronomically many (> 2^180)",
      viol_log2 > 180)

# ---------- ATTACK 2: real-row dyadic histogram vs iid ----------
def spr(q):
    n = q - 1; fs = set(); d = 2
    while d * d <= n:
        while n % d == 0:
            fs.add(d); n //= d
        d += 1
    if n > 1: fs.add(n)
    g = 2
    while any(pow(g, (q - 1) // p, q) == 1 for p in fs):
        g += 1
    return g

def dyadic_counts(q, NP=64):
    N = NP // 2
    g = spr(q)
    omega = pow(g, (q - 1) // NP, q)
    xs = np.array([pow(omega, y, q) for y in range(N)], dtype=np.int64)
    counts = {}
    logs = []
    for lo in range(1, q, 20000):
        lam = np.arange(lo, min(lo + 20000, q), dtype=np.int64)
        a = lam[:, None] * xs[None, :] % q
        lg = np.log2(np.cos(np.pi * a / q) ** 2 + 1e-300).sum(axis=1)
        logs.append(lg)
    lg = np.concatenate(logs)
    return lg

q_row = 65089  # q ≡ 1 (mod 64), prime
assert q_row % 64 == 1
lg = dyadic_counts(q_row)
N_row = 32
# iid prediction by Monte Carlo at N = 32
u2 = rng.random((4_000_000, N_row))
lg_iid = np.log2(np.cos(np.pi * u2) ** 2 + 1e-300).sum(axis=1)
print(f"\nrow q={q_row} (n'=64): dyadic near-peak counts vs iid model")
print(f"{'j':>4} {'#T>=2^-j obs':>14} {'iid pred':>12} {'K':>8}")
ks = []
for j in (8, 12, 16, 20, 24, 28, 32):
    obs = int((lg >= -j).sum())
    pred = float((lg_iid >= -j).mean()) * (q_row - 1)
    K = obs / pred if pred > 0 else float("inf")
    ks.append((j, obs, pred, K))
    print(f"{j:>4} {obs:>14} {pred:>12.1f} {K:>8.2f}")
kmax = max(k for _, o, p, k in ks if p >= 20)  # only well-estimated levels
check(f"ATTACK 2: near-peak counts within 2x of iid at all well-sampled "
      f"dyadic levels (worst K = {kmax:.2f}) — no structural surplus, the "
      "DYADIC form is the true statement", kmax < 2.0)

# ---------- PROVER LEMMA: moment-transfer identity (exact) ----------
# tiny exact row: q = 17, n' = 8, N = 4, L = 1
q0, NP0 = 17, 8
N0 = NP0 // 2
g0 = spr(q0)
om0 = pow(g0, (q0 - 1) // NP0, q0)
assert pow(om0, NP0, q0) == 1 and pow(om0, N0, q0) == q0 - 1
xs0 = [pow(om0, y, q0) for y in range(N0)]
import itertools
from fractions import Fraction
import mpmath as mp
mp.mp.dps = 60

def lhs(s):
    tot = mp.mpf(0)
    for lam in range(q0):
        prod = mp.mpf(1)
        for x in xs0:
            prod *= mp.cos(mp.pi * ((lam * x) % q0) / q0) ** (2 * s)
        tot += prod
    return tot

def rhs(s):
    tot = 0
    for k in itertools.product(range(-s, s + 1), repeat=N0):
        if sum(ky * x for ky, x in zip(k, xs0)) % q0 == 0:
            w = 1
            for ky in k:
                w *= math.comb(2 * s, s + ky)
            tot += w
    return Fraction(tot * q0, 4 ** (s * N0))

for s in (1, 2):
    L_ = lhs(s)
    R_ = rhs(s)
    err = abs(float(L_) - float(R_))
    print(f"\nmoment-transfer s={s}: LHS = {float(L_):.12f}, "
          f"RHS = {float(R_):.12f}, |err| = {err:.2e}")
    check(f"PROVER: moment-transfer identity exact at s={s} (err < 1e-9)",
          err < 1e-9)

print()
print("ALL PASS" if not fails else f"FAILURES: {fails}")
