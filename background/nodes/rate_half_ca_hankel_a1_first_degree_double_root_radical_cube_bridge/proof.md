# Proof

All identities are taken in the total quotient ring of the reduced curve,
using the same affine representatives of the contact section and locator
ratios as in the cancelled ambient identity. Since `s_F` is nonzero on
every mixed component used by that identity, division by it is valid in the
total quotient ring.

Cube `(RCB2)` and substitute `(RCB1)`:

```text
W^3=J^3/s_F^3
   =J^3 (G_L/H)/R_a
   =(J^3/R_a)(G_L/H).                                (1)
```

If every residual-root multiplicity is at most three, `J^3/R_a` is a
polynomial with each root exponent complementary to its multiplicity modulo
three. This proves `(RCB3)`.

For `R_3=(X-x_s)(X-x_d)^2`, its radical is
`J=(X-x_s)(X-x_d)`, and

```text
J^3/R_3=(X-x_s)^2(X-x_d).                            (2)
```

Substitution into `(RCB3)` gives `(RCB4)`. For
`R_2=(X-x_d)^2`, one has `J=X-x_d` and `J^3/R_2=X-x_d`,
which gives `(RCB5)`.

It remains only to identify the cube roots already calculated by the local
normal forms. In the no-ordinary cubic packets,

```text
div(J/s_F)=V_s+V_d-div(s_F)=A.                       (3)
```

The degree-one pushforward calculation gives one section, so `(3)` is its
canonical generator. In the ordinary cubic packet the same subtraction is
`A+B-R_0`, exactly its signed Picard divisor.

In the core-one quadratic double-root packet,

```text
div((X-x_d)/s_F)=V_*-div(s_F)
 =(R_*+3B)-(R_*+2B)=B.                               (4)
```

The degree-two pushforward calculation again gives one section, so this is
its canonical generator. Equations `(3),(4)` prove all section
identifications. QED.
