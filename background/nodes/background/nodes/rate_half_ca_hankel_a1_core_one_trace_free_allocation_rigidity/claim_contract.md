# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_trace_free_allocation_rigidity`
- **mathematical statement:** the dominant norm residual is exactly the
  product of local row-defect quotients; in the trace-free weld, every domain
  factor has the forced `A,B` allocation, and the exceptional slope has one
  of two exact allocations, yielding the reduced complement square `(TFA7)`
- **scope:** only the official `A=1,s=1,e=2^38-1,ell=0` face
- **dependency:** the nonzero-weld trace-descent router and its inherited
  component norm identity
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** exclude the active traces and the two rigid forms of
  the reduced complement square
- **falsifier:** an extra factor in `S_*`, a trace-free domain factor not
  dividing both `A,B`, or an exceptional allocation outside `(TFA4)`
- **nonclaims:** no global gluing of fiber gcds and no exclusion of a reduced
  system
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_trace_free_allocation_rigidity/verify.py`
- **upstream mapping:** exact SPI norm ledger / trace-free shift-pair
  allocation rigidity
