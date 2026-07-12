# prize — the clean-rate campaign, node-per-folder

- `dag.json` — the single source of truth (statuses, edges).
- `nodes/<id>/` — one folder per critical node: `statement.md` always;
  `proof.md` iff PROVED; `sketch.md` iff PROVABLE; `conditional.md`
  iff CONDITIONAL (hypotheses must match dag.json wiring); `verify.py`
  + `cert/` as needed; `notes/` freeform (referee packets, scans).
- `tools/` — validator (with the status-artifact invariant),
  orbit/webapp builder, dag_commit ritual, vendor.py (export a node
  packet into the przchojecki/rs-mca experimental/ format for
  upstream PRs).
- `orbit/` — built artifacts (critical_dag.json, svg, html).
- `notes/PRIZE_RESOLUTION_ROADMAP.md` — the full-resolution execution
  roadmap, incremental proof/audit discipline, upstream packet contract,
  and proposed standing goal text.

Workflow: edit dag.json + node folders -> tools/dag_commit.sh ->
vendored packets pushed to the fork when mature. The legacy fork
(rs-mca-l1 etc.) remains the upstream-facing vendoring target only.
