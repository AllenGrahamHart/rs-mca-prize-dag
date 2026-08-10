# Source evidence

Each role owner is a separate `PROVED` node with its own verifier and audit.
The aggregate verifier checks their exact statuses and DAG edges, reconstructs
the role-cell partition independently, and checks the exact label/system
arithmetic. The hostile audit rejects parent demotion, missing cells,
duplicate cells, extra cells, and missing owners.
