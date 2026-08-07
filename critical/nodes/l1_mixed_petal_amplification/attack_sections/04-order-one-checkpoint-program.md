
- For the remaining order-one work, consume
  `l1_mersenne_hnf_order_one_involution_component_exclusion`. Divide
  `h!*Phi_h` by `rho*c*(c-1)*(c+1)`, saturate by `c+1`, and impose only the
  residual `Psi_h=0`. The `c=-1` component is theorem-empty on every
  official row and must not enter a saturation. The live residual degrees
  are `(deg_rho,deg_c)=(2,4)` at `h=7` and `(6,12)` at `h=15`.

- Then consume `l1_mersenne_hnf_order_one_newton_reciprocal_reduction`.
  Do not construct `Res_W(L,Z-W^m)` as the primary route. Generate the
  star-root and inverse-root traces from `L_star` and the monic reciprocal
  of `L`, and impose the first three Newton equalities. They require powers
  only through `3m`. A full identity uses the `H-1` interior equalities plus
  the constant-product equation; the first-three system is necessary only.

- Before constructing `L`, consume
  `l1_mersenne_hnf_order_one_full_trace_cancellation`. The removed root
  satisfies `(x_0^star)^(mj)=x_0^(-mj)` for every `j`, so its contribution
  cancels from every trace equality. Generate the first-three system from
  the original monic degree-`h` polynomial `P_star` and the monic reciprocal
  of `P`; do not divide by `W-x_0`. This is an exact representation
  reduction, not an emptiness theorem. Retained components still owe the
  pointwise Frobenius, torsion, cyclotomic, and inner equations.

- On the four `m=8,h=7` rows, consume
  `l1_mersenne_hnf_m8_order_one_conic_reduction` before generic elimination.
  Write the residual curve as the printed quadratic in
  `u=rho*c*(c-1)`, or use the conic
  `7w^2=247z^2+770z+775` together with the retained pullback
  `c^2-zc+1=0`. Include `t=infinity`, the tangent base point, and the
  denominator-zero projective chart. This
  replaces a hashed ten-term input by an explicit genus-one-style quadratic
  cover; it does not remove the full-trace, Frobenius, torsion, cyclotomic,
  or inner conditions. Do not apply it to `h=15`.

- Then consume
  `l1_mersenne_hnf_m8_order_one_basefield_conic_router`. Delete both
  `z=-1` points. On `t in F_p`, delete the `p=8191,131071` rows and retain
  only `zeta=-1`, `z=3`, `7w^2=5308`, and `rho^p=-c rho` on the two larger
  rows, with at most two `w` signs per row. Do not send a generic base-field
  conic parameter to elimination. The branch `t notin F_p` remains the
  positive-dimensional `h=7` task.

- Superseding close: consume
  `l1_mersenne_hnf_m8_order_one_basefield_branch_exclusion`. The finite
  larger-row packets are empty as well: Frobenius reflection makes every
  root and its complement an `n`th root, while the exact color-pair atlas has
  at most six points for the seven roots of `P`. Delete the complete
  `t in F_p` branch on all four rows. Do not replay the former four packets;
  attack only `t notin F_p` in the `h=7` order-one curve.

- In that non-base-field branch, consume
  `l1_mersenne_hnf_m8_order_one_constant_color_exclusion`. The six roots of
  the reduced factor cannot share one `p+1` color: the first two colored
  reciprocal coefficients force `rho*c=1-epsilon*zeta` and then an explicit
  `F_(p^2)` formula for `c-1`, whose norm equation misses every eighth-root
  trace in all four official characteristics. Begin any colored elimination
  at nonconstant degree. Preserve the root/color assignment; this theorem
  neither licenses an assignment-free color census nor closes any
  nonconstant degree stratum.

- Also consume `l1_mersenne_hnf_order_one_linear_color_exclusion`. A linear
  interpolant is injective, but every selected color must satisfy one
  quadratic obtained from the pointwise equation `E(x)=x^(p+1)`; it cannot
  carry the six or fourteen distinct reduced roots. Hence the live `h=7`
  branch starts at `deg E=2`, while `h=15` starts at degree zero or two. Use
  the pointwise quadratic, not only `E^m=1 mod L`, in subsequent low-degree
  exclusions.

- Consume `l1_mersenne_hnf_order_one_quadratic_color_resultant` before any
  degree-two coefficient elimination. It closes the complete quadratic
  color stratum at `m=16,h=15`: fourteen reduced roots would require seven
  distinct colors, but the pointwise quadratic resultant has degree six.
  At `m=8,h=7`, use its exact degree-six color polynomial. In the
  collision-free and one-repeat chambers substitute (QCRS4) and (QCRS5),
  respectively; do not discard the double factor of the repeated color.

- Before splitting the `h=7` quadratic collisions, consume
  `l1_mersenne_hnf_m8_order_one_quadratic_pointwise_composition`. Every
  quadratic packet satisfies the assignment-preserving identity (QPC2) and
  the pure HNF equation `g(1)=(1-rho*c)^3`. Intersect this equation with the
  residual conic once for all three collision chambers; do not replace it by
  a color-multiset norm argument on unconstrained interpolant coefficients.

- The shared quadratic intersection is now
  `l1_mersenne_hnf_m8_order_one_quadratic_hnf_intersection`. Replace the
  positive-dimensional quadratic-color conic by the printed degree-fourteen
  `R_2(d)` and its eight norm-fiber gcds on each row. This is the global
  degree-two endpoint; retain the degree-eight two-antipodal endpoint as its
  cheaper specialized check.

- For every fixed `m=8` univariate norm endpoint, consume
  `l1_mersenne_hnf_m8_aggregate_norm_gcd_compiler`. Replace the eight
  color-fiber gcds on one prime by the single aggregate gcd against
  `X^(8(p+1))-1`. A unit aggregate row proves all eight color rows unit; a
  nonunit row is only a router and must be split by `zeta` before packet
  reconstruction. Do not interpret an aggregate hit as an HNF witness.

- At cubic color degree, first consume
  `l1_mersenne_hnf_m8_order_one_cubic_two_triple_reduction`. If exactly two
  colors are used three times each, their full cubic fibers factor `L` and
  force the printed second quadratic in `(r,d)`. Replace this complete
  multiplicity-`3+3` chamber by the degree-fourteen `R_33(d)` and its eight
  norm-fiber gcds per row. Do not apply the equation to any other cubic
  multiplicity partition.

- Superseding close: consume
  `l1_mersenne_hnf_m8_order_one_cubic_two_triple_exclusion`. The unused
  `W^2` coefficient of the same factorization reduces the two quadratics to
  `(2d+3)(d+3)=0`, and neither base-field root has eighth-root norm on an
  official row. Delete the complete cubic multiplicity-`3+3` chamber and
  retire `CR-L1-H7-C3-33`; no norm gcd is required.

- For the remaining cubic packets using exactly three colors, consume
  `l1_mersenne_hnf_m8_order_one_cubic_three_color_remainder_router`. Work
  with the seven cyclic color-set representatives, not all 56 triples or
  root assignments. Impose the six value-remainder coefficients and all
  three nonempty-fiber resultants, then split only into `3+2+1` and
  `2+2+2` by exact subresultant degree. Apply the assignment-preserving
  Frobenius equations only to retained components.

- On the `2+2+2` profile, immediately replace the generic remainder by
  `l1_mersenne_hnf_m8_order_one_cubic_three_double_factor_reduction`.
  Factor `L` into the three printed quadratics from one `(U,V)` family and
  impose the scale-free color ratio. Enumerate color order only at that last
  equation; do not carry a generic cubic `E` through the factor census.

- Then consume
  `l1_mersenne_hnf_m8_order_one_cubic_three_double_symmetric_compiler`.
  Replace `(u_1,u_2,u_3,V,s_3)` by the printed triangular symmetric
  elimination. The p-free core has only `(U,s_2,r,d)`, the three cleared
  coefficient equations, and the h=7 conic. Do not interpret "square" as a
  dimension verdict; classify or eliminate this core before color sharding.

- Refine that core with
  `l1_mersenne_hnf_m8_order_one_cubic_three_double_linear_remainder_reduction`.
  In the scaled variables `(x,b,q,d)`, keep the quadratic `D_b` and reduce
  both later coefficient equations modulo it. Attack `x=0` and
  `q=-6x^2` first; off those loci the fifth equation solves for `b`, so use
  the resulting three-variable generic elimination. Do not use only the
  determinant of the two linear remainders, and do not add color or norm
  shards before this p-free branch classification.

- The `x=0` branch is now reduced by
  `l1_mersenne_hnf_m8_order_one_cubic_three_double_x0_quintic_reduction`.
  Delete the norm-impossible values `d=-2,-3/2,-3`, then test the printed
  degree-five `P_5(d)` against the 32 official norm fibers. Unit gcds close
  this entire exceptional branch without solving `D_b` or `M_6`; retain any
  nonunit root for those stronger filters. Do not recompute the original
  four-variable ideal on this branch.

- The second exceptional branch is reduced by
  `l1_mersenne_hnf_m8_order_one_cubic_three_double_q6x2_degree12_reduction`.
  For `q=-6x^2`, test the printed degree-12 `R_12(d)` against the same 32
  official norm fibers. Its derivation removes the `q=d` saturation branch
  before one necessary squaring; apply the unsquared sign, `D_b`, and `M_6`
  only to nonunit norm roots. Do not carry `(x,y,b)` into the norm gcd.

- On the `3+2+1` profile, consume
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_factor_reduction`.
  Use the triple fiber as the cubic factor `F`, its complement `G`, and the
  repeated-value cubic resultant with the fixed color-difference ratio
  `lambda`. There are at most 42 role packets before row sharding; do not
  replay the generic degree-nine remainder for each root assignment.

- Refine every retained `3+2+1` role with
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_common_quadratic_compiler`.
  Replace the generic pair `(F,G)` by the common quadratic `Q`, the two
  complementary roots, and `F=G+aQ+B`. Use the first three HNF coefficients
  to eliminate `a,g_2,B`; classify the resulting five equations in
  `(g_1,y,r,d)` before norm or row sharding. Retain `a*B*(lambda-1)*Q(y)`
  and the exact gcd-degree saturation.

- Carry all `3+2+1` color roles with
  `l1_mersenne_hnf_m8_cubic_three_two_one_role_polynomial_compiler`.
  Adjoin the single degree-42 `Lambda_321(lambda)` to the symbolic-lambda
  common-quadratic core; factor retained lambda components only after the
  shared elimination. Do not launch 42 independent copies, and do not retain
  the seven removed diagonal choices `lambda=1`.

- On the collision-free cubic profile, consume
  `l1_mersenne_hnf_m8_order_one_cubic_collision_free_value_router`.
  Replace 28 missing-color pairs by the four cyclic distances and impose
  `Res_W(L,X-E)M_delta=X^8-1`. Retain the squarefree value-resultant
  saturation; this identity is invalid on every repeated-color profile.

- Complete the cubic multiplicity router with
  `l1_mersenne_hnf_m8_order_one_cubic_four_five_color_value_router`. For
  four or five colors use `V_E M=(X^8-1)D`, where `M` is the missing-color
  product and `D` is the excess-multiplicity product. Work with the exact
  orbit counts `35,35,54`; preserve coprimality of `M,D` and exact fiber
  subresultants.

- More generally consume
  `l1_mersenne_hnf_order_one_color_degree_barrier`. The pointwise degree-`d`
  color equations define curves of degrees `d` and `d+1`, so `H<=d(d+1)`.
  Delete color degrees one through three from the `h=15` order-one branch;
  its nonconstant work starts at degree four. At `h=7`, the barrier is
  sharp at degree two and supplies no additional emptiness beyond the
  linear theorem.

- For the remaining `h=15` constant chamber, consume
  `l1_mersenne_hnf_m16_order_one_constant_color_reduction`. The first two
  reciprocal coefficients reduce it to the two gcds in (CCR6) over
  `F_8191`. Do not send a fourteen-root colored resultant to generic
  elimination. A unit verdict in both gcds closes only the constant chamber;
  degrees four through thirteen remain separate.

- Superseding close: consume
  `l1_mersenne_hnf_m16_order_one_constant_color_exclusion`. Both trace gcds
  are unit by the printed modular pseudo-remainders. Delete the complete
  `h=15` constant-color chamber and retire `CR-L1-H15-COLOR0`; the live
  `h=15` color degrees are exactly `4,...,13`.

- At degree two, consume
  `l1_mersenne_hnf_m8_order_one_quadratic_collision_router`. The exact
  chambers are collision-free, one repeat, or two antipodal repeats. In the
  last chamber put `d=c-1`, `r=rho*c` and adjoin
  `r(18+d-d^2)+192=0` before any generic elimination. The equation follows
  from the odd/even common factor and is not valid in the first two
  chambers. Intersect this smallest chamber with the proved `h=7` conic
  first.

- That intersection is now
  `l1_mersenne_hnf_m8_order_one_quadratic_two_pair_univariate_reduction`.
  Replace the two-antipodal conic packet by the printed degree-eight
  polynomial `F(d)` and test its gcd with `X^(p+1)-zeta` for the eight
  colors on each official row. This is 32 tiny gcd packets, not a generic
  elimination. Keep the collision-free and one-repeat chambers separate.

- For a retained exceptional-`J_*=0` cubic `3+2+1` role factor, consume
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_j0_outer_lift_compiler`.
  Work in the proved generated field `F_(p^8)`, match the role root against
  at most 42 normalized ordered color pairs, and reconstruct the normalized
  cubic color polynomial from `F,G,B`. Check the inherited guards, one norm
  `d^(p+1) in mu_8`, and one assignment-preserving congruence
  `W^(p+1)=tau E mod L` for `tau in mu_8`. These imply the full outer
  divisibility `P|W^(8(p+1))-1`; do not construct a degree-`n` remainder or
  rerun a separate reciprocal surrogate. A retained candidate still owes
  the independent global inner lift. This compiler is not an emptiness
  result and does not apply to the other h=7 shapes.

- Before replaying any retained exceptional-`J_*=0` candidate, consume
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_j0_guard_compiler`.
  In scaled coordinate `X=dW`, construct `Qhat,Ghat,Fhat,Lhat`. The former
  common-quadratic saturation is exactly
  `aB(lambda-1)Q(y)=R_j^2/d^6`; do not carry its four factors as separate
  tests. After a normalized color pair is matched, exact fiber multiplicity
  requires only `disc(Qhat)disc(Fhat)!=0`, while split-root coprimality is
  `Lhat(-1)!=0` and `K_6=Lhat(0)`. Apply the printed algebraic ledger to
  each factor/eta/color candidate and retain named rejection reasons. This
  is not a guard outcome: passing candidates still owe the norm, degree-six
  outer congruence, and independent inner lift.

- Before expanding another colored-Frobenius subchart, consume
  `l1_mersenne_hnf_payoff_scope_router`. The post-atlas minimum-width ledger
  has 42 row/degree obligations: `4` at `m=4,h=2`, `24` at
  `m=8,h=2,...,7`, and `14` at `m=16,h=2,...,15`. Full `h=7` and `h=15`
  closures remove only five cells, while the exceptional J-zero cubic
  `3+2+1` chart alone removes none. Treat a proper subchart as bankable local
  algebra, not a critical close. Even ownership of the complete `t=p`
  residual only advances the generic packing width to `p+1`; wider exchanges
  and the Toeplitz/Pade or aggregate first-owner payment remain live.
