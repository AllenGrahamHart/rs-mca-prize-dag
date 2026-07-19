# Budget-three antipodal primitive quotient gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:** `rate_half_list_budget_three_antipodal_mobius_weld`

Retain the antipodal Mobius-weld data with dyadic `d=4s`, `s>=4`, and
`r=s-1`. Thus

```text
G_i=mu_i(R+a_iS),
product_i G_i=(Y^d-1)/product_i(Y-a_i^2),
deg G_i=r,
```

where the four `G_i` are pairwise coprime. Put

```text
f=-R/S in F(Y).
```

Then `gcd(R,S)=1` and

```text
deg f=r=s-1.                                             (APQ1)
```

Consequently the welded map is primitive with respect to every nontrivial
dyadic cyclic or dihedral quotient of the order-`d` subgroup. More precisely,
even after a fractional-linear change of target coordinate, it has neither
form

```text
g(Y^m),                 m>1, m|d,
g(Y^m+Y^(-m)),          m>=1,                            (APQ2)
```

for a nonconstant rational `g`.

The direct index-four coset partition is impossible as well. Let

```text
H_i=(Y-b_i)G_i,        b_i=a_i^2.
```

The four root sets of the `H_i` cannot be the four cosets of the order-`s`
subgroup of `mu_d`. Hence the official antipodal residual is not the standard
power-map partition with one deleted point in each fiber.

This theorem does not exclude a primitive, nonperiodic solution of the
quartic norm equation.
