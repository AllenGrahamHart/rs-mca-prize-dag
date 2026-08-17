## Preregistered O0b `FFI` root-free determinant superset

- **decision:** replace each finite common-root pair in the proved
  `z2=z5=0` collapse by its necessary `2 x 2` coefficient determinant
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  chart mask `FFI` only
- **relation to the exact chart:** necessary superset, not an equivalence
- **launcher SHA-256:**
  `9ad375b539c95c3471e78d9a37ccbe51eb7c468f21f889e879f11de2a446706b`
- **outcome-neutral checker SHA-256:**
  `1c7568f25696684263c32f6fa29453ab3c4e48b3e59a1fd9291edbd7332d31b1`
- **root-free program core SHA-256:**
  `dfdbfb078ab594d18b53e511e8e17b0375b25a551aa4d58a7d1fc82c7b3689eb`
- **collapsed timeout/result SHA-256:**
  `86d8686abf3d178bef2e1adaa17ca62e7d8b6dc0f5021b95cc8ee2f398f64335`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **input ledger:** 14 variables, 34 generators, no finite-root variables;
  six retained kernel lifts and one Rabinowitsch variable
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.06`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

After the proved infinity equations force `z2=z5=0`, each finite pair has
the form `a0+a1*u=0`, `b0+b1*u=0`. A common root implies
`a1*b0-a0*b1=0`; replacing both pairs by these determinants can only enlarge
the exact chart. The system retains the common basis, all eight kernel graph
equations, `q3`, `q7`, both determinants, and the exact guard
`f*(d^2-e^2)*(b+1) != 0`. Therefore a checked unit basis proves the exact
admissible `FFI` chart empty. No nonunit or timeout outcome has proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_ffi_rootfree_modal.py
```

**Outcome:** preregistered; not yet run.
