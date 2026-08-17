## Preregistered O0b `FFI` exact root-free chart

- **decision:** strengthen the timed-out determinant superset by the proved
  first-slope guards `m4p1*m5p1 != 0`
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  chart mask `FFI` only
- **relation to the exact chart:** equivalence, using the proved collapsed
  finite-slope-anchor node
- **launcher SHA-256:**
  `0cb0662bd9838914634c2754b0945c65234acd510bfcac5aadbf29f37d777c1a`
- **outcome-neutral checker SHA-256:**
  `d6cb810186922e42a6b2a041083ff39e86ca92a0f33f5ab56901e826b47185b5`
- **exact program core SHA-256:**
  `0d0c2da7847897a53997e50c81dc351f4490a455b3b54596623fa61b9996b9a2`
- **root-free source core SHA-256:**
  `dfdbfb078ab594d18b53e511e8e17b0375b25a551aa4d58a7d1fc82c7b3689eb`
- **collapsed timeout/result SHA-256:**
  `86d8686abf3d178bef2e1adaa17ca62e7d8b6dc0f5021b95cc8ee2f398f64335`
- **finite-slope-anchor verifier SHA-256:**
  `1059e49271b06104353ad61c2e3c766c56e253ae3480c0410fb6afa08802ac99`
- **input ledger:** 14 variables, 34 generators, no finite-root variables;
  determinants `x4,x5` and exact slope guards `m4p1,m5p1`
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.06`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

On the collapsed locus each finite first polynomial is linear with proved
nonzero slope. Its common root is therefore fixed, and the corresponding
`2 x 2` determinant is exactly equivalent to the second polynomial
vanishing at that root. The system retains the common basis, eight kernel
graph equations, `q3`, `q7`, both determinants, and one Rabinowitsch
equation for `f*(d^2-e^2)*(b+1)*m4p1*m5p1`. A checked unit basis proves
admissible `FFI` emptiness. Timeout or nonunit output has no proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_ffi_exact_rootfree_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app `ap-u6iyFxMytHuEldy71Db9JF`
returned the pinned row with status `TIMEOUT`; result SHA-256:
`da545e840fdcecaafb789df62444d3f8da68039d900cfec83c999f09e192daed`.
The outcome-neutral checker accepts the exact slope-guard ledger and rejects
all three hostile mutations. No transcript was printed within 240 seconds.
This has no mathematical status. Monolithic `FFI` basis runs in this
coordinate order are retired; the next work must factor or branch the
determinants under `q3`.
