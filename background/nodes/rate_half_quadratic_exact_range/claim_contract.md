# Claim contract

- **Claim:** exact rate-half adjacent MCA determination throughout the field
  range where the quadratic MDS staircase applies at safe radius `B-1`, plus
  a safe/unsafe bracket through `B<=k-1` and a CA-only adjacent reduction
  through `B<=2^39+1`.
- **Quantifiers:** every admissible field order `q` with
  `1<=floor(q/2^128)<=389,500,552,609` and every official order-`2^41`
  Reed-Solomon evaluation domain in that field.
- **Dependency:** the proved general theorem `mca_quadratic_prize_rows`.
- **Consumer:** `rate_half_band_closure`.
- **Nonclaims:** no safety assertion at or above the exclusive field cutoff,
  except for the printed fixed quadratic endpoint; no proof of the CA-only
  assertion `(RQ4)`; no ordinary-list or interleaved-list determination.
- **Falsifier:** failure of the quadratic hypothesis at `r=B-1`, or failure
  of the universal `B+1`-slope lower construction at `r=B`.
