# averaged_slope_conversion

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#6']

## Statement

Averaged fiber-to-slope conversion: FM locator mean => existence of a many-SLOPE pair

Precise form: from the exact FM first moment and the slope-resolved
second-moment ledger, after excluding paid fibers and applying the v8
per-slope locator cap, a family whose v8-normalized locator mean crosses `B*`
contains a pair `(u,v)` with at least `B*` distinct bad slopes.

## Ledger (migrated notes)

s2 fork F2: plausibly provable (second moment + paid-fiber exclusion); needed exactly when zone-(b) is collided | PROOF WRITTEN in flight (#212): FM1 + slope-resolved second moment + v8 cap + explicit paid-fiber exclusion; verifier green. Their honest caveat: stated for post-paid support families — row use still needs the paid-excluded strict-overlap profile. | PROVED (Codex red-node pass): the proof is local to the post-paid support-family scope; row use still depends on supplying that scoped family.
