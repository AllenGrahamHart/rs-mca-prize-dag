# Source evidence

- Modal app `ap-3hVthJkmosYTdYTQ4Kc91v`, program SHA-256
  `4a52d9141f9313cb6f8c0f78d4f9bd88bc2c3cfc2b99cca0cf5a54ccc9669a6b`,
  computes the deployed elimination bases and prints every linear `r,c`
  equation used by the atlas.
- `rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json` seals those
  equations, the simultaneous-denominator basis, and the Frobenius/Bezout
  data.
- `check_rate_half_kb_positive_433_1a_cell5_lift_atlas.py` independently
  recomputes the denominator Groebner basis, its factorization, modular
  Frobenius remainder, and Bezout identity.
