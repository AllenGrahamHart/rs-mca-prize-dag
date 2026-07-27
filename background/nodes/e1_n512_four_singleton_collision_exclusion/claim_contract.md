# Claim contract

## Inputs

- `e1_prime_field_l2_norm_collision_radius`, including the folded profile
  convention and the lower endpoint `p>=2^250`;
- `collision_norm_criterion`.

## Output

The folded profile `(a,b,c)=(0,4,0)` at `N=512,s=2` produces no collision at
any named pair-feasible anchor.

## Guards

1. The four singleton coefficients occupy distinct folded coordinates and
   lie in `{+1,-1}`.
2. The norm is the full `Phi_512` norm over all 256 odd conjugates.
3. The `V=2` autocorrelation case is treated separately; the `V>=4`
   logarithmic deficit does not cover it.
4. A pure power-of-two norm is excluded using oddness of the row prime, not a
   size comparison.
5. Profile `(1,2,0)`, higher swap-distance bands, and the total collision
   ledger remain open.

## Falsifier

An odd prime `p>=2^250` and a four-singleton folded vector whose nonzero
cyclotomic norm is divisible by `p`, or a failure of the printed variance or
cyclotomic-product identities.
