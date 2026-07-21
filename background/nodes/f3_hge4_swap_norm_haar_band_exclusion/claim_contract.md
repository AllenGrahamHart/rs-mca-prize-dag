# Claim contract

- **claim id:** `f3_hge4_swap_norm_haar_band_exclusion`
- **mathematical statement:** primitive odd swap pairs require
  `m^(h-1)<h^(m/4)`; the explicit dyadic band is swap-empty, and its overlap
  with the Haar router is completely empty
- **scope:** dyadic exact levels `m>=16`, compatible prime `p>=m^2`, and live
  HGE4 widths
- **consumer:** HGE4 exact-level lower-quarter aggregate
- **status:** `PROVED`
- **exact Haar overlap:** with `X=4(d+1)log m` and `B` the least power of two
  at least `X`, use `B<h` and `BX<m^(1-(4d+8B)/m)`; the constant-`64` band is
  only a convenient sufficient sub-band
- **proved dependencies:** primitive swap odd-moment router and
  cyclotomic-Haar near-quarter swap router
- **new open content:** after the downstream Vandermonde deletion, count free
  pairs between its cutoff and the swap cutoff and aggregate both classes
  below the swap-exclusion band
- **falsifier:** a primitive swap pair violating `(SNH1)`, or any primitive
  pair in the full Haar band
- **nonclaims:** no free-pair count outside the Haar overlap, deep-width
  aggregate, RAW-NG estimate, or HGE4 promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_hge4_swap_norm_haar_band_exclusion/verify.py`
- **independent audit:**
  `tools/ramguard tiny -- python3 background/nodes/f3_hge4_swap_norm_haar_band_exclusion/verify_audit.py`
- **upstream mapping:** primitive shift-pair swap-stratum cyclotomic norm
  exclusion and exact-level width deletion
