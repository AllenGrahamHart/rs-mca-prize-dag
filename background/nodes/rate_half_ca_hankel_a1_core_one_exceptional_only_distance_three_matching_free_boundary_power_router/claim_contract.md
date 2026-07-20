# Claim contract

- **scope:** official quotient-distance-three support packets
- **input:** the boundary root-unity labels on the exceptional pairs and
  triple
- **currency:** derivative-ratio normalization and central symmetry
- **output:** the exact matching-free tests `(MBP4),(MBP6)` and reconstruction
  of every admissible pair matching
- **consumer:** `rate_half_band_closure`
- **load-bearing hypotheses:** `A,B` are squarefree with disjoint roots;
  `P_X` is squarefree on those roots; `e=2^38-1` is odd; all boundary labels
  satisfy the proved formulas `(BRU2),(BRU4)`
- **nonclaim:** central symmetry and triple equality do not imply the dual
  row-product gate or external split design
- **failure certificate:** one pair for which `(BRU3)` and `(MBP3)` differ,
  one triple pair for which `(BRU5)` and `(MBP4)` differ, or an even value
  polynomial without a reconstructible opposite-value matching
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_matching_free_boundary_power_router/verify.py`
- **upstream mapping:** exact finite primitive shift-pair matching-free
  boundary-power gate
