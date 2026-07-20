# Claim contract

- **scope:** official `A=1`, core-one, exceptional-only sharp-cap profile
- **input:** the quotient-distance support and the exact row deficit `e`
- **currency:** MDS support comparison, disjoint affine cancellations, and
  an exact incidence lower/upper ledger
- **output:** `delta_A(h_1)=3` or
  `delta_A(h_1)>=183251937965`
- **consumer:** `rate_half_band_closure`
- **load-bearing hypotheses:** every ordinary supported fiber has `r`
  distinct roots and rank `r`, there are exactly `4e` ordinary slopes, and
  the total row deficit is exactly `e`
- **nonclaim:** neither surviving side of the distance gap is excluded
- **failure certificate:** an integer `h` in the killed interval satisfying
  the necessary incidence inequality `(QDG5)`
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_distance_gap/verify.py`
- **upstream mapping:** exact finite primitive shift-pair quotient-distance
  gap
