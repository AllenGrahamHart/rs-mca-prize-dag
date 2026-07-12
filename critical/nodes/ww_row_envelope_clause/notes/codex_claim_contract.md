# Claim contract: direct worst-word challenger envelope

- **claim id:** ww_row_envelope_clause.
- **mathematical statement:** for every official cell descriptor,
  N_chal(c)<=B_chal(c) with both integers defined in statement.md.
- **quantifiers and row scope:** every official row, cell, layout, scalar
  choice, and received word in the consumer convention.
- **consumer and slot:** safe non-planted column in
  worst_word_challenger_pricing.
- **status:** TARGET.
- **proved dependencies:** paid-column inventory, generated-field
  normalization, and exact threshold convention.
- **new open content:** a sound exhaustive upper bound on the actual challenger
  set.
- **falsifier:** one official descriptor with N_chal(c)>B_chal(c).
- **proof route:** a defined rank certificate, direct structural exhaustion, or
  another upper certificate covering the full sup quantifier.
- **replay:** python3 critical/nodes/ww_row_envelope_clause/verify.py.
- **upstream mapping:** complete profile-envelope comparison / exact SPI
  ledger.

---
SALVAGE HEADER (2026-07-12, catch #94): imported as NOTES ONLY — the
accompanying statement replacement was REFUSED (it erased the banked R1
first-match binding and R2 certificate obligation). This contract's budget
definition, min-#493 baking, and normalization pins MATCH master and are
good; any re-landing must state the inequality per first-match cell and
carry R2 as a binding clause.
