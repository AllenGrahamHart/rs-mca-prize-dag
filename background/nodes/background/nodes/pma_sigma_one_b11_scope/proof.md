# Proof - PMA sigma-one B11 scope

Because `n` and `k` are even, maximality gives

```text
M=floor((n-k+1)/2)=(n-k)/2,
b=n-(k-1)-2M=1.
```

A touched petal has one or two agreements. With `ell=2`, its deficit is
therefore in `{0,1}`, and the sum of the two smallest touched-petal deficits
satisfies `G_2<=2`. Lemma 4 in the B11 source guarantees that a non-planted
maximal-sunflower extra touches at least two petals, so `G_2` is defined.

Set `(E,V_2,V_R)=(0,2,0)`. If `d>2`, the first-match owner is `GROW`. If
`d<=2`, a member above the Johnson threshold is in `J`; every remaining
member has `G_2<=2` and is in `A2`. The later `AR` and `RES` tests require
`G_2>2`, so both are empty.

The two-anchor term specializes to

```text
binom(M,2) sum_(v=0)^2 binom(4,v) q^(2+2)
 = 11 binom(M,2) q^4.
```

The background-anchor term is zero because `V_R=0` would require
`binom(b,ell)=binom(1,2)`. Put `R=floor(sqrt(n(k-1)))`. On the official grid
`(k+1)^2<=n(k-1)`, so the first Johnson-covered agreement is `R+1`, its slack
is `lambda_J=R-k`, and its positive denominator is

```text
Delta=(R+1)^2-n(k-1).
```

This proves `(S1)` and the fourth-root formula by clearing `Delta`.

It remains to prove the field-uniform route cut. Since `q>=n+1>n`, it is
enough to compare the two-anchor term at `q=n` with `n^6`. At rate `1/8`,
`M=7n/16`, and

```text
11 M(M-1)>2n^2
  iff 27n>1232.
```

At rate `1/16`, `M=15n/32`, and

```text
11 M(M-1)>2n^2
  iff 427n>5280.
```

Both hold for `n>=2^13`. Thus

```text
11 binom(M,2) q^4
 > 11 binom(M,2) n^4
 > n^6
```

at both rates, before adding the positive Johnson term. Hence
`q_fit<n+1`. The field condition follows because a subgroup of order `n` in
`F_q^*` requires `n | q-1`. This proves the theorem.
