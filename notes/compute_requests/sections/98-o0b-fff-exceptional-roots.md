## Preregistered O0b `FFF` exceptional roots

- **decision:** form the complete polynomial ledger on which the generic
  `FFF` proof may fail, then extract every base-field root by
  `gcd(H,t^p-t)` and exact linear factorization
- **source determinant SHA-256:**
  `a222789bb3e54df1a4198536644a6d331972087d968b61b227634eca22a79786`
- **source polynomial-matrix SHA-256:**
  `ea218c257268a7887bf296dcb7d9e8f97ca3591866ca04e6595b3cd8170a0dae`
- **program core SHA-256:**
  `d8493e3738f8a552dee82f271229e66805b6f834fcda49eae34e24b015c3fb9b`
- **launcher SHA-256:**
  `926e9e98608e8a06a9186e28c3b25cc031a55ffda80d5e06dd40e693f952798a`
- **outcome-neutral checker SHA-256:**
  `568e78350d7232d9392df018b01e6936cf1b27f494dcda011b05517dc3884fa3`
- **seven source groups:** generic basis; q5 coefficient normals; q5
  extension basis; q5 multiplication and kernel normals; q7 coefficient
  normals; sixteen `R76` column LCMs; exact `R76` determinant
- **input census:** 986 polynomial occurrences, 474 group-deduplicated
  polynomials before cross-group deduplication
- **method:** monic LCM within each group and globally; compute
  `gcd(H,t^2130706433-t)` by FLINT modular powering; factor the square-free
  result into linear terms; reconstruct every root polynomial and verify the
  global union against per-group roots
- **output ledger:** per-group LCM degree/hash/root polynomial/root list;
  global LCM degree/hash/root polynomial/root list
- **envelope:** one Modal container, two CPUs, 4 GiB, 660-second wall;
  projected cost below `$0.10`
- **local safety:** one RAM-guarded Modal client under a 720-second external
  hard stop; no local polynomial factorization

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 720s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_exceptional_roots_modal.py
```

**Outcome:** pending.
