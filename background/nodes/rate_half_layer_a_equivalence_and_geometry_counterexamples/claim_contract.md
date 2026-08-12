# Claim contract

- **Claim:** (LA-EQ): any layer-A rank theorem conditioned on hypotheses
  satisfied by restrictions of strict `A=3, e=m` endpoint configurations
  already implies the endpoint's emptiness, so the rank route is a strict
  strengthening of the exclusion; the H1 and H1+H2 hypothesis rungs are
  constructively FALSE at `m = 2` (closed-form families with nullity
  exactly 1); and the `Z^m - X^{2m}` fence family has nullity exactly `2m`
  at `a = 7m-1` for every `m >= 2`, killing the bare count route at every
  `m`.
- **Dependencies:** (SAT4)-(SAT5) + (RNC1)-(RNC2) (PROVED, for the
  (LA-EQ) reading); `rate_half_layer_a_saturation_count_route_fence`
  (REQUIRES: the `m = 2` member and the banked `m = 2,3,4,6` family
  measurements this node cites as prior art).
- **Output:** the retirement of the standalone universal layer-A exclusion
  at `a = 7m-1`; the identification of the layer-A and realizability lanes
  as one question; the transportable H1+H2 starting variety.
- **Consumer:** `rate_half_band_crossing_location`.
- **Nonclaims:** (LA-PADE)/(LA-DEG) carried at POSED (mechanism = the
  PROVED (RIC3), cited not re-verified); H3/H4 untested; no
  (SAT2)-satisfying configuration built; the `O` minima are sample minima.
- **Falsifier:** an admissible H1 build with nullity != 1; a fence cell
  with nullity != 2m; or a proof that some H excluded by (LA-EQ) still
  admits a rank theorem (impossible by construction — that is the
  reading's content).
- **Replay:** `tools/ramguard local -- python3
  background/nodes/rate_half_layer_a_equivalence_and_geometry_counterexamples/verify.py`
  and the fresh-cells audit `verify_audit.py` (local).
