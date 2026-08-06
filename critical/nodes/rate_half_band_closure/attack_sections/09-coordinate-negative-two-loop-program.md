
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
