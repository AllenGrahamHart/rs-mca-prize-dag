# graded_collision_radius

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

Pairs at swap distance s have e1-difference height <= 2s, norm <= (2s)^{phi(N')}; if (2s)^{phi(N')} < p the pair is collision-free (nonzero by thm:upstairs, norm below p). At N'=128, p ~ 2^250: d* = 7. COROLLARY: when 2l' < p^{1/phi(N')} (true at N' <= 64 for prize p), ALL pairs are certified — unconditional fullness, the prop:qfloor norm-threshold mechanism restated as certification. Subsumes single_swap_injectivity as the s = 1 case.

## Ledger (migrated notes)

PROVED-IN-FLIGHT: #206 (s=1 rung subsumed; exact norm formula Phi_M(1)^(phi(N)/phi(M))) | PROVED 2026-07-04 from collision_norm_criterion and the swap-distance height bound.
