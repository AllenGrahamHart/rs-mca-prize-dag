# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_max_component_localization`
- **mathematical statement:** on the `A=1`, `s=1`, `e=2m-1`, `ell=0`
  face, one unique component has bidegree `(2e_*+1,e_*)`; every residual
  component has `(2e_i,e_i)`, their total parameter degree is at most `e/5`,
  and the official dominant component has separation rank at least five
- **scope:** only the half-distance core-one maximal-degree sharp cap
- **dependency:** the core-stratified `A=1` residual router
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** exclude a genuinely mixed dominant component of
  separation rank at least five under the two-direction split-fiber ledger
- **falsifier:** a component with `r_i-2e_i<0`, two positive defects, residual
  parameter degree above `floor(e/5)`, or dominant separation rank below the
  printed lower bound
- **nonclaims:** the sharp-cap stratum is not closed and no statement is made
  about other cores, degrees, or positive slope slack
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_max_component_localization/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / exact
  core-one component ledger
