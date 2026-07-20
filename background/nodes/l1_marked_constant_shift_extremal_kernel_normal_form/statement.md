# L1 marked constant-shift extremal kernel normal form

- **status:** PROVED
- **role:** classify the upper endpoint `T=2m` of the marked petal window
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Use the marked constant-shift setup with a monic degree-`ell` polynomial
`P`, exactly `t=2m` distinct labels `a_i`, and

```text
P-a_i=S_iV_i,       J=product_i V_i,       v=deg J,
deg F=d,       deg W<=d,       gcd(F,W)=1,
S_i | W-c_iF.
```

Assume

```text
m>=1,       m ell<d,       d+v<(m+1)ell.            (EK1)
```

Put `F'=JF`, `W'=JW`, and form the `2m` by `2(m+1)` matrix with rows

```text
(-c_i,-c_i a_i,...,-c_i a_i^m,1,a_i,...,a_i^m).    (EK2)
```

Then `(EK2)` has rank exactly `2m` and a two-dimensional kernel. For every
kernel basis represented by polynomial pairs

```text
q_0=(A_0(Z),B_0(Z)),       q_1=(A_1(Z),B_1(Z)),
deg A_j,deg B_j<=m,
```

there is a scalar `kappa!=0` such that

```text
A_0B_1-A_1B_0=kappa Q,       Q(Z)=product_i(Z-a_i). (EK3)
```

There are unique linearly independent `H_0,H_1 in K[X]`, each of degree
below `ell`, for which

```text
[F']   [A_0(P) A_1(P)] [H_0]
[W'] = [B_0(P) B_1(P)] [H_1].                         (EK4)
```

Moreover `gcd(H_0,H_1)` divides `J`, and the adjugate identity is

```text
[ B_1(P) -A_1(P)] [F']             [H_0]
[-B_0(P)  A_0(P)] [W']
  =kappa Q(P)                      [H_1].             (EK5)
```

Thus the endpoint is an exact two-generator determinant-`Q` pencil, not an
unstructured partial-petal family.

## Sharpness

The endpoint is nonempty in every strip. Let a field contain `2m` distinct
labels, put

```text
U(Z)=product_(i<=m)(Z-a_i),
V(Z)=product_(i>m)(Z-a_i),
```

and adjoin a transcendental `lambda`. For any monic `P` of degree `ell` and
`1<=c<ell`,

```text
F=1+lambda X^cV(P),       W=U(P),       d=m ell+c       (EK6)
```

has `gcd(F,W)=1` and satisfies all `2m` full-petal congruences: use value
zero on roots of `U` and value `U(a_i)` on roots of `V`. After an algebraic
field extension the locators may all be split. Hence `2m+1` in the
multistrip exclusion cannot be replaced by `2m`.

## Scope

This theorem does not count determinant-`Q` pencils, assign `(EK6)` to a
natural-scale profile owner, or classify the lower endpoint `T<2m`.

The proved `l1_marked_constant_shift_forney_window_normal_form` now supplies
that lower-endpoint module classification; this node remains the explicit
two-generator endpoint and sharpness audit.
