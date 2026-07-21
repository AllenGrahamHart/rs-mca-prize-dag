# Claim contract: NG-COUNT

- **claim id:** `f3_hge4_norm_gate_count`
- **mathematical statement:** `(NG-COUNT)` in `statement.md`
- **scope:** the full official corridor and every width `4<=h<=H_max`
- **consumer:** `f3_hge4_aggregate_budget`, through the proved x81/x83
  dichotomy bridge
- **status:** `TARGET`
- **proved dependencies:** x24 characteristic-zero classification, x81
  square-shift normal form, x83 obstruction gate, and the HGE4 assembly
- **new open content:** a uniform aggregate count of p-specific minimal
  norm-gate records
- **posedness debt:** the U2-boundary and DLI/skew deletion predicates are
  named by the consumer but lack operational in-repo definitions; use RAW-NG
  for a definition-independent proof, and do not certify a stripped
  counterexample until both predicates are positively implemented
- **falsifier:** a certified complete row or transported slice with stripped
  aggregate greater than `14n^3`
- **proved adapter:** `f3_hge4_primitive_shift_pair_aggregate_adapter` reduces
  the target to `SP_h^prim<=7000n max(1,B_h)` at every retained width
- **proved orbit router:**
  `f3_hge4_primitive_shift_pair_orbit_aggregate_router` reduces the target to
  `sum_h O_h^prim<=14n^2` and separates naive max-fiber summation
- **proved union router:**
  `f3_hge4_primitive_shift_pair_near_square_union_router` gives the exact
  anchored form `A_h^union=hO_h^prim` and removes the partition search
- **proved dual-gap exclusion:**
  `f3_hge4_near_third_dual_gap_exclusion` proves exact-level emptiness when
  `7h>=2m+1`
- **proved midpoint-pencil router:**
  `f3_hge4_near_third_kummer_midpoint_pencil` forces every retained
  near-third midpoint to divide a twisted `m`-th-power binomial; its uniform
  Kummer factor degree divides `h`, and primitivity forces that degree to be
  one, so every retained midpoint splits over the base field
- **proved quarter-width exclusion:**
  `f3_hge4_cyclotomic_norm_quarter_width_exclusion` deletes every exact-level
  width `m/4<=h<m/3`, so the live level sum stops at `m/4-1`; the Kummer
  strip is now a conformance interface rather than an open consumer branch
- **proved near-quarter swap router:**
  `f3_hge4_cyclotomic_haar_near_quarter_swap_router` removes the free class
  when `h=m/4-d`, `X=4(d+1)log m`, `B=2^ceil(log_2 X)`, and
  `B<h`, `BX<m^(1-(4d+8B)/m)`; even widths are empty and odd widths route to
  the existing half-order perfect-square support count; the constant-`64`
  band is a sufficient sub-band
- **proved swap-norm exclusion:**
  `f3_hge4_swap_norm_haar_band_exclusion` deletes the complete swap class when
  `log_2(m)(d+1)<=m/2`; its overlap with the Haar band is fully empty, while
  the remaining part of this wider band is free-only
- **proved Vandermonde-defect exclusion:**
  `f3_hge4_vandermonde_defect_band_exclusion` combines the strict defect
  ceiling with consecutive even-moment rank and the swap norm to delete every
  width satisfying `x=4(d+1)log(m)/m<=1` and
  `Y_3<=floor((h-1)/2)+2`, where `Y_3` is the printed cubic Taylor ceiling;
  this is the production empty-band cutoff
- **proof route:** prioritize the quadratic primitive-orbit aggregate through
  the near-square union representation; the per-width shift-pair estimate,
  stronger strip-free raw bound, a width cap, or a direct aggregate theorem
  remain valid alternatives
- **replay:** `python3 critical/nodes/f3_hge4_norm_gate_count/verify.py`
- **upstream mapping:** residual ray compiler for higher-dimensional balanced
  cores / primitive shift-pair control

Neither empirical zero nor NG-ZERO is claimed. Reopening F-4 minimality kills
this contract and requires DAG surgery.

## Provenance addendum (2026-07-21, wave-18 integration)

The original master-minted contract carried the route line "**proof route:**
first attempt the stronger strip-free raw bound in `attack.md`; use a width
cap or direct aggregate theorem if it fails" — superseded by the width-cap
route above, which is the route that in fact succeeded (proved exact-level
cap `m/4-1` as of wave-18). Preserved here per custody #104.
