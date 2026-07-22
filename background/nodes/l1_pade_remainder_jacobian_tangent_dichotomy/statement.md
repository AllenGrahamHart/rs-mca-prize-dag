# L1 Pade-remainder Jacobian and tangent dichotomy

- **status:** PROVED
- **role:** isolate all Pade-section rank collapse on the tangent resultant
- **consumer:** `l1_mixed_petal_amplification`

## Remainder map

Fix a received polynomial `U`, integers `k<a`, and a monic degree-`a`
polynomial

```text
L=Z^a+l_(a-1)Z^(a-1)+...+l_0.
```

Let `Rem_U(L)` be the degree-below-`a` remainder in the monic Euclidean
division

```text
U=LQ+P,       deg P<a.                               (JT1)
```

The full-locator Pade section is the zero locus of the `w=a-k` coefficients

```text
[Z^k]P,...,[Z^(a-1)]P.                              (JT2)
```

This is exactly `l1_full_locator_pade_section_all_cofactors` in ordinary
coefficient order.

## Differential

For a tangent direction `D` of degree below `a`, differentiation of `(JT1)`
gives

```text
d Rem_U|_L(D) = -(QD mod L).                         (JT3)
```

Consequently:

1. if `gcd(L,Q)=1`, multiplication by `Q` is an automorphism of
   `F[Z]/(L)`;
2. the full remainder map has Jacobian rank `a` at `L`;
3. the `w` Pade equations `(JT2)` have Jacobian rank exactly `w`;
4. the Pade section is a smooth local complete intersection of codimension
   `w` at that point.

Hence every rank-deficient point of the Pade section lies on

```text
Res(L,Q)=0,       equivalently gcd(L,Q)!=1.           (JT4)
```

The converse is not asserted: a tangent point may still have full rank after
projection to the high remainder coefficients.

## Exact-shell split

For a split locator `L|Omega`, exactness already requires
`gcd(Q,Omega/L)=1`.  Therefore every exact shell member belongs to exactly one
of two classes:

```text
primitive transverse: gcd(Q,Omega)=1;
tangent:              D=gcd(L,Q)!=1 and gcd(Q,Omega/L)=1. (JT5)
```

The tangent factor `D` is canonical and all its domain roots are agreement
roots.  Primitive transverse members lie on the smooth codimension-`w`
section.  No count of split points on that section, and no payment of the
tangent branch, is claimed.

## Sharpness witness

The tangent branch is genuine.  Over `F_17` on the order-eight domain, take a
degree-four split locator `L`, `k=1`, and a quadratic cofactor whose two roots
are roots of `L` and no complement roots.  The resulting exact shell point
has `deg gcd(L,Q)=2`; multiplication by `Q` modulo `L` has rank `2`, so the
three high-remainder equations have rank at most `2<3`.
