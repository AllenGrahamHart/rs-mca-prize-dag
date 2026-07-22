# L1 official first-checkpoint split-pencil reduction

- **status:** PROVED
- **role:** classify the minimum-width coarse collisions across the first
  checkpoint band and close its low-perturbation deep subband
- **consumer:** `l1_mixed_petal_amplification`

## Minimum-width classification

Let the official smooth domain `H` be a multiplicative coset of size `n` in
characteristic `p`. Use

```text
p>=3583,       11n<=256p.                            (FSP1)
```

Fix a coarse p-free prefix depth

```text
p<=d<=2p-2.                                          (FSP2)
```

If two fiber members have the minimum tame tail width `t=p`, write their
disjoint tail locators as `F_X,F_Y`. Then there are `b,c in F`, `c!=0`, and
a polynomial `Q` such that

```text
F_X(Z)=Z^p+Q(Z)+b,
F_Y(Z)=Z^p+Q(Z)+b+c,
deg Q<=2p-d-1.                                       (FSP3)
```

Thus every minimum-width collision in the first-checkpoint band is exactly a
pair of distinct fully `H`-split fibers of one low-degree perturbation of the
Frobenius map. Conversely, any such disjoint split pair satisfies the coarse
p-free moment equalities through depth `d`.

## Deep-band exclusion

Put

```text
r_d=2p-d-1,
r_*(p,n)=floor((p(p-1)-1)/(n-1)).                    (FSP4)
```

Absorb the constant term of `Q` into the two fiber values and choose the
nonzero value `beta`. For its `p`-point fiber `X_beta` and every nonidentity
`lambda` in the order-`n` subgroup underlying `H`,

```text
|X_beta intersect lambda X_beta|<=r_d.               (FSP5)
```

Consequently

```text
|X_beta/X_beta|
 >=1+ceil((p^2-p)/r_d).                               (FSP6)
```

If `r_d<=r_*(p,n)`, the right side is at least `n+1`, impossible because the
ratio set lies in the order-`n` smooth subgroup. Therefore

```text
d>=2p-1-r_*(p,n)  =>  t>=p+1.                       (FSP7)
```

The official uniform arithmetic gives

```text
r_*(p,n)>=floor(11(p-1)/256),                        (FSP7a)
```

so the final `floor(11(p-1)/256)` depths are closed on every row even before
using its exact `n`.

## Terminal stratum exclusion

At `d=2p-2`, equation `(FSP3)` has `deg Q<=1`. Squarefreeness forces the
linear coefficient to be nonzero, so each tail is an affine `F_p`-line.
No affine `F_p`-line lies in `H`: if `x+lambda F_p subset H`, then after
scaling `c=x/lambda` is outside `F_p`, and

```text
|(c+F_p)/(c+F_p)|=p^2-p+1.                           (FSP8)
```

This ratio set lies in the order-`n` subgroup underlying the coset, while

```text
p^2-p+1>256p/11>=n.                                  (FSP9)
```

Therefore

```text
d=2p-2  =>  t>=p+1.                                 (FSP10)
```

## Scope

The final `r_*(p,n)` depths of each first-checkpoint band have no
minimum-width collision; uniformly, this includes at least
`floor(11(p-1)/256)` depths. Below that row-sharp closed subband, the live
`t=p` object is narrowed to the split-pencil census `(FSP3)` with perturbation
degree greater than `r_*(p,n)`; this theorem does not bound that census,
higher tail widths, or L1. The affine-line proof is an independent structural
check of the terminal endpoint.
