# L1 Mersenne HNF m=8 order-one cubic three-double factor reduction

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_color_remainder_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the h=7 cubic color profile `2+2+2` on all four official rows

Normalize the cubic interpolant as

```text
E(W)=e_3 e(W),
e(W)=W^3+U W^2+V W+w,       e_3!=0.                 (TDF1)
```

Let the three colors be `alpha_i`, put `a_i=alpha_i/e_3`, and index the
three double fibers by `i=1,2,3`. There are elements `u_i` such that

```text
F_i(W)=W^2+u_iW+u_i^2-Uu_i+V,
y_i=u_i-U,                                             (TDF2)

L_(r,d)(W)=F_1(W)F_2(W)F_3(W),
a_i=w+(u_i^2-Uu_i+V)(u_i-U).                         (TDF3)
```

In particular, for any ordering of a representative color triple
`(alpha_1,alpha_2,alpha_3)`, every packet satisfies the scale-free equation

```text
(a_2-a_1)/(a_3-a_1)
 =(alpha_2-alpha_1)/(alpha_3-alpha_1).               (TDF4)
```

Equations (TDF2)--(TDF4), the h=7 conic, and the inherited norm-color
condition form a lower-degree exact necessary packet for `2+2+2`. Saturate
by the HNF factors, `e_3`, the three pairwise color differences, and the
quadratic-fiber resultants fixing gcd degree two.

No packet is declared empty. The profile `3+2+1`, four-or-more-color cubic
packets, higher degrees, cyclotomic converse, inner lifts, and L1 remain
open.
