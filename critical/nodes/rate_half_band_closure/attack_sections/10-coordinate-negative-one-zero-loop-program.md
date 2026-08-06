
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

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_exclusion`
performs that composition.  The exact orbit ledger is

```text
[0] | [1,2] | [3,6] | [4,5,7,8] | [9,10,12,13] | [11,14].
```

It is a disjoint cover of all fifteen common matching cells.  The six
terminal parents delete, in order, the aligned q survivors, crossed common
cells, the complete AB product orbit, mixed common cells, the complete
80-cell sextic product orbit, and opposite-pair common cells.  All target
and root-sign transports are included in those parents.  Therefore the
negative one-loop `(4,4,2)` packet is now closed and should be removed from
the live coordinate workboard.  Continue with negative one-loop `(4,3,3)`
or the zero-loop packet; this composition does not close the whole
coordinate orientation.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_433_loop_singleton_aligned_exclusion`
starts the remaining one-loop 433 atlas.  Normalize cell `0` by

```text
products=(-1,b,c,bc,-bc),
pairs=AB:AC and BC+:BC-.
```

For all four root-sign rows, the q-weld resultant forces `bc=+/-i` and
then fixes `r` linearly.  Product elimination in `x=t^2` leaves four
quartics related by signs and conjugation.  In deployed characteristic
they split into eight irreducible quadratics; their four discriminants

```text
2130641919, 66911228, 2063795205, 64514
```

are all nonsquares.  Thus cell `0` is empty before any outside work.  A
constant-memory `F_29/F_41` reconnaissance scan found only cells `11/14`
live at `F_29` and no live cells at `F_41`; use that only to prioritize the
five remaining target-sign orbits, not as a deployed proof.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_433_loop_singleton_crossed_exclusion`
deletes the other two loop-singleton cells.  Cells `1,2` cross `AB/AC`
against the two `BC` products.  After exact guard stripping, both q welds
are linear in `r`, with resultant

```text
same root signs:       b(c^2-1),
opposite root signs:   c(b^2-1).
```

Every factor is a product-zero or target-collision guard.  This q-only
argument covers both crossed cells and all eight sign rows.  Consequently
the complete loop-singleton sector `[0,1,2]` is empty; the live one-loop
433 common frontier consists only of the four nonloop-singleton matching
orbits.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_433_nonloop_singleton_ab_ac_finite_classifier`
classifies the first nonloop-singleton orbit, cells `[3,6]`.  In cell `3`,
product elimination gives `c` rationally in `(b,r)`; q compatibility and
the protected `t^2` equation reduce the guarded locus to one linear root of
a quartic in `r` for each sign row.  The remaining `b` equation is

```text
b^2+278278958b+1=0.
```

Its two deployed roots, combined with four `(r,t)` sign rows, give exactly
eight cell-`3` packets.  Target exchange transports these to eight cell-`6`
packets.  All sixteen satisfy the original common equations and guards.
They now require exact outside completion or exclusion; do not delete this
orbit at the common stage.  The other live common orbits are
`[4,5,7,8]`, `[9,10,12,13]`, and `[11,14]`.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_433_complete_edge_skeleton_classifier`
reduces every complete one-loop 433 outside graph to three exact orbits:
loop-free split-colored `S0`, split-colored `S1` with a loop on the
uncolored pair, and concentrated-colored `S2` with one outside loop.  The
bounded degree ledger has twelve labeled solutions in orbit sizes `3,3,6`.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_433_nonloop_singleton_ab_ac_complete_product_exclusion`
then closes cells `[3,6]`.  Their sixteen common packets have only two
target-product tuples.  The common pairs determine the product involution
and force singleton mates `673740240` and `443602659`.  Across both cells,
all outside signs, seven forced-record choices, and fifteen residual
matchings, exact Groebner reduction gives

```text
S0: 3360 unit ideals, S1: 6720, S2: 1680; total 11760.
```

The reverse variable order reproduces the census.  No outside q equations
are needed.  Delete `[3,6]`; the remaining live one-loop 433 common orbits
are `[4,5,7,8]`, `[9,10,12,13]`, and `[11,14]`.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_433_nonloop_singleton_mixed_pair_exclusion`
deletes the next orbit `[4,5,7,8]` at the common stage.  In representative
cell `4`, both q welds are linear in the singleton root.  Product elimination
is linear in `c`, and the protected square equation is independent of `c`.
After lost-degree branches reduce to guards, the four root-sign resultants
are squares of four irreducible cubics over the deployed field.  An
independent Frobenius/gcd audit confirms no cubic has a base-field root.
Target sign, target exchange, and their composition cover cells `5,7,8`.
The live one-loop 433 common frontier is now only `[9,10,12,13]` and
`[11,14]`.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_433_nonloop_singleton_bc_mixed_pair_exclusion`
deletes `[9,10,12,13]`.  Representative cell `9` has one moving and one
static row in each of the product and q halves.  The exact terminal
factorization in each root-sign row has degrees/multiplicities

```text
(1,2), (2,1), (2,2), (5,2).
```

Every nonlinear factor is irreducible over the deployed field.  At each
linear root, the candidate gcd in `b` forces the `t^2` coefficient of the
original product row to vanish while remaining coprime to its nonzero
constant, so the projection is false.  Independent Rabin tests cover all
eight quadratic and four quintic sign-row factors.  Target exchange/sign
transports cover `10,12,13`.  The sole live one-loop 433 common orbit is now
`[11,14]`.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_433_nonloop_singleton_opposite_pair_exclusion`
deletes the final orbit `[11,14]`.  Its ordinary square route and lost
moving-q coefficient route have the same four linear projections per sign
row.  Every exact candidate gcd forces `b=0` or `b=-1`; the remaining
quadratic and quartic are irreducible.  A full Rabin audit includes the
quartic's possible quadratic splitting.  Target sign transport covers
cell `14`.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_one_loop_433_complete_exclusion`
composes the terminal partition

```text
[0] | [1,2] | [3,6] | [4,5,7,8] | [9,10,12,13] | [11,14].
```

It is a disjoint cover of all fifteen cells.  Five orbits die at the common
stage and `[3,6]` dies at the complete paired-product gate.  The negative
one-loop `(4,3,3)` sector is now fully closed; continue with the remaining
zero-loop or other coordinate sectors.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_doubled_singleton_mixed_pair_exclusion`
starts the zero-loop signed atlas.  Normalize products and sums as

```text
(b,-b,c,-c,bc),       (1+b,1-b,1+c,1-c,b+c).
```

The target sign/exchange group partitions the fifteen matching cells as

```text
[0,4,7,11] | [1,3,8,10] | [2,5,6,9] | [12] | [13] | [14].
```

For representative cell `0`, ratio-preserving product reduction is linear
in `c` and `x=t^2`; the two quadratic q welds are affine-linear in `(t,r)`
after `y=r^2`.  Exact lex/Frobenius elimination in all four root-sign rows
leaves no guarded deployed packet.  Lost linear-`c`, product-solve, and
singular-q branches are independently exhausted; the only nonguard
projections have zero product denominator and nonzero numerator.  Thus the
complete orbit `[0,4,7,11]` is empty.  Continue with the five remaining
zero-loop matching orbits before constructing outside records.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_doubled_singleton_opposite_pair_exclusion`
deletes the next orbit `[1,3,8,10]`.  In representative cell `1`, product
compatibility is again linear in `c` and `x=t^2`, while safe even-factor
division preserves the q system's affine linearity in `(t,r)`.  Three sign
rows have no deployed root of their degree-14/18 eliminants.  The `(+,+)`
row has two projections, but both force

```text
y=1605884903,       X_den=0,       X_num!=0.
```

Lost linear-`c` and product branches contain only guards; the singular-q
branch adds only those same false projections.  Thus eight of fifteen
zero-loop matching cells are now empty.  Continue with `[2,5,6,9]` and the
three singleton-`BC+` cells `[12],[13],[14]`.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_aligned_doubled_pair_finite_classifier`
classifies the last doubled-singleton orbit `[2,5,6,9]`.  Representative
cell `2` has exactly eight guarded deployed common packets: four in each
same-sign root row and none in either opposite-sign row.  Every admitted
tuple passes the original product/q equations and guard; all other generic
and singular projections are guarded or have `X_den=0,X_num!=0`.  Target
transport gives exactly 32 packets across the four cells.  This orbit is
live and now requires the complete outside edge/product gate.  Separately,
the common atlas still has singleton-`BC+` cells `[12],[13],[14]` to
classify.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_complete_edge_skeleton_classifier`
now gives the exact outside edge domain for every zero-loop 433 common
packet.  Allowing the at-most-two outside roots of the nonzero quadratic
`A_1` yields 21 labeled degree solutions in five permutation types.  Three
are the familiar at-most-one-loop types; the two new types have two outside
loops.  The five types compile every signed outside product form.  Apply
them to the 32 packets in `[2,5,6,9]`, forcing the common singleton mate
before any outside q computation.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_product_skeleton_router`
executes that complete product gate over `F_(2130706433^6)`.  On every one
of the four distinct common `(b,c)` rows the involution collapses to
`y z=-c^2`.  Exact exponent-Smith enumeration deletes `Z2` and `Z3` after
target/product injectivity: all 16 `Z2` rank-two families per common
`(b,c)` row have forced collision certificates, and all isolated `Z2/Z3`
points fail a guard.
Types `Z0,Z1,Z4` have respectively `48,128,64` guarded raw product
certificates per `(b,c)` row, so the frontier moves to their quotient-label
placement and q interpolation.  Do not spend outside-q work on `Z2/Z3`.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_bc_singleton_finite_classifier`
finishes the common atlas.  Cell `12` has four packets in every sign row;
cells `13,14` have four in each same-sign row and none in opposite-sign
rows, for 32 packets across `[12],[13],[14]`.  The product determinants
split into six explicit branches, all rational solve losses are audited,
and every admitted tuple passes the original equations and guard.  Combined
with the prior orbit classifiers, all 15 matching cells are now exact: 64
common packets total, 32 in `[2,5,6,9]`, 32 in `[12,13,14]`, and none in
the remaining eight cells.  Next compile outside product involutions on the
new 32 packets while continuing quotient/q work on the live old orbit.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_bc_singleton_product_skeleton_router`
applies the complete product gate to those 32 packets.  Their common
involutions are respectively negation, reciprocal product `bc`, and
reciprocal product `-bc`.  Exact extension-log enumeration deletes
`12:{Z0,Z1}`, `13:{Z0,Z4}`, and `14:{Z0,Z4}` over every distinct product
row.  All cell-12 `Z0` free families have target-square collision
certificates.  The retained product frontier is exactly
`12:{Z2,Z3,Z4}`, `13:{Z1,Z2,Z3}`, and `14:{Z1,Z2,Z3}`; each retained type
has a guarded representative product certificate.  Only these nine
cell/type pairs should enter quotient placement and outside q work.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_complete_vieta_exclusion_router`
now composes both product ledgers with all twelve negative Vieta rows in the
explicit model `F_p[X]/(X^6+X+6)`.  Inverting the common Mobius product map
forces each outside quotient label, and the squared sum row is independent
of the deck-root sign.  Exhaustive replay deletes all live `Z0,Z1,Z4`
products in `[2,5,6,9]`, so that entire 32-packet common orbit is empty.  It
also deletes `12/Z4`, `13/Z1`, `13/Z3`, `14/Z1`, and `14/Z3`.  The exact
zero-loop 433 frontier is now only

```text
12/Z2, 12/Z3, 13/Z2, 14/Z2.
```

These four lanes have genuine rank-deficient multiplicative systems; do not
infer their deletion from sampled exponent representatives.  Reduce the
first outside squared-sum residual modulo those family ideals next.  Colored
`eta/L^c` placement is deferred until a family survives that exact cut.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_complete_exclusion`
performs that exact cut.  Every isolated Smith assignment in the four
residual lanes fails the first outside sum row.  The 192 collision-free
rank-deficient product systems, each with two common q records, give 384
polynomial ideals.  Appending at most the first three cleared squared-sum
residuals makes every ideal the unit ideal over `F_p`; this excludes the
free parameter over the algebraic closure, not only on sampled extension
exponents.  Therefore the entire negative zero-loop `(4,3,3)` skeleton is
closed.  Remove it from the coordinate frontier and return to the next live
profile/parity sector.

The PROVED
`rate_half_kb_m2_r4_coordinate_negative_complete_exclusion` now composes
the exact loop-budget partition.  Its five rows are one-loop/two-loop 442
and zero-loop/one-loop/two-loop 433.  The terminal exclusions above delete
all five, so no negative-parity coordinate-order-two packet exists.  Remove
the entire negative coordinate orientation from the `(2,4,2)` workboard.
The next coordinate work is positive parity; diagonal and trivial-stabilizer
