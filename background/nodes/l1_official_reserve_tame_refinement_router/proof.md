# Proof - L1 official-reserve tame-refinement router

## 1. Characteristic and order

Since the even integer `n` divides `p^f-1`, the characteristic `p` is odd.
For an odd integer `p`, put

```text
c=max(v_2(p-1),v_2(p+1)).
```

The standard order formula on powers of two gives

```text
ord_n(p)>=n/(p+1).                                      (1)
```

Indeed, if `n<=2^c`, the right side is at most one. If `n>2^c`, lifting the
exponent gives `ord_n(p)=n/2^c`, and `2^c<=p+1`. Since
`ord_n(p)|f`, equation `(1)` also gives

```text
f>=n/(p+1).                                             (2)
```

For `p=3` and `p=5`, the exact order is `n/4` when `n>=8`. Under `(OR1)`,
this would give

```text
log_2(p^f)>=(n/4)log_2(p)>=2048 log_2(3)>256,
```

a contradiction. Therefore

```text
p>=7.                                                    (3)
```

## 2. Canonical reserve cutoff

Let `L=log_2(p^f)`. Since `n|p^f-1`, one has `L>log_2 n>=13`. Put

```text
t=ceil(5n/(4L)).                                         (4)
```

The inequalities `k<=n/2`, `n>=2^13`, and `L>=13` imply `k+t<=n`.
Moreover,

```text
tL>=5n/4>=(1+eta)n
   >=(1+eta)log_2 binom(n,k+t).                          (5)
```

Thus `t` is admissible in `(OR3)` and `sigma_0<=t`. Using `L=f log_2 p`
and `(2)` gives

```text
ell_0<=ceil(5n/(4f log_2 p))+1
     <=ceil(5(p+1)/(4 log_2 p))+1.                      (6)
```

For every real `x>=7`,

```text
5(x+1)/(4 log_2 x)<=x-2.                                (7)
```

To check this, multiply by `ln x` and consider

```text
g(x)=(x-2)ln x-(5/4)(x+1)ln 2.
```

Direct substitution gives `g(7)>0`, while

```text
g'(x)=ln x+1-2/x-(5/4)ln 2>0
```

for `x>=7`. Combining `(3)`, `(6)`, and `(7)` yields

```text
ell_0<=ceil(p-2)+1=p-1<p.                               (8)
```

The original `sigma` satisfies the weaker `eta` reserve, so minimality gives
`sigma_0<=sigma`. The exact-shell decomposition of
`l1_exact_shell_prefix_hankel_bridge` makes `ImgFib_U(s)` the set of
degree-below-`k` codewords with at least `s` agreements. This proves `(OR5)`.

## 3. No wild fixed-petal divisor

For `s|ell_0`, the outer degree `r=ell_0/s` satisfies `1<=r<p` by `(8)`.
Hence `p` does not divide `r`, exactly the tame guard of
`l1_tame_fixed_petal_refinement_census`. Applying that theorem at every
source petal and divisor proves `(OR6)` and removes the wild fixed-petal
branch.
