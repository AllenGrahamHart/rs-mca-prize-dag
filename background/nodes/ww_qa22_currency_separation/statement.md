# QA.22 / W3 currency separation

- **status:** PROVED
- **dependencies:** `xr_target_budget_audit`,
  `ww_two_class_minimal_ledger_reduction`
- **consumers:** `ww_row_envelope_clause`, `worst_word_challenger_pricing`
  (evidence only)

QA.22 certifies, at six clean-rate candidate rows, an inequality whose
polynomial reserve is `16n^3`. That reserve bounds the MCA object
`R_post(u,v;A)`: a post-strip bad-slope count for each ordered pair `(u,v)`.

W3 uses a different currency and quantifier order. It bounds

```text
N_nonplant(U)
```

for each received word `U`, where the count includes every non-planted list
codeword. No proved theorem in the consumer chain converts
the per-pair slope reserve `16n^3` into a per-word list-codeword upper
allocation.

Therefore QA.22 is valid arithmetic calibration and evidence that its printed
staircase columns are affordable at those six rows, but it is not the W3
non-planted envelope. The exact two-class identity later helped expose a
strict counterexample to extending W3 to the unsafe cell, while QA.22 remained
type-inapplicable. The old
`xr_target_budget_audit -> worst_word_challenger_pricing` requirement is
accordingly evidence-only.
