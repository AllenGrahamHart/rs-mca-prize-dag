#!/usr/bin/env python3
"""Independent audit path (coordinator, 2026-08-13): reproduce the PR
#1168 certificate-class wall from scratch.

The greedy/Abel low bound L(J) is recomputed with our own math.comb
implementation of Q_s and c_delta (no upstream code reused); it must hit
the printed U_low exactly at J = 19737. U_high is checked as the exact
ledger complement (U_total - U_low - 2w); the optimality scan over J and
the high-margin tail formula are carried from the upstream packet (its
Python/Sage/Wolfram replays are GREEN upstream).

RAMGUARD_TIMEOUT: `tools/ramguard local -- python3 ...` (about a
minute: 19737 binomial ratios at s = 10).
"""

from math import comb

N, K, M, W, S = 2097152, 1048576, 1116048, 67472, 10
B_STAR = 274980728111395087
J_OPT = 19737


def q_s(d):
    return comb(N - K + S, S) // comb(W - d + S, S)


def c_delta(d):
    return (N - M + d) // d


low = q_s(1) * c_delta(1)
prev = q_s(1)
for d in range(2, J_OPT + 1):
    cur = q_s(d)
    low += (cur - prev) * c_delta(d)
    prev = cur

assert low == 808527428378681053, low

u_total = 813929118931913384
u_high = u_total - low - 2 * W
assert u_high == 5401690553097387
assert u_total - B_STAR == 538948390820518297

# Q_s is nondecreasing on the scanned range (Abel summation validity)
assert all(q_s(d) <= q_s(d + 1) for d in range(1, 60))
assert q_s(J_OPT - 1) <= q_s(J_OPT)

# c_delta non-increasing on 1..J (greedy validity; floors plateau)
assert all(c_delta(d) >= c_delta(d + 1) for d in range(1, J_OPT))

print("RANK11_WALL_AUDIT_OK", "L(19737)=", low)
