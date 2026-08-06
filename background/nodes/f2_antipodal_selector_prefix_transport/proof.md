# Proof

The points `theta^s` for `0<=s<m` represent the `m` antipodal pairs in
`D`, so choosing the positive or negative representative according to
`x_s` is a bijection onto the antipodal transversals.

For every exponent `l`, the contribution from pair `s` is

```text
x_s theta^(sl)+(1-x_s)(-theta^s)^l.
```

If `l` is even this is `theta^(sl)`, independently of `x_s`. If `l` is
odd it is `(2x_s-1)theta^(sl)`. Summing over `s` proves `(AS-1)`.
Because `2` is invertible, the odd coordinates in `(AS-1)` recover
`A(x)`, while the even coordinates are fixed. Hence a syndrome fiber maps
bijectionally to the transversal members of the displayed ordinary prefix
fiber. Forgetting the transversal condition proves `(AS-2)`.

For `j<=2R<p`, Newton's triangular identities have invertible diagonal
coefficient `j`. Equality of the first `2R` power sums is therefore
equivalent to equality of the first `2R` elementary symmetric functions,
or of the top `2R` nonleading coefficients of the monic locator
`prod_(a in E)(X-a)`. This is the split-locator prefix dictionary.

The plus-branch class matrix has columns
`theta^(s(2j-1))`. The exact-order presentation can add a nonzero factor
depending only on `j`, which is an invertible row scaling. The minus-branch
coefficient presentation is the same formula with its root `omega` of
order `2m`. Existing branch reductions and generated-field invariance
therefore instantiate the generic transport. The mass consequence follows
from `Z<=M`. QED.
