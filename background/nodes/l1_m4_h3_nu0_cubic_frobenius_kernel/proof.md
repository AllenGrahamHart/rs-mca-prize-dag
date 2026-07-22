# Proof - L1 m=4, h=3, nu=0 cubic Frobenius kernel

At `nu=0`, the Cartier identity and its two resonance constraints are

```text
(X^(p-4)R^3D)'=X^(p-5)R^2H,
[X^4](R^2H)=[X^(p+4)](R^2H)=0.                       (1)
```

The integrand has degree at most

```text
(p-5)+2p+h<=3p-2.
```

Its only possible degrees congruent to `-1 mod p` are `p-1` and `2p-1`.
After removing the shift `p-5`, their coefficients are exactly the two
vanishing coefficients in (1). Therefore coefficientwise integration is
possible. Setting every coefficient in degree divisible by `p` to zero gives
the unique `J` in `(CFK2)`, with `deg J<=3p-1`.

Put

```text
F=X^(p-4)R^3D,       G=X^(p-4)B_0.
```

The reduced triple gives

```text
F+G=X^(5p),       F'=J',       G'=-J'.                (2)
```

Thus `(F-J)'=0`. Over the perfect coefficient field there is a unique
polynomial `A` with

```text
F=A^p+J.                                              (3)
```

The polynomial `F` is monic of degree `5p`, while `J` has smaller degree,
so `A` is monic of degree five. Both `F` and `J` vanish at zero, hence
`A(0)=0`. Equation (2) now gives

```text
G+J=X^(5p)-A^p=(X^5-A)^p.                             (4)
```

Set `Q=X^5-A`. From the exact degree of `B_0`,

```text
deg G=(p-4)+(2p+4)=3p,       lc(G)=a.                 (5)
```

Since `deg J<3p`, equation (4) forces `Q` to have degree exactly three and
`lc(Q)^p=a`. Also `Q(0)=0`. This proves `(CFK3)` and `(CFK4)`; in
particular the degree-four and constant terms in `Q` vanish. Uniqueness
follows from the canonical `J` and injectivity of Frobenius.

Finally `R(0)`, `D(0)`, and `H(0)` are nonzero. The integrand in `(CFK2)`
starts with `R(0)^2H(0)X^(p-5)`, so

```text
[X^(p-4)]J=R(0)^2H(0)/(p-4)=-R(0)^2H(0)/4.           (6)
```

The least positive degree in `A^p` is at least `p`, whereas `p-4<p`.
Comparing degree `p-4` in (3) gives

```text
R(0)^3D(0)=-R(0)^2H(0)/4.
```

Cancellation proves `(CFK5)`.
