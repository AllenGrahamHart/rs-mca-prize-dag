# L1 official first-checkpoint split-pencil reduction

- **status:** PROVED
- **role:** classify the minimum-width coarse collisions across the first
  checkpoint band and close its terminal affine-line stratum
- **consumer:** `l1_mixed_petal_amplification`

## Minimum-width classification

Let the official smooth domain `H` be a multiplicative coset of size `n` in
characteristic `p`. Use

```text
p>=3583,       n<24p.                                (FSP1)
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

## Terminal stratum exclusion

At `d=2p-2`, equation `(FSP3)` has `deg Q<=1`. Squarefreeness forces the
linear coefficient to be nonzero, so each tail is an affine `F_p`-line.
No affine `F_p`-line lies in `H`: if `x+lambda F_p subset H`, then after
scaling `c=x/lambda` is outside `F_p`, and

```text
|(c+F_p)/(c+F_p)|=p^2-p+1.                           (FSP4)
```

This ratio set lies in the order-`n` subgroup underlying the coset, while

```text
p^2-p+1>24p>n.                                       (FSP5)
```

Therefore

```text
d=2p-2  =>  t>=p+1.                                 (FSP6)
```

## Scope

The terminal minimum-width stratum is closed. For `p<=d<2p-2`, the live
`t=p` object is narrowed to the split-pencil census `(FSP3)` with perturbation
degree at most `2p-d-1`; this theorem does not bound that census, higher tail
widths, or L1.
