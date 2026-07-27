# L1 Mersenne HNF m=16 order-zero reciprocal elimination

- **status:** PROVED
- **closure:** exact elimination certificate
- **dependencies:** `l1_mersenne_next_to_maximal_hypergeometric_normal_form`,
  `l1_mersenne_hnf_frobenius_reciprocal_gate`
- **consumer:** `l1_mixed_petal_amplification`

On the official endpoint row

```text
(n,p,m,h)=(131072,8191,16,15),
P_s(W)=sum_(r=0)^15 binom(s+r-1,r)W^(15-r),
P_s | W^n-1,       s notin F_p,                     (MRE1)
```

there is no order-zero HNF survivor. Equivalently, the complete
`m=16,h=15` order-zero outer chamber is empty, across every colored
Frobenius degree.

Together with `l1_mersenne_hnf_m8_order_zero_reciprocal_elimination`, this
closes the order-zero chamber at all five official next-to-maximal
`m in {8,16}` endpoint rows. It does not treat order one, lower value degrees,
the inner lift, or the aggregate L1 numerator.
