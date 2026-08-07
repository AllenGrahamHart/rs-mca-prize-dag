# WCL `(1,6)` sign-product formula pricing

- **consumer:** unsigned sign-product router
- **input:** `Psi_6`, the product of the 32 global-sign classes
- **question:** does `Psi_6` admit a compact exact expression in the six
  elementary symmetric functions of the squared roots?

One Modal container will eliminate `r_6,...,r_2` by paired sign products,
replace `r_i^2` by `y_i`, eliminate the final even powers of `r_1`, and call
exact symmetric reduction. Every stage prints a term-count marker. The
subprocess cap is 55 seconds; timeout banks only the completed stage markers.

## Promotion rule

- `COMPLETE` with zero symmetric remainder and a modest term count: bank the
  formula as part of the unsigned router theorem.
- `TIMEOUT`: retain the abstract 32-factor product and do not retry this
  expanded representation.
- nonzero symmetric remainder or failed direct evaluation: implementation
  alarm; no theorem promotion.

This is formula pricing only. It computes no cyclotomic norm, factorization,
or official-row exclusion.

## Result

Modal app `ap-WDu6iFzptBZRCVSDtGD5Wu` returned `TIMEOUT`. Exact paired
elimination reached term counts `16,58,294,2079` through elimination of
`r_6,r_5,r_4,r_3` and did not finish the next stage before the 55-second
subprocess cap. Under the promotion rule, the expanded elementary-symmetric
representation is retired. The abstract 32-factor product remains the
router of record and does not depend on this failed expansion.
