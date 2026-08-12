# Claim contract

- **claim id:** `rate_half_mca_supportwise_affine_span_compiler`
- **status:** `PROVED`
- **input:** an affine codeword explanation family with one exact
  pair-noncontained support per counted slope
- **replacement:** local pair noncontainment replaces global direction
  separation in the affine-span rank step
- **output:** the unchanged affine-span incidence bound
- **deployed effect:** global-core families paid through `s=13` on
  KoalaBear and `s=5` on Mersenne-31
- **nonclaims:** no bound beyond those numerical walls and no full row
  closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_supportwise_affine_span_compiler/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_supportwise_affine_span_compiler/verify_audit.py`
