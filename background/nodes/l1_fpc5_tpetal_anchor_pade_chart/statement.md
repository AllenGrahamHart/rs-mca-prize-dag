# General t-petal anchor Pade chart

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Use the pair slice, degree parameters, and saturated monic anchor `(F,W)`
of `l1_fpc5_tpetal_anchor_coordinate`. Put

```text
Lambda=product_i L_i,       e=2d+1-deg Lambda,
I=W^(-1) mod F,             deg I<d.
```

For every `H` with `deg H<=e-1`, define

```text
R_H=rem_F(-Lambda H I),       G_H=F+R_H,
B_H=(G_H W+Lambda H)/F.                              (PC1)
```

Then the division defining `B_H` is exact,

```text
deg G_H=d,       G_H monic,       deg B_H<=d,        (PC2)
```

and `(G_H,B_H)` is the unique point of the complete monic pair chart with

```text
(F B_H-G_H W)/Lambda=H.                              (PC3)
```

Thus `(PC1)` is the explicit inverse of the anchor coordinate. In
particular, the complete locator flat is the remainder graph

```text
{F+rem_F(-Lambda H I): deg H<=e-1}.                  (PC4)
```

Assume now that `F` and `G_H` are squarefree split locators whose roots
avoid `Z(Lambda)`. At a root `x` of `G_H`, the primitive guard is exactly

```text
F(x)!=0:       B_H(x)!=0 iff H(x)!=0;
F(x)=0:        B_H(x)!=0 iff
               G_H'(x)W(x)+Lambda(x)H'(x)!=0.       (PC5)
```

Consequently `gcd(G_H,B_H)=1` is equivalent to the conjunction of the
corresponding inequalities in `(PC5)` over `Z(G_H)`. On the common-root
stratum, `H(x)=0` automatically.

## Large-source consequence

Every nonempty full-petal FPC5 cell surviving `(PF6)` is therefore an
explicit primitive remainder cell: its exact contributors are precisely the
coordinates `H` for which the locator in `(PC4)` splits on the source core
and the reconstructed pair passes `(PC5)` and the remaining exact guards.
No coefficient fiber or implicit locator reconstruction remains.

## Scope

This theorem does not bound the number of split remainders in `(PC4)`, pay
the primitive cell, or aggregate sources, touched sets, defects, or owners.
It does not assert that a generic `H` reconstructs a split locator.
