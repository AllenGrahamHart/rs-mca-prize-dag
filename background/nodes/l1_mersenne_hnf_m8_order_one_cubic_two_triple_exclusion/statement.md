# L1 Mersenne HNF m=8 order-one cubic two-triple exclusion

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_two_triple_reduction`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the cubic color multiplicity partition `3+3` on all four
  official `(m,h)=(8,7)` rows

Every packet in the stated chamber satisfies

```text
rd+4(d^2+3d+3)=0,       d=c-1,       r=rho*c.        (CTE1)
```

Together with the two quadratics in the dependency, this forces

```text
(2d+3)(d+3)=0.                                      (CTE2)
```

Both roots lie in the prime field. Their norms are respectively `9/4` and
`9`, neither of which belongs to `mu_8` in any official characteristic.
Consequently the complete cubic `3+3` chamber is empty on all four rows.

No other cubic color partition, higher color degree, cyclotomic converse,
inner lift, or L1 chamber is covered.
