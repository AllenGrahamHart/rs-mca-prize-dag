# L1 Mersenne HNF m=16 order-one constant-color exclusion

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m16_order_one_constant_color_reduction`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the official `(m,h,p)=(16,15,8191)` next-to-maximal row

Both gcds in (CCR6) of the dependency are one:

```text
gcd(S(S^2-4)(S^2-2)(S^4-4S^2+2),
    28S^2+29S+370)=1,

gcd(S(S^2-4)(S^2-2)(S^4-4S^2+2),
    28S^2+27S-1202)=1                         in F_8191[S]. (CCE15)
```

Therefore the complete `h=15` constant-color chamber is empty. Combined
with `l1_mersenne_hnf_order_one_color_degree_barrier`, every remaining
nonconstant colored interpolant at `h=15` has degree at least four.

This does not exclude degrees four through thirteen, prove the cyclotomic
converse, construct an inner lift, or promote L1.
