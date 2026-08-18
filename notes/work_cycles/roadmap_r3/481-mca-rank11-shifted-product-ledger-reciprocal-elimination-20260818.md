# Cycle 481: shifted-product ledger and reciprocal elimination

## Result: two PROVED exact reductions

For the surviving quadratic shifted-inversion pencil, define

```text
R(tau,kappa)=#{(x,y) in H^2:(x+tau)(y+tau)=kappa},
F(tau,kappa)=#{x in H:(x+tau)^2=kappa},
I(tau,kappa)=R(tau,kappa)-F(tau,kappa).
```

The graph interpretation, first moments, multiplicative-energy second
moment, `H`-scaling, and coordinate-inversion identities are now exact DAG
theorems. In particular, `I` counts ordered nonfixed graph points, `I/2`
counts disjoint fibers, and the scale-invariant parameter is
`lambda=kappa/tau^2`. This reduces the shift to 1,016 subgroup cosets without
claiming a pointwise cap.

The exceptional parameter `lambda=1` is closed. Here `kappa=tau^2`, and
coordinatewise inversion on `H^2` transforms the product graph into

```text
u+v=-1/tau.
```

This is a fixed nonzero affine-reflection pencil. Its proved exact cap of
1,154 fibers contradicts the required 4,370 fibers, with margin 3,216
(equivalently 6,432 graph points).

## Audit

Both nodes pass primary verification, independent audit, and nine mutation
tests each. A subgroup of order 16 in `F_97^*` independently replays the
first/second moments, scaling, reciprocal symmetry, and the `lambda=1`
graph bijection. No Modal computation was needed.

## Route wall

The dense shifted-subgroup energy asymptotic controls a second moment, not
the largest representation count. One 8,740-point fiber is too small to
contradict that estimate at the official parameters, while the available
`32N^(2/3)` curve bound also exceeds 8,740. The general `lambda!=0,1`
shifted class therefore remains open and needs a pointwise dense-cyclotomy
bound, a higher-moment inverse theorem with explicit constants, or retained
factor-owner semantics.

## Burn-down

```text
starting local pin:       cbbbb0a60
canonical prize pin:      0dd5b3244
upstream main pin:        93fba1be3
critical target attacked: rate_half_band_crossing_location
DAG delta:                +2 PROVED nodes, +5 edges
critical status delta:    none
eliminated locus:         quadratic shifted inversion with lambda=1
compute spend:            none
next action:              pay lambda!=0,1 or the retained quotient classes
```

## Nonclaims

- no pointwise cap for general shifted inversion;
- no payment of antipodal or constant-product quotient classes;
- no classification of degrees `1,3,...,11`;
- no high-complexity payment, rank-eleven closure, or MCA closure.
