# Audit

## Scope audit

The proof starts only after the matched `c=0` generic cycle boundary has
passed canonical span and the parameter-uniform even factorization. It makes
no inference for intermediate, pure, above-floor, or denominator-mismatch
strata.

## Arithmetic audit

- `M=2^36` gives `N=8M=2^39`, `2N=2^40`, and `4N=2^41`.
- The resultant bounds are reproved at this `N`; the fixed-order old theorem
  is not treated as a black-box scale transfer.
- `2N | p-1`, not `4N | p-1`, is sufficient for every element of `mu_N` to
  be a square in `F_p`. This is the exact hypothesis used for outer-root
  descent.
- In the nonsplit residue class, `r^p=r^(1+2N)=r^(2N)r`. No assertion that
  all `4N`th roots lie in `F_p` is made before the three matching equations
  eliminate the anti-invariant shard.

## Conjugation audit

For the first and third matching equations, comparing `r` and `-r` forces
`r^2=-1`, inconsistent with `r^(2N)=-1`. For the middle equation, the two
signs in `(r-1)^4=+/-(r+1)^4` yield either the same contradiction or the
common quadratic `X^2+6X+1` for `r^2` and `q_out`; their incompatible
`N`th powers then finish the exclusion.

## Computation audit

Both local verifiers are tiny exact checks. No Modal job, official-scale
enumeration, or unpriced computation supports the theorem. CR-002-C remains
a contributor pre-request because its later algebraic gates are not yet
coverage-equivalent at the doubled order.
