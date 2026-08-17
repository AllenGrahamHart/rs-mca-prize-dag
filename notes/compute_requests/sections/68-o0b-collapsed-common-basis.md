## Preregistered O0b collapsed four-variable common basis

- **decision:** impose the proved `k2=k5=0` collapse before adjoining any
  outside variables
- **scope:** the `epsilon=(-1,-1)` saturated common component underlying the
  canonical `FFI` and `FIF` charts
- **relation to the admissible locus:** necessary common superset; the
  already-saturated common ideal is intersected with `k2=k5=0` without a
  second guard saturation
- **launcher SHA-256:**
  `45336a48a27c06ea3eadd31fa3186a9dd4d29a5ea1a82811581a4e8c4e474659`
- **outcome-neutral checker SHA-256:**
  `681cdc37686d6f8e7dacfeb56f06edb9124f0341259925b3b1dfe077d4d88b94`
- **program core SHA-256:**
  `eced1e03746a6da568cff8a6e7e0b93e42aeb8d9eb9d0d011dc70896c71f303c`
- **input ledger:** variables `t,r,c,b`; 21-element global common basis plus
  the two exact kernel equations `k2=k5=0`
- **envelope:** one CPU, 2 GiB, 60-second Singular child wall and 90-second
  container wall; projected cost below `$0.01`
- **local safety:** one RAM-guarded Modal client under a 150-second external
  hard stop; no local CAS

A checked unit basis proves the necessary collapsed common superset empty and
therefore closes both `FFI` and `FIF`. A checked nonunit basis has no
emptiness status, but provides an exact four-variable generating set for
reducing `q3`, `q7`, and the finite determinants. Timeout retires this
ordering without changing the DAG.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 150s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_collapsed_common_basis_modal.py
```

**Outcome:** preregistered; not yet run.
