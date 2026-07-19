# Proof

Because `P_i` divides `H_i(X^4)`, either root `r` of `P_i` satisfies

```text
0=H_i(r^4)=H_i(a_i^2)=H_i(b_i).
```

Thus `H_i(Y)=(Y-b_i)G_i(Y)` for a monic degree-`s-1` polynomial `G_i`.
The elementary identity

```text
X^4-b_i=(X^2-a_i)(X^2+a_i)
```

then gives `(F4A4)`.

Substitute `(F4A4)` into the locator relation. The result is

```text
sum_i lambda_i (X^2+a_i)G_i(Y)=0.                       (1)
```

The elements `1,X^2` are linearly independent over `F(Y)`, so their two
coefficients in `(1)` vanish. This is exactly `(F4A6)`.

The first identity in `(F4A3)` and `(F4A2)` give

```text
product_i H_i(X^4)=X^(4d)-1.
```

Both sides are polynomials in `Y=X^4`, hence

```text
product_i H_i(Y)=Y^d-1.
```

Dividing by the four factors from `(F4A4)` proves `(F4A5)`. Since `Y^d-1`
is squarefree in the official odd characteristic, the `b_i` are distinct
order-`d` subgroup elements. If two `G_i` shared a nonconstant factor
`C(Y)`, then `C(X^4)` would divide two block locators in `(F4A4)`, contrary
to their pairwise coprimality. Thus the `G_i` are pairwise coprime.

The two coefficient vectors in `(F4A6)` are independent. Indeed, if
`(lambda_i a_i)` were a scalar multiple of `(lambda_i)`, nonvanishing of
every `lambda_i` would make all `a_i` equal, contradicting pairwise
coprimality of the `P_i`. Hence `(F4A6)` gives two independent relations and
the span in `(F4A7)` has dimension at most two. For `s>=2`, every `G_i` is
nonconstant. A one-dimensional span would make the monic `G_i` equal, again
contradicting pairwise coprimality. This proves `(F4A7)`.

Conversely, multiply the product identity in `(F4A5)` by the factorizations
`X^4-b_i=(X^2-a_i)P_i(X)` to recover the first equation in `(F4A3)`.
Combining the two equations in `(F4A6)` recovers `(1)`, which is the locator
relation after `(F4A4)`. QED.
