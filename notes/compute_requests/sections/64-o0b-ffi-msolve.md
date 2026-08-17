## Preregistered O0b `FFI` msolve F4 comparison

- **decision:** compare one genuinely different exact Groebner engine after
  all pinned Singular architectures timed out on the multi-finite frontier
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  lifted chart `FFI` with direct inversion of `b+1`
- **launcher SHA-256:**
  `aba99e284f29e21e141dd89662bc115dd20c7ad4aec5804801049bd7dd53d4a6`
- **outcome-neutral checker SHA-256:**
  `c3be965f5dfe87584f1c65683fc0a021788640db46dfee49b3b3c4a9407b3c12`
- **explicit-input exporter SHA-256:**
  `3775ca175d8d9e848637cd58e8337a84400ff6b9f5155a1d0dc4a924539dcc8b`
- **msolve prime-field smoke result SHA-256:**
  `4bf0791c422e83438b65c2c871119eee0a7124be1e2a6d508185ce7a13e11d70`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** one CPU, 8 GiB, 240-second msolve child wall and 330-second
  container wall; projected cost below `$0.10`
- **local safety:** one RAM-guarded Modal client under a 390-second external
  hard stop; no local CAS

The Debian trixie package supplies `msolve 0.7.5`. A pinned smoke test confirms
that it accepts characteristic `2130706433` and prints the canonical basis
`[1]` for a unit ideal. Singular is used only as a deterministic `short=0`
polynomial formatter: it exports the 38 exact graph-lifted generators with
explicit multiplication and powers. The full msolve input and its hash are
retained before the single-threaded `-g 2` F4 computation.

A checked `[1]` basis closes `FFI` off `b=-1` exactly and authorizes one-mask
transport to `FIF` and `IFF`. A complete nonunit is retained. A timeout or
engine error retires msolve on this frontier and does not authorize a larger
run.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 390s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_ffi_msolve_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app `ap-JJorYivOpEN8Skp6k2dJtx`
returned the pinned row with status `TIMEOUT`; result SHA-256:
`f0846e25f26981e045d4416233bd81d36dac6c3a44b0da7b2cd19912a02c57dd`.
The outcome-neutral checker accepts the exact 18-variable, 38-polynomial
input and rejects all three hostile mutations. msolve `0.7.5` reported the
correct characteristic, 18 variables, 38 valid equations, DRL order, sparse
exact linear algebra, and one thread, but produced no basis output within 240
seconds. This has no mathematical status and retires F4 on the unreduced
lifted system. The retained 15,897-byte explicit input exposes a structural
reduction in the `q6` infinity equations: admissibility forces `z2=z5=0`,
which is the next exact route.
