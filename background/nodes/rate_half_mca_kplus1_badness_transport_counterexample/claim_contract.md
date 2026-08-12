# Claim contract

- **claim id:** `rate_half_mca_kplus1_badness_transport_counterexample`
- **status:** `PROVED`
- **scope:** one explicit deployed KoalaBear slope/support record
- **output:** support-wise MCA badness is not preserved by silent
  `RS[...,k] -> RS[...,k+1]` substitution
- **falsifier:** a failed field/support check or simultaneous degree-`<k`
  explanation on the displayed support
- **nonclaims:** no refutation of a degree-guarded adapter, Q/BC owner
  assignment, slope bound, endpoint realization, or row closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_kplus1_badness_transport_counterexample/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_kplus1_badness_transport_counterexample/verify_audit.py`
- **upstream mapping:** `OVERLAP`; promotes the mutation control in upstream
  `#1159` into an explicit witness-semantics theorem
