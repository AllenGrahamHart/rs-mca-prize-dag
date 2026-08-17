## Preregistered O0b `IFF` four-variable rational reduction

- **decision:** remove the already-closed `k2=0` infinity branch, solve the
  surviving `be=cf` branch for `d,e,f`, and clear all denominators
- **scope:** canonical `IFF` chart for
  `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`
- **relation:** necessary superset; `q5,q6` are retained through their
  scaled resultants, which also admit roots at infinity
- **launcher SHA-256:**
  `747b049182276b1feb785f5ce525ac14e70db79d8ae07cb3972310d56f3da13e`
- **outcome-neutral checker SHA-256:**
  `e6b895464bb43663ba0428a949eacd57628d1329ffdd12eda6ccb6221d12de54`
- **program core SHA-256:**
  `2a0efa6cc5e0c297575da3b2902b480eb129a49f14b3e7edc474aa81076b66f8`
- **collapsed-unit result SHA-256:**
  `38a44a30aa3421a67161acf5268d4bbfbe9e33903547e50259fc3f0da77efd03`
- **input ledger:** variables `t,r,c,b`; 21-element common basis; cleared
  equations in order `q7,q5,q6`; 16 route guards; denominator guards
  `k2,k5,a2m`; six rank cofactors
- **envelope:** one CPU, 4 GiB, 180-second Singular child wall and
  210-second container wall; projected cost below `$0.05`
- **local safety:** one RAM-guarded Modal client under a 270-second external
  hard stop; no local CAS

On the surviving infinity branch,

```text
e = k5/(b k2),
f = k5/(c k2),
d = a0m*b*k2/(k5*a2m).
```

The program verifies these substitutions symbolically, constructs scaled
quadratic resultants for the two finite pairs, and clears the `q7`
denominator. A checked unit basis proves this necessary superset empty and,
together with the closed `k2=0` branch, closes `IFF`. A nonunit result
provides a four-variable residual basis; timeout has no proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 270s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_iff_rational_reduction_modal.py
```

**Outcome:** preregistered; not yet run.
