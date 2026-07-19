# height_only_impossibility

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

SHARPENED to the proved form (#206): the pure height gate cannot certify a full quotient cell once (2 s_max)^phi(N') exceeds the field ceiling — and in the official-rate table N' = 128 already exceeds p < 2^256 for ALL FOUR rates. Any full-strength certification at in-corridor scales must use p-specific input. (Companion anchor, same PR: at most TWO primes in range can collide even half the rate-1/2 cell pairs under the height bound — the exceptional set is provably tiny.)

## Ledger (migrated notes)

negative result with queue value — prevents doomed attempts | PROVED-IN-FLIGHT: #206 — SHARPER than stated: N'=128 exceeds the p < 2^256 ceiling for ALL FOUR official rates | PROVED 2026-07-04 from the graded_collision_radius threshold arithmetic.
