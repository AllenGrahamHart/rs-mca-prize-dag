# Claim contract: rate-half ordinary-list crossing

```text
claim id: rate_half_list_adjacent_crossing
mathematical statement: every official rate-half row has an ordinary worst-list
  adjacent crossing L_1(a)<=B*<L_1(a-1)
quantifiers and row scope: every admissible official rate-1/2 row
consumer and exact slot: the rate-half branch of list_adjacency_closing
current status: TARGET
dependencies already proved: list_crossing_localization;
  rate_half_cyclic_rotated_prefix_floor (unsafe evidence);
  rate_half_list_integer_johnson_safe_anchor (safe evidence);
  rate_half_list_low_budget_exact_crossing (B*=1,2 exact);
  rate_half_list_budget_three_quadratic_scroll_primitive_module (primitive
    four-moving-target normal form for the four quadratic chambers);
  rate_half_list_budget_three_maximal_field_degree_collapse (prime/quadratic
    field dichotomy for the maximal B*=3 row);
  rate_half_list_budget_three_split_unit_single_fiber_exclusion (Vandermonde
    exclusion of the direct one-fiber quotient completion in all nine linear
    chambers);
  rate_half_list_budget_three_antipodal_primitive_quotient_gate (the welded
    fiber-four component is neither a dyadic quotient pullback nor the direct
    four-coset deletion partition);
  rate_half_list_budget_three_antipodal_pencil_degree_floor (the unique
    degree-drop direction has degree at least `2^36-2` on the maximal row,
    improved to `(2^38-4)/3` when the centered `e_2` vanishes);
  rate_half_list_budget_three_antipodal_reverse_residual_stratification (the
    generic and intermediate floor boundaries have exact linear and quadratic
    differential residuals, bounding exceptional roots of `U` by one and two);
  rate_half_list_budget_three_antipodal_fourth_root_gap_reduction (on those
    boundaries `U` is the unique fourth-root truncation, and existence forces
    respectively two-zero and one-zero omitted-coefficient gaps);
  rate_half_list_budget_three_antipodal_generic_secondary_gap_reduction (on
    the generic floor normalized `V` is a canonical square-root truncation
    with a second two-zero terminal gap);
  rate_half_list_budget_three_antipodal_generic_two_window_square_reduction
    (the simultaneous secondary gate is one direct square congruence between
    two length-`h` fourth-root windows, with linear differential forcing);
  rate_half_list_budget_three_antipodal_generic_deleted_pair_parity_reduction
    (on the two-deleted-antipodal-pair sublocus, one primary and one secondary
    zero are automatic and the remaining gate has one torsion variable);
  rate_half_list_budget_three_antipodal_generic_deleted_pair_even_factorization
    (a complete survivor splits the punctured torsion binomial into two
    coprime equal-degree square-pencil factors);
  rate_half_list_budget_three_antipodal_generic_deleted_pair_fourier_resultant_branch_collapse
    (the flat signed coloring excludes complete deleted-pair survivors in the
    prime-field and nonsplit quadratic maximal-row branches);
  rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_ode
    (the complete deleted-pair survivor has an exact half-degree
    constant-forcing ODE, which uniquely determines its monic generic
    direction for a fixed deleted quadratic and identifies its sole
    exceptional root);
  rate_half_list_budget_three_antipodal_generic_deleted_pair_mobius_ratio_router
    (the remaining Möbius check is exactly three reciprocal equations for
    the `N`-torsion outer square ratio, one per pullback of the antipodal
    pairing);
  rate_half_list_budget_three_antipodal_generic_deleted_pair_remainder_square_router
    (after the ODE and ratio branch, Euclidean division gives an exact
    square/fourth-power reconstruction test with no free lower direction);
  rate_half_list_budget_three_antipodal_generic_deleted_pair_harmonic_exclusion
    (the harmonic `q=-1` ratio is impossible throughout the exact official
    split-quadratic characteristic interval);
  rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_scalar_router
    (the remaining outer ratio is eliminated into three one-variable scalar
    identities, exact torsion traces, and a root-independent square test);
  rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_fourth_power_router
    (the scalar multipliers are explicit trace-coordinate squares, making the
    final square condition exactly one branch-independent fourth-power test);
  rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_gate
    (the first scalar-identity rejection is one explicit equation using one
    terminal reversed-quotient coefficient);
  rate_half_list_budget_three_antipodal_generic_deleted_pair_fourth_root_gcd_gate
    (the fourth root must divide `2N+kappa x^2U_0^3`, forcing a half-degree
    gcd and root-free divisibility test);
  rate_half_list_budget_three_antipodal_generic_canonical_span_criterion (the
    complete generic boundary is an exact two-dimensional canonical span test
    plus a split/Möbius check, with no free polynomial or outer variables);
  rate_half_list_budget_three_antipodal_intermediate_hensel_certifier (the
    intermediate boundary has a unique Hensel candidate off one explicit
    degenerate coefficient pair, which retains only one scalar);
  rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity (on the
    centered `e_2=e_3=0` stratum that direction has degree exactly `2^37-2`
    and is squarefree, and the remaining Wronskian factor is linear);
  rate_half_list_budget_three_antipodal_pure_harmonic_fermat_router (the pure
    stratum is exactly a non-antipodal harmonic lift router plus a coprime
    fourth-power decomposition with printed endpoint conditions);
  list_subsqrt_interleaving_collapse (post-crossing arity transport)
new open content: for every B*>=3, narrow the proved unsafe/safe bracket to
  one adjacent pair with a matching predecessor witness
falsifier: a received word exceeding B* at an asserted safe agreement
proof route being attempted: exact rate-half image-fiber/profile envelope or a
  stronger safe-side theorem paired with a new predecessor witness; on the
  quadratic B*=3 branch, price the primitive four-moving-target factorization;
  on the maximal row, treat the prime and quadratic field branches separately;
  on the line side, restrict to primitive or genuinely multi-fiber blocks;
  on the antipodal fiber-four component, prove primitive nonperiodic rigidity
  for the welded quartic norm equation, with the pure-quartic stratum fixed at
  exact degree `2^37-2` and a linear Wronskian residual, the intermediate
  floor boundary reduced to a one-coefficient fourth-root gap, the generic
  floor boundary reduced to simultaneous primary fourth-root and secondary
  square-root two-coefficient gaps, equivalently the direct two-window square
  congruence, with the deleted-pair parity sublocus reduced further to two
  scalar equations in one torsion ratio and then an exact two-cell
  square-pencil partition, with only the split quadratic field branch left
  after its Fourier-resultant bound, whose half-degree generic direction is
  fixed by one constant-forcing ODE and whose harmonic branch is removed,
  followed by three outer-ratio-free scalar identities, exact torsion traces,
  one terminal constant-coefficient gate, one branch-independent Euclidean
  fourth-power test, and its differential half-degree gcd gate before the
  canonical span certifier,
  the intermediate floor reduced by its three-way Hensel gate, and higher
  directions stratified by their exact residual degree; on the pure floor,
  exclude the harmonic-matched Fermat decomposition
replay command: tools/ramguard tiny -- python3
  critical/nodes/rate_half_list_adjacent_crossing/verify.py
upstream hard-input mapping: complete profile-envelope comparison with the
  target; rate-half list side
```
