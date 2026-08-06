# Official exact-slice worst-prefix residual budget

- **status:** TARGET
- **closure:** open

Let `N=2^41`, `K=rho N`, and let the official exact-list depth be

```text
t_XR=min{t>=0 : t log2(q) >= log2 binom(N,N-K-t)+128}.
```

Put `A=K+t_XR`. For each `A`-subset `S` of the evaluation domain, let

```text
Phi_(A,t_XR)(S)
```

be the first `t_XR` sub-leading coefficients of its monic locator. For every
prefix `z`, remove the quotient, dihedral, boundary, moment-trade, and other
explicitly paid `x4` first-match classes, and call the residual fiber `R_z`.
Prove

```text
max_z |R_z| <= N^3.
```

This is the sufficient boundary-prefix budget consumed by the exact-list
assembly. The proved `x4_locator_prefix_consumer_scope` shows why the maximum
over `z` is load-bearing: exact polynomial boundary words realize every
prefix fiber as a list, raw mode-at-null is false, and in characteristic `p`
power-sum nullity leaves the `p`-multiple locator coefficients free.

The guarded full-subset F2 terminal does not supply this claim because the
route cut gives `t_XR log2|F_p(mu_N)|<N` on every official row. The proved
null-fiber near-tail widths `15,14,13,12` remain valid evidence for a possible
strip-aware exchange-compression route, but they do not reduce an arbitrary
prefix fiber without that additional theorem.
