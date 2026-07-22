# Claim contract

- **scope:** the exact strict `m=1`, `A=3`, `e=1`, `s=0` analogue over
  `F_17` and the complete split-cubic coefficient-line census on `F_17^*`
- **mathematical claim:** the printed column-far Hankel pencil has exactly
  five supported finite slopes, and five is the exact core-free locator-line
  maximum; all sixteen maximizing lines have a unique constant-rank Hankel
  realization
- **status:** `PROVED`
- **consumer:** `rate_half_band_closure` by an `ev` edge only
- **falsifier:** a locator-line census mismatch, a fixed root in the printed
  pencil, a failed kernel identity, any specialization of rank other than
  three, a sixth supported slope, or a common split endpoint locator
- **load-bearing replay:** exhaustive `560`-locator / `156,520`-pair line
  census, all sixteen compatibility systems, and all `18` projective ranks
  per maximizing line
- **nonclaims:** no official-row counterexample, no construction for
  `m>1`, and no weakening of the official separation-rank or
  separated-pullback exclusions
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_strict_m1_corefree_five_slope_route_fence/verify.py`

