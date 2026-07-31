# Source evidence

- `critical/nodes/rate_half_band_closure/notes/kb_c2_112_positive_qslice_symmetric.py`
  supplies the corrected exact fraction-free reconstruction and raw
  ramified allocation equations.
- `critical/nodes/rate_half_band_closure/notes/kb_c2_112_aligned_positive_ramified_saturation.py`
  audits the reconstruction, solves the exact normalization, proves moving
  reciprocity, and computes the six full forbidden saturations.
- `verify_audit.py` independently reduces the raw ramified norm modulo `q`
  and compares all residual coefficients and allocation equations.

The two source hashes are pinned by `verify_runner.py`. Every CAS shard is
serial under `ramguard tiny` and a hard 60-second timeout. No Modal credit or
floating-point arithmetic is used.
