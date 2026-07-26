# L1 Mersenne HNF m=16 order-zero even-quadratic exclusion

- **status:** PROVED
- **closure:** proof
- **dependencies:**
  `l1_mersenne_next_to_maximal_hypergeometric_normal_form`,
  `l1_mersenne_hnf_order_zero_quadratic_collision_router`,
  `l1_mersenne_hnf_m8_order_zero_quadratic_exclusion`,
  `l1_mersenne_hnf_m16_order_zero_single_collision_exclusion`
- **consumer:** `l1_mixed_petal_amplification`

On the official next-to-maximal order-zero row

```text
(n,p,m,h)=(131072,8191,16,15),
P_s(W)=sum_(r=0)^15 binom(s+r-1,r)W^(15-r),
P_s | W^n-1,       s notin F_p,
E_s(a)=a^(p+1)     for every root a of P_s,          (ME1)
```

there is no even quadratic colored Frobenius interpolant with at least two
repeated colors. Consequently:

```text
deg E_s != 2                                         (ME2)
```

on the `m=16,h=15` row, and degree two is empty on all five official
`m in {8,16}`, `h=m-1` order-zero endpoint rows.

This theorem does not exclude color degree at least three, the order-one HNF
chamber, the complete outer cyclotomic intersection, or the inner degree-`p`
lift. It closes no critical node, L1 numerator, or adjacent prize row.
