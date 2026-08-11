# Proof

Suppose, toward a contradiction, that

```text
G(t,x_*)=0.                                         (1)
```

Then `X-x_*` divides `G(t,X)`. Choose any projective root `sigma` of the
squarefree quadratic `S_B` over the algebraic closure. By `(HSN1)`,

```text
ord_sigma Q(t,x_*)=3.                              (2)
```

## Sigma is not off-line supported

The exact resultant factorization is

```text
Res_X(Q,G)
 =c_R E_4 product_(delta off line)
                 ell_delta^(n-a_delta).            (3)
```

If `sigma` is not an off-line supported slope, none of the factors in the
product contributes there. This includes the case in which `sigma` is a
center slope: the product in `(3)` is explicitly over off-line slopes.
Since `E_4=c_E S_B^2`, equation `(3)` gives

```text
ord_sigma Res_X(Q,G)=2.                            (4)
```

But `(1),(2)` and resultant multiplicativity give

```text
ord_sigma Res_X(Q,G)>=ord_sigma Q(t,x_*)=3,        (5)
```

contradicting `(4)`.

## Sigma is off-line supported

The all-excess fiber theorem gives

```text
gcd_X(Q(sigma,X),G(sigma,X))=A_sigma(X)R_sigma(X). (6)
```

Since `x_*` is a common root, it lies in the actual-support factor
`A_sigma` or the padded-heavy factor `R_sigma`.

In the first case, `(1),(2)` make the local intersection multiplicity at
`(sigma,x_*)` at least three, contradicting the exact first-jet
transversality value one. In the second case, the definition of `g_*` gives
`g_*(sigma)=0`, contradicting `gcd(g_*,S_B)=1`.

Both possibilities for `sigma` are impossible. Hence `(1)` is false and
`G(t,x_*)` is nonzero. The center-overlap factorization then makes `T_j`
nonzero, and `R_lambda=G(t,x_*)` gives `(HSN3)`. QED.
