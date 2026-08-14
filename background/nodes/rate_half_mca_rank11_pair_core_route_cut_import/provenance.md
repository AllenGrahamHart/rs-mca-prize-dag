# Provenance

- Upstream packet: przchojecki/rs-mca PR `#1168`
  `[MCA] Cut KoalaBear error rank eleven to dense pair cores`
  (scottdhughes, 2026-08-13 20:26 UTC), stacked on `#1167` at
  `491ccdf53`; canonical payload
  `ca624392d1842a69ca9212533af672e4325fa984dad11952443e247db80cb6c3`.
- Audited source note:
  `experimental/notes/thresholds/kb_mca_rank11_pair_core_route_cut_v1.md`
  (branch `pr1168`).
- Predecessor context: `#1166` (harvested as
  `rate_half_mca_support_local_transversality_compiler`, wave 60) and
  `#1167`, which independently converged on our cycle-232 rank-10
  payment (`rate_half_mca_rank10_margin_interleaving_split_payment`;
  identical formula, optimum `T = 667`, totals, and `T = 16` first
  paying threshold; our proof predates it by ~11 hours and was
  published on the `#1165` comment thread — recorded on that node).
- Upstream overlap check (theirs): "no overlapping rank-11 pair/core
  PR or public-DAG work was found." Ours agrees: our DAG had no
  rank-11 pair/core content before this import.
- Local subtraction check: cycles 233-236 (wave 60) touch M31
  boundary layers, not the KoalaBear rank-11 pair-core class.
