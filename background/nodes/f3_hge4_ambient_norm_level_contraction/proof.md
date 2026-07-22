# Proof - HGE4 ambient-prime exact-level contraction

## 1. The inherited norm packet

Fix a hypothetical primitive exact-level pair of width `h`. The cyclotomic
norm construction in `f3_hge4_cyclotomic_norm_quarter_width_exclusion`
produces a nonzero `z in Z[zeta_m]`. With

```text
u=floor(h/2),
```

the first `h-1` power-sum identities and complete splitting of `p` give

```text
p^u divides |Norm(z)|.                                (1)
```

Odd-frequency Parseval gives, at every width,

```text
|Norm(z)|<=D^(m/4),       D<=4h.                      (2)
```

The nonzero assertion is load-bearing: otherwise odd Fourier inversion
would make both supports antipodally invariant, contrary to exact-level
primitivity.

## 2. Exact defect/swap gate

Retain the support-difference notation from the norm packet, put `M=m/2`,
and define

```text
g_t=f_t-f_(t+M),       q_t=f_t+f_(t+M),
D=sum_t g_t^2,         L=sum_t q_t^2.                (3)
```

Then `D+L=4h`. The consecutive even moments give a Vandermonde system for
`q`. If `q!=0`, the proved defect lemma gives

```text
L>=v_h=floor((h-1)/2)+2,
D<=4h-v_h.                                           (4)
```

Under `(ALC2-exact)`, equations `(1)--(2)` and `(4)` imply

```text
|Norm(z)|>=p^u>n^(2u)>=(4h-v_h)^(m/4)>=D^(m/4)
            >=|Norm(z)|,
```

a contradiction.

If `q=0`, the antipode exchanges the two supports. The primitive swap router
makes `h` odd, so `2u=h-1`. The one-side swap norm packet gives the necessary
inequality

```text
p^u<=h^(m/4).                                        (5)
```

But `4h-v_h>h` for `h>=4`, and `(ALC2-exact)` contradicts `(5)` through

```text
p^u>n^(2u)>=(4h-v_h)^(m/4)>h^(m/4).
```

This proves the exact gate for every lower-quarter width.

## 3. Closed-form ambient cutoff

Assume first that

```text
c_(n,m)<=h<m/4.                                      (6)
```

Put `C=ceil(mr/(8s))`, so `c_(n,m)=2C`. The displayed assumption gives
`u>=C`, and therefore

```text
n^(2u)=2^(2su)>=2^(mr/4)=m^(m/4).                    (7)
```

Since `p` is prime and `n^2` is composite, `p>=n^2` means `p>n^2`. Also
`4h<m` in `(6)`. Equations `(1)--(2)` and `(7)` give the impossible chain

```text
|Norm(z)|>=p^u>n^(2u)>=m^(m/4)>(4h)^(m/4)>=|Norm(z)|.
```

Thus no primitive pair exists in the lower-quarter interval `(6)`.

For `m/4<=h<m/3`, the quarter-width dependency already proves emptiness,
including its delicate equality and first odd width. Combining the two
intervals proves `(ALC3)`.

## 4. Cutoff arithmetic

Because `r<=s` and `m/8` is an integer,

```text
ceil(mr/(8s))<=m/8,
```

so `c_(n,m)<=m/4`. When `r=s`, equality is exact. This proves the top-level
scope statement. If `r<s`, then on `13<=s<=41`, `4<=r`,

```text
m(s-r)>=16(s-4)>8s.
```

(For fixed `s`, the ratio of consecutive values is
`2(s-r-1)/(s-r)>=1` through `r=s-2`, so the minimum is at `r=4`.) Hence
`mr/(8s)<m/8-1`, so
`c_(n,m)<=m/4-2`. The complement-third dependency deletes `h>=m/3`; together
with `(ALC3)` this proves `(ALC4)` and the strict proper-level contraction.

All printed cell counts are finite integer sums. For each ambient exponent
`s` and exact-level exponent `r`, the number of newly deleted widths in the
prize scope `h>=4` is

```text
max(0,m/4-max(4,c_(n,m))).                           (8)
```

Summing `(8)` over `13<=s<=41` and `4<=r<=s` gives
`55,050,457,488`; fixing `s=41` gives `26,817,356,728`. Direct substitution
in `(ALC2)` gives `(ALC5)` and the two equal width losses. QED.
