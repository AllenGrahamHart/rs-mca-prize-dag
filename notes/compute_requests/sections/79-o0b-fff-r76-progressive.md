## Preregistered O0b `FFF` progressive R76 coefficients

- **decision:** evaluate the same `R76(s)=Res_E(q7,q6)` coefficient
  formulas through progressive reduction modulo the 48-element graph basis
- **scope:** exact quotient-ring rearchitecture of compute request 78; no
  equation is adjoined
- **launcher SHA-256:**
  `fc1ae32daccb795d0ed1ee04b1ac0e3f1757776f37c438ec9513dc01cd2fa5cd`
- **outcome-neutral checker SHA-256:**
  `41e5e3c518d84837502e3345b431f06b6e73eab819f4d204536b34fe2dac994c`
- **program core SHA-256:**
  `4faa057513f7249d75a29143560c397f3a58db265621388450e0b81358ced61b`
- **generated Singular SHA-256:**
  `5319dc99297235aaf21a036e1d73c648187b854c06bee004eb55034bc424d6d2`
- **source raw core SHA-256:**
  `7cb0d1b17e2c8175afd59a90be30b84f9409fdad457f3df454119fe2262a22f6`
- **source raw timeout SHA-256:**
  `741bd7a2bfb06f3074fe59809a40d5399ec98b65d94386eea6d6cfc95e2fe3b0`
- **source graph result SHA-256:**
  `5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1`
- **input ledger:** base variables `x,t,r,c,b`; coefficient order
  `0,...,8`; maximum `s)-degree 8; 61 intermediate reductions and
  nine final reductions; 48-element certified standard basis
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The eight kernel entries and every convolution layer are reduced before the
next multiplication. Raw temporaries are killed after use. The source core's
independent symbolic verification still fixes the resultant identity and
degree-eight bound; only evaluation order changes. Completion retains all
nine coefficients. Timeout retains 61-stage intermediate and nine-stage
coefficient prefixes. Neither outcome alone closes `FFF`.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_r76_progressive_modal.py
```

**Outcome:** preregistered; not yet run.
