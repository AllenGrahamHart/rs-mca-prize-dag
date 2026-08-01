# Proof

For `(KB41A-1)--(KB41A-2)`, the two independent product minors and two
denominator-cleared q welds are the four polynomials printed by the
certificate.  Let their ideal be `I` and put

```text
Q=b^2+bc+c^2.
```

Exact deployed-field reduction gives

```text
(b-1)(b+1)(b-c)Q in I.                              (1)
```

All three prefactors are guards, hence `Q=0`.  Reduction modulo `I+(Q)`
then gives

```text
(br-c)(b+t^2)=0.                                    (2)
```

On `br=c`, saturation by `b` gives

```text
b=ir,       r^2+r+1=0,       t^2=c,
```

and `c=br=ir^2`, which is family A.

On `b+t^2=0`, saturate by the guards `b`, `b^2-1`, and `r-1`.  Exact
reduction gives

```text
br=-i,       bc=-1,       ib^2+b-i=0,
```

which is family B.  The quadratic implies `b^3=i`; the omitted linear factor
of `b^3-i` is `b+i`, and it would force `r=1`, already excluded.

Direct substitution of each family reduces all four defining polynomials to
zero modulo `i^2+1` and its displayed family polynomial.  One-variable gcd
checks show every label, product, target, and edge-sum guard is a unit in
both quotient algebras.

Finally, changing the sign of `B` swaps `AB+` with `AB-`; renormalizing the
first source root toggles their relative square-root sign.  Changing the sign
of `C` does the same for `AC+` and `AC-`.  These commuting changes cover all
four sign choices and preserve the matching orbit. QED.
