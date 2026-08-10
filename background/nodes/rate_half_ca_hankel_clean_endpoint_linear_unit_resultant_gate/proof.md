# Proof

Only finitely many parameter points are forbidden: the supported set, the
root of `S`, the roots of `Q(-;x_0)`, and the roots of the leading
`X`-coefficient of `Q`. Choose parameter infinity outside their union. Then
all named finite factors remain affine, `Q(z;x_0)` has degree `m`, and
`q_inf=Q(infinity;X)` has `X`-degree `rho` and does not vanish at `x_0`.
This proves that the normalization in `(LUR2)` is available.

Regard all polynomials as elements of `Fbar(X)[z]`. Write the `m` roots of
`Q` as `alpha_i` in a splitting field. The standard resultant formula gives

```text
Res_z(Q,W)Res_z(Q,B)
 =q_inf^(w+b) product_i W(alpha_i)B(alpha_i).
```

The weld `(LUR1)` says `W(alpha_i)B(alpha_i)=X-x_0` for every `i`. This
proves `(LUR3)`. It also proves that both resultants are nonzero.

For every `x!=x_0` in the cyclic domain, clean saturation writes

```text
Q(z;x)=c_x product_(gamma in A_x)(z-gamma),
|A_x|=m.
```

Compare their product with the proved norm `product_x Q(z;x)=H^rho S`.
Every supported slope has exactly `rho` incident domain points, while the
exceptional point has the `m-1`-element incidence set defining `A_0`.
Cancelling the saturated factors proves `(LUR4)`.

Now specialize the two complement identities at `X=x_0`. Since the domain
is smooth, `P(x_0)=G'(x_0)!=0`. From

```text
Q V+P W=H
```

every one of the `m-1` distinct factors of `A_0` divides `W(z;x_0)`. Hence
the local intersection order of `Q` and `W` above `X=x_0` is at least
`m-1`.

The dual identity becomes

```text
Q(z;x_0)A(z;x_0)+H(z)B(z;x_0)=0.                    (1)
```

Because `H` is squarefree and `(LUR4)` holds, the quotient

```text
Q(z;x_0)/gcd(Q(z;x_0),H(z))
```

is the one linear factor `S`, including the case in which `S` repeats one
factor of `A_0`. Equation `(1)` therefore makes `S` divide `B(z;x_0)`.
The local intersection order of `Q` and `B` above `x_0` is at least one.

The choice `(LUR2)` makes `q_inf` a unit at `x_0`. Taking the
`(X-x_0)`-valuation in `(LUR3)` shows that the two resultant orders sum to
exactly `m`. The lower bounds `m-1` and `1` are therefore equalities, proving
`(LUR5)`.

If `b=0`, then `B` belongs to `Fbar[X]` and

```text
Res_z(Q,B)=B(X)^m.
```

Its `(X-x_0)`-valuation is divisible by `m>1`, contradicting the value one
in `(LUR5)`. Thus `b>=1`. The same argument with `W` would make its
resultant an `m`th power if `w=0`, contradicting the value `m-1`. This proves
`(LUR7)`.

If `K=0`, the polynomial identity `(LUR1)` would say `WB=X-x_0`. Its left
side has positive parameter degree `w+b`, while its right side has degree
zero. Hence `K!=0`. Equality of the highest parameter degrees in `(LUR1)`
then gives

```text
w+b=m+deg_z K,
```

which proves `(LUR8)`.

Finally `Fbar[X]` is a unique factorization domain and
`gcd(q_inf,X-x_0)=1`. Divide the two resultants by their exact powers from
`(LUR5)` and compare with `(LUR3)`. This gives `(LUR6)`. QED.
