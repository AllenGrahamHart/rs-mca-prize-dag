# Claim contract

- **claim id:** `f3_h3_low_distance_ideal_star_router`
- **mathematical statement:** every cutoff-18 rich row prime divides the norm
  of a normalized two-generator collision ideal whose two generators have one
  common center, whose three vectors have squared norm at most three, and
  whose two Parseval distances are at most six
- **quantifiers and row scope:** every dyadic order `n>=4`, every prime
  `p=1 mod n`, and every nonzero rich shifted-product target
- **consumer:** `f3_h3_mobius_excess_half`, fixed-order exceptional-prime route
- **status:** `PROVED`
- **proved dependencies:** rich-fiber norm cutoff, same-fiber ideal batching,
  and distance-two 2-primary exclusion
- **new open content:** compress or classify the rooted ideal stars and bound
  or factor their normalized ideal norms at official orders
- **falsifier:** seven distinct integer vectors of squared norm at most three
  having fewer than four distance-at-most-six edges, or a rich row prime not
  dividing the selected normalized ideal norm
- **proof route:** remove distance two, sharpen the centroid packing count to
  six edges, force a two-edge star, then divide the batched ideal by
  `(1-zeta)^2`
- **replay:**
  `python3 background/nodes/f3_h3_low_distance_ideal_star_router/verify.py`
- **upstream mapping:** primitive shift-pair control / exact second-moment
  ledger
