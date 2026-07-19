# Proof

We first strengthen the cogirth basis lemma used by the affine-core charge.

**Loopless cogirth basis lemma.** Let `M` be a loopless rank-`a` matroid on
`m` elements, with cogirth at least `c`. If `b(M)` is its number of bases,
then

```text
a b(M) >= m C(a+c-2,a-1).                              (1)
```

Indeed, `M*` has rank `m-a`, girth at least `c`, and no coloops. For every
element `x`, deletion `M*\x` still has rank `m-a`. Its dual has rank `a-1`
and cogirth at least `c`, so the proved cogirth basis lemma gives at least
`C(a+c-2,a-1)` bases of `M*` avoiding `x`. Summing over `x` counts every
basis exactly `a` times and proves `(1)`.

Return to the selector. The `a`-dimensional kernel slice

```text
K=(A-A) intersect ker H
```

is represented by an `a`-dimensional subspace of polynomials of degree less
than `k`. If every polynomial in that subspace vanishes on `G`, division by
the product of the `g` distinct root factors embeds it into the polynomials
of degree less than `k-g`. Hence

```text
g<=k-a.                                                 (2)
```

At a coordinate of `G`, the value of an error in `A` depends only on its
slope: two errors at the same slope differ by a word of `K`. It is therefore
an affine function of `gamma`. It is identically zero precisely on `P_0`;
at every coordinate of `G\P_0` it vanishes at at most one selected slope.
Writing

```text
l_e=|Z_e intersect (G\P_0)|,
```

the distinct-slope hypothesis gives

```text
sum_e l_e <= g-p.                                       (3)
```

For a selected error `e`, the restriction of `K` to `Z_e` has rank `a` and
cogirth at least `h+1`, exactly as in the affine-core cogirth theorem. After
deleting its loop coordinates, it has at least

```text
m_e >= |Z_e|-p-l_e >= k+h-p-l_e
```

nonloop elements. Apply `(1)` with `c=h+1`. If `b_e` is the number of
kernel-coordinate bases contained in `Z_e` and

```text
Q=C(a+h-1,a-1),
```

then `a b_e>=m_e Q`. Summing and using `(3)` gives

```text
a sum_e b_e >= Q ( |P|(k+h-p) - (g-p) ).               (4)
```

Every kernel basis avoids all of `G`, so there are at most `C(n-g,a)`
possible bases. The proved post-strip affine-pencil argument bounds the
number of selected errors containing any one basis by `L`: if two slopes use
that basis, its persistent coordinates together with the basis are their
exact common zero set, of size at most `kappa`. Consequently

```text
sum_e b_e <= C(n-g,a)L.                                 (5)
```

Combining `(4)` and `(5)` proves `(CRB1)`.

For the uniform consequence, use `(2)` and put

```text
u=k-a-g,       v=g-p,       u,v>=0,       u+v<=k-a.
```

Then `(CRB1)` gives, with `d=a+h`,

```text
|P| <= (aL C(R+a+u,a)+Qv)/(Q(d+u+v)).                  (6)
```

For fixed `u`, the right side of `(6)` is monotone in `v`, since the sign of
its forward difference is independent of `v`. Its maximum therefore occurs
at `v=0` or `v=k-a-u`.

On the first boundary, consider

```text
f(u)=C(R+a+u,a)/(u+a+h).
```

The sign of `f(u+1)-f(u)` is the sign of

```text
(a-1)u+a(a+h)-R-1.
```

This is increasing in `u`, so `f` first decreases and then increases. Its
maximum occurs at `u=0` or `u=k-a`.

On the second boundary `v=k-a-u`, the denominator is the constant `k+h`.
The forward difference of the numerator is

```text
aL C(R+a+u,a-1)-Q,
```

which is increasing in `u`. That numerator is a convex sequence, so its
maximum also occurs at an endpoint. The only three distinct corners are

```text
(u,v)=(0,0), (k-a,0), (0,k-a).
```

Their values are exactly the three terms in `(CRB2)`. Since `|P|` is an
integer, `(6)` proves that floor bound. Substitution of the two post-strip
values of `kappa` gives the six exact paid ranks
`4,4,4,16,16,14`, as replayed by `verify.py`.
