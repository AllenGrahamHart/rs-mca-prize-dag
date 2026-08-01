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

The PROVED
`rate_half_kb_m2_r2_dihedral_residual_quartic_singularity_atlas` closes the
coefficient-geometry audit. Every allowed `Q_(a,b)` is geometrically
irreducible and rational. For `b!=a` it has three ordinary nodes; at `b=a`
two move to infinity and form one tacnode, while the third node remains.
The total delta is always three. Therefore no allowed residual parameter can
be deleted by another factorization or genus argument. The next attack must
substitute the six order-five pole fibers and complete source locators into
the printed one-parameter normal forms. No owner charge moves.

The PROVED
`rate_half_kb_m2_r2_dihedral_residual_source_cover_twist_classifier` retains
and then removes the relative second-endpoint ambiguity. If `Z=ell(Z_0)`
and `d^2=a+2`, equality of the two quadratic source subextensions forces

```text
ell^(-1)({2,b})=roots(z^2-b*d*z+b^2+d^2-4).
```

The values at the standard branch points are `(b-d)^2` and `(b+d)^2`.
Hence the rational source regime is exactly `b^2=a+2`, while its complement
is the elliptic regime. Both remain possible; the common degree-30 function,
six pole fibers, and source locators are the next live equations. No owner
charge moves.

The PROVED
`rate_half_kb_m2_r2_dihedral_degree6_common_pole_exclusion` now imposes the
common six-pole divisor in the `n=6` branch. Two generic Dickson-six fiber
structures would put two fixed-point-free involutions on the same six-point
set. Their complete projective atlas consists of the standard normalizer and
the exceptional fibers `c=27/8,756/125`; every case contradicts the forced
source-cover branch pair, with nonzero KoalaBear resultants. Thus `n=6` is
empty and `n=3` is the sole residual full-V4 dihedral profile. The full-V4
type, owner, and payment remain open.

The PROVED
`rate_half_kb_m2_r2_dihedral_degree3_geometric_realization_fence` shows that
the last profile cannot be deleted by piling on more abstract geometry. At
`a=b=-1` there is an explicit genus-zero bidegree-`(2,4)` source component
realizing the common cubic right factor, six order-five poles, special
coefficient quartic, exact star graph, and complete-source saturation. This
is not a deployed endpoint record, but it proves that the next obstruction
must use the fixed active pencil or produce a chronology-valid recurrent
owner/payment. No ledger quantity moves.

The PROVED
`rate_half_kb_m2_r2_dihedral_degree3_endpoint_cofactor_interpolation_compiler`
now makes the first actual-record gate exact. If `H` is the residual
bidegree-`(2,4)` component and `E_i=B/(z_i H(alpha_i,X))`, divisibility of
the endpoint source form by `H` is equivalent to a full-support kernel of
the `38 x 12` matrix with columns `(E_i,alpha_i E_i)`. A pinned split-field
packet satisfies the exact `s=6` invariant/noninvariant locator ownership,
two-regular pole graph, and four-edge component-color conditions, but its
stacked matrix has rank twelve. Thus abstract star/locator realizability no
longer suffices. The remaining `n=3` task is to exclude a full-support
kernel for every admissible ownership over the deployed field, or
reconstruct a surviving cofactor and route its actual block record to a
chronology-valid owner. No ledger quantity moves.

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

The PROVED
`rate_half_kb_m2_r2_dihedral_residual_one_parameter_quartic_normal_form`
performs that specialization without conflating endpoint coordinates. In a
standard dihedral coordinate the sibling conic is
`x^2+y^2-a*x*y+(a^2-4)=0`, with `a=-1` for `n=3` and `a=1` for `n=6`.
The source V4 passport proves that exactly one branch value of `h` is a
projection branch value. Normalize it to `2` and call the other `b`; the
six coefficients of the canonical quartic are then explicit polynomials
in `(a,b)`. Thus each residual profile is a one-variable irreducibility and
source-realization problem, not a six-coefficient quartic classification.
No owner charge moves.

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

The PROVED `rate_half_kb_m2_r2_dihedral_outer_factor_reduction` makes the
outer component rational in both remaining source-genus regimes. Its two
degree-two projections generate a finite dihedral group inside the deck
group of the common degree-60 function, forcing a geometric
Dickson/Chebyshev right factor of the outer map. The six distinct order-five
poles leave exactly factor degrees `n=2,3,5,6`; the exceptional `n=5` row
uses one generic order-five pole and the one totally ramified point over a
simple pole. The full-V4 source cover has branch inertia `a,c,ac` in genus
zero and `c,c,ac,ac` in genus one. This parent reduction alone does not
delete a factor degree. No owner charge moves.

The PROVED
`rate_half_kb_m2_r2_dihedral_degree5_source_star_exclusion` deletes the
exceptional `n=5` profile. At the common totally ramified dihedral value,
the two reflection quotients each have one source-pole value. The complete
source pullback identity gives two degree-two source-parameter divisors over
the corresponding endpoint source pair, and every one of their four units
lands on the same matching source-star vertex. This contradicts the proved
maximum star weight three. The full-V4 row is therefore reduced to
`n=2,3,6`. This child alone does not constrain their generic-pole incidence.

The PROVED
`rate_half_kb_m2_r2_dihedral_degree2_source_star_exclusion` deletes `n=2`.
At one generic pole of `G`, regular `D_2=V4` incidence is `K_(2,2)`: both
`Z` values see the same two `Y` values. The normalized source map and
diagonal lift force each source sheet to choose a cross edge between their
two endpoint source pairs. The two `Z` values therefore contribute eight
units to four possible star vertices. Their minimum defect is four, above
the global budget three. The full-V4 factor frontier is now `n=3,6`; both
remain open and no owner charge moves.

The PROVED
`rate_half_kb_m2_r2_dihedral_residual_star_graph_rigidity` fixes the exact
source-star shape of both survivors. The source-cover relation
`c eta c^(-1)=eta*a` makes the two endpoint lifts over each `Z` value use
complementary cross-edge orientations. Thus `n=3` gives two disjoint
`K_(2,2,2)` graphs and `n=6` gives the two-point blow-up of `C_6`. In both
cases all 24 star weights are one, the defect is zero, and every source row
has degree four. Further defect counting is therefore exhausted: the live
problem is whether either prescribed graph can be realized by the residual
birational quartic coefficient map and its genus-zero/genus-one V4 branch
passport. No owner charge moves.

The PROVED
`rate_half_kb_m2_r2_dihedral_residual_coefficient_quartic_pin` removes the
remaining arbitrary interpolation. Let `K` be the symmetric bidegree-`(2,2)`
sibling relation between the two `Y` values above one `Z` value. After
normalizing `h(t)=t^2`, if `k(sigma,pi)=0` is its equation in elementary
symmetric endpoint coordinates, then the residual coefficient image is
exactly

```text
k(S^2-2P,P^2)=0,       S=t+s, P=ts.
```

Actual existence forces this canonical pullback to be the irreducible
rational plane quartic. The live full-V4 task is therefore a symbolic
singularity and V4 branch-passport classification in the six coefficients
of `k`, followed by the `D_3` and `D_6` specializations. No owner charge
moves.

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

## 2026-07-29 KoalaBear full-V4 source-facet close

This section supersedes the earlier text naming `n=3` as the live full-V4
frontier. The PROVED
`rate_half_kb_q6_s6_common_five_outgoing_fiber_pin` imports Corollaries
9.25 and 9.27 of the pinned equality-wall source theorem. It gives
`K subset I` with `|K|=5` and, above both points of every complete source
fiber indexed by `k in K`,

```text
Root_T F_out(T,pi)=I^c.
```

For a residual cubic component, the PROVED source-star theorem identifies
the two component stars over that complete fiber with the four endpoints
`N_G(k)` in

```text
G=K_(2,2,2) disjoint_union K_(2,2,2).
```

This identification does not set the relative endpoint twist to one.
Before the facet constraint, the four endpoints are `U_k`, the complement
of one deck pair `P_k` in the relevant six-label component. Since
`k in I` and `U_k subset I^c`, one has `k notin U_k`; common-pole
membership then forces `k in P_k`, and only then `U_k=N_G(k)`.

Since the component divides `F_out`, `N_G(k) subset I^c` for every
`k in K`. Thus `K` would be independent, but `alpha(G)=2+2=4`. The PROVED
`rate_half_kb_m2_r2_dihedral_degree3_source_facet_exclusion` therefore
deletes `n=3` without ownership enumeration or field computation.

Combining this with the proved `n=2,5,6` exclusions and the exhaustive
factor-degree list closes the full-V4 type:

```text
(m,r,delta)=(2,2,4) is empty.
```

This is banked as
`rate_half_kb_m2_r2_dihedral_full_v4_exclusion`. The previous endpoint
cofactor/gain-flatness compiler remains a valid exact theorem and useful
upstream audit instrument, but universal gain nonflatness is no longer
required for this type.

The live `m=2` frontier is now exactly the order-two stabilizer type
`(r,delta)=(4,2)` and the trivial-stabilizer type `(8,1)`. No owner or
payment moves, so `rate_half_band_closure` remains TARGET.

## 2026-07-29 KoalaBear coordinate-order-two source-facet signature

For the coordinate orientation `S=<tau x 1>` in the surviving
`(m,r,delta)=(2,4,2)` type, the PROVED
`rate_half_kb_m2_r4_order2_coordinate_source_facet_signature` combines the
preserving source lift with the common-five facets. Its 24 component stars
have the exact census

```text
J-J=10,       I-I=10,       I-J=4.
```

The endpoint involution preserves both six-sets. On its three pairs in
`J`, the five complete `K` fibers have exactly one of the degree profiles

```text
(4,4),(4,4),(2,2),       or       (4,4),(3,3),(3,3).
```

This does not delete the orientation. In the allowed aligned subcase
`L=I`, a printed 24-edge abstract fixture
satisfies every horizontal facet containment, source degree four, the
two-regular pole graph, four component-color edges, involution equivariance,
and defect zero. Therefore no further attack using only source-facet
cardinality, star degree, color count, involution parity, or defect can close
this branch.

The two route-deciding actions are:

1. impose the actual component interpolation/coefficient equations on the
   two degree profiles above; and
2. derive the preserving source lift and facet signature for the diagonal
   orientation `S=<tau x tau>`.

The later PROVED
`rate_half_kb_m2_r4_coordinate_transpose_transport` performs the required
transport explicitly. Axis transposition preserves `f(T)=f(W)` and sends
a `<1 x tau>` component to a `<tau x 1>` component. Its source equation is
not the old equation transposed: endpoint roles are renamed and the degree-
two source reduction is rerun on the new second projection, producing a
fresh primed record. The complete coordinate compiler chain then applies
to that record. Thus the two coordinate subgroups are one deletion route;
only coordinate and diagonal geometry need independent order-two attacks.
The trivial-stabilizer type also remains open. No owner or payment moves.

## 2026-07-30 KoalaBear diagonal whole-fiber compiler

The diagonal orientation now has a correct source interface. The PROVED
`rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler`
multiplies the two quadratic stars over each complete `psi` fiber. The
resulting twelve split quartics `R_p` obey

```text
[R_bar(p)]=[tau^* R_p],            product_p R_p(T) ~ A(T)^4,
```

and retain the exact `K`, `eta in L minus K`, and one-exchange facet
supports. These are whole-fiber statements. The diagonal normalization
automorphism need not descend to the `X`-line, so individual-star
equivariance is not available.

Writing the quartic coefficients as `r_(p,a)` and taking a `7 x 12`
parity check `P` for degree-at-most-four evaluation at the source labels
gives the exact matrix

```text
M_(s,a),p=P_(s,p) r_(p,a),          M has size 35 x 12.
```

A full-support kernel is equivalent to interpolation by a
bidegree-at-most-`(4,4)` endpoint biform. The diagonal branch is therefore
reduced to a finite exact kernel gate followed, for survivors only, by
irreducibility and the outer self-correspondence factor identity. Prove
universal kernel failure or reconstruct and attack the unique surviving
biform; do not reuse the stronger coordinate-star equation.

The PROVED
`rate_half_kb_m2_r4_diagonal_source_subfield_dichotomy` now resolves that
descent ambiguity exactly. If the diagonal automorphism preserves the
quadratic source intermediate field, it descends to a source-line
involution and admits the geometric normal form

```text
b(X)=-X,       s(X)=1/X,       psi(X)=X^2,
tau(Z)=1/Z,
T^2 X^4 H(1/T,1/X)=+/-H(T,X).
```

The two source coefficient eigenspaces have dimensions eight and seven,
and individual-star transport is valid in this branch. If the intermediate
field is not preserved, its conjugate is a second rational quadratic
subfield; the quartic `W` projection is then a `V4` cover. Tame
Riemann--Hurwitz leaves exactly genus zero with branch inertia
`eta,eta',mu=eta eta'`, or genus one with inertia
`eta,eta,eta',eta'`. This function-field `V4` is not the deleted full
ambient-stabilizer type. The diagonal route is now two explicit algebraic
branches rather than an unresolved source-lift question; neither branch is
yet deleted and no owner charge moves.

The PROVED
`rate_half_kb_m2_r4_diagonal_branch_coefficient_compiler` turns both
branches into coefficient equations. In the lifting branch, write

```text
H(T,X)=U(T,X^2)+X V(T,X^2),
G(T,W)=U(T,W)^2-WV(T,W)^2,
deg U<=(2,2), deg V<=(2,1).
```

The two forms obey one common reciprocal sign, leaving eight or seven
source coefficients; the endpoint biform is positive reciprocal in either
case. In the non-lifting branch, the monic endpoint quartic over `K(W)` has
a completely split cubic resolvent, equivalently `V4` Galois group under
the actual irreducibility and separability hypotheses. These replace a
generic `25`-coefficient endpoint search by two exact low-dimensional
tests. Universal failure is not proved, and no owner charge moves.

The PROVED
`rate_half_kb_m2_r4_diagonal_facet_mixing_obstruction` removes a tempting
but false diagonal simplification. The endpoint involution cannot preserve
the source-facet partition `I | J`. If `c` labels cross from either six-set
to the other, then

```text
c in {2,4,6}.
```

Writing `a` for the number of involution pairs inside the common five-set
`K`, and `b` for whether the unique `xi in I minus K` is paired into `K`,
the exact remaining orbit rows are

```text
(a,b,c)=(2,0,2),(1,1,2),(1,0,4),(0,1,4),(0,0,6).
```

The proof uses only whole-fiber quartic transport. If the involution
preserved `I`, oddness of `|K|=5` would pair one `k in K` with `xi`; four
`J` roots would then transport to a fiber supporting either zero `J` roots
(`xi=eta`) or at most two (a one-exchange fiber). This is impossible.
Moreover, a `K` quartic transported to `K` uses only noncrossing `J` labels,
one transported to `eta` uses only crossing `J` labels, and one transported
to `L^c` uses at least two crossing labels. This applies to both branches of
the source-subfield dichotomy. Attack the five rows separately, starting at
`c=2`; do not impose the coordinate branch's `I,J` invariance or colored
quotient descent. No full diagonal or owner close follows yet.

The same theorem closes the aligned maximally mixed row. If `c=6`, then
`tau` swaps `I,J`; transporting the `eta` quartic rules out `L=I`. In the
near-aligned survivor,

```text
tau(eta) in K,       ell=tau(xi) in J intersect L^c.
```

Exactly the four stars above `xi,ell` are `I-J`; all other `L^c` stars are
`I-I`. Hence the colored divisor is the pullback of the positive reciprocal
quadratic `chi` on `{xi,ell}`, and the universal partial resultants descend:

```text
Q_J ~ K_5^2 chi,       chi Q_I ~ R_7^2.
```

Thus arbitrary four-edge enumeration is unnecessary in `c=6`. Attack this
single quotient system or the stronger `c=2` support rows next.

The minimally mixed rows now have an exact capacity refinement. Put
`J_0=J intersect tau(J)` and `J_1=J intersect tau(I)`, of sizes four and
two. In the `(a,b,c)=(2,0,2)` row the four common-`K` quartics transported
inside `K` saturate the `4 x 4` noncrossing incidence capacity. Consequently

```text
d_j=4 (j in J_0),       d_j=2 (j in J_1),
R_k* ~ P_(J_1)^2,       product_(k in K_0) R_k ~ P_(J_0)^4,
```

where `K_0=K intersect tau(K)` and `k*` is the remaining common-`K` label.
For `(1,1,2)`, the same capacity argument gives
`R_(tau(eta)) ~ P_(J_1)^2` and degree four at both labels of `J_1` whenever
`L=I` or `tau(eta) in K`. The sole unsaturated orbit has `L!=I` and
`eta,tau(eta) in J_0`; there only
`6 <= sum_(j in J_1) d_j <= 8` remains. The next coefficient attack should
feed the forced square fiber and the four-fiber fourth-power identity into
the source norm equation; it must retain that exceptional `(1,1,2)` orbit.

The PROVED
`rate_half_kb_m2_r4_diagonal_c2_square_fiber_linear_cut` performs the first
such substitution in the source-line branch and exposes a necessary
ramification split. For an unramified forced fiber `w`, both quadratic
stars equal `P_(J_1)`, so

```text
U(T,w), V(T,w) in <P_(J_1)>.
```

These are four independent linear conditions: the reciprocal source spaces
drop from dimensions `8/7` to exactly `4/3`. Moreover, the three coefficient
minors of the `U,V` coefficient vectors share the reciprocal source-orbit
quadratic `chi_w`, with explicit paired linear quotients. At the ramified
orbit `{0,infinity}`, however, the two stars coincide; only the applicable
value of `U` is constrained, the cut has rank two, and dimensions `6/5`
remain. Thus the earlier blanket minor argument is invalid at ramification.
Attack that weaker branch first, then insert the `4/3` parametrization and
the four-fiber fourth-power identity into the source interpolation gate.

For `(a,b,c)=(2,0,2)`, that ramified branch is now deleted. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_202_ramified_defect_exclusion` combines the
square fiber with the complete-source defect budget. The two reciprocal
branch fibers are distinct doubled star vertices and cost defect two. The
other four common-`K` fibers are unramified and supply eight reduced
`J_0-J_0` stars on at most six edges, whose balanced defect floor is two.
The resulting defect at least four contradicts the budget three. Therefore
the source-line `(2,0,2)` row is unconditionally in the `4/3`-dimensional
unramified locus. This does not apply to the source-cover branch or delete
the row; the next source-line step is the reciprocal occupancy and
four-fiber interpolation calculation.

The defect argument actually deletes the whole `(2,0,2)` row. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_202_defect_exclusion` observes that the
forced square quartic always gives one doubled `J_1-J_1` star vertex, while
whole-fiber transport gives a distinct doubled `I-I` vertex at its paired
label. This costs defect two without any source-line lift or unramifiedness.
The eight `J_0-J_0` stars still cost at least two on their six possible
edges. Hence every packet has defect at least four against budget three,
in both source-subfield branches. Remove `(2,0,2)` from the diagonal census;
four rows remain. The next defect attack is `(1,1,2)`, starting with its
saturated square-fiber cases and keeping the printed exceptional orbit.

The saturated `(1,1,2)` cases now have an exact defect classifier. The
PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_saturated_defect_classifier` shows that
the reciprocal square vertices have weight exactly two and consume two
defect units. The remaining common-`K` stars are four `J_0-J_0` and four
`J_0-J_1` edges, with each `J_1` label used twice and at most one repeated
edge. The possible `J_0` profiles are only
`(2,2,4,4),(2,3,3,4),(3,3,3,3)`. Exact enumeration leaves `1,560` labeled
packets in `123` matching-preserving orbits. Source-line star equivariance
cuts this to `96` labeled packets in `12` orbits; its four mixed edges are
distinct and transport to all four universal `I-J` stars. These are finite
attack lists, not realized survivors. Apply interpolation to the twelve
source-line orbits and the split resolvent to the branch-independent list;
keep `(KBDM-10)` separate.

The source-line list has a stronger exact quotient reduction. For a
saturated `(1,1,2)` packet put

```text
K_Lc={k in K: tau(k) in L^c},       Omega=tau(K_Lc).
```

The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_source_line_colored_quotient_compiler`
uses individual-star transport and exhaustion of the four universal `I-J`
stars to show that `|Omega|=2` and

```text
C_H ~ chi_Omega(psi),
Q_J ~ K_5^2 chi_Omega,       chi_Omega Q_I ~ R_7^2.
```

Both `Omega` fibers are unramified. In the aligned row `Omega=J_1`; in the
near-aligned row with `tau(eta) in K`, `Omega={xi,ell}`, where `ell` is the
other crossing label in `J intersect L^c`. The latter pair need not be a
`tau` orbit. Thus the twelve source-line classes do not require arbitrary
four-root colored-divisor enumeration. Split their algebraic attack into
the aligned quotient `chi=P_(J_1)` and the near-aligned quotient
`chi=P_{xi,ell}`, combining each with the existing `4/3` or `6/5`
square-fiber coefficient cut. No packet is deleted yet.

The internal pure orbit supplies a second source-line gate before full
interpolation. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_source_line_odd_part_incidence_gate`
first deletes source ramification of the unique internal common-`K` orbit:
ramification would create two doubled pure-edge vertices against the one
remaining defect unit. Over either unramified fiber its two pure stars are
distinct but cannot be disjoint, so they share one endpoint `a in J_0` and

```text
U(a,z)=V(a,z)=0.
```

When the forced square orbit `w` is unramified, deck distinction makes the
odd part nonzero, and its projective class is uniquely determined by the
sign and `q=P_(J_1)`. Writing `q=q_0+q_1T+q_2T^2`, set

```text
F=q_0-epsilon*w*q_2,  G=epsilon*q_2-w*q_0,
M=q_1(1-epsilon*w),
N=F+Ma+epsilon*G*a^2,
D=G+epsilon*Ma+epsilon*F*a^2.
```

Then `D!=0` and the internal label must satisfy `z=-N/D`. Test these two
signs and two `J_0` orbits before constructing an interpolation matrix.
After a passing test and normalization of `V`, only two/one affine `U`
parameters remain in the positive/negative signs. The forced-ramified
branch remains a separate attack.

Complete-source multiplicity removes that coefficient escape. In the
forced-ramified branch, orient the source orbit as `W=X^2=0`. The two rows
indexed by the roots of `q=P_(J_1)` are the only rows vanishing at `X=0`.
Each divides `B/z_i`, so its order is at most two; local saturation requires
their total order to be four. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_ramified_complete_source_repair`
therefore forces both row orders to equal two and hence

```text
U(T,0) in <q>,       V(T,0) in <q> minus {0}.
```

The ramified cut consequently has rank four and dimensions `4/3`, not the
square-only `6/5`. The odd-part formula and incidence value `z=-N/D` apply
with `w=0`. All saturated source-line `(1,1,2)` packets now use the same
four-case pre-interpolation gate; source ramification remains geometrically
possible but no longer needs a separate coefficient route.

The internal stars now remove the remaining continuous coefficient freedom.
Let `S_epsilon(w,q)` be the reciprocal `U` space cut by
`U(T,w) in <q>`. Evaluation at the internal label `z` is injective: a
kernel element would be `chi_z(W)R(T)`, forcing `q` to be a reciprocal
endpoint eigenform, impossible because `tau(J_1)` lies in `I`. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
therefore gives a `3 x 3` isomorphism in the positive sign and a two-plane
embedding in the negative sign.

For a compatible internal edge pair `e,f`, the pinned `V(T,z)` fixes their
relative scalars and hence the target value `U(T,z)`. The positive sign has
one reconstructed source form; the negative sign has one linear rejection
test and otherwise one form, all modulo source-deck conjugation. The five
labeled pure multisets admit `2,2,4,2,2` internal assignments. Thus each
classified packet has at most eight source-deck candidate pairs. Evaluate
the aligned or near-aligned quotient identities on those candidates; do not
carry a free coefficient family into the next stage.

The first quotient calculation has a smaller exact prefilter. Put
`q=P_(J_1)`, `G=U^2-WV^2`, and let `k_1,k_2` be the two remaining common-`K`
labels carrying the four mixed stars. At either root of `q`, the forced
square contributes `(W-w)^2`, while its two incidences among the four mixed
stars contribute two further roots. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
therefore forces

```text
Res_T(q,G) ~ (W-w)^4 ((W-k_1)(W-k_2))^2.
```

The target quadratic is `tau^*q` in the aligned branch and
`tau^*chi_Omega` in the near-aligned branch. Test this degree-eight identity
on each reconstructed form before forming either degree-six partial
resultant. A light split `F_1009` fixture reconstructs twelve positive forms
and rejects all twelve here; this is evidence only, not a generic deletion.

The negative reconstruction plane also factors before the q-slice. Normalize
the common internal endpoint to `2` by an endpoint coordinate change
commuting with inversion, and write

```text
J_0={2,1/2,b,1/b},       q=(T-c)(T-d).
```

The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_source_line_negative_reconstruction_factor_gate`
classifies the twelve negative assignments as eight fixed-moving and four
moving-moving templates. Their augmented determinants factor as `A^2 B` and
`A B C`. The same incidence formula gives

```text
z+1=(1+w)A/E.
```

Here `E!=0`, while the fixed-point-free internal orbit and source label give
`z!=-1` and `w!=-1`; hence `A!=0`. After removing only proved nonzero
collision and incidence factors, the determinants vanish exactly on

```text
fixed-moving:  B=0,
moving-moving: B C=0,
```

for the explicit low-degree factors `(KBNF-2)`. Thus the apparent `A=0`
locus is inadmissible and generic negative assignments are already deleted.
Apply the q-slice only to the genuine `B=0` and `C=0` loci; positive
candidates remain a separate direct q-slice calculation.

In the aligned branch, even those negative loci are empty. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_source_line_aligned_negative_q_slice_exclusion`
uses `b->1/b` to identify the moving `C` locus with `B=0`. If `m_j` are the
coefficients of the monic residual q-slice mismatch, exact reconstruction
gives

```text
m_0=(cd-1)(cd+1)/(c^2 d^2).
```

Since `cd!=1`, passage forces `cd=-1`; there

```text
m_1-m_3=4(c^2-1)/c=-A!=0.
```

Thus no aligned negative candidate passes `(KBQS-1)`. The aligned source-line
attack retains only the positive sign. At this checkpoint both signs remained
in the near-aligned branch because its target is `tau^*chi_Omega`, not
`tau^*q`.

The aligned positive forced-ramified branch is also empty. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_ramified_q_slice_exclusion`
keeps the repaired `w=0` equations and the exact relative `U/V` scale. For
each internal template, unique factorization leaves the `same`, `swap`, and
`mixed` residual allocations. All three fixed-moving ideals have unit full
forbidden saturation over `F_2130706433`. The moving equations are reciprocal
quartics in `b`; after exact descent to `s=b+1/b`, all three corresponding
saturations are also unit. Thus the complete aligned `w=0` branch is deleted
after combining the negative theorem. The PROVED moving `swap` and moving
`same` unramified q-slice exclusions delete those two allocations by exact
trace-minor, conic, finite-extension, and off-common replay. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_moving_mixed_full_quotient_exclusion`
handles the third moving allocation without asserting a false q-slice
deletion. Its degree-12 component has four exact q-slice points over degrees
`3,3,7,7`. The degree-7 points do not embed in the deployed degree-six field;
both reciprocal orientations over each degree-3 trace reproduce `(KBQS-1)`
but fail both normed identities derived from `(KBQ2-2)`. All twelve
off-common cofactor combinations are boundary-supported. Hence all three
moving-moving allocations are closed and exactly the three fixed-moving
aligned positive unramified cells remain at that checkpoint. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_fixed_same_full_quotient_exclusion`
then closes fixed-same. Its direct reciprocal-quartic norm has 28 factors;
deployed-field replay leaves four base-field q-slice points, and all four
fail both normed identities from `(KBQ2-2)`. Its two off-common cofactor
branches give seven distinct endpoints, all boundary-supported. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_fixed_swap_full_quotient_exclusion`
then closes fixed-swap. Its degree-333 direct norm has 26 factors; exact
deployed-field replay leaves one quadratic-field q-slice point, which
reproduces `(KBQS-1)` but fails both normed identities from `(KBQ2-2)`. The
two off-common combinations give nine distinct endpoints, all boundary.
The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_fixed_mixed_full_quotient_exclusion`
then closes the final cell. Its reciprocal degree-five component leaves four
quadratic-field q-slice points, all rejected by both full quotient norms. The
mixed-only linear rank curve is empty after replay of its complete degree-116
raw-kernel norm, and all twenty off-common combinations are boundary. Thus
all six aligned positive unramified allocations are closed; only later
packet/source-row assembly obligations remain on this route.

The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_negative_q_slice_exclusion`
also removes the negative sign from the near-aligned branch. The negative
factor gate and `b->1/b` reduce both internal templates to `B=0`; exact
reconstruction gives the same `z,V` and opposite `U`, hence the same
`G=U^2-WV^2`. Its monic residual quartic has constant one, so passage to the
near target forces `(xi*d)^2=1`. The plus branch is a label collision. On the
minus branch, exact projections for `xi=2`, `xi=1/2`, and `xi=b` reconstruct
only forbidden endpoint labels, collisions, or `w=+/-1`. Direct deployed-prime
saturation is unit in all three rows. This deletion includes the negative
forced-ramified locus `w=0`; it does not address the positive homogenized
boundary.

Seven deployed-field near-aligned positive charts are now deleted. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_fixed_xi_direct_square_exclusion`
normalizes `a=xi=2`, takes the fixed-moving template with `eta=c`, and assigns
the two residual squares to `1/2` over `c` and `1/d` over `d`. All four
generic endpoint-line pairs have only collision support; the two leading-zero
loci add only points with `z=1`. Independent resultant and Bezout replays
verify the same support modulo the KoalaBear characteristic. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_fixed_xi_swapped_square_exclusion`
interchanges the two target roots and gives the same collision-only generic
support. Its sole additional exceptional component forces the same excluded
`z=1` locus, with an independent opposite-variable audit. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_fixed_xi_mixed_exclusion`
assigns both distinct target roots to both residuals. After explicit
collision and boundary factors are removed, degree-96 and degree-186
projection certificates have only forbidden common support. A fraction-free
audit proves the opposite projection and both paths replay modulo the
KoalaBear characteristic. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_tau_xi_mixed_exclusion`
repeats the mixed allocation for `xi=tau(a)`, where the target root is `2`.
Its direct and fraction-free opposite projections again have only forbidden
common support, including modulo the deployed characteristic. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_tau_xi_square_exclusions`
deletes both square allocations in that reciprocal-`xi` orbit. Its direct
leading-zero points lie on `z=1`, and its remaining exceptional audit fiber
forces collisions; the swapped exceptional geometry is unchanged. All
sixteen pair/allocation replays pass in characteristic zero and modulo the
deployed prime. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_other_xi_square_xi_exclusion`
then treats `xi=b` and the square allocation `c->1/b,d->1/d`. Its
four product-branch pairs have only collision support or explicit fibers
forcing `b=1/2`; an independent fraction-free/subresultant replay gives
the same result modulo the deployed prime. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_other_xi_square_ell_exclusion`
closes the swapped allocation `c->1/d,d->1/b`. Its extra projected
fibers force `b=1/2` or the excluded inversion-fixed loci `c=+/-1`, and
the only nonstandard line-degeneration component also forces `b=1/2`.
Direct/resultant and fraction-free/subresultant paths agree modulo the
deployed prime. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_other_xi_mixed_exclusion`
closes the remaining mixed allocation in this relative orbit. Its four
cubic conditions split into two residual components at each q-root. All
four component pairs have complete exact `F_(p^6)` fiber routers, and every
reconstructed point is collision, inversion-fixed, finite-incidence, or on
`z=1`. Fail-closed primary shards and a no-import
fraction-free/subresultant audit agree. These results delete all 9
fixed-moving affine positive charts.

The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_a_xi_square_exclusion`
closes the first moving-moving chart. Normalize `a=xi=2`, use source edges
`{2,b},{2,1/b}`, and assign residual squares `c->1/2,d->1/d`. The four
primitive conditions are reciprocal in `b` and reduce exactly through
`s=b+1/b`. Their three-by-three component router leaves 15 nonstandard
modular factors of degrees dividing six: six linear, five quadratic, three
cubic, and one sextic. Saturating each factor with all four trace equations
by the full forbidden product gives the unit ideal. Direct/resultant and
no-import fraction-free/subresultant certificates agree.

The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_a_xi_square_ell_exclusion`
closes the swapped square allocation `c->1/d,d->1/2`. Its reciprocal trace
forms have three nonstandard parent components over `c` and two over `d`.
The six pair projections leave two irreducible degree-nine factors and one
irreducible degree-five factor, none of which meets `F_(p^6)`, plus four
linear fibers. All four linear fibers have unit forbidden saturation in the
direct/resultant and independent fraction-free/subresultant paths.

The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_a_xi_mixed_exclusion`
closes the mixed allocation `c,d->{1/2,1/d}`. After reciprocal trace
reduction, each parent has one nonstandard component and their sole
projection has degree 128. Its complete modular census leaves four linear,
five quadratic, and one cubic factor relevant to `F_(p^6)`; all ten have
unit forbidden saturations. The other irreducible degrees are 5, 7, and 29.
The direct/resultant and independent source/subresultant paths agree. Thus 12
of the 18 affine positive charts are closed, the full `xi=a` orbit is done,
and six moving-moving charts remained at that checkpoint.

The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_tau_xi_orbit_exclusion`
closes the next three charts at once. For the distinguished residual root
`2`, the square-xi, square-ell, and mixed allocations leave respectively
`3x3`, `3x2`, and `1x1` nonstandard parent component routers. Their complete
deployed-field sieves retain 15, 4, and 10 factors of residue degree dividing
six. All 29 forbidden saturations are unit in both the direct/resultant
primary and the no-import fraction-free/terminal-subresultant audit. Thus 15
of the 18 affine positive charts are closed. Only the three moving-moving
allocations in the other relative-xi orbit remain, together with negative
loci and the `w=0` boundary.

The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_other_xi_square_xi_exclusion`
closes the first of those three charts. The nonreciprocal `c` product splits
into two cubic branches, whose sum-resultants leave two nonstandard parent
components; the reciprocal `d` side leaves three. Complete factorization of
all six pair projections retains seven linear and one quadratic deployed
fiber. All eight full four-core forbidden saturations are unit in a
direct/resultant primary and an independent fraction-free/terminal-
subresultant audit. Thus 16 of 18 affine positive charts are closed. Only
the swapped and mixed moving-moving other-xi allocations remain, together
with negative loci and the `w=0` boundary.

The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_other_xi_square_ell_exclusion`
closes the swapped chart. Here the reciprocal `c` side leaves three
nonstandard parent components, while the nonreciprocal `d` product splits
into two cubic branches leaving two. Complete characteristic-zero and
deployed-prime factorization of the six `3x2` pair projections retains ten
linear, nine quadratic, one cubic, and two sextic factors. All 22 full
four-core forbidden saturations are unit in both a direct/resultant primary
and an independent fraction-free/terminal-subresultant audit. Thus 17 of 18
affine positive charts are closed. Only the mixed moving-moving other-xi
allocation remains, together with negative loci and the `w=0` boundary.

The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_other_xi_mixed_exclusion`
closes that final affine-positive chart. The product-ratio minus gate splits
into two linear branches and one reciprocal-quadratic branch; their 22
candidate fibers all have unit full four-core forbidden saturation. The
ratio-plus reciprocal quartic is handled in the trace coordinate
`s=b+1/b`: four independent generic pair gates have common projection
degree 352, while the leading-coefficient boundary has projection degree
772. Complete residue-field reconstruction leaves no admissible fiber in
either chart. A direct SymPy/FLINT primary and an independent no-import
fraction-free audit agree. Thus all 18 affine positive charts are closed.
The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_near_positive_projective_boundary_exclusion`
closes the distinct homogeneous endpoint boundary. Orienting
`eta=infinity` gives `w=0` and `q_hom=Y(T-dY)`. The projective q-slice is the
product of the finite `T=d` residual and the `T^4` coefficient residual at
infinity. Three fixed-moving saturations, two moving trace saturations, and
both signs of the moving other-xi constant gate are unit over the deployed
field. Thus the positive near-aligned queue is complete. Combined with the
near-negative theorem, the entire near-aligned source-line branch is empty.
The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_source_line_complete_exclusion` now
composes the defect census, aligned/near quotient partition, and all 25
sign/cell/boundary exclusion theorems. Its checker pins all 32 compiler and
theorem prerequisites. Therefore the complete saturated diagonal
`c2(1,1,2)` source-line branch is empty. The residual assembly frontier is
the coordinate and source-cover orientations, not another source-line cell.

The aligned positive sign has also resisted a broader exact falsifier sweep.
The seeded standard-library replay
`notes/kb_c2_112_positive_qslice_sweep.py` tests all twelve internal
assignments on twenty fixtures at each of five primes. It reconstructs
`1,188` of `1,200` assignments, skips `12` only for endpoint-label
collisions, and finds zero `(KBQS-1)` survivors. This is evidence only: no
generic positive deletion or exceptional-locus classification is claimed.

Two exact characteristic-zero slices expose the likely generic positive
certificate. The bounded script
`notes/kb_c2_112_positive_qslice_constant_slice.py` computes the full monic
q-slice mismatch at `(c,d)=(3,7)` and `(4,6)`. In the fixed-moving template,
the zero-dimensional lex eliminant is supported exactly on
`(w-1)^5(w+1)^2`. In the moving-moving template, first pass to the invariant
`s=b+1/b`; the two eliminants have the same fixed-point factors plus two
linear factors, and those extra roots reconstruct with `s=+2,-2`. Thus every
slice survivor has `w=+/-1` or `b=+/-1` and is inadmissible. The raw moving
Groebner calculation timed out at `60 s`; the invariant-coordinate version
finishes in under sixteen seconds. This is two-slice evidence, not a generic
deletion.

The PROVED `rate_half_kb_m2_r4_source_row_interpolation_compiler` supplies
the smaller shared actual-component gate. For twelve projective source-row
quartics `q_i`, stack a `9 x 12` degree-two evaluation parity check across
their five coefficients. A full-support kernel of the resulting
`45 x 12` matrix is equivalent to a unique bidegree-at-most-`(2,4)` source
biform `H` with those row divisors. Every actual packet also satisfies

```text
product_i q_i ~ B^2,       Res_T(A,H) ~ B^2,
```

and in lifted diagonal coordinates the right side is `A(X^2)^2`. Apply
this source gate before endpoint interpolation or resolvent work. Passing
still requires exact degree, irreducibility, deck distinction, branch
symmetry, and endpoint realization. No orientation or owner is closed.

The PROVED `rate_half_kb_m2_r4_coordinate_coefficient_normal_form` now
compiles the coordinate branch after that shared gate. Geometrically
normalize `tau(T)=-T`, `b(X)=-X`, and `W=X^2`. The preserving lift forces
exactly

```text
H=A_2(W)T^2+A_0(W)+XT B_1(W)                    (dimension 8),
```

or

```text
H=T A_1(W)+X(B_2(W)T^2+B_0(W))                  (dimension 7).
```

The odd-`X` part must be nonzero because the source component and its deck
conjugate are distinct. In either sign the endpoint is the quadratic norm
`G=U^2-WV^2` and is even in `T`. The coordinate orientation is therefore
at two explicit coefficient spaces, not a generic interpolation problem;
universal failure remains open and no owner charge moves.

The PROVED `rate_half_kb_m2_u2_universal_source_facet_census` extracts the
stabilizer-independent part of the coordinate argument. Every surviving
degree-two source component, including the previously unstructured
trivial-stabilizer `(r,delta)=(8,1)` type, has

```text
(J-J,I-I,I-J)=(10,10,4).
```

On the six `J` labels, the ten stars over `K` initially have exactly one of

```text
(0,4,4,4,4,4), (1,3,4,4,4,4), (2,2,4,4,4,4),
(2,3,3,4,4,4), (3,3,3,3,4,4).
```

This uses no stabilizer symmetry. The coordinate involution retains its
stronger two-profile conclusion, while the diagonal and trivial types do
not inherit it.

The later PROVED
`rate_half_kb_m2_u2_universal_component_color_profile_cut` imports the
exact Corollary 9.28 color law. A degree-two component colors four edges of
the two-regular pole graph, and `c_j=4-d_j` is the colored degree of its
left vertex. Thus `c_j<=2`; the deficit partitions `4` and `3+1` are
impossible. The universal list is now exactly

```text
(2,2,4,4,4,4), (2,3,3,4,4,4), (3,3,3,3,4,4).
```

Every `J` label occurs at least twice over `K`. The coordinate branch keeps
only the first and third rows; diagonal and trivial branches retain all
three.

The PROVED
`rate_half_kb_m2_u2_colored_source_resultant_split_compiler` packages the
four simple colored roots as one squarefree quartic `C_H`. If `D_K` is the
degree-ten pullback over `K`, `D_R=B/D_K`, and `P_I,P_J` are the two label
sextics, every residual component satisfies

```text
Res_T(P_J,H) ~ D_K^2 C_H,
C_H Res_T(P_I,H) ~ D_R^2,
c_j=deg gcd(C_H,bZ_j).
```

The next attack should classify these four-edge divisors jointly with the
`45 x 12` source gate and branch coefficient forms. Do not enumerate the
two deleted profiles or treat twelve source rows as independent. No type
or owner is closed.

For the coordinate orientation, the PROVED
`rate_half_kb_m2_r4_coordinate_colored_quotient_resultant_compiler` carries
this one step further. The colored divisor is deck invariant, hence
`C_H(X)=c(X^2)` for a squarefree quadratic `c`, selecting two complete right
pole-graph fibers. With `P_S(T)=p_S(T^2)`, the two parity systems are

```text
Phi_+=(A_2Y+A_0)^2-WYB_1^2,
Phi_-=W(B_2Y+B_0)^2-YA_1^2,
R_S=Res_Y(p_S,Phi_epsilon),
R_J~K_5^2c,       cR_I~R_7^2.
```

Thus the coordinate branch is an explicit univariate norm-factorization
problem in eight or seven source coefficients plus a two-fiber choice.
Universal inconsistency remains open.

The PROVED
`rate_half_kb_m2_r4_coordinate_k_fiber_vieta_rank_compiler` now couples
those coefficient spaces to the five actual `J-J` stars over `K`. For a
source lift `[r:s]` above `kappa=[u:v]` carrying edge `{a,b}`, the
homogeneous quotient record

```text
p=ab,       q=r*s*(a+b)
```

is unchanged by deck transport. The positive
form must satisfy, at all five `kappa`,

```text
A_0=pA_2,       u*v B_1=-qA_2,
```

and the negative form must satisfy

```text
B_0=pB_2,       A_1=-qB_2.
```

These are exact `10 x 8` and `10 x 7` homogeneous kernel gates with
nonvanishing leading values. Each parity has a five-by-five determinant
obstruction; the negative products also have a four-column rank-three
gate. The negative parity also excludes a ramified common-`K` value.
Apply these small tests before the quotient-resultant identities.
No determinant is yet proved nonzero for every admissible star packet, so
the coordinate orientation remains open and no owner charge moves.

The PROVED
`rate_half_kb_m2_r4_coordinate_vieta_profile_only_f29_route_cut` shows why
the word "before" is load-bearing. Over `F_29`, an exact aligned abstract
packet simultaneously has the allowed `(2,2),(4,4),(4,4)` paired profile,
a diagonal-free two-regular pole graph, all facet and deck transport laws,
four colored edges, defect two, and a geometrically irreducible positive
source form with full leading support whose `10 x 8` Vieta matrix has rank
seven. Thus profile, defect, irreducibility, and the determinant alone do not
form a universal exclusion interface. For this packet the `J`-resultant
forces

```text
c_0(W)=W^2-7W+9=(W-13)(W-23),
```

whose roots lie outside the six allowed `J` labels; the companion `I`
identity also fails at `W=xi`. This is a small-characteristic route cut, not
a deployed-field packet or orientation deletion. The next exact classifier
must retain rank survivors through forced colored support and the companion
quotient identity.

## 2026-07-30 coordinate complete-fiber Vieta reduction

The PROVED
`rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler` removes an
unnecessary nonlinear step from the coordinate search.  A complete packet
has twelve deck-paired source-fiber edge records over
`Omega=K union {eta} union L^c`, not only the five common-`K` records.  The
same Vieta calculation gives exact `24 x 8` positive and `24 x 7` negative
linear systems.  Their square-root-free product halves are

```text
rank[-p v^2,-p uv,-p u^2,v^2,uv,u^2]_(Omega)<=5,
rank[-p v,-p u,v,u]_(Omega)<=3.
```

Positive parity therefore has a first nonvacuous `6 x 6` determinant on
`K union {eta}`.  It rejects the earlier profile-only `F_29` witness with
determinant ten, explaining the failed companion identity without computing
a resultant.  The separator is not by itself universal: on the exact
defect-zero source-facet fixture, 140 of the 5,040 assignments of six signed
square-pairs in `F_29` pass the six-row gate with leading support.  None
passes after the six `L^c` rows are appended.  These finite counts are route
evidence for one fixture, not a deployed-field exclusion.

Negative parity is sharper.  Its product ratio `B_0/B_2` cannot be constant
without forcing an edge of weight at least four and defect at least six.
It is therefore an injective Mobius map, so all twelve edge products are
distinct.  The 14 common-`K` pair-multiplicity skeletons reduce exactly to
seven: three in profile `(4,4,2)` and four in profile `(4,3,3)`.

The next coordinate classifier should enumerate canonical complete
source-facet packets, apply the complete product matrices first, and retain
only their kernels for the full `q` equations.  Forced colored support and
the companion quotient identity then follow from realizing all 24 stars and
should be replayed as independent audits.  Do not return to profile-only or
`K+eta`-only determinant searches.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate`
adds the first complete-packet gate specific to negative parity.  Conjugate
source negation by the injective Mobius product map.  If `(y_i,z_i)` are the
edge products at the six source-label pairs, they are free orbits of one
projective involution and therefore

```text
rank [y_i z_i,-(y_i+z_i),-1]_(i=1,...,6)<=2.
```

This is a coefficient-free `6 x 3` test.  Two distinct antisymmetric product
pairs `(u,-u),(v,-v)` force the common involution to be negation, hence force
every pair sum to vanish.  The exact defect-zero fixture contains
`(AC,-AC),(BC,-BC)` but also `(DE,DF)` with nonzero sum.  It is therefore
symbolically deleted in negative parity over every odd field.  The zero
survivors among all 5,040 signed-square assignments in `F_29` and the printed
minor 12 are independent regressions.  Apply the same gate to every other
canonical negative completion retained by the later loop-budget cut before
the full Mobius and `q` systems.

The same theorem covers positive packets whenever `A_0/A_2` reduces to
degree at most one.  The constant branch violates defect three; the Mobius
branch obeys the paired-product gate.  Hence the printed fixture is also
deleted on the positive linear-product locus, and any remaining positive
realization must have genuinely quadratic product ratio.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` then uses the
sum half of the Vieta system.  Every antipodal common-`K` edge has `q=0`
and forces one root of the quadratic `A_1`.  Three loop fibers force
`A_1=0`, contradicting the required nonzero `q B_2` at a nonloop edge.
Thus negative parity has at most two `K` loops, and the seven injective
multiplicity skeletons reduce exactly to five, in loop strata
`0,1,1,2,2`.  In the two-loop strata `A_1` is already fixed up to scale.
Use these factor pins before the remaining full-product or `q` equations.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_loop_stratified_q_compiler`
packages those residual equations without redundant loop rows.  If
`R_Lambda` is the locator of the `ell=0,1,2` loop fibers, write
`A_1=R_Lambda C`.  On the nonloop fibers the rows

```text
[R(kappa),R(kappa)kappa,...,R(kappa)kappa^(2-ell),q,qkappa]
```

form a square determinant of size `5-ell`.  Thus the loop strata have exact
`5 x 5`, `4 x 4`, and `3 x 3` gates.  The two-loop skeletons are now the
smallest direct target: classify their signed cross-edge assignments through
the `3 x 3` determinant, retain leading support, and only then apply the
complete product and paired-involution gates.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_product_q_weld` couples
the two halves rather than treating that `3 x 3` determinant in isolation.
On either two-loop skeleton, the five product rows have rank exactly three
and determine the Mobius denominator `D=B_2` projectively.  If `h` is either
loop and `i,j` are nonloops, the residual sum equations are equivalent to

```text
q_i R(j)(h-i)(p_h-p_j)=q_j R(i)(h-j)(p_h-p_i).
```

Two instances against one fixed nonloop reconstruct all five common-`K`
sum rows.  Apply the product rank and leading-support gate first, then these
two scalar welds.  The next proof-producing atlas has only 960 labeled
signed assignments in skeleton `(1,1,0;1,1,1)` and 240 in
`(1,0,1;2,0,1)` before source and profile symmetries.  A no-hit search is
not a proof: a universal deletion must print symbolic factors or a complete
canonical certificate with every distinctness/support saturation.  Any
survivor still needs the other seven fibers and paired-product gate.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_442_antipodal_label_classifier`
removes the 960-case atlas for the `(4,4,2)` row.  Shared-loop cancellation
forces

```text
k_B^2=k_AB*k_AC,       k_A^2=k_AB*k_BC.
```

After normalizing by `k_AB`, the labels are `{1,l,m,m^2,l^2}`.  The exact
fifteen-cell antipodal matching table leaves only one scaled sixth-root
hexagon and two eighth-root six-subsets, distinguished by which loop label
is the missing-point singleton.  The banked `F_29` five-set lies off all
three loci, so its complete no-survivor result follows symbolically and no
further fixed-`F_29` enumeration is useful.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_442_exceptional_product_classifier`
then imposes all five Mobius product minors on those loci.  Normalize the
`J` pairs by `A=1`; the only edge-sign invariant is
`tau=sign(AB)sign(AC)sign(BC)`.  Each of the six locus/sign rows reduces to
one quadratic for `b=B/A` and one linear formula for `c=C/A`.  Thus the
entire `(4,4,2)` common-`K` product frontier has at most twelve geometric
packets.  All six algebraic rows are nonempty, so the branch cannot be
deleted at common `K`.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_442_q_orientation_lift`
also closes the remaining common-`K` sign question.  The two squared label
identities each have sign `+/-1`; after choosing the `AB` orbit orientation,
the `AC` and `BC` orientations are uniquely forced.  Exactly two of eight
orientation triples satisfy both welds, and either reconstructs all five
common-fiber Vieta rows.  Therefore construct the `eta` and six `L^c`
records next and apply the paired source-label involution.
Do not reopen generic label, edge-sign, or `b,c` enumeration.

For the second two-loop skeleton, the PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_433_antipodal_label_atlas`
applies the weld to the doubled signed `AB` pair.  If `k_+,k_-` carry the
two products and `k_C` is the other loop label, then

```text
k_C^2=k_+*k_-.
```

Normalize by `k_+`.  The labels are `{1,M,M^2,L,Z}`; the exact fifteen-cell
antipodal table retains nine one-parameter cells and deletes six collision
cells.  The banked `F_29` five-set lies off every retained cell, explaining
its q failure without enumeration.  The next direct calculation should use
products `(-1,-c^2,b,-b,bc)` on `(A,C,+,-,BC)`, impose all five Mobius
minors and the one remaining weld on each of the nine cells, and saturate by
label and signed-pair distinctness.  Do not return to the 240 labeled atlas.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_433_product_minor_cell_cut`
performs the first such pass with two transparent maximal minors.  Cells
`X1,N2,Z1` are impossible because the minor is a product of nonzero label
and signed-pair differences.  Cells `X2,N1,L1` force `b=-c^3`.  At this
intermediate cut, the exact frontier was six cells:

```text
X2,N1,L1 on b=-c^3;       M1,M2,M3 then pending further minors.
```

Substitute the cubic relation before eliminating the first three cells.
Keep the remaining squared weld explicit and treat `M1,M2,M3` separately;
one unsaturated six-cell ideal would reintroduce the deleted collision
components.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_433_constrained_product_q_classifier`
finishes `X2,N1,L1`.  The first two share

```text
P_8(M)=M^4+8M^3-2M^2+8M+1=0
```

and have the sign-specific quadratic

```text
(c^2+1)(M+1)^2 +/- c(M-1)^2=0.
```

Cell `L1` has `M^2=-1`, `2c^4+3c^2+2=0`, and
`3L=4c^3+2c-M`.  These equations are equivalent to all remaining common-`K`
product minors and the second squared weld under the exact guards.  Each
cell contributes at most eight candidates, and guard-passing finite-field
witnesses prove all three common-`K` interfaces are nonempty.  Replay these
24 candidates only during seven-fiber completion; the unresolved
common-`K` work is now exactly `M1,M2,M3`.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m1_product_q_exclusion`
deletes `M1` without suppressing an affine-chart boundary.  On `b+R=0`,
the five raw product minors force `M=R^3` and `c=MR^2`; the remaining weld
would require both `R^6+1=0` and `R^5-R+2=0`, whose resultant is `4`.
On `b+R!=0`, the normalized Mobius chart leaves two product equations and
one squared weld.  A first exact integral ideal certificate forces
`T=MR+3M+5R^2+3R+4=0` under actual guards, while adjoining `T` gives
`b^2(b+1)^2=0`, contradicting distinct nonzero signed `A,B` pairs.
Thus only `M2,M3` remain at the `(4,3,3)` common-`K` interface.  Analyze
their Mobius charts separately, including every chart boundary; do not carry
`M1` into seven-fiber assembly or ask external compute to rediscover it.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m2_m3_product_q_classifier`
finishes those last cells.  With `epsilon=-1` for `M2` and `+1` for `M3`,
both are controlled by the same reciprocal sextic

```text
P_6(M)=M^6+2M^5+7M^4-4M^3+7M^2+2M+1,
```

followed by one signed quadratic for `b` and one linear locator for `c`.
Exact elimination deletes every other factor as a label or signed-pair
collision, and an independent guard saturation returns `P_6` as its unique
univariate row.  The converse reductions and guard-passing `F_41` examples
show that each cell is a genuine common-`K` interface with at most twelve
geometric candidates.

The full `(4,3,3)` common-`K` frontier is therefore complete: four cells are
empty and `X2,N1,L1,M2,M3` have aggregate cap 48 before Galois
identification.  The next work is no longer common-`K` elimination.  Build
the `eta` and six `L^c` records for these five ledgers, apply the paired
source-label involution, and retain only complete-packet survivors for the
remaining q equations.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_433_outside_product_involution_compiler`
supplies the first exact outside record for `M2,M3`.  Their two internal
antipodal `K` pairs determine one explicit nonsingular projective involution
on products.  The singleton is `M`, so antipodality of `I` forces
`xi=I minus K=-M`, and the common-`K` Mobius map gives

```text
p_xi = epsilon b[b(M-1)^2-epsilon(M+1)^2]
       /[b(M+1)^2-epsilon(M-1)^2].
```

Both numerator and denominator are protected on the exact classifier by
iterated resultant `2^32`.  The singleton pair and the remaining three
wholly outside antipodal pairs obey one printed bilinear involution equation.
Thus a completion search must split aligned `xi=eta` from unaligned
`xi in L^c`, assign edge types to the forced `p_xi`, and enforce only those
three scalar rows before full twelve-label interpolation.  Do not rebuild a
generic `6 x 3` paired-product determinant.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_433_complete_edge_skeleton_classifier`
also removes the outside graph search for every surviving `(4,3,3)` cell.
The two common loops already use both roots of the quadratic `A_1`, so no
outside `I-I` record can be antipodal.  Degree four and product injectivity
then force the two colored `I-J` records to attach to distinct `I` pairs;
up to names the seven outside edge types are

```text
B-D, C-E, D-E, D-F(+), D-F(-), E-F(+), E-F(-).
```

Exactly one of the five internal signed types is the `eta` record.  The
other four internal types and the two colored attachments lie in `L^c`.
Combine these five `eta` choices with the forced `xi` location/product and
the three bilinear involution rows; do not enumerate arbitrary degree-four
source multigraphs.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_433_complete_product_invariance_router`
then removes explicit perfect-matching enumeration.  After sign gauge the
outside product multiset is

```text
{bD,cE,tau DE,DF,-DF,EF,-EF},       tau=+/-1,
```

where `D,E,F` are horizontal `T` coordinates and are independent of the
quotient `W` coordinate `M`.  For each of five possible `xi` edge types,
remove its forced value and require the residual binary sextic to be
projectively invariant under the explicit product involution and coprime to
its fixed-point quadratic.  This yields exactly 20 cells across `M2/M3` and
both `tau` signs, replacing 300 sign-gauged perfect matchings.

Attack these invariant cells before full interpolation.  Do not substitute
`D,E,F={1,M,M^2}`: the coefficient normal form normalizes the `T` and
source/quotient projectivities independently, so that tempting resultant is
not typed.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_edge_skeleton_classifier`
gives the parallel complete-source reduction for `(4,4,2)`.  Its two common
loops also spend both roots of `A_1`, so every outside loop is impossible.
Both colored deficits come from the degree-two `C` pair, but product
injectivity forces them to attach to distinct `I` pairs.  Up to names the
outside types are

```text
C-D, C-E, D-E, D-F(+), D-F(-), E-F(+), E-F(-),
```

with one of the five internal signed types at `eta`.  Lift the six exact
common-`K` product rows through this multiset by the same forced-mate and
invariant-binary-form strategy; do not enumerate arbitrary `(4,4,2)` source
graphs.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_442_outside_product_involution_compiler`
now performs the forced-mate step on all six q-compatible common rows.  The
two antipodal pairs already in `K` determine one nonsingular product
involution by an exact row cross product.  The singleton's mate is `xi=-1`
on `H6` and `xi=-l` on either `H8` locus, with product

```text
H6:   b(b l^2+b-l^2+2l-1)/(b l^2-2bl+b-l^2-1),
H8-L: b(2b l^2+2b-l^2+2l-1)/(b l^2-2bl+b-2l^2-2),
H8-M: b(b l^2-2bl+b-2l^2-2)/(2b l^2+2b-l^2+2l-1).
```

The numerator and denominator norms are exactly `1,49,784,8464`; hence the
fractions are finite and nonzero in deployed characteristic.  The forced
singleton pair and the three residual outside pairs obey the same
row-specific bilinear involution.  Build the invariant-binary-sextic router
from these scalar gates and the unique outside edge multiset.  Do not
recompute Mobius kernels or enumerate the fifteen residual perfect
matchings separately.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_product_invariance_router`
also completes the finite paired-product routing.  Sign gauge gives

```text
{cD,cE,sigma DE,DF,-DF,EF,-EF},       sigma=+/-1.
```

The residual `D <-> E` and `F -> -F` symmetry reduces the forced-`xi`
location to three types: a colored `cD`, the internal `sigma DE`, or one of
the four doubled signed types represented by `DF`.  Removing that forced
value and requiring invariance of the residual binary sextic under the
row-specific product involution, together with squarefreeness and
fixed-point avoidance, gives exactly 36 cells across the six common rows.
This replaces 540 sign-gauged perfect matchings.  Saturate these cells before
full interpolation, keeping `D,E,F` independent of the quotient coordinate
`l`; carry the two q orientations only for product survivors.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_442_signed_pair_matching_template_exclusion`
gives the first universal cut inside those cells.  For forced type `cD` or
`sigma DE`, the residual products have form `{a,q,+/-x,+/-y}`.  The two
unsigned values `a,q` cannot pair: the three matchings left on the two signed
pairs force either product negation or a reciprocal involution.  Negation
contradicts a common product pair and injectivity; reciprocity would require
`Alpha=0`, excluded by row norms `30625,18225,49,2401` in deployed
characteristic.  This removes 72 of 540 matching subcases.  Continue with
the twelve mixed templates per affected cell and treat forced `DF`
separately; this is not yet a whole-cell deletion.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8l_minus_cd_cell_exclusion`
completes the first two cells.  On `H8-L,tau=-1`, the common row descends to

```text
P4(b)=b^4-2b^3+b^2-2b+1,
c=(b-2)(b^2+1)/b,       p_xi=1,
```

and the forced-`cD` residual products become
`(a,sigma a/c^2,+/-x,+/-ax)`.  Exact intrinsic resultants and independent
factor norms delete all twelve mixed matchings for each `sigma`; the parent
theorem already deletes the other three.  Both cells are empty, leaving 34
`442` invariant cells and matching cap 444.  Apply this one-parameter
method next to the `sigma DE` and `DF` forced types; do not carry the deleted
colored cells into full interpolation.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8l_minus_complete_product_exclusion`
finishes that program.  Forced `sigma DE` has residual form

```text
(a,sigma c^2/a,+/-x,+/-sigma c^2 x/a^2),
```

and forced `DF` has form

```text
(a,q,sigma aq/c^2,-1,+/-q/a).
```

Factor-by-factor norms delete every ordinary matching.  Six projected `DF`
chains at indices `6,7,8` are not survivors: their full ideals are unit over
the deployed field, and an alternate resultant chain independently deletes
all 30 `DF` sign/matching cases.  Therefore all six cells over
`H8-L,tau=-1` are empty.  The live `442` frontier is five common rows, 30
cells, and matching cap 390.  Do not carry this common row into full
interpolation; test singleton-placement transport to `H8-M,tau=-1` next.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8m_minus_transport_exclusion`
performs that transport.  Loop exchange `A <-> B` followed by normalization
acts by

```text
b'=1/b,       c'=-c/b,       (D',E',F')=-(D,E,F)/b.
```

It sends the `H8-L` label tuple to `H8-M`, scales every common and outside
product by `b^-2`, preserves `sigma` and each forced type, and is involutive.
The `H8-M` forced product is `b'^2`, exactly the scaled image of `1`.
Therefore all six `H8-M,tau=-1` cells are empty.  The live `442` frontier is
four rows, 24 cells, and matching cap 312.  Analyze only the two positive-
sign eighth-root rows and two sixth-root rows next.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8_positive_complete_product_exclusion`
deletes both positive-sign eighth-root rows.  The `H8-L` row descends to

```text
P+(b)=b^4-2b^3-5b^2-2b+1,
c=(-b^2+3b+3)/2,
p_xi=(5b^3-16b^2+8b+8)/23.
```

For all three forced types, exact intrinsic resultants cover both `sigma`
signs.  The only six zero primary projections are unit ideals over the
deployed field, and a second projection order independently has nonzero
deployed norms in all 54 retained sign/matching cases.  Positive loop
exchange acts by

```text
b'=1/b,       c'=c/b,       (D',E',F')=(D,E,F)/b
```

and transports the complete deletion to `H8-M`.  The live `442` frontier is
therefore only `H6,tau=+/-1`: two rows, 12 invariant cells, and cap 156.
Reduce these two quadratic row algebras directly; do not enumerate or
interpolate any H8 packet.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h6_complete_product_exclusion`
closes the remaining rows and therefore the entire `(4,4,2)` skeleton.  On
both H6 rows the protected forced product simplifies to `p_xi=-b`.  A
forced `DF` then leaves `-DF=b`, repeating the common singleton product.
For the two colored forced types, opposite `sigma=-tau` cells have nonzero
exact factor norms.  In aligned `sigma=tau` cells, every mixed-matching ideal
is unit or forces

```text
a^2=b^2,
```

so the other colored product is `+/-b` and repeats either the common value
`b` or the forced value `-b`.  A direct 48-ideal deployed-field audit,
including 24 collision saturations, is independently unit throughout.
Hence no `442` cell reaches complete interpolation.  Remove this skeleton
from downstream work.  Continue with the 20 invariant cells already routed
over `M2/M3`, and build the missing outside forced-mate/invariance compiler
for the separate exact `X2/N1/L1` common-`K` ledgers.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m2_m3_complete_product_exclusion`
now closes those 20 routed cells.  Expressing the seven products through
`X=bD,Y=cE,U=DF` leaves two intrinsic variables for each forced type.  The
75 universal matching eliminations are evaluated in the exact deployed
rank-twelve algebra

```text
F_p[M,b]/(P6,4b^2+epsilon A(M)b+4).
```

All 300 `epsilon x tau x forced-type x matching` obstructions are units.
A second projection order and `12 x 12` multiplication-matrix ranks replay
all cases independently.  Therefore `M2,M3` do not reach full interpolation
or remaining q equations.  The live `(4,3,3)` frontier is now only the
constrained common-`K` ledgers `X2,N1,L1`, which still need their own outside
forced-mate/invariance compiler.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_433_constrained_outside_product_involution_compiler`
supplies that missing interface.  In all three rows `b=-c^3`; exact
candidate-row minors force

```text
X2: p=(-2M^3c+3M^3-16M^2c+24M^2+6Mc-9M-36c+32)/22,
N1: p=( 2M^3c+3M^3+16M^2c+24M^2-6Mc-9M+36c+32)/22,
L1: p=(3c^2+10)/8.
```

The two common antipodal product pairs compile a nonsingular bilinear
involution `Gamma yz-Alpha(y+z)-Beta=0` in each exact rank-eight base
algebra.  All protected constants and the determinant
`Alpha^2+Gamma Beta` are deployed-field units.  This defines exactly 30
cells (`3` ledgers, two outside signs, five forced-product types) without a
false base-field rationality cut.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_two_loop_433_constrained_complete_product_exclusion`
deletes all 30 cells.  The same 75 universal residual matching templates as
the `M2/M3` theorem evaluate to 450 units in the three rank-eight quotient
algebras.  A second projection order and full rank of every `8 x 8`
multiplication matrix independently replay all cases.  Together with the
`M2/M3` parent, the entire `(4,3,3)` complete paired-product skeleton is
empty.  Remove both `442` and `433` from downstream work and recompute the
remaining negative-coordinate source skeletons before starting any new
interpolation or q computation.

After that deletion, the negative coordinate frontier consists of the
zero-loop `(4,3,3)` skeleton `(0,0,0;2,2,1)` and the one-loop skeletons

```text
(4,4,2): (0,1,0;2,2,0),
(4,3,3): (1,0,0;1,1,2).
```

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld` supplies a
common exact interface for the latter two.  If `h` is the loop label and
`p=N/D` is the reconstructed Mobius product map, then on each of the four
nonloops

```text
w_s=q_s/(p_h-p_s)=D(h)C(s)/Delta,       deg C<=1.
```

Thus the four rows `[1,s,w_s]` have rank at most two.  After clearing the
nonzero product differences, two `3 x 3` scalar welds against fixed
nonloop anchors are necessary and sufficient for all five common-`K` sum
equations.  Build the two signed one-loop atlases through these welds before
constructing any of the seven complementary source records.  Treat the
zero-loop row separately through its degree-two interpolation condition.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_zero_loop_product_q_weld` makes
that last condition equally explicit.  Reconstruct `D` from the rank-three
Mobius product rows and put `v_s=q_sD(s)`.  Then

```text
rank [1,s,s^2,v_s]_(s in K)<=3.
```

Any three distinct labels determine the quadratic `-A_1`; the two `4 x 4`
determinants obtained by adjoining the remaining labels are necessary and
sufficient for all five sum equations.  Hence every live negative skeleton
now has exactly two scalar common-`K` q welds after product reconstruction.
The next step is a signed atlas, not another generic determinant compiler.

The first one-loop `(4,4,2)` atlas sector is now exact.  Under the two target
representative sign swaps, the fifteen source matching cells form six
orbits.  The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_aligned_pair_classifier`
treats the orbit where the loop is the singleton and the `AB` and `AC`
signed pairs each occupy one source antipodal pair.  Its common-`K` frontier
is exactly

```text
A: r^2+r+1=0,  b=ir,   c=ir^2, t^2=c;
B: ib^2+b-i=0, c=-1/b, r=-i/b, t^2=-b.
```

Both are guarded finite families, not deleted cells.  Carry them next into
the outside paired-product gate.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_crossed_pair_exclusion`
deletes the other loop-singleton orbit, in which both source antipodal pairs
mix `AB` and `AC` products.  Two ideal consequences have guarded resultant
`-2(b^2-1)`, contradicting target distinctness.  Thus the loop-singleton
sector is complete: two finite aligned families survive and the crossed
orbit is empty.  Four nonloop-singleton matching orbits remain to classify.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_edge_skeleton_classifier`
also fixes the outside graph before either surviving family is expanded.
One common loop permits at most one outside loop.  The two colored records
and five internal records solve the degree equations in exactly three
orbits:

```text
S0: split colored, no loop, internal multiplicities (2,2,1);
S1: split colored, loop on the uncolored pair, internal (1,1,2);
S2: concentrated colored, loop on another pair, internal (0,2,2).
```

Exactly one internal type occupies `eta`.  Apply the paired-product gate to
the two finite aligned families across only these three skeletons and their
finite `eta` choices; do not enumerate arbitrary outside multigraphs.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_aligned_outside_product_router`
performs that product step without expanding arbitrary source placements.
The two common pairs `(b,-b)` and `(c,-c)` force the product involution to
be negation, so the missing mate of the common singleton `-b^2` is `b^2`.
The other six outside products must form three negation pairs.  This deletes
`S0` outright.  It reduces `S1` to two branches, according as the forced
product is the singleton `DE` or `DF` edge, and both obey

```text
d^4=-alpha*beta*gamma*delta*b^2*c^2.
```

It reduces `S2` to the forced-loop equation `-e^2=b^2`.  Guarded `F_73`
witnesses show that `S1` and `S2` are genuine product-level survivors, so
do not delete them.  Apply the one-loop q weld and full interpolation only
to these three routed branches.  Four common matching orbits with a
nonloop singleton remain an independent classification task.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_opposite_pair_exclusion`
deletes one of those four orbits, namely cells `[11,14]`.  In a normalized
cell the `AB` records form an antipodal source pair, the loop is paired with
the nonsingleton `AC` record, and the other `AC` record is the singleton.
The product equation is linear in `c`.  Its coefficient-zero branch forces
`r^4=1`; on the regular branch, one q weld leaves only linear label
collisions or `r^2=+/-i`, and the latter forces `c=1`.  All four root-sign
classes are empty.  The nonloop-singleton frontier is now the three orbits
`[3,6]`, `[4,5,7,8]`, and `[9,10,12,13]`.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_cubic_root_gate`
handles the first exact layer of `[9,10,12,13]`.  In a normalized cell,
the loop is paired with one `AB` record, the other `AB` record is paired
with the nonsingleton `AC` record, and the other `AC` record is the
singleton.  The regular product equation reconstructs `c`; its missing
denominator branch forces a label collision.  One q weld then forces

```text
P_(e1,e2)(r)=r^3+(2e1e2+e1*i)r^2+(-1-2e2*i)r-e1*i=0.
```

This gives at most three `r` values per sign row.  A guarded `F_41` packet
satisfies both common product minors and q welds, so the orbit is genuinely
live.  Reduce the remaining product/q pair in these rank-three quotient
algebras; do not attempt to delete the orbit from the cubic gate alone.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_degree12_gate`
finishes that common-parameter reduction without dividing by the singleton
equations.  Their direct `t`-resultant, followed by the parent cubic
`r`-resultant, forces

```text
G(b)=(b^3-b^2-b-1)(b^3+b^2+b-1)
     (b^6-2b^5+7b^4-8b^3+7b^2-2b+1)=0.
```

The full resultant is `-2^56 b^24(b-1)^12(b+1)^12 G(b)` in every sign
row.  Thus there are at most 72 raw common triples per row before guards.
The `F_41` witness lies on the sextic factor.  Apply outside products to
this finite quotient; do not repeat a generic four-variable common solve.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_explicit_involution_compiler`
now supplies the outside interface for that quotient.  The common pairs
`(-b^2,b)` and `(-b,-c)` determine

```text
Phi(Y,Z)=(c+2b-b^2)YZ+b(c+b^2)(Y+Z)
         -b^2(c-b^2-2bc).
```

Its determinant is the guarded unit
`2b^2(b-1)(b+c)(b^2-c)`.  The common singleton `c` has forced outside mate

```text
m=-b(b^3+3b^2c-bc+c^2)/(b^3-b^2c+3bc+c^2).
```

For each fixed signed cell of `S0,S1,S2`, choose which outside value is `m`
and partition the other six into three `Phi=0` pairs.  This is
`7*15=105` matching templates per signed skeleton cell before symmetry and
quotient reduction.  First quotient the `8,16,1` raw edge-sign choices of
`S0,S1,S2` by target representative changes; use the resulting finite list
rather than arbitrary source placements.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_quotient_classifier`
sharpens the common quotient before that enumeration.  Both cubic factors
of the degree-12 `b` gate force `t=+/-ir`, hence the forbidden label equality
`t^2=-r^2`, in every sign row.  Only

```text
S(b)=b^6-2b^5+7b^4-8b^3+7b^2-2b+1
```

remains.  Each sign row has rank-six standard basis
`{1,b,b^2,r,br,t}`.  The `c`-denominator multiplication determinant is
`2^19`, so reconstruct `c` inside this quotient without a saturation case.
Reduce the 105 outside templates as multiplication/rank calculations in
these rank-six algebras.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_mate_coordinate_compiler`
also removes both rational layers.  Besides the `c` norm `2^19`, the forced
mate denominator has norm `652=4*163` in every sign row.  In the
representative basis,

```text
c=-1+b-b^2/2+(i-1)r/4+(1-i)t/4,
163m=(50-54i)+(87+54i)b-(126+54i)b^2
     +(30+12i)r+(-54+54i)br+(12+30i)t.
```

Evaluate forced-value equations by six-coordinate multiplication first.
Only if such an equation has a nontrivial quotient should the fifteen
residual pairings be expanded.

A first exact `S1` pilot used the representative common sign row, signs
`(alpha,beta,gamma,delta)=(1,-1,-1,1)`, forced `DE`, and residual pairs
`(CE,DF),(CF,-EF),(DD,EF)`.  The six common basis equations plus four
outside equations reached the 60-second local cap before a Groebner basis.
Do not run a local template sweep.  The external request in
`notes/PRIZE_COMPUTE_REQUESTS.md` records the sharding and certificate
requirements; symbolic sign-orbit reduction remains the preferred next
step.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier`
performs that reduction.  Sign changes of `D,E,F` leave exactly

```text
S0: tau_0=alpha*beta*gamma in {+1,-1};
S1: tau_1=alpha*beta*gamma*delta in {+1,-1};
S2: one cell.
```

Thus each common sign row has five signed outside cells, not 25.  The
forced/matching cap is `5*105=525` per common row and `2100` across all four
sextic rows before unsigned skeleton automorphisms.  Use these parity cells
in every external or symbolic continuation.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_template_orbit_classifier`
also quotients the forced-record/matching choices by the valid `E/F`
skeleton automorphisms and by their action on full signed-pair members.  The
exact canonical counts per common sign row are

```text
S0: 64,       S1: 114,       S2: 23,
total: 201.
```

The four-row cap is therefore 804, down from 10,500 raw signed templates.
Emit and evaluate one deterministic representative per orbit; never expand
the raw sign cells or all 2,625 templates per common row.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_invariance_compiler`
supersedes residual matching enumeration.  After removing the forced mate,
put the other six products into the binary sextic `H`.  The residual values
form three product-involution pairs exactly when

```text
H(Alpha X+Beta Z,Gamma X-Alpha Z)=lambda H(X,Z).
```

Product injectivity rules out fixed residual roots, so invariance is also
sufficient.  Quotienting only the signed forced-record cells leaves

```text
S0: 6,       S1: 10,       S2: 4,
total: 20 per common row, 80 over all four rows.
```

The 804 matching orbits remain a completeness audit but are no longer the
compute frontier.  Evaluate the eighty invariant-form cells directly.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_eigenvalue_compiler`
removes the proportionality scalar as well.  With
`Delta=Alpha^2+Beta*Gamma`, fixed-point freedom forces

```text
H(Alpha X+Beta Z,Gamma X-Alpha Z)=Delta^3 H(X,Z).
```

The alternative eigenvalue `-Delta^3` would put both projective fixed points
among the residual roots.  The resulting seven division-free coefficient
equations have rank three, so the accepted outside product frontier is now
eighty cells with three independent scalar conditions each.  Keep all seven
coefficient equations for audit; do not introduce `lambda`, minors, or
matching variables.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_uniform_row_selector`
fixes the independent equations uniformly.  In all four rank-six common
sign quotients, the coefficient minor of rows and columns `(0,1,2)` has
multiplication norm

```text
1133299039 mod 2130706433,
```

so it is a unit.  Therefore evaluate exactly `E_0,E_1,E_2` in every one of
the eighty cells.  No per-row rank calculation remains.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_de_f41_product_witness`
is a route cut against a characteristic-independent product-only deletion.
On the common `F_41` witness, the canonical `S1` sign row with forced `DE`
has the guarded realization

```text
(d,e,f)=(15,7,18),
residual pairs=(35,24),(33,38),(21,3).
```

All seven sextic equations vanish, and the complete 1,600-pair scan finds
this as the unique guarded invariant realization.  This does not establish
a deployed survivor.  Continue with the deployed forced-mate plus
`E_0,E_1,E_2` system, then require an explicit seven-fiber source placement
before claiming any outside-`q` conclusion.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_de_deployed_product_exclusion`
deletes that same canonical cell in the deployed characteristic.  After
`e=-m/d`, `f=sd`, its residual sextic gives three 25-term equations over the
rank-six common algebra.  The algebra splits into two irreducible cubic
fields, and exact Buchberger reduction reaches `1` after 79 S-pairs in each.
This is a raw unit ideal, so no guard saturation is needed.  Reduce the live
outside product frontier from 80 to 79 cells; do not transport the deletion
to another common sign row or forced record without a separate replay.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_de_opposite_parity_deployed_product_exclusion`
replays the other `S1` parity.  Its only factor change is
`dX+cmZ -> dX-cmZ`; both cubic components again reach `1` after 79 S-pairs.
Therefore both forced-`DE/DF` parity cells are empty in common sign row
`(1,1)`, and the accepted frontier is 78.  The other three common sign rows
remain untransported.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_colored_deployed_product_exclusion`
deletes both forced-`CE/CF` parity cells in the same common sign row.  The
forced equation `-ce=m` fixes `e=-m/c`; each parity gives three 23-term
equations, and both cubic components reach `1` after 56 S-pairs.  Four of
the ten `S1` cells in row `(1,1)` are now deleted.  The accepted four-row
frontier is 76.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_ef_tau_plus_guarded_product_exclusion`
deletes both forced-`EF+/-` cells in the `tau_1=+1` parity of common sign row
`(1,1)`.  After `f=sigma*m/e`, each three-equation system has 19 terms.  Its
completed basis contains `e=0` in both cubic components.  This is a guarded,
not raw-unit, deletion because target representatives are nonzero.  The
accepted frontier is 74.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_ef_tau_minus_guarded_product_exclusion`
does the same for `tau_1=-1`.  Its systems have 17 terms and again finish
with the forbidden guard equation `e=0` after 435 S-pairs.  Thus eight of ten
`S1` cells in common sign row `(1,1)` are deleted; only its two forced-loop
cells remain.  The accepted four-row frontier is 72.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_loop_deployed_product_exclusion`
deletes those last two representative-row `S1` cells.  Forcing `-d^2=m`
requires the genuine quadratic extension `theta^2=-m` of each cubic common
component; `-m` is a nonsquare in both.  The two parity systems each have
three 17-term equations.  Exact tower-field Buchberger reduction reaches
`1` after 57 S-pairs for `delta=-1` and 55 for `delta=+1`, in both cubic
components.  Thus all ten `S1` cells in common sign row `(1,1)` are empty
at product level and the accepted four-row frontier is 70.  No deletion is
transported to another common sign row, and the `S0`, `S2`, outside-`q`, and
interpolation tasks remain live.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_common_sign_product_transport`
now supplies the missing all-row transport at product level.  Under the
canonical maps to both cubic components, the exact coefficient triples of
`c` and `m` are identical in all four common root-sign rows.  Every `S1`
binary-sextic action and residual forced-record form is a polynomial in
`b,c,m` and its outside parity; the loop tower is uniformly
`theta^2=-m`.  Hence the ten representative-row exclusions transport
coefficient for coefficient to the other three rows.  Delete all forty
`S1` product cells and reduce the accepted frontier from 70 to 40: six
`S0` and four `S2` cells remain in each row.  This does not transport the
source-root or `q` equations.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s2_forced_colored_deployed_product_exclusion`
deletes the first `S2` orbit in all four rows.  Forcing `sigma*cd=m` leaves

```text
(X+mZ)(X+e^2 Z)(X^2-(m/c)^2 f^2 Z^2)(X^2-e^2 f^2 Z^2).
```

The three equations have seven monomials and reach the raw unit ideal after
seven S-pairs in both cubic components.  The forced sign disappears and the
all-row `b,c,m` identity transports the certificate.  Reduce the accepted
frontier from 40 to 36; six `S0` and three `S2` cells remain per row.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s2_forced_ef_guarded_product_exclusion`
deletes the forced-`EF` `S2` orbit in every row.  Clearing the admissible
denominator after `sigma*ef=m` gives

```text
(X^2-c^2d^2Z^2)(X+e^2Z)(e^2X^2-m^2d^2Z^2)(X+mZ).
```

Its three seven-term equations complete after 28 S-pairs with the monic
basis element `e^2` in both cubic components.  Since outside representatives
are nonzero, this is a guarded deletion, not a raw unit ideal.  Transport it
using the common `b,c,m` identity and reduce the frontier from 36 to 32;
six `S0` and two `S2` cells remain per row.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s2_forced_df_guarded_product_exclusion`
deletes the forced-`DF` `S2` orbit in every row.  Clearing `d^2` after
`sigma*df=m` gives

```text
(X^2-c^2d^2Z^2)(X+e^2Z)(X+mZ)(d^2X^2-m^2e^2Z^2).
```

Both cubic-component bases complete after 28 S-pairs and contain the monic
elements `d^2` and `e^2`.  This contradicts the required `d!=0` guard.
Transport the guarded deletion using the common product data and reduce the
frontier from 32 to 28; six `S0` and one forced-loop `S2` cell remain per
row.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s2_forced_loop_deployed_product_exclusion`
deletes the last `S2` orbit in every row.  Forcing `-e^2=m` leaves three
full signed pairs, so the square-root choice disappears and the residual is

```text
(X^2-c^2d^2Z^2)(X^2-d^2f^2Z^2)(X^2+m f^2Z^2).
```

Its three seven-term equations reach the raw unit ideal after seven S-pairs
in both components.  Transport gives the same result in every common row.
All sixteen `S2` cells are now empty at product level.  Reduce the accepted
frontier from 28 to 24, consisting exactly of six `S0` cells per row.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s0_forced_colored_deployed_product_exclusion`
deletes both parities of the forced-`CE/CF` type in every row.  With
`alpha=beta=1`, `gamma=tau_0`, and `CE=m`, the residual form is

```text
(X-cfZ)(X^2-(m/c)^2d^2Z^2)(X^2-d^2f^2Z^2)
(X-tau_0(m/c)fZ).
```

For either parity, the three equations have eleven monomials and reach the
raw unit ideal after 29 S-pairs in both components.  The common-product
identity transports both deletions.  Reduce the frontier from 24 to 16;
two forced-`EF` and two forced-internal `S0` cells remain per row.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s0_forced_ef_guarded_product_exclusion`
deletes both forced-`EF` parities in every row.  After `tau_0*ef=m`, clear
the admissible factor `e^3` to obtain

```text
(X-ceZ)(eX-tau_0*cmZ)(X^2-d^2e^2Z^2)
(e^2X^2-m^2d^2Z^2).
```

For either parity, the three equations have twelve monomials.  Both cubic
components complete after 190 S-pairs with monic `e^2`, contradicting
`e!=0`.  Transport both guarded deletions and reduce the
frontier from 16 to 8; only two forced-internal parity cells remain per row.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s0_forced_internal_guarded_product_exclusion`
deletes the final two `S0` parities in every row.  After `de=m`, clear the
admissible factor `d^2` to obtain

```text
(dX-cmZ)(X-cfZ)(X+mZ)(X^2-d^2f^2Z^2)
(dX-tau_0*mfZ).
```

For either parity, the three equations have fourteen monomials.  Both
components complete after 406 S-pairs with monic `f`, contradicting the
nonzero outside guard.  Transport gives all eight final deletions.  Thus all
24 `S0`, 40 `S1`, and 16 `S2` cells are empty: the accepted 80-cell product
frontier for common orbit `[9,10,12,13]` is closed.  Do not run its q or
interpolation stages; return to the other common matching orbits.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_finite_classifier`
now classifies common orbit `[3,6]`.  In a representative cell the
`AB+` record is the singleton, the loop pairs with `AB-`, and the two
`AC` records pair.  After the guarded product reconstruction, one q weld
is linear in `t`.  Substitution and direct `b` elimination leave exactly

```text
r^2=-epsilon_2*i,       2b^2+3b+2=0,
t=(-epsilon_1*i*r^2-2r-epsilon_1*i)
  /(r^2+2epsilon_1*i*r+1),
c=b(bU-V)/(bV-U).
```

There are four guarded packets in each root-sign row and sixteen total in
the deployed field.  Thus `[3,6]` is finite but live.  Compile its product
involution and outside mate next; the only common matching orbit still
unclassified is `[4,5,7,8]`.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_product_involution_compiler`
compresses the next product layer.  Every one of the sixteen common packets
also has `4c^2=5b+6`.  The pairs `(-b^2,-b)` and `(c,-c)` determine

```text
Gamma=b(b+1), Alpha=-(b^3+c^2), Beta=-b(b+1)c^2,
det=(b-c)(b+c)(b^2-c)(b^2+c),
m=iota(b)=(18-5b)/22.
```

The determinant is a product guard and the mate denominator has resultant
`176` against `2b^2+3b+2`.  Therefore every outside product cell must
contain `m` and split its other six values into three involution pairs.
Compile these templates directly over the quadratic `b` algebra; do not
carry the sixteen source-root packets into the product stage.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_s2_product_exclusion`
deletes the entire `S2` product skeleton over this common orbit.  In both
`b` rows the forced-colored and forced-loop systems are raw units after
seven S-pairs.  The forced-`DF` basis contains `d^2,e^2`, and the
forced-`EF` basis contains `e^2`; these contradict nonzero outside
representatives.  The systems use only `c^2`, so `c -> -c` transports
the certificates to every common packet.  Continue with the six `S0` and
ten `S1` forced-record cells; no `S2` q or interpolation work remains.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_s0_product_exclusion`
also deletes all six canonical `S0` cells.  In both `b` rows and both
parities, forced colored is a raw unit after 29 S-pairs, forced `EF`
contains `s^2` after 190, and forced internal contains `s` after 406.
The latter variable is a nonzero outside representative.  Simultaneously
flipping the two colored outside signs transports `c -> -c` without
changing parity.  Thus only the ten `S1` product cells remain for common
orbit `[3,6]`.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_s1_product_exclusion`
closes those final ten cells.  Forced internal and colored cells are raw
units after 79 and 56 S-pairs.  All four forced-`EF` bases contain the
nonzero representative `s` after 435 pairs.  The two forced-loop cells
need no extension because

```text
101399882^2=-893470876,       592085280^2=-1479361290,
```

and their 17-term systems are raw units after 55/57 pairs.  Both `b` rows
and the exact `c`-sign transport are covered.  Hence all
`S0=6,S1=10,S2=4` canonical product cells are empty and common orbit
`[3,6]` is retired.  Do not run q or interpolation.  The sole
unclassified one-loop 442 common orbit is now `[4,5,7,8]`.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_mixed_pair_exclusion`
deletes that final nonloop common orbit.  In a cell `4` representative,
product reconstruction gives

```text
A=r^2t^2-1, B=r^2-t^2, c=-b(bA+B)/(bB+A),
```

and the first q weld splits into `Q0: rt+1=0` and
`Q1: rt-epsilon_1*i(r+t)-1=0`.  For `Q0`, direct elimination has

```text
r^2(r^2+1)^2(r^2-1)^3
  (r^2+epsilon_2*i)(r^2-epsilon_2*i)^3;
```

the final two factors force `b=1`.  For `Q1`, the resultant is
`r^2(r+epsilon_1*i)(r+epsilon_1*epsilon_2)`.  Every root is therefore a
source guard.  All four sign rows and cells `[4,5,7,8]` are empty.  The
only remaining one-loop 442 work is the aligned loop-singleton family:
its surviving product cells still require the q weld and full
interpolation.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_aligned_loop_q_exclusion`
closes that final family before a full outside interpolation.  The common
Vieta rows compile to

```text
A: F(W)=b/W, A_1 proportional to (W-c)(W-i),
B: F(W)=bW,  A_1 proportional to (W+b)(W-i).
```

The common loop occupies `W=c` or `W=-b`.  Every retained `S1/S2`
skeleton has one outside loop, so `q=0` and pointwise `B_2!=0` force its
label to the other root `W=i`.  Its product is therefore `r` in family A
or `ib` in family B.  For `S1`, this contradicts
`d^4=-alpha*beta*gamma*delta*b^2c^2`; for `S2`, it contradicts the
forced product `b^2`.  Thus the aligned orbit is empty and no nonloop
outside q row is needed.  Compose this with the crossed and four
nonloop-singleton orbit dispositions to close the complete one-loop 442
matching atlas.
