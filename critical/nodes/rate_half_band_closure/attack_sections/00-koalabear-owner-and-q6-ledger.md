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
