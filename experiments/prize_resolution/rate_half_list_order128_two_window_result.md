# Rate-half list order-128 simultaneous two-window pilot

- **status:** experimental route evidence; no theorem promotion.
- **Modal apps:** exhaustive scan `ap-K60XbR1aXkETENbT2n7A4b`; orbit
  classification `ap-CxjRuOXnLkrszE6llB1U4m`.
- **resources:** twelve bounded functions with one physical CPU, 512 MiB RAM,
  and a 60-second hard timeout; all shards completed. The conservative
  requested-resource ceiling was below `$0.10`.
- **scope:** every `C(128,4)=10668000` deleted-root quadruple in each of the
  first eight prime fields containing an order-128 subgroup, plus the known
  order-64 control.
- **result hash:**
  `d26d03529e890157653cd69b85396dcb3984f98e130ab29985fe99af1b5548a1`.

Only `F_257` and `F_641` contain primary double gaps, with `192` packets in
each field. None of the `384` order-128 packets, and none of the `64` control
packets, passes the secondary two-window terminal-zero test.

Modulo common subgroup scaling, each positive order-128 field has one orbit
of size `128` and one of size `64`. The latter is exactly two deleted
antipodal pairs:

```text
p=257: {0,20,64,84}, terminal=(0,31)
p=641: {0, 6,64,70}, terminal=(0,381)
```

This makes parity reduction of the two-window gate a useful algebraic sublane.
It does not support an official-order conclusion: there is no transport from
fixed order `128` to the official growing dyadic order. CR-002 records the
worthwhile contributor computation as a compressed, coverage-proved symbolic
classification. More raw fixed-order prime or order sweeps are explicitly not
requested.

Replay the compact packet with

```text
tools/ramguard tiny -- python3 experiments/prize_resolution/rate_half_list_order128_two_window_check.py
```
