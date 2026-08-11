# Proof

Every omission `o_gamma=rho-u_gamma` is nonnegative. Their sum is `O=0`, so
all vanish and every supported slope has `u_gamma=rho` distinct domain roots.

The saturation deficit identity becomes

```text
sum_(x in D)(m-d_x)=1.                                (1)
```

Each summand is a nonnegative integer. Hence exactly one point `x_0` has
deficit one and all other points have deficit zero. This proves the first
paragraph.

In the component-defect localization theorem, the overlap correction obeys

```text
0<=E<=O=0,
4b_res<=O-E,                                          (2)
```

where `b_res` is the total parameter degree of every component except the
unique defect-one component. Thus `E=b_res=0`. The factorization is taken
over the algebraic closure, every component has positive parameter degree,
and `Q` is squarefree. Therefore no residual component exists and `Q` itself
is the unique factor: it is absolutely irreducible of bidegree
`(4m-1,m)`. The same ledger gives component deficits

```text
D_*=0,       C_*=1.                                   (3)
```

For the norm factorization, `J` has degree `O=0` and is a scalar, while the
residual form has degree `1+O=1`. Absorb the scalar into `S` to obtain
`R=H^rho S`, proving `(CIN3)`.

Equation `(1)` says the saturated set is exactly `D\{x_0}`. Since
`D=mu_N`, its locator is `(X^N-1)/(X-x_0)`. Substitution in the proved
complementary-factor identity gives `(CIN4)` and its degree bounds specialize
to `(CIN5)`. Finally, the proved clean-fibre count is
`3m+1-O=3m+1`, yielding the transversality statement. QED.
