# Source evidence

Each role owner is a separate `PROVED` node with its own verifier and audit.
The aggregate verifier checks their exact statuses and DAG edges, reconstructs
the role-cell partition independently, and checks the exact label/system
arithmetic. The hostile audit rejects parent demotion, missing cells,
duplicate cells, extra cells, and missing owners.

## External replay (2026-08-12 addendum, coordinator PR-sweep session)

Upstream PR `#1157` (scottdhughes, 2026-08-10) independently replayed the
raw `433-1b -> O0a` exclusion at public-DAG commit `8df0903391a2`:
15 cells, 1,575 labels, 25,200 signed systems, **zero survivors** —
matching this node's verdict exactly, from outside every producing
implementation. The replay also reconstructs the thirteen-route table
and keeps the two raw-empty routes at
`distinct_affine_slope_payment = null`, consistent with this lane's
ledger scoping (the upstream packet claims zero ledger movement).
