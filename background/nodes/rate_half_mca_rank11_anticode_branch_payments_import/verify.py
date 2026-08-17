#!/usr/bin/env python3
"""Independent arithmetic replay of the #1171/#1172/#1173 envelopes.

RAMGUARD_TIMEOUT: `tools/ramguard tiny -- python3 ...` (seconds).
"""

B_STAR = 274980728111395087
NEAR = 134944

# 1171: fixed-right ray cap and slack
assert B_STAR - 8147918 == 274980728103247169

# 1172: the rank-one branch payment at tau = 439
low_1172 = 32215263489919749
high_1172 = 242314927584173240
total_1172 = low_1172 + high_1172 + NEAR
assert total_1172 == 274530191074227933
assert B_STAR - total_1172 == 450537037167154
assert total_1172 + 96628092421444 + 450537037167154 - 96628092421444 == B_STAR
# cutoff-438 wall: over budget by the printed excess
assert B_STAR + 96628092421444 == total_1172 + 450537037167154 + 96628092421444
assert 81826485385525648 < B_STAR  # envelope minimum at tau = 3608

# 1172 residual constants
assert 1115609 + 1115609 - 2097152 == 134066  # |H_e|+|H_f|-n forces overlap

# 1173: anchored rich-flat cell (tau, h) = (1547, 42452)
r1 = 60010642445729852
r2 = 146093034425737644
anchor = 982651
tail = 68875044016173272
total_1173 = r1 + r2 + anchor + tail + NEAR
assert total_1173 == 274978720888758363
assert B_STAR - total_1173 == 2007222636724
# h = 42453 wall
assert total_1173 + 2007222636724 + 17108854816460 \
    == B_STAR + 17108854816460

print("RANK11_ANTICODE_BRANCH_IMPORT_OK",
      "slack_1172=", B_STAR - total_1172,
      "slack_1173=", B_STAR - total_1173)
