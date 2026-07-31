# Source evidence

- `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_moving_template_probe.py`
  supplies the shared edge/evaluation conventions.
- `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_moving_other_probe.py`
  reconstructs and caches the four source cores and ratio gates.
- `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_moving_other_mixed_ratio.py`
  builds the exact trace, generic pair gates, and `q=0` boundary equations.
- `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_moving_other_mixed_flint.py`
  computes the deployed-field projections and residue-field saturations with
  `python-flint==0.9.0`.
- `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_moving_other_cached_classify.py`
  replays the 22 minus-branch full-core saturations.
- `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_moving_other_mixed_audit.py`
  is the no-import source and artifact audit.

All helper and data hashes are pinned in `verify_runner.py`.
