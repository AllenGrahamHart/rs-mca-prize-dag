# Proof

Let

```text
t0=floor((N-1)/L).
t1=t0-1.
```

Then `t0 L<=N-1`, so, using `L>=128`,

```text
t1 L<=N-1-L<=N-129.                                    (0)
```

We show that `t1` already satisfies `(XR)`, which implies `t_XR<=t1` and
proves `(CUT-1)`.

For `X` binomial with parameters `(N,1/2)`, the one-sided Hoeffding bound
gives, for every integer `d>=0`,

```text
binom(N,N/2-d) <= 2^N exp(-2d^2/N),
log2 binom(N,N/2-d) <= N-2d^2/(N ln 2).                (1)
```

At rate `1/2`, the binomial in `(XR)` at `t1` has `d=t1`. At each lower
official rate its index is farther from `N/2`: because `L>=128`,
`t1<N/128`, while

```text
|(N-K-t1)-N/2|=(1/2-rho)N-t1>t1
```

for `rho<=1/4`. Thus `(1)` with `d=t0` bounds all four rates.
Here we use symmetry and unimodality of the binomial coefficients for the
indices on the upper side of `N/2`.

The floor definition and `L<256` give

```text
N-t1 L+128 < 2L+129 < 641.                             (2)
```

Also `t1>=2^33-2`. Since `ln 2<1`, exact integer arithmetic gives

```text
2t1^2/(N ln 2) > 2(2^33-2)^2/N > 641.                 (3)
```

Combining `(1)--(3)` yields

```text
log2 binom(N,N-K-t1)+128 < t1 L.
```

Therefore `t1` is an admissible candidate in `(XR)`, and `(0)` gives
`t_XR L<=t1 L<=N-129`. Finally `B0` is a subfield of `F_q`, so
`log2|B0|<=L`; `(CUT-2)` follows. QED.
