# Cycle 483: quadratic quotient factor-through interface

## Result: PROVED certificate-level inverse theorem

In the synchronized degree-two scalar-locator certificate, put `f=-u/v`.
The cyclic and dihedral locator-span identities imply

```text
antipodal:        f(X)=M(X^2),
constant product: f(X)=M(X+kappa/X),
```

for one base-field Mobius postcomposition `M`. The proof is an invertible
basis change: antipodal locators span `<X^2,1>`, while constant-product
locators span `<X^2+kappa,X>`.

This upgrades the previous root-orbit classification. The quotient factor is
now present in the actual rational slope map retained by the rank-eleven
certificate, which is the exact interface needed by Przemek's proposed
quotient-periodic inverse route.

## Audit

The primary verifier checks the source contract and all dependencies, then
tests arbitrary Mobius postcompositions for invariance under `x -> -x` and
`x -> kappa/x` in an order-16 subgroup of `F_97^*`. All 192 checks pass. The
independent proof audit passes, and nine contract mutations are rejected. No
Modal computation was used.

## Burn-down

```text
starting local pin:       6b93af319
canonical prize pin:      0dd5b3244
upstream main pin:        93fba1be3
critical target attacked: rate_half_band_crossing_location
DAG delta:                +1 PROVED node, +3 edges
critical status delta:    none
route delta:              quadratic quotient inverse step completed
compute spend:            none
next action:              build owner-safe quotient charge for factored maps
```

## Nonclaims

- no payment or deduplication of quotient records;
- no pointwise shifted-inversion cap;
- no nonquadratic split-pencil classification;
- no high-complexity payment, rank-eleven closure, or MCA closure.
