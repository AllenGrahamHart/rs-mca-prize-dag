# Proof

We first use a matroid lemma.

**Cogirth basis lemma.** A rank-`a` matroid of cogirth at least `c>=1` has at
least

```text
C(c+a-1,a)
```

bases.

Delete loops, which changes neither rank, bases, nor cogirth. The claim is
clear for `a=0`, `a=1`, or `c=1`. Otherwise there is no coloop, since a coloop
is a one-element cocircuit. Choose any element `x`. Deletion has rank `a` and
cogirth at least `c-1`; contraction has rank `a-1` and cogirth at least `c`.
Every basis either avoids or contains `x`, so induction and Pascal's identity
give

```text
#bases(M)
 >= C(c+a-2,a)+C(c+a-2,a-1)
  = C(c+a-1,a).
```

Now return to `A`. Choose `b_0 in A` with syndrome `y_0` and `q in V` with
`Hq=y_1`. Fix a basis `T` of the coordinate matroid of `K`. Restriction
`K->F^T` is bijective, so there are unique `k_(0,T),k_(1,T) in K` for which

```text
e_T(gamma)=b_0+k_(0,T)+gamma(q+k_(1,T))
```

vanishes on `T`.

Call a coordinate outside `T` persistent when both the constant and linear
coefficients of `e_T(gamma)` vanish there. There are at most

```text
|U|-r-a-1
```

persistent coordinates. Otherwise `T` together with `|U|-r-a` persistent
coordinates would make both `b_0+k_(0,T)` and `q+k_(1,T)` supported on at
most `r` coordinates, contradicting genericity.

Fix `(gamma,e) in P` and let `Z_e` be its zero set. Restriction `K->F^Z_e`
has rank `a`: a nonzero vector in its kernel would be a codeword supported on
at most `r` coordinates, contrary to `Delta>r`. Moreover, every nonzero word
of the restricted code `K|Z_e` has weight at least

```text
Delta-(|U|-|Z_e|) >= Delta-r.
```

Thus its coordinate matroid has cogirth at least `Delta-r`. The lemma gives
at least `C(Delta-r+a-1,a)` bases `T subset Z_e`.

For every such `T`, uniqueness of the kernel correction gives
`e=e_T(gamma)`. Besides `T`, at least `|U|-r-a` further coordinates vanish.
At least one is nonpersistent. Charge `(gamma,e,T)` to the first such
coordinate in a fixed order. For fixed `(T,x)` with `x` nonpersistent, the
coordinate `e_T(gamma)_x` is a nonzero affine polynomial in `gamma`, so it
vanishes for at most one slope; the corresponding error is unique as well.

There are at most `C(|U|,a)` possible bases and at most `|U|-a` charge
coordinates. Comparing lower and upper charges proves `(ACG)`.
