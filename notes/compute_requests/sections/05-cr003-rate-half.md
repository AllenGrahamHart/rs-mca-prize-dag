
## CR-003: Rate-half Hankel sharp-cap component classification

- **status:** PRE-REQUEST; THE FORMER EXACT DISTANCE-THREE FACE IS CLOSED.
  Do not run on the
  current laptop or the remaining low-credit Modal account. It is not yet a
  contributor-ready numbered run under this ledger's handoff convention:
  there is no coverage-complete implementation, measured pilot, hard resource
  ceiling, or compact nonexistence certificate. The exact contract below is
  algebraic preprocessing for such a request, not authorization to search.
- **consumer:** `rate_half_band_closure`, at strict budget `B=2^39` and
  half-distance budget `B=2^39+1`.
- **official field collapse:** both budgets are prime-field only. The proved
  `rate_half_residual_prime_field_collapse` reduces `q=p^f` by LTE to
  `f in {1,2,3,4}`, then exactly excludes all `46` quadratic candidates and
  the empty cubic/quartic residue intersections. Every official shard may
  assume `F=F_p` with `p=q>2^167`. Do not allocate extension-field,
  Frobenius-orbit, generated-field, or base-field-normalization variants.
- **proved routers:**
  `rate_half_ca_hankel_strict_a3_slope_slack_ledger` and
  `rate_half_ca_hankel_half_distance_a3_slope_slack_ledger`, together with
  `rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger`. At the
  official scale the counterexample families are indexed by

  ```text
  strict:         m<=e<=floor((4m-1)/3),  0<=h<=4(e-m),
  half-distance A=3:  m+1<=e<=floor((4m-1)/3),
                                            0<=h<=4(e-m)-1.
  half-distance A=1:  s in {0,1,2},
                      m+1<=e<=floor((4m-s)/(1+s)).
  ```

  This request concerns only `h=0` for `A=3` and `ell=0` for `A=1`. In both
  `A=3` shapes the generator is a degree-`e` rational normal kernel curve of
  exact separation rank `e+1`, its norm residual has degree at most `e`, at
  least `N-e` domain rows are saturated, and every geometric component degree
  is forced by a unique possible integer chamber. The strict matrix is
  `(4m+1) x 4m` with a unique right singular block and locator degree `rho`;
  the half-distance matrix is `4m x (4m+1)` with a unique left singular block
  and locator degree `rho+1`. In the latter case the degree-`rho` split
  `Q_gamma` is a factor of the locator with one additional distinct domain
  root. The `A=1` matrix has the same dimensions but full row rank `4m`, one
  right singular block, and a fixed core `s in {0,1,2}`. Its residual
  sharp-cap and norm degree are the exact `T_max,eta` of `(A1L4)--(A1L5)`.
- **decision:** for the complete analogues

  ```text
  m in {2,4,8,16},       N=16m,
  A=3: rho=4m-1, strict m<=e<=floor(rho/3),
       half-distance m+1<=e<=floor(rho/3), T=4e+1;
  A=1: rho=4m, s in {0,1,2}, d=rho-s,
       m+1<=e<=floor(d/(1+s)), T=T_max(s,e),
  ```

  and, for each `m`, the first three prime fields in increasing order with
  `N|(q-1)` and `q>N`, decide separately for each shape whether a syndrome
  Hankel pencil exists with the designated generic rank, minimal index `e`,
  no common degree-`r` domain-split locator, exactly `T` supported finite
  slopes, and exactly the designated fixed core (`s=0` for `A=3`). The solver
  must impose the appropriate Hankel coefficient chain, not merely search
  arbitrary biforms satisfying the norm identity.

### First meaningful analogue and raw-search fence

The smallest fixture already banked has `e=1,r=3,N=16` over `F_17`; it is a
positive route fence below the proved uniqueness threshold. The next useful
distance-three analogue on the maximal `A=1,s=1,e=2m-1` face is

```text
m=2,       e=3,       r=7,       N=32,       F=F_97.
```

After multiplicative normalization fixes the core point, there are still

```text
31 omitted rows x C(30,6) exceptional supports
  = 18,407,025 (x_0,A) packets,

31 x C(30,6) x C(24,3)
  = 37,255,818,600 (x_0,A,B) support packets.
```

Allocating the `15` perfect matchings of the six roots of `A` would inflate
this to `558,837,279,000` records. These are exact lower-level candidate
counts, not resource estimates, and they make a raw support or pairing fleet
unacceptable. A future implementation must apply the quadratic-character,
matching-free even-value polynomial, triple-power, and dual row-product
routers before reconstructing matchings or slope parameters. It should group
equal field signatures and stream only survivors.

A valid first pilot must report per-gate survivor counts for every one of the
`31` normalized omitted-row shards, preserve partial counts on timeout, and
replay the existing `e=1,F_17` positive fixture before claiming that a gate is
sound. PASS here means only that the compiler exhausts the first analogue and
emits either witnesses or a checkable no-hit certificate. A no-hit result is
route-selection evidence; it cannot close the official seam. A witness may
falsify an over-strong proposed exclusion but is not automatically an
official counterexample. Until source, pilot timing, RAM/storage ceilings,
and an independent certificate checker are banked, contributors should be
asked to help implement the compressed classifier rather than donate a raw
run.

A separate strict-`A=3` `m=1` fixture is now banked in
`rate_half_ca_hankel_strict_m1_corefree_five_slope_route_fence`: its
core-free constant-rank pencil has five split slopes against cap four, and a
complete `560`-locator census finds sixteen such Hankel-compatible lines.
This fixture is rank-two/separated and therefore not a model for the official
mixed component, but any proposed generic preprocessing gate must either
accept it or name the proved `m>1` rank/non-pullback input that excludes it.
No larger strict raw census is requested: without an official-scale
mixed-component classifier it would be evidence only.

- **preprocessing contract:** enumerate only component degree packets allowed
  by `(SSL19)--(SSL20)` or `(A1L14)--(A1L15)` and summing to the corresponding
  residual bidegree. Use the exact norm residual, complementary factorization,
  and clean-column count as early rejection constraints. Quotient by
  parameter `PGL_2`, common polynomial scaling, and cyclic domain
  automorphisms only with an inverse coverage map.
  On the `A=1,s=1,e=2m-1` sharp-cap face, impose the stronger proved packet:
  exactly one component has `(r_*,e_*)=(2e_*+1,e_*)`, every residual
  component has `(r_i,e_i)=(2e_i,e_i)`, their total parameter degree is at
  most `floor(e/5)`, and the dominant component has separation rank at least
  `ceil((e+1)/(b+1))`. Do not allocate shards to rank-at-most-four models on
  this face. Its contracted middle-Hankel matrix also satisfies the proved
  exact identity `adj M=lambda*q*q^T`, with one common linear factor and no
  other projective rank drop. A shard must divide the nonzero maximal minors
  by that same `lambda` and verify every quotient `q_iq_j`; do not treat the
  cofactors as independent elimination variables. For a surviving dominant
  component, impose its exact component norm identity with residual degree
  `e-5b-1+D_*`, `D_* in {0,1}`, and its complementary factorization over at
  least `14m+5b` residual domain rows. Output that component certificate
  separately from the balanced residual components, whose norm residual
  degrees are exactly `5e_i+D_i`. Finally impose the proved two-sided weld

  ```text
  W B-B_X E_Z=Q_* K,       V B+A E_Z=-P_X K,
  ```

  with the printed degree boxes. The external decision is now classification
  of this coupled matrix factorization together with
  `adj M=lambda*q*q^T`; independent searches for cofactors, norm factors, and
  complements are obsolete on this face. The current live handoff is:

  ```text
  B_X=X_0X_1,
  QV_a+P_XW_a=P,

  D_*=0:
    QA_a+P B_a=P_XX_1,
    W_aB_a-X_1=QK_a;

  D_*=1:
    QA_a+P_cl B_a=P_XX_1,
    W_aB_a-X_1E_Z=QK_a,
    K_a(gamma_0;X)!=0.
  ```

  Every root of `X_1` has a nonzero domain trace. Either `X_0=1`, or exactly
  one of the following boundary normalizations applies:

  ```text
  b=0,D_*=1,c=1: X_1=1 and the exceptional trace is active;
  b=0,D_*=1,c=2: X_1 has one active root with delta=1.
  ```

  The `c=1` exceptional-only boundary has a stronger proved endpoint and must
  not be sent as the generic active system above. Put `E=E_Z` and
  `q_0=Q(gamma_0;X)`. Then `q_0|P_X`, and the unique polynomial

  ```text
  J=B(gamma_0;X)/q_0,       deg J=D_0-r,
  ```

  gives the exact descended system

  ```text
  B=QJ+E B_1,       A_1=A+P_clJ,
  QA_1+PB_1=P_X,
  WB_1-1=QK_1,
  VB_1+A_1=-P_XK_1,
  deg_X A_1=D_0-r.
  ```

  A contributor shard should classify this corrected complement square
  directly. It must retain the final equality: the one-degree relaxation
  from `D_0-r-1` to `D_0-r` is why the trace-free exclusion does not close
  the profile. Do not allocate the old exceptional-only active-trace system
  or claim the trace-free contradiction after silently dropping `P_clJ`.

  Normalize the infinity block before allocating any remaining coefficients.
  With `q_inf=[X^r]Q=E q_bar`, `j_inf=[X^(D_0-r)]J`, and
  `v_inf=[X^(D_0-2)]V`, impose

  ```text
  [X^(D_0-r)]A_1=P_cl j_inf,
  [X^D_0]B_1=-j_inf q_bar,
  [X^(r-1)]W=-E q_bar v_inf,
  [X^(D_0-1)]K_1=j_inf q_bar v_inf.
  ```

  Hence `A_1` and `B_1` have exact corners `(D_0-r,T-1)` and
  `(D_0,e-1)`. Eliminate those four leading coefficients from the solver.
  Do not retain the old `deg_X B<=D_0-1` box after descent: the corrected
  `B_1` has exact `X`-degree `D_0`. The optional `v_inf` may be zero.

  Before any Hankel elimination, also require the compact two-sided
  resultant certificate. With `n_X=D_0-1`, print nonzero `c_t,c_X` and check

  ```text
  Res_t(P,Q)=c_tP_X^e,
  Res_t(P,A_1)=c_t^(-1)P_X^(T-e),
  Res_X(P_X,Q)=c_XP_cl^rE^(r-1),
  Res_X(P_X,V)=c_X^(-1)P_cl^(n_X-r)E^(n_X-r+1).
  ```

  Use product trees or subresultant certificates; do not materialize all
  official fibers merely to multiply them. A failed identity rejects the
  shard. Passing all four remains only preprocessing and does not certify the
  Hankel chain or irreducibility.

  Reduce the unit-intersection calculation further. Reuse the same `c_X`,
  put `[X^r]Q=E q_bar`, and let `m=deg_XW` after checking whether the optional
  infinity coefficient vanishes. Require

  ```text
  Res_X(Q,B_1)=c_X q_bar,
  Res_X(Q,W)=c_X^(-1)E^(m+n_X+1)q_bar^(m+n_X).
  ```

  The first resultant has degree only `e-1` in the parameter and is the
  preferred common-fiber certificate. A shard with any other irreducible
  resultant factor is invalid. Do not force `m=r-1` when `v_inf=0`, and do
  not infer that `q_bar` is root-free from this identity.

  Apply one reciprocal Euclidean step before allocating any lower
  coefficients. At the proved fixed degrees put

  ```text
  F(t,Y)=Y^rQ(t,1/Y),       G(t,Y)=Y^D_0B_1(t,1/Y),
  j_infF+EG=YL,
  Delta_inf=L(t,0)=j_inf[X^(r-1)]Q+E[X^(D_0-1)]B_1.
  ```

  Require the exact compact certificate

  ```text
  Res_Y(F,L)=c_XE^(r-1),       gcd(q_bar,Delta_inf)=1.
  ```

  The complete `q_bar` factor is thereby removed before the classifier:
  any nonexceptional irreducible factor in `Res_Y(F,L)`, or any common
  factor of `q_bar,Delta_inf`, rejects the shard. Use a subresultant or
  product-tree certificate; do not enumerate official fibers. Retain the
  exceptional `E`-supported contact and continue with the Hankel and
  splitting gates, since this reciprocal descent is necessary but not an
  exclusion.

  Do not allocate `Delta_inf` as a free coefficient. With

  ```text
  a_minus=[X^(D_0-r-1)]A_1,
  ```

  impose the proved leading Bezout ledger

  ```text
  P_clDelta_inf+E q_bar a_minus=1.
  ```

  Equivalently, compute `Delta_inf=P_cl^(-1) mod (E q_bar)` and retain
  `a_minus` as the quotient certificate. Reject immediately if either gcd
  with `E q_bar` is nontrivial or the exact polynomial identity fails. This
  modular inversion is preferred to adding coefficient variables or
  evaluating every official fiber.

  Use the full reciprocal complement rather than continuing coefficient by
  coefficient. Define

  ```text
  A_vee=Y^(D_0-r)A_1(t,1/Y)=P_clj_inf+YU,
  R_X=Y^(D_0-1)P_X(1/Y),
  ```

  and require

  ```text
  FU+P_clL=R_X.
  ```

  A shard should allocate `F,U`, test the coefficientwise divisibility
  `P_cl | (R_X-FU)`, and recover `L=(R_X-FU)/P_cl`. Do not allocate the
  lower coefficients of `L` independently. Then enforce
  `E | (YL-j_infF)` to reconstruct `G`; a packet passing only the first
  divisibility is incomplete. This replacement converts the lower
  reciprocal block into interpolation and two exact divisibility checks.

  Reduce the remaining unit square before allocating any companion forms.
  With `N=D_0+r-2` and the fixed-degree reciprocals of `V,W,K_1`, introduce

  ```text
  S=(j_infW_vee+EK_vee)/Y
  ```

  and require

  ```text
  LW_vee-FS=EY^N,
  V_vee=-UW_vee-P_clS,
  K_vee=(YS-j_infW_vee)/E.
  ```

  Thus a shard allocates only `F,U,W_vee,S`, then recovers
  `L,G,K_vee,V_vee` through the triangular ledger. Reject on any of the one
  `P_cl` or two `E` divisions, on the reduced unit identity, or on a
  recovered degree-box violation. Do not create independent coefficient
  blocks for the four recovered forms. Hankel and splitting tests still
  follow this preprocessing.

  Pin the middle-Hankel factor before checking any cofactor equations. On
  this exceptional-only shard the unique omission is at `E=0`, so print one
  nonzero base-field scalar `c_H` and require

  ```text
  adj M=c_HEqq^T,
  gcd(nonzero maximal minors)=E       up to scalar,
  (adj M/E)|_(E=0)=c_Hq(gamma_0)q(gamma_0)^T.
  ```

  The final matrix must be nonzero of rank one. With `q_r=E q_bar`, its top
  row and column are zero, while globally the top-top cofactor is
  `c_HE^3q_bar^2`. Reject a different common linear factor, a zero divided
  specialization, or any additional common cofactor factor. Do not absorb
  `c_H` into `q` unless a base-field square root is supplied explicitly.
  This pinned cofactor check is the first actual Hankel gate after the
  reciprocal reconstruction.

  Replace a generic exceptional-rank calculation by the proved kernel-plane
  gate. In a local coordinate `z=E/H`, extract `M_0,M_1,q_1`; from the
  degree-`r-1` exceptional polynomial form its two padded coefficient shifts
  `u,v`. Check

  ```text
  ker M_0=span{u,v},       M_0q_1+M_1u=0,
  u^TM_1u=0,       v^TM_1u=0,       v^TM_1v!=0.
  ```

  Use implicit Hankel convolution or structured minors, not a dense
  `(r+1) x (r+1)` matrix at large analogues. The final nonzero pairing is a
  mandatory first-order crossing check: generic rank recovery without it is
  insufficient because recovery could occur at higher order. A failure of
  any displayed relation rejects the shard before lower coefficient
  elimination.

  Collapse the three pairings to scalar convolutions before any shard is
  sent to a solver. If

  ```text
  (M_1)_(i,j)=h^(1)_(i+j),
  A(X)=sum_(i=0)^(r-1)a_iX^i,
  ```

  compute

  ```text
  Theta_s=sum_(i,j=0)^(r-1)a_i a_j h^(1)_(i+j+s),
  (Theta_0,Theta_1,Theta_2)=(0,0,nonzero).
  ```

  Prefer one polynomial convolution followed by three dot products, or the
  equivalent streaming source sums

  ```text
  Theta_s=sum_x omega_x x^s A(x)^2.
  ```

  Do not materialize `M_1`. Terms at roots of `A` may be skipped. The
  `omega_x` are contracted residual weights, not necessarily the original
  error values or nonzero. A packet passing these three sums still owes every
  lower Hankel, reciprocal degree-box, and split-fiber check.

  Apply the quotient-distance router before allocating any remaining source
  weights. Modulo the moment columns at the roots of `A`, the first-order
  syndrome has support distance at least three. At distance three, print one
  canonical unordered triple `{x_0,x_1,x_2}` and recover, rather than solve
  for, its coefficients as

  ```text
  omega_i=Theta_2/
          (A(x_i)^2 product_(j!=i)(x_i-x_j)).
  ```

  The triple is unique. The proved quotient-distance gap strengthens the
  other branch from distance at least four to

  ```text
  delta_A(h_1)>=2e/3+3=183251937965.
  ```

  Every distance from `4` through `183251937964` is empty by an exact
  incidence contradiction. A shard must not allocate a second support-three
  chart, arbitrary weights on one or two off-locator points, or any support
  in that killed interval. A second proved quotient-support double count
  removes every distance above `3(e+1)/2=412316860416`. Thus the surviving
  high-distance interval is

  ```text
  183251937965<=delta_A(h_1)<=412316860416.
  ```

  It still needs a theorem-level aggregate or dual certificate; enumerating
  supports in this interval is not an executable request. Passing either
  side remains preprocessing and does not waive any later splitting
  condition.

  The general quotient weights are no longer solver variables. The proved
  Forney-numerator normal form writes them uniquely as

  ```text
  omega_t=F(t)/(A(t)^2 B_T'(t)),
  deg F=deg B_T-3,       lc(F)=Theta_2,
  gcd(F,A B_T)=1.
  ```

  A future high-distance request must therefore begin with a finite
  classification or aggregate for the locator/numerator pair `(B_T,F)`
  coupled to the clean split locators. Enumerating support subsets or source
  weights is explicitly out of scope.

  The proved minimal-support uniqueness theorem makes this prohibition
  sharper. In

  ```text
  183251937965<=h<=274877906944=e+1,
  ```

  there is exactly one minimal support `T`; every minimum-complement ordinary
  fiber is internal and uses it. A contributor task in this interval must
  accept the single canonical Forney pair `(B_T,F)` as input or derive it by
  a coverage-proved symbolic rule. A fleet over candidate supports is
  mathematically redundant. Multiple minimal leaders are possible only in
  the still-live upper interval
  `274877906945<=h<=412316860416`, which likewise has no executable request
  until a finite aggregate replaces raw support enumeration.

  Distinct leaders now obey the exact intersection cap
  `|T intersect T'|<=2h-2e-4`. The resulting Johnson bound gives at most six
  leaders for `e+2<=h<=279180239468` and an explicit finite bound through
  `h=302646214511`. A future request in that range may accept a bounded
  symbolic leader packet, but it must derive or certify those leaders from
  the Hankel/Forney data; it may not search the ambient support family. The
  bound controls leader count, not candidate count, and therefore is not by
  itself an executable compute request.

  The sharp-ceiling theorem removes `h=412316860416`. At the retained
  endpoint `h=412316860415`, there are only two possible multisets of the
  `4e` ordinary complement sizes: all are `412316860416`, or one is
  `412316860415`, one is `412316860417`, and the rest are `412316860416`.
  Any future endpoint request must consume one of these two profiles and the
  corresponding exceptional-intersection multiset. A generic
  high-distance support search would discard the exact theorem input and is
  not a valid contributor task.

  The endpoint exceptional and complementary resultants are now completely
  prescribed as opposite `P_ord` powers, with at most one reversed
  linear-factor swap. A future endpoint computation must operate on this
  succinct pair and compare it with the reciprocal identities. Materializing
  either dense resultant is out of scope. Promote this to an executable
  request only after a subresultant or product-tree certificate has a
  measured total cost and an independent streaming checker.

  The reciprocal complement `V` completes these data to an exact `2 x 2`
  resultant matrix. Any endpoint compute proposal must preserve all four
  entries and their row/column product checks; computing only
  `Res_X(A,Q)` is now incomplete. The next useful certificate must test a
  corrected-square coefficient or coprimality condition not already forced
  by this matrix. Recomputing incidence multiplicities is redundant.

  On the quotient-distance-three chart, apply the exact MDS-escape router
  before allocating ordinary split fibers. Reconstruct the exceptional
  coefficients `beta_a`, the first-order coefficients `alpha_a`, and the
  canonical triple weights. For each ordinary slope `z`, count

  ```text
  j_z=#{a:beta_a+z alpha_a=0}.
  ```

  Exactly `e` slopes must have `j_z=2`; their cancelled pairs partition all
  `2e` roots of `A`, and their clean locator is forced to be the remaining
  exceptional roots together with the canonical triple. Exactly `3e` slopes
  must have `j_z=0`; each corresponding locator `G_z` is disjoint from that
  canonical support and must satisfy

  ```text
  G_z(t_0)/A(t_0)=G_z(t_1)/A(t_1)=G_z(t_2)/A(t_2).
  ```

  Reject `j_z=1`, `j_z>=3`, any other internal support, or any external
  support intersection. Across the `6e+4` outside points, external-root
  multiplicity is at most `e`, its total deficit is exactly `e`, and at
  least `5e+4` rows are saturated. A shard should encode the `e` disjoint
  pairs and this near-saturated external incidence structure, not enumerate
  `4e` unrelated split locators. Passing the router remains preprocessing;
  it does not certify the lower Hankel chain or the reciprocal square.

  Reconstruct the full residual generator from the internal data before any
  external split test. If the internal slopes are `xi_i`, their cancelled
  pairs have polynomials `D_i`, `B` is the canonical triple polynomial, and
  `Q(xi_i)=lambda_i B A/D_i`, use

  ```text
  Phi(z)=product_i(z-xi_i)/product_i(-xi_i),
  L_i(z)=product_(j!=i)(z-xi_j)/(xi_i-xi_j),
  Q(z;X)=Phi(z)A(X)
         +zB(X)sum_i(lambda_i/xi_i)L_i(z)A(X)/D_i(X).
  ```

  This formula is proved necessary and has separation rank exactly `e+1`.
  A distance-three shard should therefore encode only the perfect matching
  of the exceptional roots, the distinct nonzero `xi_i`, and the nonzero
  `lambda_i`; allocating an arbitrary `(r,e)` biform or independent clean
  locators is obsolete. The remaining split test asks for exactly `3e`
  other values of `z` at which this reconstructed polynomial has `r` roots
  in `D_res\(R_A union T)`, together with the exact outside-row deficit `e`.

  Apply the proved quadratic locator-rank gate to every proposed external
  block packet before constructing a dense resultant. If `g(x)` is the
  coefficient vector of the monic degree-`e` row locator on an active outside
  row, the matrix

  ```text
  (g_i(x)g_j(x))_(x,0<=i<=j<=e)
  ```

  must have rank at most `3e+1`. Hence its `6e+3` rows have nullity at least
  `3e+2`, and for `e>=4` the locator points satisfy at least `e(e-3)/2`
  independent quadrics. Reject a packet above this rank immediately. A
  contributor implementation should emit a row-reduction certificate or a
  basis of the vanishing quadrics; passing this gate is necessary only and
  does not replace the subgroup, residue, or resultant-power checks. The
  first `e=3` analogue is dimensionally vacuous for this gate, so its purpose
  there is replay compatibility; route-selection evidence begins at the
  first complete `e>=4` analogue.

  Apply the stronger complement-residue gate first whenever the external
  blocks are available. With

  ```text
  I(z)=product_i(z-xi_i),       H_x(z)=P_Z(z)/G_x(z),
  ```

  the `6e+3` residue classes `H_x mod I` must span dimension at most three.
  Before choosing `I`, the full complement polynomials must span dimension
  at most `e+4`; reject a larger coefficient rank immediately.
  Equivalently, either evaluation matrix

  ```text
  (H_x(xi_i))_(x,i),       (G_x(0)/G_x(xi_i))_(x,i)
  ```

  has rank at most three. This test is linear in the packet size after
  product-tree evaluations and needs no dense resultant. Emit three basis
  residues and coordinates for every `H_x`, or a rank-four minor as a
  rejection certificate. Exact biregularity is insufficient: the banked
  `e=4` control has 27 distinct four-blocks on 12 slopes, column degree nine,
  and complement rank four. A useful contributor classification should
  enumerate or characterize only the rank-three residue families, not all
  biregular designs. A contributor packet should therefore print both the
  full complement coefficient rank and the reduced rank-three certificate.
  The reduced rank is exactly the span dimension of the quadratic pair
  locators. Rank two is not an anonymous degeneration: the banked Mobius
  dichotomy proves that all exceptional pairs are orbits of one common
  projective involution. Route such packets to a subgroup/Mobius intersection
  classifier and report the involution matrix. Rank-three packets remain the
  generic complement-residue classification target.

  Do not promote the quadratic `rank<=3e+1` filter into an equality premise
  on that generic branch. The proved generic Schur-square saturation route
  fence constructs arbitrary-size rank-three pair families with product rank
  at most `3e`; its exact `F_101`, `e=12` fixture has ambient/product ranks
  `37/36`, while a one-pair negative control restores 37. A contributor run
  must retain rank-defective generic packets and test them against calibrated
  complement incidence, boundary, and resultant-power conditions.

  Rank-defective packets now have a mandatory deterministic classification.
  Solve the linear equations `D_i | R-y_iB`, `deg R<=2`; their nullity must
  equal `(3e+1)-rank(M_2)` and must be zero or one. A lower matrix rank or
  larger nullity rejects the claimed generic packet. A nonzero solution
  prints the projectively unique `R` and every `y_i`. All nonzero levels must
  be distinct, with at most one zero level satisfying `D_i|R`. Route nullity
  zero to the rank-`3e+1` saturated branch and nullity one to the rank-`3e`
  trigonal-fiber branch. Do not enumerate possible rational maps or discard
  a packet merely because its Schur rank is one below the cap.

  **Official trigonal branch closed; no compute request.** The proved
  `official_trigonal_subgroup_exclusion` now rules out nullity one on the
  official order-`2^41` domain. Its coincidence curve has at least `2e`
  subgroup points, while the worst admissible bidegree-`(2,3)` form has at
  most `1440N^(2/3)<2e`; the geometrically reducible case would require an
  order-three Mobius deck map, also impossible on this `2`-group. An
  official classifier may reconstruct the kernel as an audit check, but it
  must require nullity zero and quadratic rank `3e+1`. Do not enumerate
  trigonal rational maps or request a distributed trigonal search. Small-row
  trigonal fixtures remain valid route fences because the official numerical
  subgroup margin is load-bearing.

  **Saturated rank-shadow route fenced; retain calibrated residues.** The
  exact `F_151`, `e=5` cyclic control has `33=6e+3` distinct blocks,
  replication `11=2e+1`, quadratic rank `16=3e+1`, and complement span
  `9=e+4`. Thus a donated run that tests only biregularity and these two
  ranks can return a genuine survivor without deciding CR-003. The fixture
  fails the real modulo-`I` condition uniformly: every degree-five `I` with
  nonzero constant term leaves residue rank at least four. Every future
  packet and pilot must replay this control, print `I`, and certify the
  rank-three matrix `(H_x mod I)_x`; do not request a fleet over the weaker
  coefficient-span interface.

  **Optional audit CR-003-CLIFT -- saturated calibrated conic-lift
  classifier (not runnable yet).** The first nonvacuous official-shaped
  analogue of the now-closed official distance-three branch is

  ```text
  m=4,       e=7,       r=15,       N=64,       F=F_193.
  ```

  Its audit decision is whether a pair-Lagrange generator on this complete finite
  row realizes the exact external split design while simultaneously having
  quadratic locator rank `3e+1` and the actual calibrated residue rank three.
  This is the smallest analogue that sees both live generic constraints;
  `e=3` makes the quadratic rank gate dimensionally vacuous. A complete
  survivor would be a proof-relevant route fence and a template for the
  kernel-lift obstruction. A complete no-hit result would remain
  small-analogue evidence, but its first universally failing gate could
  suggest the missing uniform theorem.

  Enumerate canonical support/matching packets only after the already proved
  quadratic-character, matching-free even-value, `tau`-label, boundary, and
  dual row-product gates. Reconstruct `Q` from the pair-Lagrange formula and
  decide the external design through the sparse subgroup norm and
  resultant-power equivalence; do not allocate slopes, blocks, or arbitrary
  biform coefficients. On every reconstructed design, form

  ```text
  I(z)=product_i(z-xi_i),
  G_x(z)=monic(Q(z;x)),       H_x(z)=P_Z(z)/G_x(z),
  Htilde_x(z)=B(x)G_x(0)H_x(z).
  ```

  The proved `calibrated_conic_kernel_lift_normal_form` forces the unique
  degree-`<e` representative

  ```text
  Htilde_x mod I = R_0+xR_1+x^2R_2 mod I.
  ```

  Emit `R_0,R_1,R_2` and the complete kernel lifts

  ```text
  J_x=(Htilde_x-R_0-xR_1-x^2R_2)/I,       deg J_x<=e.
  ```

  Its leading coefficient must be `B(x)G_x(0)`, and the checker must also
  replay the exact product identity

  ```text
  product_x(Htilde_x)=kappa P_Z^(4e+2).
  ```

  Apply the proved cleared-lift quartic router before any generic lift-rank
  analysis. Compute the explicit `E_i,N_i` first-jet polynomials, construct
  the bidegree-at-most-`(2e,4e+6)` clearing `F`, and for every reconstructed
  external slope exact-divide

  ```text
  F(gamma;X)=K_gamma(X)T_gamma(X),       deg T_gamma<=4,
  ```

  where `K_gamma` is the monic locator of the `4e+2` nonincident active
  rows. Emit every quartic coefficient vector and division remainder. A
  nonzero remainder or degree above four rejects the packet or the
  implementation. Do not reject a nonsplit or varying quartic: the exact
  `F_17,e=1` replay proves both behaviors can occur below the official
  uniqueness threshold.

  Also reconstruct the global quartic weld

  ```text
  FQ=(AB)^2q_eP_Z+CzI^2Omega,       deg Omega<=(e-2,4),
  ```

  and verify
  `Omega(gamma)=ell_gamma T_gamma/(gamma I(gamma)^2)` coefficientwise
  at every external slope. Emit the five coefficient polynomials of `Omega` and
  their rank. This rank is a discovery diagnostic, not a rejection gate: no
  theorem currently forces the `P^4`-valued curve to be a line.

  Apply the proved exceptional-boundary CRT reconstruction before building
  the external cofactors. In `F[X]/(A)`, emit the pair-label class
  `delta=xi_i mod D_i`, the exact quotient

  ```text
  V_A=(sum_i D_iN_iL_i)/(z-delta),
  ```

  and the canonical remainder

  ```text
  Omega_A=rem_A(
    N^(-1)X(X-s)(X-x_0)A'Bq_e^2V_A
  ).
  ```

  Every coefficient of `X^j`, `5<=j<2e`, is an exact rejection gate and
  must be zero. Emit those high coefficients even on rejection, together
  with the quotient and remainder identities; do not report only the final
  degree. On passage, require `Omega_A=Omega` and replay the three identities
  `C(t)zOmega_A(z;t)=q_e(t)^2 sum_iD_i(t)N_i(t)L_i(z)` at the roots of `B`.
  This gate is cheaper and earlier than constructing all `T_gamma`. The
  coefficient rank of the surviving five low coordinates remains diagnostic
  only.

  Emit the equivalent dual-RS moment certificate as well. For every
  `0<=j<=2e-6`, stream the pair-algebra traces

  ```text
  M_j(z)=sum_k Tr_(F[X]/(D_k) over F)(
    X^(j+1)(X-s)(X-x_0)Bq_e^2V_k(z)
  )
  ```

  and require every coefficient to be zero. The checker must verify each
  trace from the degree-two remainder modulo `D_k`, reconcile the moments
  with the high coefficients of `Omega_A`, and retain the first nonzero
  `(j,z-degree)` coefficient on rejection. This is the preferred streaming
  certificate: it does not materialize the degree-`6e+3` active locator `C`.

  Before selecting internal slopes, build the support-only pair-crossing
  matrix `R_l` for every omitted pair `l`. Its row for
  `D_k=(X-a_k)(X-b_k)` is

  ```text
  (G_l(b_k)a_k^d+G_l(a_k)b_k^d)_(0<=d<=4),
  G_l=X(X-s)(X-x_0)B^4(A')^4D_l^2.
  ```

  Emit all ranks, kernel bases, and evaluations of each kernel basis on the
  roots of `A/D_l`. Reject immediately if one matrix has rank five or if all
  its kernel polynomials vanish at one retained root. A retained matching
  must print a quartic kernel polynomial nonzero on every other pair. The
  deterministic `e=4,5,6,7` controls must replay ranks `3,4,5,5` for every
  omitted pair. The fixed `e=6,F_113` control must also replay all `10,395`
  matchings with the exact four-pattern histogram in `(QPC7)` and zero
  all-deficient survivors. Do not enumerate internal slopes for a rejected
  matching.

  On the official row, do not propose a raw all-deficient support sweep.
  The proved `quartic_support_low_degree_fiber_reduction` has already reduced
  every such packet to global smooth antiweight or to at least `e-148`
  fibers of one rational map of degree two, three, or four. Any donated
  official-scale computation must first compile one of those four symbolic
  branches, quotient by its map automorphisms, prove coverage including the
  bounded normalization tail, and publish a measured pilot. The reduction
  is official-scale and does not prune the `e=7` analogue above; using it as
  an analogue rejection gate would be invalid.

  Its proved continuation removes degree three and reduces degree two to one
  antipodal or constant-product involution with at most forty tail pairs.
  Do not request a degree-three fleet. The proved bounded-tail row-codegree
  theorem now gives the first symbolic ledger: with `t` off-involution pairs,
  every nonidentical outside orbit has codegree at most `t`, and at most one
  orbit has identical normalized rows. Thus the official branch has
  codegree at most forty. The proved degree-two tail-rigidity continuation
  sharpens the exact-design branch to at most six antipodal tails or eight
  constant-product tails, and therefore to row codegree at most six or
  eight. The later residual-discriminant theorem excludes every resulting
  gcd-corrected complement, so tail enumeration is retired rather than an
  executable request.
  The exact internal-slice continuation also absorbs global antiweight into
  degree two or degree four, so no independent antiweight fleet should be
  requested. The abstract antiweight fixture remains a required mutation
  control for any support-only compiler.
  The remaining degree-four branch is already symbolically routed to a
  geometrically reducible coincidence divisor or the Laurent-end curve
  `XY[X^2+XY+Y^2+a(X+Y)+b]=d`. Do not request a generic quartic-map fleet.
  Any contributor computation must compile one of those two forms and state
  which theorem decision its output would settle; a raw coefficient sweep
  is not an executable request.
  The reducible half is now theorem-classified as `F(X^2)`, `F(X^4)`, or
  `F(X+c/X)`. The proved pullback-involution absorption now routes all three
  forms into the same six/eight-tail static Pade-gcd leaf. No
  reducible-factor or pullback-quotient fleet is useful.
  The absolutely irreducible Laurent-end branch is now theorem-excluded by
  the Corvaja--Zannier gcd bound. Do not request a Laurent coefficient sweep.
  Both the simultaneous-gcd compiler `CR-003-BT8` and the pullback compiler
  `CR-003-PB4` are retained below only as retired provenance.

  Only then, before selecting the `lambda_i`, build the internal-slice lambda-cube
  matrix `U` from only the support partition, matching, and internal slopes.
  Its `e(2e-7)` rows are the coefficients above degree four in `(QLK3)`, and
  its required kernel vector is `(lambda_i^3)`. Emit the component
  interpolants `Y_lk`, a row-reduction certificate, every single-column
  deletion rank, and one of:

  ```text
  REJECT_U_FULL_RANK: rank(U)=e;
  REJECT_U_COLOOP: rank(U without column i)<rank(U);
  SURVIVE_U_CUBE: a deletion-stable kernel containing an explicit
                  coordinatewise-cube vector.
  ```

  Full rank or one coloop rejects the entire support/pair/internal-slope
  packet without enumerating `lambda_i`. A deficient packet is not yet a
  survivor unless its kernel meets the coordinatewise cube subgroup; print
  the `lambda_i` preimages and verify `U(lambda_i^3)=0`.

  Only then, before constructing `P_Z`, `N_i`, `Omega_A`, or any external
  cofactor, build the proved torus-kernel matrix `T` from the retained pair
  partition, internal slopes, `lambda_i`, and `q_e`. Its rows are the
  coefficients of the derivative-free pair traces in `(QTK4)`. Emit a
  row-reduction certificate, the rank after each single-column deletion, and
  one of:

  ```text
  REJECT_FULL_RANK: rank(T)=e;
  REJECT_COLOOP: rank(T without column i)<rank(T);
  SURVIVE_TORUS: rank(T)<e and every column deletion preserves rank.
  ```

  The first two `T` outcomes reject the packet exactly. On `SURVIVE_TORUS`,
  emit a kernel basis; after `P_Z` is reconstructed, verify that
  `theta_i=xi_iP_Z(xi_i)/lambda_i^2` lies in that kernel. Do not enumerate
  kernel vectors: `q>e` makes deletion stability equivalent to existence of
  some full-support kernel vector. The deterministic controls at
  `e=3,4,5,7` must replay `U` ranks `0,4,5,7` and `T` ranks `2,4,5,7`; only
  the dimensionally vacuous `e=3` control is torus-eligible at both stages.

  Report the coefficient rank of the `J_x`, their exact coefficientwise
  interpolation degrees in the active row coordinate, and any certified
  decomposition into projective lines. These are discovery diagnostics, not
  rejection gates: the present proof does not bound the lift rank or degree.
  They are included because a moving-root argument applies to the conic
  residues only after the kernel lifts are controlled. Omitting `J_x` would
  reduce this request to the false uncalibrated rank-shadow route.

  Before promotion from pre-request, contributors must provide all of:

  1. an inverse orbit-coverage map for every support and matching
     normalization on the displayed row;
  2. a deterministic positive-certificate checker replaying the Hankel
     source, pair-Lagrange formula, sparse norm, perfect-power identity,
     reconstructed incidence, both exact ranks, and the `J_x` decomposition;
  3. a complete negative-certificate format with per-gate survivor counts
     and resumable shard hashes;
  4. a strictly smaller measured pilot with peak RAM, storage, wall time,
     retry allowance, and a conservative total dollar ceiling.

  Checkpoint by canonical `(support,triple,matching,xi,lambda)` prefix and
  preserve counts and witnesses on timeout. A found survivor is `FAIL` for
  any proposed uniform exclusion using these inputs and triggers theorem
  repair. Exhaustive no-hit is `PASS` only for this one finite analogue and
  causes no DAG promotion without a proved transport theorem. Incomplete
  output is evidence only. Cost is currently unknown and potentially large:
  do not launch this request on the local Modal balance or in WSL. When the
  rate-half packet is vendored upstream, include CR-003-CLIFT only under
  **Optional audits**, not as a missing proof step. A contributor may supply
  the compiler or pilot under an accepted resource cap if small-row route
  diagnostics are useful.

  The official subgroup/Mobius classifier is now theorem-complete for the
  nonspecial branch. Published explicit bounds give at most `32N^(2/3)`
  graph points, below `2^33`, versus the required `2^39-2`. Do not request a
  general Mobius fleet. A rank-two packet must be one of the two dihedral
  forms `a<->-a` or `a<->c/a`; apply the boundary root-unity and dual
  row-product gates symbolically to those forms. Large computation on the
  dihedral cases is not authorized until that substitution produces a
  finite compressed parameter space and a costed pilot.

  The boundary substitution is now complete. Either dihedral form requires
  `gcd(e,p-1) in {e/3,e}`. The apparent reciprocal five-point packet has
  exact form `c=sx_0`, `T={u,t,c/t}`, `u^2=c`, but the triple gate gives
  `(u/t)^(3e)=1`; coprimality with `N` then contradicts `u!=t`. Restrict any
  future rank-two implementation to the two high-order field strata, print
  the field-order gcd and the boundary involution orbits, and apply the dual
  `r`-th-power residue gate next. Do not spend compute enumerating fields or
  pairings outside this theorem-reduced list.

  **Completed arithmetic route fence (do not rerun).** Recursive Lucas
  certificates now exhibit an official-interval prime in each of the two
  retained gcd strata, with `gcd(r,p-1)=1` in both examples. Consequently a
  large prime or congruence scan has no closure value, and the dual residue
  gate cannot be a uniform exclusion. A useful large run must start from a
  coverage-complete compressed split-pencil parameterization, branch first
  on `gcd(r,p-1)`, and return a compact algebraic rejection certificate or a
  fully replayable survivor. Until such a parameterization and measured
  pilot exist, this remains a theorem task rather than a compute request.

  The dual residue gate is now compressed symbolically. For either dihedral
  branch it is the split-algebra equation

  ```text
  Y^r = kappa W(E')^2 mod E,       deg E=e, deg W=7, deg Y<e.
  ```

  Any future contributor implementation must operate on the orbit polynomial
  `E`, not on `2e` individual exceptional roots, and must emit the remainder
  identity plus an `r`-th-root witness or a power-residue rejection. Skip this
  gate when `gcd(r,p-1)=1`, where it is automatic, and apply the resultant
  perfect-power split-design test instead. A large official-degree solve is
  not yet authorized: the equation still has degree-`e` unknown data and no
  coverage-complete finite parameterization.
  A PR may request distributed compute only after an additional theorem
  reduces `E` to a finite resumable family and a small analogue measures the
  per-case cost. The replay certificate should contain `E`, the degree-seven
  `W`, `Y`, and the exact quotient in the displayed congruence; raw root or
  field enumeration is out of scope.

  The full sparse subgroup norm has also been descended to the involution
  quotient. Use

  ```text
  Res_U(U^(N/2)-1,V_-)                 (antipodal),
  fixed_Q_product * Res_U(Omega_c,V_c) (constant product),
  ```

  where both value polynomials have `U`-degree at most `r`, and `Omega_c` is
  recovered from `D_N(U,c)-2` by removing its zero or two fixed-point factors
  and taking the exact square root. Exact-degree external split slopes are
  equivalently the parameters where this degree-`r` value polynomial splits
  over the quotient set. A future large-run request should use
  cyclic-resultant or remainder-sequence arithmetic against these compact
  quotient locators and divide the known sparse-norm factors online. It must
  not enumerate `mu_N`, materialize a dense degree-`N` Dickson polynomial, or
  construct the active-row locator. No official run is authorized until a
  measured small analogue demonstrates sublinear storage, resumable shards,
  and a compact multiplicity/factorization certificate. This quotient norm
  interface is the specification contributors should implement when that
  pilot exists.

  A quotient implementation must also replay the external-product ledger

  ```text
  product_z monic(V_z)=C_2^(2e)C_1^e,
  epsilon in {0,1},
  sum_z double_roots(V_z)=epsilon e,
  sum_z simple_roots(V_z)=3er-2epsilon e.
  ```

  Here `epsilon` records the zero-or-one identical-row orbit. On the exact
  zero-tail branch, every nonexceptional paired row set has codegree zero;
  when `epsilon=1`, exactly `e` factors have the same one double root. An
  implementation should report this orbit, the simple/double histogram for
  each factor, and exact product-tree hashes for `C_1,C_2`. On the
  quartic-support branch with `t>0`, this ledger must not be asserted
  unchanged. The now-retired `CR-003-BT8` specification records the required
  row gcd and degree `d_u<=t` for regression purposes. These are rejection
  checks and compact certificates, not authorization for a large run. A
  future distributed request on a different open branch becomes valuable
  only after a theorem or complete parameterization makes its candidates
  enumerable without scanning fields, subgroup points, or arbitrary split
  polynomials. At that point contributors can shard by orbit-polynomial
  parameter and return the first failed ledger identity or a full survivor.

  The pair-complement trace gives a smaller certificate target. Every
  nonexceptional two-row orbit must emit a degree-`e` divisor

  ```text
  K_u=a_uI+chi(u)(u^2M_0-2uM_1+M_2),
  K_u | P_Z,
  ```

  and the packet must contain at least `3e-2` distinct projective divisors on
  the antipodal branch or `3e-3` on the constant-product branch. Their last
  three coordinates satisfy `b_1^2=4b_0b_2`. The abstract classification
  request has now been retired: the proved abstract-quadric route fence gives
  `6e+1` such divisor classes by three one-root-swap pencils. A computation
  enforcing only divisibility, a four-space, and the cone would therefore
  spend resources rediscovering genuine abstract survivors.

  **RETIRED contributor request -- zero-tail calibrated dihedral trace
  classification.** The proposed large run would have enforced, for every
  internal root `u_i`,

  ```text
  mu_i=P_Z(xi_i)/lambda_i^2,
  K_u(xi_i)=chi(u)mu_i(u-u_i)^2,
  K_u | P_Z,
  product_z monic(V_z)=C_2^(2e)C_1^e,
  ```

  as well as the official antipodal or constant-product subgroup orbit and
  the zero-or-one exceptional-pair rule. Do not launch it. The proved
  dihedral trace-collision exclusion rules out the exact zero-tail branches
  for every `e>=31` by combining the calibrated quadratics with the `e-4`
  minimum complement incidence. It does not by itself cover the at-most-8
  off-involution pairs produced by the quartic-support router. Preserve this
  specification only as provenance for the retired zero-tail route and as a
  regression template for the retired bounded-tail route.

### Retired pre-request CR-003-BT8: bounded-tail dihedral complement compiler

- **status:** RETIRED BY THEOREM. Do not launch or copy this request as live
  upstream work. The proved residual-discriminant exclusion rules out every
  aligned degree-one-through-four pencil and closes the complete
  all-deficient quartic-support branch. The specification below is retained
  only as provenance and as a regression interface.
- **former consumer:** the former bounded-tail degree-two branch of
  `rate_half_band_closure`, now theorem-closed.
- **proved router:** for an antipodal or constant-product involution, with
  `t<=6` or `t<=8` respectively, each nonidentical outside orbit
  `{x,tau(x)}` has

  ```text
  g_u=gcd(q_x,q_tau(x)),       d_u=deg g_u<=t,
  K_u=P_Z g_u/(q_x q_tau(x)),  deg K_u=e+d_u,
  ```

  and at most one outside orbit has identical normalized rows. The checker
  must also replay the degree-`t` eliminant `H/I_G`; it may not infer the
  codegree from sampled roots.
- **former mathematical decision:** classify every nonzero pencil

  ```text
  R(U,Z)=R_2(Z)U^2+R_1(Z)U+R_0(Z),
  1<=deg_Z R<=4,
  ```

  for which at least `e-33` antipodal or `e-44` constant-product coordinates
  `u` give distinct split squarefree divisors `R(u,Z)` of one fixed
  squarefree `P'=P_Z/P_H`, while every root of `P'` occurs at no more than
  two such coordinates. Exclude all four degrees or return a replayable
  pencil satisfying the complete packet interface. High-degree gcd,
  bivariate relation, nonzero-determinant, and individual-circuit searches
  are already paid and are not route-deciding. The residual-discriminant
  theorem supplies the uniform symbolic exclusion, so this decision is paid.
- **former pilot rows:** first replay symbolic `t=0,1,2` mutation fixtures. Then use
  only compiler-produced exact-design packets on `(m,e,N,p)=(4,7,64,193)`.
  A later threshold pilot may use `(16,31,256,257)`, but only after the first
  pilot supplies a measured per-packet cost and a complete normalized
  parameter cover. Neither pilot transports automatically to the official
  row.
- **former required artifact:** stream `R_0,R_1,R_2`, `P'`, the canonical aligned
  coordinate set, every exact division `P'/R(u,Z)`, split/squarefree
  certificates, the root-use histogram, and either a symbolic exclusion by
  degree or the first full survivor. Include mutation witnesses for degree
  drops, repeated factors, identical divisors, and roots used three times.
  Packet-level pilots must additionally emit `P_H`, `q_x,q_tau(x),g_u,K_u`,
  and exact division witnesses. A no-hit certificate must include canonical
  shard intervals, coverage counts, rolling hashes, and an independent
  checker that never materializes all subgroup points at once.
- **former resource contract:** unknown. Before promotion to a numbered request,
  bank a resumable launcher and a smaller measured pilot with hard CPU, RAM,
  storage, wall-time, retry, and dollar ceilings. Shard by canonical tail
  invariant, not by arbitrary pair tuples. Preserve the first witness and
  all completed shard totals on timeout.
- **retirement effect:** no finite pilot is needed. A replayable survivor
  would now be a falsifier of the proved residual-discriminant exclusion and
  should be reported as a proof bug with the complete packet interface. A
  no-hit computation has no additional proof value.

### Retired pre-request CR-003-PB4: quartic pullback quotient compiler

- **status:** RETIRED BY THEOREM. Do not launch or copy this request into an
  upstream PR. The proved pullback-involution absorption routes every
  quartic pullback into the bounded-tail interface, and the subsequent
  residual-discriminant exclusion closes that interface.
- **former consumer:** the former degree-four pullback branch of
  `rate_half_band_closure`, now absorbed into the static Pade-gcd leaf.
- **proved router:** every surviving quartic comparison field is one of

  ```text
  F(X^2),       F(X^4),       F(X+c/X),
  ```

  with at least `e-148` matched fibers. The generic irreducible, Laurent,
  reducible-factor, degree-three, and independent antiweight fleets are
  already retired by proofs.
- **mathematical decision:** after quotienting the complete deck action,
  decide whether the exact internal-slice, boundary-product, source, and
  external-design identities admit any quartic-pullback packet. The compiler
  must distinguish an order-two matching from an order-four fiber whose
  chosen pairs may mix deck involutions.
- **pilot:** use `(m,e,N,p)=(4,7,64,193)` only after an inverse normalization
  map proves complete ownership of every pullback packet. Reuse
  `CR-003-CLIFT` residues and kernel lifts rather than recomputing them. A
  larger run must wait for a measured pilot and a theorem identifying a
  finite quotient-parameter family.
- **required artifact:** canonical map/deck parameters, selected pair orbits,
  all at-most-148 normalization tails, exact product/source residuals, first
  failed identity or a full survivor, shard coverage hashes, and an
  independent streaming checker. Raw roots, arbitrary quartic coefficients,
  and dense degree-`N` locators are forbidden artifact formats.
- **retirement effect:** preserve this specification only as provenance for
  the discarded route and as a regression checklist for the absorption
  theorem. Any future counterexample must first falsify that theorem; absent
  such a witness, no donated compute belongs on the quartic-support branch.

  The outside-row condition is now exact, not merely a deficit budget. One
  point `x_0` outside `R_A union T` is omitted from every external locator;
  each of the other `6e+3` outside points occurs in exactly `e` of the `3e`
  external locators. If `C` is the monic polynomial on those `6e+3` points,
  require the compact identity

  ```text
  product_(z external) G_z(X)=C(X)^e,
  P_X(X)=A(X)B(X)C(X).
  ```

  A contributor should print the omitted row and a product-tree certificate
  for this power identity. Aggregate deficit alone is no longer an admissible
  certificate. The resultant-power equivalence below supersedes the former
  requirement to allocate or print the full biregular incidence matrix.

  A deterministic low-order route fence is now available at

  ```text
  background/nodes/rate_half_ca_hankel_distance_three_e1_hankel_design_route_fence/verify.py
  ```

  It exhausts all `1820` degree-four split locators and all projective slopes
  over `F_17`. The fixture is column-far and jointly passes the pair normal
  form, exact external design, affine Hankel ranks, first-order crossing,
  pinned adjugate, and supported-fiber product identity. It deliberately has
  four quotient-support triples at `r=3`, below the official `r>=4`
  uniqueness threshold. A contributor classifier must replay this fixture:
  rejecting it before an explicitly official-scale uniqueness or reciprocal
  gate signals an over-strong constraint. The next useful analogue is the
  first `r>=4` instance; a larger sweep of `r=3` fixtures has no proof value.

  Do not allocate contracted source weights or endpoint moments on a
  distance-three shard. Once the matching `D_i`, internal slopes `xi_i`,
  internal scalars `lambda_i`, and `Theta_2` are fixed, reconstruct

  ```text
  q_bar(z)=sum_i(lambda_i/xi_i)L_i(z),
  K_a=Theta_2 Delta_i /
      (Delta_0 A'(a)B(a)^2(lambda_i/xi_i)(A/D_i)(a)),
  beta_a=-xi_iK_a,       alpha_a=K_a,
  omega_t=Theta_2/(A(t)^2B'(t)).
  ```

  These coefficients uniquely determine `h_0,h_1` through degree `2r`.
  At an external slope the minimum-circuit scalar must replay as
  `Theta_2 Phi(z)/q_bar(z)`. Once all `3e` required external split fibers
  pass, the contracted Hankel identity, exceptional/ordinary ranks,
  first-order crossing, and `adj M=c_H z q q^T` are proved consequences of
  these reconstructed sources; replay them in the checker, but do not give
  them solver variables or treat them as independent search gates. Continue
  with the corrected-square converse below, then the original endpoint
  lift/column-far check and absence of extra split fibers.

  The corrected reciprocal square is no longer an independent search gate
  after the exact split design passes. For every saturated row, verify the
  degree-`e` divisibility `Q(z;x)|P(z)`; for every ordinary supported slope,
  verify `Q(z;X)|P_X(X)`. Coefficientwise interpolation then reconstructs

  ```text
  QV+P_XW=P,       QA_c+P_clB_c=P_X,
  WB_c-z=QK,       VB_c+zA_c=-P_XK.
  ```

  The proved exceptional factor-descent chain supplies every later
  reciprocal/resultant/Bezout identity. A checker should replay those
  identities, but a solver must not allocate complements, welds, reciprocal
  forms, resultants, or Bezout coefficients. Continue with the original-lift
  converse below.

  No original-lift or column-far search remains after the external design
  passes. For arbitrary endpoint scalars, recover the original moments from

  ```text
  y_(ell,0)=tau_ell,
  y_(ell,k+1)=s y_(ell,k)+h_(ell,k).
  ```

  The full locator `(X-s)Q` certifies all `4e+1` required close slopes. A
  common full locator is proved impossible: after contraction it would give
  one fixed support of at most `r+1` points, while MDS independence forces it
  to contain the `6e+3`-point union of the external locators. Additional
  close slopes only strengthen a counterexample and need not be excluded.
  Historically, CR-003's distance-three decision reduced exactly to:

  ```text
  does an official pair-Lagrange generator realize the exact external
  split design?
  ```

  The proved external split-design exclusion now supplies the complete
  official nonexistence theorem, so no official-scale computation should be
  launched for this decision. A positive small-analogue certificate remains
  a route fence, not an official counterexample.

  Apply the boundary root-unity router before allocating any remaining design
  variables. For every matched pair `D_i=(X-a)(X-b)`, compute

  ```text
  U=B(a)(A/D_i)(a)/(B(b)(A/D_i)(b)),
  zeta=-[P_X'(a)/P_X'(b)]/U^4,
  ```

  and require `zeta^e=1`. For two independent pairs `t,u` among the canonical
  triple, require

  ```text
  ([P_X'(t)/P_X'(u)]/
   ((A(t)/A(u))^4(B'(t)/B'(u))))^e=1.
  ```

  Evaluate derivatives directly as
  `N*x^(-1)/((x-s)(x-x_0))`. These gates depend only on `A,B,x_0` and the
  matching. Reject before choosing `xi_i`, `lambda_i`, external slopes, or
  blocks. Print the actual root-of-unity labels for every survivor; a bare
  pass bit loses information needed by later product constraints.

  Before even constructing the boundary value polynomial, apply the proved
  quadratic-character consequence

  ```text
  -A(0)A(s)A(x_0) in (F_p^*)^2.
  ```

  This depends only on the exceptional support and the two removed rows. A
  nonsquare rejects the support before the triple, matching, residue classes,
  slopes, or scalars are allocated.

  Before enumerating pair matchings, apply the matching-free form. Compute

  ```text
  Y_a=(P_X'(a)/(B(a)^4 A'(a)^4))^e       (a in R_A).
  ```

  The monic value polynomial `product_a(Y-Y_a)` must be even. This condition
  is equivalent to the existence of a boundary-compatible perfect matching;
  reconstruct only matchings that pair `Y_a` with `-Y_a`. On the triple,
  the three values

  ```text
  (P_X'(t)/(A(t)^4 B'(t)))^e
  ```

  must be equal. A classifier that allocates arbitrary pairings before these
  two tests is obsolete.

  Couple this evenness test to the dual row-product residue before
  reconstructing any matching. In `F_q^*/(F_q^*)^r`, put

  ```text
  c_a=C(a),       M=product_(t in T)C(t),
  Lambda(a)=(Y_a,[c_a]_r),
  tau(y,g)=(-y,[-M]_r g^(-1)).
  ```

  The label multiset must be invariant under `tau`; this is equivalent to
  existence of a matching satisfying both the boundary and `r`-th-power
  gates. It also forces the aggregate test

  ```text
  product_(a in R_A)C(a)/(-M)^e in (F_q^*)^r.
  ```

  Equivalently, test

  ```text
  Res(A,C)/(-Res(B,C))^e in (F_q^*)^r.
  ```

  Reconstruct only `tau`-paired matchings. Testing central symmetry and the
  pair residues in separate matching fleets is obsolete.

  Apply the dual row-product gate on the same support packet. The exact
  external incidence design forces

  ```text
  product_(C(x)=0) Q(z;x)=L P_Z(z)^(2e+1).
  ```

  Consequently every matched pair `D_i` must satisfy

  ```text
  R_i=product_(C(x)=0)B(x)/D_i(x) in (F_q^*)^(2e+1).
  ```

  Compute `R_i` from the compact resultant ratio
  `Res(C,B)/Res(C,D_i)`, or from the boundary values in `(DRP5)--(DRP6)`,
  and test `R_i^((q-1)/g)=1` for `g=gcd(2e+1,q-1)`. At official scale

  ```text
  e=3*174763*524287,
  2e+1=7*79*8191*121369.
  ```

  The two support-only gate families therefore occupy disjoint odd-prime
  field strata. Reject on either family before choosing `xi_i,lambda_i` or
  any external block. A contributor certificate must retain the `R_i`
  values and power-residue witnesses, not only pass bits.

  The complete external design is now one resultant test, not a block
  census. Put

  ```text
  q_e(X)=[z^e]Q(z;X),
  Delta(X)=Res_z(Q,partial_z Q),
  H(z)=Res_X(C,Q),       L=Res_X(C,q_e).
  ```

  First require `gcd(C,q_e Delta)=1`. Then compute the unique monic radical

  ```text
  P_Z=monic(H/gcd(H,H')).
  ```

  The exact necessary-and-sufficient condition is

  ```text
  deg P_Z=3e,       P_Z squarefree and split over F_p,
  H=L P_Z^(2e+1).
  ```

  The prime-field collapse gives `p>deg H`, so ordinary derivatives and the
  radical are exact. On a pass, reconstruct each block by
  `{x:C(x)=0,Q(gamma;x)=0}` for `P_Z(gamma)=0`; row squarefreeness and power
  multiplicity prove automatically that every block has `2e+1` distinct
  roots. Do not allocate external slopes, blocks, locators, an incidence
  matrix, or `P_Z` as solver variables. A contributor implementation should
  use a succinct resultant/norm representation and stream reconstructed
  blocks only for independent checking; materializing the degree-`<2^79`
  resultant in WSL is out of scope.

  Prefer the sparse subgroup-norm realization of that criterion. With
  `I(z)=product_i(z-xi_i)` and
  `R_D(z)=Res_X(X^N-1,Q(z;X))`, the proved router gives

  ```text
  z R_D(z)=
    kappa_0 Q(z;s)Q(z;x_0)(zI(z))^(2e+1)H(z),
  ```

  for the explicit nonzero scalar `(SSN3)`. Under a design this is

  ```text
  z R_D(z)=
    kappa_0 L Q(z;s)Q(z;x_0)
    (zI(z)P_Z(z))^(2e+1).
  ```

  Compute the norm against the two-term polynomial `X^N-1`, exact-divide by
  the two boundary-row forms and the known internal power, and apply the
  radical/splitting test to the quotient. This is the preferred executable
  path. It must still replay the row-discriminant gcd against `C`; the sparse
  norm replaces construction of `H`, not that independent transversality
  gate. A dense product over all active rows is a cross-check only.

  At each active domain root impose the exact gcd factorization

  ```text
  K_x=-H_xJ_x,       deg Qhat_x=delta_x+epsilon_x,
  N_x=Qhat_x/E_Z^epsilon_x,
  S_*=product_x N_x,       sum_x delta_x=C_*.
  ```

  When `D_*=1`, also impose the exceptional saturated gcd degree at least
  `e+3b` and complementary quotient degree at most `c+1`. Allocate no shards
  for `K=0`, the quartic boundary, a trace-free weld, arbitrary prime-factor
  allocations, a `Z_W` exceptional allocation, or a zero exceptional trace;
  all are proved impossible. Do not run the unreduced weld as one monolithic
  elimination. Each live shard must additionally certify the exact two-sided
  partitions

  ```text
  Q_gamma A_gamma=G_X/X_0       for every clean gamma,
  Q_x V_x=P                     for every saturated x,
  ```

  with squarefree disjoint factors of exact degrees
  `(r,D_0-deg(X_0)-r)` and `(e_*,T-e_*)`. Check the active bad-row clean
  incidence total `c e_*-C_*-E_bad` before attempting elimination. Do not
  introduce independent biform coefficients for a proposed partition packet.
  First build its saturated-row by clean-slope nonincidence graph, check the
  incidence relation in both directions, and label every edge by

  ```text
  theta_(x,gamma)=F_gamma(x)/G_x(gamma).
  ```

  The graph is proved connected. Recover its row/column potentials by one
  spanning-tree pass and reject on the first inconsistent cycle. With the
  recovered clean-fiber scalars `a_gamma`, test all `r+1` vectors

  ```text
  (a_gamma [X^j]F_gamma)_(gamma in Z_cl)
      in RS[Z_cl,e_*+1].
  ```

  These tests are necessary and sufficient to reconstruct the unique
  partition-compatible biform up to scalar, and they automatically verify
  every saturated fiber. Compute the ranks of the scaled clean-locator
  coefficient matrix, scaled saturated-locator coefficient matrix, and core
  value matrix; they must agree with `sr(Q)`, be at least
  `ceil((e+1)/(b+1))>=5`, and equal `e+1` when `b=0`. Only a packet passing
  this gate should acquire Hankel-chain, adjugate, irreducibility, or
  active-trace variables.

  The bounded prime-field reference prefilter and schema are

  ```text
  background/nodes/rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction/check_packet.py
  background/nodes/rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction/packet_schema.md
  ```

  It emits a canonical packet hash and all three ranks. It deliberately
  materializes the small-analogue core matrix and does not certify primality,
  the ambient domain/support, or any post-partition Hankel condition. Use it
  for bounded pilot shards only; a positive final certificate still needs the
  complete independent checker specified below.
- **positive certificate:** print the shape, field, domain generator, endpoint
  syndrome vectors `y_0,y_1`, the primitive `Q(U,V;X)`, its left or right
  KCF/minimal-index certificate, all `T` slopes and split locators, the
  column-far no-common-locator check, component factorization, incidence
  matrix, the corresponding norm identity, and the complementary
  factorization. For a
  half-distance `A=3` certificate, print and verify the extra locator root at
  every clean slope. For `A=1`, print the fixed core, residual generator,
  Euclidean remainder, and residual norm identity separately. The independent
  checker must rebuild every Hankel matrix and verify all ranks, roots,
  weights, and degree ledgers. For an `A=1,s=1` active partition packet it
  must also print the nonincidence graph, locator hashes, recovered potentials,
  zero Reed--Solomon parity syndromes, and the three matching rank
  certificates. A rejected packet should retain a compact inconsistent-cycle
  witness, a nonzero parity syndrome, or a rank mismatch.
- **negative certificate:** an exhaustive Groebner/regular-chain or finite
  enumeration transcript for every registered field and allowed component
  packet, including saturated ideals, symmetry coverage, and independently
  checkable inconsistency witnesses. Random sampling or a solver's bare
  `UNSAT` line is insufficient.
- **interpretation:** one positive small analogue is a route fence and a
  construction template, not an official counterexample. Complete negative
  small analogues are also evidence only, but can reveal which component
  chamber or Hankel-chain identity should be promoted into a uniform theorem.
  Neither outcome changes the critical status without a proved transport.

- **high quotient-distance endpoint handoff:** no large run is executable
  yet. A future symbolic classifier for the two exact endpoint resultant
  profiles must consume
  `quotient_clean_fiber_first_jet_transversality`, retain the reconstructed
  `F,U,L,S`, set `M=2^41` and `N_sq=M+r-3`, and emit for every clean
  selected incidence

  ```text
  F_t U W_vee=-P_cl' E y^N_sq,
  dot y=-(P_cl'E/M)y^(r-2)(1-sy)(1-x_0y)/W_vee.
  ```

  It must also verify all factors are nonzero and hash the complete
  incidence/velocity multiset. It must then consume the clean-fiber
  `W_vee` interpolation normal form and triangular unit reconstruction:
  construct canonical `W_0`, but do not allocate `A_W,B_W`. Instead stream
  the Bezout-reduced Euclidean remainders

  ```text
  C_k^0=f_0d_k+r_k,       deg r_k<e,       0<=k<r,
  rho_k=-r_k,             s_k=d_k+a_minus r_k.
  ```

  Stop at the first `deg r_k>=2` and emit that remainder with the complete
  predecessor hash as an exact rejection certificate. If every residue is
  affine, reconstruct `A_W,B_W` uniquely, form the deterministic exact
  quotient `S=(LW_vee-EY^N_sq)/F`, and emit all degree-box and Hankel
  remainders. Do not compute a modular inverse or repeat the exact division:
  `l_0P_cl+f_0a_minus=1` proves the displayed formulas. No endpoint search
  variable remains after the support and incidence packet is fixed.

  The square class

  ```text
  Xi_A=Res(A,q_1) Res(A,Phi)/(Res(A,B_T) Disc(A)).
  ```

  is a mandatory consistency gate, but the proved cancellation theorem gives

  ```text
  Xi_A=(-1)^e Norm_A(Beta) Res(A,q_1)^2.
  ```

  Weighted self-duality already makes the first factor square. Therefore no
  standalone official-scale `Xi_A` run should be requested: evaluating it
  from a complete packet only rechecks an existing determinant identity. A
  checker may verify the equality on a bounded positive certificate, but it
  must do so from streamed values and treat any nonsquare as an internal
  inconsistency. The only potentially proof-producing scalar contribution is
  a separate endpoint-profile formula for `Xi_A` derived without assuming
  the self-dual/Forney packet; that is a theorem request until such a formula
  exists, not a large-compute request.

  Do not spend compute on `Res(A,q_1)/Res(A,q_e)`. The proved endpoint
  derivative-resultant identity reduces it exactly to `P_ord(0)^k_0` in the
  flat profile and `(z_min/z_max)P_ord(0)^k_0` in the swapped profile. At the
  official odd `k_0`, its square class is obtained with at most three field
  elements. This ratio occurs squared in `Xi_A`, so it cannot strengthen the
  cancelled square gate. Retain it as the exact norm certificate for
  `p_(e-1)=q_e/q_1` in an MDS/non-MDS structural classifier; do not launch a
  resultant job merely to reproduce it.

  On the MDS branch, do not assume that codimension-one Schur square implies
  GRS. The proved half-dimension route fence gives a Euclidean self-dual
  `[8,4,5]` MDS counterexample with square dimension seven and an exact
  non-GRS syzygy certificate. Any donated classifier must consume the actual
  split-incidence polynomials and Forney unit. A generic MDS/Schur-square
  recognition run has no proof value here and should not be launched.

  On the non-MDS branch, never enumerate the `binom(2e,e)` maximal minors.
  The proved annihilating-pair router reduces a positive certificate to
  independent `u,v in U_q`, complementary `e`-set zero hashes, and
  `uv=0 mod A`. A bounded compiler may search for such pairs in a compressed
  small analogue and emit the two row-combination vectors plus the quotient
  remainder. It must also print `D_u=gcd(A,u)`, `D_v=gcd(A,v)` and route to
  either `max(deg D_u,deg D_v)>=e+1` or the exact certificate
  `D_uD_v=A`, `deg D_u=deg D_v=e`. At official scale, a run is requestable only after an
  endpoint-specific algorithm finds or excludes annihilators without listing
  subsets and supplies a peak-memory/operation bound. A raw minor or subset
  fleet is expressly out of scope regardless of available containers.
  Form each gcd from `A` and the unnormalized numerator
  `sum lambda_i q_(i+1)`; do not compute `q_1^(-1) mod A`.
  Record the common complementary rank deficiency `d`, bases for both
  shortening spaces, and all `d^2` cross pairs. One witness is insufficient
  when `d>1`.

  Every retained annihilator pair must then form the exact quotient
  `K=H_lambda H_nu/A` and verify

  ```text
  [X^(h-1)] rem_(B_T)(Phi K A^(-1))=0.
  ```

  Emit the exact-division witness, a Bezout certificate for `A^(-1) mod B_T`,
  and the top coefficient. Stop on a nonzero coefficient. At official scale,
  dense arrays of length `h` or `2e` are unauthorized; a donated run must
  first provide a compressed multiplication/reduction representation and a
  bounded pilot showing its memory profile. The scalar gate is useful only
  after an annihilator candidate is found; it does not justify a blind search
  over coefficient combinations.

  The checker may replace the support reduction by the proved equivalent

  ```text
  sum_a beta_a q_1(a)K(a)=0                         (deg K<=2e+1),
  sum_a beta_a q_1(a)K(a)=Theta_2 lc(K)             (deg K=2e+2).
  ```

  Choose whichever side has a certified compressed representation; do not
  materialize both. The transcript must state the degree branch and replay
  the boundary coefficient exactly for every one of the `d^2` cross pairs.

  Independently compute the second jets from

  ```text
  F V_vee+R_XW_vee=P_clE Y^N_sq
  ```

  along every selected root, interpolate `j_gamma=W_vee,t(gamma,Y)`, and
  emit

  ```text
  D_gamma=(j_gamma-W_0,t(gamma,Y))/P_cl'(gamma).
  ```

  Reconstruct `A_W,B_W` from the first two canonical clean slopes, stop on
  the first later failure of `D_gamma=gamma A_W+B_W`, and otherwise compare
  the pair coefficientwise with the unit-remainder pair. Retain the first
  failed slope or coefficient as the exact certificate; do not store the
  full Hermite table when a streaming comparison suffices.

  Implement each fiber through the proved quotient-ring compiler modulo
  `F(gamma,Y)`. Reduce the official powers to `Y^(r-3)` and `Y^(r-4)` before
  arithmetic, and emit Bezout witnesses for every inverted class. Root
  enumeration is unauthorized. Dense coefficient arrays of length
  `r=2^39-1` are also unauthorized and infeasible: a donated official-scale
  run is meaningful only after it supplies a compressed locator
  representation with certified multiplication, reduction, inversion, and
  equality checks. Until such a representation and a measured small pilot
  exist, this remains a proof-engineering request rather than a compute
  request, regardless of available container count.

  Before emitting any fiber polynomial, compute the quotient-algebra trace

  ```text
  Tr((j+w_Yv)w^(-1))
  ```

  and compare it with

  ```text
  (N_sq+1)E'/E+N_sq q_bar'/q_bar-(r-1)q_0'/q_0.
  ```

  Stop on the first mismatch and retain the trace certificate, the four
  logarithmic derivatives, and the quotient-ring inverse witness for `w`.
  The trace must be computed from a compressed trace/resultant oracle; a
  rootwise sum or dense companion matrix is not an acceptable official-scale
  implementation.

  Retain the coefficient-plane commitment

  ```text
  W_q=span{q_0,...,q_e},       dim W_q=e+1,
  W_q^T M_0 W_q=W_q^T M_1 W_q=0.
  ```

  Verify the two zero Gram operators and the endpoint intersections
  `W_q intersect ker M_0=span{q_0}` and
  `W_q intersect ker M_1=span{q_e}` through compressed linear-operator
  certificates. Do not emit or evaluate all `(e+1)^2` scalar pairings.
  A contributor proposal must first specify a deterministic compressed
  certificate format and its independent checker; randomized projections
  may be used as pilot diagnostics but are not proof certificates.

  The same certificate must append `v=Xq_0` and verify, without changing
  basis, that the restricted Gram operators on
  `H_q=W_q+span{v}` have ranks `(0,1)`, with the sole nonzero entry
  `v^TM_1v`. Do not allocate a separate regular Kronecker block: the proved
  rank-one flag identifies it with `H_q/W_q`.

  On the exceptional roots, emit a compressed generator commitment for the
  induced weighted self-dual code and certify `G D_beta G^T=0` and rank `e`.
  Any selected maximal minor must be paired with its complementary minor and
  checked against

  ```text
  Delta_J^2 product_J beta=(-1)^e Delta_I^2 product_I beta.
  ```

  Do not enumerate the `binomial(2e,e)` minors. A useful donated classifier
  should derive a small, profile-forced set of minors from the Forney and
  resultant data and test only those with exact determinant certificates.

  The bounded `e=3,F_101` flat frame in
  `hankel_exceptional_split_incidence_self_dual_frame/verify.py` is a required
  positive control. Future donated searches should test the first larger odd
  values of `e`, but a bare frame witness or no-hit result has no official
  force. A useful run must impose at least one additional official interface:
  the Forney weight equations, placement in one multiplicative smooth
  domain, or a proved scale-dependent invariant. Record any expensive
  large-`e` search here with a pilot cost before launch; none is authorized
  under the current local or Modal budget.

  For a candidate frame, normalize columns by `q_1(a)` and compute the
  product-space rank of `U_q^2` in `F[X]/(A)` through compressed pointwise or
  modular products. If the rank is `2e-1`, emit the unique annihilating
  functional and compare its representing class with
  `C=q_1 Phi/B_T mod A` up to scalar. If the rank is at most `2e-2`, emit two
  independent annihilators as the degeneracy certificate. The `e=3,F_101`
  positive control must report rank five and recover its unique diagonal
  weight line. Dense product matrices and unbounded rank searches remain
  unauthorized; larger runs belong in this ledger for contributors.

  The MDS-Schur router does not authorize a maximal-minor census. A donated
  packet may certify the MDS branch with a structural MDS proof plus one
  systematic generator and its `2e-1` independent product witnesses. On the
  non-MDS branch it should emit one dependent `e`-column set, its complement,
  and exact null vectors for both. Either output must then be checked against
  the Forney class; a probabilistic rank estimate alone has no proof value.

  A computation retaining only the four
  aggregate resultants is unauthorized because both endpoint profiles are
  already proved compatible at that level. Before requesting donated
  compute, bank a complete small analogue, an orbit-coverage map, a measured
  pilot, and hard RAM, wall-time, storage, and dollar ceilings. A replayable
  first-jet inconsistency would reject one endpoint profile; a finite no-hit
  result is evidence only.
- **execution shape:** checkpoint by
  `(family,shape,core,m,e,q,component packet)`, omitting `core` only for
  `A=3`; stream compact certificates and hashes; stop a shard before memory
  pressure rather than materializing all split locators. Contributors may
  parallelize independent shards, but each shard must have a declared wall,
  RAM, and dollar ceiling.
- **estimated resources:** unknown until `m=2,4` pilots; likely unsuitable for
  the current sub-`$1` policy and potentially multi-gigabyte at `m=16`.
