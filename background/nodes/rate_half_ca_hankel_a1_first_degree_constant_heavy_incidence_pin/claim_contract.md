# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_constant_heavy_incidence_pin`
- **mathematical statement:** every heavy-row supported incidence in a
  parameter-constant boundary profile consumes one unit of specialized
  excess recurrence degree; exact incidence balance leaves residual degrees
  `2..5` for core zero and `1..2` for core one
- **scope:** `e=ceil((rho-1)/3)`, `j=0`, `s in {0,1}`
- **dependencies:** ambient defect factorization, bounded residual table,
  and the contracted recurrence/Forney factorization
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** a heavy-row incidence with nonzero Forney numerator, more
  heavy incidences than total excess degree, or failure of `(CHI3)`
- **nonclaims:** no remaining residual degree is excluded
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_constant_heavy_incidence_pin/verify.py`
- **upstream mapping:** split-pencil / exact SPI incidence ledger
