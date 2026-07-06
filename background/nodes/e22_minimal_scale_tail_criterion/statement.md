# e22_minimal_scale_tail_criterion

- **status:** PROVED
- **closure:** proof

## Statement

For dyadic E22 support-scale data, a modulus `M` is the selected minimal
admissible scale exactly when

```text
|B_M(R)| < M
```

and every smaller admissible dyadic modulus `M' < M` satisfies

```text
|B_{M'}(R)| >= M'.
```

Here `B_M(R)` is the canonical leftover after deleting all full `M`-fibers
contained in `R`, as in `e22_cross_scale_support_canonical_form`.

## Falsifier

A support whose selected minimal admissible scale disagrees with the tail-size
criterion above.
