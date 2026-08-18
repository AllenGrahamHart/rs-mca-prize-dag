# Cycle 482: quadratic quotient-survivor identification

## Result: PROVED cyclic/dihedral classification

The two nonshifted outputs of the quadratic Mobius router are exactly the
quotient pencils already fenced elsewhere in the DAG.

```text
antipodal:        (X-x)(X+x)=X^2-x^2,
constant product: (X-x)(X-kappa/x)=X^2-sX+kappa.
```

The antipodal class is the degree-two cyclic power pencil and has `N/2`
fibers. The constant-product class is the degree-two dihedral pencil. It has
`N/2` fibers for nonsquare `kappa`, or `(N-2)/2` after the two repeated-root
fixed points are omitted when `kappa` is square.

At `N=2^21`, every such quotient pencil therefore has at least

```text
1048575 fibers,
1048575-4370=1044205.
```

This is an exact route decision: neither quotient branch can be removed by a
small-fiber theorem. Their first-owned record currency must be charged by a
factor-owner, denominator, recursive quotient, or chronology ledger.

## Audit

The primary verifier checks every official count and dependency, and replays
all cyclic and dihedral orbits in the order-16 subgroup of `F_97^*`. The
independent audit reconstructs the endpoint arithmetic. Nine contract
mutations are rejected. No Modal computation was used.

## Burn-down

```text
starting local pin:       547af8085
canonical prize pin:      0dd5b3244
upstream main pin:        93fba1be3
critical target attacked: rate_half_band_crossing_location
DAG delta:                +1 PROVED node, +5 edges
critical status delta:    none
route delta:              quadratic quotient classes identified exactly
compute spend:            none
next action:              prove owner-safe quotient payment or shifted cap
```

## Nonclaims

- no quotient record payment;
- no pointwise cap for shifted inversion with `lambda!=0,1`;
- no classification of degrees `1,3,...,11`;
- no high-complexity payment, rank-eleven closure, or MCA closure.
