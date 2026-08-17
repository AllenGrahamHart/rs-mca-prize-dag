## Preregistered O0b collapsed-common admissible saturation

- **decision:** reapply all base admissibility conditions to the checked
  degree-65 collapsed common scheme
- **scope:** exact base locus for canonical `FFI` and `FIF` after
  `k2=k5=0`
- **relation:** exact route-guard and rank-cofactor saturation
- **launcher SHA-256:**
  `c8f91a2236e48129b4aca19d2e2f5d3cc175a395ea47faf0ef498c474a0a67e1`
- **outcome-neutral checker SHA-256:**
  `77cbda37ec6b075b52c67d371ef09d8e336c95a15dc8763f422a3ea682c75372`
- **program core SHA-256:**
  `a5c1c2a111088f34f0ac7563e4b6b06daabb8c955a98412edf35c02e3ba9b643`
- **source basis/result SHA-256:**
  `01a48b8003766b3e34d6b47423c8aaaf8ad8e521f77b1ce01cd1a9b5a6a7f65d`
- **FGLM result SHA-256:**
  `a72b2fe045538562352b3954b016dab60c5f8fdb01a22839088e72512d61f53f`
- **eliminant-factor verifier SHA-256:**
  `08d0c74703d84ff3eebaf43e5c867fc23ed6ea387a05497f8acc7fafed2a570e1`
- **input ledger:** variables `t,r,c,b`; 43-element degree-order basis;
  16 sequential route-guard saturations and one six-cofactor ideal saturation
- **envelope:** one CPU, 2 GiB, 60-second Singular child wall and 90-second
  container wall; projected cost below `$0.01`
- **local safety:** one RAM-guarded Modal client under a 150-second external
  hard stop; no local CAS

The prior common ideal was saturated before `k2=k5=0` was imposed. The new
intersection can acquire boundary points, as witnessed by the eliminant
factors `b^3(b-1)^4(b+1)^5`. This run removes every printed route boundary
again and then enforces the rank condition by saturation with the ideal of
six cofactors. A checked unit basis proves the exact admissible collapsed
base locus empty, closing both `FFI` and `FIF`. A nonunit result retains
the exact finite base for outside specialization.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 150s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_collapsed_common_admissible_modal.py
```

**Outcome:** preregistered; not yet run.
