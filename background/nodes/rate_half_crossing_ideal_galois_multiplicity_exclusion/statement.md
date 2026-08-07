# Ideal-level Galois multiplicity exclusion

Let `n=2^m`, `h=n/2`, `K=Q(zeta_n)`, and `2<=w<=n`.  For
`S subset Z/n` of size `r`, set

```text
x_s(S) = sum_(i in S) zeta_n^(si),
I_(S,w) = (x_1,...,x_(w-1)) subset O_K.
```

For an odd prime `p`, let `Z_w(p)` be the closure of
`{1,...,w-1}` under multiplication by `p` modulo `n`, and let
`Z_w^odd(p)` be its odd elements.  Define the ordered antipodal count

```text
a_(n/2)(S) = #{(i,j) in S^2 : i-j=n/2 mod n}.
```

## The theorem

If `x_1(S) != 0` and `p` divides the absolute ideal norm `N(I_(S,w))`, then

```text
p^|Z_w^odd(p)| divides |N_(K/Q)(x_1)|,                         (IG1)
|N_(K/Q)(x_1)|^2 <= (r-a_(n/2)(S))^h,                         (IG2)
|Z_w^odd(p)| log_2 p
  <= (n/4) log_2(r-a_(n/2)(S)).                               (IG3)
```

In particular, since
`|Z_w^odd(p)|>=ceil((w-1)/2)`, every such accident satisfies

```text
ceil((w-1)/2) log_2 p <= (n/4) log_2 r.                       (IG4)
```

Thus strict reversal of `(IG4)` excludes every nonperiodic accident at that
specific base characteristic `p`.

## Exact periodic reduction

If `S` is invariant under addition by `n/2^a`, write it as the full lift of
`S_a subset Z/(n/2^a)`.  Put

```text
n_a=n/2^a,  r_a=r/2^a,
w_a=floor((w-1)/2^a)+1.
```

All moments whose indices are not divisible by `2^a` vanish, the remaining
moments are `2^a` times the moments of `S_a`, and the odd-prime support of
`N(I_(S,w))` is exactly that of the reduced ideal.  Consequently every
nonstructural periodic stratum is excluded if

```text
ceil(floor((w-1)/2^a)/2) log_2 p
  > (n/2^(a+2)) log_2(r/2^a)                                  (IG5-a)
```

at that stratum.  If `w=2^v`, exclusion at `a=0` implies `(IG5-a)` at every
`a<v`; strata `a>=v` have no surviving moment conditions and are the
structural coset-union family.

## Prize benchmark

For the formal substitution `n=2^41`, `r=2^40-w`, and `log_2 p=256`, the
first excluded integer is

```text
w_0=170,752,922,588;
```

the last unexcluded integer is `170,752,922,587`.  This is 71.1641% of the
integer bracket `[2^34,2^39]`.  The percentage is a near-256-bit
**characteristic** benchmark.  It is not uniform over rows with large
`q=p^e` and smaller `p`.
