# Source evidence

- `rate_half_kb_m2_r4_diagonal_branch_coefficient_compiler` supplies the
  exact norm form, reciprocal coefficient relations, and dimensions `8/7`.
- `rate_half_kb_m2_r4_diagonal_facet_mixing_obstruction` supplies the
  square fiber and identifies its reduced quadratic root locator as
  `P_(J_1)`.
- The distinction between two source points and one ramified point is
  retained from the fiber-resultant interface. No unramifiedness assumption
  is imported.
- The rank and reciprocal-minor calculations are proved locally and replayed
  with exact rational arithmetic.

## Upstream custody

The complete theorem and ramification warning are vendored into the diagonal
shift-pair/source-facet packet in draft PR `przchojecki/rs-mca#1132` at
commit `03deba0082443172e4eaeec928ede14420cb7e8a`:

```text
note blob:        c89716bf63bf5bb7575b9aa72a3b5e653879080b
verifier blob:    31eafd59c99a4f78162bebeb065c0b81cb4bbb34
certificate blob: f24855ce68ddcd4a034efdb24ded9cc875cfffd8
payload SHA-256:  0d1fa37ac4dc443ea19a00b2cad9bb3a6a37a1710c3f9ccd59b46609e2f6f1a6
```

The upstream verifier checks the exact `4/3` and `6/5` dimensions, both
reciprocal-minor sign identities, retention of the ramified orbit, and the
full packet against `64` hostile mutations.
