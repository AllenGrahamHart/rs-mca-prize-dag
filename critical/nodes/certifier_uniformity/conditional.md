# certifier_uniformity conditional proof

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: CONDITIONAL]
- **closure:** proof from predicate nodes

## Predicate nodes

- `lattice_cone_certificate`

Supporting convention:

- `rules_m_reading` records the accepted Reading-B style of determination
  artifact.

## Claim

Under Reading B, once the per-row lattice certificate form exists, the certifier
provably succeeds for every admissible row/prime in scope.

## Proof

Reading B treats the determination artifact as a proved-correct procedure that
yields the certified value for each admissible input. Under that reading,
uniformity has two parts.

First, correctness is certificate self-verification. The predicate
`lattice_cone_certificate` supplies the certificate grammar for the hard row
cells: a printed proof that the relevant sparse ternary cone contains no
non-cyclotomic kernel vector. A verifier for such a certificate checks the
finite matrix, cone, cyclotomic relations, and claimed exclusion. If the
certificate verifies, the row claim is proved.

Second, totality follows from exact finite search. Each admissible row instance
is finite. A complete branch-and-bound or equivalent exact solver either emits a
valid certificate for each branch or refines the branch until the finite search
tree is exhausted. Therefore there is no semantic `UNKNOWN` outcome: a completed
solver run is a proof object, not a sample.

Thus, conditional on the certificate form supplied by
`lattice_cone_certificate`, the uniform certifier layer is an assembly/procedure
claim. The classical uniform-GV theorem remains useful as an efficiency or
insurance route if a different reading is required, but it is not additional
mathematical content for the adopted Reading-B path.
