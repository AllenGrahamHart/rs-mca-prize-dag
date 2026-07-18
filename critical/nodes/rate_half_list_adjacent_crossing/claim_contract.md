# Claim contract: rate-half ordinary-list crossing

```text
claim id: rate_half_list_adjacent_crossing
mathematical statement: every official rate-half row has an ordinary worst-list
  adjacent crossing L_1(a)<=B*<L_1(a-1)
quantifiers and row scope: every admissible official rate-1/2 row
consumer and exact slot: the rate-half branch of list_adjacency_closing
current status: TARGET
dependencies already proved: list_crossing_localization;
  rate_half_cyclic_rotated_prefix_floor (unsafe evidence);
  rate_half_list_integer_johnson_safe_anchor (safe evidence);
  rate_half_list_low_budget_exact_crossing (B*=1,2 exact);
  list_subsqrt_interleaving_collapse (post-crossing arity transport)
new open content: for every B*>=3, narrow the proved unsafe/safe bracket to
  one adjacent pair with a matching predecessor witness
falsifier: a received word exceeding B* at an asserted safe agreement
proof route being attempted: exact rate-half image-fiber/profile envelope or a
  stronger safe-side theorem paired with a new predecessor witness
replay command: tools/ramguard tiny -- python3
  critical/nodes/rate_half_list_adjacent_crossing/verify.py
upstream hard-input mapping: complete profile-envelope comparison with the
  target; rate-half list side
```
