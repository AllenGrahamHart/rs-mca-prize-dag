# Proof

The nonidentity `n`th roots are the roots of

```text
(Y^n-1)/(Y-1).
```

Substitute `Y=1-X` and account for the `d=n-1` sign changes. Since `n` is
even, this gives

```text
product_(a=1)^(n-1)(X-(1-zeta^a))=((1-X)^n-1)/X,
```

which proves `(GRC1)`. In particular `F_n` is monic of degree `d` and has
constant term `-n`. Hence

```text
product_a c_a=n.                                  (1)
```

For any monic polynomial `F` with roots `r_a`, the evaluation definition of
the resultant gives

```text
Res_X(F(X),G(X))=product_a G(r_a).                (2)
```

Now

```text
X^d F_n(T/X)=product_b(T-c_b X).
```

Applying `(2)` at `X=c_a` proves

```text
Res_X(F_n(X),X^dF_n(T/X))
 =product_(a,b)(T-c_a c_b),
```

which is `(GRC2)`.

Likewise,

```text
Res_X(F_n(X),F_n(TX))
 =product_(a,b)(Tc_a-c_b).                         (3)
```

The diagonal factors in `(3)` are

```text
product_a(c_aT-c_a)=(T-1)^d product_a c_a
                    =n(T-1)^d
```

by `(1)`. Removing exactly those factors proves `(GRC3)`. The quotient is in
`Z[T]` independently: its product expression is an algebraic-integer
polynomial fixed by every odd Galois dilation, so all coefficients are
rational algebraic integers.

For `(GRC4)`, use the root factorization of `F_n` to write

```text
(CX)^d F_n((D+CU)/(CX))
 =product_b(D+CU-CXc_b).                           (4)
```

This also proves directly that the apparent rational expression is a
polynomial in `O[X,U]`. Applying `(2)` to `(4)` gives

```text
Res_X(F_n,H_(C,D))
 =product_(a,b)(D+CU-Cc_a c_b)
 =C^N product_(a,b)(D/C+U-c_a c_b)
 =C^N Pcal_n(D/C+U).
```

This is exactly the cleared polynomial `G_uv` used by the derivative-ideal
packet. Equality in `O[U]` remains equality after reduction modulo `U^19`,
so its first nineteen coefficients are obtained from the truncated
resultant. No complexity assertion is used. QED.
