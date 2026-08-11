# Cycle 134: rate-half paired-biform coefficient-MDS gate (2026-08-11)

## Cycle pins

```text
starting source:  1833bfc0c
canonical prize:  5774b9ba3c2c9b72c526b97b7b71da1a19bca9a2 plus dirty pilots
upstream main:    93fba1be3f3299b0ba4708d88715377bbb656e45
compute:          F_101 parity audit; F_337/F_421 exact rank probes
critical open:    28
```

## Exact realizability matrix

For every classified split row `x`, write

```text
G(t,x)=lambda_x product_(delta in A_x)(t-delta).
```

Because every coefficient of `G` has the same low `X`-degree, each vector
of scaled elementary-symmetric functions belongs to one punctured RS code.
Equivalently, the printed coefficient-barycentric matrix has a kernel vector
`lambda` with every coordinate nonzero. The leading coefficient is the
shared denominator, so all root-set profiles are values of rational
functions with one common denominator.

For the official zero-deficit profiles the matrix dimensions are

```text
extremal:  100743818300669342078294 rows x 824633720829 columns;
strict:     50371909150884426853035 rows x 549755813888 columns.
```

The row count is not a rank argument. The closure task is now precise:
prove that every incidence pattern allowed by the relevant pair boundary
makes this matrix lack a full-support kernel, or exhibit a survivor and
identify the additional source/Hankel equation it still must satisfy.

At `e=7,d_A=1`, the exact smooth cyclic degree ledger has full rank in both
`F_337` and `F_421`; 250 degree-preserving switch trials per field were also
full rank. This validates the obstruction but remains explicitly
non-exhaustive evidence.

## Burn-down

```text
result:                  PROVED paired coefficient-MDS kernel gate
DAG delta:               +1 PROVED
critical status delta:   none
terminal delta:          pair profiles gain exact finite rank falsifiers
delta-star movement:     none
new assumptions:         none
compute requests:        none
```
