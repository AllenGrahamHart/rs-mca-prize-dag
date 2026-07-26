# averaged_slope_conversion

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#6']

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
field certificate.

## Ledger (migrated notes)

s2 fork F2: plausibly provable (second moment + paid-fiber exclusion); needed exactly when zone-(b) is collided | PROOF WRITTEN in flight (#212): FM1 + slope-resolved second moment + v8 cap + explicit paid-fiber exclusion; verifier green. Their honest caveat: stated for post-paid support families — row use still needs the paid-excluded strict-overlap profile. | PROVED (Codex red-node pass): the proof is local to the post-paid support-family scope; row use still depends on supplying that scoped family.
