# prize — the clean-rate campaign, node-per-folder

- `critical/nodes/<id>/node.json` and
  `background/nodes/<id>/node.json` — editable graph source (proposition,
  status, and locally owned edges).
- `dag.json` — exact generated compatibility view; never edit directly.
- `critical/nodes/<id>/` and `background/nodes/<id>/` — one folder per
  node: `statement.md` always;
  `proof.md` iff PROVED; `sketch.md` iff PROVABLE; `conditional.md`
  iff CONDITIONAL (hypotheses must match dag.json wiring); `verify.py`
  + `cert/` as needed; `notes/` freeform (referee packets, scans).
- `tools/` — validator (with the status-artifact invariant),
  orbit/webapp builder, dag_commit ritual, vendor.py (export a node
  packet into the przchojecki/rs-mca experimental/ format for
  upstream PRs).
- `orbit/` — built artifacts (critical_dag.json, svg, html).
- `notes/roadmap/` — editable strategy shards and lane indexes.
- `notes/PRIZE_RESOLUTION_ROADMAP.md` — generated compatibility roadmap.

Workflow: edit one node-local manifest and its proof packet, compile
`dag.json`, run the validators, and then use `tools/dag_commit.sh`.
Vendored packets are pushed to the fork only when mature. See
`notes/DAG_MANIFEST_CONVENTION.md`.
