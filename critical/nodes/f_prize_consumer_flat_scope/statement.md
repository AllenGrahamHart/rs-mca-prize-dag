# Prize consumer flat-scope compiler

- **status:** CONDITIONAL
- **consumers:** `f_global_packing_step`, `f_primitive_case`

The current strict DAG has exactly two consumers of `conj_f`:
`imgfib` and `spi_point_counting`. Conditional on
`f_imgfib_consumer_descriptor`, combine its exhaustive LIST-side compiler
with the proved `f_spi_hankel_consumer_descriptor`. For each actual call emit
one exact descriptor containing

```text
(domain, locator degree j, projective flat dimension r,
 root threshold, punctures, first-owner chronology).
```

The descriptor must either already be paid by tangent, quotient, dihedral,
extension, or PMA ownership, or be passed without multiplicity loss to the
quantitative regime consumed by `f_global_packing_step`. The compiler is
exhaustive only for the current strict callers; a new strict caller must add a
new descriptor and re-open this node.

The full-locator Pade section is generally a polynomial section, not a linear
flat, and is not silently passed to Conjecture F. The proved
`l1_rootfree_rational_q_projective_packing` theorem extracts one exact linear
projective Conjecture-F cell inside the mixed-petal boundary route; exhausting
all LIST calls and preserving their first owners is precisely the remaining
`f_imgfib_consumer_descriptor` obligation. The broad statement "every linear
flat" is also not a substitute: the full-space rational-normal example
refutes an absolute-exponent theorem at that scope.

## Falsifier

An actual strict LIST or MCA Conjecture-F call with no emitted descriptor, a
Pade polynomial section mislabeled as a linear flat, a near-full-dimensional
descriptor outside every printed packing regime and paid owner, or a
transport that loses first ownership or incidence multiplicity.
