# unsafe_at_crossing

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#4']

## Statement

Conditional on `unsafe_crossing_family_instantiation`, `qfloor_exact`, and
`averaged_slope_conversion`, every admissible row has

```text
B_C(a_safe - 1) > B*.
```

The first predicate supplies a row-valid direct-value or post-paid occupancy
payload at the exact adjacent endpoint. The other two predicates convert the
respective `Q` and `M` payloads into distinct bad slopes.

## Attack surface

construct the exact per-row payload required by
`unsafe_crossing_family_instantiation`

## Falsifier

an admissible row with `B_C(a_safe-1) <= B*`, or a purported payload whose
endpoint, field transfer, paid-family exclusion, or occupancy inequality fails

## Ledger (migrated notes)

FALSE-GREEN CORRECTION 2026-07-26: the local supplier theorems were proved, but
their row-instantiation premises were not. In particular, “collided” alone
does not imply that the post-paid occupancy correction is small enough.
