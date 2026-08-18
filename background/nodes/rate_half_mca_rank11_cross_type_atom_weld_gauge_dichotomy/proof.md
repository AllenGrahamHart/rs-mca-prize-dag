# Proof

Choose once and for all 18 anchor records for every large type. The symmetric
packet construction can use those records on every incident edge.

## Common scalar normalization

Fix a type `p` and two incident edge certificates. Their `p`-anchored packets
contain the same 18 exact supports. After the common triple-owner core is
canceled, write each support locator as

```text
Lambda_i=L_p L_(E_i),
```

where `L_p` is the residual `p` pair-core locator and the monic exception
locators `L_(E_i)` are pairwise coprime and nonempty. Restricting a
certificate to the anchor line `h_i=a_p+gamma_i b_p` and using two slopes
shows

```text
A-Qa_p=L_pu,       B-Qb_p=L_pv,
u+gamma_i v=(c_0+c_1gamma_i)L_(E_i).                 (1)
```

The same equations hold with primes for the second certificate. Three
shared slope-locator pairs identify the two projective parameterizations of
the two-dimensional locator pencil: the induced projective automorphism
fixes three points and is the identity. Hence

```text
(u',v')=lambda(u,v),       (c'_0,c'_1)=lambda(c_0,c_1).
```

Thus all edge scalar pairs incident to `p` are proportional. One edge is
incident to both of its endpoints, and the complete type graph is connected,
so every edge certificate can be scaled to one fixed nonzero scalar pair
`c=(c_0,c_1)`.

## Triangle cocycle

Two normalized certificates on edges `{p,q}` and `{p,r}` share the 18 fixed
`p` records and now have identical locator coefficients. Subtraction cancels
the locator terms:

```text
(Q_pq-Q_pr)h_i=(A_pq-A_pr)+gamma_i(B_pq-B_pr).
```

Using two anchor slopes and `h_i=a_p+gamma_i b_p` gives a polynomial `D_p`
with

```text
C_pq-C_pr=D_p(1,a_p,b_p)=D_pT_p.                    (2)
```

The same argument at `q` and `r` gives the other two identities in `(GD1)`.
Adding the first and third differences yields the cocycle relation.

If `det(T_p,T_q,T_r)` is nonzero, the three vectors are independent over
`F(X)`. The cocycle forces `D_p=D_q=D_r=0`, so all three edge certificates
are equal.

## Global propagation

Suppose `T_a,T_b,T_c` form one independent triple. Its three edge
certificates equal some `C_*`. For any other type `s`, the two determinants

```text
det(T_a,T_c,T_s),       det(T_b,T_c,T_s)
```

cannot both vanish. Otherwise `T_s` lies in both planes
`<T_a,T_c>` and `<T_b,T_c>`, whose intersection is `<T_c>`. Since the first
coordinate of every `T` is one, this would give `T_s=T_c`, contrary to
distinct pair types. One of the two nondegenerate triangles therefore makes
its two new edges equal `C_*`.

Now take any two distinct types `s,t`. Their vectors are independent because
both have first coordinate one and are unequal. Not all three basis vectors
`T_a,T_b,T_c` lie in `<T_s,T_t>`, so some `T_x` among them makes
`det(T_x,T_s,T_t)` nonzero. The already synchronized edges `{x,s}` and
`{x,t}` equal `C_*`; the triangle identity then gives `C_st=C_*`. Hence every
edge certificate is the same.

If no independent triple exists, every triple determinant vanishes and the
span of all `T_p` over `F(X)` has dimension at most two. This is `(GD2)`.
QED.
