# `A=1` distance-three bounded-tail dihedral row-codegree

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_pair_lagrange_normal_form`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_laurent_gcd_exclusion`

Let `tau` be either `X |-> -X` or `X |-> c/X`, with `c in mu_N`. Suppose
`e-t` exceptional pairs are exact nonfixed `tau`-orbits and the remaining
`t` pair locators are arbitrary. For every nonfixed outside `tau`-orbit
`{x,y}` disjoint from the exceptional and boundary supports, the two
normalized row polynomials

```text
q_x(z)=Q(z;x)/A(x),       q_y(z)=Q(z;y)/A(y)         (QBT1)
```

have at most `t` common external roots, except at at most one outside orbit
where `q_x=q_y` identically.

More explicitly, put `alpha_i=lambda_i/xi_i`, let `G` and `T` denote the
good and tail pair indices, and define

```text
I_G(z)=product_(i in G)(z-xi_i).                     (QBT2)
```

For the antipodal case use

```text
beta_x=B(x),       beta_y=B(y),
Dhat_j(y)=D_j(y).                                   (QBT3)
```

For the constant-product case, where `y=c/x`, use

```text
beta_x=B(x),       beta_y=x^2B(y)/c,
Dhat_j(y)=x^2D_j(y)/c.                              (QBT4)
```

Then every common external root is a root of

```text
H_(x,y)(z)=
 (beta_x-beta_y)Phi(z)
 +z beta_x beta_y sum_(j in T) alpha_j L_j(z)
      [1/Dhat_j(y)-1/D_j(x)].                       (QBT5)
```

The exact divisibility and degree bound are

```text
H_(x,y)=I_G h_(x,y),       deg h_(x,y)<=t.           (QBT6)
```

If `H_(x,y)` is zero, the normalized rows are identical. Such an orbit must
satisfy

```text
x^2=-sigma_2                                      (antipodal),
x+c/x=sigma_1-sigma_3/c                    (constant product), (QBT7)
```

so there is at most one nonfixed identical-row orbit.

For the official bounded-tail degree-two branch, `t<=40`; every
nonexceptional involution-orbit therefore has row codegree at most forty.
This theorem does not yet extend the quotient trace-collision exclusion to
the resulting degree-`e+t` complements.
