# Prize consumer flat-scope compiler

- **status:** TARGET
- **consumers:** `f_global_packing_step`, `f_primitive_case`

Enumerate every prize-proof call to Conjecture-F flatness, including the
coordinate-prefix family, Hankel/split-pencil kernels, and the mixed-petal
received-word/Pade family that refuted the old two-family scope claim. For
each call emit one exact descriptor containing

```text
(domain, locator degree j, projective flat dimension r,
 root threshold, punctures, first-owner chronology).
```

Prove that the descriptor is either already paid by tangent, quotient,
dihedral, or PMA ownership, or lies in the quantitative dimension/gap regime
consumed by `f_global_packing_step`. Prove that the descriptors cover every
call and preserve actual section-point multiplicity.

The broad statement "every linear flat" is not a substitute. The known
full-space rational-normal example refutes an absolute-exponent theorem at
that scope, and `f_consumer_scoped` already proves that coordinate and Hankel
families alone omit the mixed-petal consumer.

## Falsifier

An actual LIST or MCA Conjecture-F call with no emitted descriptor, a
near-full-dimensional descriptor outside the proved packing regime and all
paid owners, or a transport that loses first ownership or section-point
multiplicity.
