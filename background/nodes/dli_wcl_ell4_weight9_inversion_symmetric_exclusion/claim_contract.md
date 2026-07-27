# Claim contract

- **claim id:** `dli_wcl_ell4_weight9_inversion_symmetric_exclusion`
- **scope:** inversion-invariant normalized Pell divisors in the WCL `(4,9)`
  endpoint
- **status:** `PROVED`
- **dependency:** `dli_wcl_ell4_weight9_quartic_divisor_descent`
- **consumer:** `dli_wcl_slot_4_9_emptiness`, as `ev` only
- **load-bearing computation:** eight exact quotient-ring remainder checks
  and cubic resultants in the pinned JSON certificate
- **excluded characteristics:** every characteristic outside
  `{2,3,17,19}`; the four exceptions are all incompatible with official
  `v_2(p-1)>=41`
- **nonclaims:** no assertion that every `(4,9)` divisor is
  inversion-invariant; no classification of the four exceptional
  characteristics; no full-slot or WCL-zone promotion
- **falsifier:** one candidate at the printed scope outside the four
  exceptional characteristics
- **primary replay:** `tools/ramguard tiny -- python3
  background/nodes/dli_wcl_ell4_weight9_inversion_symmetric_exclusion/verify.py`
- **independent replay:** `tools/ramguard tiny -- python3
  background/nodes/dli_wcl_ell4_weight9_inversion_symmetric_exclusion/verify_audit.py`
