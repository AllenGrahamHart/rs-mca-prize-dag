# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_trace_free_exclusion`
- **mathematical statement:** the trace-free nonzero-weld branch is empty;
  every official core-one maximal-degree sharp-cap profile has a nonzero trace
  of `K` on a nonsaturated domain row or the exceptional supported slope
- **scope:** only the official `A=1,s=1,e=2^38-1,ell=0` face
- **dependency:** the exact trace-free allocation and reduced complement
  square
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** exclude the active-trace factorizations `(NWT4)` and
  `(NWT7)`
- **falsifier:** a trace-free profile satisfying the reduced square, capacity
  identity, and original `A` degree box
- **nonclaims:** no exclusion of an active trace and no statement about other
  cores or degrees
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_trace_free_exclusion/verify.py`
- **upstream mapping:** exact SPI ledger / forced active shift-pair trace
