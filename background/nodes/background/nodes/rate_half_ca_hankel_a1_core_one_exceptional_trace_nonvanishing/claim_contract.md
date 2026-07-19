# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_exceptional_trace_nonvanishing`
- **mathematical statement:** a `D_*=1` active core always has nonzero
  exceptional `K` trace; the zero-exceptional third system `(ETA4)` is empty
- **scope:** only the official `A=1,s=1,e=2^38-1,ell=0` face
- **dependency:** the exact exceptional-trace allocation theorem
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** exclude the two active systems `(ETN6)`
- **falsifier:** a zero exceptional trace satisfying the degree-`r-1` fiber,
  full quotient identity, and original `A` degree box
- **nonclaims:** no exclusion when the exceptional trace is active and no
  assertion for `D_*=0`
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_trace_nonvanishing/verify.py`
- **upstream mapping:** exact SPI ledger / active exceptional shift-pair trace
