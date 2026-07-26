# L1 Mersenne HNF order-zero quadratic collision-free exclusion

- **status:** PROVED
- **closure:** proof
- **dependencies:** `l1_mersenne_next_to_maximal_hypergeometric_normal_form`,
  `l1_mersenne_hnf_order_zero_linear_color_exclusion`
- **consumer:** `l1_mixed_petal_amplification`

Retain an official next-to-maximal order-zero row and its colored interpolant:

```text
n=m(p+1),       (m,h) in {(8,7),(16,15)},
P_s(W)=sum_(r=0)^h binom(s+r-1,r)W^(h-r),
P_s | W^n-1,    s notin F_p,
E_s(a)=a^(p+1)  on the roots of P_s.                 (QCF1)
```

If `deg E_s=2`, then `E_s` is not injective on the roots of `P_s`:

```text
there are distinct roots a,b with E_s(a)=E_s(b).    (QCF2)
```

Combining this theorem with
`l1_mersenne_hnf_order_zero_quadratic_collision_router` gives the exact
quadratic color-multiplicity frontier:

```text
m=8,h=7:   exactly one repeated color;
m=16,h=15: exactly one repeated color, or an even quadratic with at least
            two antipodal repeated pairs.           (QCF3)
```

This theorem does not exclude those retained quadratic systems, any higher
color degree, the order-one chamber, cyclotomic candidates outside the
printed implication, or an inner lift.
