# Claim contract

- **claim id:** `f3_hge4_kummer_trace_power_gcd_compiler`
- **mathematical statement:** a squarefree Chebyshev trace quotient and one
  modular polynomial gcd count exactly the endpoint traces passing the HGE4
  Kummer power gate
- **scope:** every official dyadic exact-ratio level `m>=8` and compatible
  prime `p`
- **consumer:** HGE4 exact-level candidate generation
- **status:** `PROVED`
- **proved dependency:** the Kummer midpoint trace-power gate
- **new open content:** classify and count all primitive pencils above each
  passing trace and prove the exact-level aggregate
- **falsifier:** a trace admitted by `(KTP2)--(KTP4)` but omitted by the gcd,
  a gcd root not admitted by those gates, or a wrong count in a control row
- **nonclaims:** no trace-fiber bound, pencil reconstruction, orbit debit,
  width emptiness, exact-level estimate, or HGE4 promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_hge4_kummer_trace_power_gcd_compiler/verify.py`
- **independent audit:**
  `tools/ramguard tiny -- python3 background/nodes/f3_hge4_kummer_trace_power_gcd_compiler/verify_audit.py`
- **upstream mapping:** primitive shift-pair / exact split-pencil endpoint
  compiler
