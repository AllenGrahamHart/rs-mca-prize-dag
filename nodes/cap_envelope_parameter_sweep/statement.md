# cap_envelope_parameter_sweep

- **status:** TARGET

## Statement

Pro's sharpening shows the printed cap's reserve (N_rho = 1024) was a declared convenience: at rho = 1/8 the proved quotient-remainder floor supports N = 8192 with 180 bits of slack, gaining 1/16 step. QUESTION: sweep (c, d) per rate against the floor lemma's exact validity conditions — do finer scales deliver the 0.318 / 0.310 steps that rates 1/4 and 1/16 need? Naive entropy arithmetic suggests YES with large margins (d up to ~30-50 before the |B|-box eats the entropy) — but the lemma's profile conditions must be checked, not extrapolated. If true, the whole corridor family closes by parameter optimization and the wave-1 widths were measured against the lazy cap.

## Attack surface

pure compute: evaluate the floor at the (c,d) grid per rate; verify each point against cor:extension-pole-quotient-remainder-floor's hypotheses

## Falsifier

the lemma's conditions failing at every scale finer than N_rho for rates 1/4, 1/16
