# Proof

Fix a distinct transformed explanation `a` and write

```text
O(a)=|{x outside E:a(x)=r_0(x)}|,       h_a=m-O(a).
```

If `O(a)>=m`, choose an `m`-set of those outside coordinates.  There
`r_1=b`, so `(a,b)` simultaneously explains the received pair on that set,
contrary to same-support pair noncontainment.  Hence `h_a>=1`.

Every slope assigned to `a` has at least `m` total agreements.  At most `e`
of them lie in `E`, while all outside agreements are counted by `O(a)`.
Thus `O(a)+e>=m` and `h_a<=e`.

On a coordinate `x in E`, agreement at slope `gamma` is equivalent to

```text
(a(x)-r_0(x))/q(x)=gamma.
```

The slope fibers of this ratio map are disjoint.  A slope assigned to `a`
needs at least `h_a` inside agreements, so `a` owns at most
`floor(e/h_a)` selected slopes.

Let `n_h` count distinct selected explanations having exact deficit `h`,
and let `N_h=sum_(i<=h)n_i`.  Every explanation counted by `N_h` agrees
with `r_0` outside `E` on at least `m-h=d+K-h` coordinates.  After
puncturing `E`, these explanations lie in an affine flat of dimension at
most `r` inside the Reed-Solomon row

```text
n'=R+K-e,       K'=K,       agreement threshold=d+K-h.
```

The affine-span list compiler gives

```text
N_h <= floor(C(n'-K'+r,r)/C(d-h+r,r))
    = B_h.                                             (1)
```

The weights `floor(e/h)` are nonincreasing and the cumulative caps `B_h`
are nondecreasing.  Subject only to `(1)`, the weighted sum is maximized by
saturating every cumulative cap, namely `n_h=B_h-B_(h-1)`.  Therefore

```text
|Z| <= sum_h n_h floor(e/h)
     <= sum_h (B_h-B_(h-1)) floor(e/h),
```

which is `(HF1)`.  Exact integer evaluation proves each printed paid prefix
and its adjacent first-unpaid value.
