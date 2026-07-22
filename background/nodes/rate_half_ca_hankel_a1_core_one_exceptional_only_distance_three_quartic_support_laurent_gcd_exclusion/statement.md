# `A=1` distance-three quartic support Laurent gcd exclusion

- **status:** PROVED
- **closure:** proof using the Corvaja--Zannier positive-characteristic gcd theorem
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_four_reducible_deck_router`

The absolutely irreducible Laurent-end branch

```text
XY[X^2+XY+Y^2+a(X+Y)+b]-d=0,       d!=0,            (QLG1)
```

contains fewer than `2(e-148)` points of `mu_N x mu_N` on the official row

```text
N=2^41,       e=2^38-1,       p>2^167.              (QLG2)
```

Consequently it cannot contain the ordered orientations of the required
`e-148` matched fibers and is empty as a quartic support survivor.

After this exclusion, simultaneous deficiency of every support
pair-crossing matrix leaves only:

1. one fixed antipodal or constant-product involution containing at least
   `e-40` matched pairs; or
2. a degree-four cyclic/dihedral pullback
   `F(X^2)`, `F(X^4)`, or `F(X+c/X)`.

No absolutely irreducible non-pullback quartic geometry remains.
