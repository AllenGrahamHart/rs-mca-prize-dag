# Claim contract

- **claim id:** `rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity`
- **mathematical statement:** if the centered antipodal pencil parameters
  satisfy `e_2=e_3=0`, then the unique degree-drop direction has degree
  exactly `r-1`, both directions are squarefree, and its second-derivative
  Wronskian has residual degree one
- **scope:** antipodal quotient pencil in characteristic zero or
  characteristic greater than `d`
- **consumer:** `rate_half_list_adjacent_crossing`
- **status:** `PROVED`
- **proved dependency:** antipodal pencil degree floor and its descended
  product setup
- **new open content:** solve the printed linear-residual differential identity
  or otherwise exclude the `v=r-1` pure-quartic stratum, and treat the generic
  `e_2!=0` and intermediate
  `e_2=0,e_3!=0` strata
- **falsifier:** valid pure-quartic descended data with `v<r-1` or with a
  nonlinear Wronskian residual, a repeated root of `UV`, or two roots of `UV`
  in `Z(D) union {0}`
- **nonclaim:** no emptiness theorem for the `v=r-1` stratum
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity/verify.py`
- **upstream mapping:** base-field-normalized split-pencil equality-stratum
  rigidity
