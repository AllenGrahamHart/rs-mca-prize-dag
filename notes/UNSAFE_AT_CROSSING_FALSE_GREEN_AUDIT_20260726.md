# Unsafe-at-crossing false-green audit

Date: 2026-07-26

## Ruling

The former critical implication

```text
qfloor_exact + averaged_slope_conversion -> unsafe_at_crossing [PROVED]
```

was not valid at its printed every-row scope. Both suppliers are sound local
theorems, but neither supplies its own row-instantiation premises.

`qfloor_exact` requires a prime-field row, `p=1 mod n`, an active quotient
order, the strict norm threshold, endpoint alignment, and
`Acl(N',ell')>B*`. The former caller checked none of these per row.

`averaged_slope_conversion` proves the exact occupancy implication

```text
nu(A) = E[N(A)] - (q/2) C_t(A) > B-1
  => at least B distinct slopes.
```

For strict prize unsafety, `B=B*+1`, so the required premise is
`nu(A)>B*`. Merely declaring the value set “collided” supplies neither a
post-paid family nor its strict-overlap profile nor this inequality. The old
proof also lost this one-unit strictness.

## DAG correction

- `unsafe_at_crossing`: `PROVED -> CONDITIONAL`.
- New exact leaf `unsafe_crossing_family_instantiation`: `TARGET`.
- The new leaf requires a fail-closed `Q`, `V`, or `M` payload for every row.
- `zone_b -> mca_unsafe` changes from `req` to `ev`; it is a possible payload
  route, not a logically separate premise once the universal witness theorem
  is assumed.
- E1 remains useful route mathematics, but no longer pretends to route every
  admissible field. The global quantifier lives only at the new payload leaf.

## Closure standard

Promotion requires a deterministic every-row compiler, or a proved exhaustive
finite decomposition, that checks the ambient slope field, base/generated-
field transfer, first-match ownership, exact endpoint, and strict integer
crossing. Dependency-status replay alone cannot close this node.

## Upstream consequence

The same logical gap appears in upstream
`experimental/notes/thresholds/unsafe_at_crossing.md`: its sentence “if it is
collided, the averaged locator-to-slope conversion applies” omits the theorem's
quantitative premise. This is bankable as an audit/route correction after a
current-main and open-PR race check; it is not a proof of a replacement row
certificate.
