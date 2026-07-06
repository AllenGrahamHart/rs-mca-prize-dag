# e22_dyadic_local_to_common_saturation

- **status:** PROVED
- **closure:** proof

## Statement

In a dyadic E22 domain, remove a fixed exceptional tail `B`. Suppose the
remaining local non-tail blocks are

```text
S_j = union of full fibers of x -> x^{M_j}
```

for dyadic quotient moduli `M_j > t`. Let

```text
M_* = min_j M_j.
```

Then the whole non-tail union `S = union_j S_j` is a union of full fibers of
`x -> x^{M_*}`, and `M_* > t`.

Thus, once the E22 divisor constraints have supplied one fixed tail and local
dyadic quotient saturations, the common-modulus gluing step is automatic.

## Falsifier

A dyadic pair `M_* | M_j` and a full `M_j`-fiber that is not a union of full
`M_*`-fibers.
