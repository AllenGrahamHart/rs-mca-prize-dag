# L1 Mersenne HNF m=8 order-zero quadratic exclusion

- **status:** PROVED
- **closure:** proof
- **dependencies:**
  `l1_mersenne_next_to_maximal_hypergeometric_normal_form`,
  `l1_mersenne_hnf_order_zero_quadratic_collision_router`,
  `l1_mersenne_hnf_order_zero_quadratic_collisionfree_exclusion`
- **consumer:** `l1_mixed_petal_amplification`

On each of the four official next-to-maximal order-zero rows

```text
(n,p,m,h) in {
  (65536,       8191,       8,7),
  (1048576,     131071,     8,7),
  (4194304,     524287,     8,7),
  (17179869184, 2147483647, 8,7)
},
```

retain

```text
P_s(W)=sum_(r=0)^7 binom(s+r-1,r)W^(7-r),
P_s | W^n-1,       s notin F_p,
E_s(a)=a^(p+1)     for every root a of P_s.          (MQ1)
```

Then

```text
deg E_s != 2.                                         (MQ2)
```

Together with the constant/linear exclusion, the colored Frobenius degree in
the `m=8,h=7` order-zero chamber is at least three.

This theorem does not treat the `m=16,h=15` quadratic branches, degree at
least three, the order-one HNF chamber, the original cyclotomic intersection
outside `(MQ1)`, or the inner degree-`p` lift. It is an exact endpoint
stratum deletion, not a close of L1.
