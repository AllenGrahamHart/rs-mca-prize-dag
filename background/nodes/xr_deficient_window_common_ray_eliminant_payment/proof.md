# Proof

## The ray matrix pencil

Choose affine coordinates `c=(c_1,...,c_m)` on `A_m` and put `c_0=1`. At
`x_i`, write

```text
V_i(c)=sum_(j=0)^m c_j A_(ij),                      (1)
```

with `A_(i0)=E_i` and `A_(ij)=delta_j(x_i)W_i` for `j>=1`. Every `V_i(c)`
is nonzero on the active defect set.

If the tuple lies in one selected block with common error ray `rho in P^1`,
then

```text
sum_(j=0)^m c_j det(A_(ij),rho)=0,       0<=i<=m.   (2)
```

Write `(2)` as

```text
B(rho)c=-a(rho),                                    (3)
```

where `B` has `m+1` rows and `m` columns, and append `a` to obtain the
square matrix pencil `M(rho)=[a(rho) B(rho)]`. Every entry is homogeneous
linear in `rho`.

Let `t` be the rank of `B` over the rational function field `F(P^1)`. If
`M` also had generic rank `t`, then `(3)` would have a rational solution
`c(rho)` on a nonempty open subset of `P^1`. It would produce an affine
component on which the common ray varies. The distinct-pole argument rules
this out: the `m+2` functions

```text
1,lambda_(x_0),...,lambda_(x_m)
```

are linearly dependent on `m`-space, while as functions of a nonconstant
common ray their `m+1` nonconstant terms have pairwise distinct poles
`[W_i]`. No nontrivial dependence can cancel those poles.

Thus the generic rank of `M` is `t+1`. Choose a nonzero `(t+1)`-minor
`Delta(rho)` of `M`. It is homogeneous of degree `t+1<=m+1`. At every
specialized ray for which `(3)` is consistent,

```text
rank M(rho)=rank B(rho)<=t,
```

so `Delta(rho)=0`. Hence there are at most `m+1` possible projective rays.
The high-depth interaction strip allows at most one target parameter on each
ray. This proves `(CRE1)`.

## Incidence and official rows

Every target has at least `B_(s-m)` core cuts to an `m`-slice and at least
two disjoint selected blocks. Count one occurrence for every distinct-fiber
`(m+1)`-tuple in either block. There are at most `binom(N,s-m)` core subsets
and `binom(e,m+1)` point tuples, while `(CRE1)` caps each fixed pair by
`m+1`. This is `(CRE2)`.

For `m=s` there is no core cut. When `ell=1`, every block contributes exactly
`binom(r,s+1)` tuples, giving `(CRE3)`.

Put `x=d+1`, use `e<=x-3` and `r=h-x+1`, and define

```text
C_s(x)=(s+1)product_(j=0)^s(x-3-j)
              /(2product_(j=0)^s(h-x+1-j)).         (4)
```

As in the full-affine payment,

```text
C_s(x+1)/C_s(x)
 =((x-2)/(x-s-3))*((h-x+1)/(h-x-s))>1.             (5)
```

Exact cross multiplication at the printed last-paid values and their
successors proves `(CRE4)` and both row cutoffs. QED.
