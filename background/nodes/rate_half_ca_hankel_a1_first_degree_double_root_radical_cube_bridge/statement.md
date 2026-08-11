# `A=1` first-degree double-root radical cube bridge

- **status:** PROVED
- **closure:** exact function-field cube identity for retained scalar branches
- **consumer:** `rate_half_band_crossing_location`

Retain a parameter-constant first-degree scalar branch and the cancelled
ambient identity

```text
s_F^3 G_L/H=R_a|_C.                                  (RCB1)
```

In the total quotient ring of `C`, with the standard affine trivializations
used in `(RCB1)`, put

```text
J=rad(R_a),       W=J/s_F.                           (RCB2)
```

Whenever every root multiplicity of `R_a` is at most three,

```text
W^3=(J^3/R_a)(G_L/H).                                (RCB3)
```

In particular, the retained double-root scalar branches satisfy the exact
cube identities

```text
core-free cubic:
  R_3=(X-x_s)(X-x_d)^2,
  ((X-x_s)(X-x_d)/s_F)^3
   =(X-x_s)^2(X-x_d) G_L/H;                          (RCB4)

core-one quadratic:
  R_2=(X-x_d)^2,
  ((X-x_d)/s_F)^3
   =(X-x_d) G_L/H.                                   (RCB5)
```

For the three no-ordinary cubic gap-one packets, the cube root in `(RCB4)`
is the unique section of `O_C(A)`. In the ordinary packet its divisor is
`A+B-R_0`, so it has the predicted pole at `R_0`. For the core-one
quadratic double-root packet at `u=4`, the cube root in `(RCB5)` is the
unique section of `O_C(B)` from `(QG44)--(QG45)`.

## Scope

The bridge does not exclude a packet. It reduces the double-root branches
to proving that the printed separated locator ratio cannot be a cube under
the Hankel/apolar realization constraints. It does not imply that `C` is a
separated pullback `f(X)=g(U:V)`, and in characteristic three it must not be
treated as an etale Kummer cover.
