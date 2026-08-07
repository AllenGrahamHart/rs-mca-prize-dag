# Proof

For a member `S_i`, write `C_i,P_i,Q_i,H_i` as in the statement.  Locator
factorization gives

```text
L_(S_i)-L_(S0)=L_(C_i) H_i,
deg(L_(S_i)-L_(S0))<=A-e+d.                            (1)
```

For two distinct members, `L_(S_i)-L_(S_j)` is nonzero and has degree at
most `A-e+d`.  Every point of `C_i intersect C_j` and every point of
`P_i intersect P_j` is a root.  The two root sets lie in disjoint parts of
`D`, and

```text
|C_i intersect C_j|=A-2e+|Q_i intersect Q_j|.
```

Counting roots in their nonzero locator difference gives

```text
A-2e+|Q_i intersect Q_j|+|P_i intersect P_j|<=A-e+d.
```

This is `(HJ-1)`.

Suppose the family has size `M`.  For each `x in D`, let `r_x` count the
changed sets containing `x`.  With `k=2e` and `lambda=e+d`,

```text
sum_x r_x=Mk,
sum_x binom(r_x,2)<=lambda binom(M,2).
```

Cauchy-Schwarz gives `sum_x r_x^2>=M^2k^2/N`.  Substitution yields

```text
M(k^2/N-lambda)<=k-lambda=e-d.
```

The positive-denominator hypothesis now gives `(HJ-2)`.

For `d=1`, put `e0=N/4+1`.  The denominator in `(HJ-2)` is exactly four at
`e0`.  Writing `e=e0+x`, it is

```text
4e^2-N(e+1)=4+(N+8)x+4x^2.                            (2)
```

Therefore it remains positive, and

```text
N(e-1)/(4e^2-N(e+1))<=N^2/16                          (3)
```

because after multiplying out, the right side minus the left side is

```text
(N^2+8N-16)x+4Nx^2>=0.
```

There are exactly `N/4` integer widths from `N/4+1` through `N/2`.
Summing `(3)` proves `(HJ-3)`.  The difference-degree partition gives
`e>=t_XR+2` at `d=1`, leaving precisely the printed low-width interval. QED.
