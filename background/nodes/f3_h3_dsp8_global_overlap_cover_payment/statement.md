# DSP8 global overlap-cover payment

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependencies:** `f3_h3_distance_six_support_overlap_payment`,
  `f3_affine_coset_pair_cubic_preimage_stepanov`,
  `f3_h3_dsp8_antipodal_quotient_mass_payment`,
  `f3_h3_dsp8_primitive_shift_pair_adapter`

Use the `E=6`, `P(t)>=25` interface and put

```text
S_A=sum_(t antipodal,P(t)>=25)R(t),
Q_n=(n-1)(n-2).
```

The two proved one-parameter covers contain at most `2n` overlapping
generic--generic edges globally, over all targets. Consequently

```text
O_6,25^0+(17/10)O_6,25^A
 <(867/80)n^(5/3)+(17/5)S_A.                       (GOP1)
```

Write `K_25^0,K_25^A` for the decorated primitive shift-pair counts in the
proved adapter. The C36' consumer follows from

```text
10K_25^0+17K_25^A+68S_A+(867/4)n^(5/3)
 <=750n^2-255Q_n.                                   (GOP2)
```

In particular, the target-independent estimate

```text
160(10K_25^0+17K_25^A)<=76599n^2                  (GOP3)
```

is sufficient on every official row. Its effective primitive-SP constant is
`76599/160=478.74375`, replacing the preceding sufficient constant
`29031/80` and the original constant `223`. This theorem supplies no estimate
for the disjoint primitive shift-pair count.
