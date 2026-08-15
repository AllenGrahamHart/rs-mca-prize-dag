# Cycle 344: MCA rank-11 rank-eight minimal-shortening exclusion (2026-08-15)

Cycle 343 showed that the current fixed-chart output is genuinely realizable
at `K'=11`.  Before attacking its global ancestry, this cycle checks the
shortest residual row separately and closes it by dimension equality.

## Exact one-row exclusion

The dense-root saturation theorem places the fixed ten-dimensional
correction space inside the residual Reed-Solomon space:

```text
V' <= RS_{<K'},       dim V'=10.
```

At `K'=10`, the ambient space also has dimension ten.  Hence

```text
V'=RS_{<10}.
```

On any nine distinct residual coordinates, the polynomials
`1,X,...,X^8` have a nonzero Vandermonde determinant.  Equivalently,
nine-point Lagrange interpolation is surjective.  Therefore every nine-set
has evaluation rank nine, while the live affine-owner branch requires rank
eight.  That branch is empty at `K'=10`.

The boundary is exact for this argument.  At `K'=11`, the cycle-343 space

```text
span{1,X,...,X^7,L_B,XL_B}
```

has dimension ten and evaluation rank eight on `B`.  Thus no monotone
extension of the one-row proof is asserted.

```text
RATE_HALF_MCA_RANK11_RANK8_MINIMAL_SHORTENING_EXCLUSION_PASS
  toy=GF(101) rank=9 controls=6/6
RATE_HALF_MCA_RANK11_RANK8_MINIMAL_SHORTENING_EXCLUSION_AUDIT_PASS
  toy=GF(103) points=9 degree<=8 proof_pins=4/4
```

```text
result:                CLOSED one exact residual row
DAG delta:             +1 PROVED theorem node
critical status delta: none
rank-eleven boundary:  K'=10 no component target;
                       K'=11..22525 rank eight only;
                       K'=22526..37995 chronology only;
                       K'>=37996 no component target
delta-star movement:   none
compute:               two tiny finite-field interpolation checks under
                       RAMguard; no Modal run
next route action:     classify K'=11 hyperplane circuits and derive the
                       first all-55-shadow/global chronology coupling
```
