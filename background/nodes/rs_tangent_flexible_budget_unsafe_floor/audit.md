# Audit

## Provenance

Upstream source: `przchojecki/rs-mca` commit
`b13de8113a03f06b6fc22bbd2f289a8abcdf7e95`, file
`tex/slackMCA_v4.tex`, SHA-256
`810ac469b8a8a8ba4638d882ec8426be95ffddf0f8888b83315afb4d60e990b4`,
label `prop:floor`. The local proof reconstructs the received line directly.

## Scope checks

- `e=n-a` counts distinct slopes, not supports or codewords.
- The witness set has `a+1` points, which is sufficient at agreement `a`.
- The strict prize comparison is `e>B*`, not `e>=B*`.
- The theorem is field-agnostic; it does not spend a base-field count against
  an ambient extension field.
- It works below the universal-cap endpoint as a low-field error floor, so it
  is not a duplicate of `cap_theorem`.

`verify.py` exhaustively checks two small finite-field RS instances and the
budget conversion. The clean-anchor specialization has a separate verifier.
