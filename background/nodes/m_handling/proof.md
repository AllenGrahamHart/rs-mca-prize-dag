# proof: m_handling

- **status:** PROVED
- **closure:** proof

## Source

Vendored from the working record; primary artifact(s):
- `proof_sketch/s7_list_side.md#3`

## Ledger

Rules resolved: family-per-constant-m. m_le3_route serves the small-m members (conditional only on imgfib now); the large-m members route through a_regular_collapse. Both branches now live, per-m partials creditable. | DISCHARGED BY CITATION (ring-2 sweep, node 3, 2026-07-04): the exhaustive disjunction resolves to its first branch — the official reading is per-CONSTANT-m (abf26.pdf p.5, the grand list challenge box: 'for a given eps*, and a constant m, determine...'; resolutions are per-(C, m, eps*); rules_m_reading PROVED = family-per-constant-m, partials creditable). Under that reading the worst-case route suffices, with m_sweep (PROVED) covering the affordable range m <= sqrt((n-k)/t) ~ 16-31. HONEST BOUNDARY: constant-m determinations beyond the affordable range would need a-regularity (as rules_m_reading already records) — each constant-m resolution is separately creditable per the official reading, and the campaign ships the affordable range. The three hypotheses were LEAF-unwired before this audit — wired as reqs (defect pattern #6, same class as axis 8). | GATE FIX: the node was gate:any over two alt routes built for the for-all-m branch — the citation killed that branch, so the discharge flows through the reqs directly; alts demoted to ev (kept for the large-m boundary where a_regular_collapse matters). All three reqs PROVED => PROVED.
