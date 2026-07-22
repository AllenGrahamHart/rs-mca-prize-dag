# Claim contract

- **claim:** every rank-one trade has either a spanning persistent basis-
  pencil owner with cap `floor((R-v)/h)` or a proper rank-`j` flat owner of
  size at most `j+u`
- **scope:** rank-one trades produced by any normalized prize P-A
  flat-nullity core
- **output:** `(FO1)--(FO3)` and a deterministic owner rule
- **currency:** two-slope quotient cancellation, basis-persistent moving-zero
  charge, and the flat-nullity proper-flat bound
- **nonclaim:** no sum over bases/flats, no proper-flat count, no rank-two
  result, and no P-A aggregate payment
- **falsifier:** an in-scope rank-one trade whose common support admits neither
  owner or whose spanning owner exceeds `(FO2)`
- **consumer:** `xr_highcore_collision_count`
