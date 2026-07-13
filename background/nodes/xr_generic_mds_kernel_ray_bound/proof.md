# Proof

Write `N=R+d` and choose arbitrary lifts `b_0,b_1 in F^U` of `y_0,y_1`.
The MDS property says that the kernel `K=ker H_U` is an `[N,d]` MDS code.
In particular, restriction `K->F^T` is a bijection for every `d`-set
`T subset U`.

For each such `T` and `i in {0,1}`, there is therefore a unique `c_(i,T) in K`
such that

```text
e_T(gamma)=b_0+c_(0,T)+gamma*(b_1+c_(1,T))
```

vanishes on `T`. Call `x in U\T` persistent for `T` if both the constant and
linear coefficients of `e_T(gamma)_x` vanish.

There are at most `h-1` persistent coordinates for each `T`. Otherwise choose
`h` of them. The two vectors

```text
b_i+c_(i,T),       i=0,1,
```

would both be supported on at most

```text
N-d-h=R-h=r
```

coordinates. Their syndromes are `y_0,y_1`, contradicting genericity.

Now fix `gamma in Z` and choose a lift `w_gamma` of weight at most `r`. Its
zero set has size at least

```text
N-r=d+h.
```

For every `d`-set `T` in that zero set, uniqueness of the kernel correction
on `T` gives

```text
w_gamma=e_T(gamma).
```

At least `h` further coordinates vanish. Since at most `h-1` coordinates are
persistent for `T`, one of those zeros is nonpersistent. Charge `(gamma,T)`
to the first such coordinate in any fixed order on `U`.

For fixed `(T,x)` with `x` nonpersistent, `e_T(gamma)_x` is a nonzero affine
polynomial in `gamma`, so it vanishes for at most one slope. Every slope has
at least `C(d+h,d)` choices of `T`, while there are `C(N,d)(N-d)` possible
charges. Therefore

```text
|Z| C(d+h,d) <= C(N,d)(N-d)=C(R+d,d)R,
```

which is `(GRK)`.

## Scope

The theorem pays one fixed union chart `U`. Summing it over all possible
charts without a disjoint first-match atlas would reintroduce a binomial
factor and is not valid. It therefore advances the XR high-core leaf and the
upstream residual-ray compiler, but does not close either by itself.

In current upstream terminology, this complements
`thm:bounded-residual-kernel-ray` and `thm:single-mds-circuit-ray` in
`experimental/asymptotic_rs_mca_frontiers.tex`. The former has a
field-size factor `|F|^d`; the latter is field-independent only at one MDS
circuit. `(GRK)` is field-independent for arbitrary `d`, using the stronger
generic first-match hypothesis that XR already receives from its tangent
strip.
