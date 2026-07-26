# unsafe_crossing_family_instantiation

- **status:** TARGET
- **closure:** open

## Statement

For every admissible row and its proposed first-safe agreement `a_safe`, emit
an exact certificate at `a_safe-1` in at least one of the following forms.

### Q: quotient floor

Pin a quotient order `N'` satisfying every hypothesis of `qfloor_exact`, prove
that its canonical witness radius reaches `a_safe-1`, and prove

```text
Acl(N',ell') > B*.
```

### V: direct value set

Exhibit and certify more than `B*` pairwise-distinct ambient-field slopes,
each bad at `a_safe-1` for one received pair.

### M: averaged occupancy

Exhibit a deterministic post-paid support family `A`, its exact strict-overlap
profile, and the exact inequality

```text
nu(A) = E[N(A)] - (q/2) C_t(A) > B*.
```

The certificate must pin the ambient MCA slope field, generated/base-field
transfer, first-match ownership, and endpoint monotonicity. A family that is
merely “collided” is not an `M` certificate.

## Falsifier

An admissible row with exact `B_C(a_safe-1) <= B*` refutes this target and the
proposed adjacent endpoint. A purported payload is invalid if any scope,
ownership, endpoint, exact-count, or normalization check fails.
