# Proof

Equal-prefix is an equivalence relation. Its classes on `R` are precisely the
nonempty residual fibers `R_z`. The graph in the statement is therefore a
disjoint union of cliques. A vertex in a clique of size `m` has degree `m-1`,
which proves `(SP-1)` and its equivalence with `(SP-2)`.

For the distance statement, write

```text
S=C disjoint_union U,
T=C disjoint_union V,
|U|=|V|=e,
Q_S=Q_C Q_U,
Q_T=Q_C Q_V.
```

The supports are distinct, so `Q_U-Q_V` is nonzero. Hence

```text
deg(Q_S-Q_T)>=deg Q_C=A-e.                            (1)
```

Equality of the first `t` sub-leading coefficients cancels the leading term
and those `t` coefficients, giving

```text
deg(Q_S-Q_T)<=A-t-1.                                  (2)
```

Combining `(1)` and `(2)` yields `e>=t+1`. If `e=t+1`, both bounds are equal
to `A-t-1=deg Q_C`. Since

```text
Q_S-Q_T=Q_C(Q_U-Q_V),
```

the residual factor `Q_U-Q_V` has degree zero and is nonzero. This is exactly
the constant-shift top stratum. QED.
