# Budget-three antipodal Möbius weld

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:** `rate_half_list_budget_three_fiber_four_antipodal_descent`

Retain the antipodal descent with `s>=2` and put `r=s-1`. Thus the four
monic degree-`r` pairwise-coprime polynomials `G_i` span a two-dimensional
base-field space and satisfy

```text
sum_i lambda_i G_i=0,
sum_i lambda_i a_i G_i=0,       product_i lambda_i!=0.   (AMW1)
```

There are independent polynomials `U,V in F[Y]`, with `U` monic of degree
`r` and `deg V<=r-1`, and four distinct scalars `c_i in F` such that

```text
G_i=U+c_iV.                                             (AMW2)
```

The paired points `(a_i,c_i)` lie on one fractional-linear graph: there is a
unique `T in PGL_2(F)` with

```text
c_i=T(a_i)       for all i.                             (AMW3)
```

Equivalently, after one invertible base-field change of the pencil, there are
independent `R,S in F[Y]` of degrees at most `r` and nonzero scalars `mu_i`
such that

```text
G_i=mu_i(R+a_iS).                                       (AMW4)
```

Consequently the product identity from the descent is the quartic norm
equation

```text
product_i(R+a_iS)
 =kappa (Y^d-1)/product_i(Y-a_i^2),       kappa!=0.      (AMW5)
```

At the prize maximum, `deg R,deg S<=2^37-1` and `d=2^39`. Thus the explicit
antipodal residual is a single base-field-normalized Möbius-welded quartic
norm equation. This theorem does not exclude solutions of `(AMW5)`.
