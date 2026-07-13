# Claim contract: direct worst-word challenger envelope

- **claim id:** ww_row_envelope_clause.
- **mathematical statement:** after an ordered, disjoint first-match assignment
  to every paid column, for every official received word the residual classes
  obey `sum_c N_chal^o(U,c)<=B_chal(U)`, equivalently through cell allocations
  whose sum fits the one residual.
- **quantifiers and row scope:** every official row, cell, layout, scalar
  choice, and received word in the consumer convention.
- **consumer and slot:** safe non-planted column in
  worst_word_challenger_pricing.
- **status:** TARGET.
- **proved dependencies:** paid-column inventory, generated-field
  normalization, and exact threshold convention.
- **new open content:** a sound exhaustive upper bound on the actual residual
  challenger set, plus a complete paid/residual ownership descriptor.
- **falsifier:** one official word with aggregate first-match challenger count
  above its exact residual.
- **proof route:** a defined rank certificate, direct structural exhaustion, or
  another upper certificate covering the full sup quantifier.
- **replay:** `critical/nodes/ww_row_envelope_clause/verify.py` checks the
  contract and wiring; mathematical closure still requires the emitted row
  certificates.
- **upstream mapping:** complete profile-envelope comparison / exact SPI
  ledger.

---
SALVAGE HEADER (2026-07-12, catch #94): imported as NOTES ONLY — the
accompanying statement replacement was REFUSED at that time. A later
consumer-backward audit keeps R1's per-word supremum and R2's certificate
obligation but replaces the non-composing whole-residual-per-cell inequality
by the aggregate allocation law.

R3 ownership repair: paid columns are assigned first and residual challenger
cells second. In particular, a quotient/staircase word cannot be subtracted in
`P_paid` and counted again in `N_chal^o`.
