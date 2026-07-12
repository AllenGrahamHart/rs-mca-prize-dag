# Proof And Build Record

The package in `formal/lean/rs_mca_formalization` is vendored unchanged from
Przemek's `rs-mca` commit
`53bb5df4d4d8d9be77c47c6f2e1f92e093824909`. Its certification map names the
Tier-1 theorems consumed by the finite-row dossier and separately labels typed
targets and non-claims.

The pinned Lean 4.31 build compiled all 15 jobs successfully. The source-tree
hash and build measurements are recorded in `BUILD_CERTIFICATE.json`. The
source contains no executable `sorry` or `admit`; the exact arithmetic
theorems use kernel `decide` and ordinary core lemmas.

The construction read is the successful package build. The consumer-backward
read is `audit.py`, which checks the imported commit/tree hash, required theorem
names, exact numeral witnesses, certification-map classifications, and absence
of proof placeholders after stripping comments. The optional `--build` mode
replays Lake with `-Kjobs=1` for memory safety.
