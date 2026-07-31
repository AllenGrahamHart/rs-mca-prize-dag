# Source evidence

- Primary exact helper:
  `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_fixed_xi_square_direct.py`,
  SHA-256 `d42b13b0cff26e448ad93e9925ce0e4283797d03c8a2f4d630175dddd457e5f3`.
- Independent exact helper:
  `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_fixed_xi_square_direct_audit.py`,
  SHA-256 `54b993280c506bc85976aaebd746b388c6ebb0ecbcb032bc513a96708310465f`.
- Primary and independent work are each split into four endpoint-pair shards
  after broader batches reached the `60 s` cap under host load. Every pair
  shard finishes below the cap under the `tiny` RAMguard profile.
- The four primary `verify*.py` wrappers and four `verify_audit*.py` wrappers
  pin their shared helper hashes.
- No floating-point or remote computation is used.

The retracted helper and outputs remain documented in
`notes/PRIZE_RESOLUTION_ROADMAP.md`; no DAG node ever depended on them.
