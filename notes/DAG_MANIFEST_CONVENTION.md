# Node-Local DAG Manifest Convention

The editable graph source is one `node.json` in every
`critical/nodes/<id>/` or `background/nodes/<id>/` directory.
`dag.json` is a generated compatibility artifact consumed by existing
verifiers, renderers, and node proofs.

## Manifest

```json
{
  "schema": "prize-dag-node-v1",
  "node": {
    "id": "example",
    "title": "Exact proposition",
    "status": "TARGET",
    "statement": "..."
  },
  "requires": [{"from": "parent"}],
  "alternatives": [],
  "evidence_for": [{"to": "consumer"}],
  "refutes": []
}
```

The migration retains optional integer `order` fields solely to reproduce
the pre-refactor compatibility DAG byte for byte.  New nodes and edges may
omit `order`; the compiler places unordered records deterministically after
the migrated records.  Do not coordinate new work through shared order
numbers.

## Edge ownership

- A consumer owns incoming `requires` (`req`) edges.
- A consumer owns incoming `alternatives` (`alt`) edges.
- A supplier owns outgoing `evidence_for` (`ev`) edges.
- A refuting supplier owns outgoing `refutes` (`ref`) edges.

This rule gives every edge one writer and prevents duplication during
parallel work.

## Partition

Critical nodes live under `critical/nodes/`; background nodes live under
`background/nodes/`.  Criticality is still defined by requirement ancestry,
not by folder preference.  Move the complete folder when criticality changes.

The migration created owner folders for 166 legacy nodes that previously
existed only inside `dag.json`.  Six are critical and now expose their
pre-existing missing statement/proof artifacts.  The refactor does not repair
or promote those mathematical claims.

## Workflow

Edit the local manifest and proof packet, then run:

```text
tools/ramguard tiny -- python3 tools/compile_dag.py --write
tools/ramguard tiny -- python3 tools/verify_dag_manifests.py
tools/ramguard tiny -- python3 tools/verify_prize_dag.py
```

Never edit `dag.json` directly.  `verify_prize_dag.py` rejects a generated
view that differs from the manifests.  `auto_discharge.py` updates changed
node manifests first and regenerates `dag.json` atomically.

The top-level schema, description, and root live in
`graph/dag_meta.json`.  The compiler implementation is
`tools/dag_manifest.py`.
