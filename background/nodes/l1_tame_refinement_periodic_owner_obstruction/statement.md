# L1 tame-refinement periodic-owner obstruction

- **status:** PROVED
- **role:** prevent an invalid transport from fixed-petal polynomial
  refinements to the exact multiplicative-periodic owner
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Exact witness

Work in `F_17` on the multiplicative domain

```text
H=F_17^*,       n=16,       k=8,       sigma=5,       ell=6.
```

Put

```text
P(X)=X^2+3X,
T={1,2,3,11,12,13},
C={7,8,9,10,14,15,16},
R={4,5,6},       A=C union T=H\R.                     (PO1)
```

The petal `T` is the disjoint union of three complete degree-two fibers:

```text
P^(-1)(4) ={1,13},
P^(-1)(10)={2,12},
P^(-1)(1) ={3,11}.                                    (PO2)
```

Thus this is a tame fixed-petal refinement: `ell/deg(P)=3` and
`17` does not divide `3`.

Define the received word on `H` by

```text
U(x)=0 for x in A,       U(x)=1 for x in R.            (PO3)
```

The zero codeword has degree below `k` and exact agreement set `A`, of size
`13=k+sigma`. Nevertheless

```text
Stab_H(A)={1}.                                         (PO4)
```

Hence this contributor is not owned by `pma_exact_periodic_owner`, and the
degree-two partition is not the intrinsic antipodal quotient partition.

## Consequence

A whole source petal being a union of complete fibers of a tame polynomial
does not force the contributor's complete agreement support to have a
nontrivial multiplicative stabilizer. The tame map census therefore cannot be
composed automatically with the existing exact-periodic or cyclic quotient-
descent ledgers. Small-scale tame refinements require a general polynomial-
pullback owner or a collective payment over aperiodic supports.

This `n=16` witness is a route fence, not an official-row counterexample and
not a falsifier of the L1 target.
