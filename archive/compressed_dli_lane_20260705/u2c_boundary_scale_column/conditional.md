# u2c_boundary_scale_column conditional proof

## Predicate node

- `b2_modp_giant_extras`

## Claim

The boundary-scale repair column is complete once the finite-field extras bound
is proved.

## Proof

The node has three parts.

First, the dictionary clause for characteristic-zero giant blocks is already
covered by `b1_char0_giant_coset_theorem`: every 0/1 `t`-null vector on a
2-power root domain is a union of `mu_M`-cosets at the first scale `M > t`.

Second, the boundary-scale `M = t` zero-sum coset class is explicit. It is
counted by subset-sum collision counts on the quotient values, and the QA.25
arithmetic recorded in the node notes verifies that this column fits the six
campaign candidates.

Third, every remaining finite-field block is, by definition, a mod-p extra
beyond the char-0 coset classes and the boundary zero-sum class. The predicate
`b2_modp_giant_extras` is exactly the asserted no-concentration bound for that
residual class.

Combining the proved char-0 classification, the exact boundary count, and
`b2_modp_giant_extras` exhausts the column. Thus the repair is conditional only
on that residual finite-field lemma.
