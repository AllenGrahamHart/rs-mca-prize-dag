# Claim contract

- **claim id:**
  `rate_half_list_budget_three_antipodal_intermediate_hensel_quartic_gate`
- **mathematical statement:** the fourth forbidden Hensel coefficient gives a
  quartic whose remainder modulo the monic quadratic is a second explicit
  linear scalar gate
- **scope:** the `e_2=0,e_3!=0`, `v=(2^38-4)/3` boundary in characteristic
  greater than `d`
- **consumer:** `rate_half_list_adjacent_crossing`
- **status:** `PROVED`
- **proved dependency:** intermediate Hensel cubic gate
- **new open content:** reject the unique scalar selected off the exceptional
  locus and resolve the explicit `A=B=C=D=0` at-most-two-candidate branch
- **falsifier:** valid intermediate data violating `(IH4Q2)--(IH4Q6)`
- **nonclaims:** no proof that `C` is nonzero on `A=B=0`, no candidate
  rejection, no polynomiality theorem, and no adjacent-crossing promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_list_budget_three_antipodal_intermediate_hensel_quartic_gate/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / exact
  intermediate SPI scalar-elimination ledger
