## Preregistered O0b `FFF` generic-t basis

- **decision:** transport the 48-element admissible graph basis from
  `F_p[x,t,r,c,b]` to `F_p(t)[x,r,c,b]` with Singular `imap`, then
  compute and retain the generic zero-dimensional basis
- **scope:** generic fiber of the one-dimensional FFF base graph; all
  coefficient denominators remain explicit open exceptional fibers
- **launcher SHA-256:**
  `fda29f0bf534c6df593140afdd3e80f7e6628d061d278ea3ba088596f9a1e230`
- **outcome-neutral checker SHA-256:**
  `4b4d6ee692eeb7df7e5f239a60cf28699985c562a57a43626f7a76fc9929c854`
- **program core SHA-256:**
  `052089c55b078181415b9fddbac8c9cc1921fe9e768b8fcdb5168ffc465c0e50`
- **generated Singular SHA-256:**
  `bb1a5f9ebfadbe0ab1495be0bed42741516b25011be582d1dd9b72dd23e4a3ad`
- **source graph result SHA-256:**
  `5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1`
- **input ledger:** parameter `t`; fiber variables `x,r,c,b`;
  source dimension 1, basis size 48; target coefficient field
  `F_2130706433(t)`
- **envelope:** one CPU, 2 GiB, 60-second Singular child wall and
  90-second container wall; projected cost below `$0.01`
- **local safety:** one RAM-guarded Modal client under a 150-second external
  hard stop; no local CAS

The pilot retains target dimension, basis size, vector-space dimension, and
the full generic basis with a hash. Completion only establishes the generic
fiber algebra. Every denominator introduced by the basis or later reductions
must be collected, factored over the base field, and handled as a separate
finite-fiber leaf before any FFF promotion. Timeout has no proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 150s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_t_basis_modal.py
```

**Outcome:** `ENGINE_REJECTED`. Modal app
`ap-xIYe6cHFkUBtFeoIUlmDUD` reached the `imap/std` line and Singular
rejected the transcendental coefficient field with
`characteristic is too large (max is 2^29)`, then faulted. No generic
basis was produced and no mathematical status changes. This is the same
engine limitation previously observed for large-prime block orders.
Singular generic-t computation at the deployed prime is retired. The
repository's existing AbstractAlgebra/Groebner.jl pipeline supports
`GF(2130706433)(t)` and is the registered replacement.
