# Claim contract

- **claim id:** `f3_h3_double_accident_coupling_batch_odd_saturation`
- **mathematical statement:** after inverting two, one anchored coupling plus
  quotient-collision generators generates the same ideal as the symmetric
  batch of all product-to-quotient couplings; hence their odd prime-ideal
  valuations and odd ideal-norm parts agree
- **scope:** every dyadic order and every finite collection of nonidentity
  quotient lifts
- **consumer:** `f3_h3_mobius_excess_half`
- **status:** `PROVED`
- **proved dependencies:** joint-ideal router and nonzero-coupling router
- **new open content:** control of the common odd ideal norm or its surviving
  row primes
- **falsifier:** one dyadic order and odd prime ideal at which the two ideals
  in `(CBS5)` have different localizations
- **nonclaims:** no equality at the dyadic prime, no generator-independence
  assertion, no ideal-index lower bound, and no C36' promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_double_accident_coupling_batch_odd_saturation/verify.py`
- **independent audit:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_double_accident_coupling_batch_odd_saturation/verify_audit.py`
- **upstream mapping:** exact SPI / primitive shift-pair ledger, with
  two-primary normalization separated from odd row-prime alignment
