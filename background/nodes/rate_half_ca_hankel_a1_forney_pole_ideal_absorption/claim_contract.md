# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_forney_pole_ideal_absorption`
- **mathematical statement:** on every residual `A=1` curve, the full
  Forney numerator belongs to the colon ideal `(H:G)`, so one contact copy
  cancels the complete pole scheme of `G/H`
- **scope:** all fixed cores `s in {0,1,2}`
- **dependencies:** the core-stripped Forney contact section and contracted
  exceptional-root recurrence factor
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** a supported fibre where the split residual recurrence
  factor fails to divide either `Qbar_gamma` or `G`, or where multiplication
  by the residual cofactor fails to factor the Forney numerator
- **nonclaims:** the contact divisor may strictly exceed the pole scheme
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_forney_pole_ideal_absorption/verify.py`
- **upstream mapping:** exact Forney/SPI pole ledger
