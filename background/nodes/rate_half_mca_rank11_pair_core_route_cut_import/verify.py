#!/usr/bin/env python3
"""Identity checks for the PR #1168 rank-eleven route-cut import.

RAMGUARD_TIMEOUT: `tools/ramguard tiny -- python3 ...` (seconds).
"""

N, K, M, W = 2097152, 1048576, 1116048, 67472
B_STAR = 274980728111395087

U_HIGH = 5401690553097387
U_LOW = 808527428378681053
U_TOTAL = 813929118931913384

# ledger identities
assert U_TOTAL == U_HIGH + U_LOW + 2 * W
assert U_TOTAL - B_STAR == 538948390820518297
assert U_TOTAL > B_STAR
assert 10 * U_TOTAL > 29 * B_STAR          # misses by a factor > 2.9
assert 811958533186703629 > B_STAR          # nonuniform relaxation also over

# per-pair record caps dominate the printed record loads
def c_delta(d):
    return (N - M + d) // d

assert c_delta(8) == 122639 >= 114624
assert c_delta(4) == 245277 >= 200632

# the rank-10 predecessor identity (paid stratum below this wall)
assert 61871313426765543 + 213109414684629544 == B_STAR

print("RANK11_PAIR_CORE_ROUTE_CUT_IMPORT_OK",
      "wall_excess=", U_TOTAL - B_STAR)
