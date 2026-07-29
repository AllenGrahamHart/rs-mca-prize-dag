# L1 Mersenne HNF m=8 order-one cubic two-triple reduction

- **status:** PROVED
- **dependencies:** `l1_mersenne_next_to_maximal_hypergeometric_normal_form`,
  `l1_mersenne_hnf_order_one_color_degree_barrier`,
  `l1_mersenne_hnf_m8_order_one_conic_reduction`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** cubic colored interpolants whose six reduced roots use exactly
  two colors, each with multiplicity three, on the four official
  `(m,h)=(8,7)` rows

Put `d=c-1`, `r=rho*c`, and define the conic coefficients

```text
a_1=35d^2,
b_1=14d(11d^2+27d+27),
c_1=120(d^4+4d^3+7d^2+6d+3).                       (CTR1)
```

Also define

```text
q_2=5d^2(5d+7),
q_1=130d^4+540d^3+845d^2+480d,
q_0=120d^5+744d^4+1956d^3+2724d^2+2076d+720.       (CTR2)
```

Every survivor in the stated chamber satisfies

```text
a_1r^2+b_1r+c_1=0,
q_2r^2+q_1r+q_0=0.                                  (CTR3)
```

Consequently `d` is a root of

```text
R_33(d)=(a_1q_0-c_1q_2)^2
         -(a_1q_1-b_1q_2)(b_1q_0-c_1q_1).           (CTR4)
```

The polynomial `R_33` has exact degree fourteen and leading coefficient
`-576000`. Closure of this two-triple chamber on one official row reduces
to the eight norm-color gcds

```text
gcd(R_33(X),X^(p+1)-zeta),       zeta in mu_8.       (CTR5)
```

The 32 gcd verdicts are not asserted here. No other cubic multiplicity
partition, cyclotomic converse, inner lift, or L1 chamber is covered.
