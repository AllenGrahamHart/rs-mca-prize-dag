# Proof

Choose a minimal separated presentation

```text
G(t,X)=sum_(j=1)^r A_j(t)B_j(X),                   (1)
```

so `V=span{A_j}` and the `B_j` are independent of degree at most `n`.
The three-center source partition gives class sizes

```text
|M_gamma|=p-1+r_gamma,       sum_gamma r_gamma=1. (2)
```

They are therefore `n+2,n+2,n+3`. Evaluation of the `B_j` on any one
class is injective because its size exceeds `n`. Hence

```text
span{G(t,x):x in M_gamma}=V                        (3)
```

for every `gamma`.

Write `H_x=G(t,x)/L_U0'(x)`. On `M_gamma`, the source identity gives

```text
Qbar(t,x)=eta_x^(-1)q_gamma(t)H_x(t).              (4)
```

The nonzero row scalars do not change spans, so `(3),(4)` imply

```text
span{Qbar(t,x):x in M_gamma}=q_gamma V.            (5)
```

The first-degree primitive locator has `e+1` independent parameter
coefficients and `X`-degree `3e-2<R`. Evaluation on `U_0` therefore
preserves its coefficient rank, and its row span is all of
`F[t]_(<=e)`. Summing `(5)` over the three-class partition proves `(KGR3)`.
Surjectivity and rank-nullity prove `(KGR5)`.

We next identify the triple intersection. If

```text
F=bc f_alpha=ac f_beta=ab f_theta,
f_alpha,f_beta,f_theta in V,                       (6)
```

coprimality of the distinct linear forms gives one `h` with

```text
f_alpha=ah,       f_beta=bh,       f_theta=ch.     (7)
```

Thus `h in J` and `F=abc h`; the converse is immediate. For every `h in J`,
the two triples

```text
(ah,-bh,0),       (ah,0,-ch)                      (8)
```

belong to `ker Phi`. Their map from `J direct_sum J` is injective, proving
the second inequality in `(KGR7)`.

It remains to use source isotropy. Let `v_x` be the monomial coefficient
column of `Qbar(t,x)`. The marked-source frame gives

```text
sum_(x in U_0)omega_x^(s)v_xv_x^T=0,
s in {0,1}.                                        (9)
```

On `M_gamma`, `omega_x(t)=eta_x ell_gamma(t)`. Hence `(9)` is the two
coefficient equations of

```text
sum_gamma ell_gamma(t) C_gamma=0,
C_gamma=sum_(x in M_gamma)eta_xv_xv_x^T.           (10)
```

Three distinct projective linear forms in a two-dimensional space have a
one-dimensional relation, and every coefficient in that relation is
nonzero. Applying this entrywise to `(10)` gives `(KGR8)` for one symmetric
matrix `K` and nonzero `u_gamma`.

By `(5)`, the image of `C_gamma` lies in `q_gamma V`. Proportionality makes
the image of `K` lie in all three spaces, and `(KGR7)` proves the upper
bound in `(KGR9)`.

Finally write the coefficient columns of the `H_x`, `x in M_gamma`, as the
rows of a matrix `E_gamma`. Equation `(3)` gives `rank E_gamma=r`. From
`(4)`, `C_gamma` is obtained by applying the injective multiplication map
by `q_gamma` to

```text
E_gamma^T diag(eta_x^(-1)) E_gamma.                (11)
```

The diagonal matrix is invertible. Sylvester's rank inequality therefore
gives

```text
rank C_gamma>=2r-|M_gamma|.                        (12)
```

The smallest class has size `n+2`, so the common rank `k` obeys `(KGR9)`.
The official substitutions in `(KGR5),(KGR10)` are direct. QED.
