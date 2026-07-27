# L1 Mersenne HNF order-one Newton reciprocal reduction

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_order_one_frobenius_gate`
- **consumer:** `l1_mixed_petal_amplification`

Let `H=h-1`, and let `x_1,...,x_H` be the roots of the reduced polynomial
`L_(rho,c)`. Let `x_i^star` denote the roots of
`L_(rho_star,c_star)`. For `j>=1`, put

```text
P_j^star = sum_i (x_i^star)^(mj),
P_j^-    = sum_i x_i^(-mj).                          (NRR1)
```

Define `E_0^star=E_0^-=1` and recursively

```text
j E_j^bullet
  =sum_(a=1)^j (-1)^(a-1) E_(j-a)^bullet P_a^bullet. (NRR2)
```

Then the `j`th coefficient equation in the reduced reciprocal identity is
exactly

```text
E_j^star=E_j^-.                                      (NRR3)
```

The endpoint `j=H` is the constant equation
`Ctilde*Ctilde_star=1`. Consequently the complete reduced reciprocal
identity is equivalent to (NRR3) for `1<=j<H` plus that constant equation.
In particular, its first three
necessary equations can be constructed without
`Res_W(L,Z-W^m)`: use Newton traces only through powers

```text
m,2m,3m = 8,16,24    for (m,h,H)=(8,7,6),
m,2m,3m = 16,32,48  for (m,h,H)=(16,15,14).         (NRR4)
```

Positive traces are obtained from `L_(rho_star,c_star)` and negative traces
from the monic reciprocal of `L_(rho,c)`, using the ordinary Newton
recurrence for a degree-`H` polynomial. This is a bounded exact construction
in `m,h`.

This theorem removes the large generic resultant from the order-one attack.
It does not assert that the first three equations, or the full system, have
no solutions and does not close L1.
