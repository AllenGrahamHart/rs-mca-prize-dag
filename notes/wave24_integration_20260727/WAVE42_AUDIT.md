# Wave-42 audit — 433-1b cell 14: the kernel-denominator boundary branch removed

**Date:** 2026-08-02. **Planner:** Fable. **Range:** `454159b0..589b30b25`
(worker-authored delta = ONE substantive commit, `d5671b339`; the other
commits are merges of our own canonical master + a manifest refresh).
**Verdict: CLEAN — integrated in full.**

```text
dag.json: ZERO merge needed — their graph (1747/4842) is a strict
subset of ours (1753/4860 after the band mint); no new nodes, no
changed shared entries, no new edges. Integration = node FILES only.
```

## What fell

- **433-1b cell 14, statement item 6 (new)**: the common denominator of
  the interpolation-normalized eight-coordinate kernel has EMPTY
  intersection with the guarded principal curve in ALL FOUR source-sign
  cases (route-guard saturated boundary ideals all UNIT, initial
  dimension 1 / basis 20) — so the printed `(-1,1)` normalization is
  GLOBAL on the guarded curve, not merely generic, and the
  kernel-denominator boundary branch is GONE from the remaining outside
  ledger. Honest scope kept verbatim: "structural decomposition only —
  does not exclude the quadratic-cover curve or cell 14"; frontier
  updated with the do-not-scale warnings (dense five-variable
  prototype timed out; quotient/successive-resultant/latent-root
  capped).
- Modal certificate `ap-Lq3SBj46m5prGz0ixF9MRN`; new launcher +
  result JSON under `experiments/prize_resolution/`.

## Verification

Both node verifiers replayed under ramguard local:
`verify.py` -> `cell=14 charts=24 curve_dim=1 kernels=4
open_exception=unit kernel_boundary=unit`; `verify_audit.py` ->
`audit=ok ... kernel_boundary=unit`. Manifest refreshed after the file
pull. Integration hygiene: the bulk checkout initially pulled the
worker's `PRIZE_RESOLUTION_ROADMAP.md` and `verifier_manifest.json`
over ours — caught and restored; the worker's execution-log entry
(the work-cycle theorem block) PORTED into our roadmap log instead.

## Watches

- 433-1b remaining: the outside ledger on the quadratic cover (cell
  14's one exact branch) + the residual cells; next route step pinned
  by the worker (global normalized kernel + linear target-record
  structure BEFORE joint elimination).
- Export #1143: updated by the coordinator at `02d2788f` (433-1a
  aggregation); this wave's cell-14 progress goes out with the NEXT
  export batch after its own audit — it is now audited, so it is
  eligible.
- New pin: `589b30b25`.
