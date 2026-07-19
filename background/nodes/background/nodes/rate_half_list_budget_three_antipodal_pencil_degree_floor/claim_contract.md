# Claim contract

- **claim id:** `rate_half_list_budget_three_antipodal_pencil_degree_floor`
- **mathematical statement:** the unique degree-drop direction in the
  antipodal quotient pencil has degree at least `ceil((r-4)/2)`, improved to
  `ceil((2r-4)/3)` when the centered coefficient `e_2` vanishes
- **scope:** direct equal-fiber linear `K_4` antipodal component on the
  maximal official `B*=3` row; more generally any such descent in
  characteristic zero or characteristic greater than `d`
- **consumer:** `rate_half_list_adjacent_crossing`
- **status:** `PROVED`
- **proved dependencies:** antipodal Mobius weld and maximal-row field-degree
  collapse
- **new open content:** classify or exclude the generic interval
  `ceil((r-4)/2)<=v<=r-1` and the intermediate interval
  `ceil((2r-4)/3)<=v<=r-1`
- **falsifier:** valid descended data with a smaller `v`
- **nonclaim:** no emptiness theorem for the surviving high-degree interval
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_list_budget_three_antipodal_pencil_degree_floor/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census, reverse
  contact and moving-root equality case
