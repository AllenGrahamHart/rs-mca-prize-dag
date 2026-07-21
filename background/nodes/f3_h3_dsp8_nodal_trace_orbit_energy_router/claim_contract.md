# Claim contract

- **claim id:** `f3_h3_dsp8_nodal_trace_orbit_energy_router`
- **mathematical statement:** internally signed-distinct singular triples
  occur in free six-element presentation orbits; deleting same-orbit pairs
  gives `(NTE2)`, and the three trace classes have the exact cubic Fourier
  energy `(NTE4)`
- **scope:** every official H3 row; `(NTE3)--(NTE8)` concern the
  `p=1 (mod 3)` case
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **status:** `PROVED`
- **proved dependencies:** the exact nodal parameter router and the combined
  cube-preimage/quotient-line envelope
- **new open content:** in the only unresolved nodal regime `(NTE6b)`, prove
  enough cubic trace balance for `(NTE6)`, or pay the exact energy by another
  target-sensitive argument, then reserve a compatible budget for smooth
  traces
- **falsifier:** an internally signed-distinct triple with fewer than six
  ordered presentations, a signed-disjoint pair from one presentation orbit,
  an incorrect trace label `theta(1+theta)H`, or failure of `(NTE2)` or
  `(NTE4)`
- **nonclaims:** no cubic-bias estimate is asserted; `(NTE6)` is proved only
  under `(NTE6a)` and `(NTE7)` remains a sufficient condition, not a proved
  conclusion; no smooth-trace or complete DSP8 bound follows here
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_dsp8_nodal_trace_orbit_energy_router/verify.py`
