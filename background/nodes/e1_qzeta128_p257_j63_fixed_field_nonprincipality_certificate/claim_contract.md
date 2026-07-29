# Claim contract

## Exact object

In the fixed field

```text
E_63=Q(zeta_128-zeta_128^(-1)),
```

certify that the degree-one prime

```text
p_66=(257,zeta_128-zeta_128^(-1)-66)
```

is nonprincipal.

The monic degree-32 defining polynomial `f_63` is pinned in `statement.md`.
It has 32 distinct roots modulo 257, including 66, as replayed by
`verify.py`.

## Required certificate

An unconditional nonzero ideal-class coordinate, a nontrivial Artin symbol
in a certified unramified abelian extension, an exact obstruction to the
norm equation, or another proof-producing principality test. A complete
certified class-group calculation is acceptable but not required.

## Equivalence to the original test

The ideals `q_1=(257,zeta-9)` and `q_63=(257,zeta-57)` contract to `p_66`
because

```text
9-9^(-1)=57-57^(-1)=66 mod 257.
```

Their product is `p_66 O_(Q(zeta_128))`. The cyclic degree-32 field `E_63`
is ramified over `Q` only at 2 and infinity; the ambiguous class-number
formula gives a trivial ambiguous class group and hence odd class number.
Extension to the quadratic field is therefore injective on ideal classes.
Thus `p_66` is nonprincipal if and only if `q_1q_63` is nonprincipal.

## Nonclaims

- The predicted 21121-primary coordinate is evidence, not a certificate.
- The order of the relevant class-group component alone does not locate
  `p_66` in that component.
- A GRH-only or `bnfcertify(B,1)`-only coordinate is insufficient.
