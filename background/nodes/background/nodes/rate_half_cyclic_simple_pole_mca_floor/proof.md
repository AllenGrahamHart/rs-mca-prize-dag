# Proof

## 1. Quantitative simple-pole conversion

Let `C=RS[F,D,k]`, let `C+=RS[F,D,k+1]`, put `q=|F|` and `n=|D|`, and
assume `q>n`. Suppose distinct polynomials

```text
P_1,...,P_L in F[X]_(<k+1)
```

lie in the closed radius-`delta_0` ball around a word `U`, where
`0<=delta_0<1-k/n`. For `alpha in F\D` define the received line

```text
f_alpha(x) = U(x)/(x-alpha),
g_alpha(x) = -1/(x-alpha).
```

For each distinct value `P_i(alpha)`, the corresponding slope word agrees,
on every agreement position of `P_i` with `U`, with the degree-below-`k`
polynomial

```text
(P_i(X)-P_i(alpha))/(X-alpha).
```

It is therefore `delta`-close to `C` for every
`delta_0<=delta<1-k/n`. The line itself has no common codeword explanation
on more than `k` positions: such an explanation for `g_alpha` by a polynomial
`G` of degree below `k` would make

```text
(X-alpha)G(X)+1
```

a degree-at-most-`k` polynomial with more than `k` roots, although its value
at `alpha` is `1`. Thus every distinct value is a CA-bad slope. For positive
radius, the standard support-wise chain
`epsilon_ca<=epsilon_mca` makes the same slopes an MCA lower bound.

For `i!=j`, the nonzero polynomial `P_i-P_j` has degree at most `k`, so the
total number of colliding unordered pairs, summed over the `q-n` possible
poles, is at most `k*C(L,2)`. Some pole therefore has collision count at most
`k*C(L,2)/(q-n)`. If its value multiplicities are `r_1,...,r_M`, then

```text
sum r_j^2 <= L + kL(L-1)/(q-n).
```

Cauchy-Schwarz gives

```text
M >= L(q-n)/(q-n+k(L-1))
  >= L(q-n)/(q-n+kL).
```

Dividing by the `q` finite slopes proves, for CA and for MCA at positive
radius,

```text
epsilon >= E(q,L) := L(q-n)/(q(q-n+kL)).                 (1)
```

The right side is strictly increasing in `L`.

## 2. Insert the longest cyclic residual prefix

Take `c=2^22`, `d=2048`, and `s=c-1` in the dependency
`rate_half_cyclic_rotated_prefix_floor`. Its degree-block argument is valid
for every `s<c`, while its pigeonhole denominator is independent of `s`.
It therefore gives, at agreement

```text
k+sigma_max,       sigma_max=dc+c-1=8,594,128,895,
```

at least

```text
L_q = ceil(B/(N q^(d-1)))
```

distinct codewords of degree below `k`. They are in particular distinct
words of `C+`. The associated radius

```text
delta_0 = 1-(k+sigma_max)/n
```

is positive and strictly below `1-k/n`, so (1) applies. Set the real lower
bound

```text
lambda_q = B/(N q^(d-1)).
```

Since `L_q>=lambda_q` and `E(q,L)` increases with `L`, it is enough to bound
`E(q,lambda_q)`. Its reciprocal is exactly

```text
1/E(q,lambda_q)
  = N q^d/B + kq/(q-n).                                  (2)
```

Every order-`n` multiplicative domain satisfies `q>n`; since `q` is an
integer,

```text
q/(q-n) = 1+n/(q-n) <= n+1.
```

Put `Q=2^256`. Exact integer arithmetic gives

```text
N Q^d < 2^53 B,             k(n+1) < 2^82.               (3)
```

For every official field `q<Q`, equations (2)--(3) imply

```text
1/E(q,lambda_q)
  < 2^53 + 2^82
  < 2^83.
```

Consequently `E(q,L_q)>2^-83>2^-128`, proving (SP1).

Finally, if `1<=sigma<=sigma_max`, then

```text
delta_sigma = 1-(k+sigma)/n
```

satisfies `delta_0<=delta_sigma<1-k/n` and is positive. The same deep list and
simple-pole line therefore prove the claimed CA and MCA lower bounds
throughout the entire interval. Since

```text
8,592,912,738+1 <= 8,594,128,895,
```

this also proves that the former fixed adjacent-safe claim is false. QED.
