# Claim contract

- **claim id:**
  `rate_half_list_budget_three_antipodal_intermediate_hensel_cubic_gate`
- **mathematical statement:** the third forbidden Hensel coefficient gives a
  cubic whose remainder modulo the monic quadratic is one explicit linear
  scalar gate
- **scope:** the `e_2=0,e_3!=0`, `v=(2^38-4)/3` boundary in characteristic
  greater than `d`
- **consumer:** `rate_half_list_adjacent_crossing`
- **status:** `PROVED`
- **proved dependency:** intermediate Hensel quadratic gate
- **new open content:** reject the unique scalar selected when `A!=0` and
  resolve the explicit `A=B=0` at-most-two-candidate branch
- **falsifier:** valid intermediate data violating `(IHCQ2)--(IHCQ6)`
- **nonclaims:** no proof that `A` is nonzero, no candidate rejection, and no
  adjacent-crossing promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_list_budget_three_antipodal_intermediate_hensel_cubic_gate/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / exact
  intermediate SPI scalar-elimination ledger
