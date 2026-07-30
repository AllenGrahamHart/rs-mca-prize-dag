# Source evidence

- Primary exact helper:
  `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_fixed_xi_square_direct.py`,
  SHA-256 `7d3892fddcb4ab95f1fd6f6fa58127cf77c72c024e3272fab9511152df27db93`.
- Independent exact helper:
  `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_fixed_xi_square_direct_audit.py`,
  SHA-256 `96036a63c54b94beab3ce6d33b0237c6c78b7e9208ea37a770c00171159dcde5`.
- The two primary shards finish in about 35 seconds each; the two independent
  left-line batches were split into four pair shards after one batch reached
  the `60 s` cap under host load. Each independent pair shard now finishes
  below the cap under the `tiny` RAMguard profile.
- `verify.py` and `verify_left1.py` replay the primary shards.
  The four `verify_audit*.py` wrappers replay the independently written
  Bezout pair shards. Each wrapper pins its helper hash.
- No floating-point or remote computation is used.

The retracted helper and outputs remain documented in
`notes/PRIZE_RESOLUTION_ROADMAP.md`; no DAG node ever depended on them.
