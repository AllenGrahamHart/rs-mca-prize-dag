# Cycle 351: MCA rank-11 K'=12 quotient-line payment (2026-08-15)

Cycle 350 closed `K'=11` using the one global hyperplane functional.  At
`K'=12`, the annihilator of the ten-dimensional correction space is
two-dimensional, so full-rank eleven-sets select points on a projective
quotient line.  Sparse circuit supports no longer coalesce to one label.

## Cycle pins

```text
our start:       635d38a2b
canonical prize: 6156c909c
upstream main:   93fba1be3
open upstream:   #1170 in the rank-eleven dense-locator packet
```

## Quotient-line sparse-circuit theorem

For support size `c`, restrict the degree-`c` Hankel catalecticant to the
quotient line.

- If one maximal minor is nonzero, its degree `c+1` bounds the labels.
- If every maximal minor vanishes, a full-rank `c`-row chart has a cofactor
  kernel map of parameter degree `e<=c`, with at most `c` bad parameters.
- After removing `g` fixed domain roots, root-fiber incidence bounds the
  visible labels by `floor(e(m-g)/(c-g))`.
- A constant kernel cannot give two labels on one full-rank eleven-set.

Support one has at most two labels by three-point Vandermonde independence.
Summing the independent support strata `c=1,...,5` at `m'=67484` gives the
per-record cap

```text
L_*=11868577829520852215896202871552159662636920.
```

This proof does not classify lines contained in secant varieties and does
not assume their support is fixed.

## Complete K'=12 payment

Rank-deficient component eleven-sets are retained.  The canonical-basis
globalizer has shortening excess two, so only corank one has a nonzero
extension factor.  Its exact absolute capacity is

```text
K_cap=C(1048588,9)*16295594
     =68823412552626461731638254358120971630939282959681665560.
```

For full-rank components, circuits of size at least six create at least 45
rank-nine shadows.  The common-core offset cap over `j=9,10,11` is

```text
C_*=9276963034268184,
```

giving high-circuit capacity

```text
H_cap=870681505337379475658181372289433062059140012353857046633355381.
```

At the minimum residual-record count, kernel plus high plus low capacity is

```text
873945204333998831582903951502910514268526233054054867526472861,
```

against full component-incidence demand

```text
901555241262544083284435178226046105523688795046262319915891531.
```

The exact gap is

```text
27610036928545251701531226723135591255162561992207452389418670.
```

The record coefficient is positive, so the contradiction persists for
every allowed larger record population.

```text
result:                PROVED K'=12 component-row closure
newly closed row:      12
remaining rank nine:  13..15528
new nodes:             2 PROVED
new premise:           none
compute:               exact integer arithmetic and small finite-field audit
next route action:     K'=13 projective quotient-plane sparse-label census,
                       with kernel capacity and core offsets j=9..12 retained
```
