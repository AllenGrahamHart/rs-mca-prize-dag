# Claim contract

- **claim id:**
  `rate_half_list_budget_three_antipodal_intermediate_hensel_certifier`
- **mathematical statement:** the maximal intermediate floor has the canonical
  Hensel equation `(IHC5)` and terminal gate `(IHC7)`, yielding the exact
  three-way candidate split `(IHC8)`
- **scope:** the `e_2=0,e_3!=0`, `v=(2^38-4)/3` boundary in characteristic
  greater than `d`
- **consumer:** `rate_half_list_adjacent_crossing`
- **status:** `PROVED`
- **proved dependency:** antipodal fourth-root gap reduction
- **new open content:** reject the unique nondegenerate candidate and the
  explicitly isolated degenerate one-parameter branch, then treat above-floor
  and pure-quartic strata
- **falsifier:** valid intermediate data violating `(IHC5)--(IHC9)`, or a
  printed passing certificate that does not reconstruct a valid pencil
- **nonclaims:** no rejection theorem and no adjacent-crossing promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_list_budget_three_antipodal_intermediate_hensel_certifier/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / exact
  intermediate SPI Hensel ledger
