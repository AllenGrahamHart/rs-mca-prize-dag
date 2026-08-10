# General t-petal anchor determinant coordinate

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Use the pair slice `V`, degree parameters, and saturated monic anchor `(F,W)`
of `l1_fpc5_tpetal_saturated_slice_dimension`. Let `M` be the complete monic
chart

```text
M={(G,B) in V: G is monic of degree d}.
```

For `(G,B) in M`, define

```text
H=(FB-GW)/Lambda.                                     (AC1)
```

With `K[X]_(<=-1)={0}` when `e=0`, the map

```text
M -> K[X]_(<=e-1),       (G,B) -> H                  (AC2)
```

is an affine bijection sending the anchor to zero. Thus `H` determines the
complete pair `(G,B)` before splitness, primitivity, exactness, and owner
filters are imposed.

If the anchor locator `F` is squarefree, then every distinct primitive exact
member satisfies

```text
H!=0,       gcd(H,F)=gcd(G,F),                        (AC3)
```

with monic gcds. In particular, the common-defect owner is one gcd stratum
of a single degree-at-most-`e-1` affine coordinate body, and the pairwise
defect-overlap cap `deg gcd(G,F)<=e-1` follows immediately.

## Large-source consequence

Every nonempty full-petal FPC5 cell surviving `(PF6)` has this coordinate.
Relative to one exact anchor, its remaining fixed-cell count is exactly the
number of `H` for which the reconstructed locator `G_H` splits on the source
core and the reconstructed pair passes the primitive and exact guards.
Coefficient multiplicity, pair reconstruction, and fixed-owner ambiguity are
therefore closed at arbitrary `t`.

## Scope

The theorem does not bound how many `H` reconstruct split locators, how many
gcd strata occur, or how cells and first owners aggregate. It does not permit
an independent sum over the divisors of `F`.
