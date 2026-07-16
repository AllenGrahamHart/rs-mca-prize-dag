# PMA B11 first-match router

- **status:** PROVED
- **consumer:** `pma_wide_residual`
- **source:** upstream L1 Theorem B11

## Statement

In a maximal-sunflower chart at the L1 lower cutoff with generated field
`q=poly(n)`, let `ell=sigma+1`, let `d` be the missed-core defect, let
`lambda` be the agreement slack, and write

```text
G_2=v_(1)+v_(2),
G_R=(ell-r)+v_(1),
lambda_J=min{j>=0:(s+j)^2>n(k-1)}.
```

Here `r` is the retained-background size and `v_(1)<=v_(2)` are the two
smallest deficits among touched petals. For fixed nonnegative integers
`E,V_2,V_R`, every non-planted extra lies in exactly one of

```text
GROW: d>ell+E;
J:    d<=ell+E, lambda>=lambda_J;
A2:   d<=ell+E, lambda<lambda_J, G_2<=V_2;
AR:   d<=ell+E, lambda<lambda_J, G_2>V_2, G_R<=V_R;
RES:  d<=ell+E, lambda<lambda_J, G_2>V_2, G_R>V_R.
```

The three paid cells satisfy the exact union bound

```text
#(J union A2 union AR)
 <= n(n-k+1)/((s+lambda_J)^2-n(k-1))
  + binom(M,2) sum_(v=0)^V_2 binom(2ell,v) q^(2E+V_2+2)
  + M sum_(w+v<=V_R) binom(b,ell-w)binom(ell,v) q^(2E+V_R+2).
```

When `2(s+lambda_J)>n+k-1`, the first summand may be replaced by `1`.
Therefore only `GROW` and `RES` remain after the B11 gates.

## Scope

This theorem makes the proved B11 union disjoint by a fixed first-match
order. It does not define a quotient-owner predicate, pay `GROW` or `RES`, or
show that the displayed finite bound fits an official `imgfib` row allowance.
