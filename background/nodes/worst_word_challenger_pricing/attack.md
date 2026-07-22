# ATTACK — worst_word_challenger_pricing (medium; census reconstructed)

## Fresh scaffolding: the E22 census is REBUILT and gate-validated
notes/e22_reconstruction.md + e22_core.py: the E15 (#197) toy cell reconstructed
BYTE-IDENTICAL from surviving code (F_193, core = first k-1 layout, petals of
size ell=sigma+1, planted_count M = floor((n-k+1)/(sigma+1)), challenger =
non-planted mixed/full-petal list member). Gate reproduced E15 exactly.

## What to do
Run the census (notes/e22_census_modal.py is ready; flush + per-cell verdict)
OR reason from the reconstructed structure. Two outcomes:
- TWO_CLASSES_EXHAUST (UNCLASSIFIED=0 across sigma=1..3, n=16..64): then write
  (a) the EXACT challenger count formula (like planted_count = M: core/petal
  choices x scalar factors), and (b) the structural EXHAUSTION argument (no
  third class at scale — the challenger is structured mixed/full-petal, not a
  new mechanism). => the revised worst_word_planted sup-over-words is carried
  by planted + challenger jointly; list_planted_arithmetic prices BOTH.
- THIRD_CLASS_ALARM: name and characterize the new class (taxonomy grows).
Deliverable: the two-column pricing (planted + challenger) proved exact.
