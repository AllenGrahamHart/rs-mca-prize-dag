# Claim contract

- **claim id:** `f3_h3_double_accident_coupling_matrix_odd_saturation`
- **mathematical statement:** after inverting two, the complete joint ideal,
  a coupling cross, and the full product-by-quotient coupling rectangle are
  equal; characteristic-zero zero entries form a partial matching
- **scope:** every dyadic order and every pair of families of sizes `m,r>=2`
  consisting of distinct unordered product lifts and distinct ordered
  nonidentity quotient lifts
- **consumer:** `f3_h3_mobius_excess_half`
- **status:** `PROVED`
- **proved dependencies:** coupling-batch odd saturation and dyadic
  shifted-product Sidonicity
- **new open content:** a bound for the common odd ideal norm across official
  rows
- **falsifier:** one odd prime ideal at which the three ideals in `(CM5)` have
  different localizations, or one row/column with two characteristic-zero
  zero couplings
- **nonclaims:** no equality at the dyadic prime, no independence of matrix
  entries, no ideal-index lower bound from `(CM6)`, and no C36' promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_double_accident_coupling_matrix_odd_saturation/verify.py`
- **independent audit:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_double_accident_coupling_matrix_odd_saturation/verify_audit.py`
- **upstream mapping:** exact SPI / primitive shift-pair ledger, expressed as
  a base-field-normalized coupling matrix
