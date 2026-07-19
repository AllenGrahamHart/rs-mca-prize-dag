# Claim contract

- **claim id:**
  `rate_half_list_budget_three_antipodal_intermediate_hensel_quadratic_gate`
- **mathematical statement:** the second forbidden Hensel coefficient is a
  monic quadratic in the outer scalar, so the intermediate boundary has at
  most two scalar candidates even on the degenerate first gate
- **scope:** the `e_2=0,e_3!=0`, `v=(2^38-4)/3` boundary in characteristic
  greater than `d`
- **consumer:** `rate_half_list_adjacent_crossing`
- **status:** `PROVED`
- **proved dependency:** antipodal intermediate Hensel certifier
- **new open content:** reject the at-most-two exact Hensel candidates, then
  treat above-floor and pure-quartic strata
- **falsifier:** valid intermediate data violating `(IHQ3)--(IHQ6)`
- **nonclaims:** no candidate rejection, no polynomiality inference, and no
  adjacent-crossing promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_list_budget_three_antipodal_intermediate_hensel_quadratic_gate/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / exact
  intermediate SPI finite-candidate ledger
