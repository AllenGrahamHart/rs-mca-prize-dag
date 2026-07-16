# Proof - PMA sigma-one dyadic near-coset owner

Fix a scale `L` and one `K_L`-coset `B`. If `e=|B\A_P|<=s`, record the exact
missed set `E=B\A_P`. Put `q=max(0,k-L+e)`. Listedness gives

```text
|A_P\B| >= a-(L-e) >= k+1-L+e.
```

When `q>0`, this is at least `q+1`; when `q=0`, no outside point is needed.
Record the first `q` outside agreements as `J`. The set

```text
(B\E) union J
```

contains `L-e+q>=k` agreement points. Thus `(L,B,E,J)` determines `P` by
Reed-Solomon uniqueness. There are `n/L` cosets, `binom(L,e)` missed sets,
and at most `binom(n-L,q)` outside records, proving `(L-CORE)`. Including `L`
and the coset in a fixed total order and selecting the first qualifying pair
makes the union over scales injective as well.

Now take an official row `n=2^j`, `13<=j<=44`, put

```text
s_n=floor(n/(32j)),
```

and suppose `L>=k-s_n`. Then

```text
0<=q=max(0,k-L+e)<=2s_n.
```

If `q>n-L`, listedness would require at least `q+1` outside agreements in a
set of size `n-L`, so that cell is empty. For every nonempty cell there are at
most `j+1` dyadic scales, `s_n+1` values of `e`, and

```text
n/L<=n,
binom(L,e)<=n^s_n,
binom(n-L,q)<=n^(2s_n).
```

Therefore the complete owner count is at most

```text
(j+1)(s_n+1)n^(3s_n+1).                               (1)
```

Since `j+1<n`, `s_n+1<n`, and `3j<=n/64` for every `j>=13`, while
`3js_n<=3n/32`, expression `(1)` is strictly smaller than

```text
n^3 2^(3n/32) <= 2^(7n/64).                           (2)
```

Write `N=n/2`, `h=k/2+1`, `m=min(h,N-1-h)`, and `r=n/32`. Across all four
rates, `r<=m<=(N-1)/2`. Binomial monotonicity and the product formula give

```text
Q_2(k+2)=binom(N-1,m)>=binom(N-1,r)
          = product_(i=0)^(r-1) (N-1-i)/(r-i)
          > 15^r.                                      (3)
```

Indeed every factor in the product is at least `(N-1)/r=16-32/n>15`.
Finally,

```text
2^(7n/64) < 15^(n/32)
```

is exactly the integer inequality `2^7<15^2` raised to the power `n/64`.
Combining `(2)` and `(3)` proves `(FINITE-COS)`. The class is applied after
`QOWN_per`, so the two owners are disjoint. Adding the sharper periodic count
and using `Q_2>=1` gives the same
`8(1+2^-690)Q_2` combined ceiling as in the index-two specialization.
