# e22_cofactor_common_tail_kernel_invariance

- **status:** CONDITIONAL
- **closure:** proof

## Statement

For E22 mixed/full-petal challengers satisfying

```text
L_{T_i}(X) | H_i(X),
H_i(X) = U(X)L_{Z\C}(X) - a_i L_{C\Z}(X),
```

construct one common exceptional tail `B`, choose dyadic local moduli
`M_i>t`, and prove

```text
|B| < min_i M_i
```

and

```text
T_i \ B
```

is invariant under the `M_i`-th-root kernel of `x -> x^{M_i}` for every
touched petal.

This node is reduced to:

- `e22_common_tail_invariance_certificate_soundness`, the proved certificate
  semantics for common tails, local moduli, tail bounds, and kernel
  invariance; and
- `e22_common_tail_invariance_payload`, the remaining E22-specific cofactor
  construction.

## Falsifier

A cofactor divisor pattern for which every bounded common tail leaves some
non-tail set that is not invariant under any admissible dyadic local quotient
kernel, or a defect in the certificate-soundness rule.
