# Proof - L1 m=4, h=3, nu=3 quadratic Frobenius kernel

At `nu=3`, the Cartier node gives constant nonzero `H=c`, zero radical
defect, and

```text
(X^5U^3D)'=cX^4U^2.                                   (1)
```

The original reduced triple is `(QFK1)`. Put

```text
F=X^5U^3D,       G=X^5B_0.
```

Then

```text
F+G=X^(4p),       F'=cX^4U^2,       G'=-cX^4U^2.       (2)
```

The integrand in (1) has degree `2p-2`. A polynomial has an antiderivative
in characteristic `p` exactly when its coefficients in degrees `jp-1`
vanish. The only possible such degree here is `p-1`, and its coefficient is
`c[X^(p-5)]U^2=0` by the Cartier constraint. Coefficientwise integration,
with every `X^(jp)` coefficient set to zero, gives the unique `J` in
`(QFK2)` and `deg J<=2p-1`.

Now `(F-J)'=0`. Over the perfect coefficient field, there is a unique
polynomial `A` such that

```text
F-J=A^p.                                                (3)
```

Since `F` is monic of degree `4p`, `J` has smaller degree, and both vanish
at zero, `A` is monic of degree four with `A(0)=0`. Equation (2) gives

```text
G+J=X^(4p)-A^p=(X^4-A)^p.                              (4)
```

Put `Q=X^4-A`. The numerator defining `B_0` is
`(aR+b)D+alpha`; because `a!=0`, it has degree `2p+4` and leading
coefficient `a`. Division by `X^9` gives

```text
deg B_0=2p-5,       lc(B_0)=a,
deg G=2p,           lc(G)=a.                           (5)
```

As `deg J<2p`, equation (4) forces `Q` to have degree exactly two and
`lc(Q)^p=a`. Also `Q(0)=0`, so `Q=q_2X^2+q_1X` with the properties in
`(QFK3)`. Equations (3)--(4) are exactly `(QFK4)`. Uniqueness follows from
the canonical choice of `J` and injectivity of Frobenius over the field.

Finally `U(0)`, `D(0)`, and `c` are nonzero, so the integrand begins with
`cU(0)^2X^4`. Therefore

```text
[X^5]J=cU(0)^2/5.                                      (6)
```

Both `A` and `Q` vanish at zero, and the official primes exceed five, so
their `p`th powers have no degree-five term. The degree-five coefficient of
`F=X^5U^3D` is `U(0)^3D(0)`. Comparing with (3) gives `(QFK5)`.
