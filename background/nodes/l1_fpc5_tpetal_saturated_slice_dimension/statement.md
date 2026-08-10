# General t-petal saturated-slice dimension theorem

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Let `K` be a field. Let `L_1,...,L_t` be pairwise coprime monic
polynomials, put

```text
Lambda=product_i L_i,       h=deg Lambda,
```

and fix labels `c_1,...,c_t` in `K`, not necessarily distinct. For an
integer `d` with

```text
d<h<=2d+1,       e=2d+1-h>=0,                         (SD1)
```

define the linear pair slice

```text
V={(G,B): deg G<=d, deg B<=d,
            L_i divides B-c_iG for every i}.          (SD2)
```

Assume `V` contains a saturated anchor `(F,W)` with

```text
F monic,       deg F=d,       gcd(F,W)=1.             (SD3)
```

Then

```text
dim_K V=e+1.                                           (SD4)
```

Moreover, projection to the locator coordinate is a linear isomorphism

```text
V -> V_F={G:(G,B) in V for some B},                   (SD5)
```

so `dim V_F=e+1`. The degree-`d` monic chart of `V_F` is a nonempty affine
`e`-flat. Every primitive exact contributor in the slice injects into the
split locators in that affine flat, with its numerator and exact guards
reconstructed uniquely.

The assumption that defect roots avoid petal roots is automatic for a
primitive member: if `L_i(x)=F(x)=0`, then `(SD2)` gives `W(x)=0`, contrary
to `gcd(F,W)=1`.

## Large-source specialization

For a nonempty full-petal FPC5 cell surviving `(PF6)`, take

```text
h=t ell,       e=2d+1-t ell=r+1.
```

The exact prefilter gives `r>=0`, hence `e>=1`, while the list threshold
gives `h>=d+ell-b>d`. An exact contributor supplies `(SD3)`. Therefore every
surviving nonempty fixed cell has an affine split-locator chart of dimension
exactly `e`; there is no remaining arbitrary-`t` slice-dimension gap.

## Scope

This theorem supplies a typed flat and removes pair-coefficient fibers. It
does not bound the number of split locators in the flat, aggregate cells or
owners, or prove the large-source payment. Without a saturated anchor the
upper bound can fail; without `h>d` the locator projection can have a
nontrivial numerator-only kernel.
