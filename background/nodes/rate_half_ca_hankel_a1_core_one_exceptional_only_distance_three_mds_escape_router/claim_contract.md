# Claim contract

- **scope:** official `A=1`, core-one, exceptional-only sharp-cap profile,
  restricted to quotient distance three
- **input:** the unique quotient support triple and its barycentric weights
- **currency:** clean ordinary moment supports and residual-domain root
  incidences
- **output:** every ordinary slope is either an internal two-cancellation
  fiber or an exact minimum-weight Vandermonde escape; the official
  composition is exactly `e` internal plus `3e` external
- **consumer:** `rate_half_band_closure`
- **load-bearing hypotheses:** all `2r+1` moments, exceptional rank `r-1`,
  ordinary rank `r`, squarefree split clean locators, one exceptional among
  `4e+1` supported slopes, and no residual fixed domain root
- **nonclaim:** the distance-three chart is not excluded; the `3e` external
  locators are not constructed or classified beyond disjointness from the
  canonical support, the three-value ratio gate, and the exact incidence
  deficit
- **failure certificate:** an ordinary supported slope with one or at least
  three exceptional-root cancellations, an internal fiber not equal to the
  forced support, an external locator meeting the canonical support or
  violating `(MER5)`, or a composition different from `(e,3e)`
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_mds_escape_router/verify.py`
- **upstream mapping:** exact finite SPI shift-pair minimum-distance ledger
