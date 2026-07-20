# Proof

## 1. Source reconstruction

The contracted middle Hankel matrix has size `(r+1) x (r+1)` and uses the
moments through degree `2r`. At the exceptional slope its rank is `r-1`, and
its kernel is spanned by the two padded shifts of the squarefree degree-`r-1`
polynomial `A`.

Solve the Vandermonde system on `R_A` for the first `r-1` moments of `h_0`.
The two kernel shifts give the recurrence with characteristic polynomial `A`
at shifts `0,...,r+1`, so that solution reproduces every moment through
degree `2r`. Thus

```text
h_0=sum_(a in R_A) beta_a c(a).                       (1)
```

If some `beta_a` vanished, the Hankel matrix of `(1)` would have rank at
most `r-2`, contrary to its proved rank `r-1`. Hence all `beta_a` are
nonzero.

The quotient-distance router gives a representation of `h_1` on `R_A union
T` with the three printed barycentric coefficients. These `r+2` moment
columns are linearly independent because `r+2<=2r+1`, so all coefficients
in `(MER2)` are unique.

At an ordinary supported slope the middle Hankel matrix has rank `r` and its
squarefree degree-`r` locator has root set `G_z`. The same recurrence and
Vandermonde argument gives

```text
h(z)=sum_(g in G_z) lambda_g c(g),       lambda_g!=0. (2)
```

Nonvanishing again follows from rank `r`.

## 2. The MDS boundary

Let `F_z` be the support of the representation obtained by adding `(MER2)`:

```text
h(z)=sum_(a in R_A)(beta_a+z alpha_a)c(a)
       +sum_(t in T)z omega_t c(t).                   (3)
```

Every ordinary slope has `z!=0`, so all three coefficients on `T` are
nonzero and

```text
|F_z|=r+2-j_z.                                       (4)
```

Subtract `(2)` from `(3)`. If the resulting relation is nonzero, its support
has at least `2r+2` points because every set of at most `2r+1` distinct
columns `c(x)` is Vandermonde-independent. On the other hand its support has
size at most

```text
|F_z|+|G_z|=2r+2-j_z.                                (5)
```

Therefore a nonzero relation forces `j_z=0`, disjointness of `F_z=S` and
`G_z`, and equality in the MDS distance. This is the second alternative.

If the relation is zero, the two nonzero source representations coincide.
Their support sizes are equal, so `(4)` gives `j_z=2`, and their common
support is exactly `(MER4)`. This is the first alternative. These two cases
also exclude `j_z=1` and `j_z>=3`.

For a minimum-distance escape put

```text
P_z(X)=A(X)B_T(X)G_z(X).
```

The unique relation on its `2r+2` roots has coefficients

```text
mu_x=lambda/P_z'(x)                                  (6)
```

for one nonzero scalar `lambda`. At a point `t in T`, equations `(MER2)`
and `(6)` give

```text
z Theta_2/(A(t)^2 B_T'(t))
  =lambda/(A(t)B_T'(t)G_z(t)).                       (7)
```

Cancellation proves `(MER5)`, with
`kappa_z=lambda/(z Theta_2)`.

For each `a in R_A`, the affine coefficient `beta_a+z alpha_a` has at most
one zero because `beta_a!=0`. Every internal fiber consumes two such zeros.
Thus their cancelled pairs are disjoint and there are at most

```text
floor((r-1)/2)=e                                     (8)
```

internal fibers.

## 3. Exact official composition

The corrected exceptional-only face has `4e+1` supported slopes, one of
which is exceptional. Hence there are `4e` ordinary slopes. Equation `(8)`
shows that at least `3e` of them are minimum-distance escapes.

The set `S` has size

```text
|S|=(r-1)+3=2e+3,
```

so its complement in the residual domain has size `6e+4`. No residual
domain point is a fixed root of the primitive residual generator. For every
point outside `S`, specialization in the slope parameter is therefore a
nonzero form of degree at most `e`; that point can occur in at most `e`
external locators. If `N_ext` is their number, incidence counting gives

```text
N_ext(2e+1)<=e(6e+4),
N_ext<=floor((6e^2+4e)/(2e+1))=3e.                   (9)
```

Thus equality holds throughout: `N_ext=3e` and there are exactly `e`
internal fibers. Their disjoint pairs consequently partition the `2e`
roots of `A`.

Finally, subtracting the `3e(2e+1)` external incidences from the total
capacity `(6e+4)e` gives `(MER7)`. Every nonsaturated outside point
contributes at least one to this deficit, so at most `e` points are
nonsaturated and at least `5e+4` are saturated. QED.
