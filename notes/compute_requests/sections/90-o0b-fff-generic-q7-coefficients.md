## Preregistered O0b `FFF` generic `q7` coefficient bank

- **decision:** reduce `a2m,bm`, their squares, and the three coefficients of
  `q7=D0+D1*E+D2*E^2` in the dimension-eight base algebra
- **scope:** staged coefficient construction before adjoining `q7` to the
  dimension-16 `q5` extension
- **source generic SHA-256:**
  `c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`
- **source packet SHA-256:**
  `fbeda61593e73cdcb7bf1e2baa1ebe8b098a7025f834135b3e02d2c291d50cd9`
- **program core SHA-256:**
  `1a68448c922c0b2bed65973949cf1a19a1bb1459f403da767d85cfdc753fd6cf`
- **launcher SHA-256:**
  `68047af97107271170b16ad6828810cd3480a880a5a72cefe560960d9c5f8c63`
- **outcome-neutral checker SHA-256:**
  `a7194893ed46a3f1df187194dbaa4abeef965d2b5b2813083aa241568264cfb6`
- **generated Julia SHA-256:**
  `69a4e7e889e40fa249aec6ab16f0e5bb7602ce6c8b500fdf6485068716ebc050`
- **output ledger:** seven ordered representatives and profiles, including
  every intermediate; complete rational coefficient denominator ledger
- **envelope:** one deterministic task, one CPU, 8 GiB, 360-second Julia
  child wall and 420-second container wall; projected cost below `$0.25`
- **local safety:** one RAM-guarded Modal client under a 480-second external
  hard stop; no local CAS

All three `Di` are independent of `s`, so their base-algebra representatives
embed unchanged into the `q5` extension. Transformation denominators remain
open.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 480s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_q7_coefficients_modal.py
```

**Outcome:** `COMPLETE`. Modal app
`ap-34Gk6WjaK7Ptlv0Jy93XKc` retained all seven staged representatives.
Every value has fiber degree two and exactly eight quotient-basis terms. The
`D0,D1,D2` hashes are

```text
D0 175919493e8500089bd1d528d2d768b83f9e47df021048ceea6ea637bf9a5b34
D1 1d7f55723f5a0cee8ebe409c879a480637a0b0bd6fa5fb9d2b4a95f25cb7f8dd
D2 d52a21d795e753e4aa04582fa3d67f65003a48b3406383db4a84730b528e961d
```

The 56 coefficient entries contain 24 distinct denominators. Result
SHA-256:
`37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d`.
The checker verifies every staged hash and rejects all four hostile
mutations. The exact `q7` quadratic is ready for the `q5` extension.
