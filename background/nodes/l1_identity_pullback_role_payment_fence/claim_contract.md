# Claim contract - L1 identity-pullback role-payment fence

## Inputs

- a Reed--Solomon evaluation domain `D` of size `n` and dimension `k<n`;
- an arbitrary received word `U:D->F`;
- the monic degree-one pullback `P=X`;
- for the official anchored consequence, the canonical cutoff
  `ell<char(F)`.

## Output

The pullback quotient list is exactly the original ordinary list, with
`B=D`, `kappa=0`, and `z=0`. The degree-one map automatically carries every
source petal and is tame at the official cutoff.

## Falsifier

An `f` whose identity-pullback quotient agreement differs from
`Agr(f,U)`; a nonzero partial loss for singleton fibers; or an official
canonical row on which the degree-one endpoint is wild.

## Nonclaims

No list-size bound, Q-flatness theorem, Toeplitz-section bound, or payment for
any degree `s>=2`.
