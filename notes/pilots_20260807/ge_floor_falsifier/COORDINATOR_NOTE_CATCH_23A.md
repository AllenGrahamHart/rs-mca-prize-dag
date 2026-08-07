# Coordinator note (2026-08-07, round 23): d4_cone.py is UNSOUND as an emptiness certifier (CATCH-23A)

The per-level Fincke-Pohst half-width (d4_cone.py:116-124) floors a
rational window to an integer, truncating valid lattice points.
Round-22 VERDICTS survive (every EMPTY cell re-confirmed by brute
force and by the corrected round-23 enumerator), but the witness
counts at the three nonempty cells are superseded: 2 -> 8 (h=4,
p=137), 6 -> 16 (h=8, p=12289, full radius), 2 -> 16 (h=8,
p=463249). True witness sets are single full <sigma,-1>-orbits of
size 2h (Lambda_p is an ideal); the FPCOST column was measured on
a truncated tree. DO NOT reuse d4_cone.py for emptiness without
the fix; use notes/pilots_20260807/ge_lattice_cert/latlib.py (the
scaled-integer enumerator with the fail-closed rounding lemma and
planted controls). REPORT.md's D4 witness column (2,0,0,6,2,0)
reads (8,0,0,16,16,0) corrected. TIGHTEMPTY/D3 results are
UNAFFECTED (they came from the exhaustive box sweep, not the
enumerator).
