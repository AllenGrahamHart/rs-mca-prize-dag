# Attack plan

1. Choose the first joint codeword-pair explanation `(c_0,c_1)` and its
   discrepancy support `T` whenever one exists. Keep witness supports in the
   data; existential pair proximity is not a payment.
2. For each bad slope and explaining codeword `p_z`, study
   `q_z=p_z-(c_0+z c_1)`. The deep proof kills every nonzero `q_z`; the
   official regime must instead classify these codewords by their zeros on
   the witness outside `T`.
3. The branch `q_z=0` is closed by
   `xr_true_tangent_coordinate_injection`, at cost at most `|T|<=n-A`.
4. For `q_z!=0`, choose an exact-`A` witness, put `W=S\T`, and apply
   `xr_tangent_mismatch_external_zero_factor_reduction`. This produces a
   punctured GRS chart on `T` with dimension `K-|W|`, agreement `A-|W|`,
   and invariant excess `h=A-K`.
5. Replace witness-selected `W` by the full external zero set `Z_z` of the
   selected difference codeword. This is now a proved canonicalization and
   gives one chart per selected slope/codeword pair. Route quotient-periodic
   charts first.
6. Apply the generic MDS kernel-ray theorem on generic fixed charts, then
   aggregate their distinct slopes without summing a binomial number of
   possible `Z_z`.
7. On a nongeneric chart, use the proved equivalence with a second joint
   `A`-support extending `Z_z`. Distinct joint explanations form a low-core
   family with intersections at most `K-1`; bound slopes per explanation and
   aggregate that family. A support count or collision moment alone is
   insufficient because the consumer needs distinct slopes.
8. The nongeneric descent has proved depth caps
   `169,169,255,254,254,510`. Seek a per-level or amortized branch-width
   theorem; do not spend an extra `16n^3` at every level.
9. Apply `xr_nongeneric_explanation_plotkin_width` at every level. Once
   `N<=4(h+1)`, the entire live nongeneric subtree has at most
   `1+104(h+1)` instances and its genuine-tangent charges are paid by
   `420(h+1)^2`. More generally, do not enumerate explanation supports in a
   fixed logarithmic window above that boundary. Restrict the branch-width
   attack to pre-terminal levels and retain generic-chart slope aggregation
   as an independent currency.
10. In that logarithmic window, provided `h+1>=2C log_2 n`, the entire live
    nongeneric tree and all genuine-tangent charges are polynomial. Therefore
    a remaining super-polynomial branch-width attack must keep
    `N-4(h+1)` above every fixed logarithmic cap; do not restart the recursion
    one level above the equality boundary.

The smooth `F_17` counterexample in
`background/nodes/xr_nondeep_tangent_supportwise_payment` is the minimum
regression fixture: any proposed payment must retain or validly charge all
eight mismatch slopes.
