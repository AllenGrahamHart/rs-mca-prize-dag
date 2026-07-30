# Rate-half adjacent-certificate attack contract

This file records the forward-facing attack on the MCA part of this node.
Historical floor-band and list-side material in `statement.md` is not the
current seam.

## KoalaBear v4 owner ledger

The PROVED `rate_half_kb_v4_tangent_source_atom` imports upstream PR `#1049`
at its exact architecture and partition digest. At the deployed KoalaBear
candidate `a=1116048`, one canonical sparse translation pays only

```text
U_paid=n-a=981104,
B*-U_paid=274980728110413983.
```

The same first-match partition leaves `U_Q`, `U_BC`, and `U_new` unpaid. A
KoalaBear upper certificate must bound those three cells within the printed
reserve under this exact chronology. Do not import the legacy M1 owner total,
sum over alternative sparse translations, or promote the row without its
adjacent unsafe half. This atom needs no large computation; any future
deployed census should first freeze an exhaustive compiler for one of the
three unpaid predicates and be registered in `notes/PRIZE_COMPUTE_REQUESTS.md`
before paid execution.

## KoalaBear Q6 u2 structural reduction

Two PROVED upstream-derived route cuts now constrain the `Q=6,s=6,u=2`
equality-wall residue. The complete-source saturation identity

```text
sum_(i=1)^12 div(H(alpha_i,X))=2 div(B)
```

excludes every conic-image component. For every remaining actual
birational-quartic component, the degree-60 endpoint map cannot have
primitive geometric monodromy: the nine primitive degree-60 groups have no
subdegree four. The pole and Riemann-Hurwitz ledger leaves exactly the inner
degrees

```text
{2,3,4,5,6,10,12,30}.
```

The PROVED divisor adapter now shows that all eight rows preserve the local
60-point active divisor and 12-point source divisor as complete geometric
fibers. For inner degree five, the two index-five source points exhaust
Riemann-Hurwitz, so the inner map is a normalized fifth-power map. Since
`gcd(5,p^6-1)=1` for `p=2130706433`, fifth power is injective on the deployed
field and cannot have the required five-point rational active fiber. Thus
degree five is deleted and the live necessary set is

```text
{2,3,4,6,10,12,30}.
```

Upstream PR `#1130`, replayed in the PROVED source-pencil compiler, closes the
endpoint coefficient-field ambiguity: two rational active fibers give a
target transform of `h` and the corresponding outer map over `F_(p^6)`.
It also routes every degree-30 map through inner degree six. Thus the
distinct live necessary set is

```text
{2,3,4,6,10,12}.
```

Degree 12 has one canonical pencil `<A,N_0>` and one exact six-dimensional
membership test. Degree two has a challenge-field deck involution; if a
future same-record bridge places it on the prime-field carrier, the only
projective carrier folds are power-pair or fixed-point-free reciprocal-pair.

The next local theorem must exclude or assign a first-match owner to each of
these six rows by descending witness data and chronology from the endpoint
parameter line to the evaluation carrier. None of the structural cuts moves
the owner ledger, proves `u=2` empty, establishes cap `68`, or closes the
KoalaBear row. The parameter line and carrier remain distinct.

Upstream PR `#1131`, replayed in the PROVED rank/transverse compiler, removes
the same-inner-fiber branch after strict right-factor routing. The six source
profiles have 32,099 canonical templates per supplied endpoint record, with
exact rank and active-syndrome gates; this is not a global endpoint census.
Every terminal actual quartic is transverse and satisfies

```text
delta*r=4m,       delta<=m^2,       r<=60/m-1.
```

There are 26 resulting `(m,r,delta)` types. Exact controls show that
source/active divisor gates alone genuinely admit indecomposable degree-two
and degree-three pencils, so further source-only rank work cannot close the
branch. The next theorem must impose the actual quartic/source-star incidence
on the 26 transverse types and terminate each in contradiction, a strict
coarser decomposition, or a chronology-valid carrier/data/slope owner.

The PROVED `rate_half_kb_m12_outer_subdegree_route_cut` supplies the first
direct outer reduction. At `m=12`, the outer degree-five map has one rational
total pole and five distinct rational zeros. Primitive degree-five monodromy
excludes `r=3`; `r=1` would make the cover cyclic and hence a normalized
fifth-power map, contradicting fifth-power injectivity on `F_(p^6)`. Thus
only `(r,delta)=(2,24),(4,12)` survive at `m=12`, and the global transverse
frontier drops from 26 to 24 types. No owner charge moves.

The PROVED `rate_half_kb_m12_r4_low_genus_branch_profile_reduction` sharpens
the `r=4,delta=12` survivor. The actual component has normalization genus at
most three, so Riemann-Hurwitz forces the outer component to have genus at
most one. Exact tame degree-five branch-cycle enumeration leaves five rows:
`A5` profiles `(3),(2,2)` and `(3),(3)`, and `S5` profiles `(2),(3,2)`,
`(2),(4)`, and `(2),(2),(2,2)`. Tame polynomial `AGL(1,5)` and the genus-two
and genus-three profiles are excluded. The five rows remain unpaid; the
separate dihedral `r=2` survivor is deleted by the later diagonal-socle cut.
No owner charge moves.

The PROVED `rate_half_kb_m12_outer_normal_form_compiler` removes arbitrary
outer-quintic search. Geometrically, the dihedral row is a Dickson quintic
`x^5-5a*x^3+5a^2*x`; four `r=4` branch profiles have rigid printed forms,
and the last is the one-parameter family `x^2(x-1)^2(2x-5t)`. This is a
geometric affine classification, not challenge-field coefficient descent.
The next exact endpoint test must compile the outer coefficients from the
canonical `<A,N0>` pencil, certify any required descent, and then impose the
actual quartic/source-star incidence. No owner charge moves.

The PROVED `rate_half_kb_m12_split_fiber_arithmetic_descent` uses the five
simple rational outer zeros: identity Frobenius on that split fiber forces
arithmetic monodromy to equal geometric monodromy, so every outer component
is defined over `K`. It also gives `K`-affine normalizations for the rigid
`A5 (3),(2,2)`, `S5 (3,2),(2)`, and `S5 (4),(2)` forms. Only three descent
twists remain: Dickson, `A5 (3),(3)`, and the one-parameter `S5` family.
This descent argument alone deletes no family; the later diagonal-socle cut
removes Dickson. No owner charge moves.

The PROVED `rate_half_kb_m12_diagonal_socle_route_cut` uses the composition
monodromy rather than more coefficient casework. The derived block kernel
is a subdirect product of five nonabelian simple degree-12 socles. Scott's
lemma and the primitive degree-five block action make it either independent
or one full twisted diagonal. The actual size-four non-same-fiber suborbit
excludes independence. Exact cross-action orbits, including the two
outer-automorphism-related `M12` actions, then force that suborbit to contain
one synchronized point in each of four outer blocks. Hence `r=2` is empty
and only `(r,delta)=(4,12)` survives. The exact `m=12` frontier is now the
five printed `r=4` families with a synchronized diagonal correspondence;
the global transverse frontier drops from 24 to 23 types. None of the five
families is yet deleted or owned, and no charge moves.

The PROVED
`rate_half_kb_m12_secondary_degree5_decomposition_exclusion` closes the
remaining branch. Equivariant identification of the five equal degree-12
socle actions makes every normalizer element act by one common permutation
on their 12-point coordinate: the action centralizer is trivial. Hence the
degree-60 monodromy preserves twelve secondary blocks of size five. This
forces an inner-degree-five decomposition of the same endpoint map, which
the deployed-field degree-five theorem already excludes. Thus all five
`r=4` families are empty, `m=12` is fully closed, the global transverse
frontier drops from 23 to 22 types, and the live degrees are
`2,3,4,6,10`. No owner charge moves.

The PROVED `rate_half_kb_m10_scott_strip_lower_degree_router` removes inner
degree `10` as a terminal producer. The nine primitive degree-10 groups have
simple socle `A5`, `A6`, or `A10`. A trivial block-kernel projection forces
the exact `A6` or `S6` degree-60 point/two-subset flag action, whose complete
subdegree list has no four. Otherwise Scott strips in the six original
blocks have common size `1,2,3,6`; size one gives a forbidden ten-point
orbit, while the other sizes preserve synchronized column blocks and force
a second decomposition of inner degree `2`, `3`, or `6`. Thus all four
`m=10` transverse types route strictly downward. The independent frontier
drops from 22 to 18 types in live degrees `2,3,4,6`. Endpoints are not
claimed to lack every degree-10 decomposition, and no owner charge moves.

The PROVED `rate_half_kb_m6_scott_cartesian_degree2_router` removes inner
degree `6` as an independent producer. If the ten-block kernel is trivial,
the complete transitive degree-ten catalogue leaves four wreath actions
whose endpoint-stabilizer chains all have an intermediate index-five
subgroup; `A10,S10` have no primitive degree-six point-stabilizer quotient.
Thus the kernel-free branch hits the already excluded degree-five row. With
nontrivial kernel, Scott-compatible synchronized columns have size five or
ten. Size five is excluded; in size ten the actual four-point orbit lies in
one column, so the degree-ten column map has a forbidden same-fiber
subdegree four and factors to degree two or five. Thus every `m=6` producer
dies or routes to `m=2`. The independent frontier drops from 18 to 12 types
in live degrees `2,3,4`. Degree two is not deleted or paid, and no owner
charge moves.

The PROVED `rate_half_kb_m4_outer_a6s6_route_cut` removes three of the four
inner-degree-`4` types. For an indecomposable outer degree-`15` map, the
complete primitive catalogue has nontrivial subdegrees `14`, except for
the `A6,S6` two-subset actions with subdegrees `6,8`. Hence `r=1,2,4`
force a proper outer right factor of degree `3` or `5`, which gives the
endpoint an impossible inner degree `12` or `20`. Only
`(r,delta)=(8,2)` survives, with outer monodromy `A6` or `S6` on the
15 two-subsets of six points. A five-cycle acts as `5^3`, so the pole
profile does not delete it. The independent frontier has nine types: three
at `m=2`, five at `m=3`, and this single `m=4` survivor. No owner charge
moves.

The PROVED `rate_half_kb_m4_a6s6_genus_zero_passport_reduction` exhausts the
survivor's branch-cycle classes. Riemann--Hurwitz leaves residual index 16
after the mandatory `5^3` pole. Nine parity-compatible class budgets exist,
but exact product-one enumeration shows five generate only `A5` or `S5`.
Exactly four geometric passports remain: the three-point rows
`A6:(5.1,2.2.1.1,4.2)`, `S6:(5.1,2.1.1.1.1,6)`, and
`S6:(5.1,2.2.2,3.2.1)`, plus the four-point row
`S6:(5.1,2.1.1.1.1,2.2.1.1,2.2.2)`. Attack the rigid three-point rows first
through challenge-field split fibers and the quartic source-star incidence;
do not enumerate arbitrary degree-15 maps. The `m=4` type and all owner
charges remain open.

The PROVED `rate_half_kb_m4_s6_652_pair_quotient_normal_form` constructs the
rigid `S6:(5.1,2.1.1.1.1,6)` row exactly. It normalizes the unordered-pair
resolvent of the pinned degree-six companion to a rational degree-15 map with
fibers `(6,6,3)`, `(5,5,5)`, and `(2,2,2,2,1,1,1,1,1,1,1)`. The order-five
fiber is `{-77,22+33sqrt(5),22-33sqrt(5)}` and therefore splits over the
even-degree KoalaBear field. Pole descent cannot delete this row; its fixed
active fiber and quartic source-star incidence remain open, as do the other
two rigid passports and the four-point family. No owner charge moves.

The PROVED `rate_half_kb_m4_s6_562_pair_quotient_normal_form` constructs a
second rigid row, `S6:(5.1,2.2.2,3.2.1)`, from a cubic-adjoint pencil on its
unordered-pair quintic. Its exact branch fibers are `(5,5,5)`,
`(6,3,3,2,1)`, and `(2,2,2,2,2,2,1,1,1)`. The order-five points consist of
one rational point and two points over `Q(sqrt(5))`, hence also split over the
even-degree KoalaBear field. Two of the three rigid maps are now explicit;
the `A6` rigid cover, four-point family, active-fiber test, and quartic
source-star incidence remain open. No owner charge moves.

The PROVED `rate_half_kb_m4_a6_542_pair_quotient_normal_form` constructs the
third rigid row, `A6:(5.1,2.2.1.1,4.2)`, over
`Q(nu)`, `nu^2-nu+4=0`. Its exact branch fibers are `(5,5,5)`,
`(4,4,4,2,1)`, and `(2,2,2,2,2,2,1,1,1)`. Both coefficient-field
embeddings already lie in the KoalaBear base field, and the order-five
linear-plus-quadratic divisor is distinct and split over `F_(p^6)`. All
three rigid maps are now explicit and pole descent deletes none of them.
Attack their fixed active fibers and quartic source-star incidences next;
the four-point family remains separate. No owner charge moves.

The PROVED `rate_half_kb_m4_adjacency_genus_exclusion` supersedes that
incidence search for deletion. The unique `r=8` orbital is the connected
120-sheet action on ordered adjacent two-subsets. Its genera in the three
rigid passports and the four-point family are respectively `3,6,4,13`.
The actual source normalization is birational to a bidegree-`(2,4)` curve,
so has genus at most three, while its map to the outer orbital has separable
degree two. Riemann--Hurwitz would require source genus at least
`5,11,7,25`. Thus all four passports are impossible for an actual endpoint,
the complete independent `m=4` row is empty, and the frontier drops from
nine to eight types: three at `m=2` and five at `m=3`. No owner charge moves.

The PROVED `rate_half_kb_m3_primitive_outer_degree2_router` removes all five
degree-three types as independent producers. The complete primitive
degree-20 catalogue is `PSL(2,19),PGL(2,19),A20,S20`; every row is
two-transitive with subdegrees `1,19`, so none supports
`r in {2,3,4,6,12}`. The outer map therefore decomposes. Its proper right
factor gives inner degree `6,12,15`, or `30`; the existing closures and
routers make each destination impossible or furnish an inner-degree-two
decomposition. An endpoint may still have an additional degree-three
decomposition, but it is not independent. The live independent frontier is
the three `m=2` types `(r,delta)=(2,4),(4,2),(8,1)`. No owner charge moves.

The PROVED `rate_half_kb_m2_v4_outer_recurrence_router` now removes the
primitive-outer ambiguity without pretending to close those three rows.
For the quadratic deck group `V4`, the restriction degree `delta` is the
setwise stabilizer order of the actual component. Thus the three types are
respectively full-V4, order-two, and trivial-stabilizer cases. The complete
primitive degree-30 catalogue has only subdegrees `1,29`, so every outer map
decomposes; the complete proper-factor ledger either dies in a proved row or
returns to `m=2`. In every case containing the first-coordinate deck
involution, including all of `(2,4)`, the source lift is the diagonal
endpoint/source-deck involution, paired source rows avoid both paired
locators, and the weight-three source-star defect is impossible. The next
attack must break this recurrent tower with the actual equivariant source
equations or produce a same-record owner; another abstract decomposition
cycle does not move the frontier. No owner charge moves.

The PROVED `rate_half_kb_m2_r2_full_v4_source_genus_drop` sharpens the
full-V4 `(r,delta)=(2,4)` row. The source projection gives an involution
`eta`, while the diagonal endpoint/source-deck lift `a` makes the degree-four
map to `W` a V4 cover. The second endpoint involution conjugates `eta` to
`eta*a`; the alternative would factor the quartic coefficient map through
a quadratic source quotient and return to the excluded line/conic branch.
Tame fixed-point Riemann-Hurwitz leaves exactly source genus zero with two
fixed points of `a`, or source genus one with none. Genus two and three are
impossible. Neither rational nor elliptic regime is yet deleted, and the
other two `m=2` types are unchanged. No owner charge moves.

## Banked range

Put

```text
N=2^41,       k=R=2^40,       B=floor(q/2^128).
```

For every admissible `2^128<q<2^167`, the adjacent agreement is proved to be

```text
a_RH(q)=N-B+1.
```

At the same candidate, the sparse MCA layer and the adjacent unsafe witness
are already paid through `B<=2^39+1`. The only missing condition for the two
next budgets is therefore

```text
B_ca^far(N-B+1)<=B.                                  (K5-CA)
```

By `rate_half_residual_prime_field_collapse`, every admissible field in these
two budget intervals is a prime field `F_p`, with `p>2^167` and
`2^41 | p-1`. Extension-field cases must not be allocated.

## Exact residual branches

Write `m=2^37`. The split-pencil and minimal-index theorems reduce `(K5-CA)`
to the following disjoint moving-kernel profiles.

### Strict budget `B=2^39=4m`

The locator radius is `r=4m-1`. Full-column-rank pencils and every deficient
profile with `A>=5` are proved. The residue is exactly

```text
A=3,       rho=r=4m-1,       s=0,
m<=e<=floor((4m-1)/3),       target T<=4m.
```

The first endpoint `e=m` can fail only at `T=4m+1`; it has the proved
rational-normal, norm-defect, component-chamber, and Hankel/apolar routers.
Those routers do not exclude it. For `e>m`, the slope-slack ledger writes

```text
T=4e+1-h,       0<=h<=4(e-m)
```

for every possible failure.

### Half-distance budget `B=2^39+1=4m+1`

The locator radius is `r=4m`. Profiles with `A>=5` are proved. The residue is
the union of

```text
A=3: rho=4m-1, s=0,
     m+1<=e<=floor((4m-1)/3), target T<=4m+1;

A=1: rho=4m, s in {0,1,2},
     m+1<=e<=floor((4m-s)/(1+s)), target T<=4m+1.
```

The `A=1,s=1,e=2m-1` sharp-cap face has the deepest current reduction. Its
distance-three branch is now closed by the PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_external_split_design_exclusion`:
the pair-crossing gate sends every exact design into the all-deficient
quartic-support branch, and the residual-discriminant theorem makes that
branch empty. The live `A=1` work is the high quotient-distance tail and the
other component faces. The strict and half-distance `A=3` profiles also
remain theorem work.

For the high quotient-distance tail, the PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_first_jet_transversality`
adds the first constraint not visible in the endpoint resultant matrix. At
every clean selected incidence `(gamma,y)`, with domain order `M=2^41` and
corrected-square exponent `N_sq=M+r-3`,

```text
F_t U W_vee=-P_cl' E y^N_sq,
dot y=-(P_cl'E/M)y^(r-2)(1-sy)(1-x_0y)/W_vee.
```

All factors are nonzero. Hence a live endpoint attack must classify the two
printed incidence profiles together with these prescribed first jets. A
resultant-multiplicity replay alone is route-incomplete.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_w_interpolation_normal_form`
then removes the global `W_vee` biform as a free object. Its clean-fiber
values determine one canonical `W_0` of parameter degree below
`deg P_cl`, and every survivor has

```text
W_vee=W_0+P_cl(t A_W+B_W),       deg A_W,deg B_W<=r-1.
```

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_unit_triangular_affine_reconstruction`
then eliminates both corrections. In ascending `Y`-degree, the unit equation
computes one canonical residue

```text
rho_k=-C_k^0(l_0P_cl)^(-1) mod f_0,       f_0=E q_bar.
```

Every survivor must have `deg rho_k<=1`; that affine representative uniquely
gives `(a_k,b_k)`, and exact division gives the next coefficient of `S`.
Thus a non-affine `rho_k` is an exact rejection certificate. A surviving
packet has a unique `W_vee` and must pass only the final exact-division,
degree-box, and Hankel checks. The next endpoint attack should classify those
deterministic checks; do not allocate a dense `W_vee` or correction
polynomials.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_unit_bezout_remainder_gate`
simplifies this further. Since `l_0P_cl+f_0a_minus=1`, write only

```text
C_k^0=f_0d_k+r_k,       deg r_k<e.
```

Then `rho_k=-r_k` and `s_k=d_k+a_minus r_k`. Therefore each stage is one
Euclidean division and survives exactly when `deg r_k<=1`; neither modular
inversion nor a second division should appear in a classifier.

There is now an independent clean-fiber check. The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_second_jet_hermite_gate`
differentiates the reversed first complement twice along every selected root.
It reconstructs `W_vee,t(gamma,Y)` on each clean fiber and normalizes it to

```text
D_gamma=(W_vee,t(gamma,Y)-W_0,t(gamma,Y))/P_cl'(gamma).
```

Every survivor must have `D_gamma=gamma A_W+B_W`. Any two slopes reconstruct
the pair, all other slopes must lie on the same affine line, and that pair
must equal the unit-remainder reconstruction. These are exact comparison
gates before the remaining Hankel checks.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_jet_quotient_ring_compiler`
makes both jet inputs root-free. In the quotient ring by `F(gamma,Y)`, all
needed denominators are units and the smooth-domain identity reduces
`Y^N_sq,Y^(N_sq-1)` to `Y^(r-3),Y^(r-4)`. Canonical modular representatives
are exactly `W_vee(gamma,Y)` and `W_vee,t(gamma,Y)`. This avoids selected-root
enumeration and huge exponents, but it does not authorize dense official
degree-`r` arrays; any scale-up needs compressed locator arithmetic.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_unit_resultant_log_trace_gate`
extracts an earlier scalar check from the same data. If
`q_0=[X^0]Q=[Y^r]F`, then every clean slope must satisfy

```text
Tr((W_vee,t+W_vee,Y dot y)/W_vee)
 =(N_sq+1)E'/E+N_sq q_bar'/q_bar-(r-1)q_0'/q_0.
```

The actual `X`-degree of `W` cancels. A trace mismatch rejects before the
full affine-Hermite comparison or any Hankel work.

The remaining Hankel constraints are now compressed by the PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_coefficient_biisotropic_plane`.
If `q(z)=sum_(i=0)^e z^i q_i`, then the `q_i` are independent and their
span has dimension `e+1`, with

```text
q_i^T M_0 q_j=q_i^T M_1 q_j=0       for all i,j.
```

This common isotropic plane meets `ker M_0` only in the exceptional locator
line and `ker M_1` only in the top coefficient line. The next endpoint proof
should classify this plane jointly with the trace/Hermite gates; it should
not allocate separate quadratic moment equations.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_coefficient_rank_one_flag`
adds `v=Xq_0` and identifies

```text
H_q=W_q+span{v}=W_q^(perp M_0)=W_q^(perp M_1).
```

On this `(e+2)`-plane, `M_0` is zero and `M_1` has rank one, with its only
nonzero Gram entry `v^TM_1v`. Thus the regular Kronecker line is already in
the original coefficient coordinates and must not be reintroduced as a
solver block.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_exceptional_self_dual_evaluation_code`
passes this flag to the exceptional roots. Evaluation kills exactly
`span{q_0,Xq_0}` and produces an `e`-dimensional code of length `2e` that is
self-dual under the nonzero exceptional weights. Its bases occur in
complementary pairs, with the exact weighted minor law

```text
Delta_J^2 product_J beta=(-1)^e Delta_I^2 product_I beta.
```

This is the current discrete Hankel interface for classifying the two
high-distance endpoint profiles.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_exceptional_split_incidence_self_dual_frame`
makes that interface explicit. Each exceptional column is the coefficient
vector of `g_a(z)=Q(z;a)/z`, a split degree-`e-1` polynomial whose roots are
its ordinary incidences. The `2e` columns form a weighted self-dual frame on
the `4e` clean slopes with exactly the flat or swapped replication ledger.
An exact `e=3,F_101` flat frame with six disjoint root pairs and nonzero
self-dual weights survives. Therefore the frame axioms alone are fenced;
the next exclusion must use official Forney values, smooth-domain placement,
or genuinely large-`e` structure.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_residue_self_dual_algebra`
now installs the Forney values. Normalize each `g_a` by its nonzero constant
`q_1(a)` and work in `R_A=F[X]/(A)`. The normalized coefficient space `U_q`
has dimension `e`, contains `1`, and is self-dual for the residue pairing
represented by

```text
C=q_1 Phi/B_T mod A.
```

Its product span satisfies `dim U_q^2<=2e-1`. At equality, the frame
determines `C` up to scalar and must match the Forney class; lower dimension
is a separate degeneracy branch. This product-space dichotomy is the current
Hankel endpoint target.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_mds_schur_router`
sharpens that split. If the normalized exceptional code is MDS, its Schur
square has dimension exactly `2e-1`, so the frame uniquely determines the
Forney class up to scalar. Otherwise there is an `e`-set of exceptional
columns and its complement whose two determinants both vanish. The next
proof should compare the unique class on the MDS branch, or exploit the
paired split-polynomial dependence on the non-MDS branch.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_mds_half_dimension_non_grs_route_fence`
blocks a tempting overpromotion of the first branch. An exact `[8,4,5]`
Euclidean self-dual code over `F_11` has square dimension seven but is not
GRS, certified by the absence of linear syzygies among its three quadrics.
This is exactly the `n=2k` exception to ordinary Schur-square rigidity. The
official MDS branch must therefore use its split-incidence columns, Forney
normal, or smooth-domain placement; abstract MDS plus self-duality plus
minimal square does not yield a rational-normal curve.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_non_mds_annihilating_pair_router`
replaces the complementary-minor description on the other branch by a
quotient-algebra target. Non-MDS yields independent nonzero `u,v in U_q`
and complementary exceptional halves `I,J` with `u|_I=0`, `v|_J=0`, hence
`uv=0 mod A`. The next non-MDS proof should exclude this annihilating pair
using the official split coefficients or Forney residue form; it should not
enumerate the `binom(2e,e)` maximal minors. Canonical gcds give a sharper
dichotomy: either one element has at least `e+1` exceptional zeros, or
`A=D_uD_v` is an exact factorization into complementary degree-`e` zero
locators. These are the two non-MDS subbranches to exclude. Because `q_1`
is a unit, each `D` is the gcd of `A` with a direct linear combination of
`q_1,...,q_e`; no quotient-ring inverse is part of the certificate. If the
two half-restrictions have deficiency `d`, weighted self-duality makes the
deficiencies equal and supplies `d`-dimensional annihilator spaces on both
halves, with `d<=floor(e/2)`.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_non_mds_support_residue_gate`
adds the first support-side obstruction to either subbranch. Put
`K=H_lambda H_nu/A`. Hankel `M_1` isotropy and the Forney support weights
force

```text
[X^(h-1)] rem_(B_T)(Phi K A^(-1))=0.
```

In the exact-half branch `K=R_uR_v`; the excess branch retains its overlap
factor. Any nonzero top coefficient rejects the annihilator pair before
further Hankel reconstruction. Equivalently, a global-residue transfer gives

```text
sum_(A(a)=0) beta_a q_1(a)K(a)
 =0                         if deg K<=2e+1,
 =Theta_2 lc(K)             if deg K=2e+2.
```

This alternate form avoids reduction modulo the huge support locator when
the exceptional/source representation is the compressed side available.
For deficiency `d`, both forms hold entrywise for the full `d`-by-`d` matrix
of cross annihilators; a checker must not discard these extra equations.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_norm_discriminant_square_gate`
adds a router-independent scalar obstruction. Both branches must satisfy

```text
Res(A,q_1) Res(A,Phi)
---------------------  in (F_field^x)^2.
 Res(A,B_T) Disc(A)
```

Thus a nonsquare candidate is rejected before MDS classification or minor
enumeration. However, the PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_norm_square_cancellation_fence`
shows that after the full Forney/self-dual packet is imposed this expression
is exactly

```text
(-1)^e Norm_A(Beta) Res(A,q_1)^2,
```

and the first factor is already square by weighted self-duality. Directly
computing this quantity from a complete packet is therefore an audit, not a
new endpoint attack. It can exclude a profile only through an independent
profile-level formula that forces the opposite class.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_endpoint_derivative_resultant_reciprocity`
already performs the first such extraction. In the flat profile it gives

```text
Res(A,q_1)/Res(A,q_e)=P_ord(0)^k_0,
```

and the swapped profile adds the factor `z_min/z_max`. Since the official
`k_0=2^37-1` is odd, this pins the square class of the ratio from three
printed field elements. This ratio occurs squared in the cancelled norm
gate, so its remaining value is instead a structural invariant of the top
normalized coefficient `p_(e-1)=q_e/q_1`. The live routes remain the
MDS/non-MDS structural split or a genuinely independent smooth-domain
identity, not a standalone norm computation.

Paying both displayed budgets would extend the exact adjacent determination
through `q<(2^39+2)2^128`. It would not close this whole TARGET node: the
larger-budget rate-half bracket recorded in `statement.md` would remain.

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

## Compute custody

All substantial computation belongs in `notes/PRIZE_COMPUTE_REQUESTS.md`
under `CR-003`. A request is executable only after it has a proved
completeness router, resumable implementation, measured pilot, hard resource
ceiling, compact certificate, and deterministic checker. Raw split-locator,
support-subset, or biform sweeps are not authorized. Runs at or above the
local time/cost policy are contributor requests for an upstream PR, not local
Modal jobs.

## STRICT A=3 ENDPOINT: TRANSPOSED NORMAL FORM + NORM ROUTE FENCE (2026-07-26)

Full record: `notes/strict_endpoint_norm_route_fence_20260726.md`; artifact
`verify_strict_endpoint_norm_fence.py`.

Two restatements of the strict `B=2^39`, `e=m`, `h=0` sharp-cap endpoint. (a) is
SSL14 in resultant language; (b) is its transpose and was not on record.

```text
(a)  Res_X( X^N - c , Q(U,V;X) ) = H(U,V)^(4m-1) S(U,V),   S linear   [O=0]
(b)  (X - x_0) product_(gamma in Z) Q_gamma(X) = kappa (X^N - c)^m,
     kappa = product_gamma c_gamma,        1 + (4m+1)(4m-1) = 16m^2 = Nm.
```

Form (b) exhibits the endpoint as a factorization of an `m`-th power of the
smooth-domain polynomial into `4m+1` members of the `(m+1)`-dimensional space
`W=span(Q_0..Q_m)`, which lie on a degree-`m` rational normal curve in `P(W)`
(SSL4), plus one linear factor.

**FENCE — do not attack this endpoint by subgroup-norm or multiplicative-parity
arithmetic.** Comparing leading and constant coefficients of (b) gives, with
`pi_gamma = product_(x in Rt(gamma)) x`,

```text
product_(gamma in Z) pi_gamma = (-c)^m / x_0.                      (NORM)
```

(NORM) is a **consequence of the covering ledger, not a constraint**: it equals
`product_x x^(d_x) = (product_x x)^m / x_0` identically, so the two derivations
are the same identity and comparing them is circular. Verified to hold on 160
combinatorial covers with the endpoint multiplicities and no algebraic
realizability whatsoever. In cyclic-exponent form the congruence needs
`m*(N/2) = 0 mod N`; at official scale that is `2^77 = 0 mod 2^41`, vacuous with a
**36-power-of-two margin** — not a near-miss a sharper constant could rescue.

What survives is the live target: whether `4m+1` totally-`D`-split degree-`4m-1`
polynomials can lie on a degree-`m` rational normal curve in an `(m+1)`-dimensional
space with each domain point covered exactly `m` times (one point `m-1`). The
information is in the linear-series/RNC interaction with the split condition; the
multiplicative bookkeeping is now closed off.

Excludes no stratum and closes no budget; this node stays TARGET.
