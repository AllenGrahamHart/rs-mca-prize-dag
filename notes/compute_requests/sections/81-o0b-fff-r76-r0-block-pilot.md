## Preregistered O0b `FFF` R76[0] block-square pilot

- **decision:** split `a=M0[0]` into canonical 128-term blocks and test
  the square of block 0 before launching a full product wave
- **scope:** one exact summand of `R76[0]=a^2`; no coefficient assembly
  or equation is formed
- **launcher SHA-256:**
  `b3cfcfffedb25d543bfa8661fbe8cab674e8bbd522e03e4a6060929206b0b9b5`
- **outcome-neutral checker SHA-256:**
  `fd67bc6a4f96cce7fd6346cd9fb1a8f5fed047018d20eff09a92068641843168`
- **program core SHA-256:**
  `e42f2fb807ac8d3813cc6670ea249daefc310965f0cb86d6d57dc0943deb1f7c`
- **generated Singular SHA-256:**
  `6cecc2164f63001457929bf0cde0be287381a482d89ed124b1725484fca73f60`
- **source bracket result SHA-256:**
  `08dc7fefd108d4b8d17a1c7a5345f37312b65b9a74389cf7e7dfc94827b0446f`
- **source polynomial SHA-256:**
  `4dc6a43d99611455c3ffadf53c2f2489f0e252371c280c138377ecc2b0a44839`
- **input ledger:** source has 1,152 canonical terms; block size 128;
  block index 0; half-open term interval `[0,128)`; square multiplier 1;
  48-element certified standard basis
- **envelope:** one CPU, 2 GiB, 60-second Singular child wall and
  90-second container wall; projected cost below `$0.01`
- **local safety:** one RAM-guarded Modal client under a 150-second external
  hard stop; no local CAS

The term splitter verifies exact round-trip reconstruction of Singular's
canonical serialization and checks its 1,152 terms against the retained
bracket stage. Completion retains the reduced block square in full. Timeout
retains the child transcript. This pilot only calibrates deterministic
sharding and has no proof status for `R76[0]` or `FFF`.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 150s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_r76_r0_block_pilot_modal.py
```

**Outcome:** preregistered; not yet run.
