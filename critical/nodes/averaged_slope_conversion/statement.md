# averaged_slope_conversion

- **status:** see `dag.json` (single source of truth; DAG status `CONDITIONAL`)
- **refs (legacy repo):** `proof_sketch/s2_paid_ledger.md#6`

## Statement

Averaged fiber-to-slope conversion: FM locator mean => existence of a many-SLOPE pair

Precise form: for a deterministic support family `A`, let

```text
nu(A) = E[N(A)] - (q/2) C_t(A),
```

where `C_t(A)` is the exact fixed-slope second factorial moment computed from
the strict-overlap profile. For every integer `B >= 1`, if `nu(A) > B-1`,
then some received pair has at least `B` distinct finite bad slopes.

For the prize's strict unsafe inequality, set `B=B*+1`; row use therefore
requires `nu(A)>B*`, together with a supplied post-paid ownership and ambient-
field certificate. The implication is intact, but prize use is conditional on
the TARGET node `averaged_xr`, which must supply the slope-resolved second
moment in the required post-paid support-family scope.

## Ledger (migrated notes)

s2 fork F2: the local conversion is proved for a post-paid support family, but
the required slope-resolved second moment remains conditional on
`averaged_xr`. Row use additionally must supply the paid-excluded
strict-overlap profile.
