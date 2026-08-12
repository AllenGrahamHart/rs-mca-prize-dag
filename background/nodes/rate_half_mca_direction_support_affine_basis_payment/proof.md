# Proof

Apply the codeword-direction gauge and choose an `r`-dimensional affine
codeword flat containing the transformed explanations.  In the parameter
space of the support-wise affine-span proof, the incident normal at
coordinate `x` is

```text
v_x=(q(x),-c_1(x),...,-c_r(x)).
```

Let `z` be the number of zero normals.  Every zero normal lies outside
`E=supp(q)`.  Of the `n-z` active coordinates, exactly `n-e-z` therefore
lie outside `E`.  All normals at those outside coordinates have zero first
component, so no `(r+1)` of them span the `(r+1)`-dimensional parameter
space.  The number of possible ordered full bases is consequently at most

```text
(n-z)_(fall r+1)-(n-e-z)_(fall r+1).                 (1)
```

The lower bound on incident bases at every selected slope is unchanged.
Writing `z=g+c`, the proof of the support-wise compiler therefore gives

```text
|Z| <= Q(g,c) p(z),

Q(g,c)=(n-z)_(fall r+1)/((m-g)(d+c)_(rise r)),
p(z)=1-(n-e-z)_(fall r+1)/(n-z)_(fall r+1).          (2)
```

The existing endpoint argument proves `Q(g,c)<=M(K,r)` for every legal
`g,c`, with `z<=K-r`.  For `x>=e+r`, each factor

```text
(x-e-i)/(x-i)=1-e/(x-i),       0<=i<=r,
```

increases with `x`.  Hence `p(z)` increases with `z`, and

```text
p(z)<=p(K-r)
    =1-(R+r-e)_(fall r+1)/(R+r)_(fall r+1)
    =P(R,r,e).
```

Combining this with `(2)` proves `(AB1)`.  Minimum-lift interpolation gives
`e<=R`, so every factor used above is nonnegative.

For the uniform table, the first term of `M(K,r)` has no interior maximum
as `K` ranges from `r` to `R`; this is the exact one-turn calculation in the
gauge-rank router.  At `K=r` it equals the fixed second term.  Exact
comparison shows that the `K=R` term owns every displayed rank, so evaluating
`(AB1)` there bounds all shortened dimensions.  Finally,

```text
(R+r-e)_(fall r+1)-(R+r-e-1)_(fall r+1)
 =(r+1)(R+r-e-1)_(fall r)>0
```

for `e<R`, proving support monotonicity and making each adjacent integer
comparison a certificate for the whole printed prefix.
