# Proof

Fix a root `a` of `D_k`. Pair-Lagrange specialization and monic row
normalization give

```text
Q(z;a)=q_e(a) zI(z)/(z-xi_k).                         (1)
```

If `i!=k`, then `E_i(a)=B(a)A(a)/D_i(a)=0`. Differentiate `(1)` at
`z=xi_i`. Since

```text
partial_z[zI(z)/(z-xi_k)] at xi_i
 =xi_i I'(xi_i)/(xi_i-xi_k),                         (2)
```

the definition `(CLQ3)` of `N_i` reduces to

```text
N_i(a)=-q_e(a)c_iD_i(a)xi_i/
        [lambda_i(xi_i-xi_k)].                       (3)
```

The term with `i=k` in `sum_iD_i(a)N_i(a)L_i(z)` is zero because
`D_k(a)=0`. Substitute `(3)`, divide by `z-xi_k`, and use `(QTK1)--(QTK2)`.
This proves `(QTK3)`. In particular, all logarithmic-derivative terms
`rho_i=P_Z'(xi_i)/P_Z(xi_i)` have disappeared from the exceptional
boundary.

Now substitute `(QTK3)` into the dual moment `(QBM2)`:

```text
M_j(z)=sum_(k,a:D_k(a)=0)
 a^(j+1)(a-s)(a-x_0)B(a)q_e(a)^2V_a(z).              (4)
```

Interchange the sums over `i` and `k`. For fixed `i,k`, the sum over the two
roots of `D_k` is exactly the algebra trace in `(QTK4)`. The remaining
factor is `W_ik/(xi_i-xi_k)`, and the minus sign comes from `(QTK3)`.
This proves `(QTK4)--(QTK5)`.

The dual-moment dependency says that every exact design has `M_j=0` for all
displayed `j`. Taking all coefficients in `z` gives `(QTK7)`. Every
coordinate of `theta` is nonzero: the internal slopes and `lambda_i` are
nonzero, while `P_Z(xi_i)` is nonzero because internal and external slopes
are disjoint. Therefore full column rank, or a kernel disjoint from the
coordinate torus, excludes the packet.

It remains to prove `(QTK8)`. Let `K=ker T`. There is a vector in `K` with
nonzero `i`th coordinate exactly when column `i` of `T` lies in the span of
the other columns, equivalently when deleting column `i` preserves rank. If
this holds for every `i`, each coordinate hyperplane cuts at most
`q^(dim K-1)` points from `K`. Since `q>e`, the union of the `e` coordinate
hyperplanes has fewer than `q^(dim K)` points, so some vector of `K` has no
zero coordinate. The converse is immediate. QED.
