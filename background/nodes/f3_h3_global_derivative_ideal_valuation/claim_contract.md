# Claim contract

- **claim id:** `f3_h3_global_derivative_ideal_valuation`
- **statement:** the explicit odd integer `e_n` satisfies `p^X_18|e_n` for
  every prime-field order-`n` row
- **scope:** every dyadic `n>=4`; in particular all 29 C36 orders and all
  primes `p=1 mod n`
- **consumer:** `f3_h3_mobius_excess_half`, joint exceptional-prime reduction
- **status:** `PROVED`
- **dependency:** `f3_h3_shifted_product_sidon`
- **new open content:** bound or exclude the official prime divisors of `e_n`
- **falsifier:** one in-scope `(n,p)` with `v_p(e_n)<X_18`
- **replay:** `python3 background/nodes/f3_h3_global_derivative_ideal_valuation/verify.py`
- **upstream mapping:** primitive shift-pair control / exact second-moment
  ledger

This is a joint arithmetic reduction. It does not promote C36' without an
upper bound or exceptional-prime exclusion for `e_n`.
