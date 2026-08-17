## Preregistered O0b `FFF` q5 coefficients

- **decision:** decompose compressed `q5` exactly as
  `C0+C1*s+C2*s^2` and reduce each coefficient separately modulo the
  48-element admissible base-graph basis
- **scope:** exact normal-form data for the last open canonical `FFF`
  chart; no outside equation is adjoined
- **launcher SHA-256:**
  `890436d585a6f02c7d0b732b393e084cfc9300be8135dd9ffc1df14c0c4da49a`
- **outcome-neutral checker SHA-256:**
  `bd2938881150d021a7c2b86b437b4a6139b44d8aa129db0e2316123270046720`
- **program core SHA-256:**
  `2cdcfbc96ed4855637fd96d5b5e70eb65eb2887b87158fda391a2e808fc15baf`
- **generated Singular SHA-256:**
  `3cf13a1df4b48d26810e4c6234fbadcf1e76219c4267ab61f4fb2418dee5d055`
- **source graph result SHA-256:**
  `5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1`
- **source graph basis SHA-256:**
  `7f59b5557597f429a3a56914cd5aad5c988902af6d88a3ef01580aaacbdd5d9e`
- **input ledger:** variables `x,t,r,c,b`; coefficient order
  `0,1,2`; `s` degree 2; 48-element dimension-one graph basis
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The core independently verifies the generic identity

```text
(p2*q0-p0*q2)^2-(p2*q1-p1*q2)*(p1*q0-p0*q1)
  = C0 + C1*s + C2*s^2
```

for affine-linear `qi(s)`. Each completed coefficient is retained in full
with its own SHA-256. Completion supplies exact input for factorization and
low-degree `s,E` resultants; timeout retains a checked coefficient prefix.
Neither outcome alone closes `FFF`.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_q5_coefficients_modal.py
```

**Outcome:** `COMPLETE`. Modal app
`ap-1GgCht615t6eZJCKSKStPA` retained all three coefficient normal forms:

```text
C0: degree 44, 761 terms, SHA-256 98f5a959174f9899da07cb09736ef86dc449e1513821a6741dce19e749bfe913
C1: degree 44, 782 terms, SHA-256 b7defd8474f7a3b04011776833e0b4b9dce44de2c88e41633b797d4b9ce1cf9a
C2: degree 44, 799 terms, SHA-256 3f1f3db22008656b9e98b1966ad0f6f3cff897544d02b48d1ddfc14b6e48990e
```

Result SHA-256:
`25b3ac23d74e0bb710c50d636048c0f95ea4b94d51f3c5e02634cbfdfddf5f6e`.
The checker accepts the complete coefficient ledger and rejects all three
hostile mutations. This replaces regeneration of the 3,126-term whole
normal form but does not close `FFF`.
