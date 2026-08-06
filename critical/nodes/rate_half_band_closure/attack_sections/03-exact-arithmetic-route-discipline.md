
## What exact arithmetic can and cannot do

The "exact binomial ladder" cited by kernel-basis log item 115 is an
efficient way to replay neighboring huge binomial values. It is not a
split-pencil theorem and does not imply `(K5-CA)`. It may be used for final
row arithmetic after a uniform CA bound is proved, but a binomial-only run
cannot close either residual budget.

The preferred proof routes are:

1. exclude the rational-normal split-specialization profiles using their
   Hankel/apolar origin, not only their grid incidence counts;
2. prove a uniform slope bound stronger than the root-incidence cap;
3. classify a complete algebraic face with an independently checkable
   nonexistence certificate.

The proved route fence
`rate_half_ca_hankel_strict_m1_corefree_five_slope_route_fence` shows why the
first item must use official-scale structure. At `m=1`, a core-free,
constant-rank Hankel pencil has exactly five split slopes against the cap
four; all sixteen maximizing locator lines pass the Hankel compatibility
gate. The survivor has separation rank two and is a separated pullback, so
the official `m>1` component-rank and non-pullback theorems are load-bearing.

On the abstract `A=1,s=1` distance-three face, generic rank-three pair
locators alone do not force saturation of the `3e+1` quadratic-product cap.
The proved
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_generic_schur_square_saturation_route_fence`
constructs arbitrary-size
rank-three fiber families with product rank at most `3e`; its pinned `e=12`
fixture has ranks `37 -> 36`. The defect classification recovers the unique
rational map behind every such rank drop, and the proved
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_official_trigonal_subgroup_exclusion`
then excludes that map on the official order-`2^41` subgroup. Exact
Schur-square saturation is therefore a proved official conclusion, not an
abstract premise.

The generic defect is nevertheless classified exactly. Solve the linear
system

```text
D_i | R-y_iB,       deg R<=2.
```

Its nullity equals `(3e+1)-dim(VV)` and is at most one. Nullity zero is the
rank-`3e+1` saturated generic branch. Nullity one recovers a projectively
unique rational map `B/R`, but the official subgroup theorem makes this
branch empty. Any official generic quadratic rank below `3e+1` is now an
immediate rejection certificate.

Do not try to close the remaining saturated branch from biregularity and
the two uncalibrated rank shadows. The proved
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_saturated_cyclic_design_residue_route_fence`
constructs an exact `e=5` cyclic design with `6e+3` distinct blocks,
replication `2e+1`, quadratic rank `3e+1`, and complement span `e+4`.
It is rejected only after reducing complements modulo an internal locator:
every such residue matrix has rank at least four. A viable generic exclusion
must therefore use the calibrated rank-three residues jointly with external
incidence, boundary values, or the resultant power; replacing them by the
coefficient-span bound loses the live information.

The proved
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_calibrated_conic_kernel_lift_normal_form`
makes that live information explicit. With `s_x=B(x)G_x(0)`, there are fixed
degree-less-than-`e` polynomials `R_0,R_1,R_2` such that

```text
s_xH_x=R_0+xR_1+x^2R_2+I J_x,       deg J_x<=e,
product_x(s_xH_x)=kappa P_Z^(4e+2).
```

The three `R_j` are independent on the surviving generic branch, and
`[z^e]J_x=s_x`. Thus the next target is a theorem controlling the kernel
lifts `J_x` from the displayed perfect-power identity and exact incidence.
The residue conic alone is not a projective locator pencil, so the upstream
moving-root theorem cannot be invoked until such control or a proved pencil
decomposition is supplied.

The proved
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_cleared_lift_quartic_router`
now supplies the first such control. The first jets at the internal slopes
give explicit rational values `J_x(xi_i)=N_i(x)/E_i(x)`, with
`deg E_i=2e+1` and `deg N_i<=2e+3`. Clearing their common denominator gives
a biform `F` with

```text
deg F<=(2e,4e+6),       F(z;x)=(A(x)B(x))^2H_x(z).
```

At every external slope `gamma`, its exact `4e+2` nonincident active rows
factor out:

```text
F(gamma;X)=K_gamma(X)T_gamma(X),       deg T_gamma<=4.
```

These slopewise factors glue after the exact normalization

```text
FQ=(AB)^2q_eP_Z+C z I^2 Omega,       deg Omega<=(e-2,4),
Omega(gamma)=ell_gamma T_gamma/(gamma I(gamma)^2).
```

This is the current generic saturated interface. Degree four is sharp on
the exact `e=1` Hankel fixture, where the three cofactors are not
base-field split. Do not treat `T_gamma` as fixed or split. The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_boundary_crt_reconstruction`
now pays the boundary step exactly: in `F[X]/(A)`, divide
`sum_i D_iN_iL_i` by the CRT factor `z-delta`, multiply by the explicit
subgroup derivative factor, and reduce modulo `A`. A valid packet must have
no `X^j` coefficient for `5<=j<2e`; a deterministic random `e=3,F_97`
pair-Lagrange packet fails at degree five. The next theorem should couple
this exact degree-collapse system to the perfect-power or source identities.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_boundary_dual_moment_gate`
gives the interface: `2e-5` vector-valued dual-RS moments in which `C` and
`A'` cancel, expressible as base-field traces over the paired quadratics.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_boundary_torus_kernel_reduction`
packages them as `T theta=0`, where
`theta_i=xi_iP_Z(xi_i)/lambda_i^2` has no zero coordinate. On the official
field, full rank or one coloop column excludes the packet exactly. The
PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_internal_slice_lambda_cube_kernel`
moves the first gate earlier: an `e(2e-7) x e` matrix `U`, depending only on
support pairs and internal slopes, must kill the cube vector
`(lambda_i^3)`. The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pair_crossing_rank_gate`
moves earlier again. For each omitted pair an `(e-1) x 5` support-only matrix
must have a quartic kernel vector nonzero on every other pair. Rank five
excludes, and the `e=6,7` controls attain it for every omitted pair. Target a
uniform rank-five theorem or classify the deficient matchings; only those
should proceed through `U`, `T`, and any eventual line decomposition.
Do not replace the smooth weight by arbitrary nonzero pair weights: the
proved antiweight fence `H(b_k)=-H(a_k)` leaves `P_l=D_l^2` in every kernel.
The multiplicative-domain form `H=X(X-s)(X-x_0)B^4(A')^4` is load-bearing.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_low_degree_fiber_reduction`
classifies the all-deficient official branch further. It is either the
actual global antiweight identity, or at least `e-4-9d^2` pairs are fibers
of one separable base-field map of degree `d in {2,3,4}`; uniformly at least
`e-148` pairs are captured. Degrees `5,...,8` are excluded by the exact
ramification/divisibility argument in that node. Attack these four branches
directly. Do not resume an unrestricted support/matching census, and do not
assume the bounded exceptional tail is zero.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_two_three_subgroup_reduction`
removes degree three and classifies degree two. The latter has one fixed
antipodal or constant-product involution on at least `e-40` pairs, with at
most forty tails at this coarse stage. The open support list is therefore
global antiweight, bounded-tail dihedral, and degree four. The downstream
tail-rigidity theorem sharpens this to six/eight before the trace repair;
the existing zero-tail closures still cannot simply be cited.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_antiweight_absorption`
uses the actual internal-slice values to absorb global antiweight as well.
At most two actual quartics can be squared pair locators; the rest force a
common degree-two or degree-four field after degree three is removed. The
complete all-deficient list is therefore bounded-tail dihedral or degree
four. Preserve the abstract antiweight fixture as a support-only route fence,
but do not retain antiweight as a third exact-design branch.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_four_irreducible_router`
pays all ordinary absolutely irreducible degree-four maps. The remaining
degree-four alternatives are a geometrically reducible coincidence divisor
or the explicit Laurent-end curve
`XY[X^2+XY+Y^2+a(X+Y)+b]=d`. Its currently audited constant `5376` exceeds
the official margin, so do not cite the generic subgroup estimate as a
closure. Target the Laurent structure or classify the reducible quartic
tower.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_four_reducible_deck_router`
completes that classification. Every reducible quartic map is
`F(X^2)`, `F(X^4)`, or `F(X+c/X)` with subgroup-valued deck symmetry. The
only non-pullback quartic branch is now the absolutely irreducible
Laurent-end curve. Couple the pullbacks to the existing dihedral ledgers;
do not run a generic reducible-factor search.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_laurent_gcd_exclusion`
removes the Laurent-end curve using the Corvaja--Zannier gcd theorem with
`chi<=18`. The all-deficient frontier is now pullback-only: bounded-tail
antipodal/constant-product matching, or `F(X^2)`, `F(X^4)`, `F(X+c/X)`.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_bounded_tail_dihedral_row_codegree`
shows that `t` off-involution pairs create row codegree at most `t`, with at
most one identical-row orbit. The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_two_tail_rigidity`
sharpens the exact-design loss to six antipodal tails or eight
constant-product tails. Extend the zero-tail complement trace to
`K_u=P_Z gcd(q_x,q_tau(x))/(q_xq_tau(x))`, of degree at most `e+8`, or
produce a calibrated bounded-tail survivor. The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_bounded_error_pade_circuit_reduction`
does the first extension: nonzero 14-point/18-point Pade determinants are
paid by degree, while an official survivor forces respectively more than
`9999/10000` or `991/1000` of the relevant circuits to vanish identically.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pade_relation_class_reduction`
classifies them as subsets of unique degree-`t` rational relation classes.
Its shadow ledger forces one class of at least `172410` slopes antipodally
or `2128` for constant product. Prove the uniform upper bounds `172409` and
`2127`, or a sharper aggregate class payment. The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pade_large_class_static_denominator`
shows every class this large has static `B(Z)` and quadratic numerator in
`U`; its class polynomial divides `IA_2+M_0B`, `IA_1-2M_1B`, and
`IA_0+M_2B`, as well as `P_Z`. Prove the corresponding simultaneous gcd
bounds with `P_Z`; an unrestricted residual gcd bound is unnecessary. In parallel,
the PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pullback_involution_absorption`
routes `F(X^2)`, `F(X^4)`, and `F(X+c/X)` into the same six/eight-tail
interface. There is no independent quartic-pullback or generic quartic-map
search left. The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pade_aligned_residual_degree_four`
factors the large class from at least `e-33/e-44` aligned complements and
leaves a degree-`1..4`, quadratic-in-parameter split-divisor pencil with
every residual root used at most twice. The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pade_residual_discriminant_exclusion`
closes this leaf. Ratios of calibrated internal evaluations force each good
specialization in the internal variable to be a square norm. More than eight
such slopes annihilate the degree-at-most-eight parameter discriminant.
Squarefreeness then makes every aligned residual proportional to one fixed
polynomial, contradicting projective distinctness. The complete
all-deficient quartic-support sub-DAG is closed; do not launch tail,
circuit, static-gcd, pullback, or low-degree-pencil fleets for it.

Small analogues are falsification and route-selection evidence only. A
positive analogue is useful as a counterexample to an over-strong proposed
lemma; a no-hit analogue never proves the official uniform statement.
