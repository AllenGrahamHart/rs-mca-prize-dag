# `A=1` exceptional Forney MDS-Schur router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_residue_self_dual_algebra`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_exceptional_self_dual_evaluation_code`

Let `C_q` be the length-`2e`, dimension-`e` normalized exceptional code and
let `U_q^2` be its coordinatewise product span. Exactly one of the following
branches occurs.

1. **MDS branch.** Every `e`-column minor is nonzero. Then

   ```text
   dim U_q^2=2e-1.                                   (HMR1)
   ```

   Consequently the annihilating residue class
   `C=q_1 Phi/B_T mod A` is uniquely determined up to scalar by the split
   frame.

2. **Dependent-complement branch.** There is an `e`-subset `I` of the
   exceptional roots, with complement `J`, such that

   ```text
   Delta_I=Delta_J=0.                                (HMR2)
   ```

Thus a high-distance endpoint packet either prints one complementary pair of
dependent split-incidence columns or has a unique frame-determined Forney
weight line. The theorem does not exclude either branch.
