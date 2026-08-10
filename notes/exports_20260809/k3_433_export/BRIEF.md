# EXPORT PACKAGING BRIEF — the living K3 PR (2026-08-09)

MANDATE (user-ratified): package the completed K3 units for an
upstream PR in przchojecki/rs-mca, following the #1122-1143 series
conventions EXACTLY. The PR will live and receive incremental
pushes as later cells close.

## Content (the completed units only, from canonical)
1. The 112 source-line coverage completion: the literal-assignment
   coverage theorem (36/36 aligned-positive cells via the
   seven-packet census; near-positive 108->42 orbit reduction;
   aligned-negative + negative source-line + 48 projective
   boundary cells) + the restored complete-exclusion theorem + the
   M01-R11/M02-R11 discharge (the direct exact Singular replay at
   pinned PR #1144). Nodes: background/nodes/rate_half_kb_m2_r4_
   diagonal_c2_112_* (the wave-49..51 chain).
2. The 433-1b campaign, completed cells: cell-4 complete
   (cell4_complete_exclusion + its pairing/orbit chain), cells
   12-13 complete (cell12_complete_exclusion + chain), the
   universal xi4/xi3 transport, the universal positive label
   quotient, the parallel-DE matching orbit quotient, and the
   supporting compilers (Vieta minors, kernel, common curve).
   Nodes: background/nodes/rate_half_kb_m2_r4_coordinate_
   positive_433_1b_*.
   EXCLUDE: cell-9 in-flight material (it ships in a later push).

## Format (replicate the exemplar EXACTLY)
- Exemplar: the local fork checkout /home/u2470931/smooth-read-
  solomin/rs-mca (READ-ONLY; reading this sibling path is
  PERMITTED for this task), branch agent/kb-positive-three-loop-
  atlas (= PR #1143): experimental/data/certificates/<kebab-case-
  name>-v1/<snake_case_name>_v1.json per theorem; experimental/
  notes/ for the theorem notes; experimental/scripts/ for replay
  scripts; the agents-log.md convention. Study 2-3 certificate
  JSONs for the schema (fields, provenance pins, hashes) and match
  it field-for-field.
- Map each node -> one certificate JSON (statement, proof route
  summary, exact constants, the verifier's key counts, provenance:
  our repo commit 594aaa985 + the node path) + list each node's
  verify.py as the replay script reference (copy the scripts,
  adapting paths per the exemplar's convention).
- Group: one note per unit (112-coverage; cell-4; cells-12-13;
  universal transports) in the exemplar's note style.
- PR_BODY.md: series-style title "[K3] Close 433-1b cells 4 and
  12-13; complete the 112 source-line coverage" + summary +
  scope/non-claims (cell 9, [5,8], [11], the cell-3 xi4 residual
  remain open; this PR is a living branch receiving incremental
  pushes) + attribution (Codex campaign, coordinator-replayed
  verifiers, Scott's PRs 1141/1144/1149 absorbed with independent
  replays — credit him).

## Rules
- DRAFT ONLY into notes/exports_20260809/k3_433_export/ (build the
  full tree there: experimental/..., PR_BODY.md, MANIFEST.md
  listing every file + its source node). Never edit dag.json/
  nodes/tools; no git; no Modal. COMPUTE LAW: every python3 via
  tools/ramguard tiny|local -- python3 (literal --) from repo
  root, INCLUDING file patching and JSON peeking. Do not read
  notes/pilots_20260802/CAMPAIGN_LEDGER.md. Final message =
  a summary + the MANIFEST (no REPORT.md).
