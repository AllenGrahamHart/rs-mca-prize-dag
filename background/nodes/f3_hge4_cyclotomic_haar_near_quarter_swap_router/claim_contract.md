# Claim contract

- **claim id:** `f3_hge4_cyclotomic_haar_near_quarter_swap_router`
- **mathematical statement:** with `X=4(d+1)log m` and `B` the least power of
  two at least `X`, the inequalities
  `B<h` and `BX<m^(1-(4d+8B)/m)` force every exact-level width `h=m/4-d`
  pair to be antipodal-swap; `64(d+1)^2(log m)^2<m` is a closed-form
  sufficient sub-band
- **scope:** dyadic `m>=16`, compatible prime `p>=m^2`, `d>=1`, and `h>=4`
- **consumer:** HGE4 exact-level lower-quarter aggregate
- **status:** `PROVED`
- **proved dependencies:** exact-ratio tower compiler and primitive swap
  odd-moment router
- **new open content:** count the odd half-order perfect-square supports in
  the routed band and aggregate both classes in the deeper lower quarter
- **falsifier:** a primitive free-stabilizer exact-level pair satisfying
  `(CHQ1)--(CHQ2)`, or any pair at an even width in that band
- **nonclaims:** no odd swap count, deep lower-quarter free count, level
  aggregate, RAW-NG estimate, or HGE4 promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_hge4_cyclotomic_haar_near_quarter_swap_router/verify.py`
- **independent audit:**
  `tools/ramguard tiny -- python3 background/nodes/f3_hge4_cyclotomic_haar_near_quarter_swap_router/verify_audit.py`
- **upstream mapping:** primitive shift-pair dyadic defect router into the
  exact swap/half-order support census
