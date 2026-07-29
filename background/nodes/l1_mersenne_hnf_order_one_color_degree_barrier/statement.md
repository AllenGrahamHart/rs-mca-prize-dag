# L1 Mersenne HNF order-one color-degree barrier

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_order_one_frobenius_gate`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the four official `(m,h)=(8,7)` rows and the official
  `(m,h)=(16,15)` row

Let `H=h-1` and let `E(W)` be the rootwise colored Frobenius interpolant on
the `H` reduced roots. If `E` is nonconstant of degree `d`, then

```text
H<=d(d+1).                                           (CDB1)
```

Consequently every actual order-one survivor satisfies

```text
(m,h)=(8,7):       deg E=0 or deg E>=2;
(m,h)=(16,15):     deg E=0 or deg E>=4.              (CDB2)
```

Combining the first line with
`l1_mersenne_hnf_m8_order_one_constant_color_exclusion` gives `deg E>=2`
on every live `h=7` packet. The second line closes the linear, quadratic,
and cubic color strata at `h=15`.

This theorem does not exclude the constant `h=15` chamber, any degree at or
above the displayed thresholds, the cyclotomic converse, inner lifts, or
other L1 chambers.
