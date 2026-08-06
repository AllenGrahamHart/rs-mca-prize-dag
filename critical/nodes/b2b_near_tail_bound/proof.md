# Proof

The banked degree-interpolation lemma gives, for every `j>=1`,

```text
A_{t+j} <= binom(N,j)/binom(t+j,j).                  (1)
```

The complement of a `t`-null set is `t`-null, so the same count applies to
the upper layer of size `N-t-j`.

We first locate `t`. Put `t0=floor((N-1)/L)`, so `t0L<N`. At rate `1/2`,
Hoeffding gives

```text
log2 binom(N,N/2-t0) <= N-2t0^2/(N ln 2).
```

At the lower rates the relevant index is farther from `N/2`, so symmetry and
unimodality give the same upper bound. Since `t0>=2^33-1`,
`2t0^2/(N ln 2)>385`, while `N-t0L+128<L+129<385`. Thus `t0` satisfies
the corridor inequality, and minimality gives `t<=t0`. Consequently
`tL<N`; because `L>=128`,

```text
t<N/128.                                             (2)
```

Use the standard type-class lower bound

```text
log2 binom(N,xN) >= N H_2(x)-log2(N+1).              (3)
```

The following strict entropy bounds are exact integer inequalities after
exponentiation; `verify.py` replays them without floating point:

```text
H_2(63/128) > 4999/5000 > 256/257,
H_2(1/4)    > 507/625   > 256/316,
H_2(1/8)    > 1087/2000 > 256/472,
H_2(1/16)   > 843/2500  > 256/760.                  (4)
```

At rate `1/2`, (2) puts `N/2-t` between `63N/128` and `N/2`, so binomial
symmetry and unimodality bound the corridor binomial below by
`binom(N,63N/128)`. At each lower rate, (2) keeps `N-rho N-t` above
`N/2`, and moving from `N-rho N` toward the center only increases the
binomial. Hence its lower bound is `binom(N,rho N)`.

Since `N+1<2^42`, (3)-(4) and the corridor inequality give, for the
corresponding constants

```text
C_rho = 257,316,472,760,

tL >= log2 binom(N,N-rho N-t)+128 > 256N/C_rho.
```

As `L<256`, this proves

```text
t>N/C_rho.                                           (5)
```

Expanding the quotient in (1), (5) gives

```text
binom(N,j)/binom(t+j,j)
  = product_{r=0}^{j-1} (N-r)/(t+j-r) < C_rho^j.    (6)
```

For `w_rho=15,14,13,12`, respectively, exact integer arithmetic gives

```text
2 sum_{j=1}^{w_rho} C_rho^j
  < 2 C_rho^(w_rho+1)/(C_rho-1) < 2^122.            (7)
```

Summing (1), using (6)-(7), and applying complementation proves `(NT)`.
QED.
