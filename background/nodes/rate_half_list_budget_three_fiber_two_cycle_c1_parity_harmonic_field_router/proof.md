# Proof

The even-factorization dependency partitions

```text
mu_L\{1,t^(-1)}
```

into two signed cells with a flat prefix of length `L/4`. Its cyclotomic
resultant proof uses only this denominator factorization. It therefore
applies to the `c=1` role patterns and gives

```text
p=1 mod L  ==> p<4L^2,
p=-1 mod L ==> p<2L.                                (1)
```

The maximal-row field collapse leaves

```text
e=1, p=1 mod 2^41,
or
e=2, p=+/-1 mod 2^40.                               (2)
```

The prime-field case in `(2)` contradicts
`p=q_field>=3*2^128>4L^2`. The negative quadratic case contradicts
`p^2<(2L)^2<3*2^128`. Only the positive quadratic case remains, proving
`(CHF1)`.

Taking square roots of
`3*2^128<=p^2<4*2^128` and intersecting with
`p=1 mod 2^40` gives `(CHF2)`. Explicit integer ceiling gives the lower
endpoint `29058991`; the upper endpoint is `2^25=33554432`.

Since `2L|p-1`, all roots of `mu_(2L)` lie in `F_p` and are squares
there. The recurrence and normalized-square-root uniqueness arguments in the
even-factorization field proof place the canonical factors and
`lambda,mu` in `F_p`; its root evaluation makes
`-lambda,-mu` squares. Thus all outer roots descend as well. Also
`4|p-1`, so `iota in F_p`.

A top source lift satisfies `r^(4L)=1`. If `p=1 mod 4L`, it is already
in `F_p`. Otherwise `p=1+2L mod 4L`, and

```text
r^p=eta r,       eta=r^(2L) in {1,-1}.               (3)
```

Equation `(CHF3)` proves descent on `H_P`. On `H_R`, all coefficients
of `(CHF4)` are in `F_p`. If `eta=-1`, subtracting its Frobenius
conjugate from the original equation gives
`6(1+iota)r=0`. Every factor is nonzero, so `eta=1`. This proves
descent in both classes.

For `H_P`, the Gaussian conjugate of `r=(4-3iota)/5` is its reciprocal,
because `4^2+3^2=5^2`. Hence `r+r^(-1)=8/5`.
The standard trace recurrence proves `(CHF5)`.

For `H_R`, choose an eighth root `zeta` with `zeta^2=iota`; it lies in
`F_p` because `8|p-1`. Dividing `(CHF4)` by `iota=zeta^2` gives

```text
s^2+3theta s+1=0,       s=r/zeta,
theta=(1+iota)/zeta.                                 (4)
```

Moreover

```text
theta^2=(1+iota)^2/iota=2.                           (5)
```

Thus `s+s^(-1)=-3theta`, whose first doubled trace is 16. Multiplication
by the order-eight element `zeta` preserves the condition of having order
dividing `2^41`. Forty further updates from exponent two reach exponent
`2^41`, proving `(CHF6)`.

Every possible official characteristic occurs in `(CHF2)), and both trace
tests are necessary and sufficient for their respective residual source
equations to have the required top dyadic order. This proves the screen
contract and all claims. QED.

