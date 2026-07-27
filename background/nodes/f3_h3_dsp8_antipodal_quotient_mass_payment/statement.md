# DSP8 antipodal quotient-mass payment

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependencies:** `f3_h3_distance_six_support_overlap_payment`,
  `f3_affine_coset_pair_mattarei_bound`,
  `f3_h3_dsp8_primitive_shift_pair_adapter`

Use the `E=6`, `P(t)>=25` interface. Let

```text
S_A=sum_(t antipodal, P(t)>=25) R(t),
Q_n=(n-1)(n-2).
```

Then

```text
S_A <(C_M/2)(n-2)n^(2/3),       C_M=3*2^(-2/3).    (AQM1)
```

If `O_6,25^0,O_6,25^A` are the support-overlapping distance-six
moments, their class-weighted payment sharpens to

```text
O_6,25^0+(17/10)O_6,25^A
 <=6Q_n+(38/5)S_A.                                  (AQM2)
```

Write `K_25^0,K_25^A` for the decorated primitive shift-pair counts in the
proved adapter. The C36' consumer therefore follows from the target-sensitive
bound

```text
10K_25^0+17K_25^A+152S_A
 <=750n^2-375Q_n.                                   (AQM3)
```

In particular, the target-independent estimate

```text
100(10K_25^0+17K_25^A) <=36781n^2                  (AQM4)
```

is sufficient on every official row. Its effective correlation constant is
`36781/100=367.81`, replacing `29031/80` and the former sufficient constant
`223`. This theorem supplies no estimate for the disjoint primitive
shift-pair count.
