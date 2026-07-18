# Exact-integer Johnson safe anchor for rate-half lists

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **scope:** ordinary lists for any Reed-Solomon evaluation code

Let `C=RS[F,D,k]` have length `n`, let `B>=1` be an integer, and let

```text
L_1(a)=max_u #{c in C:agr(c,u)>=a}.
```

Put `ell=B+1`. For an integer `a` with `k<=a<=n`, write

```text
ell*a=n*d+r,       0<=r<n,
J_(n,k,B)(a)=n binom(d,2)+r*d-binom(ell,2)(k-1).   (IJ1)
```

Then

```text
J_(n,k,B)(a)>0  implies  L_1(a)<=B.                (IJ2)
```

The function in `(IJ1)` is nondecreasing in `a`, is positive at `a=n`, and
therefore defines the row-computable safe anchor

```text
a_IJ(n,k,B)=min {a in [k,n]:J_(n,k,B)(a)>0}.       (IJ3)
```

It is computable by `O(log n)` exact bigint comparisons, and

```text
L_1(a_IJ(n,k,B))<=B.                               (IJ4)
```

For the prize-max rate-half row, set

```text
n=2^41,       k=2^40,       B*=floor(q/2^128),
2^128<q<2^256.
```

Then `1<=B*<=2^128-1`, and the actual adjacent crossing satisfies

```text
k+2^34 <= a_L(C) <= a_IJ(n,k,B*).                  (IJ5)
```

At the two useful ends,

```text
a_IJ(n,k,B*)=3n/4                         for B*=1,2,3,
a_IJ(n,k,B*)=floor(sqrt(n(k-1)))+1        for
                    B*>=332114441762.               (IJ6)
```

This theorem proves a safe bracket, not the adjacent location. It makes no
claim that `a_IJ-1` is unsafe.
