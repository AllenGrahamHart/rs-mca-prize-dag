# Claim contract

- **claim id:** `f3_hge4_vandermonde_defect_band_exclusion`
- **mathematical statement:** for `h=m/4-d`, every primitive exact-level pair
  is absent when `x=4(d+1)log(m)/m<=1` and the cubic ceiling
  `Y_3=4((d+1)log(m)-d)-8(d+1)^2log(m)^2/m
  +(32/3)(d+1)^3log(m)^3/m^2` is at most
  `floor((h-1)/2)+2`
- **scope:** dyadic `m>=16`, compatible prime `p>=m^2`, `d>=1`, and `h>=4`
- **consumer:** HGE4 exact-level lower-quarter aggregate
- **status:** `PROVED`
- **proved dependencies:** cyclotomic-Haar defect packet and swap-norm band
  exclusion
- **new open content:** count the free class below the Vandermonde cutoff and
  both free/swap classes below the swap-norm cutoff
- **linear sub-band:** `4((d+1)log m-d)<=floor((h-1)/2)+2` remains a simple
  sufficient condition
- **falsifier:** a primitive pair in the printed cubic band; equivalently, a
  nonzero defect violating either the strict norm ceiling or consecutive
  Vandermonde support floor
- **nonclaims:** no pair count below the band, no exact-level aggregate,
  RAW-NG estimate, or HGE4 promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_hge4_vandermonde_defect_band_exclusion/verify.py`
- **independent audit:**
  `tools/ramguard tiny -- python3 background/nodes/f3_hge4_vandermonde_defect_band_exclusion/verify_audit.py`
- **upstream mapping:** primitive shift-pair control by even-prefix
  Vandermonde rank and cyclotomic antipodal-defect energy
