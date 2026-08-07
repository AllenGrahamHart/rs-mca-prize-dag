# Rate-half FPC5 uniform guarded codimension

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t2_payment`

Fix one rate-half `M=4,t=2` source, one touched pair, and a core defect

```text
d=ell+s,       0<=s<ell.
```

Let `R` be a fixed background agreement set of size `r`. The list threshold
and source geometry give

```text
s<=r<=b<ell.                                           (UC1)
```

Write `L_R` for its locator. The guarded cofactor kernel is

```text
c_2L_1A_1 == c_1L_2A_2 (mod L_R),
deg A_i<=s,                                            (UC2)
```

with locator image

```text
F=(L_1A_1-L_2A_2)/(c_2-c_1).                         (UC3)
```

Projection to `F` is injective, and

```text
dim V_F <= 2s+2-min(r,s+1).                           (UC4)
```

Therefore every nonempty monic degree-`d` chart has affine locator
codimension at least

```text
(d+1)-dim V_F
  >= ell-s-1+min(r,s+1)
  >= ell-1.                                           (UC5)
```

More precisely:

```text
r=s:       dim V_F=s+2 exactly,       codim=ell-1;
r>=s+1:    dim V_F<=s+1,              codim>=ell.     (UC6)
```

Thus the sharp full-background cell is one member of a uniform theorem: no
fixed exact-background cell has codimension below `ell-1`.

## Aggregate interface

Let `V_s` be the unguarded two-petal locator image and let `W_F` be the unique
numerator paired with `F`. Without choosing `R`, all exact contributors at
this `s` inject into the single root-rich split-pair locus

```text
F in P(V_s) intersect D_(ell+s)(C),
|{x in B:W_F(x)=0}|>=s,                               (UC7)
```

followed by candidate-wise primitivity, exact background equality,
untouched-petal nonagreement, and first ownership. The exact set
`R=Z_B(W_F)` is uniquely determined by `(F,W_F)`, so the cells are disjoint.
Nevertheless, summing a polynomial flatness bound independently over the
`binom(b,r)` possible sets `R` is not a valid aggregate payment. Closure
requires a direct root-rich split-pair count or a first-owner compression of
the realized background sets.
