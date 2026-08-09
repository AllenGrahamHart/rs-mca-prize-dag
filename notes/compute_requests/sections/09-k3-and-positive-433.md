
## CR-K3-M2-R4-DIAGONAL-FACET-SAT: order-two whole-fiber defect classifier

**Status:** REQUEST DESIGN; not authorized for local or Modal execution
until the completeness router and proof-producing backend below exist.
This is a contributor request for the `K3` exact second-moment/source-facet
frontier, not a paid local fleet.

### Mathematical decision

The PROVED
`rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler` gives
the correct necessary symmetry for the diagonal stabilizer
`<tau x tau>`. For each quotient source label `p`, the two quadratic
component stars form a quartic divisor `R_p` and

```text
[R_bar(p)]=[tau^*R_p].
```

The automorphism need not preserve the source `X`-line. Therefore the
four root incidences over one complete `psi` fiber are transported as a
multiset and may be repartitioned into the two destination stars.
Individual-star transport is forbidden in this request.

Decide whether there exists any abstract packet satisfying all of:

1. the two source-label cases from Corollary 9.25,
   `L=I` or `|L intersect I|=5`, with
   `K subset I intersect L` and `|K|=5`;
2. one of the four complete two-regular pole-graph cycle types
   `6`, `4+2`, `3+3`, `2+2+2`, including every labeled
   diagonal-free graph and every canonical facet bijection
   `I -> L^c` up to a proved relabeling action;
3. one two-subset component star in each of the 24 divisor slots, with
   repeated slots allowed exactly as required by ramified degree-two
   fibers;
4. the `K`, `eta in L minus K`, and paired one-exchange facet
   containments of Corollary 9.27;
5. source degree four at every one of the twelve labels;
6. exactly four component-colored pole edges;
7. complete-source defect at most three; and
8. one fixed-point-free endpoint involution `bar` such that the
   four-incidence multiset over `bar(p)` is the `bar`-image of the
   multiset over `p`.

### Proof-producing output

A positive result must emit one canonical JSON survivor containing
`I,L,K`, the facet bijection, pole graph, endpoint involution, all 24
stars with divisor-slot multiplicities, color assignment, degree vector,
defect, and the twelve whole-fiber transport checks. The independent
checker must reconstruct every item from the raw records.

A negative result must emit an independently checkable UNSAT certificate
for every canonical stratum. Preferred formats are DRAT/LRAT with a pinned
SAT encoder and a second checker, or a smaller exact case certificate whose
completeness proof is readable without trusting the enumerator. A no-hit
search, optimizer lower bound without a proof object, or one labeled graph
does not promote a node.

If every stratum is UNSAT, the diagonal order-two orientation is deleted
before the `35 x 12` interpolation gate. If a survivor exists, it becomes
the sole input to that exact matrix gate and prevents further
facet/defect-only work.

### Pilot and resource law

A RAMguard pilot on 2026-07-30 fixed the aligned `L=I` case and one
`4+2` pole graph. An exact suffix-pruned check found no defect-at-most-three
survivor among the first 3,000 of 10,395 endpoint involutions before the
30-second hard stop. One isolated feasible involution was proved by complete
local enumeration to have minimum defect six. These are route-selection
observations only: the remaining involutions, other labeled graphs,
misaligned case, and other cycle types were not checked.

Do not resume this as repeated laptop shards. Before external launch:

1. prove the canonical-orbit router covers all labeled `I,L,K`, facet,
   graph, ramification, and involution data;
2. make the encoder resumable per canonical stratum;
3. cap each worker at one CPU and 512 MiB;
4. measure one complete stratum and publish the projected aggregate cost;
5. require compact proof artifacts and deterministic independent replay.

The expected computation is finite and small-memory, but no dollar estimate
is accepted until the canonical router and one proof-producing pilot are
measured. Large raw enumeration without certificates is out of scope.

## CR-K3-M2-R4-COORDINATE-VIETA-F29: signed-edge gate falsifier

**Status:** BLOCKED BEFORE START by the Modal workspace spend limit on
2026-07-30. No app id was allocated and no credit was spent. Do not retry
until the workspace limit is restored. One container only; no fleet.

The PROVED
`rate_half_kb_m2_r4_coordinate_k_fiber_vieta_rank_compiler` supplies exact
`10 x 8` positive and `10 x 7` negative common-`K` kernel gates. Before a
large symbolic elimination, test whether those gates can already be made
universally nonzero from the two allowed coordinate degree profiles.

The pilot fixes the exact field/configuration

```text
F_29,
I={+/-1,+/-4,+/-9},
J={+/-2,+/-3,+/-5},
xi=-9=20,
K=I minus {xi}={1,28,4,25,9}.
```

All five `K` values are squares. Exhaust the `15^5` ordered assignments of
the three antipodal edge orbits and the six nonantipodal edge orbits with
both lift orientations. Retain exactly the proved pair-degree profiles
`(4,4,2)` and `(4,3,3)` up to pair permutation and exact duplicate-edge
defect at most three. For every retained packet,
reconstruct the two exact Vieta matrices, require nonvanishing leading
support and a nonzero odd part, and test every aligned squarefree quadratic
`c` supported on two `J` labels against both full quotient identities.

Launcher:

```text
tools/ramguard modal -- ~/.venvs/modal/bin/modal run \
  critical/nodes/rate_half_band_closure/notes/kb_coordinate_vieta_f29_falsifier_modal.py
```

Resource cap: one CPU, 256 MiB, a 60-second hard container timeout, and an
internal 52-second partial-output deadline. Conservative cost is below
`$0.01`, hence below the campaign `$1` ceiling. The worker returns the first
exact positive/negative gate witnesses, complete counters, and any full
quotient witness. The independent local checker is
`verify_kb_coordinate_vieta_f29_witness.py`.

Semantics:

- `PASS` with a gate witness: exact falsification of any claim that the
  printed degree profiles alone force the corresponding determinant nonzero;
- `PASS` with a full quotient witness: stronger small-characteristic route
  falsifier requiring side-condition and liftability analysis;
- complete no-witness output: exact only for this fixed `F_29` label packet,
  evidence only for the universal coordinate branch;
- timeout: partial evidence only, with counters and any retained witnesses;
- no outcome closes or refutes the deployed-field coordinate orientation.

The blocked pilot has already been superseded for route selection by the
hand-constructed and independently replayed PROVED node
`rate_half_kb_m2_r4_coordinate_vieta_profile_only_f29_route_cut`. That node
gives one defect-two positive rank-seven witness and shows that its forced
colored quadratic is unsupported. A future launch is useful only as a
complete census of this fixed label packet, not as discovery of the first
witness.

## CR-K3-M2-R4-COORDINATE-COMPLETE-PRODUCT: canonical packet classifier

**Status:** EXTERNAL/DEFERRED.  Do not launch while the Modal workspace spend
limit is active.  No cost estimate is accepted until one canonical stratum
is measured; aggregate cost must remain below the campaign ceiling or be
explicitly reauthorized.

The PROVED
`rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler` replaces the
five-`K` determinant search by complete twelve-fiber product gates.  A
proof-producing classifier should:

1. canonically enumerate complete coordinate source-facet packets, including
   `I,L,K,eta`, the two paired degree profiles, all six complement records,
   pole-graph colors, and defect at most three;
2. form the exact `12 x 6` positive and `12 x 4` negative product matrices;
   for negative parity first apply the `6 x 3` paired-product involution
   matrix from `(KBNP-1)`; apply the same gate to positive kernels whose
   ratio `A_0/A_2` reduces to degree at most one;
3. emit a nonzero maximal-minor certificate for each deleted packet orbit;
4. emit every survivor with its exact product-map kernel and leading-support
   values, then lift only those survivors to the complete `q` system;
5. independently replay packet completeness, canonical-orbit ownership, and
   every minor from compact artifacts.

The negative lane now starts from only the five loop-budget survivors in
`(KBNL-2)`.  Apply the symbolic `(KBNP-3)` rule before any minors: two
distinct antisymmetric product pairs force every pair to be antisymmetric
and already delete the banked defect-zero fixture.  The positive lane must
use all twelve rows: the exact
defect-zero fixture has 140 of 5,040 `F_29` separator survivors, although no
assignment in that fixed family survives the complete product matrix.

Within the negative lane, shard first by loop count and use `(KBNQ-3)`.
The two loop-count-two skeletons require only signed `3 x 3` q determinants;
do not send their already-consumed loop rows to a generic `10 x 7` kernel.
After the product matrix passes, replace that determinant by `(KBNW-2)`:
the unique rank-three Mobius kernel fixes `B_2`, and two scalar product-to-q
welds are necessary and sufficient for all five common-fiber sum rows.  The
two labeled signed atlases have raw sizes 960 and 240.  Canonicalization must
retain edge-orbit orientations, and a negative answer must certify the
product minors or weld residuals for every orbit rather than report no hits.

The 960-row `(4,4,2)` atlas is now superseded by two PROVED symbolic
classifiers.  Its common-`K` survivors lie on only three antipodal label
loci, and all product-rank survivors are the six quadratic-linear rows
`(KB4P-3)--(KB4P-5)`, at most twelve geometric packets.  An external worker
must start from those rows and their two PROVED q-compatible orientation
classes, then compile the `eta` plus six `L^c` records.  Do not spend compute
rediscovering either common-`K` products or q signs.

The `(4,4,2)` outside graph is also PROVED unique and loop-free.  Its two
colored records are `C-D,C-E` with distinct `I` attachments, and its five
internal types are `D-E,+/-D-F,+/-E-F`, one of which is `eta`.  Any future
worker must combine this multiset with the six common-`K` product rows and
their two q orientations; arbitrary outside graph enumeration is obsolete.

The forced outside mate is now also PROVED for all six rows.  It is `-1` on
`H6` and `-l` on `H8`, with a printed product fraction whose protected norms
are `1,49,784,8464`; the two common pairs fix one explicit bilinear product
involution controlling the forced pair and the three residual pairs.  A
worker must start from this compiler, remove the forced value from the
seven-product outside multiset, and test one invariant binary sextic per
sign-gauged cell.  Re-solving a common Mobius map or enumerating fifteen
perfect matchings per row is outside the accepted request.

The accepted `442` paired-product input is exactly 36 invariant-form cells:
six common rows, `sigma=+/-1`, and three forced-`xi` location orbits.  The
seven products are `{cD,cE,sigma DE,+/-DF,+/-EF}`.  Remove the forced value,
then impose projective invariance of the residual binary sextic under the
printed row involution, product distinctness, and fixed-point exclusion.
Carry both q orientations only after a product cell survives.  The
horizontal variables `D,E,F` are independent of `l`; any task identifying
them with powers of `l` must be rejected.

If the 36 exact saturations are too costly, shard one cell per external
task with explicit memory/runtime limits and compact unit-ideal or survivor
certificates.  No local fleet is authorized.

The first 72 matching templates are now deleted symbolically: in forced
`cD` and `sigma DE` cells, the two unsigned residual products cannot pair.
Any external worker must skip those three matchings in each of the 24
affected cells, leaving cap 468 across all cells.

A bounded 30-shard pilot for `H8-L,tau=-1,xi=cD` is stored at
`critical/nodes/rate_half_band_closure/notes/kb_442_h8l_minus_cd_pairing_modal.py`.
Each shard uses one CPU, 512 MiB, and timeout 60 seconds, with explicit
partial `ERROR` rows.  The 2026-07-30 launch was rejected before any
container started because the Modal workspace had exceeded its spend limit;
cost was zero and no computational result was claimed.  This request may be
replayed externally after skipping the three already-proved templates.

That pilot target is now closed symbolically and must not be replayed for
discovery.  The common row descends to one quartic `P4(b)` and the residual
cell to two intrinsic variables; exact factor norms delete all 15 matchings
for both `sigma` signs.  The live `442` compute frontier has 34 cells and
matching cap 444.  Reuse the univariate descent for forced `sigma DE` and
`DF`; do not spend containers on the deleted `xi=cD` cells.

The remaining `H8-L,tau=-1` cells are now also PROVED empty.  Forced `DE`
and `DF` reduce to two intrinsic variables over the same quartic; exact
factor norms, six deployed-field unit ideals, and an alternate resultant
audit close every matching.  The entire common row is dead.  The accepted
`442` compute frontier is now five rows, 30 cells, matching cap 390.  Any
worker retaining `H8-L,tau=-1` is using an obsolete frontier.

The equal-degree loop exchange now also PROVES `H8-M,tau=-1` empty; no
compute is needed for that row.  The accepted `442` frontier is four rows,
24 cells, matching cap 312.  External workers must exclude both negative-
sign eighth-root singleton placements.

Both positive-sign eighth-root rows are now PROVED empty as well.  Exact
quartic factor norms, six deployed-field unit ideals, and a 54-case
alternate resultant audit close `H8-L,tau=+1`; positive loop exchange closes
`H8-M,tau=+1`.  The accepted `442` compute frontier is only the two H6 rows,
12 invariant cells, and matching cap 156.  Any external worker retaining an
H8 row is using an obsolete frontier.  These remaining rows have quadratic
base algebras and should be attempted symbolically before requesting any
container fleet.

The two H6 rows are now PROVED empty too, so the accepted `(4,4,2)` compute
frontier is empty.  The forced value `-b` either causes an immediate `DF`
product collision or reduces every aligned colored matching to the collision
divisor `a^2=b^2`; the opposite-sign cells have nonzero exact norms.  A
48-ideal deployed-field audit confirms the guarded deletion.  No external
worker should launch a `442` cell, matching, q-orientation, or interpolation
task.  The next already-routed negative two-loop compute frontier, if
symbolic work does not close it first, is the 20 invariant cells over
`M2/M3`.  The other three surviving `(4,3,3)` common-`K` ledgers
`X2/N1/L1` first require their own exact outside forced-mate/invariance
compiler and must not be folded into that 20-cell count.

The 240-row `(4,3,3)`
two-loop atlas is also superseded at the label level: `(KB43-3)` gives nine
one-parameter antipodal cells.  The first product-minor cut deletes
`X1,N2,Z1` and forces `b=-c^3` on `X2,N1,L1`.  At that intermediate stage,
only those three constrained cells and `M1,M2,M3` remained; the subsequent
paragraphs record their completed common-`K` classification.  Any replay
must use these symbolic ledgers, not the original labeled assignments.

The constrained cells are now fully compiled: `X2,N1` use one reciprocal
quartic in `M` plus a quadratic in `c`, and `L1` uses degrees `2 x 4` with a
linear locator.  Their total common-`K` cap is 24, with exact witnesses.
External work should not eliminate them again; carry them into complete
source-facet/seven-fiber assembly.  `M1` is now PROVED empty by a raw-boundary
resultant and an exact two-stage interior ideal certificate.  `M2,M3` are
also fully compiled: both use one shared reciprocal sextic followed by a
signed quadratic and a linear locator, with cap 12 per cell.  Thus all nine
`(4,3,3)` common-`K` cells are classified; the five surviving ledgers have
aggregate cap 48.  External work must start from those finite ledgers and
construct `eta` plus the six complementary source-fiber records.  Do not
spend compute on any common-`K` cell elimination.

For `M2,M3`, apply the PROVED outside-product compiler before enumerating
edge types.  It forces `xi=-M`, gives `p_xi` as an explicit rational function
whose numerator and denominator have resultant `2^32`, and fixes one
nonsingular bilinear involution for the singleton pair plus the three wholly
outside antipodal pairs.  Shard aligned `xi=eta` from unaligned `xi in L^c`
and, in the latter, colored from uncolored `xi`.  Only survivors of these
scalar gates should enter the full twelve-row Mobius interpolation.

The outside signed-pair graph is also PROVED unique.  There are no outside
loops; the two colored `I-J` records attach to distinct `I` pairs, and the
five internal multiplicities are `(1,2,2)`.  Up to pair names, enumerate
only `B-D,C-E,D-E,D-F(+/-),E-F(+/-)`, with one of the five internal signed
types assigned to `eta`.  A worker that generates arbitrary outside
multigraphs is outside the accepted request.

The accepted paired-product input is now exactly 20 invariant-form cells:
`M2/M3`, `tau=+/-1`, and five possible forced-`xi` edge types.  In each,
remove the forced product from `{bD,cE,tau DE,+/-DF,+/-EF}` and impose
projective invariance of the residual binary sextic under the printed
product involution, plus fixed-point and distinctness saturation.  This
replaces 300 perfect matchings.  The variables `D,E,F` are independent
horizontal coordinates; any worker substituting powers of the quotient
coordinate `M` is invalid and its output must be rejected.

If exact saturation or full-interpolation elimination for all 20 cells is
too expensive for the campaign budget, shard one cell per task with a hard
runtime/memory declaration, deterministic partial output, and a compact
certificate for every unit ideal or survivor component.  No such fleet is
authorized locally at present.

The 20 `M2/M3` cells are now PROVED empty and this request is obsolete.
Universal elimination of the two intrinsic horizontal variables gives 75
matching obstructions; all 300 sign/base evaluations are units in the exact
deployed rank-twelve quotient algebra.  Alternate projection and
multiplication-matrix audits replay every case.  Do not launch an `M2/M3`
product, interpolation, or q task.

The constrained `X2,N1,L1` cells are now PROVED empty as well.  Their exact
outside compiler gives three rank-eight base algebras, finite nonzero forced
products, and nonsingular bilinear product involutions.  The same 75
universal matching templates give 450/450 unit obstructions, independently
replayed by alternate projections and rank-eight multiplication matrices.
Thus the complete `(4,3,3)` paired-product frontier is empty.  No external
worker should launch a `433` cell, matching, q-orientation, or interpolation
task.  Together with the preceding `442` close, both currently compiled
negative two-loop skeletons are obsolete compute targets; recompute the live
coordinate skeleton census before posing another campaign.

Suggested pilot: one canonical packet stratum, one CPU, at most 512 MiB,
60 seconds, deterministic partial output, and no parallel fleet.  Modular
reconnaissance is evidence only; universal deletion requires symbolic or
proof-producing certificates whose saturations include distinct labels,
nonzero leading support, and the source-facet side conditions.

## Request: negative one-loop 442 sextic outside templates

The live common orbit `[9,10,12,13]` is now reduced to four rank-six sextic
quotients.  The two cubic factors of the former degree-12 gate are PROVED
empty.  In each live sign row the standard basis is

```text
{1,b,b^2,r,br,t},
S(b)=b^6-2b^5+7b^4-8b^3+7b^2-2b+1,
Norm(D_c)=2^19,       Norm(D_m)=652.
```

The explicit product involution is

```text
Phi(Y,Z)=(c+2b-b^2)YZ+b(c+b^2)(Y+Z)
         -b^2(c-b^2-2bc),
```

and the common singleton `c` has one forced outside mate `m`.  For each
fixed signed outside cell, choose one of seven products to equal `m` and one
of fifteen perfect matchings of the other six products.  The raw edge-sign
counts before target-sign symmetry are `S0=8`, `S1=16`, and `S2=1`; hence
`105` templates per signed cell, not per unsigned skeleton.

The target-representative sign quotient is now PROVED and must be used:

```text
S0: two parity cells tau_0=alpha beta gamma,
S1: two parity cells tau_1=alpha beta gamma delta,
S2: one cell.
```

Therefore the accepted cap is five signed cells and `525` templates per
common sign row, or `2100` over all four sextic rows, before quotienting by
the residual unsigned skeleton automorphisms.  A worker that expands the
original 25 sign cells is obsolete.

The residual template quotient is also now PROVED.  Simultaneous action on
the sign cell, forced record, full-pair members, and residual matching gives

```text
S0: 840 raw -> 64 canonical,
S1: 1680 raw -> 114 canonical,
S2: 105 raw -> 23 canonical.
```

The accepted compute cap is therefore 201 templates per common sign row and
804 over all four sextic rows.  The orbit-size distributions and a complete
enumerator are in the template-orbit classifier node.  External workers
must consume its deterministic representatives; the former 2,100-row cap
is obsolete.

The residual matching endpoint is now itself obsolete.  The PROVED binary-
sextic compiler replaces fifteen matchings by one invariant-form test after
the forced record is removed.  Quotienting signed forced records gives

```text
S0: 6 cells,       S1: 10 cells,       S2: 4 cells
```

per common sign row.  The accepted frontier is twenty invariant-form cells
per row and eighty over all four sextic rows.  The 804 matching orbits remain
an independent completeness audit only.  External workers must impose
coefficient proportionality of

```text
H(Alpha X+Beta Z,Gamma X-Alpha Z) and H(X,Z)
```

and must not enumerate residual perfect matchings.

The unknown-scalar formulation is now also obsolete.  The PROVED
binary-sextic eigenvalue compiler forces the exact identity

```text
H(M(X,Z))=Delta^3 H(X,Z),  Delta=Alpha^2+Beta*Gamma.
```

Its seven coefficient equations have rank three.  External workers should
reduce three independent equations per canonical cell and retain all seven
only as an audit.  They must not add a proportionality scalar or coefficient
minors.  The accepted workload is eighty cells times three scalar
conditions before outside sums and interpolation.

The row choice is now fixed as well.  The PROVED uniform-row selector shows
that `E_0,E_1,E_2` are independent in all four common sign quotients; their
`(h_0,h_1,h_2)` minor has deployed multiplication norm `1133299039`.
Workers should use those three equations exactly and should not spend a
shard selecting or row-reducing coefficient equations.

One caution is now exact.  The canonical `S1` forced-`DE` cell has a guarded
product-invariant `F_41` realization `(d,e,f)=(15,7,18)` on the printed
common witness, with all twelve products distinct.  A complete 1,600-pair
scan finds it uniquely.  Therefore a characteristic-independent
product-only contradiction does not exist for this cell.  Deployed shards
remain useful, but any deployed product survivor must be handed to the
seven outside source-fiber/`q` assignment; product survival is not packet
survival.

The representative deployed `S1` forced-`DE` task is complete and should no
longer be requested.  Sparse quotient multiplication gives three 25-term
polynomials; splitting the common algebra into its two irreducible cubic
fields gives the unit ideal after 79 S-pairs in each.  The accepted frontier
is now 79 cells.  External workers may reuse the checked sparse builder and
cubic-field solver on another canonical cell, but must pin its common signs,
outside signs, and forced record explicitly.

The opposite `S1` parity for the same forced-`DE/DF` type is also complete:
changing the first sparse factor from `dX+cmZ` to `dX-cmZ` again gives the
unit ideal after 79 S-pairs in both cubic components.  The accepted frontier
is 78.  Do not request either parity of this forced type in common sign row
`(1,1)`.

Both forced-`CE/CF` parity cells in common sign row `(1,1)` are now complete
as well.  Their three equations have 23 terms and reach the unit ideal after
56 S-pairs in each cubic component.  The accepted frontier is 76; these two
cells should not be requested again.

The two `tau_1=+1` forced-`EF+/-` cells in common row `(1,1)` are also
complete.  Their exact bases contain the forbidden coordinate `e`, after
435 S-pairs in each cubic component.  These are guard-saturated deletions,
not raw unit ideals.  The accepted frontier is 74.

The two opposite-parity forced-`EF+/-` cells are complete too: their 17-term
systems again finish with the forbidden equation `e=0` after 435 S-pairs in
both components.  Only two forced-loop `S1` cells remain in common sign row
`(1,1)`, and the accepted frontier is 72.

The two forced-loop `S1` cells in common sign row `(1,1)` are now complete
as well.  The forced equation `-d^2=m` is handled over the genuine quadratic
extension `theta^2=-m` of each cubic common component; nonsquareness of
`-m` is checked in both.  Each parity gives three 17-term equations.  Their
exact tower-field bases contain `1` after 57 S-pairs for `delta=-1` and 55
for `delta=+1`.  All ten `S1` cells in the representative row are therefore
empty, and the accepted frontier is 70.  Do not request another `(1,1)`
`S1` computation.  The next useful task is a proof of common-sign transport
or a separately pinned cell in another row; `S0` and `S2` also remain live.

Common-sign product transport is now PROVED, so no `S1` computation in any
of the four common rows should be requested.  Exact component reduction
shows that the reconstructed `c` and `m` coefficient triples are identical
in all eight row/component pairs.  The rational and forced-loop `S1`
systems are therefore coefficient-identical to the ten representative-row
systems.  All forty `S1` cells are empty and the accepted frontier is 40,
consisting of six `S0` and four `S2` cells per row.  This retirement applies
only to product invariance; source-root, `q`, and interpolation tasks are not
transported.

The forced-colored `S2` cell is also retired in every common sign row.
Forcing `sigma*cd=m` produces three seven-term equations; both cubic
components reach the raw unit ideal after seven S-pairs.  The forced sign
disappears and the all-row common-product identity transports the result.
Do not request this cell.  The accepted frontier is 36: six `S0` and three
`S2` cells per row.

The forced-`EF` `S2` cell is retired in every common row as well.  Its
denominator-cleared equations have seven terms and complete after 28
S-pairs with `e^2=0` in both cubic components.  This contradicts the
required nonzero outside representative, so it is a guard-saturated
deletion rather than a raw unit ideal.  The accepted frontier is 32: six
`S0` and two `S2` cells per row.

The forced-`DF` `S2` cell is retired in every common row.  Its three
seven-term equations complete after 28 S-pairs with both `d^2=0` and
`e^2=0` in each cubic component, contradicting the forced denominator guard
`d!=0`.  This is guard-saturated, not raw-unit.  The accepted frontier is
28: six `S0` and one forced-loop `S2` cell per row.

The forced-loop `S2` cell is retired in every common row, completing the
`S2` product close.  Once `-e^2=m` is forced, all six residual products form
three signed pairs, so no quadratic extension is needed.  The three
seven-term equations reach the raw unit ideal after seven S-pairs in both
cubic components.  Do not request any `S2` product cell.  The accepted
frontier is 24, all six `S0` cells in each common row.

Both forced-colored `S0` parity cells are retired in every common row.
Their three equations have eleven terms and reach the raw unit ideal after
29 S-pairs for both parities and both cubic components.  The accepted
frontier is 16: two forced-`EF` and two forced-internal `S0` cells per row.

Both forced-`EF` `S0` parity cells are retired in every common row.  Their
denominator-cleared twelve-term equations complete after 190 S-pairs with
`e^2=0` in all four parity/component runs, contradicting `e!=0`.  The
accepted frontier is eight: only two forced-internal parity cells per row.

Both forced-internal `S0` parity cells are retired in every common row.
Their fourteen-term equations complete after 406 S-pairs with `f=0` in all
four parity/component runs, contradicting the nonzero outside guard.  This
closes all `24+40+16=80` invariant-product cells for common orbit
`[9,10,12,13]`.  Do not request another product, q-placement, or
interpolation task for this orbit; determine the next live common orbit.

One local pilot has already been attempted and must not be interpreted as a
survivor.  It used common signs `(+,+)`, `S1` signs
`(alpha,beta,gamma,delta)=(1,-1,-1,1)`, forced `DE=m`, and residual pairs

```text
(CE,DF),       (CF,-EF),       (DD,EF).
```

The six common basis equations plus four outside equations reached the
60-second `ramguard tiny` cap before producing a Groebner basis.  No local
or Modal fleet is authorized.

An external run should shard one symmetry-reduced
`(common-sign row, signed skeleton cell, forced edge, residual matching)`
per task.  Every task must:

1. print its identifiers and equation degrees before elimination;
2. enforce a declared wall and memory cap and emit deterministic partial
   status on timeout;
3. return a compact unit-ideal certificate, or a guarded survivor ideal with
   dimension, basis, and all denominator/distinctness norms;
4. keep product-level survivors separate from outside sum and full
   interpolation claims; and
5. include an independently replayable reduction or multiplication-matrix
   audit before any DAG node is promoted.

Prefer a CAS with efficient finite-field quotient and elimination support
over generic SymPy Groebner.  A pilot should use one task only; estimate its
cost from that result before requesting parallel capacity.

## CR-KB-POS3-SAT: positive three-loop parametric saturation

**Status:** deferred theorem/algorithm and donated-compute request.  It is
not authorized for local or Modal execution.  The local exact compilers and
small-field pilots are complete; a raw point search is not requested.

**Target:** the eight signed lanes under the open critical node
`rate_half_band_closure`, specifically positive coordinate parity in the
residual KoalaBear `(m,r,delta)=(2,4,2)` row.

**Pinned inputs:**

- `rate_half_kb_m2_r4_coordinate_positive_three_loop_common_placement_atlas`:
  four loop-placement residuals `R_442,L`, `R_442,H`, `R_433,L`,
  `R_433,H`;
- `rate_half_kb_m2_r4_coordinate_positive_three_loop_signed_outside_vieta_atlas`:
  two cycle signs and seven target records per placement;
- `rate_half_kb_m2_r4_coordinate_positive_three_loop_outside_edge_eliminant_compiler`:
  the 22-term generic edge resultant and exact linear-product degree drop;
- `experiments/prize_resolution/rate_half_kb_positive_three_loop_fixed_kernel_groebner_probe.py`:
  four deterministic `F_17` algebraic-closure fixtures.  Seven of eight raw
  full ideals are units; the eighth has basis
  `d^2-4,e+1,f+1` and becomes a unit after target-collision saturation.

**Requested sharding:** one task for each
`(442/433, root-low/root-high, cycle sign)` lane.  Do not combine lanes in a
single basis computation.

For one lane, a worker should:

1. construct a primitive common-kernel vector from the `4 x 4` matrix
   cofactors and impose the corresponding common residual;
2. substitute that vector into the six noncycle edge eliminants, then append
   the selected cycle-sign eliminant;
3. split or saturate the generic `A!=0`, linear `A=0,B!=0`, and impossible
   constant branches without dividing away a degree drop;
4. saturate by `beta`, leading support at all five common labels, the common
   source-label differences, all six target-square differences, every
   outside/common root difference, and pairwise outside-root differences;
5. return either an exact unit-ideal/Nullstellensatz certificate or a
   positive-dimensional/zero-dimensional survivor basis with every guard
   norm and an original-row back-substitution witness.

**Acceptance standard:** a modular unit basis alone is route evidence, not a
theorem.  Promotion requires either an exact rational/integer certificate or
a modular reconstruction with independently replayed characteristic and
denominator bounds covering the official field.  A survivor must include
the seven guarded quotient roots, not only seven vanishing scalar
resultants.

**Pilot and cost gate:** first run exactly one 433 lane, because three of the
four fixed fixtures die before the cycle edge and this is the best candidate
for a short certificate.  Print input term counts, maximum basis size,
peak memory, wall time, and certificate size.  Estimate all eight tasks from
that pilot before parallel launch.  If the pilot exceeds its declared cap,
return the partial basis and do not retry at a larger cap without maintainer
approval.

## CR-KB-POS433-QPAIR: positive 433-1a quadratic outside-product systems

**Status:** deferred algorithm/certificate request.  Do not launch a raw
case fleet.  The exact interface is proved locally, but two representations
of one aligned case already exhausted 130-second and 180-second caps.

**Target:** the positive `433-1a -> O0b` route under
`rate_half_band_closure`.

**Pinned inputs:**

- the common-kernel uniqueness theorem and its full `A_2,A_0,B_1` vector;
- the quadratic paired-product resultant interface, including the separate
  `eta` and missing-mate `xi` choices;
- the seven-record outside-edge eliminant compiler, including generic,
  linear, and impossible-constant degree branches;
- the two signed `O0b` target lanes;
- the exact fifteen-cell common Vieta atlas and four pivot charts.

Each common row and cycle sign has a formal `5*7*15=525` outside-product
ledger.  This is not the requested shard count.  The residual target-sign
quotient is now exact: after the signed-edge gauge, the faithful stabilizer
has order two (`d -> -d`) and gives 39 aligned plus 228 near-aligned formal
orbits per common row and cycle sign.  The sealed certificate prints all
267 representatives.  The `EF` missing-mate subledger has 39 orbits; the
current A/B templates are gauge partners and cover five.  A subsequent
exact target-monomial calculation supersedes the proposed 34-template
fleet: all 267 representatives are relabelings of one universal system with
four necessary-and-sufficient product binomials, seven cleared squared-sum
equations, and explicit reconstruction of `d,e,f`.  Duplicate-role and
common-root-sign quotients are not yet composed.

A useful contribution should substitute this universal target compiler in
the guarded common-curve coordinate rings and quotient the resulting source
systems.  Do not derive more target-specific triangle templates.

For one canonical representative:

1. substitute the missing-mate product and squared-sum equations before
   elimination;
2. impose the three quadratic resultants without introducing source-root
   variables unless the resultant survivor must be lifted;
3. append at least one of the six remaining outside sum rows before running
   a standard basis;
4. saturate all common/outside leading-support, source-label, target-pair,
   and denominator guards;
5. return a replayable unit certificate or a guarded lifted survivor with
   all twelve original product/sum rows checked.

**Known pilot boundary:** direct source-pair variables timed out after 130
seconds in Modal run `ap-E6pJY7vJcqMmRTbdjiXkQ9`.  Three reduced quadratic
resultants exhausted the 180-second function cap in
`ap-ZAFf2iYtIe9hzMCa6lMD0g`.  These are failed algorithms, not survivors.
The exact `F_29` aligned probe with the missing-mate sum retains only 8
common points and 16 target triples in role cell `5`, cycle `+1`
(`ap-zH5YzdeJ1cG4hfyK6Q9eTJ`); this prioritizes but does not delete cells.
The near-aligned probe retains 32 common points and 64 target triples in
cells `4/-`, `5/+`, and `12/-` at `F_29`, while `F_13/F_17` are empty
(`ap-3u9hr5P3djUL4LhW10TZHm`, `ap-WmRDAbdJ2aYTgHG83lIHP8`,
`ap-k9y0M76KmbUE4qf16AhLNz`).  These also prioritize rather than delete.
Complete squared-sum `F_29` replays then delete every aligned and near-
aligned relaxation survivor (`ap-8dCdvjclUG5u1lmLxpkQGM`,
`ap-TabMc9Ck6pc6dVnLk4h6kY`).  Do not request more small-prime sweeps; the
open task is a deployed-field symbolic certificate for the lifted systems.

**Cost gate:** estimate the symmetry-reduced orbit count and run one case
with basis-size, peak-memory, wall-time, and partial-basis telemetry.  Do
not fan out unless that pilot has a plausible total budget and improves on
the known timeout.  Exact sparse elimination, triangular decomposition, or
finite-algebra methods are preferred over generic lexicographic Groebner.

### 2026-08-01 target-free refinement

The surviving `F_29` cell-5/cycle-`+1` lifts use two matching templates.
For both templates the target representatives `d,e,f` now eliminate
exactly.  The first version listed three necessary product-chain equations;
an exact lattice audit added the missing independent cross relation, so the
repaired chain has four product equations and one compact squared-sum cut in
the common rational maps `F,H` and source deck labels `u,v,w`.  See
`rate_half_kb_m2_r4_coordinate_positive_433_1a_triangle_target_elimination_compiler`.
The finite-field observation does not prove these two templates exhaustive.

The deployed-field cell-5 common chart is not finite: after exact guard
localization it has dimension one and a 23-element degree-order standard
basis (`ap-3NNIpulALnODMHqWkGTzM3`).  Direct expansion of either compact
target-free cut timed out (`ap-hiw5WgQAWd21qUlGGxugnw`), and an unsaturated
ambient seven-variable type-A standard basis hit 120 seconds
(`ap-5LekROrgmIeQwn2fIpVvVy`).

A useful contributed run should therefore:

1. ingest or reconstruct the 23-element localized common-curve basis;
2. compute a function-field, regular-chain, or quotient-ring presentation
   of that curve without expanding the target-free cuts ambiently;
3. reduce the four product-chain equations first, then append the single
   compact sum cut;
4. saturate source-pair distinctness and leading support only after the
   reduced system is zero-dimensional;
5. return a replayable unit certificate or a guarded original-row witness.

Do not rerun the ambient `dp` basis at a larger cap and do not fan out over
the 267 formal symmetry representatives.  The target exponent lattice is
already complete and universal; work on common-curve/source-system
quotients instead.

### 2026-08-01 signed-family regular-chain request

The PROVED cell-5 signed-family interface now eliminates the target roots
exactly.  For `DE+/DE-/BE` it gives four target-free unsquared equations in
three source roots; `DF+/DF-/CF` is identical with `b` replaced by `c`.
Exact relaxed probes found no independent seven-record Vieta completion
among 368 `F_17` or 1,072 `F_29` common survivors
(`ap-kFi1MWruL9asXhwnUqi5US`, `ap-oEfa1ita3OEaMxXD5yKsxH`).

The corrected saturated common quotient has dimension six and basis size
twelve after adjoining three source roots and two target roots.  In that
quotient the six original unsquared generators are sparse: each product row
has degree 15 and 96 terms, and each sum row degree 18 and 240 terms.  A
quotient-compatible generic `std` still exhausted 190 seconds
(`ap-uG1IwuZNXrj32LwEaDaO5b`).  The manually target-free presentation is
worse: cut sizes are 769, 78,105, 43,634, and 58,964 terms
(`ap-XvpdSEjqpJgkteo3AudUPb`).
The `BE` endpoint polynomial now factors exactly as a guarded unit times
`(z-t)R_b(z)` with `degree_z R_b=3`, total degree 14, and 120 terms.  The
known root `z=t` is forbidden for the outside edge.  Replacing the colored
product row by `R_b` did not make the combined generic basis finish
(`ap-OEAvKJxyhQn0ulMiNUF8Yq`), so use the cubic only after signed-pair
decomposition.
The signed pair by itself has common-quotient dimension five, basis size
twelve, and only four 96/240-term generators, yet generic `std` still timed
out (`ap-cGvpVPiwsv1wiGLv3z4FHK`).  This rules out “drop the colored row and
retry the same algorithm” as the requested contribution.

Requested contribution:

1. ingest the saturated projected common ideal, not the unsaturated
   three-minor ideal;
2. triangularize only the signed `DE+`,`DE-` pair first, preferably by a
   regular chain, subresultant sequence, or factor-by-factor norm;
3. report dimensions and guard norms for every component before appending
   `BE`;
4. append the colored edge only to surviving signed-pair components, then
   saturate `Delta D_0D_1D_2`, source collisions, and common/outside labels;
5. return a unit certificate or an original unsquared-row witness;
6. repeat for the `DF` family only if the first family survives.

Do not increase the generic standard-basis cap, run both families in
parallel, expand the four target-free cuts ambiently, or fan out over the
267 matching representatives.  The desired output is a component ledger,
not a longer timeout.

### 2026-08-01 finite-algebra refinement

The common compiler now accepts an explicit `(prime,iota)` and recomputes
all modular normalization at that prime.  This repairs an invalid discovery
shortcut that reduced polynomials already made monic modulo the deployed
prime.  The only banked small-field results below use a genuine square root
of `-1` in the probe field.

At `p=65521`, `iota=24297`, the saturated generic cell-5 fiber over
`F_p(t)` has dimension zero, basis size six, vector dimension four, and one
minimal component (`ap-9rQUOuge1TNoa1ufF3u9MR`).  FGLM gives a three-element
lex basis whose primitive `b` polynomial is a reciprocal quartic.  Direct
coefficient reversal and the lifted substitution `u=b+b^{-1}` independently
verify its descent to a quadratic (`ap-KCxeFPbJGAalI2aKR9nxem`).

After eliminating `r,c`, the signed `DE+`,`DE-` pair is one reciprocal
quartic plus four cuts of `(degree,terms)=(9,24),(8,32),(9,24),(8,32)`.
A four-minute `slimgb` pilot still timed out
(`ap-F0mNsrUqkAmnr1ADk2V20i`).  Do not rerun that basis with a larger cap.
Ordinary deployed block elimination subsequently produced the exact 19-term
reciprocal quartic and trace quadratic
(`ap-D4GXYWOVhTEiEfabnKO9Ht`), now banked as a PROVED child.  A second exact
run (`ap-3hVthJkmosYTdYTQ4Kc91v`) gives one guard-unit `r` formula and four
`c` charts; their simultaneous exceptional cubic has no deployed-field
root.  Compute the signed cuts separately on those four rational charts.
Only then append the residual `BE` cubic and sum row.

Singular 4.3.1 cannot lift this function-field workflow directly to the
deployed characteristic: its backend rejects characteristics above `2^29`
after the 12-element affine basis is computed
(`ap-JwQiY0HAW4TvF01vmVmtPj`).  A contributed implementation must use a
different exact finite-algebra backend or symbolic identities checked in the
deployed polynomial ring.  The `F_65521` result is evidence and a shape
compiler, not a deployed-field theorem.

### 2026-08-01 deployed colored-chart backend fence

Do not expand the target-free square cut at the deployed prime.  The
factored Singular assignment enters a backend capped at `2^29`; the Python
route expands other cuts to 58,964 terms before any basis step
(`ap-WHPxRTl9RMJGjEtD328bNO`).

The equivalent unsquared system with explicit `d,e` compiles cleanly with
signed-equation term counts `96,240,96,240,120,240` and a nine-term chart
guard (`ap-ixMbNHMyuEwVxEDbYXAUsT`).  Chart 2 nevertheless timed out after
240 seconds (`ap-UcfpDVxgnQOjNOoqELThke`); do not fan this basis to the other
three charts.  Algebraically eliminating `d` lowers the `DE+/DE-` ledger to
`769,4502,240` terms, but Singular rejects the deployed cubic-edge resultant
(`ap-EnuadAiVWmVBrNOExVkFDX`).

The next implementation should reuse the already-PROVED 22-term
quadratic-quartic edge norm.  Encode its coefficient definitions and norm as
a sparse auxiliary-variable circuit, or compute the one low-degree
resultant in a backend that supports `p=2130706433`.  Do not request a longer
generic basis.

The sparse norm circuit has now been implemented.  Its deployed chart-2
ledger has common equations `19,19,24` terms, reconstructed signed-pair
equations `769,4502,240`, and colored norm definitions bounded by 757 terms
with final pseudo-remainder/norm equations of `6,7,3` terms
(`ap-UygmUkG2dtvijTgXIIx5Xs`).  The combined circuit still timed out at 240
seconds (`ap-RMLTMaMIIjpqLWjEKaJ4ps`).  This localizes the next task: remove
the colored circuit again, triangularize the `769/4502/240` signed pair over
the rank-four reciprocal algebra, and append the colored norm only to its
component ledger.  Do not parallelize the same combined basis over charts
3--5.

The pair arithmetic circuit is smaller still: its six evaluation definitions
have at most 97 terms, its three signed-pair equations have `2,4,5` terms,
and its chart guard has nine terms (`ap-39oTPQR9XZaltpf0xAuYX8`).  Removing
all unused colored variables does not make either the elimination-block or
total-degree Singular basis finish at 240 seconds
(`ap-gysnK6QVGTEyVrlr64Rt7T`, `ap-9StDk2Yi93vpdKOnsgEft7`).

A direct SymPy implementation over `GF(2130706433)(t)` correctly detects the
rank-four primitive and denominator gcd certificates; SymPy's `invert` has a
false zero-divisor failure on the quadratic `c` denominator, repaired by
explicit `gcdex`.  Even with monomial-by-monomial degree-four reduction, the
six common coefficients do not finish within the five-minute wrapper
(`ap-xEl0f94ZLQjaPWCxVelMaE`, `ap-KVgOXwaAAJCZ3oNWUuC5Sf`).  Do not retry
this SymPy coefficient engine unchanged.  The requested computation is now
precise: implement the same four-generator system over
`GF(p)(t)[b]/(P)` in Nemo/FLINT/Magma (or another efficient rational-function
backend), return the signed-pair regular-chain/component ledger, and only
then append the compact colored norm.

### 2026-08-01 signed-pair stable-rank completion and revised request

The generic four-generator backend request above is now superseded.  The
Nemo/Groebner.jl route computes the exact chart-2 squared `DE+/DE-` quotient
over `F_2130706433(t)`: an 18-element Groebner basis gives vector dimension
64.  If `M` is multiplication by `g=d0*d1`, exact rational certificates give

```text
rank(M^2)=rank(M^3)=24,
dim A[g^-1]=24.
```

The upper bound is a checked factorization of all 64 columns through the
first 24 columns of `M^2`; the lower bound is the nonzero top-left minor at
the regular fiber `t=2`.  An independent checker clears denominators and
verifies all 5,160 polynomial identities with a 512-point NTT, above their
maximum degree 380.  A hostile audit rejects three certificate mutations.

Authoritative Modal apps, all stopped after bounded runs:

```text
ap-iL0NlhcML6PNSbeivvlEzy   M^2 normal forms
ap-EYSaER3gP4AUY24qgSBR9R   one-column retry
ap-8fGTO2L3xlaWIjHUftJLn3   exact structured rank factorization
ap-oXrrTGaRKqCJ4dWcE3nwht   cleared-denominator certificate
```

The revised contributed-compute request is not another standard basis.
Starting from the hash-pinned length-24 localized algebra:

1. determine its radical and residue-field factorization over `F_p(t)`;
2. certify nilpotent multiplicities if it is not reduced;
3. compute the finite exceptional-`t` discriminant and denominator locus;
4. restore the source-root square, nonzero, and distinctness guards on each
   surviving factor;
5. evaluate the compact colored `BE` norm factor by factor.

Return exact factor polynomials, guard norms, and independently replayable
certificates.  Do not call the length 24 a component count, sample only
special fibers, retry the failed generic basis, or append the colored norm
before the residue ledger is known.

### 2026-08-01 signed-pair generic-reducedness completion

The radical part of the revised request is now complete.  On the certified
24-dimensional stable image, exact multiplication by
`ell=x1+2*x0+3*b` was computed in all 24 columns and checked in all 64
ambient quotient rows.  At the regular fiber `t=2`, the first coordinate
vector is cyclic and the degree-24 minimal polynomial has derivative gcd
one.  Consequently `ell` is generically primitive and the localized algebra
is reduced over `F_2130706433(t)`.

The full two-column campaign completed ten shards and returned explicit
timeouts for columns 13--14 and 19--20 in
`ap-JbaRjWcp7CtiDT2nqnl8Sp`.  Exact one-column/matrix-method retries completed
the missing coverage in `ap-uAXb13GnCsiaM4LEhf3NLU`,
`ap-AfNdHRICf9Pb3bWsGVV0u0`, and
`ap-wn8HRH4Q7HLq0JKnI1RhbJ`.  All apps are stopped.

The new contributor request begins after radical computation:

1. compute the exact degree-24 characteristic/minimal polynomial of `ell`
   over `F_p(t)`;
2. factor it and report exact residue degrees and factor polynomials;
3. compute its discriminant and all source/denominator guard norms;
4. apply the residual colored `BE` product and unsquared sum on those
   factors.

Do not rerun radical algorithms or infer 24 components from degree 24.

### 2026-08-01 signed-pair primitive residue completion

The primitive polynomial and generic factor ledger are now complete.  Exact
Krylov elimination in `ap-oyB5HrYYmeguXMKmqODnsw` gives the monic degree-24
polynomial for `ell=x1+2*x0+3*b`; exact Nemo factorization in
`ap-yP081HXaVybgPvzsNW5FUX` gives irreducible degrees

```text
4,4,4,8,4
```

with every multiplicity one.  A standard-library checker reconstructs the
full rational-function product exactly and checks a regular pairwise-coprime
squarefree fiber.  SymPy 1.14 was tested as a second factor backend, but its
finite-field fraction-field conversion fails and multivariate finite-field
factorization is unimplemented; that failed audit is not evidence.

The revised contributor request starts in the five residue fields:

1. express the required source-square, collision, chart, and colored
   invariants as polynomials in `ell` modulo each factor;
2. compute exact guard norms and the finite exceptional-`t` locus;
3. evaluate the residual colored `BE` cubic and unsquared sum factor by
   factor;
4. return unit gcds/norms or exact surviving residue factors.

Do not recompute the pair quotient, stable rank, radical, primitive
polynomial, or factorization.

### 2026-08-02 signed-pair primitive coordinate completion

The first item in the residue-ledger request is complete.  Exact multiplication
columns for `x1,x0,b` were computed in `ap-9TDK6ccFWgwFvBjLsIIkwb`.
Three independent exact Krylov solves in
`ap-oJCcerqPq6wNwVNLasPkSx` express every variable as a degree-below-24
polynomial in `s=ell`.  A combined three-right-hand-side attempt
`ap-HpMM8Cb1LRiDU6cIvMUx0r` timed out and supplies no claim.  All apps are
stopped.

The exact map packet is
`001c959648176669651c87a913f2c830ad425a4f1e240041cc4edeb63d69a009`;
the coordinate-column packet is
`f5bfdb6cb515b6bbe54fa1abd19d1517759b0a584f501aa308e76f68e1ff1e25`.
The independent checker verifies `p_x1+2*p_x0+3*p_b=s` coefficientwise and
replays all three actions at `t=2`.

Requested next computation:

1. translate the already-defined source nonzero, collision, square, and chart
   guards into `s` with these maps;
2. reduce them modulo each exact primitive factor of degrees `4,4,4,8,4`;
3. compute exact resultants/norms over `F_2130706433(t)`;
4. distinguish an identically zero component from a nonzero norm with a finite
   exceptional-`t` locus;
5. append the compact colored `BE` condition only after this guard ledger.

Do not recompute the stable basis, primitive polynomial, factorization, or
coordinate maps.  Do not infer a source-root lift or component deletion from
the squared coordinate formulas alone.

### 2026-08-02 generic guard-unit completion

Whole-component guard degeneration is now excluded without a remote run.
At the exact regular fiber `t=2`, the five primitive factors, exact
`b,x0,x1` maps, and chart-2 `r,c` lift give 150 nonzero remainders:
22 declared common-chart guards and eight necessary squared
outside-incidence guards on each factor.  The canonical ledger hash is
`a48d3a028d422b19edda8d6ecac1f663bf2710fbc491a492b660b6b6e264bcb6`.
Therefore all 30 elements are units over `F_p(t)` in every residue field.

This does not print their rational norms or classify the finite
exceptional-`t` zeros.  The preferred next route-deciding computation is
the generic colored `BE` restriction on all five fields, with exceptional
guard-norm fibers kept as a separate ledger.  Do not spend a broad campaign
computing all 30 norms unless the colored restriction survives generically.

### 2026-08-02 cell-5 generic colored-gcd bounded campaign

**Decision.**  On each of the five proved primitive residue fields

```text
E_j=F_2130706433(t)[s]/(phi_j),   deg phi_j in {4,4,4,8,4},
```

compute the exact gcd in `E_j[e]` of the DE+ signed-pair necessary
polynomial and the compact colored `BE` necessary eliminant.  Then divide
that gcd by its gcd with the target-collision guard `e^2-1`.  This is the
route-deciding generic colored restriction requested in the preceding
ledger entry.  The upstream interface is the exact second-moment / primitive
shift-pair lane; exceptional `t` fibers and all other matching cells remain
outside the campaign.

**Completeness and parameters.**  The proved primitive factorization gives
exactly five factors and the proved coordinate maps express `x1,x0,b` in
each one.  The proved chart-2 atlas reconstructs `r,c`; the proved outside
edge compiler supplies the DE+/BE necessary equations.  The launch covers
factors `1,2,3,4,5` independently, with no sample-prime or sample-`t`
substitution in the primary computation.

**Source and command.**  Source commit is the current Codex worktree until
banked.  Launcher:

```text
tools/ramguard modal -- modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd_modal.py \
  --factors 1,2,3,4,5 \
  --output experiments/prize_resolution/rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd_result.json
```

**Ceiling and partial-output contract.**  At most five parallel containers,
one CPU and 8 GiB RAM per container, a 270-second Julia subprocess cap, and
a 300-second Modal function cap.  Conservative total wall time is five
minutes and conservative requested-resource cost is below `$1`.  Each shard
returns `COMPLETE`, `TIMEOUT`, or `ERROR` with elapsed time, provenance
hashes, program hash, and bounded stdout/stderr.  Completed factors remain
usable if another shard times out; incomplete output is evidence only and
changes no status.  The app is stopped after the bounded campaign.

**Certificate.**  Every complete shard returns the exact pair and colored
polynomials, their monic gcd, Bezout multipliers, the collision-guard part,
and the quotient outside that guard as rational functions in `t` and `s`.
The deterministic local checker
`check_rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd.py`
validates provenance and independently replays the Bezout, gcd, guard, and
quotient identities on every irreducible finite subfactor at the regular
fiber `t=2`.  A generic theorem still requires an independent exact audit;
the regular-fiber replay alone is not used to promote a node.

**Effects.**  PASS means every outside quotient is constant and authorizes
an exact generic colored-incompatibility theorem after the independent audit.
FAIL with a positive outside degree returns an exact surviving generic
factor and redirects the attack to that component.  INCOMPLETE has no DAG
effect.  Compact results are stored at the output path above; raw artifacts
remain in Modal and are identified by the app ID and program hashes.

The one-factor setup validation app `ap-pmWZTeSBvdQXSwTDiBctqD` stopped
before Julia was launched because the remote Python image omitted SymPy,
which regenerates the six pinned sparse-kernel expressions.  It produced no
mathematical result.  The launcher now pins `sympy==1.14.0`; the Nemo image
layer completed and is cached.

The corrected bounded campaign completed in apps
`ap-jcIuGHdW1WxLKephFQDv0O` (factor 1) and
`ap-IKaYuOEIwen2OhFi6ccFhg` (factors 2--5); both apps stopped normally.
Exact function times were respectively `24.33` seconds and
`16.35,24.01,233.42,20.45` seconds.  The four quartic factors have monic
gcd exactly `e^2-1`; the octic factor has gcd `1`.  Thus every quotient
outside the collision guard has degree zero.  The compact five-factor packet
has SHA-256
`710b438062fc2e80f5c7b14ffb987d8f36a02d4b57953b30419bb320b88877a7`.

The deterministic checker passes all five shards and every irreducible
finite subfactor at `t=2`, including the returned Bezout identities.  This
completes the bounded campaign but does not yet promote a theorem: an
independent exact audit must reconstruct the DE+/BE polynomials and verify
the generic identities before the result enters the DAG.

**Registered exact audit.**  At source commit `e774c74a`, run the independent
packet parser
`rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd_audit_modal.py`
on factors `1..5`.  It does not invoke the primary gcd routine: it rebuilds
each `phi_j`, parses every rational-function coefficient independently, and
checks the returned Bezout identity and exact common factor in
`F_p(t)[s]/(phi_j)[e]`.  Five one-CPU/4-GiB shards have 150-second subprocess
and 180-second function caps; conservative campaign time is three minutes
and cost is below `$1`.  Each shard returns explicit `COMPLETE`, `TIMEOUT`,
or `ERROR` telemetry and a program hash; partial output has no status effect.
The local audit script regenerates every program hash and checks all markers.
PASS completes the generic certificate audit but still leaves exceptional
`t` fibers and source-equation provenance as the stated boundaries.

The audit completed in apps `ap-cpk6ggojSG2qXUsMmJ8BP4` (factor 1) and
`ap-JDaA7cgwB2vcKgfWVNJzvG` (factors 2--5); both stopped normally.  Exact
function times were `9.26` seconds and `7.92,9.60,13.85,7.96` seconds.
All five exact generic identities pass.  The audit packet has SHA-256
`e1651bf40f716eeef1daafab71b0f0b49a010d2d38395aa6ecde1d3e82b7bb81`,
and its local hash/marker checker passes.  This pays the generic Bezout
certificate audit; it does not classify exceptional `t` fibers.

### 2026-08-02 cell-14 linear-pair exact census

**Decision and authorization.**  The user renewed the monthly Modal credit
and explicitly authorized valuable numerical experiments.  The campaign
tests the route-deciding cell-14 subfamily in which a `de` record is missing
and the two residual `de` records are paired.  All arithmetic is exact over
`F_2130706433`; no sampled-prime inference is used.  The campaign exceeded
the protocol's default five-minute aggregate window under that explicit
authorization, but retained per-task hard caps, at most 32 containers, and a
conservative cost below `$3`.

**Completeness router.**  The signed atlas gives four source signs, four
target lanes, seven missing outside records, and fifteen perfect matchings.
The selected subfamily is the exact Cartesian product of 4 source signs,
4 lanes, 3 missing `de` records, and 3 residual-`de` matchings: 144 logical
cases.  Quadratic-pair reduction gives one target-free linear equation.  Its
open resultant and every irreducible factor of the common-coefficient
boundary are checked separately.

**Execution.**  Final apps were `ap-L0KpNyaoVMYhGpecdOKI2R` (48 pairing-0
complete cases), `ap-vElucfytu5kl97fbXEr2lp` (96 open projections),
`ap-tXKscerl0pr5s0NY8Wx2Sn` (768 role-0/1 boundaries), and
`ap-1LVqOLunDONjPiKM5zLStF` (320 role-2 boundaries).  One role-2 factor
timed out in the parallel launch.  Isolated replay
`ap-wNUhANWcKOGTQbuK1NAwkQ` used identical definition and program hashes and
completed unit.  Every app stopped normally.

**Certificate and effect.**  The compact aggregate has 144 open and 1632
boundary unit ideals, with explicit Cartesian coverage, source/result hashes,
factor profiles, and timeout-replay custody.  The independent audit checks
the matching enumeration, two boundary profiles, exact missing-role identity,
and hostile count mutations.  PASS promotes only
`rate_half_kb_m2_r4_coordinate_positive_433_1b_cell14_linear_pair_outside_exclusion`;
1536 raw cell-14 outside cases remain open.

### 2026-08-06 XR fiber-rigidity boundary fixture

**Decision.**  Test the proposed field-independent `(FR)` mechanism for
`xr_band_forced_commonroot_syzygy_count` on one exact smooth boundary
fixture.  The construction has `q=193`, `n=64`, `k=4`, `d=13`, `h=18`,
`ell=2`, and `r=h-d=2ell+1=5`.  The remote task exhausts all
`C(64,4)=635376` interpolation anchors and all 194 projective slopes, checks
the global tangent ceiling, and applies the normative lexicographic
first-match selector.

**Scope.**  PASS with split selected blocks falsifies only the broad
field-independent/THEOREM-R-style reading of `(FR)`.  It does not falsify an
official-row conjecture restricted to the first unpaid affine dimensions or
post-envelope profiles.  The preregistration and full adjudication are in
`notes/pilots_20260804/fiber_rigidity/`.

**Execution.**  The packaging-only app
`ap-3mwM41d1SzL3tjsBGyEZoG` failed before mathematical work began and was
stopped.  Primary app `ap-z6h81Tc1oAr9HAKqIdbkxZ` completed and stopped
normally.  It exhausted all 635,376 anchors, retained 631,833 canonical
codeword pairs, found global maximum 22, exactly two live slopes, and
`L_P=2`; both selected blocks have profile `(2,1,1,1)`.  Certificate SHA-256
is
`91248465187ab72abd9cbb4e9debe6e0feef9e52d26afed7fb568a0826680ec2`.

Independent-audit app `ap-wQGFHF5dPs7XXgZEBMq9cC` completed and stopped
normally.  Its checker imports no constructor code, rebuilds all structural
algebra, repeats the complete anchor/slope scan, agrees on all per-slope
maxima and first-match supports, and rejects twelve hostile mutations.

```text
XR_FIBER_RIGIDITY_BOUNDARY_COUNTEREXAMPLE_PASS seed=20260806 subsets=635376 canonical_pairs=631833 live=2 Lp=2 profiles=2,1,1,1/2,1,1,1
XR_FIBER_RIGIDITY_INDEPENDENT_AUDIT_PASS full_scan=true mutations=12
```

**Effect.**  The broad mechanism is refuted, while the official
post-envelope `(FR)` remains open.  No DAG status or edge changes.  A repaired
statement must use an explicit official-subgroup, high-affine, or
post-envelope hypothesis; local primitive equations alone are insufficient.

### 2026-08-07 K3 degree-12 checkpointed parity instantiation

**Decision.** Do not rerun the expanded degree `22`/`23` leading-curve
Gröbner routes. Two direct 780-second runs completed exact dimension-one seed
bases of sizes 25 and 27 but timed out after row reduction; a separate exact
pseudo-division run lowered both rows to `x`-degree five but grew them to
`23616` and `23484` terms before the final timeout. These endpoints are
fenced in the degree-12 decomposition node.

**Tested route.** Instantiate the PROVED parity identity

```text
V^d P(-U/V) =
  sum_j a_(2j) V^(d-j) Z^j
  - sum_j a_(2j+1) U V^(d-j-1) Z^j       mod U^2-VZ
```

for the two literal remaining rows before expanding `U,V,Z`. The bounded
metrics-only phase completed in app `ap-jVjceB5Npmz4Rm1xlGdJWm` in `51.64`
seconds at about `0.42 GB` peak child RSS. The direct rows have `52336` and
`49949` terms; the parity representatives still have `52257` and `49848`.
Their exact hashes are bound by the parity-identity verifier.

**Custody and ceiling.** The uncheckpointed prototype is
`degree12_parity_reduced_evaluation_probe_modal.py`. App
`ap-4QZZtNn47Q0jNj4rJCqIQA` was preempted twice around five minutes and then
aborted, producing no mathematical packet. A rerun is authorized only after
adding durable phase checkpoints. Use one four-CPU/16-GiB container, a
15-minute hard cap per phase, partial output on timeout, and a total requested
resource cost below `$1` for the representative. The representative does not
compress materially, so phase two and other-cell replay are not authorized.
Any successor must first exhibit a block-level factorization or syzygy while
`U,V,Z` remain unexpanded.

### 2026-08-08 positive 433-1b cell-4 matching-11 exact replay

**Decision.** Close the last live cell-4 matching-exchange orbit by exact
quadratic-resultant elimination and complete finite-field replay. The user
explicitly permits longer valuable Modal computations and renewed the monthly
credit. The primary compiler retained eight source-sign/colored-lane rows,
hard completion semantics, compact output, and a deterministic independent
checker. Total one-CPU cost remained below `$1`; no WSL-heavy computation was
used.

**Execution.** Compiler app `ap-KZ72bRFmoRTN8VNueSuzDK` completed all eight
rows. The first verifier app `ap-YnHNxRzPD9DpVJQrqp9SLP` exposed a stale
expected eliminant degree (`8` instead of the recorded exact degree `6`), not
a theorem failure. After repair, app `ap-hD8LPsYApvAxTnBAJS5d37` reached the
generic 270-second replay cap. The content-identical replay with a 600-second
remote-only cap, app `ap-74kOL7uM1Y7OHlIhM5mI1A`, passed in 372.41 seconds.
All apps stopped normally.

**Certificate and effect.** The complete root union has 60 candidate `r`
values, 16 guarded source points, eight compatible `(z,q)` candidates, and
16 nonzero final `Pair(-q,sigma_o ef)` evaluations, with no witness, target
boundary, free branch, or unresolved row. The independent verifier
recomputes all degree-3864/3868 norm roots and every source lift. This closes
matching 11 directly; exact transports pay matching 14 and both xi4 partners.
Separate disjoint-cover verifiers then close all 105 cell-4 labels and the
duplicate-role orbit `[4,7]`.

### 2026-08-08 positive 433-1b cell-12 elliptic common-locus campaign

**Decision.** Select a compact exact presentation for the next unclosed
duplicate-role orbit `[12,13]` before compiling any of its 105 outside
labels. Cell `12` is the representative: `BC-` is singleton and the source
matching is `(LA,AB),(AC,BC+)`. All expensive standard-basis work was sent
to Modal; only hash, JSON, and low-degree polynomial audits ran under local
`ramguard tiny`.

**Route selection.** The initial four-pivot chart found one-dimensional
common ideals for every pivot. Exact subset searches showed that no triple
of the eight lex rows generates the full guarded affine ideal, even after
route localization. Four specific quadruples become exact after additionally
inverting their leading coefficients. The failed exploratory birational
launcher had parser/syntax faults, produced no evidence, and was deleted.
The corrected pivot app was `ap-xjoaAlJ031oiZi6jcVczhf`; the unsaturated
subset app was `ap-BeB5FduQYUhe8wyHKYqfvf`; and the final exhaustive
leading-localized subset app was `ap-deMSQ71aFOEXmluIwPriXF`. These packets
are route-selection evidence only and promote no separate node.

**Complete structure.** App `ap-UGTRxHvSZteecD6UcEscYD` checked the selected
`AC` pivot in all four source-sign rows and all six product-cofactor charts:
all 24 runs completed with dimension one, compact basis size `15`, lex basis
size `8`, and unit pivot boundary. App `ap-Jc9a3zuxX9HLZwWOJMpaGx` proved the
exact leading-open presentation by a quadratic in `t`, a palindromic
quadratic in `b`, and a linear recovery of `c`; an alternate linear recovery
gave the same localized ideal. Removing the doubled route factor from each
base discriminant leaves a square-free quartic, hence a genus-one normalized
base.

**Boundary and kernel.** App `ap-J73jbPfsrEcJzlKzj4LCVU` classified all 12
leading fibers. Four split `b` fibers give exactly eight guarded deployed
points; eight quadratic `c` fibers have no deployed points. App
`ap-jKyXbePmY48WoHuLsDi9EZ` then produced one sign-independent primitive
eight-coordinate kernel. Seven common-row pairings vanish identically and
the remaining three reduce to zero on all four exact common ideals. The
independent local audit also checks all 80 row pairings at the eight boundary
points.

**Effect and spend.** The campaign promoted two small PROVED structural
nodes: the complete elliptic common-locus decomposition and its global
common kernel. It closes no outside label and does not close cell `12`.
Each final app used at most four 4-GiB containers for under five minutes;
the aggregate final-certificate cost is conservatively below `$1`. The next
authorized computation is a cheap 105-label structural router against the
fixed kernel, not a broad norm campaign.

**Rational-boundary outside closure.** The immediate finite follow-up ran in
primary app `ap-WZvIMr7B4J34FR0TsNOTqZ`. It covered the exact Cartesian
product of eight rational leading-boundary points, four target lanes, seven
missing records, and 15 residual matchings: 32 shards and 3,360 labels. The
missing product and squared sum give four target lifts for roles `0..4`;
the two endpoint roles fail a source-only compatibility equation. All shards
completed with zero witnesses and zero unresolved branches.

Independent app `ap-LI2VGTAZjNrxqXGCFpBcS5` reconstructed the lifts with a
separate Tonelli-Shanks implementation, computed each common pair-equation
factor through `gcd(G,y^p-y)`, and removed every target-guard factor. It also
completed all 3,360 labels, with zero free branches and total guarded root
degree zero. A transient Modal heartbeat warning did not affect the remote
tasks or final complete output; the app stopped normally. The combined cost
was well below `$1`. This promotes the complete deployed rational-boundary
exclusion, but pays no point on the generic elliptic chart.

**Generic endpoint-role closure.** Source-only pilot app
`ap-gCH6oQc1fW2VTAZcNiuDon` adjoined the necessary endpoint equation
`(u^2+m)^2-Su^2=0` to the generic common curve. All eight source-sign and
endpoint cases became zero-dimensional with one exact `r` eliminant.
Deployed-root replay app `ap-wOtqklCmNfzcLPWGf9r6tS` lifted every linear
`r` factor through the proved tower and retained exactly 16 `BF` source
points and 24 `sigma_c CF` source points. No retained point lay on a route
or leading boundary.

The first full residual launch, `ap-utANE9kl0WA64d8VFvhZJj`, exposed only an
output-parser defect and produced no mathematical packet. After repair,
one-case validation app `ap-zdnEev7PHNSTrbRgZT8tua` paid 60 of 60 systems.
Primary app `ap-jrMESwKeGzouPFEPhqMscX` then completed all 32 source/endpoint
and target-lane shards: 2,400 of 2,400 guarded bivariate ideals were unit.
Independent app `ap-33sFbnRJM7VZHWz9dAKmVU` rebuilt the systems in SymPy and
computed unrestricted lex bases; all 2,400 were again unit, with zero
witnesses, target boundaries, finite residual branches, or unresolved rows.
Every app stopped normally. Aggregate cost was well below `$1`.

Together with the prior rational-boundary theorem, this promotes a scoped
PROVED node closing both endpoint roles in cell `12`: 30 labels, or 12 of
the 36 generic label orbits. The remaining generic workload is 24 orbit
representatives covering 75 labels. No complete-cell or Prize claim follows.

**Parallel-`DE` first-pair closure.** A direct eight-case Gröbner scout,
app `ap-ktQn2vT3AeMkBlys9jk7wS`, timed out during rational simplification;
a denominator-cleared, three-relation one-case retry,
`ap-PLvdEvwn66TRIQmwJ4xIii`, also reached the five-minute cap. Neither app
produced mathematical evidence. The retained four-basis formulation instead
completed a validation in `ap-wl1LaLm9HAbluHk5R5YR5h`, all rows in
`ap-mQsdrJxZ9czCBxKWyh4H2W`, and the final deterministic exact-coefficient
packet in `ap-IJFw7P0QEymI25xOtUvIER`. The two target-free cuts have norm degrees 350
and 362 and only eight and seven deployed roots per source-sign lane.

Final direct replay app `ap-g44ta4GmDCL8N8V1NUvI4B` accounted for all 116
case-labeled norm and inverse candidates. The negative-`DE` cut has no
generic zero; the positive-`DE` cut has two per source-sign lane. An initial
residual census and independent audit, apps `ap-0CVpkHNEHafBi9p0ZtE3MU`
and `ap-lZUhVykRbSdgKPG2YucyTD`, exposed a missing compiler equation: using
only `de=m` admits false projected witnesses. Restoring the mandatory Vieta
equation `(d+e)^2=S` makes every guarded residual ideal unit. Final primary
app `ap-OPmO1UlkaIs9vAkfUEA3Zl` and independent reduced-variable audit app
`ap-XtMGYHQ33046N1viWrJobe` agree on 96 of 96 unit systems, with no witness
or unresolved branch.

This closes nine labels, or four more generic orbits. The cell-12 frontier
is now 20 representatives covering 66 labels. The squared-sum omission is a
hard fence for every future missing-record compiler. Retained work cost was
below `$1`; the two failed direct scouts were bounded and are not to be
relaunched.

**Reciprocal-role matching-0 closure.** The already proved cell-4
reciprocal-square compiler is 1,139 lines, so it was not copied. A pinned AST
adapter extracts its `evaluate_case` function unchanged and supplies the
cell-12 tower through a six-slot schema shim. Initial app
`ap-uEmPUxl7Mnx1ZsXSP3RVfl` found one `FREE_B` terminal; exact evaluation
showed that it lies on the cell-12 `b`-leading complement. The adapter now
routes only coefficient-zero `FREE_B/FREE_C` terminals to the proved boundary
theorem. Validation app `ap-MPpJc7ic8DzACr3qnqtl33` then completed exactly.

Full app `ap-mMiXtJUDca1GdAHTkPorqD` completed all 24 source-sign, rational
`q`-branch, and `sigma_o` rows. A transparent container preemption was
retried by Modal and did not affect the complete packet. The exact census
contains 340 candidate roots, 472 guarded source points, 48 common `y` rows,
96 `(y,d)` candidates, and 192 final `sigma_c` lane evaluations. Every final
pair is nonzero; there are no witnesses or unresolved rows. An independent
local audit reconstructs all 89 unique norm/inverse finite-root sets and
checks every one of the 24 leading-boundary transports.

This closes missing `DF`, matching `0`, and its exact `D/E` partner: two
labels or one generic orbit. Cell `12` now has 19 representatives and 64
labels open. Total incremental Modal cost was well below `$1`.

**Reciprocal-role matchings-1/2 closure.** The same pinned-AST strategy
reuses the audited cell-4 reciprocal-linear compiler for cell `12`. The
missing Vieta quartic in `z=1/d` and the matching-specific quadratic have a
linear remainder in the exact four-basis algebra. One-row adapter validation
app `ap-VHGJqSCvU83mITBwKamC3h` completed before the complete 36-row run.

Full app `ap-fzs25UIEv1GTD1kKhPy0kG` covered all source signs, three rational
`q` branches, and the required matching anchors. The retained census has 244
target-norm roots, 620 total norm/inverse candidates, 1,040 guarded source
points, 80 common nonzero `z` candidates, and 192 final-lane evaluations.
All 36 rows are complete and every final value is nonzero. The 36 free-`b`
compiler exits evaluate exactly on the already-paid cell-12 leading
boundary; no other unresolved branch occurs.

An independent verifier reconstructs 125 unique finite-field polynomials,
all 576 profile visits, every candidate-root union and leading-boundary
transport, and all final lanes. This closes matchings `1` and `2` for missing
`DF` and their exact `D/E` partners: four labels or two generic orbits. Cell
`12` now has 17 representatives and 60 labels open. The run was bounded and
well below `$1`.

**Reciprocal-role matching-3/6 closure.** Matching `3` uses the colored
source pair to constrain `z=1/d`, followed by two target polynomials in
`q=de`. The pinned adapter reuses the audited cell-4 reciprocal-square and
sign-free compiler with the cell-12 tower. One-row validation app
`ap-8WEM4ndbuvRT6z3fZqW44E` completed before the full run.

Complete app `ap-gVXjM6KiAYRUMqc52sWMU7` covered all eight source-sign and
`sigma_c` rows. The retained packet has 68 target-norm roots, 120 total
norm/inverse candidates, 176 guarded source points, 40 common nonzero `z`
lifts, and 80 final `sigma_o` lanes. No final `q` candidate, witness, or
unresolved branch survives. Eight free-`b` exits evaluate on the proved
cell-12 leading boundary.

The independent verifier reconstructs 45 unique finite-field polynomials
and all 112 profile visits. It additionally rebuilds the source kernel at
every `z` lift and computes the two final `q` polynomials directly; all 80
gcds are constant. Duplicate-positive-`DE` exchange and exact outside `D/E`
transport close matching class `{3,6}` for both missing roles: four labels
or one generic orbit. Cell `12` now has 16 representatives and 56 labels
open. The bounded run cost well below `$1`.

**Reciprocal-role matching-4/9 closure.** Matching `4` requires the audited
nested sign-free reduction in `u=q^2`, `z=1/d`, and `y=z^2`. Initial
five-minute adapter probe `ap-KUjnRrPEPizCTHjRxOtxh1` timed out before the
resultant phase and is not evidence. Extended one-row app
`ap-8gPIxDrmfyKppQLrS3bNeF` completed in 398 seconds, justifying the four-row
parallel run.

Complete app `ap-bPXHMELqRWfL6mKQBLWGEF` finished in about 5.6 minutes wall
time. The exact packet has 32 target-norm roots, 72 total norm/inverse
candidates, 120 guarded source points, eight compatible `(z,q)` lifts, and
32 final target lanes. Every final pair is nonzero; four free-`b` exits lie
on the proved leading boundary, with no witness or unresolved branch.

Direct local reconstruction of all degree-up-to-5434 roots was intentionally
stopped after three minutes to preserve the host-compute policy. Independent
Modal app `ap-tXwZKeVrmXb8r4KclbW7hG` instead reconstructed 45 unique
profiles in parallel using SymPy/Galois tools. The fast local audit validates
all 64 profile visits and directly replays the kernel, Vieta relation, and
three paired equations at every lift. Exact transports close class `{4,9}`
for both missing roles: four labels or one generic orbit. Cell `12` now has
15 representatives and 52 labels open. Total cost remained well below `$1`.

**Reciprocal-role matching-5/12 closure.** The sibling nested sign-free
compiler fixes `sigma_c` inside its second pair, so eight source-sign/anchor
rows are required. With the measured matching-4 runtime, the full set was
launched directly under a 15-minute cap. Complete app
`ap-66X2RoJ3b0eWp3KHAleEXL` finished all rows; one preempted shard restarted
transparently.

The exact packet has 88 target-norm roots, 168 total norm/inverse candidates,
256 guarded source points, 16 compatible `(z,q)` lifts, and 32 final
`sigma_o` lanes. Every final pair is nonzero; eight free-`b` exits lie on the
proved leading boundary, with no witness or unresolved branch.

Independent root app `ap-anuKZnM08xltiExRoCP3DV` reconstructed all 45
degree-at-most-5388 profiles and 244 roots with the separate SymPy/Galois
implementation. Several inputs were preempted and automatically restarted;
the retained certificate is complete. The fast local audit validates all
128 profile visits and directly replays every equation at all 16 lifts.
Exact transports close class `{5,12}` for both missing roles: four labels or
one generic orbit. Cell `12` now has 14 representatives and 48 labels open.

**Reciprocal-role matching-7/10 closure.** This class uses a direct
quadratic-in-`q` resultant followed by the sign-free `z` reduction. One-row
validation app `ap-fcr4ueqVTji80aR1qmpdTD` completed in 144 seconds. Full
eight-row app `ap-AsoabwG2JvSRt8cgkWTAA1` then finished in under three
minutes wall time.

The exact packet has 56 target-norm roots, 112 total norm/inverse candidates,
160 guarded source points, 16 compatible `(z,q)` lifts, and 32 final
`sigma_o` lanes. Every final pair is nonzero; eight free-`b` exits lie on the
proved leading boundary, with no witness or unresolved branch.

Independent root app `ap-hiouIDHxqHvElOI6F3ZTLZ` reconstructed all 41
degree-at-most-4364 profiles and 192 roots. The fast local audit validates
all 112 profile visits and directly replays every equation at the 16 lifts.
Exact transports close class `{7,10}` for both missing roles: four labels or
one generic orbit. Cell `12` now has 13 representatives and 44 labels open.

**Reciprocal-role matching-8/13 closure.** This sign-swapped sibling uses the
same pinned quadratic-in-`q` resultant and sign-free `z` reduction. Complete
eight-row app `ap-R1zUSOfqjyRYFhIdmpwhaQ` covers every source-sign and
`sigma_c` row.

The exact packet has 56 target-norm roots, 112 total norm/inverse candidates,
160 guarded source points, 16 compatible `(z,q)` lifts, and 32 final
`sigma_o` lanes. Every final pair is nonzero; eight free-`b` exits lie on the
proved leading boundary, with no witness or unresolved branch.

Independent root app `ap-76MQUn2Qxxq9Mdkmz9zKJl` reconstructed all 41
degree-at-most-4364 profiles and 192 roots using a separate SymPy/Galois-tools
implementation. The fast local audit validates all 112 profile visits and
directly replays every equation at the 16 lifts with the matching-8 sign
placement. Exact transports close class `{8,13}` for both missing roles:
four labels or one generic orbit. Cell `12` now has 12 representatives and
40 labels open.

**Reciprocal-role matching-11/14 closure.** The final reciprocal class uses
the pinned quadratic-in-`q` resultant with `q` in both `BF/CF` pairs and
`-q` in the final `EF` pair. Complete eight-row app
`ap-nTsos4Qmbgwl8kZKnnxgf2` covers every source-sign and `sigma_c` row.

The exact packet has 60 target-norm roots, 108 total norm/inverse candidates,
136 guarded source points, 16 compatible `(z,q)` lifts, and 32 final
`sigma_o` lanes. Every final pair is nonzero; eight free-`b` exits lie on the
proved leading boundary, with no witness or unresolved branch.

Independent root app `ap-3rc86N9rjOcdikbsSFiFbn` reconstructed all 45
degree-at-most-4044 profiles and 220 roots using a separate SymPy/Galois-tools
implementation. The fast local audit validates all 112 profile visits and
directly replays every equation at the 16 lifts. Exact transports close
class `{11,14}` for both missing roles: four labels or one generic orbit.
All reciprocal-role labels are now paid; cell `12` retains 11 generic
representatives and 36 labels, all in the parallel-`DE` family.
