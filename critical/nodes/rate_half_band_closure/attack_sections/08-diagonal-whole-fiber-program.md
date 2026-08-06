
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
