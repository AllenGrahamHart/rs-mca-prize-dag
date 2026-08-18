## Preregistered O0b `FFF` `R76` NTT determinant

- **decision:** reconstruct the exact determinant of the column-cleared
  16-by-16 `R76` polynomial matrix by a 32,768-point number-theoretic
  transform and pointwise finite-field determinants
- **source polynomial-matrix SHA-256:**
  `ea218c257268a7887bf296dcb7d9e8f97ca3591866ca04e6595b3cd8170a0dae`
- **source matrix-ledger SHA-256:**
  `15749ad35ba394a9dce27a8c759f0203746233a2fb354efcc3655d44ea205de4`
- **program core SHA-256:**
  `9fdee300f358b53ad6e1aefc18ccdb150efa2801cf729c8818cfd08e5a049bf0`
- **launcher SHA-256:**
  `f438f8db8bbec243eba76b2cf4e8a28b3225a096525bcc5177cc0d80916da642`
- **outcome-neutral checker SHA-256:**
  `122ed0b3c2f863ddbc93d3feed8bacb3ab04ec49fd7dff15d1525527336c7778`
- **generated C++ SHA-256:**
  `097aecc70b5c06ac12f99b5c971ff445e55f8291b13b302613ff952ee49b407a`
- **field structure:** `2130706433-1=127*2^24`; primitive root `3`;
  primitive 32,768th root `1168510561`
- **completeness bound:** every matrix entry has degree at most 1388, so
  `deg det(P) <= 16*1388=22208 < 32768`. Zero coefficients above 22208 are
  asserted after inverse NTT.
- **algorithm:** forward NTT all 256 coefficient vectors; compute 32,768
  independent 16-by-16 determinants by exact modular Gaussian elimination;
  inverse NTT the determinant values
- **cross-checks:** direct matrix determinant and reconstructed polynomial at
  `t=2` must both equal `1087830147`; repeat at independent holdout `t=3`
- **output ledger:** exact trimmed determinant coefficients, degree, term
  count, and canonical hash
- **envelope:** one Modal container, eight CPUs, 8 GiB, 180-second compile
  wall plus 420-second execution wall, 660-second container wall; projected
  cost below `$0.25`
- **local safety:** one RAM-guarded Modal client under a 720-second external
  hard stop; no local compiler or determinant computation

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 720s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_r76_ntt_determinant_modal.py
```

**Outcome:** pending.
