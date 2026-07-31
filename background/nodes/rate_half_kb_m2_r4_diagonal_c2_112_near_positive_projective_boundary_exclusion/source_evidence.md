# Source evidence

- `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_positive_projective_boundary.py`
  rebuilds the homogeneous reconstruction, checks the two projective q-roots,
  emits all seven saturated ideals, and proves each basis is unit.
- `verify_audit.py` independently reconstructs the projective form, checks
  the finite/infinity resultant product and both forced divisions, verifies
  moving reciprocity, and rederives the other-`xi` sign split.

The source hash is pinned by `verify_runner.py`. Every CAS shard is serial
under `ramguard tiny` and a hard 60-second timeout. No Modal credit or
floating-point arithmetic is used.
