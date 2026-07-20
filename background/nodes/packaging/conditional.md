# packaging conditional proof

- **status:** CONDITIONAL
- **closure:** proof from deliverable predicate nodes

## Predicate nodes

- `compiler`
- `harness`
- `dossier_partial`
- `bridge_ledger`

## Claim

Conditional on the predicate nodes, the submission package has compiler
verdicts, gate-checked dossier versions, and descriptor-generated constants.

## Proof

`compiler` supplies the prize-facing verdict mechanism: rows and proof packets
are translated into `SAFE`, `UNSAFE`, `CONDITIONAL`, or `UNKNOWN`, with the
refusal rule preventing prize-facing claims over open axes or conjectural
ledgers.

`harness` supplies the verifier runner, manifest/certificate checks, and
negative controls needed to make the package reproducible.

`dossier_partial` supplies the gate-checked dossier payload, now framed as
Paper-D-attached packets rather than a parallel standalone artifact.

`bridge_ledger` is already proved and prevents silent convention/provenance
crossings between packets.

Together these four components are exactly the packaging statement: compiler
verdicts are emitted under the refusal rule, dossier versions are gate-checked,
and constants/provenance are carried through the descriptor and bridge-ledger
machinery.

---

## Predicate note (2026-07-20, wave-15): the submission dossier

`submission_quality_paper_dossier` (TARGET) is a req predicate of this
node (the submission-quality paper is a genuine packaging obligation).
This adds an open requirement; packaging stays CONDITIONAL. [The v7
list-corridor re-architecture on this node's other predicates is HELD
for maintainer ratification — Section C, not adopted here.]
