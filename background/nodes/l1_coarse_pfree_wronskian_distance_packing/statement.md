# L1 coarse p-free Wronskian distance packing

- **status:** PROVED
- **role:** give an arbitrary-target max-fiber bound for the coarse p-free
  prefix map
- **consumer:** `l1_mixed_petal_amplification`

## P-free collision distance

Let `F` be a finite field of characteristic `p`, let `H subset F` have `n`
distinct elements, and fix `1<=d<=a<=n`. For an `a`-set `A subset H`, put

```text
S_j(A)=sum_(x in A) x^j,
Phi_free(A)=(S_j(A):1<=j<=d, p does not divide j).    (PWD1)
```

If distinct `A,B` lie in one fiber of `Phi_free`, write

```text
C=A intersect B,       X=A\C,       Y=B\C,
|X|=|Y|=t.
```

Then

```text
t>=tau:=ceil((d+2)/2),
|A intersect B|<=a-tau.                              (PWD2)
```

The half-depth loss is sharp: over `F_4` in characteristic two, the two
sets `{0,1}` and `{alpha,alpha+1}` have the same p-free depth-two prefix and
attain `t=tau=2`.

## Packing consequence

Put

```text
s=a-tau+1.                                           (PWD3)
```

Every `s`-subset of `H` belongs to at most one member of a fixed coarse
p-free fiber. Therefore

```text
max_z |Phi_free^(-1)(z)|
 <=floor(binom(n,s)/binom(a,s)).                     (PWD4)
```

For the scalar L1 locator prefix, `a=k+d`, so

```text
s=floor((a+k)/2),
max_z |Phi_free^(-1)(z)|
 <=floor(binom(n,floor((a+k)/2))
          /binom(a,floor((a+k)/2))).                 (PWD5)
```

Put `r=n-a`. If `s>=n/2`, then

```text
binom(n,s)/binom(a,s)
 =product_(i=0)^(r-1) (n-i)/(n-s-i) >=2^r.          (PWD6)
```

Since every official field has `q<2^256`, its finite numerator
`floor(q/2^128)` is below `2^128`. Therefore `(PWD4)` cannot by itself
certify an official finite payment whenever

```text
a+k>=n,       n-a>=128.                              (PWD7)
```

This diagnoses the strength of the bound; it is not a lower bound on the
actual fiber.

## Scope

This is an explicit arbitrary-target max-fiber bound and needs no checkpoint
union or structured subtraction. Its packing cap can remain exponential in
the active linear band, so it does not prove row-sharp Q, the Pade-graph
intersection, or L1. Future work should apply stronger shift-pair structure
only on rows where `(PWD4)` exceeds the allocated payment.

Do not read `(PWD2)` as an improvement to an exact mixed locator-prefix or
fixed-cofactor Pade shell. Equality of the full depth-`d` locator prefix gives
the stronger elementary bound `t>=d+1` when `a=k+d`, since the difference of
the two monic locators has degree at most `k-1`. The half-depth theorem is for
the larger coarse p-free fiber after Frobenius checkpoints are forgotten;
the `F_4` sharpness fixture shows why full-prefix distance cannot be imported
there.
