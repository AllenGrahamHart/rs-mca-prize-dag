# Claim contract

- **claim id:** `f3_h3_distance_four_cross_overlap_router`
- **mathematical statement:** every selected same-fiber distance-four edge is
  either antipodal with `x^2=u+v-uv` or reduces to the canonical cross-overlap
  equation `ux(1-y)=u^2-y`; the global edge ledger is at most
  `(3n^2+n)/2`
- **scope:** every dyadic order `n>=4` and every odd-characteristic common
  shifted-product fiber after the rich-fiber diagonal/`-1` deletion
- **consumer:** `f3_h3_mobius_excess_half`, distance-four candidate sublane
- **status:** `PROVED`
- **proved dependencies:** rich-fiber norm cutoff and distance-two 2-primary
  exclusion
- **new open content:** exploit the exact edge budget jointly with quotient
  weights, and classify the remaining distance-six candidate lane
- **falsifier:** a generic same-fiber distance-four pair with no cross signed
  atom, or a cross witness violating `(D4R2)`
- **proof route:** signed-support overlap, same-kind cancellation, and exact
  finite-field elimination
- **replay:**
  `python3 background/nodes/f3_h3_distance_four_cross_overlap_router/verify.py`
- **upstream mapping:** primitive shift-pair control / exact second-moment
  ledger
