# Proof - L1 tame fixed-petal refinement census

## 1. A refinement is a right component

Let `T_i` be the union of complete degree-`s` fibers with labels in `A`.
For each `a in A`, the monic degree-`s` polynomial `P-a` has exactly the `s`
distinct points of that fiber as roots. It is therefore the monic locator of
the fiber. The fibers are disjoint, so multiplying these identities proves
`(TR2)`. In particular `|A|=r`, and `F_A` is monic, split, and squarefree.

## 2. Recover the right component from high coefficients

Write

```text
P=X^s+p_(s-1)X^(s-1)+...+p_1 X+p_0,
F=Z^r+f_(r-1)Z^(r-1)+...+f_0,
L_(T_i)=F(P).                                           (1)
```

For `1<=j<=s-1`, every term `f_u P^u` with `u<r` has degree at most
`s(r-1)=rs-s`, strictly below `rs-j`. Hence the coefficient of
`X^(rs-j)` in `L_(T_i)` comes only from `P^r`. In that coefficient, using
`p_(s-j)` once and `X^s` in the other `r-1` factors contributes
`r p_(s-j)`. Every other contribution uses only
`p_(s-1),...,p_(s-j+1)`. Therefore

```text
[X^(rs-j)]L_(T_i)
 =r p_(s-j)+Phi_j(p_(s-1),...,p_(s-j+1)).              (2)
```

When `p` does not divide `r`, equation `(2)` successively determines
`p_(s-1),p_(s-2),...,p_1`. The constant `p_0` is the only undetermined
coefficient. Replacing `P` by `P+c` merely replaces `F(Z)` by `F(Z-c)`, so
this is exactly the declared additive-shift equivalence. Equivalently,
normalizing `P(0)=0` leaves at most one right component. This proves tame
uniqueness for one `(T_i,s)`.

Assign every refinement class to the least source petal it carries. There is
at most one class for each owner and each tame divisor `s|ell`. Thus their
number is at most `M_src tau(ell)`. The petals in `(TR1)` are disjoint, so
`M_src ell<=n`; also `tau(ell)<=ell`. This proves `(TR4)`.

## 3. Wild counterfixture

Let `K=F_(p^2)`. For every one-dimensional `F_p`-subspace `V subset K`, put

```text
P_V(X)=product_(v in V)(X-v).
```

This is a monic `F_p`-linearized polynomial of degree `p` with kernel `V`.
Its image `W_V=P_V(K)` is another one-dimensional `F_p`-subspace. Put

```text
G_V(Y)=product_(w in W_V)(Y-w).
```

The monic polynomial `G_V(P_V(X))` has degree `p^2`. Its roots are exactly
`K`: on `K`, membership `P_V(x) in W_V` is automatic, and squarefreeness
follows equally from the `p` disjoint fibers of size `p`. Hence

```text
G_V(P_V(X))=product_(x in K)(X-x)=X^(p^2)-X.            (3)
```

There are `p+1` such subspaces. Their locators `P_V` are distinct and all
have constant term zero, so no two differ by a nonzero constant. This proves
the wild boundary claim. It does not place `K` itself inside a multiplicative
evaluation domain and therefore does not decide wild admissible L1 cells.

## 4. Exact residual

The theorem counts refinement maps, not their complete-fiber role vectors.
For small `s`, independently assigning roles to `n/s` fibers gives the unsafe
raw overcount `3^(n/s)`. Closing the local L1 route still requires a
collective small-scale payment or a natural-scale owner theorem, plus a
domain-specific treatment of wild right components and unanchored locators.
