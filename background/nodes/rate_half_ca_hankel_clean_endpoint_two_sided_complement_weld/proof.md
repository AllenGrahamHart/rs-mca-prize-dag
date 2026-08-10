# Proof

For every `gamma in Z`, clean saturation says that `Q(gamma;X)` is a
squarefree degree-`rho` divisor of `G=X^N-1`. Define

```text
A_gamma(X)=G(X)/Q(gamma;X).
```

Its `X`-degree is `N-rho`. Interpolate every coefficient of `A_gamma` at the
`T` distinct values of `gamma`. This gives `A(z;X)` with

```text
deg_z A<T,       deg_X A=N-rho.                       (1)
```

Every coefficient in `X` of `Q A-G` vanishes at all roots of the squarefree
polynomial `H`. Hence `H` divides `Q A-G`. Choosing the sign of the quotient
gives

```text
Q A+H B=G.                                           (2)
```

Since `deg_z Q=m`, equation `(1)` gives

```text
deg_z B<=m+(T-1)-T=m-1.                              (3)
```

The `X`-degree of `Q A` is at most `rho+(N-rho)=N`, so `deg_X B<=N`.
This proves `(CWD2)--(CWD3)`.

The clean endpoint corollary supplies

```text
Q V+P W=H,       G=P(X-x_0).                         (4)
```

Multiply `(4)` by `B`, use `(2)`, and eliminate `H B`:

```text
Q(VB+A)+P(WB-(X-x_0))=0.                             (5)
```

The absolutely irreducible `Q` has positive parameter degree, whereas `P`
depends only on `X`; therefore `gcd(Q,P)=1`. Equation `(5)` implies that `Q`
divides `WB-(X-x_0)`. Define the quotient to be `K`. Substitution into `(5)`
then gives `(CWD6)`.

The degree bounds are direct:

```text
deg_z K<=T+(m-1)-m=T-1,
deg_X K<=(rho-1+N)-rho=N-1.                          (6)
```

If `B=0`, equation `(2)` would make the positive-parameter-degree
irreducible polynomial `Q` divide the `X`-only polynomial `G`, which is
impossible. If `W=0`, equation `(4)` would similarly make `Q` divide the
parameter-only polynomial `H`. Hence both factors are nonzero. Reducing
`(CWD5)` modulo `Q` proves `(CWD8)`. QED.
