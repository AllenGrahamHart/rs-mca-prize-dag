# Claim contract

- **claim id:** `f3_hge4_kummer_midpoint_trace_power_gate`
- **mathematical statement:** every primitive near-third Kummer pencil has
  endpoint ratio `x in mu_m\{+/-1}` and midpoint scalar
  `kappa=-(1+x)^2/(8x)`; its trace satisfies one Dickson equation and one
  exact `m`-th-power test, and `x` is necessarily a square
- **scope:** every official exact-ratio level and retained near-third width
  `m=3h+e` with `0<e<h`
- **consumers:** the trace-power gcd compiler and HGE4 exact-level
  orbit/certificate generation
- **status:** `PROVED`
- **proved dependencies:** the near-third Belyi endpoint identities and the
  primitive base-field Kummer midpoint collapse
- **new open content:** bound or classify the primitive split pencils above
  each surviving trace, and sum their exact-level orbit counts
- **falsifier:** one genuine primitive near-third pencil violating `(KTP1)`,
  `(KTP2)`, or `(KTP3)`
- **nonclaims:** no converse, trace-fiber bound, orbit debit, width exclusion,
  exact-level estimate, or HGE4 promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_hge4_kummer_midpoint_trace_power_gate/verify.py`
- **independent audit:**
  `tools/ramguard tiny -- python3 background/nodes/f3_hge4_kummer_midpoint_trace_power_gate/verify_audit.py`
- **upstream mapping:** primitive shift-pair control / base-field-normalized
  split-pencil census
