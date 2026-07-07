# Upstream program DAG (comparison artifact)

Reconstruction of przchojecki/rs-mca's conditional program (v13 raw +
grande_finale + towards-prize.md @ ab7721e5, 2026-07-07) under the SAME
structural laws as our prize DAG: three colors on the critical surface,
reds are logical leaves (ev-only into reds), validator-checked. KEPT
FULLY SEPARATE from ../dag.json (one-writer, no cross-contamination).

CONVENTION: statuses are UPSTREAM'S OWN CLAIMS, with pedigree tags in
every statement (V12-AUDITED / V13-RAW / GF-SELF-AUDITED / LEAN-CHECKED
/ OPEN-PR / EXTERNAL). Exceptions we independently replayed are noted
(staircase compiler). Under our replay-before-build banking, several of
their greens would be ambers — the pedigree tags carry that information
without distorting their claimed structure.

Shape: 36 nodes / 46 edges total; critical surface 22 nodes / 25 edges /
3 rings; reds = 4 (q_atom_finite, q_poly, normalized_band,
bc_residual_audit), trending to 1-2 as BC->Q discharges integrate.
Compare ours: 189 critical nodes / 17 rings / 7 reds.

Rebuild: python3 tools/verify_prize_dag.py && python3 tools/build_critical_orbit.py
