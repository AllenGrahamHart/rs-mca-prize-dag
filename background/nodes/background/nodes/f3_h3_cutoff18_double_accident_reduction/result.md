# Replay result

Run under the `tiny` RAMguard:

```text
F3_H3_CUTOFF18_DOUBLE_ACCIDENT_REDUCTION_PASS
point_checks=2145 fixture_checks=3 constant_checks=29
boundary_X18=4 boundary_Y18=0 mutation_controls=2
```

Every asserted identity and constant comparison uses exact integers.

The independent consumer-backward audit also passes:

```text
AUDIT_F3_H3_CUTOFF18_DOUBLE_ACCIDENT_REDUCTION_PASS
aggregate_checks=400 implication_checks=29
boundary_X18=4 boundary_Y18=0
```
