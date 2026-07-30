# Source evidence

- Shared primary helper:
  `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_fixed_xi_square_direct.py`,
  SHA-256 `d42b13b0cff26e448ad93e9925ce0e4283797d03c8a2f4d630175dddd457e5f3`.
- Shared independent helper:
  `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_fixed_xi_square_direct_audit.py`,
  SHA-256 `54b993280c506bc85976aaebd746b388c6ebb0ecbcb032bc513a96708310465f`.
- Four primary and four independent pair shards replay below sixty seconds
  under `ramguard tiny`. The primary uses `--swap`; the audit independently
  uses the same chart flag but no primary imports.
- All eight wrappers pin their helper hash. No floating point, Modal, or
  unpriced remote computation is used.
