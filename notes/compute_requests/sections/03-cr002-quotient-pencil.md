
## CR-002: Quotient-pencil rank-two component classification

- **status:** READY FOR EXACT SYMBOLIC CONTRIBUTOR COMPUTE; do not replace it
  with an official-field point sweep.
- **consumer:** `rate_half_list_adjacent_crossing`.
- **proved router:** `rate_half_list_budget_three_fiber_four_rank_gate`.
  The known antipodal component is already descended and welded by
  `rate_half_list_budget_three_fiber_four_antipodal_descent` and
  `rate_half_list_budget_three_antipodal_mobius_weld`. The follow-on
  `rate_half_list_budget_three_antipodal_primitive_quotient_gate` proves that
  its official residual is neither a dyadic cyclic/dihedral pullback nor the
  direct four-coset deletion partition. The reverse-contact theorem
  `rate_half_list_budget_three_antipodal_pencil_degree_floor` further proves
  that the monic pencil's degree-drop direction has degree at least
  `2^36-2`. On the centered pure-quartic stratum `e_2=e_3=0`, the Wronskian
  refinement `rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity`
  proves the exact degree `v=2^37-2`. The differential refinement
  `rate_half_list_budget_three_antipodal_reverse_residual_stratification`
  proves that `T=dDU-Y(D'U+4DU')` has exact degree
  `r+4-q(r-v)`, where `q` is the first nonzero centered coefficient.

  The proved
  `rate_half_list_budget_three_fiber_two_cycle_quotient_embedding` adds a
  second direct chamber to a parameter-uniform quartic-pencil input:

  ```text
  source branch             quotient order   member degree   dyadic M
  fiber-four antipodal          2^39            2^37-1         2^35
  fiber-two cycle, matched c=0  2^40            2^38-1         2^36.
  ```

  The cycle router is exhaustive in the number `c=0,1,2` of antipodal
  deleted-root pairs; completion-root coincidence is analytically impossible.
  Every stratum inherits the Mobius weld, primitive map
  degree, and degree floor `deg V>=2^37-2`. Only `c=0` has the matched
  denominator `product_i(Y-rho_i^2)` in the table. The `c=1,2` denominators
  replace one or two repeated coefficient-square roots by exceptional-pair
  squares and require separate symbolic routing. The proved
  `rate_half_list_budget_three_fiber_two_cycle_boundary_transfer` now replays
  the reverse-residual, pure, fourth-root, secondary, two-window, parity, and
  canonical-span stages at `d=2^40,s=2^38`. It finds linear generic and
  intermediate floor residuals and pins the completion-root PGL matching.
  The remaining finite symbolic audit begins after canonical span: the
  matched `c=0` two-antipodal-denominator subbranch now passes through
  `rate_half_list_budget_three_fiber_two_cycle_matched_lift_field_router`.
  At `M=2^36`, the order-`2^39` Fourier resultant removes the prime-field and
  negative quadratic branches. In the remaining `p=1 mod 2^40` branch, all
  quotient coefficients and outer roots descend to `F_p`; conjugating the
  three Mobius-ratio equations also eliminates the apparently quadratic
  anti-invariant source lifts. The proved
  `rate_half_list_budget_three_fiber_two_cycle_matched_post_field_compiler`
  then closes the harmonic branch and transfers the ODE, scalar, constant,
  Legendre, and gcd stages. Its exact final gate is `T/q_out=W^4`, invariant
  under reciprocal choice. This repairs the old unscaled `T=W^4` condition,
  which is false as a coverage gate for exact-order-`2^39` outer ratios in the
  nonsplit field class. The proved
  `rate_half_list_budget_three_fiber_two_cycle_matched_trace_jacobi_norm_transfer`
  now supplies the remaining exclusion interface: two torsion-sign packets,
  each with six degree-`2^36` Jacobi gcds, one top norm at order `2^39`, and a
  37-level plus tower through order `2^38`. The mathematical contract is
  complete for this parity subbranch,
  but no compressed implementation or measured pilot exists. Other matched
  denominator geometries are not covered. For `c=1,2`, the proved mismatch
  invariant router replaces the old denominator-lift Mobius search by 24 and
  six explicit binary-quartic scalar tests. The follow-on trace-resolvent
  theorem eliminates their radicals and discrete lift signs: `c=1` is twelve
  quadratic norms, while `c=2` is one degree-`6`/degree-`3` resultant in the
  coefficients of `D_*` and the canonical outer quartic. The proved
  `rate_half_list_budget_three_fiber_two_cycle_c2_outer_torsion_trace_gate`
  adds an outer official-order prefilter for `c=2`: forty squarings and cubic
  reductions test whether the outer invariant cubic has a trace coming from
  `mu_(2^40)`. The proved joint selector then intersects that terminal trace
  equation with the degree-six actual-pair resolvent. Its degree-at-most-three
  gcd is nonconstant exactly when the same trace belongs to an actual pair
  with invariant coupling and quotient torsion; outer-only false positives
  are discarded before reconstruction. Finally, common subgroup scaling
  replaces the six labelled pairs by one role-labelled `(t,S,P)` chamber
  modulo `(t,S,P)->(t^-1,S/t,P/t^2)`, with forty scalar squarings compiling
  all three nontrivial quotient roots. These are constant-memory theorem-side
  reductions, not contributor computations. The remaining next step is
  symbolic substitution of the twelve `c=1` norms and the normalized `c=2`
  chamber into the coefficient-gap and canonical-span equations, not a raw
  official-order sweep. The `c=1` packet
  also has a coefficient-only compiler: one bidegree-at-most-`(18,18)`
  divided-quartic iterated resultant equals `e_4^36` times the twelve-norm
  product. Future implementations must use that resultant rather than factor
  `D_*` merely to enumerate the root choices. Canonical covariance further
  turns theorem search into one role-labelled `(S,P,c)` chamber with
  repeated square one. Its three quotient-root torsion conditions use forty
  coupled scalar squarings. This normalization is cheap preprocessing, not a
  compute request; split, square-class, gap, and canonical-span checks remain.

  **Pre-request CR-002-C (next-order cycle shard).** The boundary transfer
  proves that a two-antipodal-pair denominator uses `M=2^36`, and the matched
  lift field router proves that every surviving normalized lift lies in
  `F_p`. This conclusion requires only `p=1 mod 2^40`; a contributor must not
  impose the stronger `p=1 mod 2^41` or allocate a separate quadratic-lift
  shard. A preregistered `$0.25`-capped harmonic extension has already checked
  the only new source-trace level over all `2,247,720` split congruence classes
  and found no hit; contributors must not repeat that campaign. The proved
  trace-Jacobi/cyclotomic-norm transfer gives the exact torsion-only screen at
  `M=2^36`: one top
  cyclotomic norm at order `2^39` and a `37`-level plus tower at orders
  `2^2,...,2^38`. Record this as a second contributor shard after
  CR-002-J0, not as permission to run it. PASS, FAIL, and incomplete outputs
  have the same certificate meanings as J0 but must carry the cycle source
  key, `c=0`, and the doubled parameter ledger. The `c=1,2` mismatch strata
  now have a coverage-equivalent thirteen-gate radical-free elimination, and
  `c=2` also has the cheap forty-step joint actual-pair selector and normalized
  `(t,S,P)` chamber above.
  The `c=1` side is likewise one constant-degree coefficient resultant.
  Any future `c=1` implementation must use its normalized `(S,P,c)`
  chamber and may not multiply work by twelve labelled root choices.
  They remain theorem requests rather than norm-compute requests until
  canonical span has been eliminated or a separately piloted algorithm has a
  finite completeness and cost boundary. A future contributor proposal must
  report how many candidates survive the joint selector and must not spend
  official-order resources on candidates that fail it. The exact
  decision contract is now:

  - **PASS:** neither torsion resultant has an official-compatible odd-prime
    divisor; this closes both six-branch trace-Jacobi packets in the matched
    parity subbranch and all fourteen primary/torsion/constant tests in the
    generic two-antipodal `c=1` parity packet.
  - **FAIL:** print each `(p,epsilon)`, a compact factor certificate, and
    `gcd(J,K_epsilon) mod p`; then evaluate the relevant signed `F_(j,s)` gcds
    and all relevant `c=1` polynomials: `F_R0,epsilon`, plus
    `F_R(s),F_P0(s),F_P(s)` for both roots `s^2=-epsilon`. Then replay the
    corrected scalar, next-coefficient, gcd-degree, and `T/q_out=W^4`
    filters.
  - **INCOMPLETE:** retain proved norm levels, cofactors, hashes, and exact
    characteristic coverage, with no DAG status change.

  This complete mathematical contract does not promote the task to a runnable
  request. It still lacks a compressed implementation, small-order measured
  pilot for that implementation, streaming checker, memory/storage estimate,
  and conservative dollar ceiling. Any larger or alternative official-order
  run must remain recorded here and be proposed in an upstream PR only after
  those artifacts exist. In particular, no contributor should run the old
  unscaled fourth-power schema at `M=2^36`; all survivors use the corrected
  downstream gate.

  **Completed CR-002-C1H (c=1 parity harmonic residues).** The proved
  `c=1` parity Mobius router leaves only two harmonic classes up to sign
  and conjugation:

  ```text
  H_R: r^2+3(1+iota)r+iota=0,
  H_P: 5r-4+3iota=0.
  ```

  They have fixed reciprocal-trace forms. For `H_P`,
  `r+r^(-1)=8/5`. For `H_R`, choose `zeta^2=iota`,
  put `s=r/zeta`, and set `theta=(1+iota)/zeta`; then
  `theta^2=2` and `s+s^(-1)=-3theta`. Source torsion requires the
  corresponding repeated-square trace recurrence to reach `2` by level
  `41`.

  The field router now proves the complete positive-quadratic interval and
  descent of both source lifts. Modal app
  `ap-Js6Im9DeoBlc0di05YG2WE` then completed the bounded two-trace
  campaign over all `4,495,441` integer moduli with no hit. All 32 shards
  finished in at most 3.121 seconds under the `$0.50` ceiling. The result,
  digests, launcher hash, and independent checker are pinned in the
  harmonic-exclusion node. This closes only harmonic `c=1` parity.
  Contributors must not duplicate the campaign; the remaining valuable work
  is theorem-level control of the six nonharmonic tests.

  **Pre-request CR-002-C1N (c=1 parity nonharmonic scalar packets).** The
  proved nonharmonic scalar compiler now supplies the exact mathematical
  interface that a future contributor implementation must preserve. There
  are six role-labelled source traces `y`, not a free outer-ratio search.
  Each branch has the complete decision sequence

  ```text
  y_39=2,       y notin {2,-2},
  S^2=(y+2)T,
  T/q_out=W^4,       q_out^2-yq_out+1=0,
  4tH_(4M-1)(t)^2+y+2=0,
  deg gcd(S,2L+kappa x^2U_0^3)>=M-1.
  ```

  Here `M=2^36`, `L=2^39`, and the reciprocal choice of `q_out` does not
  change the fourth-power verdict. All square-pencil and unordered-trace
  data descend to `F_p` on the exact field line `q_field=p^2`,
  `p=1 mod 2^40`; the source lift itself must not be assumed to descend.

  This is still an algorithm pre-request, not permission for an
  official-degree run. A contributor-scale campaign becomes useful only
  after an implementation represents `U_0,S,T,H` without materializing
  degree-`2^37` dense polynomials, proves that all six branches and all
  official characteristics are covered, and publishes a measured
  small-order pilot. Its request packet must include a conservative CPU,
  RAM, storage, and dollar ceiling; resumable characteristic/branch shards;
  and a streaming checker for every displayed identity.

  **PASS** means all six packets reject on every official characteristic and
  would close the two-antipodal `c=1` parity subbranch. **FAIL** must emit a
  replayable characteristic, role, source trace, reciprocal quadratic,
  compact polynomial certificates, and the first failed/passed gate; it may
  expose a genuine survivor or a false upstream premise. **INCOMPLETE** must
  retain exact interval/branch coverage, hashes, and partial certificates
  and causes no DAG status change. Cost is currently unknown, so this item
  remains outbound contributor work and is not authorized against the local
  Modal balance.

  **Pre-request CR-002-C2N (normalized c=2 mismatch chamber; not runnable).**
  This is the recorded handoff for a potentially valuable large computation;
  it must not be replaced by a sweep over six labelled denominator pairs.
  The theorem-side input is one chamber

  ```text
  D_A(Y)=(Y-1)(Y-t)(Y^2-SY+P),
  z=(1+t)^2/t,
  K_A(z)=0,
  t_40=1,       T_40=2,       P_40=1,
  tP(t-1)(1-S+P)(t^2-St+P)(S^2-4P)!=0,
  ```

  modulo the orientation involution
  `(t,S,P)->(t^-1,S/t,P/t^2)`. The forty-step recurrences and the
  degree-at-most-three joint actual-pair selector are exact. Any campaign
  must then use the proved normalized gap-span compiler. It generates
  `E^(-1/4)` by the signed four-term recurrence, enforces
  `a_(2H-2)=a_(2H-1)=0`, uses the equivalent secondary differential
  divisibility without constructing the high window, reconstructs
  `alpha=4c,beta,gamma`, and applies the final scalar invariant equation at
  `z_t=(1+t)^2/t` before cycle reconstruction. The torsion terminal already
  forces splitting and square class; distinctness remains explicit.

  The mathematical decision interface is now finite and coverage-exact, but
  a naive implementation has official length and is not a responsible run.
  Missing prerequisites are a compressed evaluator for the recurrence and
  polynomial span identity, an exhaustive official characteristic ledger
  organized into the fixed and reciprocal-Frobenius chambers, a canonical
  representative or orbit-safe deduplication under the involution, and a
  measured small-order pilot. Until
  those exist there is no responsible CPU, RAM, storage, or dollar estimate;
  cost is explicitly **unknown and potentially large**, so the local Modal
  balance must not be used.

  A bounded falsification sweep now constrains the theorem strategy. Across
  `680,500` normalized quartets in twenty smooth rows (`H=3,...,12`, two
  admissible characteristics per height), the nondegenerate primary gap had
  22 survivors, including twelve non-pure quartets. Thus primary-only
  fourth-root rigidity is false and must not be used in a contributor
  compiler. None of the twelve non-pure survivors passed the secondary square
  gate; all six primary-plus-secondary survivors were pure fourth-root
  quartets. A separate proof excludes that pure geometry at the official odd
  value `H=2^37+1`.

  The minimal repaired implication "primary plus secondary, together with
  official root torsion and distinctness, implies a
  two-antipodal denominator" is therefore a high-value theorem/falsification
  target, not a compute assumption. The official qualifiers cannot be
  dropped: the split squarefree quartic
  `1+z+11z^2+34z^3+43z^4` over `F_53` passes both gap packets at `H=8` but
  is nonparity. Its roots have orders `52,13,13,52` and mixed square classes,
  so it is an exact gap-only counterexample rather than an official packet.
  The stronger pure
  fourth-root conclusion also survived the sweep, but is unnecessary: the
  proved parity router collapses all six `c=2` selected pairs to three traces
  and imports the existing CR-002 Jacobi norm pair. The pure value itself is
  already excluded at the official row. More bounded rows cannot certify
  either official quantifier. A donated large run should not be requested
  merely to extend this census; contributors should instead seek an algebraic
  proof using the subgroup constraints, a compact official-torsion
  counterexample, or a coverage theorem reducing parity forcing to finitely
  many arithmetic cases. A gap-only differential or Groebner campaign cannot
  prove the required result and should not receive donated compute. The
  scripts, representative
  counterexamples, exact downstream census, and ledger check are in
  `experiments/prize_resolution/` under the
  `rate_half_list_*rigidity*` and
  `rate_half_list_fiber_two_cycle_c2_normalized_small_order_census*` names.

  **Pre-request CR-002-C2PAR (official-torsion parity certificate; not
  runnable).** A potentially valuable donated-compute task is to construct a
  sparse cyclotomic/elimination certificate for the following exact
  alternative at `H=2^37+1`, `N=2^40`: every distinct normalized quartet in
  `mu_N` that passes both coefficient gaps is two-antipodal, or there is a
  compact official-compatible witness. The
  purpose is to close the structural gate before canonical span and route all
  survivors through the shared CR-002 norms.

  Inputs must be the four-term fourth-root recurrence, the proved equivalent
  secondary differential divisibility (which removes the high coefficient
  window), forty-step scalar torsion recurrences, and distinctness. The proved
  torsion-field router makes splitting and square class automatic and divides
  the algebra into fixed and reciprocal-Frobenius chambers. A valid algorithm
  must exploit dyadic/cyclotomic structure or produce a parameter-uniform
  certificate. Naive enumeration of
  `mu_N` quartets, dense degree-`2^36` polynomials, and gap-only Groebner
  elimination are out of scope. No coverage algorithm, pilot, or credible
  resource estimate exists yet; the cost is **unknown and potentially very
  large**, so this is a contributor design request, not authorization to use
  the local Modal credit.

  Every shard or certificate component must emit its normalized parameter
  region, exact integer/modular hashes, first unresolved gate, and a compact
  replay object. An independent checker must reconstruct the quartet or
  certificate, replay torsion and both gaps, and verify the parity/nonparity
  conclusion without trusting search logs. **PASS** is a coverage-complete
  certificate for official parity forcing and would make the parity router
  applicable to all `c=2` candidates. **FAIL** is one distinct order-`2^40`
  nonparity quartet passing both gaps; splitting and square class are checked
  consequences of torsion. It refutes `C2-PAR` and
  redirects work to canonical span and coupling. **INCOMPLETE** preserves
  exact covered regions and certificates but changes no DAG status.

  The exactly-one-antipodal stratum now has a stricter pre-request interface.
  Normalize its known pair to `{1,-1}`, put

  ```text
  P=cd,       t=c/d,       Z=t+t^(-1),       X=P(Z+2),
  a_(2H-2)=F_H(X,P),       a_(2H-1)=(c+d)G_H(X,P).
  ```

  Since `X!=0` on this stratum, both primary equations are `F_H=G_H=0`.
  Complementary-root torsion must be imposed on that same `(P,Z)` by

  ```text
  P_(j+1)=P_j^2,       Z_(j+1)=Z_j^2-2,       0<=j<39,
  P_39^2=1,            Z_39=2P_39.
  ```

  A donated symbolic campaign may target a sparse joint cyclotomic
  certificate for this circuit before the antipodal-free stratum. It must
  not stop at `Res_X(F_H,G_H)` intersected with independent product and ratio
  torsion: incompatible half-order signs leave false positives. The exact
  distinctness gate is `(Z^2-4)(1+P^2-PZ)!=0`; reconstruction makes a
  separate square test unnecessary. In both official field chambers
  `Z in F_p`. Use `P in F_p` in the fixed chamber and `P^p=P^-1` in the
  reciprocal chamber.

  **PASS** for this subcampaign is a coverage-complete certificate that the
  displayed exactly-one-pair circuit has no official-field solution; it
  removes that stratum but leaves antipodal-free C2-PAR open. **FAIL** emits
  one official characteristic and compact `(P,Z)` certificate from which an
  independent checker reconstructs `t,c,d`, replays both primary
  coefficients, all 39 coupled torsion updates, distinctness, and `X!=0`.
  **INCOMPLETE** emits the covered cyclotomic factors or parameter regions
  and changes no DAG status. No compressed representation of `F_H,G_H`,
  official-coverage implementation, measured official-scale pilot, or
  credible cost ceiling exists, so this remains an algorithm and
  donated-compute request with unknown potentially large cost.

  A guarded small-order pilot on 2026-07-21 tested the complete split-field
  one-antipodal circuit at `N=8,16,32,64`. It enumerated respectively
  `6,672`, `53,424`, `251,580`, and `1,039,740` admissible unordered
  complementary pairs over every prime `p=1 mod N` below
  `20,000`, `50,000`, `100,000`, and `200,000`, with no simultaneous primary
  double-gap hit. Total coverage was `1,351,416` pairs. Separate symbolic
  resultants at `N=16,32` showed why the coupled gate must remain: product
  torsion has exceptional-characteristic common roots, but every checked
  split exceptional root failed the half-order trace sign.

  This is heuristic support for the exact circuit, not evidence about the
  official quantifier. It does not supply the missing compressed
  representation, and scaling the pair enumeration to `N=2^40` would be
  worthless. A valuable large contribution is still an algorithmic theorem:
  a sparse dyadic/cyclotomic representation of the joint primary and coupled
  sign ideal, with a measured bounded-order replay and a proved official
  coverage map. Until that exists, its cost remains unknown and no paid run
  is requested.

  **Pre-request CR-002-C2CELL (one-antipodal canonical-cell classifier; not
  runnable).** There is now a downstream alternative to eliminating the
  primary `(P,Z)` circuit. After secondary gap, canonical span, and split
  outer gates, every complete one-antipodal candidate gives

  ```text
  Q=(1-z^N)/E=product_(i=1)^4(B+w_i z^H C),
  mu_N\{1,-1,c,d}=A_1 disjoint_union ... disjoint_union A_4,
  |A_i|=2H-3.
  ```

  The proved Fourier ladder makes the four cell power sums equal through
  degree `H-1`. More generally, a weight vector orthogonal to
  `1,w,...,w^s` annihilates all cell moments below `(s+1)H` for
  `s=0,1,2`. Under source negation, each such weighted coloring is either
  exactly invariant or has support at least `(s+1)H+1`; the official sharp
  forms are `2H+2` for `s=1` and `3H+1` for `s=2`.

  The unique barycentric direction is no longer a dichotomy. With
  `Phi(W)=product_i(W-w_i)` and `lambda_i=1/Phi'(w_i)`, its negation
  difference has zero moments below `3H` and first syndrome exactly `-2H`.
  Hence its support is always at least `3H+1`. At equality, if `Psi` is the
  support polynomial, every value is forced to be `-2H/Psi'(a)` and `Psi`
  is even. A contributor classifier must enforce this syndrome and equality
  packet before considering larger-support cases; a run that merely checks
  the older invariant alternative is obsolete.

  The barycentric direction also has a cell-free endpoint. The proved
  compiler forms one even polynomial

  ```text
  J=(1-Sz+Pz^2)C(z)^2Theta(z)
    +(1+Sz+Pz^2)C(-z)^2Theta(-z),
  Theta=HBC+z(BC'-B'C),       deg J<=5H-11.
  ```

  Minimum support is equivalent to `J` having degree `5H-11`, dividing
  `(z^N-1)/(z^2-1)`, and avoiding `+/-1`. Consequently a contributor must
  not enumerate canonical cells even in the equality case. The useful
  algorithm request is a compressed subgroup-divisor rejection for `J`,
  followed by a root-count/classification argument for the larger-support
  cases. Dense construction of `B,C,J` is still forbidden, and no compressed
  evaluator or cost model exists.

  The collision geometry now controls the full low-support band, not only
  equality. If the four barycentric weights are distinct, the odd Wronskian
  root count gives `|supp(u)| >= 4H-2`. Otherwise exactly one pair collides,
  and the normal form and `L/Q` alternatives in `(COLL1)` apply at every
  support. Thus every one-antipodal packet with `|supp(u)| <= 4H-4` is already
  on the `L/Q` locus. A contributor implementation should route the
  distinct-weight case to the high-support ledger and should not scan it in
  the low band.

  Canonical degree now refines this routing. Put `e=H-3-deg C`. If `r_J`
  counts the ordinary subgroup roots of the support polynomial, then

  ```text
  |supp u|=3H+3e+1_(e even)+eta,       eta in 2 Z_(>=0).   (COLL0)
  ```

  On `e=0`, the Euler/cube gate `(COLL2)`, infinity gate `(COLL4)`, and the
  selected-antipodal affine and Stepanov gates `(COLL5)--(COLL8)` are valid
  at every support. Route those packets through the filters before any
  support-level enumeration. The split-divisor condition for `J`, endpoint
  `Xi` gate `(COLL3)`, and conclusions that explicitly use `eta=0` remain
  minimum-support-only. Degree-deficient packets must retain `(COLL0)` and
  must not be tested with maximal-degree top-coefficient formulas.

  **Deferred large run CR-002-C2CELL-COLL (minimum-support one-pair collision
  locus; contributor compute only).** The proved collision router removes
  every minimum-support packet except an exact one-pair derivative-weight
  collision. For a nonzero pair-sum parameter `s`, put `y=s^2/alpha`. A
  retained packet has

  ```text
  beta=-s^3,
  gamma=alpha^2/4+alpha s^2/2,
  Phi(T)=(T^2-sT+s^2+alpha/2)(T^2+sT+alpha/2),
  L: y(z_t+12)=2z_t-8,
  Q: [y(z_t+12)-16]^2=64z_t,
  -2alpha/(z_t+12) is a nonzero square.               (COLL1)
  ```

  Triple, two-pair, and fourfold collisions are proved impossible and must
  not be searched. The old cubic invariant equation has also been replaced
  by the two displayed branches; the two square-root signs on `Q` are one
  orbit and must not be duplicated. The two branch intersections
  `(y,z_t)=(0,4),(4/3,36)` belong to `L`; define the second shard by
  `Q=0,L!=0`. The requested run is a compressed
  classifier on `(COLL1)` together with `(C2G3)--(C2G8)`, the selected-ratio
  torsion recurrence, the exactly-one-antipodal source equations,
  squarefree/field-chamber conditions, and the split-divisor gate for `J`.
  It must retain `s` and the displayed factors, not merely solve the
  eliminated equation
  `(4gamma-alpha^2)^3=8alpha^3 beta^2`, which is only necessary over the
  official base field. Raw scans of `(alpha,beta,gamma)`, dense
  official-degree `B,C,J`, subgroup enumeration, and any trace-`-12` campaign
  are obsolete.

  The selected-antipodal shard is fixed at `z_t=0`, `y=4/3`, with
  `12gamma=11alpha^2`, `27beta^2=64alpha^3`, `J=0`, and `-alpha/6` square.
  It should be screened first because it has no residual `y` search. The
  non-antipodal shards use the `L/Q` label and the unordered square-root
  trace orbit `x~=-x`, where `z_t=x^2`.

  Every shard has a mandatory outer-free prefilter. Form

  ```text
  T_0=(H-1)EB+Hc_0z^(2H)-(H-1)E_4b_0z^(2H+1),
  P_0=z^(-2H)(T_0B^3-(H-1)),
  c_0=a_(2H),       b_0=a_(2H-3).
  ```

  Minimum support forces `deg C=H-3`; more generally every retained
  maximal-degree packet, at any support, must satisfy

  ```text
  C divides P_0,
  C_sharp=C/lc(C),
  Res(C_sharp,T_0)Res(C_sharp,B)^3=(H-1)^(H-3),
  Res(C_sharp,T_0) is a nonzero cube.                  (COLL2)
  ```

  The secondary-differential theorem makes this gate derivative-free; no
  high coefficient window is an input. This Euler remainder precedes all
  outer coefficients, selected-pair traces, and `L/Q` branches. A contributor
  implementation should evaluate `(COLL2)` first and stop a shard immediately
  on a nonzero remainder. A run that constructs or scans
  `alpha,beta,gamma,y,z_t` before applying this gate is obsolete.

  A shard surviving `(COLL2)` has a second mandatory constant-size endpoint
  prefilter.  Write `r=2H-3`, `m=H-3`, let `b_i=[z^i]B` and
  `c_j=[z^j]C`, and compute

  ```text
  Delta_inf=b_(r-1)c_m-b_rc_(m-1),
  Xi=H/(P c_m^2 Delta_inf).
  ```

  Minimum support forces `Delta_inf!=0`, and every retained packet must pass

  ```text
  Xi^(N/2)=1,                    N/2=2^39.            (COLL3)
  ```

  This test reads only the four top canonical coefficients and the
  complementary-source product `P`.  The checker must reject zero
  `Delta_inf`, reconstruct `Xi`, and evaluate `(COLL3)` by bounded repeated
  squaring before any full `J` split-divisor or `L/Q` work.  It must not build
  `J`, list its roots, or enumerate `mu_N` merely to check `(COLL3)`.  Failure
  is a proved rejection of that minimum-support shard; passage is only a
  necessary condition and does not certify the packet.

  After the canonical outer coefficients are available, apply the
  infinity-cell quartic gate before either `L/Q` branch is expanded.  Put

  ```text
  b=[z^(2H-3)]B,       c=[z^(H-3)]C,
  O_inf(X)=(X-b)^4+alpha c^2(X-b)^2
             +beta c^3(X-b)+gamma c^4.              (COLL4)
  ```

  A retained packet must have `c!=0`, `O_inf(0)=P^(-1)`, and
  `O_inf | X^N-1`.  Check the last condition without factoring: start with
  `R_0=X mod O_inf`, perform forty reductions
  `R_(j+1)=R_j^2 mod O_inf`, and require `R_40=1`.  The checker must also
  verify that the four reciprocal derivative weights of `O_inf` have exactly
  one equal pair.  On the fixed selected-antipodal shard it must additionally
  require the centered binary-quartic invariant `J_inf=0`.

  This is four-coefficient arithmetic and does not authorize construction of
  a subgroup list.  It is not an emptiness theorem: an exact order-32 control
  over `F_97` is a non-antipodal `J_inf=0` subgroup quartet with exactly one
  derivative collision.  Any classification or campaign which treats
  `(COLL4)` alone as contradictory is invalid; it must retain the canonical
  recurrence, gap, source, and completion coupling.

  The fixed selected-antipodal shard has a smaller replacement interface.
  Choose `q^2=-alpha/6`, put `a=s/(2q)`, and derive from the canonical top
  coefficients

  ```text
  tau=ell_4,       y=ell_3/ell_4,       a^2=-2,
  A_a(y)=(a+2)y-(a+1),
  B_a(y)=(a-1)y+(2-a).                               (COLL5)
  ```

  Require

  ```text
  y!=1,
  tau,y,A_a(y),B_a(y) in mu_N,
  tau^4 y A_a(y)B_a(y)=P^(-1).                       (COLL6)
  ```

  Before reconstructing `tau`, apply the scale-free two-bit gate

  ```text
  Z_inf=P y A_a(y)B_a(y),
  Z_inf^(N/4)=1,                    N/4=2^38.         (COLL7)
  ```

  Reject a shard immediately when `(COLL7)` fails.  Passing `(COLL7)` says
  only that a fourth-root scale exists in `mu_N`; the canonical `tau` must
  still be reconstructed and checked against `(COLL6)`.

  Four scalar forty-squaring traces check the memberships.  The two choices
  of `q` are one orbit under
  `(a,y,tau)->(-a,y^(-1),tau y)` and must not be duplicated.  A checker can
  reconstruct

  ```text
  u=a+(y+1)/(y-1),       d=tau(y-1)/2,
  b_(2H-3)=du,            c_(H-3)=d/q
  ```

  and compare them with the canonical outputs before retaining the shard.
  Any future classification should attack this three-affine-image subgroup
  intersection by a coverage-proved algebraic or character-sum method.  Raw
  enumeration of `y in mu_N` is forbidden, and an exact order-32 passing
  control shows that `(COLL5)--(COLL6)` alone are not contradictory.

  The proved all-field Stepanov specialization gives the exact a priori cap

  ```text
  #{y in mu_N:A_a(y),B_a(y) in mu_N}
    <=355106851<2^29.                                 (COLL8)
  ```

  It uses `A_0=D_0=79896510`, `B_0=12902`, and the official characteristic
  lower bound `p>=31950697969885030204`; it is valid in the prime, split
  quadratic, and unitary quadratic chambers.  This cap is not itself an
  enumeration algorithm.  A sweep over all `355106851` possible retained
  values, or over all `2^40` subgroup elements to find them, is outside the
  local and current Modal budget.  Such a campaign remains a donated-compute
  request unless a pilot supplies a nonenumerative candidate generator,
  measured throughput and memory, checkpoint format, independent checker,
  and a conservative dollar ceiling below the contributor's approved spend.

  **Completed finite sieve CR-002-C2CELL-COLL-RF (reciprocal selected-
  antipodal affine shard; do not rerun).** The reciprocal field
  chamber no longer has an affine search variable. For

  ```text
  N=2^40,       p=kN-1,
  29058991<=k<=33554432,
  r=(2a-1)/3,       a^2=-2,
  ```

  the three memberships in `(COLL6)` force

  ```text
  y=-r^2=(7+4a)/9,
  A_a(y)=r,       B_a(y)=-r.
  ```

  They hold exactly when the base-field trace recurrence

  ```text
  R_0=-2/3,       R_(j+1)=R_j^2-2,       R_40=2 mod p
  ```

  passes. There are exactly `4,495,442` progression values before primality.
  Modal app `ap-Ifv7cgmA0WCon3SfgP1aSo` partitioned the inclusive interval
  into sixteen disjoint shards. It processed all `4,495,442` values, including
  composites, with exact coverage and **zero hits**. The longest shard took
  `3.13` seconds under `512 MiB`, below the registered `$0.25` ceiling. The
  positive control `N=32,p=31` passed. The launcher, banked result, sixteen
  coverage digests, and deterministic checker are registered and hash-pinned.

  This is a stronger PASS than a prime-only sieve and excludes the reciprocal
  maximal-degree selected-antipodal collision shard. No extension-field
  arithmetic, subgroup enumeration, affine scan, or canonical coefficients
  were used. Do not rerun this campaign; redirect contributor compute to the
  fixed-field, degree-deficient, or non-selected-antipodal branches.

  Shard by official field chamber, first-match branch, normalized `(s,alpha,z_t)` orbit,
  and the compressed recurrence state. Each shard must checkpoint its exact orbit
  interval, retained-count ledger, rolling hash, and every compact survivor.
  The independent checker reconstructs the two outer quadratics, verifies the
  repeated derivative weight, the Euler remainder and cube resultant, the
  endpoint determinant and half-order torsion test, the infinity-cell quartic
  remainder and derivative-collision pattern, the selected-antipodal affine
  packet when applicable, all forty source torsion recurrences, primary and
  secondary gaps, canonical span, source distinctness, and the `J` divisor or
  root-count verdict. Keep large logs and factors remotely; vendor only
  manifests, compact survivors, and checker fixtures.

  **PASS** is coverage-complete emptiness of `(COLL1)` after all retained
  gates; it removes the minimum-support one-antipodal branch but leaves
  larger support open. **FAIL** emits one complete replayable candidate and
  changes the downstream DAG according to its independently checked status.
  **INCOMPLETE** preserves exact shard coverage and has no DAG effect. There
  is not yet a compressed evaluator, coverage proof, or credible cost model,
  so no run is authorized against the remaining local Modal balance. A pilot
  must publish CPU, RAM, storage, and a conservative dollar ceiling below
  `$1`; any larger campaign is an upstream request for donated compute.

  A valuable contributor result would be a coverage-complete classification
  of these invariant and large-mismatch alternatives that also preserves
  the outer Mobius matching. Raw enumeration of `mu_N`, arbitrary four-color
  partitions, or dense construction of the four degree-`2H-3` factors is
  forbidden: none is a complete or plausibly costed algorithm. A proposal
  must first give a compressed orbit/transition representation, prove that it
  covers every coloring satisfying the ladder, publish a small-order pilot,
  and state CPU, RAM, storage, and dollar ceilings.

  **PASS** is a parameter-uniform proof or independently checked certificate
  that no exactly-one-antipodal canonical coloring passes all source and
  completion gates; it removes this complete-candidate stratum without
  asserting primary-only emptiness. **FAIL** emits one official
  characteristic and a compact formula for `c,d,B,C,w_i` and the four cells
  from which a checker reconstructs the factorization, Fourier ladder,
  negation transitions, Mobius match, and downstream cycle packet.
  **INCOMPLETE** retains exact orbit/transition coverage and hashes but has no
  DAG effect. No coverage algorithm or cost model exists, so this is an
  upstream theorem/algorithm and donated-compute request only.

  A future request must be resumably sharded by official characteristic,
  fixed/reciprocal field chamber, and normalized orbit, with a conservative
  dollar ceiling and hard memory limit. Its independent checker must replay
  all forty scalar recurrences, distinctness, both coefficient gaps, and the
  parity verdict from compact emitted certificates. **PASS** proves C2-PAR
  and routes the surviving parity packets to the already shared CR-002 norm
  interface; it does not by itself close that norm interface. **FAIL** must
  print one replayable official row, `(t,S,P)` orbit, coefficients, and a
  nonparity quartet passing both gaps.
  **INCOMPLETE** must retain exact shard/orbit coverage, hashes, and partial
  witnesses and has no DAG status effect. This pre-request is suitable for
  an upstream PR asking contributors for algorithm design or donated compute
  after the missing compressed implementation, field ledger, and pilot are
  supplied.

  **Completed CR-002-C1AI (anti-invariant source residues; do not run).**
  Frobenius comparison of the six source traces reduces every anti-invariant
  non-`R0` lift to two fixed traces: `-8` for `R1/R2` and `6/5` for
  `P1/P2`; `P0` is algebraically impossible. Modal app
  `ap-6KQ2mJjoE3Qkq7VaKqnxlZ` checked all `2,247,721` odd-`k` moduli in the
  exact positive-quadratic interval with no hit. All 16 shards completed,
  the longest took 2.957014 seconds, and the compact digest packet and
  independent checker pass. This proves that `R1,R2,P0,P1,P2` source lifts
  descend to `F_p`; it does not reject their invariant packets.

  `R0` is the only source trace invariant under `r -> -r`. Its lift variable
  has now been removed analytically: the two traces over fixed `t=r^4` are
  the roots of

  ```text
  K_t(Y)=t(Y-2)^2+4(t-1)^2,
  ```

  and scalar elimination gives

  ```text
  t(S^2-4T)^2+4(t-1)^2T^2=0,
  4t(1+tH_(4M-1)(t)^2)^2+(t-1)^2=0.
  ```

  Any future CR-002-C1N implementation must use direct `F_p` source
  arithmetic on the five descended branches and the quadratic quotient
  compiler on `R0`. It must not allocate extension-field lift shards or
  repeat C1AI. The entire primary/torsion/constant packet now reduces further
  to seven degree-`2^36` Jacobi gcds per torsion sign. Exact lift norms
  collapse the six source roles to `R0`, common `R1/R2`, `P0`, and common
  `P1/P2` families. Their torsion prefilters are literally the same
  `R_-,R_+` norm pair already requested by CR-002-C. Do not request a
  separate `c=1` norm campaign. A compatible divisor must additionally pass
  one of

  ```text
  F_R0,epsilon,
  F_R(s), F_P0(s), F_P(s),       s^2=-epsilon.
  ```

  The remaining expensive issue is compressed evaluation of the shared
  norms and then the fourteen branch-specific scalar and later Euclidean,
  fourth-power, and gcd packets, not characteristic screening or duplicated
  norm construction.
- **deleted-pair final router:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_scalar_router`.
  After the constant ODE, Mobius router, Euclidean reconstruction, and
  harmonic exclusion, it removes `q_out` from the search. For the three
  printed pairs `(a_j,b_j)`, completion is exactly

  ```text
  4b_jT=a_jS^2,
  y=4b_j/a_j-2,       y notin {2,-2},
  y_(m+1)=y_m^2-2,       y_38=2,
  S/(1+q_out) is a nonzero square,       X^2-yX+1=0.
  ```

  The final square verdict is invariant under
  `q_out<->q_out^(-1)`. A contributor should implement three one-variable
  certifiers in `r`, not a two-variable torsion search.

  The stronger proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_fourth_power_router`
  removes even that root-independent `q_out` square verdict. With
  `chi=r+r^(-1)`, the three multipliers are the explicit squares

  ```text
  h_0^2=1/(4(chi-1)^2),
  h_1^2=(chi-2)^2/(4(chi+2)^2),
  h_2^2=chi^2/(4(chi-4)^2).
  ```

  Conditional on `T=(h_jS)^2`, the final square-pencil condition is exactly
  that `T` is a nonzero fourth power. This is the implementation endpoint.

  The first implementation stage begins with the proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_gate`,
  but its terminal quotient has now been eliminated by the stronger proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_legendre_collapse`.
  Define

  ```text
  H_n(t)=[z^n]((1-z)(1-tz))^(-1/2),       H=H_(4M-1)(t).
  ```

  Then `sigma=S(0)=2H`, and the three first-rejection gates are exactly

  ```text
  t H^2+(chi-1)^2=0,
  t(chi-2)^2H^2+(chi+2)^2=0,
  t chi^2H^2+(chi-4)^2=0.
  ```

  The sequence has the width-two recurrence

  ```text
  2(n+1)H_(n+1)=(2n+1)(1+t)H_n-2ntH_(n-1)
  ```

  and, for `t=r^4`, the Legendre form
  `H_n(r^4)=r^(2n)P_n((r^2+r^(-2))/2)`. A contributor should attack uniform
  torsion nonvanishing or provide a coverage-proved fast holonomic,
  diagonal, or cyclotomic-resultant evaluator. Do not reconstruct `R,S,T`,
  and do not iterate `2^37-1` recurrence steps for each torsion point.

  **Deferred large run CR-002-L (recorded for contributor compute).** Put
  `n=4M-1=2^37-1` and

  ```text
  K_n(t)=4^nH_n(t)
        =sum_(j=0)^n binom(2j,j)binom(2n-2j,n-j)t^j.
  ```

  After clearing the `r` and power-of-four denominators, the three branch
  polynomials are

  ```text
  B_0(r)=r^6K_n(r^4)^2+4^(2n)(r^2-r+1)^2,
  B_1(r)=r^4(r-1)^4K_n(r^4)^2+4^(2n)(r+1)^4,
  B_2(r)=r^4(r^2+1)^2K_n(r^4)^2
         +4^(2n)(r^2-4r+1)^2.
  ```

  The exact decision is whether any admissible official split-quadratic
  characteristic `p`, source order `ord(r)|2^40`, and branch `j` has
  `B_j(r)=0`, after applying the already proved distinctness, primary-gap,
  and characteristic filters. A negative result closes the scalar-gate
  portion of the generic deleted-pair sublane. A positive result must emit
  `(p,ord(r),j)` and the minimal common factor, then pass the existing full
  scalar, trace, gcd, and fourth-power checkers before it counts as a
  survivor.

  Source torsion must be inside the elimination ideal, not applied as an
  informal post-filter. The proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_primary_legendre_torsion_necessity_fence`
  gives one exact good-characteristic `M=1` primary-gap solution for each
  `B_j`; every row retains the required nonzero next coefficient, and every
  row fails `r^32=1`. Thus the pairwise primary/`B_j` resultant has genuine
  large-prime false-route hits. A contributor output that omits
  `r^(32M)-1` does not answer CR-002-L.

  The preferred lower-degree implementation is the proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_chebyshev_gegenbauer_sign_router`.
  Put `L=2M`, `y=(r+r^(-1))/2`, `x=2y^2-1`, and
  `epsilon=r^(8L)`. The coverage-equivalent system is

  ```text
  T_(8L)(y)=epsilon,       epsilon^2=1,
  C_L^(1/4)(x)=0,
  ```

  followed by one of

  ```text
  P_(2L-1)(x)=s(2y-1),
  P_(2L-1)(x)(y-1)=s(y+1),
  P_(2L-1)(x)y=s(y-2),       s^2=-epsilon.
  ```

  There are two sign choices in each line. These six unsquared systems are
  an exact intermediate endpoint; they retain source torsion and reduce the
  branch degree relative to `B_j(r)`.

  Apply the stronger proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_trace_gcd_router`
  before an official computation. Since `t!=1` forces `x^2!=1`, replace the
  torsion equation by

  ```text
  epsilon=-1: G_epsilon=T_(2L),
  epsilon= 1: G_epsilon=U_(2L-1).
  ```

  Put `C=C_L^(1/4)` and `R=P_(2L-1) mod C`. For each `s^2=-epsilon`, the
  three branch polynomials are

  ```text
  E_(0,s)=(R+s)^2-2s^2(x+1),
  E_(1,s)=2(R+s)^2-(x+1)(R-s)^2,
  E_(2,s)=(x+1)(R-s)^2-8s^2.
  ```

  Reduce `G_epsilon` and `E_(j,s)` modulo `C`. The exact official decision
  is now whether any of the six gcds

  ```text
  gcd(C, G_epsilon mod C, E_(j,s) mod C)
  ```

  is nontrivial in an admissible characteristic. Every representative has
  degree at most `L=2^36`. A PASS must provide compact Bezout or subresultant
  certificates for all six signs and every official characteristic class. A
  FAIL must print the common factor, reconstruct `y` using `(TGR6)`, and then
  replay the retained next-coefficient and downstream filters. A contributor
  may use the larger cleared `r`-polynomials as an independent checker, but
  should not make them the primary official-scale representation without a
  measured reason.

  Apply the proved even-Jacobi norm router before implementing this batch.
  With `L=2M`, `w=2x^2-1`, replace the primary polynomial by
  `J_M^(-1/4,-1/2)(w)`, replace the two torsion factors by `T_L(w)` and
  `U_(L-1)(w)`, and replace each signed trace polynomial `A_j+xB_j` by
  `A_j^2-((w+1)/2)B_j^2`. Reduce during construction. This is coverage-
  equivalent and lowers the maximum degree from `L=2^36` to `M=2^35`.
  It does not make a dense run affordable; the benchmark, certificate, and
  spending requirements below remain in force.

  **First external shard CR-002-J0 (torsion-only characteristic sieve).**
  Before constructing any of the six signed norm polynomials `F_(j,s)`,
  decide, without materializing them, whether either of the two
  primitive-integer cyclotomic resultants

  ```text
  R_- = Res_w(J_M^(-1/4,-1/2)(w), T_(2M)(w)),
  R_+ = Res_w(J_M^(-1/4,-1/2)(w), U_(2M-1)(w)),
  M=2^35.
  ```

  Consume the proved torsion cyclotomic-norm decomposition. For

  ```text
  H_M(z)=z^M J_M^(-1/4,-1/2)((z+z^(-1))/2),
  ```

  odd-prime screening of `R_-` is exactly screening the single norm
  `Res(Phi_(2^38),H_M)`. Screening `R_+` is exactly screening the `36`
  factors `Res(Phi_(2^j),H_M)`, `2<=j<=37`; these may be checked and
  short-circuited level by level. Their odd-prime valuations are twice the
  corresponding resultant valuations. A proposed implementation should
  target these modular norm pieces directly, not recover them from `R_+`.

  Equivalently, use the proved trace factorization

  ```text
  R_+=(2M)^M product_(j=0)^35 Res(J_M,T_(2^j)).
  ```

  Each trace factor is the square root of its cyclotomic norm level up to a
  printed power of two. This lowers the largest plus-branch torsion degree
  from `2M-1` to `M`; it does not make an explicit degree-`M` resultant
  affordable. A modular implementation may choose whichever of the paired
  trace and cyclotomic forms gives the cheaper independently checked shard.

  For the minus branch, use `theta^2=2` in the official field and

  ```text
  T_(2M)=(theta T_M-1)(theta T_M+1).
  ```

  The two degree-`M` resultants are Galois conjugates and their product is
  `R_-`; at official even `M`, either one has quadratic norm `R_-`. This also
  lowers the largest minus torsion degree from `2M` to `M`. Recursive trace
  splitting may be used for bounded-memory parallel shards, but it does not
  by itself reduce total work and is not authorization to enumerate roots.

  has an official-compatible prime divisor. Clear only the known powers of
  two from the Jacobi normalization and print the exact primitive numerator
  convention. A common root of any triple in
  `(EJN7)` first requires the official characteristic to divide `R_-` or
  `R_+`, according to its torsion sign. Thus:

  - **PASS:** certified modular/cyclotomic exclusion ledgers show that neither
    resultant has an official-compatible prime divisor. This closes all six
    deleted-pair trace-gcd branches before their signed norms are built.
  - **FAIL:** print every compatible `(p,epsilon)`, a compact factor
    certificate, and `gcd(J,K_epsilon) mod p`. Only these characteristic
    shards proceed to `F_(j,s)` and the downstream scalar/fourth-power gates.
  - **INCOMPLETE:** retain proved factors, cofactors, hashes, and interval or
    congruence exclusions; make no DAG status change.

  The route-selection pilot used exact rational resultants at small `M` and
  trial division only on the first three rows. The primitive numerator bit
  lengths are

  ```text
  M       8    16    24    32
  R_-   574  2411  5475  9910
  R_+   500  2244  5248  9541.
  ```

  They track roughly quadratically at these controls. Scaling the `M=32`
  ratios to `M=2^35` projects about `1.14e22` and `1.10e22` bits,
  respectively, or about `1.4e21` bytes for either integer. This is an
  empirical route-sizing observation, not a lower bound on the official
  resultants, but it decisively route-fences explicit integer output and
  factorization: an implementation must never form `R_-` or `R_+` as an
  integer.

  Under the standard Jacobi normalization its first exact primitive
  numerators include

  ```text
  M=1: R_-=-23,                       R_+=-1;
  M=2: R_-=3^4*47*39023,              R_+=3^3*17*47;
  M=4: R_-=5^8*7^8*97*641*33247*402078190242382847,
       R_+=3*5^7*7^9*13*97*182711*258045217.
  ```

  These are normalization and positive-factor controls, not scaling
  evidence. The official implementation must instead use a doubling
  recurrence, cyclotomic norm modulo candidate characteristics, or an
  equivalent coverage-proved compressed method. It must not materialize a
  dense degree-`2^35` polynomial or either integer resultant. First benchmark
  a power-of-two ladder and report asymptotic and measured cost per
  characteristic, total CPU/RAM/storage, aggregation strategy, and an
  explicit spending cap. The checker should verify the recurrence or norm
  certificate, primitive normalization, official field-ledger coverage, and
  any surviving modular common factors independently. Without such an
  algorithm and benchmark, CR-002-J0 is a theorem/algorithm request rather
  than a compute run; it is not authorized on the low-credit Modal account.

  The deterministic small control is vendored at

  ```text
  experiments/prize_resolution/cr002_j0_resultant_pilot.py
  ```

  and replays under `tools/ramguard tiny -- python3 <path>`.

  A responsible implementation should work by power-of-two cyclotomic norms
  modulo the official candidate characteristics or a comparably
  coverage-proved batch algorithm. It must emit compact recurrence,
  subresultant, or product-tree certificates with an independent streaming
  checker. An exhaustive root-by-characteristic
  sweep is specifically out of scope: the existing interval ledger contains
  `4,495,441` congruence moduli before primality, and each field can contain
  up to `2^40` source roots. Their Cartesian product has no reasonable cost
  envelope. The official batch is unauthorized here and likely well above
  the current sub-`$1` budget. Before requesting it, contributors must publish
  a small-order benchmark, a total CPU/RAM/storage estimate, a resumable
  shard plan, and a hard spending cap. Until then this item is a
  theorem/algorithm request, not a request to start containers.

  Apply the proved
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_fourth_root_gcd_gate`
  before extracting that fourth root. With

  ```text
  P=2N+kappa x^2U_0^3,
  ```

  every survivor satisfies `S|P^2` and `deg gcd(S,P)>=M-1`. A contributor
  should compute `P mod S`, its square modulo `S`, and a compact gcd-degree
  certificate. A proof that the gcd degree is always smaller than `M-1`
  closes this deleted-pair sublane without a fourth-power extraction.
- **pure harmonic first sieve:** before classifying any ramification passport
  or constructing the degree-`2^39` Fermat decomposition, consume the proved
  `rate_half_list_budget_three_antipodal_harmonic_torsion_characteristic_sieve`.
  The nondegenerate harmonic lift locus is empty in characteristic zero. At
  official lift order `2^40`, all finite survivors lie in the bad
  characteristics of one explicit unit ideal. Its pruned repeated-squaring
  presentation has `126` variables, `127` equations, and maximum degree
  three. An integer identity

  ```text
  Delta_H=sum_j H_jE_j,       Delta_H!=0,
  ```

  would confine the characteristic support exactly, but it is no longer an
  authorized first computation. The `F_97`, order-16 witness
  `(x,y,w)=(27,12,75)` confirms that finite bad characteristics are real.
  More importantly, exact aspect-ratio controls give nondegenerate normalized
  harmonic counts

  ```text
  N       16  32   64  128   256   512
  count    8  64  160  640  2040  5680,
  ```

  for primes scaled like `p approximately N^1.6`. At `N=512`, the count is
  `0.975` times the random main term `N^3/p`. The official relation
  `N=2^40`, `p approximately 2^64=N^1.6` has the same aspect and random main
  term about `2^56`. This is route-selection evidence, not a theorem about
  official primes, but it makes a characteristic-exclusion-only certificate
  unlikely to close the branch.

  Do not launch the `126`-variable Nullstellensatz computation merely to hope
  that its integer has no official divisor. First provide either a theorem
  showing official-aspect harmonic scarcity, or a certificate algorithm that
  couples harmonic lifts directly to the Fermat/passport equations. A
  surviving official
  characteristic must print `(p,x,y,w)`, replay the six distinct-square
  inverses and all `40` squarings, and only then proceed to the Fermat tests.
  The exact small control is
  `experiments/prize_resolution/rate_half_pure_harmonic_aspect_pilot.py`.

  The proved
  `rate_half_list_budget_three_antipodal_pure_harmonic_binary_quartic_norm_gate`
  now replaces relabelled cross-ratio tests by one support invariant. For the
  split deleted quartic `D`, its harmonic-lift resolvent is the product of the
  cubic binary-quartic invariant over eight sign classes. It is a symmetric
  degree-`24` polynomial in the four roots of `D`. Three iterated quadratic
  norms evaluate it exactly, and its factorization through the three harmonic
  pairings gives a short radical-free base-field formula. A guarded attempt
  to print the full symbolic expansion reached the tiny-local wall limit;
  this does **not** create a contributor compute request. The pairing norm is
  already the exact certificate, while a large coefficient expansion would
  neither exclude a support nor couple it to the Fermat equation.

  A valuable external harmonic computation must instead eliminate this
  compact support norm together with `Q=B^4+Z^4` or with one of the proved
  Euler/passport packets. Before launch it must provide a finite complete
  family, a succinct representation that avoids degree-`2^39` coefficient
  arrays, a measured pilot, total cost and storage ceilings, and a checker
  that emits either a Bezout/nonexistence certificate or a replayable matched
  support. Until such a coupling is specified, this remains a theorem and
  algorithm request rather than an authorized large run.
- **decision:** classify the saturated algebraic locus on which four
  pairwise-coprime monic quadratics `P_i=X^2+u_iX+v_i` satisfy

  ```text
  dim_(F(X^4)) span {1/P_0,1/P_1,1/P_2,1/P_3}=2.
  ```

  Determine whether the nondegenerate locus consists only of the antipodal
  component `u_0=u_1=u_2=u_3=0`, up to the exact scaling and permutation
  symmetries that preserve `F(X^4)`, or print every additional component.
- **algebraic input:** form `P=product_i P_i`, decompose each `P/P_i` in the
  basis `1,X,X^2,X^3` over `Z[u_i,v_i,Y]`, and impose every coefficient in
  `Y` of every `3 x 3` minor. Saturate by `2`, the four constant terms, the
  four discriminants, and all pairwise resultants. Any further normalization
  must come with a proved coverage map.
- **bounded pilot:** the complete pairing census over `F_13` has `50,856`
  rank-four, `1,104` rank-three, and `15` rank-two cases; all rank-two cases
  are antipodal. It runs in a few seconds with negligible memory and is
  vendored as an audit, but it is not a characteristic-free classification.
- **downstream posedness:** the antipodal component is already nonempty at the
  first nonconstant quotient boundary (`d=8` over `F_97`): an exact
  `26,880`-assignment census finds `192` algebraically valid Möbius-graph
  pencils.
  At arbitrary scale the proved descent and weld reduce it to

  ```text
  product_i(R+a_iS)=kappa (Y^d-1)/product_i(Y-a_i^2).
  ```

  Therefore an antipodal-only component classification does not close the
  rate-half node; it identifies this quartic norm equation as the remaining
  official-scale rigidity problem. Any follow-on symbolic attack on that
  equation must retain the odd-degree primitive condition and may discard
  quotient-pullback and four-coset components by theorem, with the discarded
  ideal factors named explicitly in its certificate. It must also parameterize
  only degree-drop directions in `2^36-2<=v<=2^37-2`; constant and low-degree
  translation components have already been excluded analytically. Split the
  outer-parameter ideal by `e_2`, then `e_3`: every `e_2=0` component must
  impose `v>=(2^38-4)/3`, and the `e_2=e_3=0` component must impose
  `v=2^37-2` together with the exact linear-residual Wronskian identity from
  the outset. In that pure component, require `U,V` squarefree and saturate
  away every branch with two roots of `UV` in `Z(D) union {0}`. None of the
  `192` exact `d=8` positives even has centered `e_2=0`.

  At the generic floor `v=2^36-2`, impose the exact linear identity

  ```text
  dDU-Y(D'U+4DU')=t_0+t_1Y
  ```

  and saturate away branches where `U` has two repeated, deleted-divisor, or
  zero roots. At the intermediate floor `v=(2^38-4)/3`, impose the analogous
  quadratic identity and saturate away branches with three such roots. Above
  either floor, separate components by the exact residual degree
  `r+4-q(r-v)`, which rises by `q` per added degree of `V`. A contributor run
  that omits these identities is not solving the posed downstream problem.

  The boundary identities now admit a stronger elimination and this should be
  used before introducing any coefficients of the official-degree `U`. Put

  ```text
  E(z)=product_(i=0)^3(1-b_i z),
  E(z)^(-1/4)=sum_(m>=0)a_mz^m,       b_i^d=1,
  s=2^37,       d=2^39.
  ```

  The monic `U` is uniquely the reverse of the truncation through `a_(s-1)`.
  A generic-boundary solution requires `a_s=a_(s+1)=0` and
  `a_(s+2)!=0`; an intermediate-boundary solution requires `a_s=0` and
  `a_(s+1)!=0`. The coefficients obey

  ```text
  4m a_m=-sum_(j=1)^4(4m-3j)eta_j a_(m-j),
  E=1+eta_1z+eta_2z^2+eta_3z^3+eta_4z^4.
  ```

  A valuable contributor-scale follow-on is an exact compressed
  nonvanishing/component certificate for these gaps on four distinct
  order-`d` roots, modulo common scaling and permutation, with the centered
  outer `q=2` and `q=3` conditions retained through the `a_i^2=b_i` lift and
  Möbius weld. PASS excludes the corresponding boundary; FAIL must print an
  admissible finite field, four roots, square-root lift, outer parameters, and
  replayable recurrence values. A point sample or a linear scan through
  `2^37` recurrence steps has no completeness claim. Use a compressed
  algebraic-series, diagonal, resultant, or cyclotomic representation and
  provide its coverage proof before a large run.

  In the generic `q=2` branch, the primary gap is only half of the posed
  certificate. Set `B=sum_(m=0)^(s-1)a_mz^m`, `h=2^36+1`, and

  ```text
  J=z^(-2h)(E^(-1)(1-z^d)-B^4)/B^2,
  P=(J/J(0))^(1/2),       P(0)=1.
  ```

  The normalized reverse of `V` is fixed by `P mod z^h`, and its degree
  `h-3` forces `[z^(h-2)]P=[z^(h-1)]P=0`. A generic-boundary PASS must exclude
  the simultaneous four vanishings

  ```text
  a_s=a_(s+1)=[z^(h-2)]P=[z^(h-1)]P=0,
  ```

  not merely the primary pair. A FAIL certificate must replay both nested
  series and then reconstruct the remaining outer-coefficient identities.

  The secondary series now has a cheaper exact interface. Write

  ```text
  d=8h-8,       r=2h-3,
  L=sum_(m<h)a_mz^m,       T=sum_(m<h)a_(2h+m)z^m.
  ```

  After `a_(2h-2)=a_(2h-1)=0` and `c=a_(2h)!=0`, the two secondary
  vanishings are equivalent to

  ```text
  L T=c C^2 mod z^h,       C(0)=1,       deg C<=h-3.
  ```

  The full shifted tail also satisfies the proved first-order equation

  ```text
  E'B+4EB'
    =-z^(2h-1)((zE'+8hE)T_hat+4zE T_hat'),
  ```

  whose parenthesized forcing has degree at most one. A contributor
  implementation should use this square-plus-differential gate before the
  canonical span test; it should not build the nested square root or either
  official-degree polynomial. A rejected packet may print the first failed
  square coefficient. A survivor must print the two coefficient windows,
  `c`, the normalized square root, and the two linear-forcing coefficients.

  Before the canonical span, apply the generic Euler divisor gate. Reverse
  the canonical truncations to monic `U,V`, form the linear residual

  ```text
  T=dDU-Y(D'U+4DU'),
  ```

  write `T=t_1(Y-tau)`, and first apply the scalar norm gate

  ```text
  t_1^2V(tau) in (F^*)^3.
  ```

  For a base field of order `q=1 mod 3`, certify this by exponentiation to
  `(q-1)/3`; when `q=2 mod 3`, skip it because cubing is bijective. A scalar
  rejection certificate needs only the canonical field, `t_1,tau,V(tau)`,
  and the cubic-character value.

  Next compute

  ```text
  N_T=Res(V,T),       N_Q=Res(V,(Y^d-1)/D).
  ```

  Require `N_Q` to be a fourth power and require the exact coupling

  ```text
  N_T^4N_Q^3=d^(4v).
  ```

  Use subgroup products or compressed resultants; do not expand the
  degree-`d-4` quotient. The certificate prints both norms, their character
  values, and the coupling residual. A coupled scalar survivor must then
  certify

  ```text
  (TU^3+d) mod V=0.
  ```

  Evaluate `U^3 mod V` in a compressed quotient-algebra representation and
  multiply by the linear `T`; do not materialize `TU^3+d`, whose degree is
  `6*2^36-2`. A remainder rejection certificate prints a hash-pinned nonzero
  remainder. Passing either gate is only a necessary-condition hit and
  continues to the span and split/Mobius stages.

  Shard any contributor implementation by the proved maximal-field character
  table. Over the ambient field, the fourth-power test is active in every
  branch. The cubic test is active in every quadratic-extension branch and in
  the prime-field `p=1 mod 3` branch; only prime-field `p=2 mod 3` packets
  skip it. A specialized packet whose data have been proved to descend from
  `F_(p^2)` to `F_p` must recompute both characters over `F_p`. The shard
  manifest must name the field in which each character was evaluated.

  There is now an exact deterministic reconstruction for that last step. Put

  ```text
  Q=(1-z^d)/E,                 Rbar=z^(-2h)(Q-B^4),
  alpha=Rbar(0),               Cbar=P mod z^h,
  S=Rbar-alpha B^2Cbar^2,
  X=z^hBCbar^3,                Y=z^(2h)Cbar^4.
  ```

  A complete generic candidate must satisfy `S=beta X+gamma Y`, where
  `beta=[z^h]S` and `gamma=[z^(2h)](S-beta X)`, and the centered quartic
  `W^4+alpha W^2+beta W+gamma` must split into four distinct parameters with
  the Möbius matching to square-root lifts of the `b_i`. The contributor run
  should therefore stream-reject in this order: primary gaps, secondary gaps,
  Euler cubic norm, Euler fourth norm, norm coupling, Euler remainder, full
  span equality, quartic splitting, Möbius matching. It must use compressed
  reversals and never materialize or retain official-degree `U,V` coefficient
  arrays.

  Common subgroup scaling preserves the certifier, so normalize one `b_i=1`;
  quotient by permutations as well. The certificate must include the inverse
  orbit-coverage counts. PASS means every normalized orbit rejects at one
  named stage. FAIL prints the first complete passing orbit and all compact
  canonical data. Prefix agreement in the span test is not a PASS.

  A bounded order-64 pilot (`ap-wLXZpGxaBiBlZ1NZ3MP14e`) exhausts all
  `C(64,4)=635376` quadruples over each of the first eight primes above the
  deliberately strong threshold `p>=64^2`, `p=1 mod 64`. It finds no primary
  double gap, although six fields contain between `64` and `192` single gaps.
  The `p=193` positive control reproduces all `64` members of the known
  double-gap scaling orbit and already has `p>d`. The square threshold is not
  a uniform official hypothesis: the maximal-row quadratic field branch has
  only `p>2^64` at `d=2^39`. The
  hash-pinned result and checker are
  `experiments/prize_resolution/rate_half_list_order64_primary_gap_result.*`.
  Do not turn this into a large fixed-order prime sweep: no proved transport
  makes additional order-64 fields complete for the official growing-order
  question. The valuable large request is the compressed, coverage-proved
  simultaneous-gap/span certificate above.

  A final bounded order-128 route pilot
  (`ap-K60XbR1aXkETENbT2n7A4b`, with orbit classifier
  `ap-CxjRuOXnLkrszE6llB1U4m`) exhausts all `C(128,4)=10668000`
  quadruples in each of the first eight split prime fields. Only `p=257` and
  `p=641` contain primary double gaps, with `192` packets apiece, and no
  packet passes the secondary two-window gate. Modulo common subgroup scaling,
  each positive field has one orbit of size `128` and one orbit of size `64`;
  the size-`64` orbit is two deleted antipodal pairs. The hash-pinned evidence
  packet is `experiments/prize_resolution/rate_half_list_order128_two_window_result.*`.
  This is the last justified raw fixed-order sweep. It selects a parity-
  reduced one-parameter sublane for algebraic treatment but supplies no
  transport to official order. Contributors should spend additional compute
  only on the coverage-proved symbolic request above, not on more primes or
  larger fixed orders.

  That sublane now has a proved exact router. If the deleted roots are two
  antipodal pairs and `d=16M`, normalize their squared ratio to
  `t in mu_(8M)\{1}`. One primary and one secondary zero are automatic; the
  remaining gate is `F_(2M)(t)=G_M(t)=0` with `F_(2M+1)(t)!=0`, where the
  `F_j` obey a second-order recurrence and `G_M` is one terminal coefficient
  of a length-`M+1` square root. A useful symbolic contributor subtask is a
  characteristic-explicit Bezout, resultant-factor, or torsion-nonvanishing
  certificate for this pair at symbolic `M`. A table of fixed `M` gcds is not
  the requested output and does not authorize a large recurrence campaign.

  The complete canonical survivor has a still stronger exact interface.
  Parity forces `beta=0` and gives

  ```text
  (1-w^(8M))/((1-w)(1-tw))
   =(B_0^2+lambda w^(2M+1)C_0^2)
    (B_0^2+mu     w^(2M+1)C_0^2),
  ```

  with two coprime degree-`4M-1` factors partitioning the undeleted torsion
  roots. This two-cell primitive square-pencil classification is the preferred
  contributor subtask: determine every possible root-cell partition under
  the displayed form, then impose the existing nonperiodic and Möbius-matching
  gates. The inverse-root cells have identical Fourier moments through
  frequency `2M`, and their first difference at `2M+1` is exactly
  `-(2M+1)(lambda-mu)`. A symbolic classification or prefix-flatness
  transcript has a DAG outcome; enumerating the `8M` roots or constructing
  official-degree factors does not.

  A proved primitive-resultant bound now removes the prime-field and nonsplit
  quadratic branches from this deleted-pair subtask. Any contributor
  classification should therefore work only in the split quadratic branch
  `q=p^2`, `p=1 mod 2^40`. A campaign covering either eliminated branch is
  obsolete. All quotient-pencil factors, outer parameters, and Möbius data in
  the surviving branch descend to `F_p`; an implementation should use
  `F_{p^2}` only for the full evaluation-domain check. The ordinary four-root
  orbit and the non-generic boundary strata remain separate CR-002 work.

  On the deleted-pair generic sublane, eliminate the generic direction before
  any CAS component calculation. In original half-degree coordinates every
  complete packet has

  ```text
  D=D_0(Y^2),       U=YU_0(Y^2),       V=V_0(Y^2),
  (16M-4)D_0U_0-2xD_0'U_0-8xD_0U_0'=kappa.
  ```

  For fixed monic quadratic `D_0`, the displayed constant-forcing ODE has at
  most one monic polynomial solution `U_0`; its coefficient recurrence has
  one terminal equation. Generate `U_0` from that recurrence and reject at
  the terminal equation before introducing `V_0,lambda,mu`. Preserve the
  forced simple root `U(0)=0`, but saturate away every second repeated,
  deleted-divisor, or zero root. A contributor transcript that allocates an
  independent official-degree `U`, or saturates away the zero root, does not
  cover the proved sublane.

  The outer ratio is no longer a free scalar either. Normalize the four
  deleted-root lifts to `(1,iota,r,iota r)`, put `q_out=mu/lambda`, and split
  the classifier into exactly the three reciprocal branches

  ```text
  r^2(1+q_out)^2=4q_out(r^2-r+1)^2,
  (r-1)^4(1+q_out)^2=4q_out(r+1)^4,
  (r^2+1)^2(1+q_out)^2=4q_out(r^2-4r+1)^2.
  ```

  For fixed `r`, each branch determines at most one unordered
  `{q_out,q_out^(-1)}`. Do not enumerate 24 point matchings and do not divide
  by `1+q_out`: the harmonic `q_out=-1` cases are retained by the cleared
  router equations. The official harmonic-exclusion theorem then removes
  all of them: app `ap-YVKd2kCRyMVnpUDLR9id5x` checked every one of the
  `4,495,441` exact characteristic congruence classes with no trace-recurrence
  hit. Allocate no `q_out=-1` shard. Impose `q_out^N=1` before any remaining
  polynomial solve; the two monic root-cell factors prove this from their
  constant terms.
  A complete contributor certificate should identify the selected pairing
  branch before applying the remainder-square router.

  In fact, do not solve for either of those objects. Once the ODE has produced
  `U_0`, form

  ```text
  Q=(x^N-1)/D_0,       A=xU_0^2,       R=Q-A^2.
  ```

  For `q_out!=-1`, Euclidean division `R=AS+T` is a complete router. Do not
  retain `q_out` as a variable. For pairing `j`, impose the exact identity
  `4b_jT=a_jS^2`, recover `y=q_out+q_out^(-1)=4b_j/a_j-2`, and apply the
  38-step trace gate above. The valuable contributor task is a compressed,
  coverage-proved uniform rejection of these three one-variable tests,
  followed by one exact fourth-power certificate for `T`. Allocating
  coefficients of `V_0`, sampling square prefixes, materializing `x^N-1`,
  sharding harmonic data, constructing `q_out`, duplicating reciprocal roots,
  or running the old polynomial-square test is obsolete.
  Before allocating full Euclidean data, reject at `(CCG3)` using the one
  terminal reversed-quotient coefficient. Only then reject unless `S|P^2` and
  `deg gcd(S,P)>=M-1`; compute these through modular remainders rather than a
  dense square. A PASS certificate for uniform nonexistence may consist of a
  coverage-proved strict gcd upper bound on all three scalar branches.

  The intermediate `q=3` floor now has a root-free preferred endpoint. In
  original coordinates form the canonical `U`, the exact quadratic residual

  ```text
  T=dDU-Y(D'U+4DU'),
  P=TU^3+d,       W=T'U+3TU'.
  ```

  **CR-002-I: RESOLVED ANALYTICALLY; DO NOT RUN.** Define

  ```text
  A=4YDT'+3T(dD-YD'),       J=dA^3+27T^7.
  ```

  The exact identity `4YDW=UA-3T^2` proves

  ```text
  gcd(P,W)|J,       deg J=18.
  ```

  But a survivor would force `deg gcd(P,W)>=(2^38-4)/3`. Hence the maximal
  intermediate boundary is empty. No holonomic, subresultant, modular, dense,
  or official-field run is needed; contributors should spend no compute on
  CR-002-I.

  The same annihilator closes the first higher-degree band. If
  `t=deg T=3v-2r+4>=5`, then `deg J=7t`, so a survivor requires

  ```text
  10v>=7r-14,       v>=96,207,267,429.
  ```

  Do not run any intermediate experiment for
  `v<=96,207,267,428`; all `4,581,298,449` degrees from the official floor
  through that endpoint are proved empty. The interval above
  `96,207,267,429` is not yet a ready large-compute request: first derive a
  new compression or annihilator that can decide degrees where `7 deg T`
  reaches `v`.

  The compact Hensel certifier remains below only as an audit trail and small
  analogue decoder. With `h=(2^37+1)/3`, form

  ```text
  Rbar=z^(-3h)(Q-B^4),       theta=Rbar(0),
  H=Rbar/(theta B),          C_*=H^(1/3),
  Delta=[z^(h-1)]C_*^2/B,   kappa=[z^(2h-1)]C_*,
  Delta_1=[z^h]C_*^2/B,     kappa_1=[z^(2h)]C_*,
  Delta_2=[z^(2h)]C_*^2/B,  Gamma_1=[z^h]C_*^3/B^2,
  kappa_2=[z^(3h)]C_*,       Delta_3=[z^(3h)]C_*^2/B,
  Gamma_2=[z^(2h)]C_*^3/B^2, Xi_1=[z^h]C_*^4/B^3,
  kappa_3=[z^(4h)]C_*.
  ```

  Stream-reject `Delta=0,kappa!=0`. If `Delta!=0`, test only the unique
  `u=3kappa/Delta` and require
  `u^2-uDelta_1+3kappa_1=0`. If `Delta=kappa=0`, test only the at-most-two
  base-field roots of `X^2-Delta_1 X+3kappa_1`; there is no longer a
  parameterized scalar branch. Reduce

  ```text
  81kappa_2-27uDelta_2+27u^2Gamma_1-35u^3
  ```

  modulo that monic quadratic and apply the printed linear gate `A u+B=0`.
  If `A!=0`, test only `u=-B/A`; if `A=0,B!=0`, reject. Only `A=B=0`
  reaches the next gate. Reduce

  ```text
  243kappa_3-81uDelta_3+81u^2Gamma_2-105u^3Xi_1+154u^4
  ```

  by the same quadratic and apply `C u+D=0`. On `A=B=0`, if `C!=0` test
  only `u=-D/C`; if `C=0,D!=0`, reject. Two roots remain only on
  `A=B=C=D=0`. A survivor must make the unique solution of

  ```text
  H=C_u^3(1+u z^h C_u/B)
  ```

  a polynomial of degree at most `2h-2`. The exact cube-part form is likewise
  retained for audit and reuse outside the now-closed maximal boundary:

  ```text
  Rbar=theta C_u^3(B+u z^hC_u),
  C_u^2 | gcd(Rbar,Rbar'),
  C_u | gcd(Rbar,Rbar',Rbar'').
  ```

  For each normalized cube divisor `C`, the exact cofactor test is

  ```text
  Rbar/(theta C^3)-B=u z^hC.
  ```

  Do not materialize dense official-degree polynomials or extend the Hensel
  coefficient hierarchy one term at a time. The degree-eighteen annihilator
  has already rejected every official maximal-intermediate candidate before
  this cofactor or its split/Mobius matching can arise.

  The pure `q=4` floor must use the harmonic-Fermat router. Choose lift signs
  `a_i^2=b_i`, quotient by common scaling and relabel to a harmonic ordering,
  then normalize `a_0=1` and generate

  ```text
  w=(2x-y(1+x))/(1+x-2y),       x^(2d)=y^(2d)=w^(2d)=1.
  ```

  Reject equality or antipodality among the four lifts. For every surviving
  orbit, test the exact coprime decomposition

  ```text
  Q=(1-z^d)/E=B^4+Z^4,
  B(0)=1,       ord_0Z=1,       deg B,deg Z<=2^37-1,
  ```

  together with the proved squarefree and linear-Wronskian constraints.
  Harmonicity itself is not a rejection stage: complete lift-subgroup scans at
  orders `16,32,64,128` already contain `4,40,500,3660` normalized harmonic
  sets. PASS must exclude the matched Fermat decomposition for every harmonic
  orbit; FAIL prints the lift orbit, `B,Z`, factor assignment, and Wronskian
  replay.

  Equivalently, and preferably for implementation, evaluate the proved
  binary-quartic support norm before selecting an ordering. A nonzero norm
  rejects all eight lift-sign classes at once. A zero norm prints one
  vanishing invariant factor and only then enters the Fermat and passport
  checks. Do not request or materialize the expanded degree-`24` symmetric
  polynomial; the three radical-free pairing norms, or independently the
  three-step quadratic-norm transcript, are the canonical certificates.

  The proved harmonic spectral quadratic gate now couples this test directly
  to the Euler reconstruction. If

  ```text
  D_Phi=(Y^2-SY+q)(Y^2-TY+u),
  ```

  one short difference-of-squares expression in `S,q,T,u` is exactly the
  eight-sign norm for that pairing; test the three quadratic splittings after
  the degree-four spectral gcd and fourth-power quotients. A contributor
  implementation should use this combined packet. Separate lift searches,
  cross-ratio scans, and support-resultant expansions are now redundant and
  should not be proposed as large runs.

  The complete `d=8,16` toy pilot finds no combined survivor in seven
  admissible field rows. Do not extrapolate this into a raw larger-order
  fleet: its `d=16` fourth-power reconstruction relies on `r=3<4`, where the
  first three coefficients determine `B` before `Z^4` begins. A contributor
  request at larger `r` first needs a complete uniform reconstruction or
  recurrence that resolves the overlapping `B^4` and `Z^4` coefficients.

  Convert every pure candidate to the exact Euler ramification packet before
  any official-degree coefficient elimination:

  ```text
  T=dDU-Y(D'U+4DU'),       C=4YD V'+V(YD'-dD),
  TU^3+d=e_4V^3C,
  T'U+3TU'=V^2L,          deg L=1.
  ```

  Verify the equivalent derivative identity
  `(TU^3)'=U^2V^2L`. Reject a nonlinear `L`, a second repeated-factor
  defect, or a critical value outside `{0,-d,(TU^3)(root(L))}`. A positive
  packet should encode the factorization and the linear critical factor,
  rather than materialize a dense second-derivative Wronskian. The remaining
  classification must still retain `D`, the harmonic lift matching, and the
  Fermat factor assignment.

  Apply the proved ramification-passport router next. Check the exact weld
  `Lambda=dL`, then label the packet as one of: `generic`, `U-T`, `double-T`,
  `V-C`, or `double-C`. The first is an almost-Belyi family with one moving
  simple branch value; the other four are exact Belyi passports. An
  official-degree enumeration of covers with these passports is not an
  authorized or useful large run. A valuable contributor computation would
  instead produce a symbolic uniform parametrization or recurrence that keeps
  the harmonic lifts and deleted quartic visible, with an independent
  coverage proof. Record such a proposal here with a cost estimate before
  launching it.

  For any proposed symbolic passport family, do not allocate `D,U,V`
  independently. From `Phi=sum phi_mY^m`, form the succinct Euler lift

  ```text
  S=1+sum_m phi_m/(d-m)Y^m
  ```

  and certify `deg gcd(S,Y^d-1)=4`, together with the two fourth-power
  quotients `(Y^d-1+S)/D` and `-S/D`. A contributor run is valuable only if
  it implements these operations on a recurrence, straight-line program, or
  comparably succinct cover representation and prints an independently
  checkable coverage certificate. Materializing `2^39` coefficients or
  launching a generic dense gcd is explicitly out of scope.

  Do not launch a raw harmonic-pair enumeration at official order without a
  compressed subgroup router and an orbit-coverage certificate.
- **required certificate:** a Groebner/regular-chain/primary-decomposition
  transcript over `Z[1/2]` or a justified characteristic-zero base; explicit
  saturated component ideals; nondegeneracy witnesses; and, for each claimed
  symmetry reduction, a machine-checkable inverse coverage map.
- **checker:** an independent exact script must verify ideal containment in
  both directions after saturation, replay every component parametrization,
  and check that discarded components lie in a named discriminant or
  resultant divisor. Probabilistic modular reconstruction alone is
  insufficient.
- **DAG outcome:** an antipodal-only result proves that the welded quartic norm
  equation is the complete direct fiber-four residual. Additional components
  become a finite, printed list of separate algebraic subcases and must each
  be transported to its own subgroup-product equation. A counterexample to
  the proposed component list repairs the classification target but does not
  affect the already-proved rank-three and rank-four exclusions. On the
  antipodal component, a useful next certificate must address the primitive,
  nonperiodic high-degree locus; a quotient-periodic or low-degree-translation
  census has no remaining DAG outcome. A pure-quartic certificate with
  `v<2^37-2` is likewise incompatible with the proved Wronskian theorem.
  Generic- or intermediate-boundary output with residual degree other than
  one or two, respectively, is incompatible with the proved reverse-residual
  theorem and must be treated as a generator or normalization error.
- **execution shape:** use a contributor machine or capped remote CAS job;
  checkpoint elimination stages and export compact bases plus hashes. Do not
  materialize large artifacts in WSL.
- **estimated resources:** unknown until a modular pilot; potentially
  multi-gigabyte and therefore outside the current laptop and sub-`$1` Modal
  policy.

A raw `d=16` or larger antipodal point census is not a third compute request.
The `d=8` positives already defeat scale-free emptiness, while a finite larger
negative cannot certify the official `d=2^39` quartic norm equation. Such a
run becomes responsible only after a proved lifting/classification theorem
makes a bounded range complete.
