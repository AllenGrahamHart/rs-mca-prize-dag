# PMA rate-half source cross-ratio fiber reduction

- **status:** PROVED
- **consumer:** `petal_mixed_amplification`
- **role:** reduce the aligned tail certificate to one normalized source-label fiber

## Statement

Use the notation of `pma_ratehalf_source_aligned_gcd_excess`. Let
`RS(C,K_0)` denote the degree-`<K_0` core code.

### Affine source-label normalization

If the three source labels are changed by

```text
c_i' = alpha c_i+beta,       alpha!=0,              (XR1)
```

then the associated core lists are in bijection and have identical agreement
sets. In particular every distinct label triple is equivalent to

```text
(c_1,c_2,c_3)=(0,1,lambda),
lambda=(c_3-c_1)/(c_2-c_1) notin {0,1}.              (XR2)
```

For fixed core and petals, the three-dimensional source quotient code from
the predecessor intersects `RS(C,K_0)` in exactly the one-dimensional
constant-label line. Hence its image modulo `RS(C,K_0)` is two-dimensional,
and (XR2) is its projective one-parameter family.

### The small exceptional set

Let `(P_2,Y_2)` and `(P_3,Y_3)` be the source division pairs for label vectors
`(0,1,0)` and `(0,0,1)`. Then

```text
P_2=L_1L_3R_2,       P_3=L_1L_2R_3,
deg R_2,deg R_3<ell,       R_2R_3!=0.               (XR3)
```

The normalized source numerator is `P_*(lambda)=P_2+lambda P_3`. On the core
define

```text
B_3={x in C:P_3(x)=0}={x in C:R_3(x)=0}.
```

Then

```text
|B_3|<=ell-1.                                        (XR4)
```

### Residual lambda-fiber certificate

Let three contributors `H_i` have agreement sets

```text
S_i={x in C:P_*(lambda)(x)+L(x)H_i(x)=0},
|S_i|>=m.
```

Give a point of multiplicity `r_x=#{i:x in S_i}` overlap weight
`max(0,r_x-1)`. The total weight is the aligned gcd bonus from the predecessor.
After removing `B_3`, the remaining weighted incidences have size at least

```text
2(K_0-1)+3a-2(ell-1)=2b+3a-2.                       (XR5)
```

At every remaining overlap point, the common contributor value `h(x)` votes
for the unique source cross-ratio

```text
lambda=-(P_2(x)+L(x)h(x))/P_3(x).                   (XR6)
```

Thus any three-contributor tail cell forces at least `2b+3a-2` weighted
nonexceptional incidences in one normalized `lambda` fiber. If no such fiber
certificate exists, the complete three-petal tail is bounded by `8n` per
carried source.

## Scope

This theorem does not bound the fiber in (XR6). It reduces three free source
labels to one projective cross-ratio and proves a positive, row-explicit
nonexceptional incidence requirement. The exceptional contribution uses
overlap weight two per point; charging it only once is invalid.
