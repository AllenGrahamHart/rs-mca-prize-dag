# Proof

For a valid solution, reverse the four monic pencil factors and absorb the
nonzero leading coefficient of `V` into the centered outer parameters. If
`Cbar=C/C(0)` and `w_i=C(0)c_i`, then

```text
product_i(B+w_i z^h Cbar)=Q.                           (1)
```

The `w_i` are centered, so writing their elementary symmetric functions as
`alpha,beta,gamma` expands `(1)` to

```text
Q=B^4+alpha z^(2h)B^2Cbar^2
       +beta z^(3h)BCbar^3+gamma z^(4h)Cbar^4.         (2)
```

The generic coefficient `alpha` is nonzero. Subtracting `B^4` in `(2)` proves
that `R` has exact order `2h`, and division by `z^(2h)` gives

```text
Rbar=alpha B^2Cbar^2+beta z^hBCbar^3
                    +gamma z^(2h)Cbar^4.              (3)
```

Evaluation at zero identifies `alpha=Rbar(0)`. Reducing `(3)` modulo `z^h`
gives

```text
Rbar/(alpha B^2)=Cbar^2 mod z^h.                       (4)
```

The normalized square root in `(CSC3)` is unique because the characteristic
exceeds `d`. Equation `(4)` therefore recovers `Cbar mod z^h`. Since
`deg Cbar=h-3`, it proves `(CSC4)` and the two secondary zero coefficients.

Subtract the first term on the right of `(3)`. The result is exactly `(CSC6)`.
The two basis polynomials have respective orders `h` and `2h`, and both have
unit residual factor at their first term. Hence the coefficient at `z^h`
uniquely gives `beta`; after its term is removed, the coefficient at `z^(2h)`
uniquely gives `gamma`. This proves `(CSC7)`.

By construction, `alpha,beta,gamma` are the elementary symmetric functions
of the centered `w_i`, proving `(CSC8)`. The Möbius weld in the dependency
chain gives one fractional-linear matching `w_i=T(a_i)` after incorporating
the allowed scalar into `T`.

Conversely, suppose the printed canonical conditions hold. Factor `(CSC8)`
with a matching of its distinct roots to the chosen square-root lifts. Identity
`(CSC6)` reverses the preceding algebra to give `(3)`, then `(2)`, and hence
`(1)`. Reverse `B` and `Cbar` to obtain `U,V` and set
`G_i=U+w_iV`. Multiplying by the deleted divisor gives `Y^d-1`; squarefreeness
of the binomial makes the four factors pairwise coprime.

To verify the relation coefficients, write
`T(a)=(rho a+sigma)/(tau a+upsilon)`. Multiplying the matched column
`(1,a_i,w_i,a_iw_i)^T` by its nonzero denominator expresses it as the
evaluation at `a_i` of four quadratic polynomials. Those polynomials span
`1,a,a^2`: the denominator and numerator span `1,a`, and their multiples by
`a` supply `a^2`, because the defining `2 x 2` matrix of `T` is invertible.
Hence any three matched columns are independent, while all four are dependent
by the cross-ratio identity. The unique kernel vector therefore has every
entry nonzero and supplies exactly the two relations in the antipodal descent.
Its converse reconstructs the original component.

Finally let `lambda^d=1` and replace every `b_i` by `lambda b_i`. Since
`1-z^d=1-(lambda z)^d`, direct substitution gives

```text
E_lambda(z)=E(lambda z),       Q_lambda(z)=Q(lambda z),
B_lambda(z)=B(lambda z),       R_lambda(z)=R(lambda z).
```

Dividing by `z^(2h)` proves the transformation of `Rbar` in `(CSC9)`;
normalizing its square root gives `Cbar_lambda(z)=Cbar(lambda z)`. Therefore
`S_lambda=lambda^(2h)S(lambda z)`, which transforms `(CSC6)` with
`beta_lambda=lambda^(3h)beta` and `gamma_lambda=lambda^(4h)gamma`.
The outer parameters scale by `lambda^h`. Choosing a square root of `lambda`
inside the official order-`4d` domain transports the Möbius matching as well.
This proves `(CSC9)` and the normalization claim. QED.
