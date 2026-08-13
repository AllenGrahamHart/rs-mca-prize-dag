# Audit

The proof was checked against PR #1166 head `af0e7c63b`. The source note,
primary verifier, and manuscript hashes are pinned in `source_contract.json`.
The local replay reconstructs both rational endpoints of `(ST1)`, every
printed shortened-row threshold, and the adjacent failing margins. The
independent audit uses a separate fraction implementation and a finite
support model where the old global factor and the new local factor differ.

The critical scope guard is that `theta` is support-local and presentation-
dependent. Any gauge must recompute it in the translated direction space.
