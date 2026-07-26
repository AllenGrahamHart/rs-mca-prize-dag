# L1 Mersenne HNF m=16 order-zero single-collision exclusion

- **status:** PROVED
- **closure:** proof
- **dependencies:**
  `l1_mersenne_next_to_maximal_hypergeometric_normal_form`,
  `l1_mersenne_hnf_order_zero_quadratic_collision_router`,
  `l1_mersenne_hnf_order_zero_quadratic_collisionfree_exclusion`,
  `l1_mersenne_hnf_m8_order_zero_quadratic_exclusion`
- **consumer:** `l1_mixed_petal_amplification`

On the official next-to-maximal order-zero row

```text
(n,p,m,h)=(131072,8191,16,15),
P_s(W)=sum_(r=0)^15 binom(s+r-1,r)W^(15-r),
P_s | W^n-1,       s notin F_p,
E_s(a)=a^(p+1)     for every root a of P_s,          (MS1)
```

a quadratic `E_s` cannot have exactly one repeated color on the roots of
`P_s`.

Combining this with the quadratic collision router, collision-free exclusion,
and proved `m=8` quadratic exclusion gives the exact remaining degree-two
frontier:

```text
m=8,h=7:    empty on all four official rows;
m=16,h=15:  E_s is even and at least two distinct colors have antipodal
             repeated root pairs.                   (MS2)
```

This theorem does not exclude the retained even multi-repeat system, color
degree at least three, the order-one HNF chamber, the full outer
cyclotomic intersection, or the inner degree-`p` lift. It closes no critical
node or adjacent prize row.
