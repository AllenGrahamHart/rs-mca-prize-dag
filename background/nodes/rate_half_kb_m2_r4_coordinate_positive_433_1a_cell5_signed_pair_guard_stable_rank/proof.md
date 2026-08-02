# Proof

Work over `K=F_p(t)` at `p=2130706433`.  Substitute the proved chart-2
formulas for `r,c` into the reciprocal primitive and the first two
target-free signed rows.  Eliminating the reconstructed target root and
writing `xj=zj^2` gives exactly `P,g3,h` from the statement.  The only
division in this reduction is by the retained guard `d0*d1`.

## Finite quotient

Groebner.jl, using exact `K` arithmetic, certifies the exported 18-element
basis as a Groebner basis.  Its standard monomials form a 64-element
quotient basis.  The canonical basis-text hash is

```text
8fd93095924f616770e49257ae45f255a8859f43c4f87100859cadfc8cc77ed6.
```

Thus `A` is finite-dimensional of dimension 64.  Reducing
`g^e` times every standard monomial gives the multiplication matrices
`M^e`; normal-form composition agrees with multiplication in `A`.

## Exact rank of `M^2`

The power-two normal-form packet has canonical coefficient hash

```text
cb2a07bc8e8d70f25220d89133b02750d05db59c1105856d13bc33c758ba9c11
```

and packet hash

```text
c10acad4d6e6971fb978498f49a1a8306326b81f23c6cdf3c06cb318ba6f61d3.
```

Let `U` be its first 24 columns.  Exact rational-function solves give a
24-by-64 matrix `C`, beginning with the identity, such that

```text
M^2 = U*C.                                       (1)
```

Every one of the 40 nonpivot columns was checked against all 64 rows.
Hence `rank_K(M^2)<=24`.

At `t=2` every packet denominator is nonzero.  The top-left 24-by-24 minor
specializes to determinant

```text
109382047 != 0 mod p.
```

A nonzero specialization cannot arise from the zero rational function, so
the generic minor is nonzero and `rank_K(M^2)>=24`.  This proves
`rank_K(M^2)=24`.

The primary Julia/Nemo calculation checks (1) directly.  The independent
checker first binds the packet to the exported basis-file hash, recomputes
the canonical 18-polynomial hash, checks the exact leading-monomial ledger,
and independently counts its 64 standard monomials.  It then clears one
denominator per matrix row and coordinate column.  Every resulting residual
has degree at most 380.  It evaluates those polynomial identities at all 512
powers of a primitive 512th root in `F_p`; since `512 | p-1` and a nonzero
polynomial of degree below 512 cannot vanish at 512 distinct points, this is
a deterministic exact replay.  The cleared packet hash is

```text
664ffeb8b6093302a6b5cd795d59a09363e1d5beaeb6bd12c4fe48a4d9e38c82.
```

## Stabilization and localization

The same independent replay specializes `M` at `t=2,3,4,5`, verifies that
the direct `M^2` packet equals the square of `M`, and obtains

```text
(rank M, rank M^2, rank M^3)=(32,24,24)
```

at every sample.  In particular the regular specialization at `t=2`
shows `rank_K(M^3)>=24`, while
`rank_K(M^3)<=rank_K(M^2)=24`.  Thus the two generic ranks are equal.

For a linear endomorphism of a finite-dimensional vector space, equality
of two consecutive image dimensions makes the restriction to the stable
image bijective, so all later images have dimension 24.  Localizing the
finite algebra at `g` kills precisely the `g`-power torsion and identifies
with this stable image.  Therefore `dim_K A[g^-1]=24`, proving (KBGS-1).
QED.
