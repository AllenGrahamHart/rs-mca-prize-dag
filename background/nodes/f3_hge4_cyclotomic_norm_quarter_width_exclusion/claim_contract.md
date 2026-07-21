# Claim contract

- **claim id:** `f3_hge4_cyclotomic_norm_quarter_width_exclusion`
- **mathematical statement:** primitive exact-level top shift pairs are empty
  throughout `m/4<=h<m/3` under the official split-prime size condition
- **scope:** dyadic `m>=16`, prime `p=1 mod m`, and `p>=m^2`
- **consumer:** HGE4 exact-level orbit aggregate
- **status:** `PROVED`
- **proved dependencies:** exact-ratio tower orbit compiler and near-third
  Belyi necklace theorem
- **new open content:** uniformly aggregate the lower-quarter widths
  `4<=h<=m/4-1`
- **falsifier:** a primitive exact-level top shift pair in the excluded width
  interval at a compatible prime `p>=m^2`
- **nonclaims:** no lower-quarter count, exact-level budget, RAW-NG estimate,
  stripped norm-gate estimate, or HGE4 promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_hge4_cyclotomic_norm_quarter_width_exclusion/verify.py`
- **independent audit:**
  `tools/ramguard tiny -- python3 background/nodes/f3_hge4_cyclotomic_norm_quarter_width_exclusion/verify_audit.py`
- **upstream mapping:** primitive shift-pair exact-level width exclusion by
  cyclotomic norm and odd-frequency Parseval
