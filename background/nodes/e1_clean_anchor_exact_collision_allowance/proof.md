# Proof

Write the quotient roots as `h=N/2` antipodal pairs. An `ell`-subset has `t`
singleton pairs, each with one of two signs, and `u=(ell-t)/2` full pairs.
Moving the `u` full pairs among the remaining `h-t` positions does not change
`e_1`, since each full pair sums to zero. The characteristic-zero rigidity
theorem says these moves are all the equal-value relations. Thus, for each
feasible pair `(u,t)`, there are `binom(h,t)2^t` classes. Summing gives the
displayed formula for `K`.

Global sign sends a class value to its negative. It does not identify the two
classes. This is why the formula is not divided by two. For example,
`A_2(16,9)=3280=(3^8-1)/2`, in agreement with `thm:exactcount`.

Now reduce the `K` characteristic-zero values into the actual finite slope
field and partition the classes by their reduced values. For a fiber of size
`r>=1`, collapsing that fiber loses `r-1` values and creates `binom(r,2)`
unordered colliding pairs. Since

```text
r-1 <= r(r-1)/2,
```

summing over fibers gives `K-L<=P`. If `P<=K-B*-1`, then

```text
L >= K-P >= B*+1 > B*.
```

The canonical quotient locator construction does not need the qfloor norm
threshold to show that each realized reduced `-e_1` value is a bad slope. The
threshold is used only to prove that distinct characteristic-zero classes do
not collide after reduction. Hence the inequality above is a valid direct
value-set `V` compiler below that threshold, provided the row packet pins the
ambient slope field, quotient embedding, endpoint, and owner.

Every quotient root lies in `B=F_p(Q)`, and elementary symmetric functions of
those roots also lie in `B`. Thus the reduced E1 image is a subset of `B` and
has size at most `|B|`. If `|B|<=B*`, it cannot contain more than `B*` slopes.
This proves the generated-field route cut without an injectivity assumption.

For the six candidate predecessors, `N=n/(m-k)` gives `256,256,512` at rates
`1/4,1/8,1/16`, and `ell=rho N+1` gives `65,33,33`. Substitution into the exact
class formula and then `g_max=K-B*-1` gives the statement table. All arithmetic
is integral and is replayed twice independently.
