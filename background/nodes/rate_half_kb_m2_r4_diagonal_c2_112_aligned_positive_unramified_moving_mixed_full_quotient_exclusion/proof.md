# Proof

After solving the exact relative scale and removing only the printed open
factors, the four mixed-allocation equations descend through
`trace=b+b^-1` to quadratics. Let their `4 x 3` coefficient matrix be `M`.
A common trace root forces all maximal minors of `M` to vanish and the
first-two-row kernel to lie on the Veronese conic.

## Projection support

Factor the three star projections of the four residual minors over the
deployed prime. Their common nonopen support is

```text
4p+5t+4
```

and one irreducible 91-term polynomial of bidegree `(12,12)`, with digest

```text
9b318c946825ce375fc493b90aa2699b8aebf6868bf552e9a1e8419a66d134b5.
```

On the linear component, the gcd of all minors and the conic is
`t^4(t+1)(t+4)(w-1)`, hence forbidden.

After common/open removal, projections `01`, `02`, and `03` have `3`, `4`,
and `1` residual factors. The exact twelve-way screen computes both
`p`-resultants for every `3 x 4 x 1` choice and takes their `t` gcd. Two
choices are empty; the other ten factor linearly. Endpoint replay deduplicates
them to six `(p,t)` values, and every value kills

```text
p(p-1)(p-t+1)(p+t+1)(p+2t+4)
(4p+2t+1)(5p+4t+5)(t^2-4p).
```

Thus no admissible off-common point remains.

## Direct component

The resultant of residual minor 0 and the residual kernel conic is not
divisible by the degree-12 component. Its component norm has degree 1224 in
`t`, digest

```text
13a295c5219450a00c588cc9661863022d03ddca67429eb9626d398fe4515dae,
```

and 38 irreducible factors. For every factor, instantiate its exact finite
field, recover every `p` factor, gcd all four residual minors and the conic
in `w`, and replay the four original trace equations and the full forbidden
product. Exactly four q-slice points survive. Their irreducible `t` degrees
and factor indices are

```text
(3,3), (5,3), (10,7), (12,7).
```

An element of degree `d` over `F_p` lies in `F_(p^6)` only if `d` divides
`6`. Hence factors 10 and 12 cannot occur in the deployed field.

## Full quotient rejection

For either degree-3 point the moving quadratic
`B^2-trace*B+1` splits over `F_(p^3)`, giving the two reciprocal orientations
`b,b^-1`. Reconstruct the positive source form

```text
H(T,X)=U(T,X^2)+X V(T,X^2),
G(T,W)=U(T,W)^2-WV(T,W)^2
```

with the pinned exact relative scale. In the aligned `(1,1,2)` cell, if
`z` is the internal common-`K` label, then

```text
J=J_0 union Root(q),
I={w,w^-1,z,z^-1,c^-1,d^-1},
K=I minus {w^-1}.
```

Thus `K_5` and `R_7` are explicit. Multiplying each identity `(KBQ2-2)` by
its source-deck conjugate gives the necessary norm identities

```text
Res_T(P_J,G) ~ K_5^4 q^2,                 (1)
q^2 Res_T(P_I,G) ~ R_7^4.                 (2)
```

Each six-label resultant is evaluated as the product of three exact
quadratic resultants. As a reconstruction control, all four orientations
first reproduce `(KBQS-1)`. Coefficientwise comparison then rejects all
four orientations in both `(1)` and `(2)`. Therefore no direct-component
point in `F_(p^6)` passes the full quotient system.

The open factors, linear component, direct component, and every residual
projection intersection exhaust the projection factorization, completing
the claimed deployed-field exclusion.
