## Preregistered O0b `FFI` leading-collapsed pilot

- **decision:** exploit the proved infinity-pair implication `z2=z5=0` before
  computing the `FFI` boundary ideal
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  chart mask `FFI` only
- **launcher SHA-256:**
  `b622498b9b812eaf018ad65a227f75d334fef77549ec09bcec3ef44fb42372d1`
- **outcome-neutral checker SHA-256:**
  `318345ac994f056f85ff66d92f44c920c83fdc9b7841518ec841d9ec8d870886`
- **collapsed program core SHA-256:**
  `37c2e59eaa893327e409a67fdf719f8c99aa7fa1e03ac766a37c6c6826535bf9`
- **explicit msolve input/result SHA-256:**
  `f0846e25f26981e045d4416233bd81d36dac6c3a44b0da7b2cd19912a02c57dd`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.06`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The proved collapse removes lift variables `z2,z5`, replaces their graph
equations by `k2=k5=0`, and makes both finite matching pairs linear in `u4`
and `u5`. The 16-variable, 36-generator system inverts exactly
`f*(d^2-e^2)*(b+1)`: the first two factors justify the collapse and the last
is the repeatedly observed forbidden boundary. Therefore a checked unit basis
proves admissible `FFI` emptiness. Completion authorizes the analogous `FIF`
reduction. A timeout permits only further structural elimination in `FFI`.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_ffi_collapsed_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app `ap-CUpVsyqTjfJYECd7zUqcL8`
returned the pinned row with status `TIMEOUT`; result SHA-256:
`86d8686abf3d178bef2e1adaa17ca62e7d8b6dc0f5021b95cc8ee2f398f64335`.
The outcome-neutral checker accepts the exact collapse and guard ledger and
rejects all three hostile mutations. No transcript was printed within 240
seconds. This has no mathematical status. The next structural reduction may
eliminate `u4,u5`: after `z2=z5=0`, each finite common-root pair consists of
two linear equations in one root, so vanishing of its `2 x 2` coefficient
determinant is necessary. Proving the resulting root-free superset empty is
sufficient to close `FFI`.
