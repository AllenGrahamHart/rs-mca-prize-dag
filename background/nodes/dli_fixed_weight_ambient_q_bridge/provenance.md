# Provenance

Local starting pin: `8b6666db1` on
`codex/full-prize-resolution-v12-20260807`.

Canonical prize pin: `0dd5b3244` (`WAVE 69 INTEGRATED`).

Upstream pin: `przchojecki/rs-mca` `origin/main` `93fba1be3`. The terminology
and normalization are compared with:

- `experimental/grande_finale.tex`, `def:primitive-q`;
- `lem:image-ambient-moment-conversion`;
- `thm:primitive-q`, "Primitive Q after a Sidon moment payment".

Those upstream results date to commit `a3017697a`, which is an ancestor of
the pinned main. They are not imported as dependencies: the present finite
bridge is proved directly. Upstream Q is image-normalized, asymptotic, and
conditional on a Sidon moment payment; the exact defect and 21-bit mismatch
are retained here.

Newest open upstream PR at reconnaissance: #1173, head `2788d5ec3`.
Canonical and upstream trees were inspected read-only.

