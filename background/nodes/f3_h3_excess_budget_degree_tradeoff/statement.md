# H3 excess-budget versus multistar-degree tradeoff

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:** `f3_h3_quotient_block_identity`,
  `f3_h3_excess_multistar_degree_ladder`

For a nonidentity target put

```text
e(t)=max(P(t)-18,0).
```

For every integer `0<=E<=17`, split

```text
X_18^<=E=sum_(t!=1,e(t)<=E) e(t)R(t),
X_18^>E =sum_(t!=1,e(t)> E) e(t)R(t).
```

The exact quotient-mass identity gives

```text
X_18^<=E <= E(n-1)(n-2).                           (EBD1)
```

Consequently the single high-tail estimate

```text
17 X_18^>E <= B_E(n),
B_E(n)=300n^2-17E(n-1)(n-2),                       (EBD2)
```

implies C36', `17X_18<=300n^2`.

Every target retained by `(EBD2)` has a weighted multistar center of degree
at least

```text
Delta_E=L(7+ceil((E+1)/2)),                        (EBD3)
```

where `L(m)=m-4` for even `m` and `m-3` for odd `m`. The Pareto choices in
this interface are

```text
E       conservative B_E/n^2       Delta_E
0       300                         4
2       266                         6
6       198                         8
10      130                         10
14      62                          12
```

The exact budgets in `(EBD2)` are slightly larger than the conservative table
for every `E>0`. Intermediate cutoffs have the same guaranteed degree as an
earlier displayed cutoff and a smaller residual budget.

This is a family of sufficient reductions. It does not prove any of the
high-tail estimates `(EBD2)`.
