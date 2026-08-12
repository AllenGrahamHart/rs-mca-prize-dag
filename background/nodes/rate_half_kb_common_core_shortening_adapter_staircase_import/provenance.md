# Provenance

- Upstream packet: przchojecki/rs-mca PR `#1163`,
  `[MCA] Cut common-core shortening staircase` (scottdhughes,
  2026-08-11), head `e26c15b2d`, stacked on `#1160` at `c5f4ea7a`.
- Audited source note:
  `experimental/notes/thresholds/kb_mca_v4_common_core_shortening_staircase_route_cut_v1.md`.
- Upstream canonical payload:
  `f5aac02184e6e3c0c3acda8fc64929d37e3166ce74556e7b3d217cdc8a520b7c`.
- Upstream status at import: "candidate proved local theorem;
  independent review required". This node's banking rests on the
  coordinator line audit (2026-08-12) plus the independent from-scratch
  replay in `verify_audit.py` — the same standard as the `#1160`
  import at `45b01e4e0`.
- The upstream packet's own reconciliation confirms no duplicate
  common-core packet among open upstream PRs and no overlap with our
  `#1161`/`#1162` beyond the agents-log seam.
- Local subtraction check (2026-08-12): our repo's prior "shortening"
  content is the L1/FPC5 GRS-shortening lane (a different operation on
  a different ledger); no collision.
