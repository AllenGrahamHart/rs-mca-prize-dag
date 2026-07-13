# Direction-distance residual ray bound

- **status:** see `dag.json` (single source of truth)

Let `H_U:F^U->F^R` be a parity-check restriction, put `N=|U|` and
`K=ker H_U`, and fix a nonconstant syndrome line `y_0+gamma*y_1` with
`y_1 in im(H_U)`. Define

```text
d_U(y_1) = min{wt(b): H_U b=y_1},
mu_U(y_1) = N-d_U(y_1).
```

Suppose every `gamma` in a finite set `Z` has a lift of
`y_0+gamma*y_1` supported on at most `t<N` coordinates of `U`. If

```text
(N-t)^2 > N mu_U(y_1),                                  (DD)
```

then

```text
|Z| <= floor(N(d_U(y_1)-t) / ((N-t)^2-N mu_U(y_1)))
    <= N^2.                                               (DDR)
```

No transversality hypothesis is needed. If `(DD)` fails, `y_1` has a lift
of weight at most

```text
floor(2t-t^2/N),
```

so the complementary chart is an explicit sparse-direction chart. For an RS
syndrome line induced by `(u,v)`, extending this lift by zero says that `v`
differs from a codeword on only those coordinates; the codeword component can
be absorbed into the candidate pencil.

This is a fixed-chart theorem. It neither constructs nor counts a
witness-exhaustive atlas of charts.

