# Proof: RS deep-point list-to-CA conversion

Put `epsilon=epsilon_ca(C,delta)` and `f=floor(delta N)`. Fix a received word
`U:D->F` and distinct polynomials

```text
P_1,...,P_L in F[X]_{<K+1}
```

whose evaluation words lie in the closed radius-`delta` ball around `U`.
Each `P_i` agrees with `U` on at least `A=N-f` points. By `(DP1)`,
`A>=K+1`.

For `alpha in F\D`, define

```text
f_alpha(x)=U(x)/(x-alpha),
g_alpha(x)=-1/(x-alpha).                              (1)
```

On every agreement support of `P_i`,

```text
f_alpha(x)+P_i(alpha)g_alpha(x)
  =(P_i(x)-P_i(alpha))/(x-alpha),                    (2)
```

which is the evaluation of a polynomial of degree below `K`. Distinct values
among the `P_i(alpha)` therefore give slopes whose line points are
`delta`-close to `C`.

The received pair in `(1)` is CA-far on every such support. Indeed, if a
polynomial `G` of degree below `K` agreed with `g_alpha` on more than `K`
points, then

```text
(X-alpha)G(X)+1
```

would have degree at most `K`, more than `K` roots, and value `1` at
`alpha`, a contradiction. Thus every distinct value in `(2)` is a CA-bad
slope.

Let `Omega=F\D`, so `|Omega|=q-N`. For `i!=j`, the nonzero polynomial
`P_i-P_j` has degree at most `K` and hence at most `K` roots in `Omega`.
The total number of colliding unordered pairs over all `alpha in Omega` is
therefore at most

```text
K binom(L,2).                                         (3)
```

Choose `alpha` whose collision count is at most the average in `(3)`. If
`m_1,...,m_M` are the multiplicities of the distinct values at this `alpha`,
then

```text
sum_r m_r=L,
sum_r m_r^2<=L+K L(L-1)/(q-N).                       (4)
```

Cauchy-Schwarz applied to `(4)` gives

```text
M>=L(q-N)/(q-N+KL).                                  (5)
```

All `M` values are CA-bad slopes, so

```text
epsilon>=L(q-N)/(q(q-N+KL)).                         (6)
```

Solving `(6)` yields

```text
L<=epsilon q(q-N)/(q-N-K epsilon q),                 (7)
```

provided the denominator is positive. Under `(DP2)`, that denominator is at
least `(1-eta)(q-N)`, proving `(DP3)` after taking the integer ceiling.

For `(DP5)`, a numerator bound `Q` gives `epsilon<=Q/q`. Set

```text
eta=KQ/(q-N).
```

Condition `(DP4)` places `eta` in `[0,1)`, makes `(DP2)` an equality at the
upper bound `Q/q`, and specializes `(DP3)` to `(DP5)`. QED.
