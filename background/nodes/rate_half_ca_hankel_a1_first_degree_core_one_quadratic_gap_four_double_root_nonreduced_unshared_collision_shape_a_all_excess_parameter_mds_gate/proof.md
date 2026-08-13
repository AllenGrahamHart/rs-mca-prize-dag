# Proof

For each `0<=i<=n`, write

```text
G(t,X)=sum_(i=0)^n h_i(t)X^i.                      (1)
```

The parameter degree bound is equivalent to

```text
deg h_i<=m=e-2.                                    (2)
```

At a slope `delta`, the coefficient of `X^i` in `(APG3)` is

```text
h_i(delta)
 =sum_(h=0)^a_delta d_(delta,i-h)c_(delta,h).      (3)
```

There are `|Gamma|=3e` slope points. The dual description of the
Reed--Solomon evaluation code of dimension `m+1=e-1` says that a vector
`(v_delta)` is the evaluation of a polynomial of degree at most `m` if and
only if

```text
sum_(delta in Gamma)
 v_delta delta^l/L_Gamma'(delta)=0,
0<=l<=3e-m-2=2e.                                   (4)
```

Substituting `(3)` into `(4)`, for every `i`, is exactly the matrix equation
`(APG6)`.

If the fibers come from `G`, equations `(1)--(4)` prove necessity.
Conversely, if `(APG6)` holds, `(4)` supplies for every `i` a unique
polynomial `h_i` of degree at most `m` taking the values `(3)`. The biform
defined by `(1)` has bidegree at most `(m,n)` and specializes to
`D_delta C_delta` at all `3e` slopes. This proves sufficiency.

The shape-A excess identity is `sum_delta a_delta=e`. Every block has
`a_delta+1` coefficients, so

```text
sum_delta(a_delta+1)=e+3e=4e,                      (5)
```

which proves `(APG7)`. The row count in `(APG8)` is

```text
(n+1)(2e+1).                                       (6)
```

The official substitutions are exact arithmetic. Finally, `C_delta` is a
nonzero scalar multiple of `H_delta`, so its degree is
`a_delta-q_delta`, proving `(APG9)`. QED.
