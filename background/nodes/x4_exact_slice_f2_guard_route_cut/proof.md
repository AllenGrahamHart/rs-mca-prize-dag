# Proof

Let

```text
t0=floor((N-1)/L).
```

Then `t0 L<N`. We show that `t0` already satisfies `(XR)`, which implies
`t_XR<=t0` and proves `(CUT-1)`.

For `X` binomial with parameters `(N,1/2)`, the one-sided Hoeffding bound
gives, for every integer `d>=0`,

```text
binom(N,N/2-d) <= 2^N exp(-2d^2/N),
log2 binom(N,N/2-d) <= N-2d^2/(N ln 2).                (1)
```

At rate `1/2`, the binomial in `(XR)` at `t0` has `d=t0`. At each lower
official rate its index is farther from `N/2`: because `L>=128`,
`t0<N/128`, while

```text
|(N-K-t0)-N/2|=(1/2-rho)N-t0>t0
```

for `rho<=1/4`. Thus `(1)` with `d=t0` bounds all four rates.
Here we use symmetry and unimodality of the binomial coefficients for the
indices on the upper side of `N/2`.

The floor definition and `L<256` give

```text
N-t0 L+128 < L+129 < 385.                              (2)
```

Also `t0>=2^33-1`. Since `ln 2<1`, exact integer arithmetic gives

```text
2t0^2/(N ln 2) > 2(2^33-1)^2/N > 385.                 (3)
```

Combining `(1)--(3)` yields

```text
log2 binom(N,N-K-t0)+128 < t0 L.
```

Therefore `t0` is an admissible candidate in `(XR)`, and
`t_XR L<=t0 L<N`. Finally `B0` is a subfield of `F_q`, so
`log2|B0|<=L`; `(CUT-2)` follows. QED.
