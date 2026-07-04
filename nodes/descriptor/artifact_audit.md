# descriptor artifact audit

- **status:** TARGET
- **closure:** artifact

## Verdict

Leave red. `descriptor` is not truth-apt as currently stated.

## Current meaning

The node asks for a symbolic row descriptor:

```text
(p, e, s, rho) -> full derived row table
```

with polynomial-time generation, regression against the pinned row and master
table, and sole-source use by the dossier/compiler constants.

## Why it does not flip

There is no predicate input whose truth implies this node. The node is a missing
tool/build artifact, and the validator already reports it under artifact-kind
nodes. Its consumers are packaging and uniformity nodes:

- `compiler`,
- `row_slate`,
- `safe_assembly_uniformity`.

Those consumers need either the actual descriptor artifact or a truth-apt
replacement such as a descriptor-soundness proposition: generated constants are
complete, regression-checked, and used as the unique constants source.

Until that artifact or proposition exists, the correct critical-path status is
still red, but its red status means integration/build debt rather than a
frontier mathematical proof.
