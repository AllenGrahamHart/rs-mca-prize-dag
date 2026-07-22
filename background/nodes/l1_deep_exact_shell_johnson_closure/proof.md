# Proof - L1 deep exact-shell Johnson closure

## 1. Pairwise agreement packing

Let `P_1,...,P_L` be distinct codewords, each with at least `m` agreements
with `U`.  Select an arbitrary `m`-subset `A_i` of the agreement set of each
`P_i`.  For distinct codewords,

```text
|A_i intersect A_j|<=k-1,                            (1)
```

because `P_i-P_j` is a nonzero polynomial of degree below `k`.

For each coordinate `x`, let `c_x` be the number of selected sets containing
`x`.  Then `sum_x c_x=Lm`.  Cauchy--Schwarz and `(1)` give

```text
sum_x binom(c_x,2)
 >= (L^2m^2/n-Lm)/2,

sum_x binom(c_x,2)
 = sum_(i<j)|A_i intersect A_j|
 <= binom(L,2)(k-1).
```

After multiplication by `2n` and cancellation of `L>0`,

```text
L(m^2-n(k-1))<=n(m-k+1).
```

Under `(DJ1)` division and integer rounding prove `(DJ2)`.  The case `L=0`
is immediate.

## 2. The deep threshold

Write `s=k-1`.  Since `m_J>(n+s)/2`,

```text
m_J^2>(n+s)^2/4>=ns=n(k-1),
```

where the middle inequality is `(n-s)^2>=0`.  Thus `(DJ2)` applies at
`m_J`.  Its denominator is a positive integer and its numerator is at most
`n^2`, proving `(DJ4)`.

Every codeword in a shell with `2m>n+k-1` has at least `m_J` agreements.
Exact shells are disjoint by complete agreement size, and their union is a
subset of `L_>=m_J(U)`.  Hence their total size is at most `n^2`.
