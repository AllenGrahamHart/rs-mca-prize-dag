# Prize Resolution Roadmap — r3, the date-free plan of record

> **OPERATING PROTOCOL:** The joint end-to-end goal is governed by
> `notes/JOINT_PRIZE_RESOLUTION_PROTOCOL.md`. This roadmap selects strategy;
> the protocol controls proof status, cross-repository custody, PR procedure,
> verification, computation, and the terminal completion audit.

Supersedes r2 and the divergence-era copy (snapshotted at
`notes/roadmap_r3_20260721/PRIZE_RESOLUTION_ROADMAP_pre_r3_snapshot.md`,
custody #104). Derived from the 18-agent review of 2026-07-21
(`notes/roadmap_r3_20260721/` — ROADMAP_R3.md, gap_matrix.md,
technique_dossier.md, completeness_critic.md); every number below survived
its adversarial fact-check. Deliberately DATE-FREE: sequencing is by GATES
(events and conditions), never by calendar. The dated snapshot is archival;
this file is the guide of record and is refreshed at gate events, not on a
clock. This document is not itself a proof and changes no node status;
`dag.json` remains the single source of truth.

Mission: fully resolve both Proximity Prize grand challenges (grand list +
grand MCA), or failing that, land the strongest honest partial posture the
spec's split-award structure supports. Lanes: our proofs; audit-gated Codex
integration; upstream mining/feeding (przchojecki/rs-mca). House laws in
force throughout: one-writer, custody (#104/#155), falsification-first,
compute law + the sub-5-minute self-auth time rule (Decision 5), claim
discipline (never over-claim upstream), forced-corrections authority
boundary. The current local execution envelope is the stricter intersection
of the time and spend limits: a route-deciding job must be conservatively
under five minutes total and under `$1`. Any valuable run above either limit,
with unknown cost, or liable to exhaust the remaining credit is recorded in
`notes/PRIZE_COMPUTE_REQUESTS.md` instead of launched. Every related upstream
PR must carry its live ledger entries in a distinct **Compute requests**
section so contributors with suitable compute can accept a declared budget.

---

## 1. The two theses (why the plan has this shape)

**Engineered rows.** Official rows carry v_2(q-1) >= 41 (or a lane norm
gate). This makes every bounded-complexity witness class arithmetically
overdetermined, which is why the same technique families keep winning across
unrelated lanes — cyclotomic-norm/engineered-prime exclusions (~15 instances,
3 lanes, the only family that outright closes), extended-window/orbit
repricing, chart-carried descent (true) vs row-uniform descent (false,
twice), exact staircases, vacuous-round saturation. These are ONE phenomenon:
the finite/structured part of both problems is systematically exhaustible.
It also predicts where transfer FAILS: the quasi-random cores, where
engineering gives no purchase.

**Sweeping vs paying.** Every technique in either tree — ours and his — is
an EXHAUSTION tool. No technique on the board has ever PAID a sharp
constant. Corollary (the meta-datum): four consecutive waves, +195 nodes,
+709 edges, ZERO red closures. Reduction is exhausted; every remaining leaf
is priced at full cost. The program must either transfer its proven closers
to untried targets, or pay one shared object once — not grind 20 mathematical
sieges.
The three unifying-lemma candidates are the three legs of the only argument
shape that addresses this: exhaust structure (U1), carry the fibration
exactly (U2), pay the remainder globally at the correct window (U3).

## 2. The walls, and identification discipline

The two walls did not move and are not expected to move under sweeping:

- **The Sidon/Fourier payment** — his six-input #3, our `f2_growing_order_
  myerson` summit. Two PROVED cross-tree identifications are now available:
  his row-sharp Q atom == our F2 zero-prefix instance (Myerson identification
  chain, each link machine-verified), and the scalar-cofactor top exact shell
  of arbitrary-word L1 == one locator-prefix Q fiber
  (`l1_exact_shell_fixed_cofactor_prefix_transport`).
- **The balance line** — our theorem cap 4.73-4.83 bits short from below
  (log2 C(127,64) = 123.17 vs 127.90+, all 2,978,146 band cells); his
  packing-ceiling overhead ~1.66M bits from above. Regime-complementary,
  zero overlap, zero contradiction.

Identification count, held honestly: TWO proved (Q-atom == F2 zero-prefix;
L1 scalar-cofactor top shell == one locator-Q fiber); ONE strong lead (input
3 <-> the F2 summit); ONE speculative (atlas <-> XR cells). The Q <->
rate_half_band_closure bridge is ANALOGY-ONLY (fatal side and quantifier
mismatches; WP5 verdict "structurally incapable"). Do not promote
identifications without a machine-verified chain.

## 3. Unifying-lemma candidates (posed attackably)

- **U1 — Official-Row Low-Complexity Emptiness.** The first-work-item audit
  is now extracted in `notes/U1_OFFICIAL_ROW_NORM_GATE_TABLE.md`. It corrects
  the former schematic `2^f(w) | Norm(u)`: the banked common currency is
  `p^r | |Norm(u)| <= G(w,m)`, where `r` counts distinct prime ideals above
  the row characteristic and `p` has a lane-specific lower bound. The
  condition `v_2(p-1)>=41` is instead an engineered-prime factor filter; it
  is not 2-adic divisibility of the norm. Newton short-window is a third,
  norm-free mechanism. The table shows that HGE4 has genuine growing `r`,
  while the current WCL and C36 packets are principally one-prime candidate
  sieves. In particular, the banked C36 star packet still has `r=1` and
  ceiling `6^(n/4)/4`, so it cannot by itself derive DSP8 max-P <= 24 from
  `p>=n^2`. That flagship remains the deliverable test, but its next theorem
  must obtain Galois-separated prime ideals, a sub-`n^2` common-ideal ceiling,
  or a complete engineered-prime sieve. Until then U1 remains a roadmap
  candidate, not a DAG lemma. Ceiling, honest: U1 is a broom, not a key — it
  never touches the bracket or the summit. One additional broom instance is
  now proved in HGE4: retaining the ambient `p>n^2` norm scale at every proper
  exact-ratio level contracts its live widths to
  `h<2 ceil(m log_2(m)/(8 log_2(n)))`, deleting `55,050,457,488` official
  level-width cells. A stronger per-width norm/Vandermonde/swap predicate
  deletes additional parity-sensitive cells below that closed form, including
  top-level cells. This validates the ambient-to-level transfer mechanism but
  does not pay any surviving orbit aggregate or by itself satisfy the D1 HGE4
  purchase. The follow-on multiscale Haar norm product is the first payment
  from this transfer: it shares one defect-energy budget across every dyadic
  moment norm, prices structural zero scales by exact powers of two, and
  proves the complete exact level `m=64` empty on every official ambient row.
  The balanced-factor augmentation then extracts the previously unspent
  factor `Norm(1-zeta_O)=2` from every nonzero norm in that product. At the
  next exact level it closes every `m=128` width `h>=12`, including the upper
  widths already routed through the quarter/complement gates, and confines
  the residual to `4<=h<=11`. Only the all-nonzero Haar mask remains at
  `h=11`, and two masks remain at `h=10`. Thus `m=128` is no longer a full
  lower-quarter campaign, but it is not yet a zero-debit level close. The
  D1 uniform HGE4 purchase still requires this finite residual and the levels
  `m>=256`.
- **U2 — Exact-shell prefix descent, with two closure routes.**
  `l1_exact_shell_prefix_hankel_bridge` proves that the exact agreement shells
  of `#ImgFib_U(k+sigma)` are precisely zero fibers of the received-word
  interpolation-prefix maps, and identifies those zero conditions
  unitriangularly with the saturated Hankel equations in every sunflower
  chart. This removes an object-identification ambiguity but not the
  max-fiber estimate. The two valid routes are:

  **U2-G (global received-word prefix):** prove row-sharp flatness for
  primitive received-word exact shells and pay the quotient-periodic shells
  separately. This avoids internal rechart enumeration. The proved
  `l1_received_word_barycentric_q_scope_fence` shows that these are moving-
  weight barycentric moments `U(x)x^j/L_A'(x)`, not the fixed-column locator
  map in upstream `def:q-row-atom`. Existing locator Q, toy power-sum Q, and
  the special F2 Myerson theorem are not substitutes unless an explicit
  map-and-owner transport theorem is proved.
  The proved `l1_exact_shell_complement_toeplitz_normal_form` then removes the
  moving denominators on the smooth domain: with complement locator `M`, the
  equations are the coefficient gap
  `[Z^(n-w)]UM=...=[Z^(n-1)]UM=0`. Thus the positive target is primitive
  row-sharp flatness for received-word Toeplitz sections of the split-divisor
  variety, or a first-match decomposition of every realized section into a
  paid number of upstream prefix-affine atoms. Low-degree shifts of `U` are
  already quotiented out exactly.
  Cross-tree typing: this Toeplitz census is a strong candidate algebraic
  model for Grande Finale v3's separately open arbitrary-word list-interior
  term `U_list-int`, not merely for its locator-Q atom. Do not record an exact
  identification until upstream supplies the `U_list-int` owner definition
  and integer budget; propose `(CT1)--(CT5)` as that missing interface in a
  future PR.
  The proved `l1_exact_shell_fixed_cofactor_prefix_transport` further splits
  this target by `e=deg(U)-a`. The top shell `e=0` is exactly one locator-Q
  atom. Each `e>0` is at most `q^e` depth-`w+e` locator-prefix atoms.
  The proved `l1_official_newton_cofactor_window_router` makes the power-sum
  overlap exact on a large finite range. The strict field cap and
  `8192|p^f-1` force `p>=3583`, while the canonical reserve gives
  `p-ell_0>=3174`. For normalized degree `h`, every shell above
  `a_0=k+ell_0-1` is Newton-safe whenever
  `h-a_0<=p-ell_0`; this covers 3,175 excess layers uniformly and all words
  if `p>=n-k`. In that scope, locator-prefix Q and power-sum Q are the same
  target fibers. The router removes small-characteristic cycle bookkeeping,
  not the row-sharp max-fiber or collective Pade-graph theorem, and it does
  not turn the special F2 summit into general Q.
  The follow-on `l1_official_frobenius_checkpoint_q_router` removes the depth
  restriction without hiding a cycle loss. The cap implies
  `p>=11n/256>n/24`, so every depth has at most 23 characteristic multiples.
  Keeping p-free power sums and replacing each divisible-index sum by the
  corresponding elementary coefficient is triangularly equivalent to the
  full locator prefix. The all-depth target has two exact forms: **flatness
  of the larger coarse p-free Q fiber**, which transfers to each mixed fiber
  with zero checkpoint loss, or **conditional flatness with checkpoint values
  coalesced by the realized Pade owner**. A raw union over all checkpoint
  vectors costs `<n^453`, preserving qualitative polynomiality, but cannot
  certify the finite `q/2^128` threshold once even one checkpoint is present.
  This is theorem work, not a useful large-compute request.
  The proved `l1_official_coarse_pfree_entropy_reserve` then shows that the
  stronger coarse route is not average-obstructed. The first checkpoint is at
  least 3,175 layers beyond `d_0=ell_0-1`; four-rate binomial growth, the
  field-order lower bound, and the 23-checkpoint cap give
  `mu_free(d)<2^-28276`. Therefore ambient max-to-average inflation
  `K_d<=q 2^28148` already implies the finite target. The remaining
  checkpoint-depth theorem is this loose coarse inflation bound, or an
  owner-sensitive conditional Pade bound; image-normalized Q must still print
  its effective-image conversion.
  Sharpening with `q=p^f`, `f>=2` on every active checkpoint, and
  `d_0<=ceil(5(p+1)/44)` proves that an exactly owner-pruned F2-shaped
  residual with `max Exc_d<=2^(15(d-r))mu_free(d)` lies below `2^-3393` and
  is empty; the same coarse inequalities do not certify 16 bits per
  condition. This statement must not be applied to the full nonempty fiber.
  F2's printed constant is sufficient only after transport. The live gap is
  exact: replace its zero target, structured-extras subtraction, and
  Frobenius-sector owner by a uniform arbitrary-target subtraction with the
  received-word/Pade first-owner interface.
  The proved `l1_coarse_pfree_wronskian_distance_packing` supplies the first
  target-uniform maximum theorem on the resulting coarse fibers. Equality of
  p-free moments through depth `d` forces disjoint-tail width at least
  `ceil((d+2)/2)`, hence every `a`-set fiber is bounded by
  `floor(binom(n,s)/binom(a,s))` with
  `s=a-ceil((d+2)/2)+1`; for scalar L1, `s=floor((a+k)/2)`. This deletes all
  close-pair concentration and should be prepaid before any shift-pair
  analysis or compute. It does not finish U2-G because the exact packing cap
  can remain exponential at linear density. The positive residual is now
  narrower: prove owner-aware shift-pair/exchange compression for a
  far-separated coarse fiber, or show that the printed row numerator already
  pays the cap.
  The exact endpoint diagnosis prevents overclaiming this route. When
  `a+k>=n`, the packing quotient is at least `2^(n-a)`; because
  `q<2^256`, it cannot by itself certify a finite prize cell with
  `n-a>=128`. Conversely, on a full mixed locator prefix the ordinary
  codeword argument already gives tail width `d+1`, stronger than the coarse
  half-depth result. Keep the two successors distinct: build a new
  p-free-moment exchange theorem for the zero-loss coarse route, or use the
  existing decorated shift-pair/Pade compiler after retaining checkpoints.
  The proved `l1_coarse_pfree_tame_tail_distance_upgrade` sharpens the coarse
  endpoint before that choice. If `t<p`, the Wronskian has degree at least
  `t-1`; combined with its upper degree this gives
  `t>=tau_p=max(ceil((d+2)/2),min(d+1,p))`. Hence the ordinary Newton window
  has full `d+1` distance, and every official checkpoint collision exchanges
  at least `p>n/24` roots. The strict endpoint is necessary (`F_4` at
  `t=p`), so all successor theory and compute must start at `tau_p`.
  The proved `l1_official_first_checkpoint_split_pencil_reduction` then
  classifies the minimum width throughout `p<=d<=2p-2`: the two tails are
  split fibers of `Z^p+Q`, with `deg Q<=2p-d-1`. At `d=2p-2`, those fibers
  are affine `F_p`-lines and are excluded by their ratio set. The
  nonzero-fiber multiplicity bound gives the exact row cutoff
  `r_*(p,n)=floor((p(p-1)-1)/(n-1))`: if
  `r_d=2p-d-1<=r_*`, then
  `|X/X|>=1+ceil((p^2-p)/r_d)>n`. Hence the final `r_*` depths start at width
  `p+1`. The official relation `11n<=256p` guarantees
  `r_*>=floor(11(p-1)/256)`, but use the exact row value. At lower depths the
  remaining object is an exact higher-degree Frobenius split-pencil census.
  The proved `l1_official_split_pencil_value_capacity` removes one more axis:
  for fixed normalized `Q`, distinct split values have disjoint `p`-point
  fibers, so there are at most `floor(n/p)<=23` values and at most 253
  unordered fiber pairs. Treat the residual as a census of normalized `Q`
  records with a bounded value payload. That payload is recovered exactly as
  the squarefree gcd of the coefficient remainders of
  `(Z^n-alpha) mod (Z^p+Q-T)`; its `T`-degree is at most 23, and pair
  existence forces a rank defect in a `p` by at-most-24 matrix. This is the
  typed overlap with the split-pencil lane before generic exchange
  compression. Before retaining any such record, apply the low-complement
  closure: `2p>n` admits no pair, while `2p<=n<3p` forces
  `deg Q>=3p-n` and removes all first-checkpoint depths `d>=n-p`. At
  `(n,p)=(8192,3583)`, this starts the closed band at `4609` instead of the
  ratio-only `5599`. The number of `Q` records in the surviving band remains
  the theorem-level gap in general. In the `m=2` band it has a sharper form:
  the `s=n-2p` point complement locator `C` uniquely reconstructs a pair
  exactly when `(Z^n-alpha)/C=R^2+c` with `c` a nonzero negative square.
  Polynomial abc, with the Frobenius-degenerate branch retained, then forces
  `s=2`. Every broad `m=2` row is empty at `t=p`; at `s=2`, the complement is
  antipodal and the exact pair count is `n/2`, occurring only at depths
  `p,p+1`.
  The proved `l1_official_checkpoint_characteristic_atlas` makes this a
  finite family: only 59 `(n,p)` pairs can have `p<n`; 33 have `m=1` and are
  empty at `t=p`, 10 have `m=2`, and 16 have `m>=3`. Every successor theorem
  or compute request must name one of these atlas rows rather than range over
  arbitrary characteristics or all formal checkpoint counts through 23.
  Among the ten `m=2` tuples, six are theorem-empty and four have the explicit
  `n/2` family. No `m<=2` minimum-width compute target remains; only the 16
  `m>=3` atlas tuples retain the general eliminant problem. Within those 16,
  consume `l1_official_max_split_value_complement_census` before retaining a
  frontier. At actual value degree `h`, put `u=n-hp` and
  `ell_h=u-d+p`; that many complement roots determine the normalized pencil,
  giving at most
  `binom(h,2)floor(binom(n,ell_h)/binom(u,ell_h))` unordered pairs. This is
  an exact compression but not a polynomial payment when `ell_h` grows. At
  value capacity, polynomial abc forces
  `(n-mp)(-m^(-1) mod p)<=p`; all 16 rows violate the inequality, so `h=m`
  is empty at every depth. The precise surviving minimum-width object is now
  `2<=h=deg G_Q<=m-1`; on all four `m=3` rows it is exactly `h=2`.
  Every lower-`h` record has depressed-pencil valuation
  `ord_0(R)<=n-(h+1)p`; in particular `h=m-1` gives `ord_0(R)<=n-mp`.
  Next consume
  `l1_official_broad_checkpoint_frobenius_periodicity_exclusion`. Prime-field
  Frobenius closure of the signed-support Fourier zeros gives even period on
  every one of the seven rows with `n-mp>16`, contradicting the odd sign
  support size `p`. Their complete `t=p` strata are empty. The exact residual
  is only nine rows of shape `n=m(p+1)`, `m in {4,8,16}`, with
  `2<=h<=m-1`.
  Stratify by `h`, `ell_h`, and this valuation; do not describe or compute
  the endpoint as one undifferentiated higher-multiplicity family or
  enumerate the raw complement bound when its exponent grows.
  The coarse successor is further compiled by
  `l1_coarse_pfree_wronskian_neighbor_compiler`. Once an exchanged anchor
  subset `X` is fixed, its Wronskian determines the opposing tail uniquely.
  At formal half-depth excess `j`, certificate degree is at most `2j` for
  even prefix depth and `2j+1` for odd depth, but the admissible range starts
  at `j=tau_p-ceil((d+2)/2)`; the exact full-support certificate count is
  `R_q(t,D)=sum_i (-1)^i binom(t,i)q^max(D+1-i,0)`. The resulting neighbor
  theorem leaves exactly the `binom(a,t)` exchange-subset axis. At deployed
  linear width that axis is still exponential, so U2-G's next positive
  coarse theorem should bound the number of `X` compatible with one
  low-degree certificate and first owner. Do not spend theory or compute on
  multiplicity after `(X,W)`, which is now one.
  `l1_cofactor_depth_budget_cancellation` corrects the accounting: for
  `e<k`, the `q^e` factor cancels exactly against the `e` additional prefix
  equations under an ambient-normalized deeper-depth bound. Under upstream's
  primitive image normalization, the exact residual factor is instead the
  effective-image collapse `q^(w+e)/L_(a,w+e)`; with integer ceilings the
  additive loss is `<q^e`. The active row-sharp Q atom is only posed at one
  degree and depth `w`, and the F2 ladder/tower theorem transfers the Fourier
  model rather than max-fiber constants across depths. At the deployed rows
  the ambient slice becomes subunit at `e=2` for KoalaBear and `e=1` for
  Mersenne-31; these are also the first powers `q^e` exceeding the printed
  row budgets. Therefore U2-G's genuinely new content is **depth-uniform Q
  before collapse, then split-divisor/Pade-graph transversality after
  collapse**. Do not charge `q^e` before
  checking ambient cancellation, and do not erase the image-collapse factor.
  The proved `l1_cofactor_prefix_pade_graph_normal_form` removes the remaining
  object ambiguity for `e<k`: in reversed high-coefficient coordinates the
  `q^e` targets form one codimension-`w` polynomial graph
  `Lhat=Uhat/Qhat mod T^(w+e+1)`. Projection to the first `e` locator
  coordinates is bijective and recovers the cofactor; exact shells are the
  split-divisor intersection with this graph plus the complement gcd guard.
  Hence the positive theorem should be posed as **row-sharp transversality of
  the primitive split-divisor prefix image against every realized Pade
  graph**, not as independent occupancy of `q^e` fibers. Its ambient density
  is already exactly `q^(-w)`; the entire issue is algebraic alignment after
  first-match payments.
  `l1_full_locator_pade_section_all_cofactors` removes the former `e>=k`
  representation gap. For every cofactor degree the full reversed locator
  lies in the `w`-equation section
  `[T^(e+1..e+w)]Uhat/Lhat=0`, and exact shells are its split points with the
  gcd guard. Below `e=k` this is the graph cylinder of exact ambient size
  `q^k`; at and above the cap the reciprocal continues beyond locator degree
  `a`, with no cardinality asserted. Therefore the all-shell positive theorem
  is one uniform **full-locator Pade-section transversality** statement, with
  separate analytic treatment allowed on the two sides of the cap but no
  raw `q^e` fallback above it.
  `l1_pade_remainder_jacobian_tangent_dichotomy` then removes local rank
  collapse from the primitive branch. Writing `U=LQ+P`, the remainder
  differential is `D -> -(QD mod L)`. On `gcd(L,Q)=1` this is an automorphism,
  so the `w` section equations have full Jacobian rank and define a smooth
  local complete intersection of codimension `w`. Every rank failure lies on
  the tangent resultant `Res(L,Q)=0`; exactness puts its domain gcd roots
  inside the agreement support. The global route therefore splits into a
  tangent/common-factor first-match payment and a row-sharp split-point bound
  on a **smooth primitive Pade section**. Rank-collapse experiments on the
  primitive branch are now analytically obsolete.
  `l1_tangent_hasse_root_pinning_census` resolves the fixed-owner part of the
  tangent payment.  If `D=gcd(L,Q)` has degree `r`, then
  `D^2|U-P`; equivalently the codeword matches the received word in value and
  first Hasse derivative at every `D`-root.  The confluent map has exact rank
  `min(k,2r)`, so one exact owner supports at most
  `q^max(k-2r,0)` shell members, while the Pade Jacobian loses at most `r`
  ranks.  Exact-gcd ownership prevents support-subset overcount.  The raw
  aggregate `sum_r binom(n,r)q^max(k-2r,0)` is generally too large, so the
  fixed-owner estimate must not be summed directly.
  `l1_tangent_confluent_packet_packing` supplies the first collective
  ceiling. For every `j<=floor(k/2)`, the doubled Hasse conditions on `j`
  tangent roots plus `k-2j` ordinary agreement values form disjoint
  `k`-condition packets across distinct codewords, giving
  `sum_P binom(r_P,j)binom(a-j,k-2j)
  <=binom(n,j)binom(n-j,k-2j)`. The `j=1` case bounds all tangent mass without
  enumerating owners. In the balanced band the companion weighted-
  intersection inequality
  `sum_P binom(r_P,j)binom(omega,s-j)
  <=binom(n,j)binom(n-j,s-j)` starts at complement packing when `j=0` and
  sharpens high-degree tails for positive `j`. Its consecutive ratio is
  `(w+j+1)/(r_0-j)`: complement packing is optimal through `r_0<=w+1`, and
  the high-tail optimizer is the clipped
  `ceil((r_0-w-1)/2)`. These are field-independent
  exact ceilings and replace the raw owner sum, but can remain
  exponential in the linear band. The residual tangent task is therefore
  **packet-ceiling excess absorption** into quotient/primitive payments, not
  fixed-root interpolation or unconstrained owner census.
  Deployed log-scale calibration confirms the limitation: all-tangent
  `j=1` is about `588290/588312` bits on the two list rows, versus
  `501080/501136` for complement packing; even the maximal-degree optimized
  mixed tail is about `430829/430868` bits. No deployed profile closes from
  this inequality alone.
  `l1_tangent_double_root_descent_to_primitive_shell` gives the exact object
  after fixing one owner.  For `2r<=k`, divide out its forced double roots:
  `P=P_D+D^2R` bijects the exact-`D` tangent stratum with a primitive exact
  shell under `(n,k,a,e,w)->(n-r,k-2r,a-r,e-r,w+r)`.  For `2r>k` one owner
  has at most one member.  Thus tangency is consumed in one step and surplus
  improves; the residual obstruction is that `H\roots(D)` need not be a
  smooth domain on the profiles not paid by the packet ceiling. A positive
  route may prove puncture-stable primitive flatness, or show that those
  punctures are quotient-paid. It must not silently reuse smooth-domain Q.
  `l1_pade_split_section_support_moment_inversion` closes the object-level
  cross-tree interface.  The unguarded split count of the full Pade section
  is exactly Paper D v13.2's shifted-lattice/split-pencil support census
  `cen(U;m)`, with
  `cen(U;m)=sum_{a>=m}binom(a,m)Z_a(U)` and an exact finite inverse.  Hence an
  upstream upper bound on `cen(U;m)` immediately bounds the exact shell
  `Z_m`; no map transport is needed at this level.  What remains before
  importing an active certificate is owner-sensitive: match the
  primitive/quotient priority map, guard-pruned interior numerator, local
  shift-pair numerator, and summed adjacent-row reserve.  Do not call the
  unguarded support moment or its base-field support floor the exact codeword
  count.
  `l1_exact_shell_balanced_shifted_lattice_reduction` then removes the
  near-rational support branch from L1 entirely in the active band
  `2m<=n+k-1`.  Upstream's `d_1<=w` case is empty or one codeword with at
  least `m+1` agreements; its large binomial support moment contains zero
  complete level-`m` codewords.  Therefore every nonempty exact shell has
  `w+1<=d_1<=d_2<=omega` and lies in one guarded two-generator split pencil
  of coefficient dimension `omega-w+1`.  This upgrades the former
  "candidate algebraic model" to an exact reduction for the list-interior
  band.  The positive U2-G theorem may now be posed directly as the
  **owner-pruned, exact-guarded balanced split-pencil census**, with raw
  support-ray floors removed before pricing.  Deep shells outside the band
  retain their separate existing payments.
  `l1_deep_exact_shell_johnson_closure` makes that last sentence exact: all
  shells with `2m>n+k-1` are contained in the ordinary list at
  `m_J=floor((n+k-1)/2)+1`, whose classical Johnson bound is at most `n^2`
  (`2^88` over the full prize box).  This is the polynomial L1 payment; the
  coarse number is not by itself a finite adjacent-row budget claim.  The
  deep tail is charged once, not once per level.  U2-G now has complete range
  coverage and one unresolved object:
  the owner-pruned, exact-guarded balanced split-pencil census in
  `2m<=n+k-1`.
  `l1_band_complement_dimension_packing` pays the band-side transition before
  that census.  With `s=omega-w=n-2m+k`, exact complement locators have
  pairwise intersection at most `s-1`, yielding
  `Z_m<=floor(binom(n,s)/binom(omega,s))`.  This is `exp(O(s))` at linear
  complement density, so fixed `s` and reserve-sublinear `s` are closed.  The
  active BC/Q wall can be restricted to linear projective dimension `s` at
  the deployed frontier.
  `l1_boundary_shifted_lattice_affine_q_cell` aligns that band exactly with
  the active upstream off-by-one convention.  The boundary
  `d_1=w+1,d_2=omega` is one fixed-codeword projective point, paid by at most
  one exact member, plus the guarded affine Q cell `g_2+A g_1`; when
  `W_1=1` it is the prescribed-top-`(w+1)` locator-Q atom.  The strict
  interior `d_1>=w+2` is guarded BC.  For nonconstant `W_1`,
  quotient/residue Q coalescing remains open, as does the exact-guarded
  interior BC bound.  These are disjoint obligations and must carry separate
  finite numerators.
  `l1_interior_bc_floor_higher_shell_q_routing` removes an important false
  calibration from the list-side interface.  Paper D's strict-interior
  base-field floor at `d_1` is built from exact agreement
  `m'=k-1+d_1>m`: all `binom(m',m)` proper sub-supports fail the level-`m`
  gcd guard and cancel under inversion.  Each codeword belongs once to the
  level-`m'` boundary-Q bucket.  The raw floor remains valid for upstream's
  support/MCA consumers; `M_B^soft` remains their soft raw-census baseline,
  not concrete exact-L1 mass.  L1 must expose a separate
  `BC_exact_guarded` numerator after this cross-level first match.  Its size
  and any surviving field dependence remain open.
  `l1_polynomial_led_interior_to_deeper_q_curve` then resolves the object for
  every polynomial-led excess `1<=e<=k`, not merely the floor family.  The
  exact guarded shell is a disjoint `B^e`-curve of depth-`w+e` locator-Q
  fibers; the cofactor is solved triangularly from the first `e` locator
  coefficients.  Ambient density cancels the slice count, while discrete
  max-fiber rounding leaves `|B|^e`.  Therefore polynomial-led below-cap BC
  joins the depth-uniform Q programme, with **collective curve occupancy** as
  its finite endpoint.  At this stage separate exact BC remains for
  nonconstant minimal vectors and the above-cap primitive section.
  `l1_split_pencil_content_exact_shell_descent` then removes the cross-level
  owner ambiguity for all of those cells.  In any interpolation-module basis
  a raw member `(W,N)=A g_1+B g_2`, `N=Wc`, satisfies
  `agr(U,c)=m+deg gcd(A,B)`; the coefficient ideal is basis invariant.
  Therefore exact level `m` is exactly the coprime `(A,B)` locus, and division
  by content routes every other member uniquely to its true higher shell.
  The live BC object is now the **primitive coprime coefficient-pair
  split-pencil census**, not support-ray multiplicity or same-codeword
  coalescing.  This identity supplies no row-sharp bound on that primitive
  locus.
  `l1_boundary_q_planted_root_descent` removes the domain-root degeneracy of
  the nonconstant boundary vector exactly.  The determinant identity
  `W_1P-N_1=c_PL` makes `gcd(W_1,Omega)` one fixed planted agreement owner.
  After division, both locator degree and codeword dimension fall by its
  degree, so the Q depth stays `w`; the rigid branch costs at most one.  The
  live boundary theorem is therefore root-free **rational Q flatness**, or a
  numerator-preserving transport of that atom to polynomial-led Q.  The
  punctured domain must remain explicit because smoothness is not inherited.
  `l1_rootfree_rational_q_projective_packing` then puts that residual exactly
  inside Paper D's Conjecture-F framework: it is the full gcd-trivial
  projective intersection for a dimension-`d=k-r` space in degree
  `j=m-r`, with no split point at infinity.  The exact support packing ceiling
  `floor(binom(n-r,d)/binom(m-r,d))` pays all fixed-`d` cells and costs only
  `exp(O(d))` at linear locator density.  Hence `d=o(n)` is subexponential,
  with reserve absorption when `d=o(R log |B|)`.  The remaining boundary wall
  is therefore linear-residual-dimensional projective flatness and cross-cell
  coalescing, not the dimension-one, sublinear, or planted strata.
  Its exact second moment is now compiled by
  `l1_growing_cofactor_decorated_shift_pair_compiler`: ordered pairs satisfy
  `AQ_1-BQ_2=R` with the same `w`-deep cancellation. Scalar cofactor recovers
  upstream's shift-pair ledger exactly. For primitive cofactor pairs and
  `e<=w`, each ordered split support pair has decoration multiplicity one.
  Therefore the next positive U2-G theorem should count primitive split
  support pairs directly, while routing common cofactor gcds to explicit
  tangent/common-factor owners and treating `e>w` separately. It must not
  reintroduce a `q^(2e)` cofactor charge in the primitive `e<=w` region.
  The canonical gcd descent now composes those two exceptions: a gcd of
  degree `c` changes `(e,w)` to primitive `(e-c,w+c)` and confines all domain
  gcd roots to the common agreement core. Support-pair uniqueness therefore
  applies whenever `e<=w+2c`; only the reduced high branch `e-c>w+c` needs a
  received-word owner. This endpoint is sharp: ten exact `F_13` witnesses at
  `(e',w')=(2,1)` defeat any U-free support-only extension. The next theorem
  must consequently be a target-sensitive pair estimate, not a larger
  universal support atlas.

  **U2-L (local descent):** charts factor onto quotient charts (SUCCESSOR-A
  form); tail collapse m+1 per chart; payment transport over all dyadic
  scales; NO row-uniform strengthening (witnessed false, catch #124). The
  object-agnostic firstocc/prefix-atlas kernels prove only totality and
  disjointization; that part is imported as
  `l1_first_match_totality_scope_pin`. Axiomatize chart-local payment and
  quotient compatibility, prove the payment-transport inequality, and
  re-derive K4 / Lemma COL / qa22 as corollaries. The proved
  `l1_general_first_layout_domination` removes maximal source-layout
  composition first: fix one source and add at most `M` anchors. This route's
  non-intrinsic branch is therefore not "enumerate source layouts" or "find
  an exhaustive atlas." The proved
  `l1_fixed_source_quotient_partition_anchor_census` now also removes the
  quotient-polynomial axis in every anchored degree-`ell` common-pencil cell:
  one full source petal fixes `P` up to additive shift, so there are at most
  `M` partitions and `M 3^(n/ell)=poly(n)` complete-fiber structural keys.
  The proved `l1_fixed_source_anchored_triple_polarity_closure` then removes
  the entire fixed-polarity anchored box, including partial source cores,
  residual points outside complete fibers, and all numerator/Forney
  multiplicity. Its explicit aggregate is
  `M(R_0+1)(B_0+1)(P_0+1)16^(n/ell)n^(R_0+B_0+P_0)q^(2P_0)`.
  Therefore U2-L no longer asks for fixed-cap Forney-key enumeration. The
  proved `l1_tame_fixed_petal_refinement_census` also removes tame refinement-
  map multiplicity: for each `s|ell` with `char(F)` not dividing `ell/s`, one
  whole source petal fixes at most one degree-`s` partition up to shift, and
  all such classes cost at most `M tau(ell)<=n`. The exact local residual is
  now: pay the `n/s` fiber roles collectively at small tame scales; treat
  unanchored maps; pay growing signed
  layout/core-defect/petal polarity; and handle arbitrary petal locators
  outside one common pencil. Dense support on a source petal is not sufficient
  to supply the anchor. The `F_9` additive right-component fixture remains a
  valid guard outside the official cutoff. The proved
  `l1_official_reserve_tame_refinement_router` removes its wild branch from
  the actual consumer: at the least reserve-qualified threshold,
  generated-field order arithmetic and the `<2^256` cap give
  `ell<char(F)`, so every fixed-petal refinement is tame. This completely
  pays map supply, not the remaining fiber roles. The proved
  `l1_identity_pullback_role_payment_fence` then prevents that residual from
  being mistaken for a smaller local problem: at `s=1`, `P=X`, the quotient
  receiver and code are the original L1 instance, with `kappa=z=0`, and every
  petal is automatically anchored. Therefore an `s>=2` refinement theorem is
  useful branch removal but cannot close L1; the global exact-shell/Toeplitz
  theorem remains mandatory for the identity endpoint.
  `l1_tame_refinement_periodic_owner_obstruction` separately proves that tame
  map supply does not imply intrinsic quotient payment: an exact `F_17^*`
  chart has a complete affine-quadratic source petal and an aperiodic full
  agreement support. The next small-scale owner must cover general polynomial
  pullbacks or aggregate those aperiodic supports; it cannot simply alias them
  to `pma_exact_periodic_owner`.
  `l1_general_pullback_interleaving_descent` now supplies the exact positive
  interface for fully fiberwise cells: `f=sum_(j<s)X^j g_j(P)`, with a
  Vandermonde quotient receiver and sparse-coverage multiplier
  `q^kappa`, `kappa=sum_j max(0,k_j-b)`. Full complete-fiber partitions have
  `kappa=0`, and the proved sub-square-root theorem collapses interleaving to
  one ordinary quotient list. The residual is correspondingly sharper:
  prove the ordinary list/payment on realized, generally non-smooth label
  domains; control `q^kappa` under sparse coverage; and pay partial-fiber
  boundaries.
  `l1_full_pullback_divisibility_johnson_closure` removes the positive-gate
  part. A nontrivial fully fiberwise dyadic support cannot occur at exact
  agreement `k+ell-1`; for `s<=k`, every full-partition tame map with
  `(k+ell)^2>(k-s)n` costs at most `(n/s)^2`, and `s>k` is automatic. The
  aggregate over tame maps is at most `n^3`, with no smooth-label assumption.
  The full-partition residual is therefore the exact nonpositive Johnson gate,
  not an unqualified ordinary quotient-list problem.
  The proved `l1_full_domain_pullback_intrinsic_rigidity` now retires that gate
  too. Complete degree-`s` fibers partitioning `alpha mu_n` give
  `X^n-alpha^n=F(P)`; cyclic Galois correspondence forces `P=X^s+c`.
  Therefore every fully fiberwise full-domain support is intrinsic and already
  exact-periodic. The non-intrinsic general-pullback residual begins only with
  incomplete domain fibers, partial-fiber agreement, or loss of the fixed-
  petal anchor.
  `l1_partial_pullback_johnson_router` now pays the strict-gate part of that
  residual. With `z` agreements outside fully agreed complete fibers,
  `h_Z=ceil((k+ell-1-Z)/s)`, and sparse-coverage exponent `kappa`, every
  `z<=Z`, `h_Z^2>b(ceil(k/s)-1)` cell costs at most `q^kappa b^2` per map.
  Fixed `kappa` is polynomial across all tame anchored maps. The theorem's
  abstract frontier retains the nonpositive gate, unbounded `kappa`, wild
  decomposition, or missing whole-petal anchor; the official-reserve router
  removes the anchored wild case on the consumer scope.
  `l1_pullback_coverage_kernel_tradeoff` then removes `kappa` as a separate
  mechanism: exactly `kappa=max(0,k-sb)`, and every listed word satisfies
  `kappa<=max(0,z-ell+1)`. Hence `z<=ell-1+K` automatically supplies the
  router's `kappa<=K` hypothesis. The exact official pullback frontier is now
  the nonpositive Johnson gate, growing partial-loss excess, or missing
  whole-petal anchor.

  The proved `l1_maximal_background_anchor_injection` now supplies the local
  U2-L cell currency: every exact support cell costs at most
  `q^max(0,d-max(r,a_*)+1)`, with an explicit `(t,u,r,E)` stratum ledger.
  U2-L must transport and sum this charge after support entropy; it must not
  replace it by the weaker petal-only cofactor exponent.
  The proved `l1_raw_support_ledger_exponential_route_fence` shows that raw
  summation cannot perform this transport: a balanced legal formal profile
  makes both the root-pinning and background-anchor numerical allowances
  exponential. The next positive theorem must establish algebraic sparsity of
  feasible supports, a collective injection across supports, or a globally
  paid anchor/refinement, growing-polarity, or arbitrary-locator owner
  classification.
  Both routes must respect the proved F_23 cross-quotient obstruction and
  exact-shell ownership; neither raw support counting nor a chartwise zero
  equivalence alone supplies row-sharp flatness.
- **U3 — Pay-Structured-First + exchange compression, with the FD clause.**
  Per binding row: structured mass paid exactly (staircase/first-match/
  extended window after gating a finite accident class) + remainder confined
  to a Sidon-type cell where the exchange-compressed major/minor payment is
  valid and sharp. FD (Finite Defect): every refuted truncated ledger seen
  so far differs from a true extended ledger by finitely many gateable,
  orbit-quantized accidents — the missing composition property of catches
  #102/#119. First instance: the c2pp bulk identity (worst case 1.0662,
  monotone-decreasing slope). Cheapest adjudication: the DSP8 harness with a
  Sidon-strip preprocessing step. If live: the same restructure is owed at
  the summit and (jointly with upstream) his input 3 — the only recorded
  route onto the wall from either tree. The former ww instance is retired:
  its safe-side envelope is unproved and unnecessary to its consumer, while
  the stronger unsafe-cell extension is false.

## 4. Board anatomy

- **Counts** (refreshed from `dag.json`, the single source of truth; pinned by
  `tools/verify_orbit_census.py`): critical surface 179 PROVED / 38 CONDITIONAL /
  24 open mathematical red leaves; **math orbit** = req-closure (+alt) of the two
  grand challenges {`mca_grand`, `list_grand`} = **241** nodes. *(Q0, 2026-07-26:
  this line previously read "req-closure of `prize` = 260" — wrong root. The
  closure of `prize` is the* **submission orbit** *= 256 = 191/40/25, i.e. the math
  orbit plus a 15-node packaging spine.)* The separate submission dossier is a
  target artifact rather than a mathematical leaf — it is the submission orbit's
  25th TARGET and does not appear in the 24. The 2026-07-26 E1 and
  unsafe-at-crossing false-green audits account for the delta from the earlier
  `201/36/23` pin.
- **Wired bottlenecks** (no alt, no upstream substitute):
  `l1_mixed_petal_amplification`, `rate_half_list_adjacent_crossing`,
  `rate_half_band_closure`, + the dossier. There is NO MCA-only resolution
  (F1 pole pricing imports the base-row list threshold).
- **The true critical path:** `l1_mixed_petal_amplification` — in the
  irreducible core under every wiring including the RK world, wired into
  both grands, and the longest-stalled core leaf.
- **Minimal win sets:** unconditional = all 24 mathematical leaves + dossier
  (pure AND). `list_grand` alone = {l1, adjacent_crossing}, closing its five
  conditional ancestors. The former `17/20` RK-prune and direct-prune counts
  predated the N11 truth ruling and are retired pending a fresh route-surgery
  audit; do not cite them. The former worst-word route is retired.
- **Clean-rate scope (Conflict-4 resolved):** the proved
  `f1_pole_same_rate_scope_router` pins that base-field and tower pole pricing
  preserve `(D,kappa)` and hence the RS rate. The clean-rate MCA/list
  milestone therefore excludes both rate-half mathematical leaves. The global
  all-rate F1 dependency remains correct for the full prize. On the corrected
  board the clean-rate milestone contains 22 of the 24 mathematical leaves;
  the two excluded leaves are the rate-half band and list-adjacent targets.
- **Concentration risk:** 12 of 24 leaves and 3 of 5 demotion triggers live
  in the dli lane behind one req edge. STANDING D2 CAP: dli receives at most
  one-third of any phase's effort; any demotion event freezes further dli
  spend for one full phase while the B-WEAK-direct re-pose is drafted from
  surviving mechanism data.

## 5. Risk register (pre-registered triggers -> consequences; all live)

| Trigger | Fires when | Consequence / fallback |
|---|---|---|
| c1r3 amber-2 | round census finds K' >= 2 (watch) / > 4 (kill); worst banked 1.401644 | dli RED; strip subtree re-stalls; D2 freeze |
| c2pp reserve break | round 3 breaks the 2^21 reserve (round 2 used 14.53%) | Decision 6 reversed; B-WEAK-direct re-pose from mechanism data |
| WCL slot falsifier | admissible row + vanishing polynomial (most exposed: (1,5) remaining mass; four cells have only sample-scale powered screens and no cell has an exhaustive new census) | baseline dies at that ell -> dli RED |
| DSP8 satellite | any official row with P >= 21 | vacuous-close route dead; CR-001 (36,1) fallback forces a PRE-DRAFTED re-wire |
| HGE4 #99/#100 | F-4 minimality challenged; strips undefined | norm_gate_count false-as-posed; pin in-statement BEFORE claiming |
| w8-C9 AZC | any (h,R,8n^3) re-pin without the AZC re-run (0.5005% margin) | unsound close; standing re-run obligation |
| non-polynomial word | witness outside fiber reduction | delta* RELOCATES (see §9); certify at the relocated value |
| l1 stall persists | successive waves with zero movement | escalation: clause-(P)/floor-band-emptiness + formally price RK |
| packaging drift | grammar divergence vs his compiler | mitigated by the rolling crosswalk (Track C) |

## 6. The gates (sequencing; conditions, never dates)

- **D0 — RESOLVED BY SCOPE CORRECTION AND REWIRE.** The exact two-class
  identity exposed a consumer mismatch. The admissible rate-`1/4` row
  `q=1705*2^120+1`, `n=8192`, `k=2048` has an unsafe spending-cell receiver
  with six plants and one factored quotient-fiber non-plant while `B*=6`.
  This algebraic counterexample refutes applying W3's upper inequality at the
  unsafe endpoint, but it does not refute W3's literal safe-side claim. The
  consumer polarity was wrong: the lower side needs one witness, not an upper
  bound on every planted receiver there. Clean-rate adjacency now consumes
  `list_unsafe`, `list_safe`, and `list_corridor_ledger` directly. W3 remains
  an open background `TARGET` and is removed from the critical requirement
  path; do not restore it unless a future consumer genuinely needs it.
- **D1 — transfer adjudication.** After the Track-B poses have each run one
  F-round: if >= 3 of {DSP8 max-P, HGE4 odd-width, summit census, chamber
  pilot} + the unit-ideal pilot land, file U1 as a DAG lemma node and route
  remaining slots through it; if <= 1, U1 is lane-local folklore — keep the
  instances, stop generalizing.
- **U3 adjudication.** Via the DSP8 Sidon-strip harness: residual tightens
  toward <= 24 => U3 live => propose the JOINT BRIEF on input 3. W3 no longer
  participates in this test: its unsafe-cell extension was refuted by a
  structured fiber layout, while its literal safe-side claim is unnecessary.
- **D3 — the self-kill.** If, after Tracks A-C have each run their first
  full round of purchases, there are still zero red closures: the
  transfer/insight allocation has failed its own falsifier; revert to pure
  grind ordering, record it in loop memory, and take the submission-posture
  decision (§10). The roadmap is itself an experiment with a pre-registered
  falsifier.

## 7. The tracks

**Track N — immediate information purchases (ordered by information value):**
N1 DONE: D0 W3 scope mismatch resolved and rewired out of the prize path; no
compute request remains. N2 SCOPE DONE, LIFT OPEN: the proved
`rate_half_arbitrary_line_syndrome_router` replaces the old polynomial-fiber
launcher by the exact arbitrary-syndrome criterion `(SL1)`. Its complete
`F_7` toy census has a seven-slope witness against the `r+1=3` baseline, but
no official-row lift; `RH-NP` is recorded as a non-runnable contributor
pre-request. A lifted hit triggers the delta*-relocation fallback, not
program death. N3 DONE, NO ISSUE: `deployed_identity_prefix_owner_scope_audit`
replays all four exact adjacent attack values and proves the identity-prefix
populations are boundary/higher-shell Q or simple-pole owners, not the local
post-strip `B_ap` residual. It proves no safe row. N4 CORE DONE:
`upstream_finite_q_shortcut_route_cuts` imports the mass-aware moment-order
floor, the million-bit packing gap, and the one-pencil-versus-boundary-Q
dimension cut. The printed moment floors apply unchanged only at `tau=1`;
specialized Route-D no-go packets remain parked until they have an exact
current local consumer. N5 DONE: the Conflict-4 audit proves that F1 pole/tower
descent preserves the rate, so rate-half adjacency is not a hidden clean-rate
  premise; the current clean milestone is 22/24 mathematical leaves. N6 harness
debt: xr_highcore top-level verification DONE (six row pins, both currencies,
paid/open rank tables, 28 proved inputs, and 10 contract mutations); the KB
#107 lightweight-certificate repair is DONE. The harness-coverage sweep is
DONE and reproducible in `CRITICAL_HARNESS_COVERAGE_20260722.md`; after the
QA.22 and XR strip-classification packaging repairs it finds 49/210 green
critical-orbit nodes with local checkers, 156 markdown-only folders, five
legacy-only nodes, zero artifact-free nodes, and four truth-status
contradictions. Remediation is N11; the census itself changes no status. N7
upstream triage watch (#1010/#1013/#1019 and the open #1023--#1039 M31 wave;
no chasing). N8 governance: the
octave-31 compute-law amendment. N9 DONE, FIXED ENDPOINTS:
`dli_wcl_extended_six_slot_sparse_divisor_endpoints` replaces the six
never-scanned widened WCL leaves by exact squared-root unit ideals of
`76--142` variables and `78--147` cubic-or-lower equations. Blind affine
support scans need at least `6.4e9--1.5e22` classes and are rejected; the six
integer-certificate computations are parked as `CR-004-X6`. N10
DONE, NO FALSIFIER: the exact-support L1 chart census now gives
`43 -> 2879 -> 109391` and `33 -> 2857 -> 108600` through `n=64`; both
second doubling factors are about `38`. This is polynomial-shaped evidence
on two structured chart families, not a uniform L1 bound. The run cost about
`$0.016`; `n=128` is parked as `L1-N10-128` because the present generator has
`1,821,304,128` candidates per schedule and an estimated cost above `$4`.
PLUS the
two one-time audits: spec-to-DAG fidelity (first finding banked as
`ww_parametric_row_scope_router`; continue beyond W3 because the prize spec
is PRELIMINARY and dag `prize` is not yet fully audited against the actual
challenge) and the
falsifier POWER audit (classify every floor tested-with-power /
tested-vacuously / untested; vacuous floors get one powered round or an
honest label before entering any dossier).

N11 DONE, TRUTH BEFORE PACKAGING: all four false-green candidates from
`CRITICAL_HARNESS_COVERAGE_20260722.md` are adjudicated. `generator_economy`,
`integer_code_distance_cert`, and `u2_per_row_certifier` are restored to
`TARGET`; `far_pair_separation` is restored to `CONDITIONAL`, with the
downstream lattice/value-set/census chain regressed accordingly. The
signed-8-core budget discharge is `REFUTED`: its `2^89.0555` raw count uses
`2^52.7641` zero-sum padding copies per fixed `e_1` center, leaving at most
`2^36.2914` named centers. The exact route-fence checker is manifest-backed.
The partition-aware auto-discharge regression sweep is repaired and now has a
fail-closed verifier; it also removed one stale generated proof from the
already-amber `worst_word_challenger_pricing` node. The adopted-row distance
and Row-C per-row computations are prerequisite-gated contributor requests
`N11-ICD` and `N11-U2` in `PRIZE_COMPUTE_REQUESTS.md`, not local Modal jobs.
The serial all-verifier replay was honestly bounded by RAMguard's five-minute
wall: 847 checks passed before termination and four unrelated legacy checks
failed because they still assert superseded node statuses or statement text
(one HGE4, two XR, one DLI). The N11 refutation and regression-path checks pass
directly in normal and optimized Python; do not cite this bounded replay as a
clean full-suite result.
The formerly artifact-free `xr_strip_classification_rungs` packet and exact
QA.22 checker remain restored. Computation claims still require a pinned
result plus an independent checker; procedure totality is not a row result.

N12 DONE, E1 CERTIFICATE FALSE-GREEN CORRECTION: the two purported folded
certificate leaves are restored to `TARGET`. The `N'=128` record consisted of
rounded fpylll output with no exact transcript, completion flag, lower-bound
certificate, or independent checker. The `N'=256` DAG entry had silently
substituted an almost-all-primes density estimate for the complete named-field
zero-vector certificate still consumed by its `req` edge. These are evidence
and a quantifier mismatch, not proofs. Nine automatic consumers regress to
`CONDITIONAL` through `mca_unsafe`, giving the then-current `190/45/25` math orbit.
`tools/auto_discharge.py` is now genuinely regression-to-fixpoint and checks
failed `gate:any` alternatives; reversed-node-order and alternative-gate tests
are banked. No Modal job was launched. See
`E1_CERTIFICATE_FALSE_GREEN_AUDIT_20260726.md`.

N12-E1-256 FALSIFIER COMPLETE, NO HIT: Modal app
`ap-uImvgijoKNeruVABf32Cc9` ran the one authorized four-seed campaign in
`81.65--125.33 s` per worker. Bounded LLL/BKZ plus exact negacyclic-shift
combinations reached basis and pair infinity norm five but no vector in the
required box. The checker returns `INCOMPLETE`; no status, edge, endpoint, or
delta-star bracket changes. The run is not to be scaled. The E1 priority is
now the route-uniform density quantifier, not repeated named-field BKZ.

N13 DONE, E1 QUANTIFIER ROUTE CORRECTION: closing the two named-field
certificate leaves would still not prove a theorem over every row assigned to
the direct E1 route. The invalid exhibit-to-family implication is removed.
`e1_official_prime_exception_control` is the route-uniform `TARGET`; the
official quantifier pin and 13 named-exhibit/certificate nodes are retained as
background evidence with `ev` edges only. See
`E1_NAMED_EXHIBIT_QUANTIFIER_AUDIT_20260726.md`.

N14 DONE, UNSAFE-AT-CROSSING FALSE-GREEN CORRECTION: the proved local
`qfloor_exact` and `averaged_slope_conversion` theorems did not supply their
per-row hypotheses. "Collided" does not imply the exact post-paid occupancy
inequality, and strict unsafety requires `nu(A)>B*` with `B=B*+1`.
`unsafe_at_crossing` regresses to `CONDITIONAL` on the new universal leaf
`unsafe_crossing_family_instantiation`; `zone_b` and E1 become evidence routes
to that leaf rather than unconditional global premises. Current math orbit:
`241 = 177/39/25`; submission orbit: `256 = 189/41/26`. See
`UNSAFE_AT_CROSSING_FALSE_GREEN_AUDIT_20260726.md`.

N14B DONE, CANONICAL AVERAGED-XR FALSE-GREEN CORRECTION: reconciliation with
the Fable tree at `3cca68b7` found that `averaged_xr` had no conditional proof:
its generated `proof.md` cites a nonexistent `conditional.md`, while its sole
former requirement proves only the same-slope exponent dictionary and
presupposes the de-correlation claim. The source itself leaves worst-case
de-correlation open. Therefore `averaged_xr` is a new `TARGET`;
`averaged_slope_conversion`, `xr_gvn`, `xr_inverse`, and the clean-anchor
occupancy route cut propagate to `CONDITIONAL`; and
`xr_ledger_exponent_reconciliation` moves to background evidence. The current
board is `241=177/39/25`, and all 39 ambers still auto-discharge from the 25
red leaves. The preferred new attack is the source's Hooley--Katz / Scott
exponential-sum lane.

N14C DONE, EXACT AVERAGED-XR REPAIR: the N14B demotion remains the correct
ruling on the generated auto-proof, but upstream commit `674503f` contains a
later elementary theorem that the old DAG citation missed. For exact
`(k+t)`-supports at exchange distance `d`, the joint interpolation map has
rank `t+min(d,t)`. After `(f,g)->(f+zg,g)`, this gives the exact fixed-slope
pair probability and restricted-family factorial moment. The occupancy
conversion then follows pointwise from
`1_(X_z>0)>=X_z-X_z(X_z-1)/2`; no cross-slope independence or Hooley--Katz
input is required. The proof was independently rederived and replayed on
9,047 interpolation-matrix support pairs plus exhaustive toy counts.
`averaged_xr` and `averaged_slope_conversion` return to `PROVED`, while the
broader off-orbit `xr_gvn` claim is explicitly restored to `TARGET` because
the exact pair moment does not prove a multi-exchange inverse chain. Current
math orbit: `241=179/38/24`; submission orbit: `256=191/40/25`.

N14D DONE, `m=128` HAAR-ENERGY ROUTE CUT: an exact low-memory dynamic program
tests the first tempting refinement of the new HGE4 frontier. At `h=10`, Haar
mask `011`, the attainable energy triple `(22,24,24)` has upper product
`22^32 24^24>2^235`, over `219051` times the current divisor threshold.
Therefore integer-energy sharpening alone cannot pay this residual mask.
The target remains open, and the next attack is explicitly redirected to the
full moment/primitive equations or a genuine orbit debit. See
`experiments/prize_resolution/F3_M128_RESIDUAL_ROUTE_CUT.md`.

N15 DONE, UPSTREAM IDENTITY-PREFIX UNSAFE SUPPLIER HARVEST: upstream's
`lem:capff1-identity-prefix-floor` and `cor:capg-budget-conversion` combine to
give an exact `V` payload whenever
`C(n,m)>|B|^(m-k-1)B*` and `C(B*+1,2)k<q-n`. The general proof is
independently reconstructed and source-pinned in
`identity_prefix_flexible_budget_unsafe_floor`; its checker verifies the
strict floor conversion and the two deployed MCA instances. KoalaBear at
agreement `1116047` and Mersenne-31 at `1116023` therefore have exact
adjacent-unsafe payloads. This closes a finite deployed slice only:
`unsafe_crossing_family_instantiation` remains `TARGET` over all admissible
rows, and neither next-row safety assertion is imported.

N16 DONE, IDENTITY-PREFIX CLEAN-ANCHOR ROUTE CLASSIFICATION: writing
`M=floor(q/2^t)`, the flexible-budget pair-root premise is impossible over
the whole budget interval whenever `Mk>=2^(t+1)`, and holds over the whole
interval whenever `C(M+1,2)k<M2^t-n`. Exact application rules out the
identity-prefix supplier on five of the six clean anchors: RowC rates `1/4`
and `1/8`, and all three prize-max clean rates. The sole survivor is RowC
rate `1/16`; there `w=1`, and the prefix condition is equivalent to a proved
domain field of order at most
`194309137781254382992506402317422272798923813601398339285841609906262`.
The current RowC characteristic is explicitly unpinned, so this branch is not
instantiated. Result: the harvested supplier is exhausted as a high-field
clean-anchor strategy; those rows need `Q`, another direct `V`, or `M`.

N17 DONE, QFLOOR CLEAN-ANCHOR NORM-THRESHOLD ROUTE CUT: the six clean
predecessors have canonical quotient parameters
`(N',ell')=(256,65),(256,33),(512,33)`. The strict qfloor norm thresholds
`(2ell')^(N'/2)` have `899,774,1548` bits, respectively, while every official
characteristic satisfies `p<=q<2^256`. Thus `qfloor_exact` is inapplicable on
all six rows. Their exact raw binomial counts still exceed budget by factors
of at least `1245`; this is strong quotient-multiplicity evidence, not a
distinct ambient-slope certificate. The positive quotient route now lands
precisely on direct-E1/value-set injectivity or a replacement collision
theorem. No safety or endpoint movement follows from the route cut.

N18 DONE, E1 CLEAN-ANCHOR FINITE-ALLOWANCE COMPILER: upstream
`thm:exactcount` gives the characteristic-zero class count
`K=A_2(N,ell)` without a further global-sign quotient. For reduced-value fiber
sizes `r_y`, the exact unordered collision-pair count
`P=sum_y C(r_y,2)` satisfies `K-|image|<=P`; hence the sufficient finite
certificate is `P<=K-B*-1`. Exact `K`, `B*`, and allowances are printed and
independently replayed for all six anchors. This also corrects the old cell
notation: clean quotient orders are `N=256,512`, while `128,256` are folded
dimensions. Finally, if `B=F_p(Q)` is the quotient-generated field, then the
E1 image lies in `B`; `|B|<=B*` is therefore a proved E1 route cut. A second
exact cut comes from balanced fibers: for `K=sb+r`, every reduction has
`P>=b C(s,2)+rs`, so the pair-loss compiler is impossible below
`b_pair_min=ceil((K+B*+1)/3)`. Its six thresholds have `188,134,170` bits by
rate. The open pointwise pair target now has this noncircular high-field
domain. No row is paid and no endpoint moves: the next theorem must prove or
falsify the exact `P` allowance there, while the universal router separately
pays the impossible-E1 and direct-image-only field ranges. See
`notes/E1_CLEAN_ANCHOR_FINITE_ALLOWANCE_AUDIT_20260726.md`.

N19 DONE, TANGENT-FLOOR LOW-FIELD ROUTER: upstream `prop:floor` is
independently reconstructed as a direct `V` supplier. At predecessor
agreement `a`, it gives `e=n-a` distinct bad slopes and pays target `2^-128`
exactly when `q<=e*2^128-1`. The six clean formulas therefore have exact
maximum field orders of 138 bits on RowC and 169 bits on prize-max. This pays
a genuine low-field branch, but none of the six named high-budget envelopes:
their numerator budgets are respectively `2^122` and
`317494674775468773183020924238786383963`, both above the corresponding
`e`. The residual envelope problem is now explicitly high-field and still
belongs to direct E1/value-set, another line, or post-paid occupancy. Route
failure is not safety. See
`notes/TANGENT_FLOOR_ROUTE_AUDIT_20260727.md`.

N20 DONE, CLEAN-ENVELOPE AVERAGED-OCCUPANCY ROUTE CUT: for any support
family with witness sizes at least the unsafe predecessor agreement, FM1 is
maximized by the complete family. Its size-by-size upper bounds form a
geometric tail with ratio below `n/q<1/2`. Exact RowC binomial comparisons and
exact prize rational-entropy certificates prove the entire tail is below
`B*` at all six named high-budget envelopes. Hence
`nu(A)<=E[N(A)]<B*` before any same-slope correction, and no post-paid
subfamily can trigger the proved `M` supplier there. This is not safety and
does not bound explicit lines. The envelope unsafe frontier is now forced onto
direct `Q`/`V`, with E1 the only current route on the pair-feasible generated-
field branch. See
`notes/AVERAGED_OCCUPANCY_FIRST_MOMENT_ROUTE_CUT_AUDIT_20260727.md`.

N21 DONE, E1 PAIR-FEASIBLE AMBIENT GENERATION: if
`B=F_p(Q)` is a proper subfield of an official ambient field, then
`|B|^2<=q<2^256`, so `|B|<2^128`. Every one of the six exact
`b_pair_min` thresholds is larger than `2^128` (the smallest has 134 bits).
Therefore the pair-feasible E1 branch automatically satisfies `F_p(Q)=F`.
This removes the generated-field transfer axis from
`e1_official_prime_exception_control`; proper-subfield rows remain in the
direct-image-only or E1-impossible branches of the universal router. No
collision bound or row payment follows. See
`notes/E1_PAIR_FEASIBLE_AMBIENT_GENERATION_AUDIT_20260727.md`.

N22 DONE, E1 PAIR-FEASIBLE PRIME-FIELD REDUCTION: ambient generation still
allowed an extension field `F_(p^d)`, while the sparse-kernel interface assumes
`p=1 mod N`. On the generated branch `d=ord_N(p)`. Exact perfect-power checks
over the two budget intervals exclude every `d>1`; the four possible RowC
square roots fail parity or order. Thus every named-anchor pair-feasible row
has `q=p` and `p=1 mod N`. The remaining target is the exact pointwise
collision allowance over primes in those intervals, not an extension-field
transfer problem. No row is paid. See
`notes/E1_PAIR_FEASIBLE_PRIME_FIELD_REDUCTION_AUDIT_20260727.md`.

N23 ACTIVE, CRITICAL PROOF-ARTIFACT RECOVERY: canonical audit proved that the
historical `proof_sketch/` tree is unavailable and that the refs checker had
silently skipped hollow node folders. Local replay finds 197 hollow legacy-ref
nodes, including 44 on the critical surface and 42 of those marked PROVED;
36 critical PROVED nodes also have empty DAG statements. The DAG verifier now
pins these counts against growth. Submission readiness requires the critical
counts to reach zero through route-driven proof reconstruction or proved
replacement, not by accepting unreplayable labels or mass status churn. See
`notes/CRITICAL_PROOF_ARTIFACT_RECOVERY_AUDIT_20260727.md`.

N24 DONE, E1 FOLDED-L2 COLLISION RADIUS: odd-conjugate Parseval gives
`|Norm(alpha)|<=S^(h/2)` for the folded coefficient square mass `S`, replacing
the crude `(2s)^phi(N)` bound. Exact antipodal profile accounting, including
division by two in the all-even extremal case, excludes every swap distance
`s<=4` at `N=256` and `s=1` at `N=512` throughout both field intervals. The
live pointwise ledger now starts at `s=5` for rates `1/4,1/8` and `s=2` for
rate `1/16`. The first open bands have only two folded profiles each:
`(4,2,0),(3,4,0)` and `(1,2,0),(0,4,0)`, respectively. This is a genuine
algebraic band close, not a total collision bound or row payment. See
`background/nodes/e1_prime_field_l2_norm_collision_radius/`.

N25 DONE, E1 N=512 FOUR-SINGLETON EXCLUSION: for profile `(0,4,0)` at
`s=2`, the exact negacyclic autocorrelation variance `V` is even. The cases
`V=0`, `V=2`, and `V>=4` are paid separately by a pure power-of-two norm, an
exact primitive-power-of-two cyclotomic product, and a uniform logarithmic
deficit. In every case no odd pair-feasible prime can divide the norm. The
first `N=512,s=2` band now has one unresolved profile, `(1,2,0)`. This is one
profile close, not a total pair ledger or row payment. See
`background/nodes/e1_n512_four_singleton_collision_exclusion/`.

N26 DONE, E1 N=512 COMPLETE s=2 BAND: the remaining profile `(1,2,0)`
normalizes to 129540 signed trinomials and 748 odd-Galois orbits. Dual exact
SymPy/FLINT resultants give 746 norms. Across both full prime intervals, the
1492 complementary-cofactor windows contain only four integers, only one
divides, and its quotient is composite and `0 mod 512`. Thus no pair-feasible
prime divides any norm. Together with N25, every `N=512,s=2` collision is
excluded and the live ledger begins at `s=3`. The route-wide pair allowance
remains open. See
`background/nodes/e1_n512_trinomial_interval_norm_exclusion/`.

N27 DONE, E1 N=256 SQUARE-MASS-16 VARIANCE CUT: in profile `(3,4,0)` at
`s=5`, the conjugate-square mean is 16 and maximum is 100. An exact global
logarithmic majorant with denominator 2070 excludes every autocorrelation
variance `V>=136`; `V=0` has pure norm `2^256` and is also excluded. The
profile is reduced to positive even `V<=134`. This is an analytic reduction,
not a classification of that low-variance residual or a row payment. See
`background/nodes/e1_n256_s16_high_variance_collision_exclusion/`.

N28 DONE, E1 N=256 PROPER-CONDUCTOR EXCLUSION: if the actual folded support
differences in either first-band profile have gcd `d>1` with `256`, a
monomial normalization places the vector in a cyclotomic subfield of degree at
most 64. Its nonzero small-field norm is at most `18^32<2^250`, and the
full norm is a power of that integer, so no live row prime divides it. Every
surviving `N=256,s=5` collision therefore has full conductor. The stronger
shortcut "low variance implies proper conductor" is false: a bounded
17,920-state falsification run found, and the local verifier exactly replays,
a full-conductor profile-`(3,4,0)` vector with `V=36`. The next attack must
classify the full-conductor low-variance residual rather than periodic lifts.
See
`background/nodes/e1_n256_proper_conductor_collision_exclusion/`.

N29 DONE, E1 N=256 2-ADIC COFACTOR GATE: total ramification identifies the
root multiplicity `mu` of the folded polynomial modulo two at `X=1`
with the 2-adic valuation of its cyclotomic norm. The exact L2 norm bounds and
`p>2^250` force `mu<=5` in profile `(3,4,0)` and
`mu<=16` in profile `(4,2,0)`. Thus the four-singleton
reduction in the first profile is not divisible by `(X+1)^6`, and the
two singleton exponents in the second are not congruent modulo 32. This is an
exact route-uniform screen, not a close of either profile. Apply it before
residual norm work. See
`background/nodes/e1_n256_2adic_cofactor_collision_exclusion/`.

N30 DONE, E1 N=256 SIGNED-CHORD GATE: in profile `(3,4,0)`, the
21 support chords have baseline squared weight 102. Diameter chords form a
matching of weight at most 21. Expanding the exact negacyclic energy gives

```text
V/2=102-D_64+2C.
```

The currently sharpened residual `V<=76` therefore forces signed
repeated-distance cross sum `C<=-22`. Every live support has an
oppositely signed pair of equal
non-diameter chords and hence a three-term-progression or four-point
parallelogram relation. This removes all circular-Sidon supports and turns the
next task into an additive-template classification; it does not yet exclude
those templates. See
`background/nodes/e1_n256_s16_signed_chord_collision_gate/`.

N31 DONE, E1 N=256 LOCAL-NORM COFACTOR COLLAPSE: explicit local reciprocity
for `Q_2(zeta_256)` gives `R/2^mu=1 mod 256` for every
nonzero integral norm. Since the live prime also satisfies
`p=1 mod 256`, a collision cofactor obeys
`m/2^mu=1 mod 256`. In profile `(3,4,0)`, `m<64`
therefore collapses to the five values `m=2^mu`,
`1<=mu<=5`; the odd norm part must itself be the row prime. In
profile `(4,2,0)`, the cofactor window contracts to 419 explicit
values. A 513-resultant FLINT falsification run found no congruence failure,
but the proof is the local reciprocity norm-group theorem. See
`background/nodes/e1_n256_local_norm_cofactor_collapse/`.

N32 DONE, E1 N=256 SPARSE-L1 VARIANCE REFINEMENT: the positive-half
autocorrelation has at most 21 nonzero integer coefficients. If its energy is
`E=V/2` and L1 norm is `L`, then
`E>=3L-42`, yielding a variance-dependent conjugate-square ceiling.
Five exact logarithmic majorants exclude every even `V` from 112
through 134. The profile-`(3,4,0)` residual is now positive even
`V<=110`; N33 below sharpens this further. This is a twelve-value
analytic exclusion, not a close of the remaining 55 variance values. See
`background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/`.

N33 DONE, E1 N=256 CHORD-DEFICIT VARIANCE REFINEMENT: the raw chord
magnitudes in profile `(3,4,0)` are three `4`s, twelve `2`s,
and six `1`s, with total magnitude 42 and square mass 102. For every
non-diameter distance class, the square-energy cancellation deficit `Q_d`
and L1 cancellation loss `H_d` satisfy `Q_d<=4H_d`; diameter chords
obey the same factor-four charge. Consequently

```text
4L<=E+66.
```

Two additional exact logarithmic majorants exclude `V=106,108,110`.
Together with N32, all fifteen even variances from 106 through 134 are
excluded, leaving positive even `V<=104`. The signed-chord cross sum
therefore satisfies `C<=-15`; N34 below sharpens both bounds. This
remains a structural reduction, not a close of the 52 live variance values or
profile `(4,2,0)`.
See `background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/` and
`background/nodes/e1_n256_s16_signed_chord_collision_gate/`.

N34 DONE, E1 N=256 LOW-SLACK ENDPOINT REFINEMENT: for a non-diameter
distance class, the exact slack in the factor-four chord charge is

```text
delta=(S-2)^2+4r+3t-4,
```

where `r,t` count magnitude-two and unit chords and `S` is the
absolute class sum. The `delta=0,2` classifications show that
`E=52` forces `L<=28` and `E=51` forces `L<=27`.
Two exact logarithmic majorants with `(B,C)=(72,1600)` and
`(70,1568)` exclude `V=104` and `V=102`. The current residual is
positive even `V<=100`, and the signed-chord gate strengthens to
`C<=-16`. No exploratory partition computation is load-bearing. This is
still a route reduction rather than a close of the residual or profile
`(4,2,0)`. See
`background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/`.

N35 DONE, E1 N=256 OPTIMIZED QUADRATIC MAJORANT: the low-slack ledger also
gives `L<=28` at `E=50`, although that ceiling is geometrically sharp.
For `0<x<=72`, the exact majorant

```text
log x <= log 16+1/150+(23/336)(x-16)-(x-16)^2/1344
```

has derivative roots 14 and 48. Degree-four, degree-six, and degree-three
rational Taylor certificates verify its two minima and the final six-bit
decay. It excludes `V=100`, leaving positive even `V<=98`.
A 16-worker Modal route test (`ap-XfP3XD3lCoE4sCUmTfC3PA`) found a
full-conductor `E=50,L=28` witness in every worker, falsifying the
stronger geometry-only shortcut. A one-container exact norm replay
(`ap-Aq7Pqe17R47TNQMFyu1oT2`) found a representative norm of 233 bits;
both experiments are non-load-bearing. See
`background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/`.

N36 DONE, E1 N=256 SLACK-SIX AND SECOND OPTIMIZED MAJORANT: extending the
exact local slack classification through `delta=6` gives

```text
E=49 => L<=27,
E=48 => L<=26.
```

The derivative-root `(14,48)` majorant from N35 excludes `V=98`.
A second exact majorant with roots `(14,46)`, linear coefficient
`11/161`, and quadratic coefficient `1/1288` excludes `V=96`.
The residual is positive even `V<=94`, and the signed-chord gate
strengthens to `C<=-17`. Both arguments use short rational Taylor
certificates and no new computation. See
`background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/`.

N37 DONE, E1 N=256 SLACK-NINE AND TIGHT-INTERCEPT MAJORANTS: exact charge
decompositions give

```text
E=47 => L<=25,
E=46 => L<=26,
E=45 => L<=25.
```

Derivative-root majorants with pairs `(14,45)` and `(14,46)`, using
allowances `1/150` or `1/160` as appropriate, exclude
`V=94,92,90`. The residual is positive even `V<=88`, and the
signed-chord gate strengthens to `C<=-19`. All minimum and six-bit
checks are exact rational Taylor inequalities. See
`background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/`.

N38 DONE, E1 N=256 RELAXED SLACK TABLE AND QUADRATIC ENDPOINT: a stated
finite recurrence computes the minimum possible energy in an enlarged chord
relaxation for each global slack through 13. It gives

```text
E=44 => L<=24,
E=43 => L<=23.
```

Root pairs `(14,44)` and `(14,43)`, both with allowance
`1/160`, exclude `V=88,86`. The residual is positive even
`V<=84`, and the signed-chord gate strengthens to `C<=-20`.
At `E=42`, however, the relaxed optimum returns to `L=24`; the
specific derivative-root templates used above no longer supply six bits.
This is a route-decision point, not a proof that every quadratic or
higher-moment majorant fails.
See `background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/`.

N39 DONE, E1 N=256 LAYERED THIRD MOMENT AND CUBIC ENDPOINT: the formal
`E=42,L=24` ceiling is geometrically attainable, so an `L<=23` repair is
false. For the full `E=42,L<=24` locus, expand the absolute negacyclic
autocorrelation into nested integer level sets. Each ordered layer triple
loses every pair summing to zero, and exact substitution over all 42 possible
integer magnitude profiles gives

```text
M_3<=3660.
```

The worst layer ledger is the profile with nine magnitudes two and six
magnitudes one. The cubic Hermite interpolant to `log` at 14 and 60 is a
global majorant because the fourth derivative of `log` is negative. Its
positive leading coefficient and the moment cap put the average logarithm
strictly below `(125/32)log 2`, excluding `V=84`. The residual is now
positive even `V<=82`; `C<=-20` is unchanged. The exact proof uses no
Modal result. See
`background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/`.

N40 DONE, E1 N=256 SECOND CUBIC ENDPOINT: the same exact mechanism continues
one row lower. The relaxed slack table excludes `L=26,25,24` at `E=41`,
so `L<=23`. Among the 39 compatible integer magnitude profiles, the nested
layer count gives

```text
M_3<=3438,
```

with worst layer ledger `(n_1,...,n_6)=(5,9,0,0,0,0)`. Reusing the cubic
Hermite majorant at 14 and 60 puts the average logarithm strictly below
`(125/32)log 2`, excluding `V=82`. The residual is positive even `V<=80`,
and the signed-chord gate strengthens to `C<=-21`. See
`background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/`.

N41 DONE, E1 N=256 THIRD AND FOURTH CUBIC ENDPOINTS: extending the exact
relaxed slack recurrence through global slack 21 gives `L<=22` at `E=40`
and `L<=21` at `E=39`. The 34 and 29 compatible magnitude profiles have
nested-layer caps

```text
M_3<=3224,       M_3<=3018,
```

with worst ledgers `(4,9,0,0,0,0)` and `(3,9,0,0,0,0)`. Cubic Hermite
majorants at `(14,58)` and `(14,57)` have exactly certified positive
six-bit margins, excluding `V=80` and `V=78`. The residual is positive even
`V<=76`, and the signed-chord gate strengthens to `C<=-22`. The best tested
two-contact cubic at `V=76` misses by about `0.002625`, so the next attack
must add information rather than continue this cubic family mechanically.
See `background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/`.

N42 ROUTE DECISION, E1 N=256 VARIANCE 76: continuous optimization confirms
that the two-contact cubic route misses by `0.0025927093`; the elementary
quartic moment dual collapses to the same cubic. The exact replacement target
is now a weighted Schur bound `T(A,B)<=2806` for nested symmetric layers of
sizes 28 and 16. The strongest structured example found is 2718, while actual
seven-term `E=38,L=22` witnesses stayed at or below 816 in 9,348 sampled
visits. Equality in the slack recurrence reduces the chord origins to 24
signatures, no unit diameter, and at most four positive-slack classes. The
next proof should use that finite signature list or a cyclic compression
inequality; generic SAT and further cubic scans are explicitly fenced off.
See
`background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e38_route_report_20260727.md`.

N43 DONE, E1 N=256 AUTOCORRELATION-SUBFIELD CUT: at `V=76`, the exact
slack recurrence gives `L<=22` and hence conjugate squares at most 60. If all
nonzero autocorrelation distances are divisible by four, then
`beta=F(zeta)conjugate(F(zeta))` belongs to `Q(zeta_64)`. Its small-field
norm `N` satisfies `0<|N|<=60^32<2^250`, while the full norm `R` obeys
`R^2=N^4`; no pair-feasible row prime can divide `R`. This removes the
structured weighted-Schur example of value 2718 and forces the live
`V=76` route to contain a nonzero distance outside `4 Z/128 Z`. See
`background/nodes/e1_n256_s16_autocorrelation_subfield_exclusion/`.

N44 DONE, E1 N=256 VARIANCE-76 QUOTIENT-SCHUR CLOSURE: the exact mod-16
fiber bound was exhaustively optimized over 43,153,083 admissible nested-layer
allocations. For the exceptional profiles `(6,8)` and `(2,9)`, the caps in
`Z/128 Z` are 2782 and 2580; after division by two, the caps in `Z/64 Z` are
2760 and 2422. For `(9,5,1)`, the outer 30-point Schur term is at most 840,
the two-point top-layer triple is zero, and the full cap is 2796. Every other
profile is at most 2668. Odd outer support uses the first census, support in
`2Z` but not `4Z` uses the divided census, and the proved subfield cut removes
the `4Z` chamber. Hence every live `V=76` row has `M_3<=2796<2806`; the exact
cubic certificate excludes it and improves the profile-`(3,4,0)` residual to
positive even `V<=74`. See
`background/nodes/e1_n256_s16_e38_quotient_schur_exclusion/`.

N45 DONE, E1 N=256 VARIANCE-74 QUOTIENT-SCHUR CLOSURE: at `E=37`, the exact
slack recurrence gives `L<=21`, and only three of 29 magnitude profiles exceed
the cubic threshold 2592. A complete 19,732,753-allocation quotient census
closes `(1,9)` and the outer term of `(8,5,1)` directly. For `(5,8)`, the
`B not subset 4Z` chamber is at most 2576. In the remaining chamber, all 6,435
symmetric 16-point inner layers in `Z/32 Z` satisfy `R(B,B,B)<=174`; maximizing
that replacement allocation by allocation gives 2560. The full live-row cap
is therefore `M_3<=2576<2592`, so the exact cubic excludes `V=74` and improves
the profile-`(3,4,0)` residual to positive even `V<=72`. See
`background/nodes/e1_n256_s16_e37_quotient_schur_exclusion/`.

N46 DONE, E1 N=256 VARIANCE-72 QUOTIENT-SCHUR CLOSURE: at `E=36`, the exact
slack recurrence gives `L<=20`, and only three of 26 magnitude profiles exceed
the cubic threshold 2377. A complete 8,144,380-allocation quotient census
closes `(0,9)` and the outer term of `(7,5,1)` directly. For `(4,8)`, the
odd-outer, inner-outside-`2Z` chamber is at most 2208. In the remaining
chamber, a separate complete census of all `binom(31,8)=7,888,725` symmetric
16-point subsets of `Z/64 Z` proves `R(B,B,B)<=174`; maximizing that
replacement allocation by allocation gives 2344, while the divided chamber
is 2332. The full live-row cap is therefore `M_3<=2344<2377`, so the exact
cubic excludes `V=72` and improves the profile-`(3,4,0)` residual to positive
even `V<=70`. See
`background/nodes/e1_n256_s16_e36_quotient_schur_exclusion/`.

N47 DONE, E1 N=256 VARIANCE-70 QUOTIENT-SCHUR CLOSURE: at `E=35`, the exact
slack recurrence gives `L<=19`, and only two of 21 magnitude profiles exceed
the cubic threshold 2162. A complete 2,946,287-allocation quotient census
closes `(3,8)` at 2152. For `(6,5,1)`, the outer-only odd cap 460 misses the
sufficient target 458 by two, but only four of 104,750 outer allocations reach
that chamber. Exhausting all 276 compatible middle/top nestings bounds their
full three-layer objective by 2054; all low outer cases are at most
`458+1704=2162`, and divided cases are at most 2158. Thus the exact cubic
excludes `V=70` and improves the profile-`(3,4,0)` residual to positive even
`V<=68`. See
`background/nodes/e1_n256_s16_e35_quotient_schur_exclusion/`.

**Track A — conservative backbone:** unit-ideal certificate pilot at the
(1,5) three-variable ideal (retires the census model for all 10 slots if it
lands). The minimal Singular image now works, but the exact 52-variable
global-`dp` lift and the exact 49-auxiliary elimination both timed out cleanly
at 240 seconds over `F_32003`. A python-flint successor reproduced the native
Singular through-128 term sequence, completed exponent 256 in `3.729` seconds,
and pinned the resulting five three-variable polynomials by content hash.
The expansion bottleneck is retired. A compiled F4 pilot now ingests the
exact `20,721,921`-byte input (SHA-256
`c7b87cdf08b13210480aa6d6cad4a0774247328954c81757226277bca54f46cf`).
Both `msolve 0.7.5` and current `0.10.1` made sustained progress but timed out
after `240` and `210` seconds without a basis. Therefore the five-minute
self-authorization gate did not land: no integer reconstruction or longer
local run is funded. A different ordering/engine attempt is external request
`CR-004-MSOLVE-LONG`, with an independently replayable modular identity or
compatible point required. Large basis or reconstruction runs belong
in `PRIZE_COMPUTE_REQUESTS.md` for outside contributors, not on the remaining
Modal credit. Canonical pin `0ae71ef1` also isolates a cheaper partial route:
the `243,567`-orbit order-256 mixed-parity coset layer is estimated at
`7--25` CPU-hours and `$2--$5`. It is recorded as external request
`CR-004-S1`, together with the prerequisite promotion of the reported
small-order/symmetric probable-prime results to replayable Pocklington
certificates. Even a complete S1 packet pays only about `11.98%` of the
`(1,5)` orbit space, so the three-variable unit-ideal certificate remains the
preferred closure route. Canonical pin `a222b5f5` adds deterministic powered
screens on 934 sampled orbits across `(1,5)`, `(1,6)`, `(1,7)`, and `(2,7)`:
zero events/candidates and maximum observed `v_2(q-1)=24` against gate 41.
This is survival evidence with a rough-odd-part cofactor blind spot, not a
census subtraction. It does not justify scaling the screen; all complete
factor/certificate campaigns remain the outbound CR-004 requests. Continue
with the Job A
finish only as a maintainer spend line item, after the re-shard +
ECM repairs; the order-1024 Norm(u) soundness fix (precondition for any
(2,7)+ contributor request); dli amber maintenance (c1r3 round 3 after N8;
c2pp round 3) with the reversal contingency pre-drafted; the local
rate-half seam ({2^39, 2^39+1} via the uniform Hankel split-pencil bound in
`critical/nodes/rate_half_band_closure/attack.md`; this extends the determined
window to ~(2^39+2)*2^128); the former
`xr_tangent_support_mismatch_bridge` red is closed by an
obligation-preserving scope contraction: support-local LineRay
transversality routes the former combined nongeneric `16n^3` obligation
verbatim into P-A2. P-A1/P-B retain the original generic `8+8` allocation;
the full-zero descent is now the P-A2 attack, not a third red.

**Rate-half seam route fence:**
`rate_half_ca_hankel_strict_m1_corefree_five_slope_route_fence` is PROVED.
At the exact `m=1` strict analogue, the cap fails `5>4` on a core-free
constant-rank Hankel pencil; the complete `560`-locator census finds exactly
sixteen maximizing lines and all sixteen pass Hankel compatibility. This is
not an official counterexample: every survivor is rank-two/separated. It
rules out a scale-uniform incidence or Hankel-only proof and makes the
official `m>1` separation-rank and non-pullback inputs mandatory.

The distance-three face now has an additional theorem-scale gate:
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quadratic_locator_rank_gate`.
For any surviving external design, the quadratic Veronese matrix of the
`6e+3` monic row-locator vectors has rank at most `3e+1`, not merely the
generic degree bound `4e+3`. Thus an official packet carries at least `3e+2`
row dependencies and lies on at least `e(e-3)/2` independent quadrics. This
is a cheap packet rejection test and a possible classification route; it
does not yet exclude the low-rank family.

The sharper
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_complement_residue_rank_three_gate`
reduces that family further. If `I` is the internal-slope locator and
`H_x=P_Z/G_x` is an active row's degree-`2e` external complement locator,
then all `6e+3` classes `H_x mod I` span dimension at most three. A simple
kernel count also forces the full complement locators to span dimension at
most `e+4`, before the internal slopes are chosen. A simple `e=4` biregular
design has full complement span nine above the permitted eight, and residue
rank four, so this is genuine pair-Lagrange structure rather than incidence
bookkeeping. The next
theorem-level target is classification of split divisor families with this
rank-three residue property, coupled to the exact replication ledger.
The residue rank is exactly the span dimension of the quadratic exceptional
pair locators. The proved pair-locator Mobius dichotomy identifies the only
rank drop: rank two means every exceptional pair is an orbit of one common
Mobius involution; all other pairings have rank three. Treat the Mobius branch
as a subgroup-intersection/quotient classification, separately from the
generic rank-three complement family.
The proved Mobius subgroup reduction closes the nonspecial part of that
rank-two branch. The explicit `32N^(2/3)` subgroup-curve bound is below
`2^33`, while the official matching has `2^39-2` ordered points. Only the
two genuine dihedral involutions survive: antipodal pairs `a<->-a` and
constant-product pairs `a<->c/a`. The next rank-two work should spend the
boundary and dual-residue gates on exactly those two forms; no general
Mobius search or compute request remains.
The boundary-power substitution now narrows those forms further. Every
antipodal and every constant-product packet requires `gcd(e,p-1)` to be
`e/3` or `e`. The apparent reciprocal alternative has exact normal form
`c=sx_0` and `T={u,t,c/t}`, with `u^2=c`, but its triple boundary ratio is
`(u/t)^3`. The required `e`-th-power equality gives `(u/t)^(3e)=1`, which is
impossible because `u/t` lies in `mu_N`, `gcd(3e,N)=1`, and `u!=t`.
Therefore only the two high-order field strata remain for the dual residue
and split-design gates.
The proved high-order-field nonemptiness fence supplies recursive Lucas
certificates for one official-interval prime in each stratum, and both
examples have `gcd(r,p-1)=1`. Thus neither stratum can be removed by
congruence or primality considerations, and the dual residue gate is
automatic on valid fields in both strata. A uniform rank-two proof must use
split-pencil structure in the `gcd(r,p-1)=1` subcase; a field scan is not a
proof route.
The dual-residue substitution is also complete at orbit level. In either
dihedral branch the degree-`2e` pair expressions reduce to
`R_i=kappa W(u_i)E'(u_i)^2`, where `E` is the degree-`e` orbit polynomial
and `W` has degree seven. All `e` power-residue tests are equivalent to one
split-algebra equation

```text
Y^r = kappa W(E')^2 mod E,       deg Y<e.
```

When `gcd(r,p-1)>1`, the rank-two target may use this equation jointly with
the boundary-power identities. When `gcd(r,p-1)=1`, it is automatic, so the
target is instead to exclude the resultant perfect-power split design for
the two dihedral orbit forms. Work in the nontrivial residue subcase should
use this orbit equation; re-expanding both members of every exceptional pair
discards the proved reduction.
The sparse subgroup norm needed by that perfect-power test now descends to
the involution quotient. In the antipodal branch it is

```text
Res_U(U^(N/2)-1,V_-(z;U)),       deg_U V_-<=r.
```

In the constant-product branch the quotient locator is the exact square-root
part of `D_N(U,c)-2` after removing zero or two fixed-point factors, and the
same norm is a degree-at-most-`r` orbit resultant plus those explicit fixed
evaluations. This halves the norm domain and makes the dihedral symmetry
native to the perfect-power test. More strongly, an exact-degree `Q_z` splits
over `mu_N` if and only if its descended degree-`r` polynomial splits over
the quotient orbit set. The next theorem target is therefore a uniform bound
on split members of these two structured orbit-polynomial families, or a
multiplicity/factorization obstruction for their quotient resultants after
the known `Q(z;s)Q(z;x_0)(zI(z))^r` factors are removed.
The quotient external-product ledger adds the exact multiplicity target. If
`C_2` locates two-active-row orbits and `C_1` singleton active orbits, the
`3e` monic external factors obey

```text
product_z V_z=C_2^(2e)C_1^e.
```

The two row polynomials in an orbit can coincide only at `u=-sigma_2` in the
antipodal branch or `u=sigma_1-sigma_3/c` in the constant-product branch.
Every nonexceptional paired row set is actually disjoint across all external
blocks: a hypothetical common slope forces `J=0`, after which the row value
is the nonzero `Phi E`. Hence, if the exceptional orbit is absent, all `3e`
factors are squarefree and their aggregate simple-root mass is `3er`. If it
is present, exactly `e` factors have that same one double root and the simple
mass is `3er-2e`. The multiplicity pattern is now fully classified; the next
argument must use the structured coefficients or product identity rather
than seek a stronger generic squarefreeness estimate.
Those coefficients now give a finite-dimensional divisor formulation. For
each nonexceptional two-active-row orbit, the complement of its two disjoint
row locators is a split squarefree degree-`e` divisor `K_u` of `P_Z`. All
such divisors lie in the exact four-space

```text
span{I,M_0,M_1,M_2},
K_u=a_uI+chi(u)(u^2M_0-2uM_1+M_2),
```

and their projective coordinates satisfy `b_1^2=4b_0b_2`. Boundary orbit
counting and injectivity give at least `3e-2` distinct divisors on the
antipodal branch and `3e-3` on the constant-product branch. The abstract
quadric-count route is now closed negatively by
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_abstract_quadric_divisor_route_fence`.
For every `e>=3`, a uniform three-pencil one-root-swap construction places
`6e+1` split degree-`e` divisors of one squarefree degree-`3e` polynomial on
a rank-three quadric cone in one projective three-space. Thus degree,
divisibility, four-space dimension, cone rank, and cardinality cannot close
the packet.

The remaining rank-two theorem therefore had to use the calibrated data
omitted by that construction:

```text
mu_i=P_Z(xi_i)/lambda_i^2,
K_u(xi_i)=chi(u)mu_i(u-u_i)^2,
```

together with the exact subgroup-orbit coordinates and external product
ledger. This target is now closed by
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_dihedral_trace_collision_exclusion`.
For every external root `gamma`, the calibrated formula defines one
quadratic `q_gamma(U)`. Each complement selects exactly `e` quadratics with
the same value, while saturated incidence forces every quadratic to be
selected at least `e-4` times. Distinct quadratic classes collide at no more
than two orbit coordinates. For `e>=31`, the resulting double count forces
exactly three classes of size `e`, hence at most three complements, against
the required `3e-3`. This excludes both dihedral distance-three branches on
the official `e=2^38-1` row. The exclusion closes this Hankel boundary
packet, not the full rate-half band target.

The generic rank-three branch remains, but one tempting continuation is now
closed negatively by
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_generic_schur_square_saturation_route_fence`.
Rank-three pair locators do not force the quadratic coefficient space to
attain the abstract `3e+1` cap. For arbitrary `e`, selecting pair factors
from distinct fibers of one cubic rational map `B/R` keeps
`dim span{D_i}=3` while a printed nonzero functional annihilates every
quadratic product, giving `dim(VV)<=3e`. The exact `F_101`, `e=12` packet has
ambient rank 37 and product rank 36; replacing one fiber pair restores rank
37. Therefore the next generic theorem must combine the conic residue packet
with exact external incidence, boundary values, or the resultant power. It
must not assume Schur-square saturation from pair-locator rank alone.

The defect itself is now completely classified by
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_generic_schur_defect_trigonal_fiber_classification`.
For `V=span{A,BA/D_i}`, the exact identity

```text
(3e+1)-dim(VV)
 =dim{(R,y):deg R<=2 and D_i divides R-y_iB for every i}
```

splits the generic branch without search. Full rank is the saturated branch.
The recovery space has dimension at most one, so the only other rank is
exactly `3e`, with one projectively unique degree-three rational map `B/R`;
all but at most one pair occupy distinct fibers. On an external packet,
`dim(VV)` is exactly the quadratic locator-matrix rank. Future work therefore
initially had two honest generic targets. The trigonal target is now closed
by
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_official_trigonal_subgroup_exclusion`.
A nonzero recovery kernel would put `2e` ordered exceptional pairs on one
bidegree-`(2,2)` rational-map coincidence curve. After two explicit torus
coordinate repairs, the worst published subgroup bound is
`1440N^(2/3)<2e`; geometric reducibility would instead force an order-three
Mobius deck map, whose only subgroup-heavy forms are incompatible with the
order-`2^41` group. Thus every official generic packet has quadratic rank
exactly `3e+1`. The sole honest generic target is now to use those full-rank
quadratic equations together with the exact external incidence/resultant
power. There is no intermediate rank-drop case and no trigonal fleet to run.

The first saturated shortcut is now fenced by
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_saturated_cyclic_design_residue_route_fence`.
Over `F_151`, an exact `e=5` cyclic `1-(15,5,11)` design has all `6e+3`
blocks distinct, quadratic locator rank exactly `3e+1`, and complement span
exactly `e+4`. Hence biregularity plus both uncalibrated rank shadows still
does not exclude the chart. The same fixture has residue rank at least four
modulo every degree-`e` internal locator with nonzero constant term. The live
saturated theorem must use the actual calibrated rank-three classes
`H_x mod I` together with replication, boundary, or resultant power. A
classifier or donated computation that retains only quadratic rank and full
complement coefficient rank is now known to target a false implication.

The proved
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_calibrated_conic_kernel_lift_normal_form`
now isolates the information omitted by that false route. After scaling by
`s_x=B(x)G_x(0)`, every complement is

```text
R_0+xR_1+x^2R_2+I J_x,       deg J_x<=e,
```

and the product over all active rows is exactly `kappa P_Z^(4e+2)`. The
`R_j` are independent on the live generic branch. The next theorem must
control the `J_x` from this power identity and incidence, or decompose the
lifted family into a certified number of genuine projective pencils. The
residue conic by itself is not eligible for a one-pencil moving-root payment.

The first-jet continuation is now PROVED as
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_cleared_lift_quartic_router`.
After clearing `A B q_e`, one obtains a biform of bidegree at most
`(2e,4e+6)` whose external fiber is

```text
F(gamma;X)=K_gamma(X)T_gamma(X),
deg K_gamma=4e+2,       deg T_gamma<=4.
```

The normalized quartics are not unrelated: one global weld gives

```text
FQ=(AB)^2q_eP_Z+CzI^2Omega,       deg Omega<=(e-2,4),
Omega(gamma)=ell_gamma T_gamma/(gamma I(gamma)^2).
```

Here `K_gamma` is exactly the known active-row nonincidence locator. The
quartic bound is sharp and nonsplit on the `e=1` exact Hankel fixture.
Boundary control is now exact rather than aspirational. The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_boundary_crt_reconstruction`
forms the pair-label class `delta=xi_i mod D_i` in `F[X]/(A)`, divides the
first-jet sum by `z-delta`, and reconstructs `Omega` by one explicit
subgroup-derivative remainder modulo `A`. A valid packet forces this generic
degree-`<2e` remainder to collapse to `X`-degree at most four. Random
pair-Lagrange data at `e=3,F_97` attain degree five, so this is a genuine
rejection gate. The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_boundary_dual_moment_gate`
rewrites that collapse as exactly `2e-5` vector-valued dual-RS moments. In
those moments the active locator `C` and interpolation derivative `A'`
cancel, leaving streaming base-field pair traces of the first-jet data. The
PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_boundary_torus_kernel_reduction`
then makes all traces linear in the nonzero labels
`theta_i=xi_iP_Z(xi_i)/lambda_i^2`. A valid packet requires a torus vector in
the kernel of an explicit `(2e-5)(e-1) x e` matrix. Since `q>e`, full rank or
one coloop column is an exact exclusion certificate. Deterministic subgroup
controls are full rank at `e=4,5,7`, while `e=3` is dimensionally incapable
of full rank and has no coloop. The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_internal_slice_lambda_cube_kernel`
is earlier and sharper still. Evaluating at `xi_l` removes every external
label except a nonzero scalar; the forbidden high coefficients form an
`e(2e-7) x e` matrix `U` independent of all `lambda_i` and `P_Z`, with
kernel vector `(lambda_i^3)`. The `e=4,5,7` controls have full ranks `4,5,7`
and maximal internal-slice remainder degrees, whereas `e=3` has no rows.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pair_crossing_rank_gate`
eliminates even the internal slopes. For each omitted pair it gives an
`(e-1) x 5` matrix depending only on the support and matching; a valid packet
needs a quartic, nonzero on every other pair, in its kernel. Rank five first
becomes possible at `e=6`, and every `e=6,7` deterministic control has rank
five for every omitted pair. On the fixed `e=6,F_113` support, a complete
`10,395`-matching census finds no all-deficient matching; 584 matchings have
at least one deficient omitted-pair matrix, but every one has rank five at
another omitted pair. The next theorem target is now support-level:
prove that every official generic matching has rank five for some omitted
pair, or classify the rank-at-most-four matchings and pass only those to
`U`. Only later survivors should reach `T theta=0`, the perfect power,
source constraints, or a line decomposition. This is not authorization to
call the five-coordinate curve a projective pencil.
The gate also carries an exact route fence: arbitrary nonzero weights are
insufficient, since the antiweight pattern `H(b_k)=-H(a_k)` makes
`P_l=D_l^2` survive for every omitted pair. A proof must use the actual
smooth weight `H=X(X-s)(X-x_0)B^4(A')^4`, not only matching distinctness.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_low_degree_fiber_reduction`
now classifies the simultaneous-deficiency branch. Comparing two kernel
quartics cancels `H` and gives degree-at-most-eight rational functions with
the same values on nearly every matched pair. Function-field generator
compression, an exact `98`-point Bezout charge for normalization defects,
and tame ramification reduce every official survivor to exactly one of:

```text
(i)  H(a_k)+H(b_k)=0 for every k; or
(ii) at least e-4-9d^2 matched fibers of one separable map psi,
     d in {2,3,4}.
```

Thus at least `e-148` pairs share one low-degree map in the second branch.
Degrees five through eight are impossible: all pairwise comparison maps
would be Mobius functions of `psi`; Riemann--Hurwitz then makes all but
`2d-2` own quartics divisible by their pair locator, and two such quartics
produce a forbidden nonconstant degree-at-most-four member of `F(psi)`.
The next theorem target is no longer a universal five-column determinant.
It is the four-way exclusion/payment problem consisting of the actual
antiweight identity and the degree-two, degree-three, and degree-four fiber
geometries. Degree two should reuse the Mobius/dihedral machinery with the
explicit bounded tail; degrees three and four should use their low-bidegree
subgroup coincidence divisors and classify subgroup-heavy components.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_two_three_subgroup_reduction`
now completes the first half of that program. Every degree-three map admits
a cubic-over-quadratic target normalization with nonzero cubic constant
term, so the audited `(2,2)` coincidence-curve proof applies after charging
the `85` tails; its irreducible and order-three deck alternatives are both
impossible. In degree two the unique deck involution has at least
`2(e-40)` subgroup graph points, forcing one fixed special graph. Hence at
least `e-40` pairs are all antipodal or all constant-product, with at most
`40` arbitrary tails. The exact support frontier is now only:

```text
global smooth antiweight;
bounded-tail antipodal/constant-product;
degree-four common fibers (at least e-148 pairs).
```

At this stage the coarse route decision was whether the existing dihedral
product ledgers absorbed forty tails; the later tail-rigidity theorem below
sharpens that loss before the trace repair. In parallel the degree-four
coincidence divisor needs its irreducible/component classification. No
degree-three compute is useful.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_antiweight_absorption`
also removes global antiweight as an independent exact-design branch. The
support-only fixture remains valid, but the actual internal-slice values
permit at most two quartics proportional to `D_l^2`; three would force a
squared Mobius ratio to take one value at three distinct internal slopes.
The other quartics generate a proper common field of degree two, three, or
four. Degree three is already empty, degree two is dihedral (with at most
six tails on this subbranch), and degree four captures all but one pair.
After merging with the non-antiweight cases, the complete all-deficient
frontier is now only:

```text
bounded-tail antipodal/constant-product (coarsely at most 40 tails);
degree-four common fibers (at most 148 tails).
```

This was the merged interface before the downstream divisor-invariance
sharpening. The current interface is the six/eight-tail bound printed below;
there is no longer a separate antiweight fleet to run.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_four_irreducible_router`
now pays every ordinary absolutely irreducible degree-four map. After a
target normalization `psi=S/R` with `deg S=4`, `S(0)!=0`, and `deg R<=3`,
the exact boundary rows leave only monomial denominators. The middle
monomial has a determinant-one torus transform of bidegree `(3,2)` and
constant `960`; the ordinary `(3,3)` constant is `2592`. Both lie below
`2(e-148)`. The two end monomials are subgroup-inversion equivalent and
leave precisely

```text
psi=X^3+aX^2+bX+c+d/X,
XY[X^2+XY+Y^2+a(X+Y)+b]=d.
```

The audited generic transform for this Laurent-end curve has constant
`5376`, genuinely above the official margin, so it remains rather than
being rounded away. The degree-four frontier is now exactly this
three-parameter absolutely irreducible curve or a geometrically reducible
coincidence divisor. These are the two current support targets alongside
the bounded-tail dihedral branch.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_four_reducible_deck_router`
now classifies the reducible half. A graph factor gives a deck Mobius map;
the residual has bidegree at most `(2,2)`. An exact enumeration of all `458`
two-dimensional Newton supports exhibits an admissible transform of
constant at most `1440`; two residual components plus a nonspecial graph
cost at most `2912N^(2/3)+8`, still below `2(e-148)`. Any toral residual
component collapses by degree multiplicativity to a scaling or inversion
graph. Thus every reducible survivor is exactly

```text
F(X^2),       F(X^4),       or       F(X+c/X).
```

The complete support frontier is now bounded-tail dihedral matching,
cyclic/dihedral quartic pullback, or the absolutely irreducible Laurent-end
curve. The first two share invariant-field structure and should be attacked
together using the exact product/source identities; the Laurent-end curve
is the only non-pullback quartic geometry.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_laurent_gcd_exclusion`
now removes that final non-pullback geometry. The stronger published
Corvaja--Zannier positive-characteristic gcd theorem applies directly on
the smooth normalization with `u=x^N`, `v=y^N`. Here `deg x=deg y=3`, the
genus is at most four, the zero/pole support has size at most twelve, and
`chi<=18`. Its first constant is `3*324^(1/3)` and its characteristic term
is `108N^2/p`; both are far below `2(e-148)`. This supersedes the unpaid
`5376` Stepanov transform for this branch without changing that earlier
route fence.

The complete all-deficient support frontier is therefore pullback-only. The
initial normalization bounds are:

```text
one antipodal/constant-product matching with at most 40 tails; or
one quartic comparison map F(X^2), F(X^4), or F(X+c/X).
```

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_bounded_tail_dihedral_row_codegree`
starts that weld on the degree-two branch. If `t` exceptional pairs miss the
common involution, eliminating the good pair-Lagrange terms shows that every
nonidentical outside involution orbit has normalized-row codegree at most
`t`; at most one orbit has identical normalized rows. The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_two_tail_rigidity`
then uses divisor invariance and the exact internal-slice values to sharpen
the true degree-two loss. At most two tails have `P_l` proportional to
`D_l^2`; every other no-fixed-point tail charges one of at most four roots
of a fixed comparison quartic. Fixed points cost zero antipodally and at
most two for constant product. Thus `t<=6` antipodally and `t<=8`
reciprocally, and the row-codegree theorem gives the same bounds. The old
zero-tail complement becomes

```text
K_u=P_Z gcd(q_x,q_tau(x))/(q_x q_tau(x)),
deg K_u=e+d_u,        0<=d_u<=8.
```

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_bounded_error_pade_circuit_reduction`
now controls these complements without pretending that their gcd factors are
constant. It writes

```text
K_u=I A_u+chi(u)g_u[u^2M_0-2uM_1+M_2],
deg A_u,deg g_u<=t,
```

and associates every `2(t+1)` selected roots with an explicit Pade
determinant of degree at most `2(t+1)` in `u`. Nonzero determinants are paid
by their degree. Exact official incidence counting forces more than
`9999/10000` of the relevant antipodal 14-circuits, or more than `991/1000`
of the reciprocal 18-circuits, to vanish identically. The remaining
degree-two theorem is therefore a zero-circuit classification or upper
bound, not a generic complement census. Independently, the quartic
pullbacks still need to be welded to the exact product/source identities,
including the possible order-four deck action. There is no remaining generic
or Laurent coefficient family to enumerate.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pade_relation_class_reduction`
performs that classification over `F(U)`. Zero circuits are exactly the
subsets of one unique rational relation class

```text
q_gamma(U)=-A(gamma)/B(gamma),
deg_Z A,deg_Z B<=t.
```

Distinct classes meet in at most `2t` points, each class is the root set of
a fixed factor of `IA+Q_UB` and has size at most `e+t`, and their
`(2t+1)`-shadows are disjoint. The exact shadow ledger forces one class of
at least `172410` external slopes in the antipodal branch or `2128` in the
constant-product branch. At this intermediate stage the degree-two closure
targets were
the uniform class bounds `172409` and `2127`, respectively, or any sharper
aggregate relation-class payment. This is a symbolic fixed-factor problem;
individual official circuit enumeration has no proof value. The later
discriminant exclusion below pays this target without such enumeration.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pade_large_class_static_denominator`
removes the orbit coordinate from every class large enough to matter. A
circuit kernel has `U`-degree at most `2(t+1)`; if its denominator depended
on `U`, its `U`-resultant would allow at most `4t(t+1)+t`, namely `174` or
`296`, class points. The forced classes are much larger. Therefore every
survivor has

```text
B=B(Z),
A=A_2(Z)U^2+A_1(Z)U+A_0(Z),
deg A_j,deg B<=t,
```

and the class polynomial divides all three residuals

```text
IA_2+M_0B,       IA_1-2M_1B,       IA_0+M_2B.
```

The resulting intermediate degree-two leaf was the simultaneous univariate Pade gcd with
the split external locator `P_Z`, bounded by `172409` for `t=6` or `2127`
for `t=8`. This weaker exact predicate exposes the external product identity
used by the downstream aligned-residual and discriminant theorems.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pullback_involution_absorption`
also removes the quartic pullbacks as an independent leaf. Each of
`F(X^2)`, `F(X^4)`, and `F(X+c/X)` has a subgroup-preserving deck
involution. A pole-orbit bootstrap shows that at most `9/11` of the captured
pairs can initially miss it, so one exact deck pair exists; comparing every
pair against that orbit recovers the global `6/8` tail bounds. The
antiweight-derived branch has stronger `2/4` bounds. Thus every
all-deficient support survivor now terminates at the one simultaneous static
Pade gcd obstruction. The separate quartic-pullback compiler is retired.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pade_aligned_residual_degree_four`
then uses external-block incidence to collapse that gcd obstruction. A large
class aligns with at least `e-33` antipodal or `e-44` constant-product
complements. Factoring it from the common quadratic-in-`U` polynomial leaves

```text
R(U,Z)=R_2(Z)U^2+R_1(Z)U+R_0(Z),
1<=deg_Z R<=4.
```

For every aligned `u`, `R(u,Z)` is a split squarefree divisor of the fixed
polynomial `P_Z/P_H`; every root outside `H` occurs at no more than two
aligned coordinates. The first incidence pass forces residual degree at
most six, and the second sharpens it to four.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pade_residual_discriminant_exclusion`
closes that last leaf. Ratios of the calibrated internal evaluations cancel
the row-dependent scalar and force

```text
R(U,xi_i)=c_i(U-u_i)^2
```

at every good involution pair. The parameter discriminant has `Z`-degree at
most eight and more than eight roots, so it vanishes identically. Hence
`4R_2R=(2R_2U+R_1)^2`. Every aligned `R(u,Z)` is nonconstant and squarefree;
valuation parity forces all of its roots into `R_2`, making every aligned
complement projectively identical. This contradicts the three-good-index
calibration. Thus the entire all-deficient quartic-support sub-DAG is now
closed, including bounded tails, antiweight, Laurent, and quartic pullbacks.
High-degree gcd, circuit, pullback, and low-degree pencil fleets are retired.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_external_split_design_exclusion`
composes this with the pair-crossing necessity theorem. Every exact external
design would have a nonzero quartic in every omitted-pair kernel and would
therefore enter the now-empty all-deficient branch. Consequently the complete
official `A=1,s=1,e=2m-1` distance-three chart is closed. The live rate-half
frontier moves to the high quotient-distance tail, the other `A=1` component
faces, and the strict/half-distance `A=3` profiles.

The first new high-distance invariant is now PROVED as
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_first_jet_transversality`.
The corrected-square matrix factorization gives, at every clean selected
root, with domain order `M=2^41` and `N_sq=M+r-3`,

```text
F_t U W_vee=-P_cl' E y^N_sq,
dot y=-(P_cl'E/M)y^(r-2)(1-sy)(1-x_0y)/W_vee.
```

Thus every endpoint incidence is parameter-transverse and carries a fixed
first-jet weight. The flat and one-factor-swapped endpoint resultant matrices
remain compatible at the multiplicity level; the next endpoint theorem must
use these first jets or stronger Hankel coefficients. Replaying or scaling
the four aggregate resultants has no decision value.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_w_interpolation_normal_form`
uses all clean fibers at once. They determine a canonical biform `W_0`, and
the sharp parameter-degree box leaves exactly

```text
W_vee=W_0+P_cl(t A_W+B_W),       deg A_W,deg B_W<=r-1.
```

Thus future endpoint algebra should eliminate the two univariate correction
polynomials against the exceptional, unit, and Hankel identities. Dense
allocation of `W_vee` or independent clean-fiber coefficients is obsolete.

That elimination is now PROVED as
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_unit_triangular_affine_reconstruction`.
Writing `f_0=E q_bar` and `l_0=Delta_inf`, Bezout coprimality makes
`l_0P_cl` invertible modulo `f_0`. The coefficient of `Y^k` in the unit
equation therefore forces

```text
rho_k=-C_k^0(l_0P_cl)^(-1) mod f_0.
```

Because `deg f_0=e>2`, the correction exists exactly when this canonical
remainder is affine in `t`, and then it uniquely supplies `(a_k,b_k)` and the
next quotient coefficient. Induction removes all correction variables. The
live endpoint is now a deterministic residue sequence followed by exact
division, degree-box, and Hankel compatibility checks. This is a reduction,
not an endpoint exclusion: neither printed high-distance profile has yet
been proved to fail those final checks.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_unit_bezout_remainder_gate`
removes an apparent operation from that sequence. The exact identity
`l_0P_cl+f_0a_minus=1` means that if

```text
C_k^0=f_0d_k+r_k,       deg r_k<e,
```

then `rho_k=-r_k` and `s_k=d_k+a_minus r_k`. Thus each coefficient requires
one Euclidean division only, and `deg r_k>=2` is the canonical exact
rejection certificate. Future proof and compute work should use this
remainder stream, not modular inversions.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_second_jet_hermite_gate`
adds an independent reconstruction. Twice differentiating
`F V_vee+R_XW_vee=P_clE Y^N_sq` along each moving selected root determines
`W_vee,t` on every clean fiber. After subtracting `W_0,t` and dividing by
`P_cl'`, the resulting polynomials must satisfy

```text
D_gamma=gamma A_W+B_W.
```

Two slopes recover the correction pair; every other clean slope gives an
affine-line check, and the recovered pair must match the unit-remainder
pair. The endpoint therefore has two independently derived deterministic
certificates before Hankel compatibility. A proof should now target failure
of either comparison uniformly, rather than count the raw number of
constraints.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_jet_quotient_ring_compiler`
turns the two jet reconstructions into quotient-ring arithmetic modulo
`F(gamma,Y)`. Since that locator divides the reciprocal smooth-domain
locator, `Y^N_sq=Y^(r-3)` and `Y^(N_sq-1)=Y^(r-4)` in the quotient. The
canonical modular representatives are the complete fiber polynomials
`W_vee(gamma,Y)` and `W_vee,t(gamma,Y)`. Root enumeration and giant
exponentiation are obsolete. This does not make dense official arithmetic
feasible: `r=2^39-1`, so any donated implementation must expose compressed
locator multiplication, reduction, inversion, and equality certificates.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_unit_resultant_log_trace_gate`
projects those modular jets to one scalar per clean slope. Logarithmically
differentiating the pure-power `(Q,W)` resultant and accounting for
reciprocal reversal gives

```text
Tr((j+w_Yv)w^(-1))
 =(N_sq+1)E'/E+N_sq q_bar'/q_bar-(r-1)q_0'/q_0.
```

The unknown actual degree of `W` cancels. This trace is now the first
high-distance check: a uniform contradiction here would close an endpoint
profile without constructing the global correction pair. If it survives,
the affine-Hermite and unit-remainder comparisons remain next.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_coefficient_biisotropic_plane`
compresses the Hankel side. The `e+1` coefficient vectors of the primitive
minimal kernel are independent and span a maximal common isotropic plane for
`M_0,M_1`; its intersections with the exceptional and infinity radicals are
exactly the first and last coefficient lines. Equivalently, every pair of
coefficient polynomials has zero weighted product moment for both endpoint
syndromes. The live classification should combine this subspace geometry
with the scalar trace and affine-Hermite gates. Materializing the
quadratically many pairings is neither mathematically necessary nor
computationally responsible.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_coefficient_rank_one_flag`
identifies the common orthogonal flag
`H_q=W_q+span{Xq_0}`. Both orthogonal complements of `W_q` equal this flag;
`M_0` vanishes on it and `M_1` restricts to one nonzero scalar on the
quotient line. This exposes the regular Kronecker block without changing
basis. The remaining Hankel problem is therefore a classification of one
maximal coefficient plane with a pinned shifted line, not a search over a
general pencil or adjugate.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_exceptional_self_dual_evaluation_code`
turns the coefficient flag into a length-`2e`, dimension-`e` weighted
self-dual code on the exceptional roots. Its column matroid is
complement-self-dual, and complementary Plucker coordinates satisfy a
printed weighted square law. This is a finite combinatorial interface for
the remaining endpoint classification: use the known Forney values and
resultant incidence to constrain this self-dual code, rather than returning
to the full Hankel pencil.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_exceptional_split_incidence_self_dual_frame`
identifies every code column with the coefficient vector of the split
incidence polynomial `Q(z;a)/z`. Hence the two endpoints are two explicit
weighted self-dual frame classes with flat or one-swap replication. The
exact `e=3,F_101` flat witness in the verifier is a route fence: no argument
using only splitness, replication, rank, and diagonal self-duality can be a
uniform exclusion. The live theorem must add the official Forney weight
formula, multiplicative-domain placement, or a scale-dependent obstruction.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_residue_self_dual_algebra`
adds the first of those missing interfaces. After constant-term
normalization, the incidence rows form a self-dual half-space `U_q` in the
squarefree algebra `F[X]/(A)` for the explicit residue unit
`C=q_1 Phi/B_T`. Its product span lies in the `C`-residue hyperplane. If that
span has dimension `2e-1`, it determines `C` up to scalar and can be compared
directly with the Forney class; if its dimension is at most `2e-2`, the
packet enters a higher-degeneracy branch. The `e=3` positive control is in
the codimension-one branch. This is now the preferred Hankel-side split.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_mds_schur_router`
makes the split certificate-level. MDS forces product dimension `2e-1` by an
elementary systematic-generator argument, hence a unique frame normal that
must equal `q_1 Phi/B_T` up to scalar. Non-MDS supplies a vanishing maximal
minor together with its vanishing complementary minor. Future work should
not test MDS by enumerating minors: either prove it structurally from the
official incidence placement, or derive one dependent set directly and use
the paired dependence.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_mds_half_dimension_non_grs_route_fence`
shows that the MDS side cannot be replaced by a generic GRS classification.
The exact `F_11` code `[I_4|B]` in that node is Euclidean self-dual and MDS,
has the minimal square dimension seven, but is not GRS: its three vanishing
quadrics have no linear syzygy, unlike a twisted cubic ideal. The official
code lies at the same exceptional ratio `n=2k`. Hence any rational-normal
conclusion must use the split-polynomial incidence, explicit Forney normal,
or smooth-domain placement. This route fence is independent of scale and
retires abstract Schur-square classification as a closure strategy.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_non_mds_annihilating_pair_router`
gives the preferred interface on the non-MDS side. A complementary singular
minor pair is equivalent to producing independent nonzero `u,v in U_q`
whose zero sets contain complementary exceptional `e`-sets; therefore
`uv=0` in the reduced algebra `F[X]/(A)`. This turns the branch into an
annihilator exclusion problem. Attack the possible zero sets and the
split-polynomial coefficient span directly; do not enumerate maximal minors.
A positive certificate is just the two coefficient combinations, their
complementary zero-set hashes, and a checked zero remainder modulo `A`. The
canonical gcds split the branch further: an excess-zero word has gcd degree
at least `e+1`, while the boundary case prints coprime degree-`e` factors
`D_u,D_v` with `D_uD_v=A`. This factor dichotomy is the preferred exact
interface for endpoint-specific exclusion. Compute the gcds from the
unnormalized numerators `sum lambda_i q_(i+1)`: the unit `q_1` does not
change exceptional zeros, so quotient inversion is unnecessary.
For a half-rank deficiency `d`, self-duality forces the same deficiency on
the complementary half and produces two `d`-dimensional shortening spaces;
all `d^2` cross products vanish. Retain the deficiency, not only one pair.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_non_mds_support_residue_gate`
couples this exceptional factorization back to the minimal quotient support.
For `K=H_lambda H_nu/A`, every annihilator pair must satisfy

```text
[X^(h-1)] rem_(B_T)(Phi K A^(-1))=0.
```

This follows from `M_1` isotropy after the exceptional contribution vanishes.
It is the first exact scalar gate shared by the excess-zero and exact-half
subbranches. The next non-MDS attack should combine this residue with the
degree bounds on `H_lambda,H_nu` and the endpoint support profile, seeking a
uniform nonzero top coefficient or a further family of coefficient gates.
The equivalent exceptional-side identity is zero for `deg K<=2e+1` and
equals `Theta_2lc(K)` at the sole top boundary `deg K=2e+2`. This gives a
second compressed checker route and isolates the only leading-degree escape.
Both identities hold for all `d^2` cross pairs, so higher deficiency adds a
matrix of constraints rather than merely more witnesses.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_norm_discriminant_square_gate`
now supplies a global obstruction common to both branches:

```text
Res(A,q_1) Res(A,Phi)/(Res(A,B_T) Disc(A))
```

must be a field square. The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_norm_square_cancellation_fence`
identifies its exact limitation. Substituting the Forney interpolation
formula reduces the expression to

```text
(-1)^e Norm_A(Beta) Res(A,q_1)^2,
```

and weighted self-duality already makes `(-1)^e Norm_A(Beta)` square. Thus a
direct official-scale evaluation from a complete packet is only a consistency
check. It cannot be the next exclusion theorem. A useful scalar attack would
need an independent profile-level formula that forces a nonsquare without
first assuming the self-dual packet.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_endpoint_derivative_resultant_reciprocity`
extracts the first compressed identity directly from the endpoint profile:

```text
Res(A,q_1)/Res(A,q_e)=P_ord(0)^k_0                 (flat),
Res(A,q_1)/Res(A,q_e)=(z_min/z_max)P_ord(0)^k_0    (swapped).
```

The official exponent `k_0=2^37-1` is odd. Hence the derivative-resultant
ratio has square class `P_ord(0)` in the flat branch and
`z_min z_max P_ord(0)` in the swapped branch. No large resultant calculation
is needed for this factor. Because it occurs squared in the cancelled norm
gate, its useful content is the exact norm of the top normalized frame
coefficient `p_(e-1)=q_e/q_1`, not a route to a new square obstruction. The
preferred endpoint work returns to the MDS unique-normal comparison and the
paired dependence on the non-MDS branch, with independent smooth-domain
identities retained as a possible third route.

The optional small-analogue audit handoff `CR-003-CLIFT` remains recorded in
`PRIZE_COMPUTE_REQUESTS.md`; it is no longer an official proof dependency,
while `CR-003-BT8` is retained only as retired provenance. `CR-003-CLIFT` is
scoped to the first
nonvacuous official-shaped analogue `(m,e,N,p)=(4,7,64,193)` and must emit
the full kernel lifts and the exceptional CRT degree-collapse certificate
after subtracting the calibrated conic residue, not only rank summaries.
The CRT gate comes before external cofactor construction and should reject a
shard immediately on any nonzero coefficient above degree four. Its
equivalent pair-trace moments should be emitted as streaming zero
certificates, avoiding materialization of `C`. The torus-kernel matrix is an
earlier gate still, but the internal-slice lambda-cube matrix now comes
after the support-only pair-crossing matrix: rank five there rejects the
matching before internal slopes are selected. `U` then rejects the retained
support/pair/internal-slope packet before selecting any `lambda_i`. Full rank
or one coloop at the later stages is exact. The cost is unknown and no local
launch is authorized. The useful contribution is presently a
coverage-complete compiler, checker, and measured pilot; a larger run becomes
responsible only after those exist.

**Track B — transfer offensive:** U1 step one (the (f,g) table), then the
master statement; the DSP8 max-P <= 24 flagship pose (falsifier P >= 21
satisfiable at pose time; cascade = the 3-amber single-req chain + u1_x4
feed; the CR-001 fallback re-wire drafted BEFORE the round runs); the HGE4
odd-width parity+norm pose (with #99/#100 pinned in-statement); the summit
weight-<=4 ambient-exclusion census (shrinks the honest 2^(o(n)) form;
does not claim the wall; all other F2 items route through the F2_FLIP_GOAL
ladder or are labeled new); one real chamber pilot of the 13 (validates the
WCL-template port; low strategic yield priced in); the c2pp bulk-identity
lemma (the FD instance, honest 1.0662 worst case).

**Track-B gate event, c2 chamber pilot.** The reciprocal quadratic-field,
maximal-degree, selected-antipodal collision shard is now closed. Frobenius
reduces its three affine subgroup tests to the fixed element
`r=(2a-1)/3`, `a^2=-2`; a hash-pinned 16-shard screen covered all
`4,495,442` official progression moduli and found no hit. This validates the
engineered-field port on one genuine chamber shard but does not close any of
the thirteen chambers. Fixed-field, degree-deficient, non-selected-
antipodal, and high-support packets remain, so the roadmap still prices the
full chamber route as low-yield after this exact exclusion.

**Track-B DSP8 structural purchase.**
`f3_h3_dsp8_nodal_smooth_high_tail_domination` proves that the nodal trace
locus is not an independent high-tail payment. Targetwise, nodal
signed-disjoint distance-six edges are dominated by smooth edges for
antipodal-free `P>=33` and antipodal `P>=35`, preserving the exact quotient
weight `R(t)`. The remaining analytic task is a smooth quotient-weighted
moment plus the bounded bands `25<=P<=32` and `25<=P<=34`, respectively.
This is a structural reduction, not a DSP8 close; no broad point sweep is a
proof of either remaining term.

The paired-PGL2 route has also been repriced at the actual consumer. Writing
`P=I_inv` and `R=I_aff-1`, the formerly posed global score cap `39` closes
the stronger M35 route. The exact pointwise C36' target is

```text
I_inv>=19  =>  I_aff<=18.
```

A convenient stronger scalar certificate is

```text
P>=19  =>  I_inv+2I_aff<=56.
```

This forces `R<=17`, whence `17X_18<289n^2`. Threshold `57` admits the
boundary profile `(P,R)=(19,18)`, so `56` is sharp among constant-score caps
implying the rectangle, but over-solves profiles with `P>19`. The theorem
search should target the gcd-degree rectangle implication before the CR-001
fleet; it has no fixed-order elimination dependency. Both the implication and
the scalar cap remain open.

The fixed-order fallback is now an explicit external-compute ladder rather
than a local campaign. The quotient-orbit decomposition proves that at
`n=8192` the maximum-degree class contains `12,285` of `24,534` blocks and
`75.009%` of total algebraic degree; the top two classes carry `93.757%`.
Consequently a low-degree pilot cannot price CR-001. The responsible order is
`n=8` conformance, a complete larger toy comparison, one maximum-degree
block, then a separately approved fixed-order campaign, and only then an
all-29-order request. Every stage needs a streaming certificate checker and
an external CPU/RAM/time/storage/dollar ceiling. No CR-001 production run is
authorized against the remaining local Modal credit. The exact packages are
`CR-001-ALG-PILOT`, `CR-001-N8192`, `CR-001-ALL`, and `CR-001-P24` in the
compute ledger; future H3/shift-pair PRs should copy them as contributor
requests.

The vacuous `P<=24` satellite also has a quotient-free exact candidate
compiler. The monic unordered shifted-product polynomial satisfies
`Ucal_n^2=Pcal_n Delta_n`; its first thirteen Hasse derivatives, with the
identity target algebraically removed, retain exactly the odd
characteristics with a nonidentity unordered multiplicity at least thirteen.
Every `P>=25` row is retained, and the only boundary overcandidate is
`U=13,D=2,P=24`. At `n=8192` this halves the dense product degree to
`33,550,336`, but no efficient official-scale scalar elimination or costed
pilot is known. `CR-001-P24` records the missing implementation as an
outbound contributor request; no raw orbit fleet or local Modal run is
authorized.

At a fixed row the satellite has an exact PASS checker. If `G_12` is the
gcd of `Ucal_n` and its first twelve Hasse derivatives, remove its complete
identity factor and put `H_D=gcd(Delta_n,Delta_n^[1])`. Then

```text
max_(t!=1) P(t)<=24  iff  G_12^neq divides H_D.
```

The local valuations are `(U-12)_+` and `(D-1)_+`, so this rejects both
`U>=14` and the boundary `U=13,D<=1`. The completeness router and checker
are proved; the remaining blocker is sparse official-scale construction or
elimination with a measured resource envelope.

An exact alternate compiler starts before the dense product polynomial. For

```text
F_n(X)=((1-X)^n-1)/X,
G_n(T,X)=X^(n-1)F_n(T/X),
```

specialization at `T=t` has gcd degree `P(t)`. The coefficient ideal of
subresultants `0,...,24`, saturated away from `T=1`, therefore has exactly
the nonidentity `P>=25` characteristic support, with no unordered boundary
false positive. It gives contributors two complete implementations to
compare, but the zeroth subresultant is still the degree-`(n-1)^2` global
product resultant and no cost claim follows.

The same obstruction has a bounded-degree divisor presentation. A monic
degree-25 polynomial, inverse selectors, and two length-`s` modular squaring
towers give exactly

```text
98s+30 variables and 98s+54 quadratic equations,
```

at most `4,048` variables and `4,072` equations on the official band. This
is polynomial in `log n`, but the constant is large and no solver cost is
known. The compute ledger requires a small pilot before any contributor run;
no Modal job is authorized.

An exact ordered-root alternative uses `50s+328` variables and `50s+352`
quadratic equations, at most `2,378` variables and `2,402` equations on the
official band. Its lower dimension comes with a `25!` permutation symmetry,
so a contributor pilot must benchmark it against the symmetric divisor-tower
formulation rather than select it by variable count alone. This is a solver
contract, not a solver or cost claim; no Modal job is authorized.

**Track-N gate event, W3 scope correction and consumer repair.** The
descriptor, two-class ledger, and QA.22 currency separation exposed the exact
claim and its safe-side scope. The fiber-layout packet gives `7>6` at the
unsafe spending cell, killing the stronger all-cell interpretation but not
literal W3. The former large campaign is canceled because W3 is no longer
consumed. The repaired adjacency dependency uses the proved qcore/list-unsafe
lower side and the independent list-safe upper side. This removes W3 from the
critical orbit without claiming that its safe-side target is decided.

**Track C — convergence:** VENDOR-BEFORE-CENSUS as standing law (any
upstream wave within one edit-distance of an open red triggers translation
into our coordinates, never a race) — first application: the M31 wall
library into chart/atlas coordinates, then the GRS4 census with the AZC
re-run; the ROLLING grammar crosswalk (our packaging emissions vs his
compiler JSON + Paper D (F1)-(F4); adapters as waves land, never a
big-bang at the end); PR pipeline discipline (one audit-genre PR in flight;
candidates must show a consumer); the l1 standing lane (first-match scope pin
landed -> joint background-anchor cell charge landed -> general first-source
domination landed -> fixed-polarity anchored closure landed -> tame refinement-
map census landed -> periodic-owner shortcut fenced -> general-pullback descent
landed -> full-domain pullbacks proved intrinsic -> partial-pullback Johnson
router landed -> coverage kernel absorbed by partial loss -> U2 internal-
rechart payment transport -> verify
small-scale tame-role, wild/unanchored-refinement, growing-polarity, and
arbitrary-locator owner-cell budgets -> LS6 guarded atom fallback; large
classification work remains parked behind the theorem gate); one timeboxed
P-B transport attempt (every shift fiber with `t>=K`, including the complete
official terminal interval, is now multiplicity-one; the remaining transport
target is the repeated-difference range below `K` with RS realization and
first-match ownership; full-side puncturing gives smaller generic instances,
and unique subset ownership now pays the cross-difference energy prefixes
`c=K-t<=2,1,1,6,5,4` on the six clean-rate rows; the deeper aggregate is
open; the contributor-scale compiler is recorded as
XR-PB-ENERGY and is not yet authorized; this is Boolean energy, not CAP25's
local locator-SPI input); U2 formalization on his
firstocc partition base plus an explicit quotient-compatibility/payment layer
(feeds his checklist item 2; Lean effort capped ~10%, aligned to HIS
four-item Lean priority order).

**Track-C upstream event, Grande Finale v4 / Paving v9.2.** Upstream main is
now `fb6d9555` (`cc1d8784` integrates the reviewed M31 wave and `fb6d9555`
adds the explicit post-Johnson list-decoding priority). Grande Finale v4's
moving-root theorem pays a chart only after
its selected locators are proved to lie in one genuine projective pencil. It
does not pay P-A1, P-A2, or P-B: the XR canonical charts remain arbitrary
MDS kernel-ray charts, with neither one-pencil coverage nor a paid pencil
count. The theorem is retained as a local tool, not imported as an XR
payment. The v4 workboard also makes direct exact-row impact the upstream
contribution gate; future handoffs should name K/M/T workboard items rather
than the superseded v3 six-input checklist alone.

**Track-C upstream event, open M31 source/Pade wave (#1023--#1041).** The
stacked packets now give an exact full-layer Pade--Forney source, its
locator/numerator coupling, a v4 LIST source adapter, masked Popov--Pade
kernel identities, factor-one common-core add-back, and rank-two-coloop
deletion. They do not pay the deployed row. The later route cuts are
load-bearing for allocation: #1037 refutes the raw `T46<=259880` shortcut and
the packing-at-most-four/four-point-transversal inference; #1039 realizes a
`6,796,405`-member fixed-remainder C1 boundary source and proves that no flat
raw baseline is simultaneously source-compatible and strong enough for the
current two-row Forney payment. #1026 independently shows that exact image
normalization does not make absolute MI+MA equivalent to Sidon payment.
#1040 then exhausts all `261,192` `c=2048` occupancy profiles and proves that
the `260,576` bi-deep profiles contribute at most `7,556,704` codewords unless
one profile contains a same-profile 30-column coupled Pade--Forney carrier.
This is a route cut with zero ledger movement: the carrier has no paid owner,
and its conditional `9,216,781` face-plus-carrier allowance still needs a
boundary-to-prefix adapter and a fixed codeword-disjoint compiler. #1040's
proposed per-profile residual cap 29 is not a live route after #1041.
Therefore do not fund raw `T46`, flat-baseline, bounded-packet, all-profile,
or absolute dual-mass campaigns.
The live upstream M1 terminals are the chronology-valid row-sharp-Q/cross-
weight owner payment and the successor
`M31_C2048_FIXED_SYNDROME_MULTIPREFIX_FACE_CARRIER_OWNER`, with received-word-
uniform C1 accounting still open. #1041 proves that the carrier is populated,
not removable: one `(1,1)` source has `1,693,898` members, and a deployed
same-remainder pair has distinct actual locator prefixes in both orientations.
The portable field-generic source and route cut are independently proved in
`l1_fixed_syndrome_multiprefix_route_cut`. Consequently neither a universal
profile cap 29 nor a maximum-prefix-fiber computation is a valid next step;
the residual is the attained-target sum in `(L_S,H)` coordinates with a
chronology-valid owner. These are open-PR results, so vendor or
consume them only with their exact stack commits and nonclaims until
integration.

**Track-C upstream event, open M31 intercept/tangent wave (#1047--#1049).**
PR `#1048` is independently replayed and imported as
`l1_m31_t64_quotient_prefix_intercept_fence`. Its pinned quotient profile has
six deficiency-64 same-prefix neighbors and `floor(4H_64/p^32)=0`, so the
coefficient-four shell route is false at intercepts three through five.
This is the auxiliary `2^-100` M31 list row, not a `2^-128` Prize row.
Intercept six is only the first arithmetic survivor; the packet has no
received-word, first-owner, or slope projection. Therefore the local L1/Q
target must either pay the intact `T_64` swaps through a chronology-valid
owner or use a genuinely collective attained-image theorem. PR `#1049` is
independently replayed and imported as
`rate_half_kb_v4_tangent_source_atom`. Exact sparsification and finite-image
counting bank its canonical KoalaBear tangent cell at `U_paid=981,104`; the
frozen partition digest is
`4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc`,
and the remaining reserve is `274,980,728,110,413,983`. The exact partition
still leaves `U_Q`, `U_BC`, and `U_new` unpaid, so this is an evidence atom,
not a KoalaBear row close. The legacy M1 owner total is not imported. PR
`#1047` is independently replayed and imported as
`l1_m31_semantic_owner_profile_regression`. Its deployed M31 constructors
compile only supplied theorem-certified near-rational and primitive
one-pencil slope lists of sizes at most `1` and `2`. Its exact `F_241`
received-line regression proves that two genuine earlier owners repair the
false ten-neighbor support shell and leave an eight-neighbor `3+7` residual
with margin `18295`. It does not prove deployed owner exhaustivity, an
all-residual theorem, a row payment, or any KoalaBear MCA cell. None of these
open PR imports closes a local red.

**Track-C upstream event, M31 depth-32 counterexample (#1102).** The explicit
packet is independently reconstructed in
`l1_m31_depth32_uniform_intercept_counterexample`: `1225` whole-`T_64`
triple exchanges and twelve mixed `T_16` exchanges give one anchor with
`d_192>=1237`, refuting the proposed uniform in-band cap `1233`. This does
not kill the coefficient-four route: substituting intercept `1237` leaves
reserve `1767799`. It does rule out treating the former cap as a proved
flatness input. No replacement upper bound, received-word realization,
first-match survival, row payment, or `2^-128` Prize statement is imported.

**Track-C upstream event, Lane-L draft PR #1051.** The proved local
`rate_half_cyclic_rotated_prefix_floor` now has a direct consumer in
Przemek's post-Johnson ordinary-list lane. The exported packet prints the
exact row, closed radius, Johnson comparison, code object, and 243-bit list
lower bound, with two independent stdlib replays and a concrete Pocklington
field anchor. It is a lower/unsafe result only: no MCA conversion, list upper
bound, asymptotic theorem, or safe adjacent row is claimed. Local DAG status
does not move because the unsafe side was already green. The remaining
rate-half prize obligation is still the safe-side localization above
`a=k+2^34-1`, represented by `rate_half_list_adjacent_crossing`.

**Track-C checkpoint refinement (proved, 2026-07-22).** The minimum
characteristic-width coarse branch has been reduced from an unbounded
split-pencil census to nine exact Mersenne-shape rows. The official atlas has
59 `(n,p)` pairs: all `m=1` rows are empty; all `m=2` rows are either empty
or the explicit antipodal family; maximal split-value degree is empty on all
16 `m>=3` rows; and Frobenius periodicity removes seven broad-remainder rows
at every first-checkpoint depth. The surviving rows have
`n=m(p+1)`, `m in {4,8,16}`, and `2<=h<=m-1`. This is a real closure of the
`t=p` endpoint outside those nine rows, not an L1 status flip. The next proof
step now starts from the proved Mersenne cyclotomic normal form: frequency
`q(p+1)+b` survives exactly outside two residue classes modulo
`gcd(2b,m)`, and every collision is an exact-weight `2p` codeword above an
`N+1` BCH floor. The complete `(32,7,4)` analogue has 16 `h=2` pencils and no
`h>=3` pencil. All 16 are embedded order-`2(p+1)` antipodal families, and the
same construction now proves exactly `n/2` explicit pairs at depths `p,p+1`
on every official surviving row. Total emptiness is therefore false as a
strategy; prepay this polynomial family and attack `m=4,h=3` plus
nonembedded `h=2`. Oddness pairs every embedded split value with its
negative, so maximal-degree emptiness proves that the `m=4,h=3` branch is
entirely nonembedded. The corresponding large-run idea remains parked as `CR-L1-MCP`,
gated on a completeness-preserving low-weight-codeword compression and a
measured pilot.
The nonembedded `m=4,h=3` object is no longer an unspecified split-pencil
census: it is exactly the two-Schur section `b,b^[2] in C_M`, with three
nonzero colors of size `p` and a `p+4` zero complement. The next analytic
target is a component or emptiness theorem for that section. Any computation
must retain both code constraints; a one-code BCH search does not test the
posed branch.
The first compressed CP-SAT pilot at the next analogue `(p,n)=(31,128)` is
explicitly `INCOMPLETE`: after two model-validation repairs, the validated
run hit the 60-second Modal function cap before returning any solver status.
It supplies no mathematical evidence. The subsequent analytic closure makes
it obsolete as a route-deciding contributor task, so `CR-L1-MCP-C31` is now
a retirement record and should not be rerun. Its model and independent replay
remain conformance artifacts.
The exact abc ledger now sharpens the analytic route further. In any
hypothetical official `m=4,h=3` record, the depressed cubic has nonzero
linear coefficient and a low-degree Wronskian eliminant containing the full
defect factor. The Cartier refinement excludes `ord_0(R)=4`; the four
remaining valuations `0,1,2,3` have eliminant degrees at most `3,2,1,0` and
four exact missing-derivative coefficient constraints. These proved
reductions are `l1_m4_h3_mason_defect_budget` and
`l1_m4_h3_cartier_resonance_reduction`. The immediate proof target is a
four-case low-defect Davenport-Mason classification. The companion
`l1_m4_h3_euler_quotient_factorization` pins the eliminant's constant term
and converts its degree into the exact degree `p+deg(H)-4` of
`nu U+XU'`. The tangent-radical successor then excludes `nu=3` and all
positive strata except `(nu,deg H)=(1,2),(2,1)`; the latter has an exact
cubic tangent radical. The exact positive-value coset certificate now removes
both positive strata entirely at `p=8191,131071` and reduces the two larger
characteristics to `a^3+8b^2=0`. The Belyi, base-field normalization, and
fixed-point certificates further compile `(2,1)` to scalar-free
multiplicity triples. The stronger
`l1_m4_h3_positive_tangent_multiplicity_exclusion` now removes both parent
strata without a search: at every repeated tangent root,
`ord(X^nu H-kappa)` equals the tangent multiplicity, but this polynomial is
cubic and there are at most three tangent roots. This would force `p<=9`.
Thus positive valuation is empty on every official `m=4,h=3` row, and the
Belyi artifacts remain conformance reductions rather than a live endpoint.
All `nu=0` degrees now share a canonical sparse cubic Frobenius kernel. On
the `b!=0` arm, tangent localization excludes the middle degrees one and two,
leaving a scalar-pinned constant eliminant and a cubic eliminant with two or
three tangent roots before the final local arguments below. The zero-`b`
value-coset certificate deletes all four `b=0` degrees at
`p=8191,131071`; at `p=524287,2147483647` it retains them only under
`a^2+3aR(0)^2+R(0)^4=0`.
The constant nonzero-`b` endpoint is now finite at the outer-projective
level. Its scalar equation has two components; a local Euler-order argument
deletes `2aR(0)+3b=0`, and the exact 16-quarter fiber-product certificate
leaves only `(A,B)=(6,20)` on the first three characteristics and that pair
plus `(844833809,2002167159)` on `p=2147483647`. Here
`A=a/R(0)^2,B=b/R(0)^3`. The quarter step alone is not a lift or endpoint
exclusion. The next Euler-divisor step excludes the universal `(6,20)` packet on every
characteristic: a forced `p`th-power rational function would require the
nonzero roots of `R-R(0)` all to have multiplicity `(3p-1)/4`, incompatible
with their total degree `p-1`. Thus this endpoint is empty on the first three
characteristics. Only the exceptional largest-characteristic packet remains;
the exact auxiliary-fiber theorem then forces its normalized shifted cubic to
divide `W^(4(p+1))-1`, but the remainder is `876663072!=0`. Hence the entire
nonzero-`b` constant endpoint is empty on all four characteristics.
`CR-L1-MCP-NU0-H0` is retained only as a retirement record; no contributor
compute should be requested for it.
The remaining cubic nonzero-`b` endpoint is also theorem-empty.
`l1_m4_h3_nu0_h3_tangent_multiplicity_exclusion` shows that a tangent root
of multiplicity `e>=2` forces the cubic `H-kappa` to vanish to exact order
`e`: the tangent rational map has nonzero derivative, whereas the Euler
correction starts at order `2e-1`. With only two or three tangent roots this
would force `p<=9`. Hence no nonzero-`b`, `nu=0` branch remains, and no
contributor search should target one. Combining this with the positive and
zero-`b` value-coset exclusions closes the complete `m=4,h=3` endpoint for
`p=8191,131071`. On `p=524287,2147483647`, the exact residual is only the
four invariant-pinned `nu=0,b=0` degrees.
That last residue is now closed by
`l1_m4_h3_nu0_zero_b_euler_exclusion`. On every root of the complete fiber
`R=0`, the differentiated domain identity and Euler quotient give
`H=12alpha/a`; evaluation at zero forces `a/R(0)^2=-3/2`, contradicting the
value-coset invariant outside characteristic five. Therefore every official
`m=4,h=3` row is empty. `l1_m4_h3_official_emptiness` packages the exhaustive
case split as a first-class green DAG node. The live first-checkpoint frontier is now
nonembedded `m=4,h=2`, `m=8` with `2<=h<=7`, and `m=16` with
`2<=h<=15`, after subtracting the proved embedded antipodal family.
The endpoint degrees are now sharply reduced but not closed:
`l1_mersenne_next_to_maximal_exceptional_reduction` excludes every
nonconstant-Euler tangent branch and both binomial outer forms at
`m=8,h=7` and `m=16,h=15`. Any survivor has `nu=0`, constant `H=q`,
simple nonzero tangent values satisfying `qG(y)=m alpha y`, and squarefree
tangent fibers disjoint from the complement. Exact degree comparison also
pins `deg T=h-2`, `deg(XR')=p-m`, and the leading scalar; lower-degree
tangent chambers are already empty. Squarefreeness leaves only
`ord_0(T)=0,1`, and the residual quotient of `G-(m alpha/q)Y` is quadratic
with `R(0)` as a root. Its two quotient fibers exactly reconstruct `D` and
`R'` through their radical and ramification factors. After target
normalization the exact residue is a domain-supported polynomial Belyi map
with critical values `0,1`. The next analytic step is to classify this
Belyi normal form; the
unknown-cost proof-producing fallback is recorded as `CR-L1-MCP-NMCE` and
must be delegated rather than launched on the current account.
The first generalization of the `m=4` auxiliary-fiber close is now proved:
`l1_mersenne_next_to_maximal_belyi_shifted_value_gate` makes the normalized
degree-`h` split-value polynomial divide `W^n-1` and excludes every nonzero
passport whose two projective invariants descend to `F_p`. Therefore the
`z=0` chamber is also locally impossible, and the live `h=7/15` residue is
genuinely non-prime-field normalized.
The next analytic question is a Frobenius/descent classification of that
small-degree cyclotomic divisor, additionally constrained by the exact
weighted-derivative equation, not a degree-`p` coefficient census.
That question now has a coefficient-free exact normal form. In the
`ord_0(T)=0` chamber,
`P_s=sum_(r=0)^h binom(s+r-1,r)W^(h-r)` for one `s notin F_p`, and the only
outer condition left is `P_s|W^n-1`. In the `ord_0(T)=1` chamber, a top-down
recurrence generates `G` from `(A,c)`, the final coefficient equation cuts
out the explicit hypergeometric curve
`[t^h](1-t)^(c rho)(1-ct)^(-rho)=0`, where
`rho=2A/[c(c-1)]`, and the zero split value imposes
`(c-1)^n=1`. This is
`l1_mersenne_next_to_maximal_hypergeometric_normal_form`. The proper next
step is an exact univariate cyclotomic gcd and curve-torsion intersection,
not enumeration over fields or degree-`h` coefficient vectors; the
unknown-cost campaign remains delegated as `CR-L1-MCP-NMCE`.
The order-zero branch has a further bounded-degree prefilter:
`l1_mersenne_hnf_frobenius_reciprocal_gate`. With
`Q_s(Z)=Res_W(P_s(W),Z-W^m)`, cyclotomic survival forces
`Q_s(0)Q_(s^p)(Z)=Z^hQ_s(1/Z)`. Replacing `s^p` by `t` gives a coefficient
system whose degrees depend only on `m,h`; a unit saturation by `t-s`
closes the order-zero branch without constructing a degree-`n` remainder.
This off-diagonal saturation is now the first exact contributor target.
Only its retained components should be tested against `t=s^p` and the full
cyclotomic remainder.
The first exact `(31,8,7)` benchmark built the seven equations in under six
seconds but timed out in SymPy's generic three-variable Groebner saturation
at 120 seconds. This is no mathematical evidence. It routes donated compute
to a stronger elimination backend or a structure-aware two-variable
saturation; do not retry the same SymPy path or expand `W^n-1` first.
The order-one branch now has the parallel bounded gate
`l1_mersenne_hnf_order_one_frobenius_gate`. Its torsion condition gives only
`m` chambers through `zeta=(c-1)^(p+1)` and
`c^p=1+zeta/(c-1)`. The Frobenius hypergeometric curve and reciprocal
resultant then form a bounded-degree saturation in each chamber. The known
zero split value supplies an automatic resultant factor; cancelling it
reduces the reciprocal polynomial from degree `h` to `h-1`. This reduced
system is the first order-one contributor stage; actual `p`th-power and
degree-`n` tests are reserved for retained components.
The next analytic target is therefore an exhaustion theorem for low-weight
balanced signed words in the `m=4` Mersenne cyclic code. The exact finite
falsifier `CR-L1-MCP-M4H2-C31` asks contributors to classify the order-128
analogue after blocking every embedded word and symmetry orbit. It is
unknown-cost and must not run on the current account; a witness would change
the theorem strategy, while a certified exclusion would calibrate the
embedded-family conjecture without pretending to prove an official row.
The complete scalar-free analogues at `p=7,31,127` have zero divisibility
witnesses and are now the conformance oracle for a future compiler; they do
not exclude an official row.
`CR-L1-MCP-NU2` is now retained only as a retirement record. The new local
theorem removes its parent stratum, so no large multiplicity-triple run has
mathematical decision value.

**Track H — hedges (funded, never built on):** H1 price RK by one dedicated
refutation round (survives -> insurance; dies -> the 17-leaf prune comes off
the books); H2 FD as a schema only after the c2pp instance adjudicates;
H3 = the D3 self-kill.

## 8. Endgame

If U3 adjudicates live: transport the restructure to the summit parity model
and then the joint exchange-compressed brief with upstream; if the payment lemma
lands anywhere it lands on our side of the balance line (4.73-4.83 bits vs
his ~1.66M-bit overhead) in his formulation. If the wall stands: the
partial-credit posture — list grand (if closed) + the rate-1/2 MCA
determination to ~(2^39+2)*2^128 + the strongest per-row replay/audit record
in either tree; positioned on AUDIT DEPTH, not bit-lead.

Dossier (the full packaging tier): total certified f(C) compiler;
clean-checkout replay CI; provenance chain; nonclaim-ledger emptying; the
folder-census sync to the DAG; the harness census closed; a freeze date set
AT the posture decision (gate D3). Joint merge at his input 6 (co-signed
summed integer certificates; every joint status flip double-keyed: his
triage + our Modal execution re-pin — hash-green != execution-green).
Bilaterality stated precisely: ours is the only independent adversarial
replay lane between the two trees.

## 9. The progress metric

The grand challenges ask to DETERMINE delta*, not to prove our conjectured
value. Paper D bounds delta* from above; our floors bound it from below.
Therefore: a floor demotion RELOCATES delta* rather than ending the program
(the refutation branch, certified at the relocated value, is a first-class
prize deliverable — this fallback is recorded); and honest progress is
**bits of remaining delta*-bracket, jointly over both trees** — the only
metric under which the reduction waves were not zero progress.

## 10. Maintainer decision queue (standing; rule as they become ripe)

Spend: the Modal envelope; the Job A line item; the (2,7)+ contributor gate
(three preconditions); a named owner for the aggregate compute budget.
Outward: PR pacing ratification; joint-brief authorization on input 3 (only
if U3 live); the co-authorship/credit
conversation (anchored to input 6, raised at the first declared milestone);
the submission-posture decision (at gate D3). Policy: the octave-31
compute-law amendment; integration-audit cadence re-affirmation; a
ceremony-batching rule for the first red closures; re-scoping the F2
standing rule to the B4 + ladder items; owners for the orphaned threads
(DLI-CLOSE-6, the paused M5 packet, the artifact-refresh rule extension).

## 11. Planning priors (not evidence; re-issue at every gate)

Full resolution of both grands under this plan: ~10%. `list_grand` alone:
~25%. The clean-rate milestone (now scoped by the resolved Conflict-4 audit): ~50%.
Partial-credit conditional dossier at submission quality: ~85% — the
statistically likely outcome, and the reason dossier work is front-loaded.
Relocated-delta* determination: ~5-10%. If D1/U3 adjudicate a unifying
lemma live, the top lines move and the priors are re-issued.

## 12. Joint harvest execution log

**2026-07-26, H1 complete:** the affine-span, generalized-weight,
fixed-union ray, single-circuit, and fixed-syndrome Johnson compilers from
upstream `b13de811` now have independent local proofs and bounded replays in
`upstream_gfv4_affine_span_list_compiler` and
`upstream_gfv4_fixed_union_johnson`. Their exact scopes are crosswalked.

The rate-half equality case is stronger than the initial planning note:
`rate_half_list_budget_three_affine_rank_rigidity` proves that every
four-codeword witness at `(n,K,m)=(4d,2d,3d-1)`, `d>=3`, has affine codeword
rank three. Rank two would force `2d+2` active agreement coordinates but
only six roots among pairwise affine-linear quotient differences.

This changes no chamber status and no adjacent endpoint. The thirteen
chambers classify block-locator Plucker geometry; the imported theorem
classifies affine flats of actual codewords. The next route-deciding theorem
is therefore a bridge from a chamber's locator identities to a constant
affine dependence among its four codewords. Without that bridge, calling a
locator Grassmann line a codeword pencil is a scope error. Fixed-union
compilers remain one-chart evidence only and must not be summed over support
unions without a disjoint atlas.

**2026-07-26, first joint outbound packet:** the proved
`xr_generic_mds_kernel_ray_bound` was translated into upstream K3 terminology
and opened as draft PR
[`#1106`](https://github.com/przchojecki/rs-mca/pull/1106). On the exact
KoalaBear MCA row it pays every column-far fixed-union chart through nullity
nine; nullity ten exceeds the full row budget. This is a real route cut but
does not count retained unions, pay the sparse branch, or move an endpoint.
The next XR theorem must therefore address first-match chart aggregation (or
prove a structural collapse that avoids it), rather than improving the same
per-chart constant again.

**2026-07-27, PR #1106 supersession audit:** the PR was revised at head
`835ddaca` after its author found that the merged agreement-weighted
transverse-secant theorem strictly dominates our GRK specialization. The
one-line column-far binding supplies that theorem's per-witness hypothesis,
and exact KoalaBear arithmetic pays `nu<=10` (`nu=11` first unpaid). This
strengthens the finite route cut but confirms the same strategic conclusion:
do not optimize another fixed-union constant. The binding red wall is the
aggregation of retained unions, with the sparse branch kept separate.

**2026-07-27, Lane-L PR #1101 audit:** the zero-remainder boundary theorem at
`c=1,s=0` reaches the same unsafe agreement `k+2^34-1` as our optimized
positive-remainder construction but raises the certified lower-list bit scale
from hundreds to at least `1,466,604,010,422`. This cannot move
`rate_half_list_adjacent_crossing`, because both bounds already exceed `B*` at
the same agreement. Its new route cut is valuable: an abstract family with
only the pairwise intersection restriction is too large to yield the needed
safe upper bound, so the Lane-L close must use Reed-Solomon locator, syndrome,
or coefficient consistency. The open PR remains upstream-owned and is not
duplicated locally.

**2026-07-27, F3 `m=128` route decision:** exact energy integrality was already
known to miss the `h=10`, mask-`011` endpoint. A new explicit support fixture
shows that retaining only the exact Taylor multiplicity still misses by over
`15` bits. Exact even/odd recursion on a stronger adversarial support gives a
joint order-`128,64,32` resultant product more than five bits above the
required divisor threshold, killing the uniform joint-product route as well.
The three norms nevertheless have common gcd exactly `512`; an actual moment
solution needs the same official odd prime at valuations at least `(5,2,1)`.
The next theorem is therefore a common-prime alignment exclusion. Independent
scalar-energy, Taylor-only, and product-magnitude bounds are now fenced as
routes that discard the load-bearing information.

**2026-07-26, L1 endpoint color-degree cut:**
`l1_mersenne_hnf_order_zero_linear_color_exclusion` proves that the colored
Frobenius interpolant in the `m=8,h=7` and `m=16,h=15` order-zero HNF rows
cannot be linear. Injectivity would identify the hypergeometric locator with
an affine image of `mu_m` minus one color; the first three coefficients have
resultant

```text
-2(h+1)x(x-1)(hx+1),
```

and every branch forces either an impossible coefficient equation or
`s in {1,-m} subset F_p`; a separate coefficient comparison in the same
theorem excludes a constant interpolant. The next exact order-zero attack
starts at `deg E=2`. This is `NARROWED`, not a status flip: the higher color
degrees, the order-one chamber, actual
cyclotomic divisibility, and the inner lift remain open. No Modal job or new
compute request was used.

**2026-07-26, L1 quadratic color-collision router:** the next order-zero
degree is now structurally split without a generic saturation. If a quadratic
color interpolant repeats two colors, Frobenius forces either a zero collision
center or an affine transport of the truncated-binomial locator. Its weighted
derivative identity permits only identity and reflection; identity violates
`s notin F_p`, while reflection forces
`P_s | [W(1-W)]^m-1`, whose exact top remainder coefficient again puts `s`
in `F_p`. Thus every multiple-repeat quadratic is even. On the four
`m=8,h=7` rows, an exact even/odd pseudo-remainder also forbids two antipodal
pairs, so a quadratic candidate has at most one repeated color. The
`m=16,h=15` even multi-collision branch and the collision-free/single-repeat
systems stay open. Result: `NARROWED`, no critical status or endpoint change,
no Modal use, and no new compute request.

**2026-07-26, L1 collision-free quadratic exclusion:**
`l1_mersenne_hnf_order_zero_quadratic_collisionfree_exclusion` removes the
remaining injective quadratic branch on all five endpoint rows. The reflected
locator product descends through `U=W(W-S)`; Newton identities give root
power sums `p_j=-s`, so its first three coefficients are exactly
`binom(s+r-1,r)(1-S)^r`. A collision-free color map would therefore be the
same punctured-cyclotomic linear template already excluded by the resultant
`-2(h+1)x(x-1)(hx+1)`. The quadratic frontier is now exactly one repeated
color on `m=8`, and exactly one repeat or an even multi-repeat on `m=16`.
Result: `NARROWED`, with no complete degree, row, critical status, endpoint,
Modal job, or compute request claimed.

**2026-07-26, L1 m=8 quadratic close:**
`l1_mersenne_hnf_m8_order_zero_quadratic_exclusion` removes the final
degree-two color system on all four official `m=8,h=7` endpoint rows. The
previous pair of quadratic theorems forces exactly one repeated color. After
normalizing it to one, there are 21 pairs of omitted eighth-root colors.
Their first three centered moments impose one quadratic `q_(i,j)(s)`, while
the product of the seven locator roots and `P_s|W^n-1` force
`binom(s+6,7)^n=1`. Exact gcds in `F_p(mu_8)[s]` are one for all 84
row-pattern pairs; an independent `F_p[u]/(u^2+2)` implementation verifies
84 nonzero Sylvester resultants and pins four row digests. The live `m=8`
order-zero color degree now begins at three. Result: one whole endpoint
degree closed but L1 remains `TARGET`; `m=16` quadratic systems, degree
`3+`, order one, outer divisibility, and the inner lift remain. No Modal job
or compute request was used.

Cycle burn-down:

```text
starting pins: local 4cb03477; canonical e7edb006; upstream b13de811;
               PR #1106 head 98149fc6
ending math pin: local 9167125b; canonical/upstream/PR unchanged
node attacked: l1_mersenne_hnf_m8_order_zero_quadratic_exclusion
result: CLOSED (the m=8 degree-two stratum); NARROWED (L1)
DAG delta: +1 PROVED node, +4 edges; critical math orbit unchanged at
           201 PROVED / 36 CONDITIONAL / 23 TARGET
upstream terminal delta: none; this is not a deployed K/M/L atom
delta-star bracket movement: 0 bits
new assumptions: none; all three dependencies are PROVED
live compute requests: none added or consumed
next route-deciding action: apply the same exact-one-repeat torsion test to
                              m=16, then isolate its even multi-repeat branch
```

**2026-07-26, L1 m=16 single-collision close:**
`l1_mersenne_hnf_m16_order_zero_single_collision_exclusion` applies the
centered-moment/torsion method to the one official `m=16,h=15` row. Its 105
exactly-one-repeat color patterns impose quadratics on `s`; every one is
coprime over `F_8191(mu_16)` to the necessary equation
`binom(s+14,15)^131072=1`. A second basis verifies 105 nonzero resultants
with pinned digest `9c05ecd...e9e31f`. The complete quadratic frontier is
now empty on `m=8` and reduced on `m=16` to even interpolants with at least
two antipodal repeated-color pairs. Result: `NARROWED`; no critical status,
upstream atom, endpoint, Modal job, or compute request changes.

**2026-07-26, L1 complete quadratic color close:**
`l1_mersenne_hnf_m16_order_zero_even_quadratic_exclusion` removes the sole
remaining degree-two shape. An even `m=16` interpolant with two repeated
colors would make the odd and even parts of `P_s` share at least two roots.
The exact first-subresultant coefficients have gcd

```text
s^6(s-3)(s-2)(s-1)^6(s+1)^6(s+2)^5(s+3)^5
(s+4)^4(s+5)^4(s+6)^3(s+7)^3(s+8)^2(s+9)^2(s+10)(s+11),
```

whose roots are all prime-field values and therefore forbidden. An
independent stdlib audit reconstructs the coefficients from 322 Sylvester
minors at 161 points, using the exact determinant degree bound 160. Constant,
linear, and quadratic colors are now empty on all five endpoint rows.
Result: `CLOSED` for endpoint color degree two and `NARROWED` for L1; the
live order-zero degree begins at three. No critical status, endpoint bracket,
upstream terminal, Modal job, or compute request changes.

Cycle burn-down:

```text
starting pins: local 9167125b; canonical e7edb006; upstream b13de811;
               PR #1106 head 98149fc6
ending math pin: local 2fdc6d4b
ending combined pin: local e5baf2ad; canonical 4b4a43a0;
                     upstream/PR unchanged
nodes attacked: l1_mersenne_hnf_m16_order_zero_single_collision_exclusion;
                l1_mersenne_hnf_m16_order_zero_even_quadratic_exclusion
result: CLOSED (degree two on all five HNF endpoint rows); NARROWED (L1)
local DAG delta: +2 PROVED nodes, +10 edges; canonical import adds one
                 noncritical TARGET bridge and its evidence edge
critical delta: none; math orbit remains 201 PROVED / 36 CONDITIONAL /
                23 TARGET, with all 36 conditionals propagation-owned
upstream terminal delta: none; no K/M/L atom or adjacent payment
delta-star bracket movement: 0 bits
new assumptions: none; every consumed dependency is PROVED
live compute requests: none added or consumed
next route-deciding action: use the colored Frobenius congruence/resultant
                              system to classify cubic order-zero colors
```

**2026-07-26, complete m=8 order-zero outer close:**
`l1_mersenne_hnf_m8_order_zero_reciprocal_elimination` bypasses the cubic
split and closes every remaining color degree on all four `m=8,h=7` rows.
For the reciprocal coefficient equations `F_j(s,t)=0`, form
`R_12=Res_t(F_1,F_2)` and `R_13=Res_t(F_1,F_3)`. Exact bounded
interpolation gives degrees 1320 and 1760, and on every official
characteristic their gcd is

```text
s^176(s-1)^4(s+1)^176(s+2)^168(s+3)^162
(s+4)^152(s+5)^128(s+6)^64(s+7)^2.
```

Every root is prime-field valued, contradicting `s notin F_p`. An
independent audit reconstructs all `Q_s` coefficients from 228 companion-
matrix characteristic polynomials before repeating the eight eliminants.
Result: `CLOSED` for the complete `m=8` order-zero outer chamber and
`NARROWED` for L1; `m=16` order zero, order one, and the inner/global
payments remain. No Modal job, compute request, critical status, upstream
terminal, or endpoint bracket changes.

Cycle burn-down:

```text
starting pins: local e5baf2ad; canonical 4b4a43a0; upstream b13de811;
               PR #1106 head 98149fc6
ending math pin: local edfab050; canonical/upstream/PR unchanged
node attacked: l1_mersenne_hnf_m8_order_zero_reciprocal_elimination
result: CLOSED (all color degrees in the four m=8 order-zero outer
        chambers); NARROWED (L1)
DAG delta: +1 PROVED node, +3 edges; critical math orbit unchanged at
           201 PROVED / 36 CONDITIONAL / 23 TARGET
upstream terminal delta: none; no K/M/L atom or adjacent payment
delta-star bracket movement: 0 bits
new assumptions: none; both dependencies are PROVED
live compute requests: CR-L1-MCP-NMCE narrowed to m=16/order-one work;
                       no run launched or consumed
next route-deciding action: derive a certificate-producing reduction for
                              the m=16 reciprocal system, or switch to a
                              nearer critical/upstream terminal if the raw
                              eliminants remain unpriced
```

**2026-07-26, canonical bridge reconciliation:** canonical `f2634a1f` added
a substantial analysis of a hypothetical affine-rank-two budget-three list
witness and proposed reducing its six fibers to the rate-half minimal-index
split-pencil seam. In the joint tree that branch is vacuous: the already
proved `rate_half_list_budget_three_affine_rank_rigidity` excludes affine
rank two at exactly the same `(4d,2d,3d-1)`, `d>=3`, scope. The equality
case would have to inject `2d+2` active coordinates into the six roots of
pairwise affine-linear quotient differences. The chamber bridge is therefore
narrowed to `(d_1,d_2,d_3,b)` for rank three. The rank-flat denominator shows
that lower, not upper, control of `b` is useful. The proposed `(MI2)` import is
also fenced: that theorem assumes a primitive apolar Hankel kernel, whereas
the six residual polynomials form an arbitrary pencil; the applicable
arbitrary-pencil incidence theorem is sharp at six here.

Cycle burn-down:

```text
starting pins: local 007d86e2; canonical 4b4a43a0; upstream b13de811;
               PR #1106 head 98149fc6
canonical integration: local merge 9c95bcd8; canonical f2634a1f
ending math pin: local 9080cb67; upstream/PR unchanged
node attacked: rate_half_list_chamber_affine_rank_bridge
result: NARROWED; s=3 is supplied by an existing PROVED theorem and the
        imported s=2/MI2 route is retired
DAG delta: +1 ev edge and corrected TARGET contract; critical math orbit
           unchanged at 201 PROVED / 36 CONDITIONAL / 23 TARGET
upstream terminal delta: none; upstream has no matching chamber-rank bridge
delta-star bracket movement: 0 bits
new assumptions: none
live compute requests: none added or consumed
next route-deciding action: compute chamber-uniform bounds on
                              (d_1,d_2,d_3,b) and test whether any of the
                              thirteen exact rank-flat caps is at most three
```

**2026-07-26, budget-three compiler route fully adjudicated:** the selected
intersection theorem has `n_0=0`, so the four chosen agreement sets cover the
domain. At a common direction zero all four codeword values coincide; one
selected agreement therefore forces the common value to equal the received
word. This proves `b=0` in every chamber. The remaining generalized-weight
arithmetic then fences the compiler completely. Every incidence type has a
pair attaining `K-1=2d-1` agreements, hence `d_1=2d+1`, and a selected triple
intersection of size at least `d-1`, hence `d_2<=3d+1`. With
`2d+3<=x=d_3<=4d`, the rank-flat expression is bounded below by

```text
x(x-1)(x-2) / (2d^2(x-d-1)) > 4.
```

The last inequality follows from positivity of
`x(x-1)(x-2)-8d^2(x-d-1)` at `x=2d+3` and its positive first and second
derivatives thereafter. Thus its floor is always at least four: neither the
affine-span cap eight nor the rank-flat compiler can prove the required cap
three. The bridge is now PROVED as a route fence, and the thirteen chambers
must be attacked through their official-subgroup arithmetic or a stronger
list theorem.

Cycle burn-down:

```text
starting pin: local 9080cb67; canonical f2634a1f; upstream b13de811;
              PR #1106 head 98149fc6
intermediate theorem pin: local 1e359dfb
ending math pin: local a44a4392; canonical/upstream/PR unchanged
nodes attacked: rate_half_list_budget_three_common_mismatch_zero;
                rate_half_list_chamber_affine_rank_bridge
result: CLOSED (b=0 theorem); CLOSED AS ROUTE FENCE (compiler bridge)
DAG delta: +1 PROVED node, bridge TARGET -> PROVED, +5 edges;
           overall PROVED 1041 -> 1043 and TARGET 69 -> 68
critical delta: none; math orbit remains 201 PROVED / 36 CONDITIONAL /
                23 TARGET
upstream terminal delta: none; this proves a limitation of the harvested
                         Lane-L compiler, not a K/M/L payment
delta-star bracket movement: 0 bits
new assumptions: none; every dependency is PROVED
live compute requests: none added or consumed
next route-deciding action: return to direct official-subgroup arithmetic in
                              rate_half_list_adjacent_crossing, or select a
                              different one of the 23 critical red leaves;
                              do not spend further cycles on this compiler
```

**2026-07-26, L1 m=16 Singular route-pricing attempt:** the one authorized
`R_12` launch stopped during image construction. Modal app
`ap-wGlT1diHx4C7gUii0LhVyq` exposed Debian's default `singular` package
fanout: 891 new packages, 29 upgrades, 1,077 MB of archives, and 4,098 MB
installed. It was terminated at package 310 before a function container or
algebra started. The exact billed amount was `$0.00348072`. The launcher now
suppresses recommended packages, but no retry is authorized by this result.
This is an infrastructure `INCOMPLETE`, not evidence about the eliminant.

Cycle burn-down:

```text
starting pin: local f77bf695; canonical cb1e506c; upstream main b13de811
attempted node: l1_mixed_petal_amplification via the m=16 order-zero
                reciprocal-elimination chamber
result: INCOMPLETE at image build; no algebra or theorem claim
DAG delta: none; critical math orbit remains 201 PROVED / 36 CONDITIONAL /
           23 TARGET
upstream terminal delta: none
delta-star bracket movement: 0 bits
new assumptions: none
compute spend: $0.00348072; the single authorization is consumed
next route-deciding action: integrate canonical cc979e4b, adjudicate its new
                              WCL descent against the critical frontier, and
                              use a non-compute L1 reduction if returning here
```

**2026-07-26, WCL descent reconciliation:** canonical `cc979e4b` correctly
proves that product-one normalisation is unique at odd weight and obstructed
at even weight, and adds a useful specialized `(4,11)` coordinate packet.
Its planning inference was stale: the prior proved
`dli_wcl_extended_six_slot_sparse_divisor_endpoints` already supplies the
parity-separated even locator `F(X)=E(X^2)-XB(X^2)`, exact divisor converse,
and pruned cubic certificate system. Thus `(4,10)` does not need a new
sub-tuple router. All three `ell=4` leaves are already at explicit
finite-characteristic certification: `(4,9)` has a `114/119` pruned system,
`(4,10)` has `129/133`, and `(4,11)` has `142/147`. Direct expanded
remainders are not the only Delta interface. The correct order starts with
`(4,9)` because it is smaller; no descent leaf closes from this correction.

Cycle burn-down:

```text
starting pin: local f3d3e663; canonical cc979e4b; upstream main b13de811
nodes audited: dli_wcl_ell4_weight11_quintic_divisor_descent;
               dli_wcl_extended_six_slot_sparse_divisor_endpoints;
               dli_wcl_zone_coverage
result: RECONCILED; false missing-(4,10)-router premise removed
DAG delta: +3 proved dependency edges; no status change; critical math orbit
           remains 201 PROVED / 36 CONDITIONAL / 23 TARGET
upstream terminal delta: none; open PRs #1091--#1108 contain no WCL
                         characteristic certificate
delta-star bracket movement: 0 bits
new assumptions: none
compute spend: none
next route-deciding action: seek an analytic reduction of the (4,9) Pell/
                              114-by-119 certificate endpoint; do not duplicate
                              the already proved descent or launch CR-004 locally
```

**2026-07-26, `(4,9)` inversion-component close:** anti-reciprocity reduces
the inversion-invariant Pell stratum to four rational and four cubic
branches. Exact branchwise powering modulo `P=YA^2-1` gives obstruction gcd
one on every branch. The complete denominator support is `{2,3,17,19}`, so
the official split gate excludes it. The new PROVED node
`dli_wcl_ell4_weight9_inversion_symmetric_exclusion` is wired by `ev` to the
unchanged TARGET `dli_wcl_slot_4_9_emptiness`. This is genuine component
movement, not full-cell closure: arbitrary nine-subsets of `mu_1024` need
not be inversion-stable.

```text
starting pin: bb4d2188
node attacked: dli_wcl_slot_4_9_emptiness, inversion-invariant component
result: CLOSED (component), NARROWED (parent)
DAG delta: +1 PROVED node, +1 req edge, +1 ev edge; parent remains TARGET
upstream terminal delta: none
delta-star bracket movement: none
new assumptions: inversion invariance, explicitly local and not shared by parent
live compute requests: no retry; full CR-004 remains external/deferred
next route-deciding action: find a complete structural split complementary
                              to inversion invariance, or return to the full
                              114/119 sparse certificate endpoint
```

**2026-07-26, universal unsafe-route correction and identity-prefix harvest:**
an implication audit found that `unsafe_at_crossing` had been promoted without
an every-row instantiation of either local supplier theorem. The corrected
`unsafe_crossing_family_instantiation` target requires an exact `Q`, `V`, or
`M` payload at every proposed predecessor. The independently reconstructed
identity-prefix flexible-budget theorem then closes the `V` payload for the
two deployed MCA rows while leaving the universal quantifier explicit.

Cycle burn-down:

```text
starting pins: local af908721; canonical cc979e4b;
               upstream origin/main b13de811
ending proof pin: local 224720bc; canonical/upstream unchanged
nodes attacked: unsafe_at_crossing; unsafe_crossing_family_instantiation;
                identity_prefix_flexible_budget_unsafe_floor
result: CORRECTED (false green); HARVESTED (general V supplier);
        CLOSED (two deployed MCA unsafe payloads); universal target OPEN
DAG delta: unsafe_at_crossing PROVED -> CONDITIONAL; +1 critical TARGET;
           +1 off-orbit PROVED supplier and +3 evidence edges; five route-local
           E1/zone nodes moved off the critical folder partition
critical delta: math orbit is 242 = 180 PROVED / 38 CONDITIONAL / 24 TARGET;
                every conditional is propagation-owned
upstream terminal delta: none new upstream; the theorem is already proved at
                         b13de811 and is now banked locally under its labels
delta-star bracket movement: none globally; the two deployed unsafe edges are
                             exact finite payloads
new assumptions: none
compute spend: none; proof review and exact integer checks only
next route-deciding action: compile the identity-prefix inequalities over the
                              exact admissible-row descriptor output, classify
                              the residual rows as Q/V/M/uncovered, and mint a
                              smaller algebraic target for the first uncovered
                              exhaustive class
```

**2026-07-26, identity-prefix clean-anchor route exhausted:** the official row
model is parametric rather than a finite row list, and the six RowC/prize
entries are envelope checks. Extracting the pair-root condition against the
exact budget interval gives a complete anchor-level route classification:
five clean anchors cannot use the supplier, while RowC rate `1/16` reduces to
one explicit base-field cutoff. The repository's pre-existing warning that
the RowC characteristic is unpinned prevents a fabricated instantiation.

Cycle burn-down:

```text
starting pin: local 5b1dc9a9; canonical cc979e4b;
              upstream origin/main b13de811
ending proof pin: local e0856fc5; canonical/upstream unchanged
node attacked: unsafe_crossing_family_instantiation, identity-prefix branch
result: CLOSED AS ROUTE CUT on five clean anchors; NARROWED to one typed
        RowC-1/16 subfield branch; universal target remains OPEN
DAG delta: +1 off-orbit PROVED node, +1 req edge, +1 evidence edge;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24
upstream terminal delta: none; candidate for a grouped unsafe-side/no-go packet
delta-star bracket movement: none
new assumptions: none; the surviving branch prints its required domain-field
                 containment instead of assuming the unpinned RowC prime
compute spend: none; 2,527 exact router checks and one small binomial only
next route-deciding action: skip identity-prefix on the high-field clean rows;
                              audit the existing quotient/direct-value witness
                              at their exact unsafe predecessors, beginning
                              with whether the banked A-1 quotient witness is
                              already a valid ambient-field Q payload
```

**2026-07-26, clean-anchor qfloor route exhausted:** exact derivation of the
canonical quotient orders confirms that the above-budget `A-1` binomial
censuses are outside the proved qfloor norm regime on every clean anchor. The
smallest raw-count margin is still a factor of `1245`, so the witness family
is large; the missing fact is distinctness after reduction, not multiplicity.

Cycle burn-down:

```text
starting pin: local cb8dd9a6; canonical cc979e4b;
              upstream origin/main b13de811
ending proof pin: local 57256915; canonical/upstream unchanged
node attacked: unsafe_crossing_family_instantiation, quotient-Q branch
result: CLOSED AS ROUTE CUT on all six clean anchors; direct E1/value-set
        injectivity remains OPEN
DAG delta: +1 off-orbit PROVED node, +1 req edge, +1 evidence edge;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24
upstream terminal delta: none; this is a scoped no-go extraction
delta-star bracket movement: none
new assumptions: none
compute spend: none; six exact powers and binomial comparisons
next route-deciding action: treat the clean quotient family as a direct-value
                              problem; determine the exact Acl/value-set lower
                              bound required on each candidate and whether one
                              route-uniform exceptional-prime theorem can pay
                              all six, otherwise move to an exact post-paid M
                              family rather than reusing qfloor
```

**2026-07-27, tangent-floor low-field branch compiled:** upstream
`prop:floor` was independently reconstructed and converted into an exact
field-order router at the six clean predecessor formulas. The guaranteed
`n-a` slopes pay a real low-field slice, but none of the named high-budget
anchors. This narrows the residual unsafe problem without asserting a converse
or upper-bounding the full bad set of the tangent line.

Cycle burn-down:

```text
starting pin: local 024156c3; canonical 4cffa790;
              upstream origin/main b13de811
ending proof pin: local ca8630f6; canonical/upstream unchanged
node attacked: unsafe_crossing_family_instantiation, tangent-V branch
result: CLOSED on the guaranteed low-field payload; CLOSED AS APPLICABILITY
        CUT at all six named envelopes; universal target remains OPEN
DAG delta: +2 off-orbit PROVED nodes, +1 req edge, +2 evidence edges;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24
upstream terminal delta: upstream theorem banked locally under prop:floor;
                         finite envelope classifier is ours-only
delta-star bracket movement: none at the named envelopes
new assumptions: none
compute spend: none; bounded exact local replay only
next route-deciding action: classify the residual high-field rows and compare
                              direct E1 against an exact post-paid M supplier
```

**2026-07-27, averaged occupancy eliminated at clean envelopes:** the existing
row descriptor was confirmed to validate arbitrary inputs without inferring a
safe agreement, so there is no finite official row list to classify. On the
six named envelopes, however, the largest possible support-family first
moment is already below budget. This removes the `M` supplier before overlap
optimization and leaves explicit `Q`/`V` as the positive unsafe routes.

Cycle burn-down:

```text
starting pin: local 8c845519; canonical 1aca1792;
              upstream origin/main b13de811
ending proof pin: local 0893de24; canonical/upstream unchanged
node attacked: unsafe_crossing_family_instantiation, averaged-M branch
result: CLOSED AS ROUTE CUT at all six named high-budget envelopes;
        universal target remains OPEN
DAG delta: +1 off-orbit PROVED node, +2 req edges, +1 evidence edge;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24
upstream terminal delta: none; exact finite route cut is ours-only
delta-star bracket movement: none
new assumptions: none
compute spend: none; exact integers and bounded local replay only
next route-deciding action: direct E1/value-set control on the pair-feasible
                              generated-field class, or a new explicit V line
```

**2026-07-27, pair-feasible E1 field axis closed:** the strict official field
cap and the exact six thresholds imply that every pair-feasible quotient root
set generates the ambient field. This removes extension transfer from the live
E1 collision target while preserving the unresolved proper-subfield branches
with the universal router.

Cycle burn-down:

```text
starting pin: local 03de7042; canonical dd4ef328;
              upstream origin/main b13de811
ending proof pin: local e169a43f; canonical/upstream unchanged
node attacked: e1_official_prime_exception_control, field-normalization axis
result: CLOSED AS ROUTE REDUCTION; exact collision-pair target remains OPEN
DAG delta: +1 off-orbit PROVED node, +1 req edge, +2 evidence edges;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24
upstream terminal delta: none; finite route reduction is ours-only
delta-star bracket movement: none
new assumptions: none
compute spend: none; 1,199 bounded tower checks plus exact thresholds
next route-deciding action: exploit ambient generation in the norm-divisor or
                              sparse-kernel collision count, seeking a theorem
                              or an exact pair-feasible counterexample
```

**2026-07-27, pair-feasible E1 prime-field axis closed:** ambient generation
still left a possible extension degree and therefore did not validate the
prime-field kernel interface. The exact degree identity and perfect-power
interval checks remove that gap at all six named anchors. The simultaneous
canonical audit also exposed unreplayable legacy proof debt and pinned it
against growth without treating missing artifacts as mathematical refutations.

Cycle burn-down:

```text
starting pins: local e3084268; canonical 342b52d9;
               upstream origin/main b13de811
ending proof pin: local 260395c5; canonical d18fdc83;
                  upstream unchanged
node attacked: e1_official_prime_exception_control, extension-degree axis
result: CLOSED AS ROUTE REDUCTION; exact prime-field collision target OPEN
DAG delta: +1 off-orbit PROVED node, +1 req edge, +2 evidence edges;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; reproducibility debt now
                pinned at 44 hollow critical nodes, 42 marked PROVED
upstream terminal delta: none; exact finite reduction is ours-only
delta-star bracket movement: none
new assumptions: none; the canonical quotient set is cyclic of printed order
compute spend: none; 14 exact integer-root checks and bounded regressions
next route-deciding action: bound or falsify the exact E1 collision allowance
                              over primes p=1 mod N in the two budget intervals
```

**2026-07-27, E1 low swap-distance bands closed:** folded coefficient Parseval
turns the cyclotomic norm estimate into an `L2` bound. Exact profile arithmetic
then removes the first four `N=256` bands and the first `N=512` band. The latest
canonical literature sweep was checked before banking; it identifies no
external theorem for this fixed-prime E1 ledger.

Cycle burn-down:

```text
starting pins: local 09c6cceb; canonical d18fdc83;
               upstream origin/main b13de811
ending proof pin: local c2bf0fd9; canonical b55c21d0;
                  upstream unchanged
ending profile-refinement pin: local 789e190e
node attacked: e1_official_prime_exception_control, low-distance bands
result: CLOSED for s<=4 at N=256 and s=1 at N=512; first open bands
        reduced to two folded profiles apiece; parent target OPEN
DAG delta: +1 off-orbit PROVED node, +2 req edges, +2 evidence edges;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: none; 164 profile and 336 toy orthogonality checks
next route-deciding action: attack profiles (4,2,0),(3,4,0) at N=256 and
                              (1,2,0),(0,4,0) at N=512 by exact norm structure
```

**2026-07-27, N=512 four-singleton profile closed:** exact negacyclic
autocorrelation variance separates the low-variance cyclotomic-product cases
from a global logarithmic norm deficit. No large computation was used.

Cycle burn-down:

```text
starting pins: local dae9de7b; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local 46c5c261
node attacked: e1_official_prime_exception_control, N=512 s=2 profile (0,4,0)
result: CLOSED for profile (0,4,0); parent target OPEN
DAG delta: +1 off-orbit PROVED node, +2 req edges, +2 evidence edges;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25;
                reproducibility debt unchanged
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: none; bounded toy autocorrelation replay only
next route-deciding action: attack the sole remaining N=512,s=2 profile
                              (1,2,0) by exact trinomial norm structure
```

**2026-07-27, complete N=512 distance-two band closed:** a finite but
route-uniform signed-support certificate screens every possible prime in both
field intervals. Exact interval division replaces integer factorization.

Cycle burn-down:

```text
starting pins: local 581c487d; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local dc74d931
node attacked: e1_official_prime_exception_control, N=512 s=2 profile (1,2,0)
result: CLOSED for profile (1,2,0) and complete s=2 band; parent target OPEN
DAG delta: +1 off-orbit PROVED node, +3 req edges, +2 evidence edges;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: short one-container Modal runs only; two load-bearing exact
               replays, no run above 91 MB and aggregate well below $1
next route-deciding action: compare N=512,s=3 against the N=256,s=5 profiles;
                              attack the smaller exact orbit quotient first
```

**2026-07-27, N=256 square-mass-16 high variance removed:** an exact
logarithmic deficit converts autocorrelation energy into the six norm bits
needed at the field endpoint.

Cycle burn-down:

```text
starting pins: local e28e1d04; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local d2dc303b
node attacked: e1_official_prime_exception_control, N=256 s=5 profile (3,4,0)
result: NARROWED to positive even autocorrelation variance V<=134;
        parent target OPEN
DAG delta: +1 off-orbit PROVED node, +2 req edges, +2 evidence edges;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: none; exact rational arithmetic only
next route-deciding action: classify the bounded low-variance residual of
                              profile (3,4,0), beginning with realizable V
```

**2026-07-27, N=256 proper-conductor supports excluded:** exact subfield
descent shows that a proper-conductor first-band norm has no prime divisor at
the live field scale. A bounded falsification test killed the stronger
periodicity classification before it entered the DAG.

Cycle burn-down:

```text
starting pins: local d08646bc; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local 7a8f103f
node attacked: e1_official_prime_exception_control, N=256 s=5 conductor split
result: NARROWED to full-conductor supports in both profiles; parent target OPEN
DAG delta: +1 off-orbit PROVED node, +2 req edges, +2 evidence edges;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: one 6.3-second Modal orchestration, peak 55 MB, well below $1;
               no computation is load-bearing
falsification: full-conductor profile-(3,4,0) vector found at V=36, so low
               variance does not imply proper conductor
next route-deciding action: classify the full-conductor V<=134 residual by
                              repeated-difference cancellation structure
```

**2026-07-27, N=256 2-adic cofactor gate banked:** total ramification turns
the small norm cofactors into exact singleton-exponent restrictions in both
first-band profiles.

Cycle burn-down:

```text
starting pins: local f1d30ba8; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local f7d50f3f
node attacked: e1_official_prime_exception_control, N=256 s=5 2-adic screen
result: NARROWED to mu<=5 in (3,4,0) and singleton gap not 0 mod 32
        in (4,2,0); parent target OPEN
DAG delta: +1 off-orbit PROVED node, +2 req edges, +2 evidence edges;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: none; exact integer and local-field arithmetic only
next route-deciding action: combine the 2-adic screen with the signed
                              repeated-difference cancellation ledger
```

**2026-07-27, N=256 signed-chord gate banked:** the bounded variance residual
is now an exact additive-structure problem rather than a generic sparse-support
problem.

Cycle burn-down:

```text
starting pins: local 83d6fe00; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local 9e539677
node attacked: e1_official_prime_exception_control, N=256 (3,4,0) residual
result: NARROWED to signed 3-term-progression/parallelogram templates;
        parent target OPEN
DAG delta: +1 off-orbit PROVED node, +1 req edge, +2 evidence edges;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: none; exact autocorrelation and matching arithmetic only
next route-deciding action: classify the signed template types jointly with
                              full-conductor and 2-adic screens
```

**2026-07-27, N=256 local-norm cofactors collapsed:** the explicit norm group
of the conductor-256 local cyclotomic extension removes almost all cofactor
ambiguity before any template norm is computed.

Cycle burn-down:

```text
starting pins: local 0d2ad4ef; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local 89dc4e5c
node attacked: e1_official_prime_exception_control, N=256 cofactor windows
result: NARROWED to five cofactors in (3,4,0) and 419 in (4,2,0);
        parent target OPEN
DAG delta: +1 off-orbit PROVED node, +2 req edges, +2 evidence edges;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none; standard explicit local reciprocity is cited and pinned
compute spend: one 7.1-second Modal orchestration, 513 FLINT resultants in
               0.177 container-seconds; no computation is load-bearing
next route-deciding action: prove the odd parts of the signed-template norms
                              are composite or outside both row intervals
```

**2026-07-27, N=256 sparse-L1 variance refinement:** the attempted universal
odd-part factorization was first falsified by an exact 248-bit prime below the
row floor. The replacement analytic route uses autocorrelation sparsity to
remove twelve additional variance values.

Cycle burn-down:

```text
starting pins: local 1b13e252; canonical b55c21d0;
               upstream origin/main b13de811
route-fence pin: local 20787068
ending proof pin: local 3268bcf2
node attacked: e1_official_prime_exception_control, N=256 (3,4,0) variance
result: NARROWED from positive even V<=134 to V<=110; signed cancellation
        strengthened from C<=-7 to C<=-13; parent target OPEN
DAG delta: +1 off-orbit PROVED node, +2 req edges, +2 evidence edges;
           signed-chord dependency repointed to the sharpened child
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: two short one-container route tests; exact proof uses no Modal
next route-deciding action: extend the sparse moment majorant below V=112 or
                              classify the stronger C<=-13 templates
```

**2026-07-27, N=256 chord-deficit refinement:** a profile-specific charging
lemma extends the analytic variance exclusion by three further values without
enumeration or new assumptions.

Cycle burn-down:

```text
starting pins: local 2967967b; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local 06e0ef63
node attacked: e1_official_prime_exception_control, N=256 (3,4,0) variance
result: NARROWED from positive even V<=110 to V<=104; signed cancellation
        strengthened from C<=-13 to C<=-15; parent target OPEN
DAG delta: no new node or edge; two existing PROVED contracts strengthened;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: none; exact integer and rational arithmetic only
next route-deciding action: close the V=104 logarithmic gap by a sharper
                              phase/L1 bound, or classify the C<=-15 templates
```

**2026-07-27, N=256 low-slack endpoints excluded:** the exact local slack
classification closes the two quadratic-majorant rows immediately below the
general chord-deficit range.

Cycle burn-down:

```text
starting pins: local 8f2da00e; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local 80074790
node attacked: e1_official_prime_exception_control, N=256 (3,4,0) variance
result: NARROWED from positive even V<=104 to V<=100; signed cancellation
        strengthened from C<=-15 to C<=-16; parent target OPEN
DAG delta: no new node or edge; two existing PROVED contracts strengthened;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: two RAM-guarded relaxed DPs under 16 seconds each discovered
               the pattern; exact proof and verifier do not depend on them
next route-deciding action: exploit the equality templates at E=50,L=28 or
                              replace the quadratic logarithmic majorant
```

**2026-07-27, N=256 variance 100 excluded:** the geometry-only endpoint
shortcut was falsified and replaced by an exact optimized quadratic
majorant.

Cycle burn-down:

```text
starting pins: local bbfeb42c; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local 535a2e5f
node attacked: e1_official_prime_exception_control, N=256 (3,4,0) variance
result: NARROWED from positive even V<=100 to V<=98; C<=-16 unchanged;
        parent target OPEN
DAG delta: no new node or edge; two existing PROVED contracts strengthened;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: one 16-worker bounded Modal falsifier and one exact
               one-container norm probe; both completed in seconds and are
               non-load-bearing
route fence: full-conductor E=50,L=28 geometry exists; L<=27 is false
next route-deciding action: extend the exact low-slack L table and optimized
                              majorants to V=98 and below
```

**2026-07-27, N=256 variances 96 and 98 excluded:** the low-slack ledger and
optimized-majorant route extends without additional computation.

Cycle burn-down:

```text
starting pins: local a8ffea1f; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local ed7662cf
node attacked: e1_official_prime_exception_control, N=256 (3,4,0) variance
result: NARROWED from positive even V<=98 to V<=94; signed cancellation
        strengthened from C<=-16 to C<=-17; parent target OPEN
DAG delta: no new node or edge; two existing PROVED contracts strengthened;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: none; exact finite slack and rational Taylor arithmetic only
next route-deciding action: classify slack 7--10 and optimize the V=94/92
                              majorants, with exact feasibility checks
```

**2026-07-27, N=256 variances 90 through 94 excluded:** matching-aware
charge decompositions and tight-intercept quadratic majorants continue the
same analytic route.

Cycle burn-down:

```text
starting pins: local f45775fa; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local f09f1d93
node attacked: e1_official_prime_exception_control, N=256 (3,4,0) variance
result: NARROWED from positive even V<=94 to V<=88; signed cancellation
        strengthened from C<=-17 to C<=-19; parent target OPEN
DAG delta: no new node or edge; two existing PROVED contracts strengthened;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: none; exact finite slack and rational Taylor arithmetic only
next route-deciding action: determine whether the optimized quadratic route
                              continues at E=44 or reaches its true endpoint
```

**2026-07-27, N=256 variances 86 and 88 excluded:** a finite relaxed
minimum-energy recurrence makes the low-slack endpoint argument exact and
extends the optimized-majorant route by two rows.

Cycle burn-down:

```text
starting pins: local 9363c0d2; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local cd5dff92
node attacked: e1_official_prime_exception_control, N=256 (3,4,0) variance
result: NARROWED from positive even V<=88 to V<=84; signed cancellation
        strengthened from C<=-19 to C<=-20; parent target OPEN
DAG delta: no new node or edge; two existing PROVED contracts strengthened;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: none; exact finite recurrence and rational Taylor arithmetic
next route-deciding action: classify the E=42,L=24 equality patterns and
                              test phase-sensitive or higher-moment bounds
```

**2026-07-27, N=256 variance 84 excluded:** exact geometric witnesses first
falsified the tempting `E=42 => L<=23` repair. A global nested-layer count
then bounded the third central moment, and a cubic Hermite logarithmic
majorant closed the endpoint without geometric classification.

Cycle burn-down:

```text
starting pins: local 48bd9578; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local a96150b7
node attacked: e1_official_prime_exception_control, N=256 (3,4,0) variance
result: NARROWED from positive even V<=84 to V<=82; C<=-20 unchanged;
        parent target OPEN
DAG delta: no new node or edge; two existing PROVED contracts strengthened;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: about 85 short bounded Modal containers, roughly eight
               aggregate CPU-minutes; all exploratory and non-load-bearing
route fence: full-conductor E=42,L=24 geometry exists; L<=23 is false
next route-deciding action: apply the layered-moment method at E=41 or
                              combine it with the exact slack table
```

**2026-07-27, N=256 variance 82 excluded:** the exact slack and layered
third-moment mechanism continues at the next energy, using the same global
Hermite majorant.

Cycle burn-down:

```text
starting pins: local e4d24fca; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local f2057a6b
node attacked: e1_official_prime_exception_control, N=256 (3,4,0) variance
result: NARROWED from positive even V<=82 to V<=80; signed cancellation
        strengthened from C<=-20 to C<=-21; parent target OPEN
DAG delta: no new node or edge; two existing PROVED contracts strengthened;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: one short Modal symbolic-derivation container; exact proof and
               verifier are local, deterministic, and Modal-independent
next route-deciding action: extend the slack table and layered-moment
                              certificate to E=40 or locate its endpoint
```

**2026-07-27, N=256 variances 78 and 80 excluded:** the exact slack and
layered-third-moment route continues for two rows and then reaches a measured
cubic-Hermite boundary at variance 76.

Cycle burn-down:

```text
starting pins: local b1d4b944; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local 45171710
node attacked: e1_official_prime_exception_control, N=256 (3,4,0) variance
result: NARROWED from positive even V<=80 to V<=76; signed cancellation
        strengthened from C<=-21 to C<=-22; parent target OPEN
DAG delta: no new node or edge; two existing PROVED contracts strengthened;
           no critical status change
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: one short bounded Modal route-map container; proof and
               verifier are local, deterministic, and Modal-independent
route fence: best tested two-contact cubic at V=76 has margin about
             -0.00262488212622; this cubic family must not be extrapolated
next route-deciding action: add a fourth-moment or geometry-sensitive
                              invariant at E=38 instead of extending cubics
```

**2026-07-27, N=256 variance-76 periodic autocorrelation excluded:** exact
route analysis identified the needed third-moment threshold and the strongest
subgroup example; a small-field norm argument then removes the entire
subgroup-supported chamber.

Cycle burn-down:

```text
starting pins: local 78225c5f; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local 5497a588
node attacked: e1_official_prime_exception_control, N=256 (3,4,0), V=76
result: NEW PROVED autocorrelation-subfield exclusion; every live V=76
        candidate has a nonzero A_d with 4 not dividing d; residual V<=76
DAG delta: one PROVED background node and four edges added; parent target OPEN
critical delta: math orbit remains 242 = 180/38/24; submission target set 25
upstream terminal delta: none; theorem is ours-only and crosswalked
delta-star bracket movement: none
new assumptions: none
compute spend: bounded exploratory Modal only: one direct CP-SAT run, six
               threshold shards, and eight 15-second geometry workers;
               all proof claims replay locally without Modal
route fences: continuous cubic and elementary quartic dual both miss;
              generic CP-SAT upper bounds are too weak and must not be scaled
next route-deciding action: prove the nonperiodic E=38 weighted-Schur cap
                              M_3<=2806 from the 24 slack signatures
```

**2026-07-27, N=256 variance-76 quotient-Schur closure:** the nonperiodic
third-moment bottleneck was reduced to exact mod-16 fiber capacities and
closed by a complete low-memory census.

Cycle burn-down:

```text
starting pin: local abcb2258
node attacked: e1_official_prime_exception_control, N=256 (3,4,0), V=76
result: NEW PROVED quotient-Schur exclusion; global live M_3<=2796;
        V=76 excluded and residual improves to positive even V<=74
DAG delta: one PROVED background node and five edges added; parent target OPEN
compute: 80 cheap Modal shards, 43,153,083 complete allocations, under 20 sec;
         final run ap-n57PHWIhpfTIODFu1x2CMu
new assumptions: none
route fences: generic CP-SAT bounds and the parity-purity lemma are retired;
              the final proof uses exact quotient capacities plus the 4Z cut
next route-deciding action: derive the E=37 L1/profile ledger and test whether
                              the quotient-Schur/cubic mechanism closes V=74
```

**2026-07-27, N=256 variance-74 quotient-Schur closure:** the inherited
quotient mechanism was refined by an exact inner-layer Schur census and closes
the next variance endpoint.

Cycle burn-down:

```text
starting pin: local 1ebf7aec
node attacked: e1_official_prime_exception_control, N=256 (3,4,0), V=74
result: NEW PROVED quotient-Schur exclusion; global live M_3<=2576;
        V=74 excluded and residual improves to positive even V<=72
DAG delta: one PROVED background node and five edges added; parent target OPEN
compute: 48 cheap Modal shards per pass; final complete run
         ap-CQM1N1zJGw5E0FXC4k6qim; 19,732,753 allocations
new assumptions: none
route decision: the raw 2626 quotient obstruction was repaired only after
                proving the support-specific inner bound R(B,B,B)<=174
next route-deciding action: derive the E=36 L1/profile and cubic ledgers before
                              deciding whether quotient descent remains viable
```

**2026-07-27, N=256 variance-72 quotient-Schur closure:** the inherited
quotient mechanism remains viable after a support-specific `Z/64 Z` inner
Schur theorem and closes a third consecutive variance endpoint.

Cycle burn-down:

```text
starting pin: local 243645b1
node attacked: e1_official_prime_exception_control, N=256 (3,4,0), V=72
result: NEW PROVED quotient-Schur exclusion; global live M_3<=2344;
        V=72 excluded and residual improves to positive even V<=70
DAG delta: one PROVED background node and five edges added; parent target OPEN
compute: 48 quotient shards and 16 inner-census shards; final runs
         ap-UO3twT5yf4p6bQ4Dy8sktP and ap-Rz22K5DtG8oBeelSyV39Zd;
         8,144,380 quotient allocations and 7,888,725 inner sets
new assumptions: none
route decision: the raw 2398 obstruction is removed by the exact
                R(B,B,B)<=174 theorem; the resulting cap is 33 below threshold
next route-deciding action: derive the E=35 L1/profile and cubic ledgers and
                              test whether the exact quotient descent persists
```

**2026-07-27, N=256 variance-70 quotient-Schur closure:** a two-count
outer-only miss was resolved by exhausting the exact nested three-layer
coupling rather than refining the quotient globally.

Cycle burn-down:

```text
starting pin: local a6964327
node attacked: e1_official_prime_exception_control, N=256 (3,4,0), V=70
result: NEW PROVED quotient-Schur exclusion; global live M_3<=2162;
        V=70 excluded and residual improves to positive even V<=68
DAG delta: one PROVED background node and five edges added; parent target OPEN
compute: one 32-shard Modal run, ap-Gwlrl9cLfJsa2bS83BFw4k;
         2,946,287 quotient allocations; four high outers and 276 nestings
new assumptions: none
route decision: quotient descent persists, but the first outer-only miss shows
                that exact nested coupling must precede any finer quotient
next route-deciding action: derive the E=34 L1/profile and cubic ledgers and
                              test whether nesting remains a bounded exception
```

**2026-07-27, N=256 variance-68 route boundary:** exact preflight shows that
the sequential quotient descent changes character at `E=34`.

Cycle burn-down:

```text
starting pin: local 859064a3
node attacked: e1_official_prime_exception_control, N=256 (3,4,0), V=68
result: NO STATUS CHANGE; L<=20, 24 profiles, cubic threshold M_3<=1947;
        six exceptional profiles remain, including three/four-layer cases
compute: tiny exact symbolic preflight only; no Modal campaign launched
new assumptions: none
route decision: stop endpoint-by-endpoint quotient runs until one common
                nested-layer compiler or a stronger analytic certificate exists
next route-deciding action: return to a shared critical route with a new
                              theorem candidate rather than scale six censuses
```

**2026-07-27, Mattarei affine-pair import and DSP8 nodal payment:** the
primary 2007 source resolves the apparent contradiction in Fable's literature
map and supplies a stronger theorem than its provisional substitution used.
Mattarei permits arbitrary Fermat coefficients, so the theorem covers both
the twisted order-`n` quotient fiber and the order-`3n` cube-preimage fiber.
His Remark 3 explicitly distinguishes the Garcia--Voloch route from the
one-polynomial HBK/Stepanov method fenced by NSB2.

Cycle burn-down:

```text
starting pins: local a712d6ac; canonical b55c21d0;
               upstream origin/main b13de811
ending proof pin: local a7330b59
node attacked: f3_h3_dsp8_correlation_bound
result: NEW PROVED Mattarei transport; raw nodal payment improves from
        <552/<2387 n^2 to <116/<498 n^2 in the one-/three-root cases;
        more than 1443n^2 of the current raw allowance remains for smooth
        traces; DSP8 stays TARGET
uniform target: 25(10K_25^0+17K_25^A)<=12134n^2, improving the former
                160(10K_25^0+17K_25^A)<=76599n^2
DAG delta: one PROVED background node; three req edges replaced; no critical
           status change
source: Mattarei, Finite Fields Appl. 13 (2007), 773-777,
        DOI 10.1016/j.ffa.2006.03.005, arXiv math/0511339v1
audit: 798,864 exact small-field affine fixtures, including 254,822 nonempty
       slopes outside the subgroup; proportional-form mutation rejected
compute spend: none; tiny local exact arithmetic only, no Modal
new assumptions: none; prime-field scope is explicit
upstream map: OVERLAP with SP primitive shift-pair control, not a proof of the
              full upstream exact second-moment ledger
next route-deciding action: exploit smooth trace geometry and the remaining
                              >1443n^2 budget; do not return to nodal retuning
```

**2026-07-27, exact DSP8 smooth residual isolated:** the new nodal payment is
subtracted once in the raw `G=4K` ledger, leaving a single printed smooth
primitive shift-pair target rather than a qualitative instruction to
"control smooth traces."

Cycle burn-down:

```text
starting pin: local 29cef0d8
ending proof pin: local e7faf967
node attacked: f3_h3_dsp8_correlation_bound
result: NEW PROVED smooth-residual router; DSP8 remains TARGET
exact open target: 10G_sm^0+17G_sm^A<=(36086/25)n^2 uniformly,
                   equivalently
                   10K_sm^0+17K_sm^A<=(18043/50)n^2
one-root allowance: (45636/25)n^2 in raw normalization
DAG delta: one PROVED background node and four edges; no critical status
           change
compute spend: none; exact rational subtraction only
new assumptions: none
upstream map: exact finite budget interface for SP primitive shift-pair
              control; not an estimate for the upstream ledger
next route-deciding action: derive a smooth elliptic trace-pair estimate that
                              retains richness, class, and quotient weights
```

**2026-07-27, DSP8 prime-subfield scope bridge:** the apparent extension-field
obstruction to the Mattarei affine-pair supplier is removed exactly for the
deployed KoalaBear affine factors, while the Mersenne row is fenced rather
than silently generalized.

Cycle burn-down:

```text
starting pins: local 9ef1680d; canonical acb39b1f;
               upstream origin/main b13de811
ending proof pin: local 155439f6
node attacked: f3_h3_dsp8_correlation_bound
result: NEW PROVED prime-subfield descent; if K and one nonconstant affine
        factor are defined over F_p, K-membership forces the extension-field
        variable into F_p and the count is literally prime-field-valued
KoalaBear scope: p-1=127*2^24, n=2^21, index 1016, 1016^3>4n;
                  p=2 mod 3 makes the cube preimage equal H
Mersenne fence: v_2((2^31-1)-1)=1, so its order-2^21 quartic subgroup does
                not descend; no extension-subgroup Mattarei bound is claimed
DAG delta: one PROVED background node and two edges; DSP8 remains TARGET
compute spend: none; exact integer and finite-field scope replay only
new assumptions: none
upstream map: portable scope rule for SP affine factors; not primitive
              shift-pair control and not a full second-moment estimate
next route-deciding action: retain this supplier only on descending affine
                              charts and seek a separate Mersenne supplier
```

**2026-07-27, exact DSP8 smooth quotient-cap compiler:** the quotient pair can
be removed pointwise with the Mattarei bound, but doing so prints a genuinely
strong unweighted smooth primitive-SP obligation. This decides which existing
additive-combinatorial estimates are too weak before further computation.

Cycle burn-down:

```text
starting pin: local 9ef1680d
ending proof pin: local 155439f6
node attacked: f3_h3_dsp8_correlation_bound
result: NEW PROVED quotient-cap compiler; DSP8 remains TARGET
exact implication: G_sm^c<C_M n^(2/3)U_sm^c and
                   189(10U_sm^0+17U_sm^A)<=144344n^(4/3)
class-blind supplier: U_sm^0+U_sm^A<=(144344/3213)n^(4/3)
                      <44.926n^(4/3)
DAG delta: one PROVED background node and four edges; no critical status flip
route decision: ordinary O(n^2 log n) shifted energy is too weak, while the
                available multi-shift theorem sees repeated copies of one
                quotient shift and gives no n-power gain
compute spend: none; exact rational compilation and mutation audits only
new assumptions: none; U_sm retains smoothness, richness, trace class,
                 split, and signed-disjointness
upstream map: exact finite consumer threshold for primitive SP, not an SP
              estimate and not an identification with every upstream stratum
next route-deciding action: prove an O(n^(4/3)) rich signed-disjoint smooth
                              base-tuple theorem, or return to a direct
                              weighted/endpoint route that avoids this loss
```

**2026-07-27, scoped H3 norm-one affine quotient cap:** a quadratic norm
identity gives a sharp raw quotient-fiber theorem on multiplicative subgroups
inside a norm-one torus. An upstream domain audit then prevented an invalid
Mersenne line-round promotion.

Cycle burn-down:

```text
starting pins: local 155439f6; canonical d17038d6;
               upstream origin/main b13de811
ending proof pin: local 8691e84e
node attacked: f3_h3_mobius_excess_half / DSP8 quotient factor
result: NEW PROVED scoped theorem; for H in a quadratic norm-one torus,
        every nondegenerate affine intersection has size at most two;
        the H3 identity point gives R(t)<=1
concrete instance: p_M=2^31-1, n=2^21, and the order-n multiplicative
                   subgroup of F_(p_M^4)^* lies in F_(p_M^2) norm one;
                   hence 17X_18<17n^2<300n^2 on that subgroup instance
scope catch: upstream's deployed M31 line round is D=chi(mathcal D) for a
             twin coset, not H; no Chebyshev projection adapter is proved,
             so no deployed-row or adjacent-safe status changes
upstream overlap: their two-slope split-pencil theorem applies only after six
                  routed branches are removed; it is not this raw fiber cap
DAG delta: one PROVED background node and three edges; critical nodes stay open
audit: complete F_(31^2), order-16 torus replay; 210 sharp affine targets;
       eight hostile mutations; DAG, harness, protocol, and manifest green
compute spend: none; tiny local exact arithmetic only
new assumptions: none
next route-deciding action: do not pursue this as an M31 shortcut; return to
                              a prize-critical leaf or prove a genuine
                              Chebyshev-line adapter before claiming transfer
```

**2026-07-27, order-128 high-field integer kernel closed analytically:** the
dim-64 folded certificate has a proof branch that needs no SVP transcript.
For an odd prime `p>253^32` containing `mu_128`, odd-conjugate Parseval gives
`|Norm(W)|<=S^32`. If a folded coefficient is odd then `S<=253`; if all are
even, division by two gives norm at most `64^32`. Hence every ternary kernel
vector is antipodal/cyclotomic.

Cycle burn-down:

```text
starting pin: local 5babf9cd; canonical dd76658c;
              upstream origin/main b13de811
node attacked: integer_code_distance_cert
result: NEW PROVED high-field order-128 branch; target remains TARGET
DAG delta: one PROVED background node and two edges; no critical status flip
exact paid scope: p>253^32, order 128, complete folded cube
remaining scope: p<=253^32, other quotient orders, literal adopted-row
                 registry, and proof that the certified cell count exceeds B*
route cuts: rounded fpylll output is still not a certificate; a nonofficial
            rational-base prime is not an adopted prize row
compute spend: none; tiny exact arithmetic only, no Modal
new assumptions: none
verification: theorem verifier, DAG structure, conditional propagation,
              critical-harness coverage, orbit census, and manifest self-test
              pass; composed replay is blocked before the delta by the
              pre-existing failed dli_wcl_weight5_first64_mitm_exclusion row
upstream state: open PR #1107 supplies a literal corridor prime but no
                value-set budget or kernel transport is claimed from it
next route-deciding action: pin the actual residual row registry and budget;
                              then attack only the rows outside the theorem
```

**2026-07-27, integer-certificate quantifier repaired:** the requested row
registry does not exist. `official_row_primes_pinning` proves that the prize
quantifies over an admissible family, not a hidden finite prime table. The
target now requires either a family-uniform no-vector theorem or a named
exhibit certificate whose consumers are narrowed to that same field. Every
payload must print its exact cell cardinality and `B*`; solver totality alone
cannot establish a collision-free verdict.

The four pinned Proth prize exhibits have 167--171-bit primes, below the
`253^32` high-field threshold. The 256-bit corridor prime is above the
threshold and therefore has a free order-128 folded-kernel certificate, but
its current packet only pins a denominator and safe-side comparisons: no
lattice-route class cell or value-set budget consumes it. It must not be used
to promote `integer_code_distance_cert`.

```text
node audited: integer_code_distance_cert
result: specification repair; status remains TARGET
DAG delta: official_row_primes_pinning becomes an ev scope guard
route cut: no finite "official-row certificate sweep" is well posed
residual: universal row assignment plus no-vector and cell-count certificates
compute spend: none
next decision: leave this as the alternative lattice siege unless a real
               consumer row is pinned; select a closure-capable critical leaf
```

**2026-07-27, complete m=16 order-zero HNF close:** the corrected bounded
Singular route is cheap and exact. For the first three reciprocal coefficient
equations, the two eliminants have degrees `11472` and `15296`; their
degree-`9912` gcd has squarefree radical

```text
s(s-1) product_(j=1)^15(s+j).
```

It divides `s^8191-s`, so every common solution is prime-field valued and
contradicts the HNF condition `s notin F_8191`. A second worker constructed
`Q_s` from the companion matrix of multiplication by `W^16`, traces, and
Newton identities rather than from `Res(P_s,Z-W^16)`; it reproduced both
eliminants, their gcd, and the radical hash exactly. The local verifier
independently checks the radical expansion, squarefreeness, and field-
polynomial divisibility.

```text
node proved: l1_mersenne_hnf_m16_order_zero_reciprocal_elimination
result: CLOSED, complete m=16,h=15 order-zero outer chamber
combined endpoint result: all five m in {8,16} next-to-maximal order-zero
                          HNF chambers are closed
critical delta: none; l1_mixed_petal_amplification remains TARGET
remaining first-checkpoint scope: order one, lower value degrees,
                                  nonembedded m=4,h=2, and inner lifts
primary: ap-TFttWNnwIi68tCQ3n32vBn, 16.746444 s, 110 MB
audit:   ap-myN6sycfDSBAi2okj8hc2P, 12.792499 s, 110 MB
compute spend: exact bill not queried; conservative whole-campaign bound
               below $0.05
new assumptions: none
compute request: CR-L1-MCP-NMCE narrowed to order one only
next route-deciding action: attack the bounded order-one torsion systems, or
                              switch if their first exact chamber is not cheap
```

**2026-07-27, order-one involution component deleted:** a 1-CPU exact
factorization probe found that after the already-saturated factors, both
official hypergeometric curves contain `c+1`. This is structural:
at `c=-1` the generating series is `(1-t^2)^(-rho)`, so every odd top
coefficient vanishes. The separate torsion condition then kills the complete
component. Indeed `(c-1)^n=2^n=1` would force the odd prime order
`q in {13,17,19,31}` of `2 mod (2^q-1)` to divide the power-of-two `n`.

```text
node proved: l1_mersenne_hnf_order_one_involution_component_exclusion
result: CLOSED, c=-1 component on all five next-to-maximal rows
residual h=7 curve:  deg_(rho,c)=(2,4), 10 terms
residual h=15 curve: deg_(rho,c)=(6,12), 64 terms
critical delta: none; l1_mixed_petal_amplification remains TARGET
Modal: ap-HLlQUd2eURywjmrrMr2EeV, 0.688987 s, 88 MB
compute spend: exact bill not queried; conservative bound below $0.01
route rule: saturate by c+1 and never recompute the involution component
next action: derive the first reciprocal equations on Psi_7=0 and price one
             exact m=8 order-one elimination before any full saturation
```

**2026-07-27, order-one resultant route retired and replaced:** the exact
SymPy profile campaign consumed 315 aggregate app seconds. After two
representation corrections, the normalized degree-six quotient had the
expected denominator `(c-1)^6`, 77 numerator terms, and total degree 12,
but `Res_W(L,Z-W^8)` still hit the final 180-second timeout. No reciprocal
equation completed and there is no mathematical verdict. The campaign cap
is exhausted; no Singular retry is authorized on the current account.

The algebra itself removes the bottleneck. If `x_i` are the reduced roots,
the `j`th reciprocal equation is exactly

```text
e_j((x_i^star)^m)=e_j(x_i^(-m)).
```

Newton identities construct the first three equations from traces only
through `m,2m,3m`; the `H-1` interior equations plus the constant-product
equation recover the full reciprocal identity. This is proved independently of the failed
profile.

```text
node proved: l1_mersenne_hnf_order_one_newton_reciprocal_reduction
route cut: generic mth-power resultant retired as the primary construction
critical delta: none; l1_mixed_petal_amplification remains TARGET
failed apps: ap-2JqEoR1tUWnWY1uaGIpxzh,
             ap-0Zf035x3KMj8qBJ7V8FtBT,
             ap-UxUdP4JCXNMzidTip4FogP
campaign: 315 aggregate app seconds; conservative cost below $0.10
next action: exact trace/Newton elimination on Psi_7=0, preferably by an
             external contributor or a future separately capped campaign
```

**2026-07-27, N=256 variance-68 reduced to three exact profiles:** the common
nested-layer compiler and one coupled inner-support census close every
`E=34` magnitude profile except three equality cases. This replaces the
earlier six-profile route boundary without promoting the universal unsafe
target.

```text
starting pins: local ad97cb69; canonical dd76658c;
               upstream origin/main b13de811
ending proof pin: local e207280f
canonical reconciliation: canonical 7f54beaa integrated at local 9b6393c9
node attacked: unsafe_crossing_family_instantiation, N=256 (3,4,0), V=68
result: NARROWED; every pair-feasible collision now has profile
        (6,7), (9,4,1), or (12,1,2), and all three have L=20
exact closures: 18 abstract profiles have M_3<=1940; profiles (5,5,1)
                and (14,1,0,1) have quotient caps <=1922; profile (2,8)
                has coupled cap <=1942 and inner-4Z support cap 1536
threshold: every excluded profile has M_3<=1942<1947
DAG delta: one PROVED background node and six edges; critical status unchanged
critical census after reconciliation: 179 PROVED / 38 CONDITIONAL / 24 TARGET
compute: ap-Ec22WlisgFjRNPFuigxlEy, ap-zx5C3lSHLdaYAZE2Ic0tZA,
         ap-8xzV3fZniv8jms4V2EI19N; 71 seconds aggregate client wall;
         conservative combined campaign cost below $0.45
new assumptions: none
upstream overlap: no open PR supplies this E34 signed-chord classification;
                  #1107-#1109 remain the nearest live field/WCL packets
route decision: no broader support enumeration or Modal run; first classify
                the 41 exact L=20 relaxed signed-chord signatures and use
                E=102-D_64+2C, which already sharpens C<=-22 to C<=-24
next route-deciding action: filter those signatures against the three residual
                              profiles and prove a chord-origin exclusion or
                              isolate a finite realizable survivor family
```

**2026-07-27, E34 parity collapse and light-Sidon pin:** integer parity of the
signed chord formula removes two of the three quotient survivors without a
new computation.

```text
starting pin: local 23d41df7
ending proof pin: local ad8d994a
node attacked: unsafe_crossing_family_instantiation, N=256 (3,4,0), V=68
result: NARROWED; sole magnitude profile (6,7), with L=20
structural delta: the six unit-product chords occupy six distinct
                  non-diameter classes; the four light positions are
                  circular Sidon for unoriented differences modulo 128
signed ledger: D_64 in {0,4,8,12,16,20} and
               C=-34+D_64/2 in {-34,-32,-30,-28,-26,-24}
DAG delta: one PROVED background node and four edges; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
compute spend: none; exact parity and matching arithmetic only
new assumptions: none
route decision: the 41 signatures are not three independent profile sieges;
                they are heavy-chord collision patterns around one light-Sidon
                support. Classify that smaller object before any support search.
next route-deciding action: quotient the 41 signatures by the six diameter
                              ledgers and identify the forced heavy-light or
                              heavy-heavy progression/parallelogram templates
```

**2026-07-27, E34 heavy-template split and quarter close:** the magnitude-four
chords force a four-case additive template split. The bounded quarter case is
then paid by two independent complete exact censuses.

```text
starting pin: local d31d98b3
template proof pin: local 49f79efb
ending proof pin: local 9888a619
node attacked: unsafe_crossing_family_instantiation, N=256 (3,4,0), V=68
result: NARROWED; quarter template CLOSED, three heavy templates remain
template theorem: quarter / nonquarter diameter / progression / generic;
                  every singleton non-diameter heavy-heavy class contains a
                  heavy-light chord; quarter D_64=20 is algebraically empty
quarter census: 9,381,251 supports and 300,200,032 signed vectors;
                1,031,680 full-conductor profile-(6,7) candidates;
                exact maximum M_3=1188<1947
independent apps: ap-kLTKBwJM3lNWUZA3hul5w7 (45.781851 worker-seconds),
                  ap-XXTZkD7kcupvXULmbp2GKZ (52.691880 worker-seconds)
DAG delta: two PROVED background nodes; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
compute spend: conservative combined ceiling below $0.15; no further run
new assumptions: none
route decision: do not enumerate arbitrary seven-point supports. Attack the
                nonquarter diameter template next because it has a fixed
                antipodal heavy pair and exactly two forced heavy-light welds.
next route-deciding action: normalize that antipodal pair, classify its third
                              heavy orbit and weld choices, then decide whether
                              an analytic cap or another bounded exact census
                              closes the branch
```

**2026-07-27, E34 nonquarter-diameter weld reduction:** the next heavy
template is reduced to 31 exact normal forms and one five-position support
condition without computation.

```text
starting pin: local 2bb5265f
proof pin: local 6ce23319
node attacked: unsafe_crossing_family_instantiation, N=256 (3,4,0), V=68
result: NARROWED; nonquarter-diameter branch normalized exactly
normal forms: H={0,64,t}, 1<=t<=31
weld condition: one of {64-t,64+t,128-t} is light, or both
                {2t,64+2t} are light
exact chamber: 915,125 light supports per t; 1,815,608,000 signed vectors
DAG delta: one PROVED background node and four edges; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
compute spend: none; elementary orbit and inclusion-exclusion proof
new assumptions: none
upstream overlap: no open PR supplies this finite E34 signed-weld normal form
route decision: the chamber is six times the quarter search but has the same
                exact low-support metric and a natural 31-shard partition
next route-deciding action: run a separately capped exact profile-and-moment
                              census only if a verifier-scale pilot confirms
                              the branch remains below the sub-dollar budget
```

**2026-07-27, E34 nonquarter-diameter close:** two independent complete
implementations close the second heavy template well below the cubic
threshold.

```text
starting pin: local 831fa2dc
proof pin: local df102559
node attacked: unsafe_crossing_family_instantiation, N=256 (3,4,0), V=68
result: CLOSED nonquarter-diameter branch; progression and generic remain
exact census: 28,368,875 supports; 1,815,608,000 signed vectors;
              899,456 full-conductor profile-(6,7) candidates
moment cap: exact maximum M_3=1560<1947, margin 387
independent apps: ap-EfGZditRQm7eDLLLWpNiSA (271.301709 worker-seconds),
                  ap-MQpKibQl8PBqzuhB5DKf2m (339.920267 worker-seconds)
DAG delta: one PROVED exclusion node and six edges; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
compute spend: 611.221976 worker-seconds; conservative ceiling below $0.90
new assumptions: none
upstream overlap: no open PR supplies this finite E34 signed-chord close
route decision: do not broaden the diameter census; it is complete
next route-deciding action: normalize the progression template, split its
                              outer-sign cases, and seek a comparably exact
                              weld chamber before considering computation
```

**2026-07-27, E34 progression orbit reduction:** repeated-class arithmetic
forces opposite outer signs, and cyclotomic unit transport reduces 62 heavy
forms to five invariant representatives.

```text
starting pin: local d8573a35
proof pin: local fb1aa985
node attacked: unsafe_crossing_family_instantiation, N=256 (3,4,0), V=68
result: NARROWED progression branch; generic remains untouched
normal forms: H={0,t,2t}, 1<=t<=63, t!=32; outer heavy signs opposite
weld condition: L meets {-2t,3t,-t,4t}
raw chamber: 1,195,965 supports per form; 2,372,794,560 signed vectors
unit-orbit chamber: representatives t=1,2,4,8,16; 191,354,400 vectors
DAG delta: one PROVED background node and four edges; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
compute spend: none; exact chord arithmetic and unit-orbit proof
new assumptions: none
upstream overlap: no open PR supplies this finite cyclotomic progression close
route decision: the five-form chamber is cheaper than the completed quarter
                census and is the next route-deciding computation
next route-deciding action: build two independent five-shard exact censuses
                              with a conservative sub-dollar cap; close the
                              branch if maximum M_3<=1947
```

**2026-07-27, E34 progression close:** the five unit-orbit representatives
close the third heavy template, leaving only generic at variance 68.

```text
starting pin: local 7b55c261
proof pin: local 5cafbad0
node attacked: unsafe_crossing_family_instantiation, N=256 (3,4,0), V=68
result: CLOSED progression branch; generic is the sole E34 template
representative census: 5,979,825 supports; 191,354,400 signed vectors;
                       329,776 full-conductor profile candidates
weighted 62-form count: 3,131,008 full-conductor profile candidates
moment cap: exact maximum M_3=1722<1947, margin 225
independent apps: ap-i5ZUL3DXjsMVeoSd2KwzT4 (29.943997 worker-seconds),
                  ap-x6NGO4WBkgu0GbaGBpeQim (50.977832 worker-seconds)
DAG delta: one PROVED exclusion node and six edges; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
compute spend: 80.921829 worker-seconds; conservative ceiling below $0.20
new assumptions: none
upstream overlap: no open PR supplies this finite E34 progression close
route decision: do not enumerate all generic supports; first quotient generic
                heavy triples and classify three simultaneous weld sets
next route-deciding action: derive a generic heavy normal form under affine
                              and odd-unit symmetries, including exact weld
                              intersections and sign constraints
```

**2026-07-27, E34 generic affine-weld reduction:** two independent orbit
classifiers reduce the last heavy template to 57 representatives and three
exact weld shapes.

```text
starting pin: local cbf1260e
proof pin: local 06a4294e
node attacked: unsafe_crossing_family_instantiation, N=256 (3,4,0), V=68
result: NARROWED generic branch; it is now the sole E34 template
orbit census: 325,376 heavy triples -> 57 affine odd-unit representatives
weld shapes: 52 regular rows, four [0,2^v,3*2^v] rows, one terminal v=4 row;
             no triple intersection
exact chamber: 243,285,056 normalized signed vectors
DAG delta: one PROVED background node and four edges; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
compute spend: ap-RX2pnnmJRiFhsRSBEJS6To; 1.110289 worker-seconds;
               conservative ceiling below $0.05
new assumptions: none
upstream overlap: no open PR supplies this finite generic weld classifier
route decision: the final chamber is comparable to the closed quarter branch
                and small enough for a bounded independent decision
next route-deciding action: build two exact 57-shard profile-and-moment
                              censuses under a conservative sub-dollar cap;
                              close E34 if maximum M_3<=1947
```

**2026-07-27, E34 endpoint close:** the final generic census closes all four
heavy templates and advances the `(3,4,0)` variance frontier from 68 to 66.

```text
starting pin: local b4613976
proof pin: local 196de799
node attacked: unsafe_crossing_family_instantiation, N=256 (3,4,0), V=68
result: CLOSED complete E34 endpoint; residual positive even V<=66
generic census: 3,801,329 supports; 243,285,056 signed vectors;
                418,464 full-conductor profile candidates
moment cap: exact maximum M_3=1770<1947, margin 177
independent apps: ap-XpmKEOhClEfy8STvFbMH9y (34.471246 worker-seconds),
                  ap-GUW2NuOkVnhQDU4jUvepbZ (50.538048 worker-seconds)
synthesis: three profiles -> one parity profile -> four templates -> empty
DAG delta: two PROVED nodes (generic exclusion and endpoint synthesis),
           fifteen requirement/evidence edges; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
compute spend: 85.009294 worker-seconds; conservative ceiling below $0.20
new assumptions: none
upstream overlap: no open PR supplies this finite E34 endpoint close
route decision: E34 is complete; do not rerun any E34 campaign
next route-deciding action: derive the exact V=66 integer-profile and parity
                              ledger, then decide whether the E34 template
                              machinery transports or must be replaced
```

**2026-07-27, V=66 profile/parity/diameter reduction:** exact arithmetic
reduces the next endpoint to four profiles and five diameter ledgers.

```text
starting pin: local 75be5956
proof pin: local 4ee12f2b
node attacked: unsafe_crossing_family_instantiation, N=256 (3,4,0), V=66
result: NARROWED from 21 integer profiles to four exact profiles
slack: L<=19; boundary minimum-energy trace 53,49,45,41,37,33
cubic: exact threshold M_3=1732 (positive at 1732, negative at 1733)
parity survivors: (5,7), (1,8), (4,5,1), (0,6,1)
diameter: exactly one light-light edge;
          D_64 in {1,5,9,17,21}, C=(D_64-69)/2
independent replay: Cartesian and recursive profile censuses; independently
                    solved rational Hermite system; complete matching census
DAG delta: one PROVED background node and six edges; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
compute spend: none; all checks verifier-scale under the 256 MiB RAM guard
new assumptions: none
upstream overlap: no open PR through #1109 supplies this finite E1 reduction
route decision: do not transport the E34 four-template split wholesale;
                attack (0,6,1), whose cap 1782 is only 50 above threshold
next route-deciding action: derive the exact b=2*1_A+1_T moment ledger for
                              nested sizes (14,14,2), exploit T={+/-t} and
                              quotient/parity constraints, and authorize a
                              bounded census only if the analytic gap remains
```

**2026-07-27, V=66 profile `(0,6,1)` close:** a sharp symmetric
target-fiber theorem removes the nearest cubic branch without a census.

```text
starting pin: local 487d1450
proof pin: local 3fa13674
node attacked: unsafe_crossing_family_instantiation, V=66 profile (0,6,1)
result: CLOSED one of four V=66 profiles; three remain
exact ledger: b=2*1_A+1_T, |A|=14, T={+/-t}
new theorem: for A=-A subset Z/128Z\{0,64} and z in A,
             r_A(z)<=|A|-2
moment: 8*R(A,A,A)+12*R(A,A,T)+6*R(A,T,T)<=1644<1732
sharpness: attained by the abstract order-16 subgroup minus {0,64}
independent replay: all 6,435 symmetric 14-subsets of Z/32Z; exact maxima
                    R=168, target fiber=12, weighted moment=1644
DAG delta: one PROVED background node and five edges; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
compute spend: none; finite audit completed under the 256 MiB RAM guard
new assumptions: none
upstream overlap: no open PR through #1109 supplies this finite E1 close
route decision: the target-fiber bound is sharp at abstract-set scope; do not
                spend effort trying to improve it without autocorrelation data
next route-deciding action: attack (4,5,1), using its five-odd
                              diameter-Sidon support and unique magnitude-three
                              class before any bounded exact census
```

**2026-07-27, V=66 profile `(4,5,1)` close:** the deterministic quotient
compiler reaches the exact cubic boundary and removes a second profile.

```text
starting pin: local 71d6dbc2
proof pin: local 35740f83
node attacked: unsafe_crossing_family_instantiation, V=66 profile (4,5,1)
result: CLOSED second of four V=66 profiles; two remain
layers: exact nested sizes (20,12,2)
order-128 census: 5,421,301 allocations, exact maximum M_3=1732
order-64 census:  3,086,861 allocations, exact maximum M_3=1670
outer-4Z close: L=17 gives nonzero degree-32 norm <=50^32<2^250
independent replay: Python objective reconstruction and allocation DP;
                    seven-shard repartition agrees with sixteen-shard primary
production/replay apps: ap-XlApOnmQmoX3P5Gd6qsVXb,
                        ap-BnCaKbLKE6f99c19iKJ1D5
DAG delta: one PROVED background node and five edges; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
compute spend: bounded route probes plus exact census, conservative total
               below $0.30; no further run authorized
new assumptions: none
upstream overlap: no open PR through #1109 supplies this finite E1 close
route decision: quotient allocation is sufficient at equality; no chord-origin
                census is needed for (4,5,1)
next route-deciding action: run the same exact quotient compiler for (1,8);
                              reserve heavy/light geometry for (5,7) if needed
```

**2026-07-27, V=66 profile `(1,8)` close:** the quotient relaxation fails,
but an exact one-odd light-support classification reduces the actual geometry
to eleven affine-unit templates and closes the third profile.

```text
starting pin: local f4af4606
proof pin: local 07398f4b
node attacked: unsafe_crossing_family_instantiation, V=66 profile (1,8)
result: CLOSED third of four V=66 profiles; only (5,7) remains
bare quotient obstruction: exact maximum 1936>1732 in both quotient orders
coupled quotient obstruction: maxima 2028 (order 128), 1740 (order 64)
classification catch: the initial six-orbit draft omitted {0,1,63,64};
                      independent checker repaired two reflection families
light geometry: 132 normalized supports -> eleven affine-unit orbits
exact census: 11*binom(124,3)*64=218,327,296 normalized signed vectors;
              17,144 profile vectors; exact maximum M_3=1356<1732
independent replay: signed folded-chord and ordered-negacyclic-product engines;
                    identical per-template profile counts and maxima
hostile controls: omitted reflection family, omitted shard, and 1355 maximum
production app: ap-TbM5Ao0mujKzSnl3E7cFL5; 26.636356 worker-seconds
DAG delta: one PROVED background node and four edges; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
compute spend: four cents-scale route probes and one exact campaign;
               conservative total below $0.10
new assumptions: none
upstream overlap: no open PR through #1109 supplies this finite E1 close
route decision: quotient allocation has reached its limit; the actual chord
                geometry is decisive at V=66
next route-deciding action: attack sole profile (5,7), using its five-odd
                              diameter-Sidon condition before authorizing any
                              further complete signed-vector campaign
```

**2026-07-27, V=66 endpoint close:** the final diameter-Sidon profile closes
after an exact conductor split, completing the whole variance-66 endpoint.

```text
starting pin: local d8175531
proof pin: local c87e1991
node attacked: unsafe_crossing_family_instantiation, V=66 profile (5,7)
result: CLOSED final V=66 profile and complete E33 endpoint;
        residual positive even variance V<=64
light geometry: 7,200 normalized diameter-Sidon supports -> 100 affine-unit
                orbits under z -> uz+t, u odd, t in {0,64}
exact coverage: 100*binom(124,3)*64=1,984,793,600 normalized signed vectors
profile ledger: 28,048 profile-(5,7) vectors; 17,768 full-conductor vectors
near-counterexample: unrestricted maximum M_3=1758>1732 at support
                     (36,48,60,0,4,24,64), exact conductor 4
live bound: exact full-conductor maximum M_3=1416<1732, margin 316
conductor router: e1_n256_proper_conductor_collision_exclusion removes every
                  gcd-greater-than-one support, including the maximizer
independent apps: ap-GpozWWr9n5UCGVYAn4Ydl8 (signed folded chords,
                  238.629139 worker-seconds), ap-Q31nLvELxLsAfXipcD01L5
                  (ordered negacyclic product, 382.736139 worker-seconds)
independent agreement: every one of 100 template counts and maxima agrees
DAG delta: two PROVED nodes (profile exclusion and endpoint synthesis),
           twelve requirement/evidence edges; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
compute spend: 621.365278 aggregate worker-seconds; conservative total below
               $0.10, no further V=66 campaign authorized
new assumptions: none
upstream overlap: no open PR through #1109 supplies this finite E1 close
route decision: E33 is complete; do not rerun any V=66 campaign
next route-deciding action: return to unsafe_crossing_family_instantiation's
                              remaining bands/profiles and select the next
                              exact endpoint or upstream-bankable shared leaf
```

**2026-07-27, V=64 algebraic reduction:** the next variance endpoint now has
three exact residual profiles, with no broad computation required.

```text
starting pin: local 22079669
proof pin: local cd1b5957
node attacked: unsafe_crossing_family_instantiation, V=64 algebraic front end
result: PROVED reduction; profiles (4,7), (0,8), (3,5,1) remain
slack ledger: L<=18 from the exact Delta=2,6,...,26 recurrence
profile ledger: 18 integer profiles; seven above the abstract cubic cutoff
cubic certificate: exact M_3 threshold 1517; opposite signs at 1517/1518
parity close: four high profiles have 8 or 12 odd coefficients, exceeding
              the six available non-diameter unit chords
diameter ledger: zero or two light-light diameters;
                 D_64 in {0,2,4,8,12,16,18,20}
independent replay: Cartesian and recursive profile enumerators; direct and
                    Gaussian-elimination Hermite reconstruction; analytic and
                    complete labeled-matching diameter enumeration
hostile controls: removing the six-unit gate restores all four deleted profiles
compute spend: verifier-scale local integer arithmetic only; no Modal run
DAG delta: one PROVED node and six edges; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
scope audit: repaired stale auto-discharge prose in
             e1_official_prime_exception_control; its route-uniform TARGET
             status and every-row obligation are unchanged
new assumptions: none
route decision: V=64 is materially narrower than profile (4,2,0)
next route-deciding action: run a bounded quotient relaxation for (3,5,1);
                              stop immediately if its cap exceeds 1517
```

**2026-07-27, V=64 profile `(0,8)` close and quotient route cut:** the first
profile is empty, while the basic quotient compiler is decisively retired for
`(3,5,1)`.

```text
starting pin: local fc905690
proof pin: local 122de20c
node attacked: unsafe_crossing_family_instantiation, V=64 profiles
quotient probe: profile (3,5,1), exact maxima 1610 (order 128) and
                1594 (order 64), both above threshold 1517
quotient coverage: 1,828,183 and 1,165,828 complete allocations
route witnesses: compact maximizing allocations replay both objectives locally;
                 they are relaxation witnesses, not actual collisions
profile closed: (0,8), first of three V=64 profiles
light classification: 333,375 normalized supports checked; exactly 63 pass
                      zero-odd parity, all two antipodal pairs
affine-unit router: {0,64,t,64+t}, t in {1,2,4,8,16,32}
exact coverage: 6*binom(124,3)*64=119,087,616 normalized signed vectors
production app: ap-Q9Gv4Od8ny1Ixkcb8ej0Q9, folded-chord engine,
                14.231192 aggregate worker-seconds
audit app: ap-kKHuq4icz9mhgKv7qJJsD5, direct negacyclic-product engine,
           22.741897 aggregate worker-seconds
independent agreement: zero profile-(0,8) vectors in every template
hostile controls: missing shard, missing t=32 orbit, and nonzero packet count
compute spend: quotient probe plus 36.973089 census worker-seconds;
               conservative cost below $0.10
DAG delta: one PROVED node and three edges; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
new assumptions: none
live V=64 residual: (4,7), (3,5,1)
route decision: both survivors have four odd autocorrelation coefficients and
                should share one zero/two-diameter light-support router
next route-deciding action: classify that common light-support orbit space
                              before authorizing either signed-vector census
```

**2026-07-27, V=64 common four-odd light router:** both surviving profiles now
share one exact finite geometry chamber.

```text
starting pin: local e2a5fab2
proof pin: local 7b44cea1
node attacked: V=64 profiles (4,7) and (3,5,1), common light geometry
normalized classification: 28,800 of 333,375 four-light supports
diameter result: every valid support has zero light-light diameters
distance ledger: multiplicities 2,1,1,1,1
shape result: the repeated edges always share a vertex; every support contains
              a light three-term progression; no repeated matching survives
affine router: 148 odd-unit/translation orbits
orbit sizes: 32 (4 orbits), 64 (16), 128 (40), 256 (88)
independent replay: vertex triples versus positive circular gaps; expanded
                    printed orbits are disjoint and cover all 28,800 supports
diameter ledger: D_64 in {0,4,8,12,16,20}
compute spend: verifier-scale local classification only; no Modal run
DAG delta: one PROVED node and three edges; critical status unchanged
critical census: 179 PROVED / 38 CONDITIONAL / 24 TARGET
new assumptions: none
route decision: form each signed autocorrelation once and apply both live
                profile filters in one 148-template representative census
next route-deciding action: joint Modal census with unrestricted and
                              full-conductor maxima, followed by independent
                              direct-negacyclic replay if closure is indicated
```

**2026-07-27, V=64 joint census and profile `(3,5,1)` close:** the common
router pays one branch outright and isolates the exact norm gap in the last
profile.

```text
starting pin: local fcd52e30
node attacked: V=64 profiles (4,7) and (3,5,1), shared actual geometry
production coverage: 148*binom(124,3)*64=2,937,494,528 representative vectors
production app: ap-DuxqODKmBVrz1XwQGhui61, folded-chord engine
audit app: ap-RjKrdoGVLkBnsZLmm9Loeu, direct negacyclic-product engine
independent agreement: all 148 per-template counts, conductor splits, maxima
profile (3,5,1): 29,238 vectors; 15,440 full conductor;
                     exact unrestricted/full maximum M_3=1392<1517; CLOSED
profile (4,7): 87,818 vectors; 60,148 full conductor;
                 unrestricted maximum 1584; full-conductor maximum 1524
extremizer audit: exact resultant bit lengths 240 (proper) and 239 (full),
                  both below 2^250; over-cutoff M_3 is not a counterexample
route catch: the quotient relaxation failed for (3,5,1), but actual chord
             geometry lowers its exact maximum by 125 below the cutoff
compute spend: two 148-task one-core campaigns plus three resultants;
               conservative cost below $0.10
new assumptions: none
live V=64 residual: (4,7) only
route decision: the cubic-Hermite certificate is seven units too weak on the
                exact full-conductor maximum, while actual extremal norms pass
next route-deciding action: sharpen the finite 60,148-vector norm ledger by
                              exact resultants or a higher-moment majorant;
                              do not rerun the geometry census
```

**2026-07-27, profile `(4,7)` and V=64 endpoint close:** two independent exact
resultant ledgers pay the non-sharp cubic tail and finish the endpoint.

```text
node attacked: final V=64 profile (4,7)
pilot coverage: templates 59,35,139; 1,500 full-conductor resultants;
                both backends agree, maximum 246 bits, aggregate worker time
                7.36 seconds (FLINT) and 14.19 seconds (PARI)
full coverage: all 148 templates and 2,937,494,528 representative vectors
retained ledger: 60,148 full-conductor profile-(4,7) vectors
production app: ap-wUY2sEVOlPTj95cuuaJhkT, folded chords + Python FLINT,
                377.786140 aggregate worker-seconds
audit app: ap-b1DkMwYxO1Wt886rrpSVYT, direct negacyclic product + PARI/GP,
           631.679933 aggregate worker-seconds
exact maximum: 119477984433218714943829098200259691143739376720677525742811917286342611458
maximizing vector: positions (5,7,9,0,1,2,12),
                   coefficients (2,-2,-2,1,1,1,1)
strict margin: 15*N_max < 2^250 < 16*N_max; maximum bit length 247
proper conductor: discharged by e1_n256_proper_conductor_collision_exclusion
endpoint synthesis: profiles (0,8), (3,5,1), and (4,7) all PROVED impossible
result: V=64 CLOSED; live positive even variance frontier V<=62
compute spend: 1009.466073 aggregate full-run worker-seconds plus pilots;
               conservative cost remains below $0.10
new assumptions: none
route decision: exact finite norms are materially sharper than the cubic
                majorant at M_3=1524; do not rerun any V>=64 campaign
next route-deciding action: start V=62 (E=31) with exact algebraic profile,
                              slack, parity, and diameter reduction before any
                              new census; compare against the (4,2,0) lane
```

**2026-07-27, V=62 algebraic reduction and endpoint close:** the odd-parity
geometry collapses the next chamber to eight templates, and two inexpensive
independent censuses pay all three residual profiles.

```text
starting pin: local 05f66d4d
node attacked: N=256, folded profile (3,4,0), V=62 (E=31)
slack result: L<=17; exactly 15 energy profiles
exact cubic cutoff: M_3=1302
parity survivors: (3,7), (2,5,1), (1,3,2)
light router: 960 normalized supports in eight affine odd-unit orbits
templates: {0,t,2t,64}, {0,t,32,64}, t in {1,2,4,8}
geometry: one light diameter; non-diameter multiplicities 2,1,1,1;
          repeated edges form a wedge
production app: ap-QVT4zR1b0UV4Z3QVYzLo4B, folded-chord engine
audit app: ap-09HiyZJzn23MDKtzPjXS1M, direct negacyclic-product engine
coverage per engine: 8*binom(124,3)*64=158,783,488 representative vectors
independent agreement: all eight row counts, conductor splits, and maxima
profile (3,7): 7,204 vectors; 3,856 full conductor;
                 unrestricted max M_3=1380; full max M_3=1206<1302
profile (2,5,1): 1,590 vectors; unrestricted max M_3=1068<1302
profile (1,3,2): 388 vectors; unrestricted max M_3=1122<1302
proper conductor: the 3,348-vector complement of full-conductor (3,7) is
                  discharged by the existing conductor theorem
endpoint synthesis: all three profiles PROVED impossible
result: V=62 CLOSED; live positive even variance frontier V<=60
compute spend: 21.161992 production plus 31.049432 audit aggregate
               worker-seconds, eight 256 MiB workers per campaign
DAG delta: three PROVED nodes; critical orbit census unchanged because these
           are evidence suppliers, not new required leaves
critical census: math 241 (179/38/24), submission 256 (191/40/25)
new assumptions: none
route decision: begin V=60 (E=30) algebraically; do not extrapolate the cubic
                endpoint descent without first proving a comparably small
                template router, and compare value against the (4,2,0) lane
```

**2026-07-27, V=60 reduction and five-profile close:** exact parity and
quotient routing close three profiles, while a complete two-odd census and
exact resultant ledger close two more. The endpoint remains open on a
three-profile six-odd branch.

```text
starting pin: local ffd030fa
node attacked: N=256, folded profile (3,4,0), V=60 (E=30)
slack result: L<=18; exactly 18 energy profiles
exact cubic cutoff: M_3=1087
parity survivors: (6,6), (2,7), (5,4,1), (1,5,1), (4,2,2), (0,3,2),
                  (6,2,0,1), (3,0,3)
light split: two odd classes for (2,7),(1,5,1); six odd classes otherwise
two-odd geometry: 8,168 normalized supports in 87 affine odd-unit orbits
six-odd geometry: 280,720 normalized supports; every light chord distinct
six-odd census fence: at least 1,097 affine orbits and
                      21,773,185,792 representative signed vectors
quotient app: ap-6rqImRUb2uMS1GmFe1rVMT; 128 complete tasks;
              106.631016 aggregate worker-seconds
discarded launch: ap-Y3PyxbL9jWc8vSqM0zXKQe completed zero tasks and emitted
                  an explicit incomplete packet; it is not evidence
quotient closures: (0,3,2) maxima 936/936;
                   (6,2,0,1) maxima 1058/1048;
                   (3,0,3) maxima 1002/940, all below 1087
two-odd production: ap-kByaSsYhxYgKb4TJqkEuLT, folded chords,
                    219.666239 aggregate worker-seconds
two-odd audit: ap-FqluYkBc3DLz687GeYxBgp, direct negacyclic product,
               331.165567 aggregate worker-seconds
coverage per engine: 87*binom(124,3)*64=1,726,770,432 vectors
profile (1,5,1): 7,722 vectors; 3,572 full conductor;
                   full-conductor max M_3=1068<1087
profile (2,7): 44,302 vectors; 28,114 full conductor;
                 cubic max 1320, requiring exact norms
norm production: ap-iEm8zqbRcOWdVO9qSVwi4o, folded chords + FLINT,
                 217.814119 aggregate worker-seconds
norm audit: ap-pBUnRmFuHfemCN6jBFUmG6, direct negacyclic + PARI/GP,
            340.729671 aggregate worker-seconds
exact maximum: 255193811126065252065353356643030254729479452452701245894186298519499407392
maximizing vector: positions (7,39,103,0,1,20,109),
                   coefficients (2,-2,-2,-1,1,1,1)
strict margin: 7*N_max<2^250<8*N_max; zero norms at or above 2^250
proper conductor: both complementary two-odd branches discharged by the
                  existing conductor theorem
closed profiles: (0,3,2), (6,2,0,1), (3,0,3), (2,7), (1,5,1)
live V=60 residual: (6,6), (5,4,1), (4,2,2), all six odd
aggregate successful compute: 1216.006612 worker-seconds
new assumptions: none
route decision: do not descend to V=58 and do not run the direct six-odd
                census. Seek a stronger moment inequality, additive
                six-light structure, or a norm factorization that treats the
                three residual profiles simultaneously.
```

**2026-07-27, profile `(4,2,2)` structured close:** conditioning the cubic
moment on the six light differences replaces the 21.77-billion-vector route
by a 1,234-mask relaxation and six-vector exceptional ledger.

```text
node attacked: N=256, V=60 profile (4,2,2)
odd-set identity: b = 1_O + 2*1_(P union E), where O is the symmetric
                  six-difference set of the four light positions,
                  |P/+-|=2 inside O, |E/+-|=2 outside O
normalized light supports: 280,720
distinct odd masks modulo odd units: 1,234
relaxation assignments: 1234*binom(6,2)*binom(57,2)=29,541,960
production relaxation: ap-tvZbcv7UZUzrmCYpkGAOTG,
                       direct cyclic-convolution expansion,
                       7.487322 aggregate worker-seconds
audit relaxation: ap-dJMmIFzqO9ccMXj6V7w4EQ,
                  positive circular gaps + signed-triple kernel,
                  1.929715 aggregate worker-seconds
independent agreement: every shard, mask count, assignment count, maximum,
                       histogram, and exceptional pattern
relaxation maximum: M_3=1146; exactly three assignments exceed 1087
exceptional primitive light support: {0,1,6,8}
exceptional layers: odd {1,2,5,6,7,8}, magnitude-three {1,2},
                    magnitude-two {3,4}; other two are dilates by 2 and 4
actual-vector app: ap-6dp2yFFRypuGUw2Xs9tKcD
actual coverage per engine: 3*binom(124,3)*64=59,543,808 vectors
actual engines: folded unordered chords and direct negacyclic product
actual survivors: two per exceptional orbit; conductor split 2,0,0
proper conductor: the four scale-two/scale-four vectors are excluded
primitive vectors: F_1=1+x+2x^2+2x^3-2x^4+x^6-x^8,
                   F_2=F_1(-x)
norm app: ap-z7K1Nn5YhdCDPYES6pvGLd, FLINT and PARI/GP
common exact norm: 4039047355553663302249733085042470588482730556495866201164489362016333826
strict margin: 447*N_max<2^250<448*N_max; bit length 242
result: profile (4,2,2) CLOSED
live V=60 residual: (6,6), (5,4,1), both six odd
successful census compute: 20.626053 aggregate worker-seconds plus two
                           negligible exact resultants
discarded launch: ap-IQ6rztTj4LeLC4wg1DSGgC failed during audit-source
                  compilation and ran zero numerical tasks
new assumptions: none
route decision: extend the odd-mask method to (6,6) and (5,4,1), but replace
                raw choices of six or four even classes by branch-and-bound,
                an exact optimizer, or a provable additive upper bound. Do
                not run either direct vector census and do not descend to
                V=58.
```

**2026-07-27, profile `(5,4,1)` structured close:** an exact cubic optimizer
over the even layer reduces 2.924 billion abstract assignments to 321 light
orbits, after which two independent actual-vector engines and two independent
resultant engines close the profile.

```text
node attacked: N=256, V=60 profile (5,4,1)
odd-set identity: b = 1_O + 2*1_(P union E), where O is the symmetric
                  six-difference set of the four light positions,
                  |P/+-|=1 inside O, |E/+-|=4 outside O
normalized six-odd supports: 280,720
distinct odd masks modulo odd units: 1,234; exactly one affine light-support
                                      orbit per mask
orbit-atlas app: ap-gydIct2AQV7tjgwU9nH0Xb; 1.620819 aggregate worker-seconds
relaxation assignments: 1234*6*binom(57,4)=2,924,654,040
production relaxation: ap-xt8CzSXbM9zdtJ7QFkPsou,
                       40.135081 aggregate worker-seconds
audit relaxation: ap-ek9XQdOs4gck36Cji9TX9h,
                  40.844229 aggregate worker-seconds
independent agreement: all 64 shards, 1,456 above-cutoff assignments,
                       321 exceptional light orbits, maximum M_3=1278
production actual census: ap-Rib373enlZ4XZYrLYvi353,
                          810.405329 aggregate worker-seconds
audit actual census: ap-qotcG4Gq0XxspTOe5jWxhZ,
                     1193.826166 aggregate worker-seconds
actual coverage per engine: 321*binom(124,3)*64=6,371,187,456 vectors
independent actual agreement: 45,846 profile vectors; 440 above cutoff;
                              86 full conductor; maximum M_3=1278
proper conductor: the complementary 354 vectors are excluded by the existing
                  conductor theorem
norm app: ap-ac61MPIVeEN9CWlcxSt4Zf; FLINT and PARI/GP agree on all 86 vectors
distinct norms: 42
exact maximum: 147314768947604483837877250659211387932426327951806688176613401078756416516
strict margin: 12*N_max<2^250<13*N_max; bit length 247
result: profile (5,4,1) CLOSED
live V=60 residual: (6,6) only
new assumptions: none
route decision: solve the six-even-class optimization for (6,6), preserving
                the 1,234-mask reduction. Do not run its 21.77-billion-vector
                direct census and do not descend to V=58.
```

**2026-07-27, profile `(6,6)` and E30 endpoint close:** the measured
per-template cost made a complete exceptional-mask census inexpensive on
Modal. Independent relaxations, independent actual-vector engines, conductor,
and independent exact norms close the final profile and the whole chamber.

```text
node attacked: N=256, V=60 profile (6,6)
odd-set identity: b = 1_O + 2*1_E, where O is the symmetric six-difference
                  light set and E is six classes outside O
relaxation assignments: 1234*binom(57,6)=44,779,702,968 per engine
relaxation production: ap-R8qZ3NFpBLlaSCjEPobazm; signed zero-sum kernel;
                       100.879807 aggregate worker-seconds
relaxation audit: ap-HhZLnYkj1E6sx207Qc1FwO; cyclic base vectors, pair sums,
                  three-plus-three decomposition; 79.819110 worker-seconds
exact relaxation agreement: all 1,234 rows; 33,737 exceptions on 1,191 masks;
                            maximum M_3=1542
actual production: ap-tzoEgc0dyKoBc3yghLmKLF; folded oriented chords;
                   2,781.809284 aggregate worker-seconds
actual audit: ap-NXOjRlg7idEiFtq2ALTgxX checkpointed 864/1191 at launcher wall;
              ap-BZCZ0tCpInuxZwZoxLl7V4 resumed the remaining 327 only;
              4,240.754407 aggregate worker-seconds over the complete packet
actual coverage per engine: 1191*binom(124,3)*64=23,638,891,776 vectors
exact actual agreement: 240,672 profile vectors; 6,244 above cutoff;
                        1,232 full conductor; maxima 1530/1338
proper conductor: complementary 5,012 exceptions discharged by the existing
                  conductor theorem
norm app: ap-BngTsJiGLxbGZxPkOOPRU6; batched FLINT and PARI/GP
norm agreement: all 1,232 vectors; 575 distinct norms
exact maximum: 384340001363476246612319029755636117549080229904040014178244445877664108548
strict margin: 4*N_max<2^250<5*N_max; bit length 248
result: profile (6,6) CLOSED; V=60 endpoint CLOSED
live positive even variance frontier: V<=58
new assumptions: none
route decision: derive the exact E29 slack/profile/parity reduction before any
                V=58 census; compare its expected cost and structural leverage
                against the 419-cofactor (4,2,0) lane. Never rerun V>=60.
```

**2026-07-27, E29 reduction and V=58 endpoint close:** odd diameter parity
makes the next chamber substantially smaller. A complete 111-template census,
independent direct audit, conductor split, and dual exact-resultant ledger
close all eight profiles without a speculative dependency.

```text
node attacked: N=256, folded profile (3,4,0), V=58 (E=29)
reduction app: ap-cStwZGv722wX16Xv1IwVyb
slack result: L<=17; exactly 17 energy profiles
exact cubic cutoff: M_3=872; certified sign change at 872/873
parity fact: D_64 odd, hence exactly one light-light diameter
above-cutoff profiles: 13
parity survivors: (5,6), (1,7), (4,4,1), (0,5,1), (3,2,2),
                  (5,2,0,1), (2,0,3), (1,3,0,1)
complete one-diameter atlas:
  odd 1: 264 supports, 11 affine orbits, partition (2,2,1)
  odd 3: 960 supports, 8 affine orbits, partition (2,1,1,1)
  odd 5: 14,400 supports, 100 affine orbits, partition (1,1,1,1,1)
relevant router: 11+100=111 affine light templates
diameter ledger: (D_64,C)=(1,-36),(5,-34),(9,-32),(17,-28),(21,-26)
production app: ap-bK8FgTfXIIVwtoGo3F2n5X; folded oriented chords;
                281.417969 aggregate worker-seconds
audit app: ap-3A3ZpIs4p0CuKplBr3VyfX; direct negacyclic products;
           443.275135 aggregate worker-seconds
coverage per engine: 111*binom(124,3)*64=2,203,120,896 vectors
exact row agreement: 61,408 vectors in the eight profiles;
                     4,812 above M_3=872; 820 full conductor
proper conductor: complementary 3,992 exceptions discharged by theorem
norm app: ap-Lr43rWTE9sjJ7D87pDRgvj; FLINT and PARI/GP agree on all 820
distinct norms: 242
exact maximum: 186828941137106397532470537651505306486275228904728704307636700572095315972
strict margin: 9*N_max<2^250<10*N_max; bit length 247
result: all eight profiles CLOSED; V=58 endpoint CLOSED
live positive even variance frontier: V<=56
new assumptions: none
route decision: derive the exact E28 slack/profile/parity reduction before any
                V=56 census, then compare its finite cost against the
                419-cofactor (4,2,0) lane. Never rerun V>=58.
```

**2026-07-27, E28 reduction and V=56 endpoint close:** the exact reduction
reuses the proved four-odd atlas and needs only 154 affine templates. Two
complete census engines and two exact resultant systems close the chamber.

```text
node attacked: N=256, folded profile (3,4,0), V=56 (E=28)
successful reduction app: ap-BEcZIXOVjDX7VcTVMin3Bd
discarded launch: ap-O0c99UzKohFBiFyJrHkEkS failed during module import and
                  executed no mathematical task
slack result: L<=16; exactly 14 energy profiles
exact cubic cutoff: M_3=658; certified sign change at 658/659
parity survivors: (4,6), (0,7), (3,4,1), (2,2,2), (4,2,0,1),
                  (1,0,3), (0,3,0,1), (3,0,1,1)
zero-odd branch: 63 antipodal-pair supports in six affine orbits
four-odd branch: 28,800 supports in the proved 148-orbit wedge atlas
relevant router: 6+148=154 affine light templates
production app: ap-PQuIHM0okhzDOzZI6rgd4Y; folded oriented chords;
                417.141898 aggregate worker-seconds
audit app: ap-ZWrJEBdrWedbKw7pdza9ho; direct negacyclic products;
           625.422659 aggregate worker-seconds
coverage per engine: 154*binom(124,3)*64=3,056,582,144 vectors
exact row agreement: 48,716 vectors in the eight profiles;
                     12,638 above M_3=658; 4,372 full conductor
proper conductor: complementary 8,266 exceptions discharged by theorem
norm app: ap-0LbmLFyAQLcHe8swtJKntb; FLINT and PARI/GP agree on all 4,372
distinct norms: 1,723
exact maximum: 296015175952529502165108365809577184284217843110959136601469787066321741314
strict margin: 6*N_max<2^250<7*N_max; bit length 248
result: all eight profiles CLOSED; V=56 endpoint CLOSED
live positive even variance frontier: V<=54
new assumptions: none
route decision: derive the exact E27 slack/profile/parity reduction before any
                V=54 census and compare its router size against the
                419-cofactor (4,2,0) lane. Never rerun V>=56.
```

**2026-07-27, E27 reduction and V=54 endpoint close:** parity collapses the
next chamber to the eight-template three-odd atlas. Two complete census
engines and two exact resultant systems close it at negligible cost.

```text
node attacked: N=256, folded profile (3,4,0), V=54 (E=27)
reduction app: ap-uT47ZBzFbCYqTmdbn7zG1I
slack result: L<=15; exactly 12 energy profiles
exact cubic cutoff: M_3=443; certified sign change at 443/444
parity survivors: (3,6), (2,4,1), (1,2,2), (3,2,0,1),
                  (0,0,3), (2,0,1,1)
three-odd branch: 960 normalized supports in eight affine orbits
production app: ap-TQfwKsNXu1kB9LO9TAgZT6; folded oriented chords;
                19.015265 aggregate worker-seconds
audit app: ap-a7WhPP5KNGWSOf96KvBtw7; direct negacyclic products;
           30.721920 aggregate worker-seconds
coverage per engine: 8*binom(124,3)*64=158,783,488 vectors
exact row agreement: 4,124 vectors in the six profiles;
                     2,000 above M_3=443; 404 full conductor
proper conductor: complementary 1,596 exceptions discharged by theorem
norm app: ap-OfeHk15LrirQxEKgld7vBk; FLINT and PARI/GP agree on all 404
distinct norms: 144
exact maximum: 172876856486553232403068097247779856553359362267270754177943490636016856066
strict margin: 10*N_max<2^250<11*N_max; bit length 247
result: all six profiles CLOSED; V=54 endpoint CLOSED
live positive even variance frontier: V<=52
new assumptions: none
route decision: derive the exact E26 slack/profile/parity reduction before any
                V=52 census and compare its router size against the
                419-cofactor (4,2,0) lane. Never rerun V>=54.
```

**2026-07-27, E26 reduction and two-odd branch close:** the exact reduction
finds a sharp route boundary. The bounded two-odd branch is completely paid;
the six-odd branch is too large for an undifferentiated census and remains the
live endpoint.

```text
starting local pin: ab709d27
canonical prize pin: b60ec497
upstream main pin: b13de8113a03f06b6fc22bbd2f289a8abcdf7e95
relevant live upstream PR: #1110 (E1 first-band variance route boundary)
node attacked: N=256, folded profile (3,4,0), V=52 (E=26)
reduction app: ap-6FCOpigQ0DnR00JZXFRPB5
discarded reduction app: ap-7jev6lqubs6DibhWhq1kBo failed before writing a
                         result packet and supplies no evidence
slack result: L<=16; exactly 13 energy profiles
exact cubic cutoff: M_3=228; certified sign change at 228/229
parity survivors: six two-odd profiles and four six-odd profiles
two-odd atlas: 8,168 normalized supports in 87 affine orbits
six-odd atlas: 280,720 normalized supports in 1,234 affine orbits
direct router floor: 26,219,123,456 vectors per engine
discarded census app: ap-58gqxzADkt6TRnH4o03zey failed at worker import,
                      completed 0/87 tasks, and supplies no evidence
production app: ap-TcZRS6xma3n8xdyUiNOg8b; 247.467486 worker-seconds
audit app: ap-jP3CZ7pvZjaZ20jDUQ8LSF; 323.193324 worker-seconds
two-odd coverage per engine: 87*binom(124,3)*64=1,726,770,432 vectors
exact row agreement: 27,380 profile vectors; 17,624 above M_3=228;
                     8,060 full conductor
proper conductor: complementary 9,564 exceptions discharged by theorem
norm app: ap-R4vDRzg2rsb0k2gJD2xmqB; FLINT and PARI/GP agree on all 8,060
distinct norms: 1,442
exact maximum: 902560312161452055740126650872074695232473707768299835426377069738129096704
strict margin: 2*N_max<2^250<3*N_max; bit length 249
result: six two-odd profiles CLOSED; V=52 endpoint remains OPEN
live residual: (6,5), (5,3,1), (4,1,2), (6,1,0,1)
six-odd direct floor: 1,234*binom(124,3)*64=24,492,353,024 vectors per engine
new assumptions: none
route decision: do not brute-force the six-odd chamber. Reuse the exact
                odd-mask, quotient, and norm structure from E30 to seek a
                profile-specific relaxation or algebraic exclusion.
```

**2026-07-27, E26 six-odd branch and V=52 endpoint close:** two cheap
structural relaxations failed to shrink the template axis, but a bounded
top-mask pilot showed the actual-vector engine was fast enough to justify a
single complete dual pass. The resulting exact certificate closes the whole
branch.

```text
node attacked: N=256, folded profile (3,4,0), V=52 (E=26), six-odd branch
odd-mask relaxation: every one of 1,234 masks survives for both tested cheap
                     profiles; maxima 870 and 606 exceed M_3=228
quotient relaxation maxima at orders 128/64:
  (6,5) 1282/1248; (5,3,1) 1062/1054;
  (4,1,2) 870/870; (6,1,0,1) 734/732
route decision from no-go probes: quotient and magnitude-only relaxations do
                                  not close or materially shrink the branch
top-mask pilot app: ap-L2vmgKMlAx8lsHkCxmzySB; 32 masks;
                    635,133,952 vectors; 44 primitive cubic exceptions
pilot norm app: ap-sSRw4M4r3Lo3CFYJzKwm74; dual agreement; no norm >=2^250
discarded census app: ap-Jq5ilys1UDMuhHb04wAVdk failed at remote import;
                      completed 0/1,234+0/1,234 and supplies no evidence
complete census app: ap-w01euXu1uuSZMynixEsU9m
coverage per engine: 1,234*binom(124,3)*64=24,492,353,024 vectors
independent engines: folded oriented chords and direct negacyclic products
exact row agreement: 78,848 profile vectors; 74,614 above M_3=228;
                     45,408 full conductor
proper conductor: complementary 29,206 exceptions discharged by theorem
norm app: ap-B13nYXtQQsbfCqFKDPTeUr; FLINT and PARI/GP agree on all 45,408
distinct norms: 20,636
exact maximum: 1139098407599461804511111865916270680930143333943822578584573946997885235216
strict margin: N_max<2^250<2*N_max; bit length 250
result: all four six-odd profiles CLOSED; V=52 endpoint CLOSED
live positive even variance frontier: V<=50
new assumptions: none
route decision: derive the exact E25 slack/profile/parity/light reduction and
                quantify its router before authorizing any V=50 census.
                Never rerun V>=52.
```

**2026-07-27, E25 reduction and V=50 endpoint close:** this is the last live
even level for the fixed cubic-Hermite majorant. The cutoff is tiny, but the
actual-vector and exact-norm remainders remain bounded and close completely.

```text
node attacked: N=256, folded profile (3,4,0), V=50 (E=25)
failed route app: ap-0xK5g91qR7LZzevi5tScu5 failed at remote import;
                  completed no computation and supplies no evidence
reduction app: ap-Bmu0kinryPMCm1zYI5CWas
slack result: L<=15; exactly 12 energy profiles
exact cubic cutoff: M_3=13; certified sign change at 13/14
parity survivors: nine profiles; five one-odd and four five-odd
light atlas: 264+14,400 normalized supports in 11+100=111 affine orbits
coverage per engine: 111*binom(124,3)*64=2,203,120,896 vectors
census app: ap-GPkfA9swDimrWIrdVL3u7Z
independent engines: folded oriented chords and direct negacyclic products
exact row agreement: 31,686 profile vectors; 31,280 above M_3=13;
                     16,984 full conductor
proper conductor: complementary 14,296 exceptions discharged by theorem
norm app: ap-P7nLJ3MSSHmUrHb9P2RSoX; FLINT and PARI/GP agree on all 16,984
distinct norms: 3,727
exact maximum: 689346143769176281255733260656192958605975198224651023251426809106119000068
strict margin: 2*N_max<2^250<3*N_max; bit length 249
result: all nine profiles CLOSED; V=50 endpoint CLOSED
live positive even variance frontier: V<=48
new assumptions: none
route boundary: local PROVED node e1_first_band_variance_route_boundary,
                imported exactly from PR #1110 at 52775686, proves the fixed
                majorant has negative optimistic margin even at M_3=0 for
                every even V<=48; it closes no variance level
route decision: derive the exact E24 profile/parity/light router without a
                cubic cutoff. Price a count-only actual-vector pass before
                retaining every primitive vector for direct exact norms.
                Never rerun V>=50.
```

**2026-07-27, E24 cutoff-free route and V=48 endpoint close:** the first level
below the fixed-majorant boundary closes by geometry, conductor, and direct
exact norms.

```text
node attacked: N=256, folded profile (3,4,0), V=48 (E=24)
discarded apps: ap-BllzyqghssXfECvbtq14LT failed during remote import;
                ap-fs6qDeT2zhk2cNUY23gOpQ hit an out-of-range diagnostic;
                neither wrote a result packet or supplies evidence
reduction app: ap-BHdqdt3NzeCkN5oPfwNwAo
slack result: L<=14; exactly nine energy profiles
majorant policy: not invoked; its optimistic margin is negative at M_3=0
parity survivors: two zero-odd and four four-odd profiles
light atlas: 28,863 normalized supports in 6+148=154 affine templates
coverage per engine: 154*binom(124,3)*64=3,056,582,144 vectors
count app: ap-k55Y5gyShllfB8hQqHCwQ1; dual engines agree exactly
actual profiles: [10878,0,2780,306,452,0], total 14,416
full conductor: [5870,0,836,30,98,0], total 6,834
proper conductor: complementary 7,582 vectors discharged by theorem
collector app: ap-YUhoRVWWVQcb1O5XcckRAp; dual vector agreement
norm app: ap-3hh9iFYztMHpgVSG9ydtd6; FLINT/PARI agreement on all 6,834
distinct norms: 2,684
exact maximum: 934000596876556404040131946795508791323292938762264172037712523409677324304
strict margin: N_max<2^250<2*N_max; bit length 250
result: all six profiles CLOSED; V=48 endpoint CLOSED
live positive even variance frontier: V<=46
new assumptions: none
route decision: derive the exact cutoff-free E23 (V=46) router and price its
                actual-vector residue. Never rerun V>=48.
```

**2026-07-27, E23 cutoff-free route and V=46 endpoint close:** odd diameter
parity collapses the next chamber to the eight-template repeated-chord atlas.

```text
node attacked: N=256, folded profile (3,4,0), V=46 (E=23)
reduction app: ap-GuKw0MZUMz3HlWbFd7G2uw
slack result: L<=13; exactly seven energy profiles
majorant policy: not invoked
parity survivors: four three-odd profiles on 960 normalized supports
light atlas: eight affine templates
coverage per engine: 8*binom(124,3)*64=158,783,488 vectors
census app: ap-v5PL88R8Ux130XBREm4eA1; dual exact engine agreement
actual profiles: [1176,522,46,144], total 1,888
full conductor: [352,108,0,24], total 484
proper conductor: complementary 1,404 vectors discharged by theorem
norm app: ap-4g3qQD2QBjTJtojanosSzw; FLINT/PARI agreement on all 484
distinct norms: 176
exact maximum: 721495288731652690472090495266069052907254127194382380048009480013819013124
strict margin: 2*N_max<2^250<3*N_max; bit length 249
result: all four profiles CLOSED; V=46 endpoint CLOSED
live positive even variance frontier: V<=44
new assumptions: none
route decision: derive the exact cutoff-free E22 (V=44) router. Never rerun
                V>=46.
```

**2026-07-27, E22 cutoff-free route and V=44 endpoint close:** even diameter
parity reopens the two/six-odd atlases, but count-only routing keeps the exact
residue small enough for direct norms.

```text
node attacked: N=256, folded profile (3,4,0), V=44 (E=22)
reduction app: ap-R4qgQHRIHJgTwquZvDY2X9
slack result: L<=14; exactly nine energy profiles
majorant policy: not invoked
parity result: (9,1,1) rejected; four two-odd and four six-odd survivors
light atlas: 288,888 normalized supports in 87+1,234=1,321 templates
coverage per engine: 1,321*binom(124,3)*64=26,219,123,456 vectors
discarded count app: ap-P1qQjalsb356Myrg2vdPGB failed during remote import;
                     completed no template and supplies no evidence
count app: ap-dpRsXRNVjQZefmrwM9Z1kz; dual exact engine agreement;
           7,919.618 aggregate dual worker-seconds
actual profiles: [15924,5228,4532,1096,790,22,104,302], total 27,998
full conductor: [9688,2550,2074,242,368,0,28,52], total 15,002
proper conductor: complementary 12,996 vectors discharged by theorem
collector app: ap-Z4JCbeBxhxRPjAlBxbUvLV; dual vector agreement;
               7,774.627 aggregate dual worker-seconds
norm app: ap-hxfrf1vAUiZNYnbuVtAfNZ; FLINT/PARI agreement on all 15,002
distinct norms: 5,991
exact maximum: 1336721602285440319478157639166117651370659494817695620407452489394658888194
strict margin: N_max<2^250<2*N_max; bit length 250
result: all eight profiles CLOSED; V=44 endpoint CLOSED
live positive even variance frontier: V<=42
new assumptions: none
route decision: derive the exact cutoff-free E21 (V=42) router. Never rerun
                V>=44.
```

**2026-07-28, E21 cutoff-free route and V=42 endpoint close:** odd diameter
parity returns to the small one/five-odd atlas, and the complete exact residue
again fits direct dual norms.

```text
node attacked: N=256, folded profile (3,4,0), V=42 (E=21)
discarded reduction app: ap-WheEh8ejQUWcxI3NrF52Iu failed before producing
                         a route packet and supplies no evidence
reduction app: ap-xmWUTZrP3C8A1Q5ZTdWInc
slack result: L<=13; exactly eight energy profiles
majorant policy: not invoked
parity result: (8,1,1) rejected; three one-odd and four five-odd survivors
light atlas: 14,664 normalized supports in 11+100=111 templates
coverage per engine: 111*binom(124,3)*64=2,203,120,896 vectors
count app: ap-sB6bBUn8fAtNRenTKaRqGa; dual exact engine agreement;
           684.456 aggregate dual worker-seconds
actual profiles: [6400,1676,1658,252,348,44,76], total 10,454
full conductor: [3608,488,456,16,68,4,0], total 4,640
proper conductor: complementary 5,814 vectors discharged by theorem
collector app: ap-8y0cQsyAvpSx8Is0Athw8k; dual vector agreement;
               684.327 aggregate dual worker-seconds
norm app: ap-F5Bs9JuuZRpjReqxeTSNIE; FLINT/PARI agreement on all 4,640
distinct norms: 1,365
exact maximum: 1067431210213337343847285566520999617146298326197261566762764923557911188994
strict margin: N_max<2^250<2*N_max; bit length 250
result: all seven profiles CLOSED; V=42 endpoint CLOSED
live positive even variance frontier: V<=40
new assumptions: none
route decision: derive the exact cutoff-free E20 (V=40) router and price its
                actual-vector residue. Never rerun V>=42.
```

**2026-07-28, E20 cutoff-free route and V=40 endpoint close:** even diameter
parity reduces the chamber to the zero/four-odd atlas, and the exact residue
is smaller than at either of the preceding even endpoints.

```text
node attacked: N=256, folded profile (3,4,0), V=40 (E=20)
discarded reduction app: ap-8UFxz5tQyXEHmOzAK1rLmQ failed before producing
                         a route packet and supplies no evidence
reduction app: ap-xzC1R27IwAsKJ1lyw6A0kW
slack result: L<=12; exactly seven energy profiles
majorant policy: not invoked
parity result: (7,1,1) rejected; two zero-odd and four four-odd survivors
light atlas: 28,863 normalized supports in 6+148=154 templates
coverage per engine: 154*binom(124,3)*64=3,056,582,144 vectors
count app: ap-iegnpEhh0V6js6IkkcDEWr; dual exact engine agreement;
           952.816 aggregate dual worker-seconds
actual profiles: [2588,2160,888,52,34,704], total 6,426
full conductor: [1090,544,194,8,0,64], total 1,900
proper conductor: complementary 4,526 vectors discharged by theorem
collector app: ap-18QcozEhrOO0MkhBtr6sTU; dual vector agreement;
               964.815 aggregate dual worker-seconds
norm app: ap-WGuf8zhWii313tpUoMUdWG; FLINT/PARI agreement on all 1,900
distinct norms: 526
exact maximum: 1047057848181589561057910777870710713025120091730047736000219719807296950274
strict margin: N_max<2^250<2*N_max; bit length 250
result: all six profiles CLOSED; V=40 endpoint CLOSED
live positive even variance frontier: V<=38
new assumptions: none
route decision: derive the exact cutoff-free E19 (V=38) router and price its
                actual-vector residue. Never rerun V>=40.
```

**2026-07-28, E19 cutoff-free route and V=38 endpoint close:** odd diameter
parity reduces the chamber to the one-diameter three-odd atlas, and the full
actual-vector residue closes by conductor and exact norms.

```text
node attacked: N=256, folded profile (3,4,0), V=38 (E=19)
reduction app: ap-9mBPqJQyYGcOTtaHQ1AEXz
slack result: L<=11; exactly five energy profiles
majorant policy: not invoked
parity result: (6,1,1) rejected; four three-odd survivors
light atlas: 960 normalized supports in 8 affine templates
coverage per engine: 8*binom(124,3)*64=158,783,488 vectors
census app: ap-42XirNxhFdMDLcgSyAoyqK; dual exact engine agreement;
            45.217 aggregate dual worker-seconds
actual profiles: [370,182,10,12], total 574
full conductor: [112,24,0,0], total 136
proper conductor: complementary 438 vectors discharged by theorem
norm app: ap-qH9fzHkBAjTdTeWWEgJ7iN; FLINT/PARI agreement on all 136
distinct norms: 40
exact maximum: 1096349292027446593481621675930218905147073043465918102751396673154250061826
strict margin: N_max<2^250<2*N_max; bit length 250
result: all four profiles CLOSED; V=38 endpoint CLOSED
live positive even variance frontier: V<=36
new assumptions: none
route decision: derive the exact cutoff-free E18 (V=36) router and price its
                actual-vector residue. Never rerun V>=38.
```

**2026-07-28, E18 cutoff-free route and V=36 endpoint close:** even diameter
parity reduces the chamber to the two/six-odd atlases. The whole-norm cutoff
fails for the first time, but the exact odd-part criterion closes the residue.

```text
node attacked: N=256, folded profile (3,4,0), V=36 (E=18)
reduction app: ap-YxeY4JsxalEEMItNl8DQOC
slack result: L<=12; exactly seven energy profiles
majorant policy: not invoked
parity result: (9,0,1) rejected; six two/six-odd survivors
light atlas: 288,888 normalized supports in 87+1234=1,321 templates
coverage per engine: 1321*binom(124,3)*64=26,219,123,456 vectors
census app: ap-87cpQMjvYyW2nYdoZpL6Uz; dual exact engine agreement;
            7,712.034 aggregate dual worker-seconds
actual profiles: [2410,3096,842,208,4,152], total 6,712
full conductor: [1100,1622,226,18,0,28], total 2,994
proper conductor: complementary 3,718 vectors discharged by theorem
superseded norm diagnostic: ap-u5Kj4NOzDFQPwSB1TLUNdT
final norm app: ap-k5DWA74ZUKZK3N03ngNeEP; FLINT/PARI agreement on all 2,994
distinct norms: 895
exact whole-norm maximum: 3244660049331064070204285700733501169431397018164712582311239362105072116226
whole norms at or above 2^250: 6 (strong shortcut REFUTED)
exact odd-part maximum: 1622330024665532035102142850366750584715698509082356291155619681052536058113
strict odd margin: odd_max<2^250<2*odd_max; odd threshold hits 0
result: all six profiles CLOSED; V=36 endpoint CLOSED
live positive even variance frontier: V<=34
new assumptions: none
route decision: derive the exact cutoff-free E17 (V=34) router and price its
                actual-vector residue. Never rerun V>=36.
```

**2026-07-28, provisional KoalaBear K3 equality-wall stack reconciliation:**
four open upstream PRs materially reduce one source-bound equality-wall
residual, but none currently supplies a bankable first-match atom. They are
recorded as upstream-watch route evidence only; no local node, `req` edge,
crosswalk status, or critical status changes.

```text
starting local pin: 8f211958
canonical prize pin: b60ec497
upstream main pin: b13de8113a03f06b6fc22bbd2f289a8abcdf7e95
critical counts at start: TARGET=73, CONDITIONAL=58
crosswalk: PASS, 74 rows, 11 IDENTICAL
PR #1114: 702cd8e16673f2971ac1e7898603de2d7d087dfa
          replays the 22 prerequisite families for the source-bound wall
PR #1115: 065f347a96c91ade7d80df8bf324f646329c623e
          excludes q=1 and split degrees 2,...,11; leaves 12,...,16
PR #1116: 44542e91e459364a521870ed2ebde7f6fe5055bf
          reduces the normalized residue to Q=6,u=2 plane/conic/quartic
          geometry; its synthetic-model search remains finite evidence
PR #1117: f42ad6ab64cda5f1d4061b73e739f8944ebb13eb
          excludes 60 P3+C3 labeled graphs; 405 labeled graphs remain, and
          the open orbit counts 46,30,10,10 are not a partition of 405
local owner: rate_half_band_closure, KoalaBear v4 owner ledger
relation: OVERLAP/evidence with the unpaid K3 balanced-core/residual-geometry
          obligation; not a supplier for rate_half_kb_v4_tangent_source_atom
nonclaims: no U_Q, U_BC, U_new, global pencil-chart census, fixed-union
           aggregation, exhaustive slope payment, adjacent-safe certificate,
           or endpoint movement
promotion test: after merge, independently replay the exact stack and prove
                a source-bound transport into one frozen first-match cell;
                then either derive its exact distinct-slope integer or an
                exhaustive zero residual and wire that theorem to the local
                KoalaBear owner
result: HARVESTED as provisional route evidence; no DAG delta
next route-deciding action: continue direct E17/V34 descent while watching
                            the stack for a global owner/payment theorem
```

**2026-07-29, KoalaBear K3 coarse-invariant route cut:** upstream PR #1122
settles which part of the 405-case equality wall cannot close by abstract
incidence alone.

```text
upstream source: PR https://github.com/przchojecki/rs-mca/pull/1122
head: c93988e829e73d2f85db0eb33769bf677935afae
status at pin: OPEN, READY FOR REVIEW
exact abstract fixture:
  69 records, carrier size 1894736, support 981105
  affine/secant rank 8, full vertex-function rank 9
  minimum pair secant distance 1053746
  minimum directed exchange 121284
  all 3280 projective ternary directions have distance at least 1052958
  60 canonical bounded circuits, no singleton atoms, all printed
  restriction-rank inequalities
route verdict:
  those pairwise/ternary/exchange/rank/circuit consequences do not imply
  cap 68 and are not source-bound owner evidence
load-bearing successor:
  use the full arbitrary-coefficient GRS-span distance, actual split
  locators/source quotient/cocycle, primitive Hilbert-Burch module, or a
  same-record active owner while classifying the 405 live conic cases
scope fence:
  abstract fixture only; no GRS embedding, received line, slope, partition,
  charge, row atom, endpoint, local DAG status, or Prize movement
independent replay:
  Python PASS checks=960747; optimized Python PASS; mutations 42/42 rejected
compute spend: none; local exact replay used under RAMguard, peak input 76 KiB
```

**2026-07-29, KoalaBear Q6 u2 conic and primitive-monodromy harvest:**
upstream PRs #1128 and #1129 turn the `Q=6,s=6,u=2` geometric residual into
one finite functional-decomposition problem. Both scoped theorems were
audited, replayed locally with independent tiny verifiers, and imported as
PROVED route evidence. They do not move the owner ledger.

```text
source reduction: 44542e91e459364a521870ed2ebde7f6fe5055bf
manual integration pin: 0f7476f0fcbc5d1a1d3eed0c03221aaa48f5767d

PR #1128 head: ad109774f7d9bc320e7e0c046ba83471f39d5cd9
theorem blob: bd4ca8c756c22f6f475cb06c142de4c981d6b320
payload SHA-256: 30a5d45895957f774ef972118e227fa54522fc27a48ee0e2a99a0d5a012a5451
banked theorem:
  twelve degree-four source divisors saturate 2 div(B)
  conic invariance excludes reciprocal, D4, and D5 profiles
  complete Q6 u2 conic-image branch empty

PR #1129 head: 59c4449ca0f5cee929dd39fc7b5ae8b0a33877f4
theorem blob: 5d0ec0315fca34de80c22983b76bbafa12dd5661
payload SHA-256: 21a8ca7800745c2c94876d48473801e84f4d9c8f9e6ce5b53e8b8bd66b699962
banked theorem:
  residual birational quartic implies monodromy subdegree four
  none of the nine primitive degree-60 groups has subdegree four
  residual endpoint map is functionally decomposable
  exact possible inner degrees: 2,3,4,5,6,10,12,30

local nodes:
  rate_half_kb_q6_u2_complete_source_conic_exclusion [PROVED]
  rate_half_kb_q6_u2_primitive_subdegree4_route_cut [PROVED]
local consumer: rate_half_band_closure [evidence edges only]
ledger movement: zero
nonclaims: no domain-compatible quotient owner, descent of a decomposition,
           u2 closure, cap 68, first-match payment, adjacent certificate,
           official-row close, or endpoint movement
next theorem:
  construct the eight-degree domain-compatible decomposition adapter; for
  each inner degree either prove incompatibility with the source divisor and
  pole data or assign an exact first-match owner and charge
compute policy:
  classification is already finite and paid; begin symbolically from pole
  partitions and source-field descent, with no broad enumeration
```

**2026-07-29, KoalaBear decomposition divisor adapter and degree-five
deletion:** direct symbolic continuation of the PR #1129 route cut proves
that geometric decomposability already preserves the local active and source
divisors, then eliminates one of the eight degree rows over the deployed
field.

```text
parent: rate_half_kb_q6_u2_primitive_subdegree4_route_cut [PROVED]
new nodes:
  rate_half_kb_degree60_decomposition_divisor_adapter [PROVED]
  rate_half_kb_degree5_decomposition_exclusion [PROVED]
endpoint divisor: div(f)=D_act-5 D_src
active consequence:
  every outer zero is simple and unramified under h
  D_act is exactly 60/m complete m-point fibers in F_(p^6)
source consequence:
  order-five outer poles pull back to unramified m-point source fibers
  simple outer poles pull back to m/5 source points of index five
degree-five row:
  two index-five points contribute 8=2*5-2, exhausting Riemann-Hurwitz
  after a deployed-field domain normalization, h-fiber equality is x^5=y^5
  p=2130706433=3 mod 5 and p^6=4 mod 5
  gcd(5,p^6-1)=1, so fifth power is injective on P1(F_(p^6))
  contradiction with a complete five-point rational active fiber
result: inner degree 5 CLOSED; live degrees {2,3,4,6,10,12,30}
DAG delta: two PROVED nodes and evidence only toward rate_half_band_closure
ledger movement: zero
nonclaims: no coefficient-field descent for the seven rows, full deployed
           evaluation-domain quotient, witness-data descent, same-record
           owner, charge, u2 close, cap 68, adjacent certificate, or row close
compute spend: none; exact integer replays only under RAMguard
next route-deciding action:
  exploit the one- or two-fiber source profiles for m=6 and m=12 to test
  coefficient-field descent and constrain the bidegree-(4,4) component
```

**2026-07-29, upstream PR #1130 source-pencil harvest:** the independently
opened successor overlaps the local divisor and degree-five proofs and adds
four bankable structural reductions. Its scope was audited against the
endpoint/carrier distinction before import.

```text
upstream PR: https://github.com/przchojecki/rs-mca/pull/1130
head: a14a05d9ba80068133e93e2fa77d6d1dc8828829
parent: 59c4449ca0f5cee929dd39fc7b5ae8b0a33877f4
theorem blob: e15b77679b7dbc0bb28cf5642a04bb4c71e61429
certificate blob: 911bac3c1c5d1b4cd9822c59939d60e832b7ef23
payload SHA-256: 638190df24415e5609fa9c2f50dde8fd22bd150f60e7bef5cd1496cb22d75b4e
local node: rate_half_kb_decomposition_source_pencil_compiler [PROVED]
relation:
  OVERLAP on divisor pullback and degree-five deletion
  ADDITIVE on source-pencil equivalence, challenge-field descent,
  degree-30-to-6 refinement, canonical degree-12 compiler, and degree-two
  deck/carrier-stabilizer gates
banked consequences:
  h and the outer map admit models over F_(p^6) after target normalization
  every source profile is one coprime degree-m binary pencil certificate
  degree 30 factors through degree 6 and is not a separate row
  degree 12 has one canonical pencil and one six-dimensional membership test
  the degree-two deck involution lies in PGL_2(F_(p^6))
  conditional carrier projectivities are kappa*x or kappa/x only
result: distinct live degrees {2,3,4,6,10,12}
ledger movement: zero
scope fence:
  endpoint parameters are not evaluation coordinates; carrier cardinality
  and projectivity results remain conditional on a same-record bridge
nonclaims:
  no carrier bridge, received-data or slope descent, owner, payment, u2
  close, cap 68, adjacent certificate, endpoint movement, or row close
next route-deciding action:
  derive witness-data/chronology descent from the actual bidegree-(4,4)
  component; use the canonical degree-12 test and degree-two deck gate as
  fail-closed endpoints rather than reconstructing arbitrary maps
compute spend: none; finite arithmetic replayed locally under RAMguard
```

**2026-07-29, upstream PR #1131 rank/transverse harvest:** the next stacked
packet compiles all six source profiles and proves that the actual quartic
cannot remain inside a terminal inner fiber. It identifies the precise
source-coupled outer theorem now required.

```text
upstream PR: https://github.com/przchojecki/rs-mca/pull/1131
head: e287c54252c7872e1745c7594cfef62b74a65cf5
parent: a14a05d9ba80068133e93e2fa77d6d1dc8828829
theorem blob: b4a69440c518f22189ec2060cb3a3a500a23e724
certificate blob: 5c16c7884b349d7e474b8dfc1267ab357ef0d477
payload SHA-256: 6d4bc83e40e491f02f7d265b021628ffb7d52b1978c0655f83e5a9d3e0a9f4bb
local node: rate_half_kb_source_pencil_rank_transverse_compiler [PROVED]
per-record source templates: 32099; explicitly not a global endpoint census
exact compiler:
  source rank two
  active symmetric-power membership
  special degree-12 49x5 rank-five / 44-syndrome gate
same-fiber route:
  strict proper right factors first
  primitive degrees 2,3,4,6,10,12 have no subdegree four
  terminal bidegree-(4,4) component cannot lie in h(T)=h(W)
transverse terminal:
  delta*r=4m, delta<=m^2, r<=60/m-1
  26 exact (m,r,delta) types
route fence:
  source/active divisor controls survive for indecomposable m=2,3
  another source-only rank calculation cannot close the branch
ledger movement: zero
nonclaims:
  no global endpoint census, transverse-row deletion, actual-component
  realization of controls, carrier bridge, owner, charge, u2 close, cap 68,
  adjacent certificate, endpoint movement, or row close
next route-deciding action:
  impose the inherited quartic/source-star incidence on the 26 transverse
  rows and terminate each by contradiction, strict coarser decomposition,
  or chronology-valid carrier/data/slope ownership
compute spend: none; exact integer replays only under RAMguard
```

**2026-07-29, direct inner-degree-12 outer cut:** challenge-field splitting
and the primitive degree-five subdegree list remove two of the four
degree-12 transverse types without computation.

```text
new node: rate_half_kb_m12_outer_subdegree_route_cut [PROVED]
outbound PR: https://github.com/przchojecki/rs-mca/pull/1132 (draft)
route-cut layer: e368e5c8fc101ae0040b47265c2cd167e70dadd2
current outbound head: c23eb801af8853d0369a72ea8834c84e7a3242f6
stack parent: PR #1131 head e287c54252c7872e1745c7594cfef62b74a65cf5
inputs:
  outer F has degree 5, one rational pole of order 5, and five distinct
  rational simple zeros
  initial transverse rows (r,delta)=(1,48),(2,24),(3,16),(4,12)
r=3:
  impossible; primitive degree-five groups have subdegrees 1,2,4 only
r=1:
  gives a nontrivial deck graph, hence a cyclic degree-five cover
  unique pole and second branch point are rational
  normalized F=a*x^5+b over F_(p^6)
  gcd(5,p^6-1)=1 forbids five distinct rational zeros
result:
  live m=12 rows (2,24),(4,12)
  global transverse count 26 -> 24
DAG delta: one PROVED evidence node; critical target unchanged
ledger movement: zero
nonclaims:
  no deletion of r=2 or r=4, m12 close, owner, charge, u2 close, cap 68,
  adjacent certificate, endpoint movement, or row close
next route-deciding action:
  apply the canonical degree-12 source pencil and 21-vertex source-star bound
  to the dihedral r=2 and one-orbit r=4 survivors
compute spend: none; exact field arithmetic only under RAMguard
```

**2026-07-29, inner-degree-12 r4 low-genus reduction:** the remaining
one-orbit degree-five outer component is no longer a generic quintic
correspondence. A normalization-genus bound and complete tame branch-cycle
ledger leave five exact rows.

```text
new node: rate_half_kb_m12_r4_low_genus_branch_profile_reduction [PROVED]
input type: (m,r,delta)=(12,4,12)
actual-curve genus:
  H0 has bidegree (2,4) and is birational to Gamma, hence g(Gamma)<=3
  Gamma->C has degree 12, hence Riemann-Hurwitz forces g(C)<=1
outer polynomial ledger:
  infinity branch cycle (5), finite branch indices sum to 4
  off-diagonal normalization is the 20-sheet ordered-pair orbit
complete low-genus profiles:
  A5: (3),(2,2), genus 0
  A5: (3),(3), genus 1
  S5: (2),(3,2), genus 0
  S5: (2),(4), genus 0
  S5: (2),(2),(2,2), genus 1
route cuts:
  tame polynomial AGL(1,5) absent
  S5 profiles (2),(2),(3) and four copies of (2) have genus 2 and 3
  and are impossible
exact replay:
  all 120 permutations of S5; 310 admissible ordered two-transitive tuples
  independent explicit representatives and ordered-pair index audit
DAG delta: one PROVED evidence node; critical target unchanged
ledger movement: zero
nonclaims:
  no deletion or realization of the five profiles; r2 untouched; no r4,
  m12, owner, carrier/data bridge, charge, u2, cap 68, endpoint, or row close
next route-deciding action:
  normalize the genus-zero two-finite-branch rows to rigid polynomial forms;
  use the genus-one degree-12 cover and source-pole divisor on the other two;
  attack the dihedral r2 survivor separately
compute spend: 120-permutation exact local replay under tiny RAMguard; no Modal
```

**2026-07-29, inner-degree-12 outer normal forms:** the six live geometric
outer families now have explicit polynomial representatives, eliminating
arbitrary quintic discovery from this row.

```text
new node: rate_half_kb_m12_outer_normal_form_compiler [PROVED]
outbound custody: draft PR #1132 head f7a42415bdb24c7e626b76394558bad100c5a874
theorem blob: 5a36de4a27d80d5a885aa0751db9fc37d9744aab
certificate blob: 8e0ecd7f5b008900ada67dbf80848e8dbbff8416
payload SHA-256: 7eb4f4053f90cb4ca0d0f3379fa3f8f33522ae0ec9b3dc67f5c7e602150d22f0
r2 dihedral form:
  D5(x,a)=x^5-5a*x^3+5a^2*x
  divided difference splits over sqrt(5) into the two r=2 conics
r4 rigid forms:
  A5 (3),(2,2): x^3(12x^2-15(1+t)x+20t), 3t^2+4t+3=0
  A5 (3),(3): x^3(6x^2-15x+10)
  S5 (2),(3,2): x^3(x-1)^2
  S5 (2),(4): x^4(5-4x)
r4 one-parameter form:
  S5 (2),(2),(2,2): x^2(x-1)^2(2x-5t), on the profile's open locus
proof engines:
  genus-zero D5 Galois closure and explicit invariant fields
  exact derivative integration and repeated-critical-value equations
scope fence:
  forms are geometric affine normalizations; no challenge-field coefficient
  descent or endpoint-record membership is inferred
DAG delta: one PROVED evidence node; critical target unchanged
ledger movement: zero
nonclaims:
  no family deletion or realization, owner, carrier/data bridge, charge,
  m12, u2, cap 68, endpoint, or row close
next route-deciding action:
  derive a fail-closed challenge-field affine-equivalence classifier for the
  actual outer coefficients recovered from the canonical <A,N0> pencil;
  then impose split zeros and actual quartic/source-star incidence
compute spend: exact rational/quadratic-field identities under tiny RAMguard
```

**2026-07-29, inner-degree-12 split-fiber arithmetic descent:** the actual
split simple zero fiber removes the constant-field ambiguity and descends
three of the five `r=4` normalizations all the way to `K`.

```text
new node: rate_half_kb_m12_split_fiber_arithmetic_descent [PROVED]
arithmetic monodromy:
  F^(-1)(0) is five distinct K-points, so rational-fiber Frobenius is identity
  identity lies in the arithmetic Frobenius coset, hence G_ar=G_geom
  every geometric outer component is defined over K
K-affine normal forms:
  A5 (3),(2,2)
  S5 (3,2),(2)
  S5 (4),(2)
A5 ratio descent:
  3t^2+4t+3=0 has discriminant -20
  every prime-field element is square in the even extension F_(p^6)
  a nonsplit critical pair would force t=1/t, but t is not +/-1
exact remaining twist list:
  Dickson D5
  A5 (3),(3)
  S5 one-parameter (2),(2),(2,2)
DAG delta: one PROVED evidence node; critical target unchanged
ledger movement: zero
nonclaims:
  no family deletion or realization, twist classifier, source-star close,
  owner, carrier/data bridge, charge, m12, u2, cap 68, endpoint, or row close
next route-deciding action:
  compile coefficient invariants for the three twists; substitute the three
  descended rigid forms into the canonical pencil and source-star equations
compute spend: exact modular arithmetic only under tiny RAMguard
```

**2026-07-29, inner-degree-12 diagonal-socle route cut:** composition
monodromy removes the full Dickson branch and exposes a synchronized
one-point-per-outer-block structure on every actual survivor.

```text
new node: rate_half_kb_m12_diagonal_socle_route_cut [PROVED]
terminal degree-12 catalogue:
  M11, M12, PSL2(11), PGL2(11), A12, S12
  simple socles M11, M12, PSL2(11), A12; every action has subdegrees 1,11
block-kernel theorem:
  N = kernel on the five outer blocks
  [N,N] projects onto every simple inner socle
  Scott strips + primitive degree-five block action give S^5 or full diagonal S
  S^5 gives a 12-point orbit in every other block, contradicting |Delta|=4
cross-action audit:
  equivalent actions give point-stabilizer orbits 1,11
  paired ATLAS M12 12a/12b generators reconstruct order 95040
  the order-7920 12a stabilizer is transitive on 12b
route consequence:
  every block met by Delta contributes exactly one synchronized fixed point
  |Delta|=4 therefore forces outer subdegree r=4
  r=2 Dickson is deleted; the five r=4 normal forms remain
  in the M12 case all five block actions have the same action class
DAG delta: one PROVED evidence node; critical target unchanged
ledger movement: zero
nonclaims:
  no r4-family deletion, source-star close, owner, carrier/data bridge,
  charge, m12, u2, cap 68, endpoint, adjacent certificate, or row close
next route-deciding action:
  impose the synchronized diagonal point across all five outer fibers on
  the canonical <A,N0> pencil and actual source-star divisor
compute spend: 95,040-element exact permutation replay, under tiny RAMguard
```

**2026-07-29, inner-degree-12 closure by secondary degree five:** the full
diagonal socle automatically preserves a second block system, reducing the
last `m=12` survivor to the already-deleted degree-five row.

```text
new node: rate_half_kb_m12_secondary_degree5_decomposition_exclusion [PROVED]
outbound custody: draft PR #1132 head c23eb801af8853d0369a72ea8834c84e7a3242f6
theorem blob: cd29c893dceb63283c7a731c9a3c4280fa665c5c
certificate blob: 9e1bd3d89dac6409f148dc134fda46d3bf644c11
verifier blob: 989e6780f29c22acaa5d231ef9f1e54b47255138
payload SHA-256: 456b51c78e837c8a27ffda0b43409c63c88128b254be320723728868db096e6f
normalizer theorem:
  identify the five equivalent degree-12 socle actions on X
  a faithful nonregular two-transitive action has trivial Sym(X) centralizer
  every g normalizing diagonal S acts as (x,i) -> (n_g(x),pi_g(i))
secondary block system:
  twelve synchronized columns C_x, each of size five
  monodromy/intermediate-field correspondence gives an inner-degree-5 factor
contradiction:
  the existing deployed-field degree-five exclusion quantifies over every
  geometric decomposition of the endpoint map
  fifth-power injectivity forbids its complete five-point rational fibers
route consequence:
  all five r4 normal-form families are deleted
  m=12 is fully closed
  global transverse frontier: 23 -> 22 types
  live decomposition degrees: 2,3,4,6,10
DAG delta: one PROVED evidence node; critical target unchanged
ledger movement: zero
nonclaims:
  no close for another degree, owner, carrier/data bridge, charge, u2,
  cap 68, endpoint, adjacent certificate, or KoalaBear row close
next route-deciding action:
  seek a forced secondary block system at m=6; otherwise impose the actual
  source-star incidence on the smallest surviving outer type
compute spend: tiny exact finite block and field arithmetic only
```

**2026-07-29, inner-degree-10 Scott-strip lower-degree route:** all four
degree-10 transverse types route strictly to smaller decomposition rows.

```text
new node: rate_half_kb_m10_scott_strip_lower_degree_router [PROVED]
outbound custody: draft PR #1132 head 412bc68f1dcb6ac3924d6445146417f3c713ef89
theorem blob: 13645fac5d116ec90ebbd5f1254d74b9715f83be
certificate blob: 6e49093fdb9d9e55b45c55265eb3cc0c0e65e8c9
verifier blob: 9f12c4e749b3ab147b2374943c3d9b56c2c90697
payload SHA-256: 66117d7ba207a66606fc4ae4770a2b314b3510066be7af734b4e579d028ce1d1
terminal degree-10 catalogue:
  A5, S5; five A6 almost-simple extensions; A10, S10
  simple socles A5, A6, A10; subdegrees 1,3,6 or 1,9
kernel-free audit:
  only A5 and S5 can fit through the order-120 outer point stabilizer
  N=1 then forces the global A6 or S6 action on 60 point/two-subset flags
  exact subdegree rows contain 1,2,3,6,12 but no 4, contradiction
nontrivial-kernel route:
  [N,N] is subdirect in six simple socles
  Scott supports have common size t in {1,2,3,6}
  t=1 gives a 10-point orbit in another block, contradicting |Delta|=4
  all socle automorphisms are realized on ten points and centralizers vanish
  synchronized columns in each strip give inner degree t in {2,3,6}
route consequence:
  m=10 has no terminal producer; its four types route strictly downward
  global independent transverse frontier: 22 -> 18 types
  live independent decomposition degrees: 2,3,4,6
DAG delta: one PROVED evidence node; critical target unchanged
ledger movement: zero
nonclaims:
  endpoints may still admit degree-10 decompositions; no close for another
  degree, owner, carrier/data bridge, charge, u2, cap 68, endpoint,
  adjacent certificate, or KoalaBear row close
next route-deciding action:
  classify the degree-6 block kernel and Scott supports; if no strict route
  survives, impose the actual source-star incidence on its smallest type
compute spend: exact 720-permutation flag audit under tiny RAMguard; no Modal
```

**2026-07-29, inner-degree-6 Scott-Cartesian degree-two route:** all six
degree-six transverse types die through degree five or route to degree two.

```text
new node: rate_half_kb_m6_scott_cartesian_degree2_router [PROVED]
outbound custody: draft PR #1132 head 30be68b9421ba37155499d52a0635fa7b10ae3b2
theorem blob: 0135c1f76e01cac07c958356dc5b5a1056d85432
certificate blob: af5fd87a5c28f3b021fc05971a665e6d92f978af
verifier blob: 4df203a90a682d2a1ab7e36f7f98221b7db40592
payload SHA-256: b34e096730f3d93644c283f95d65f622100d6868e9882ed2b901fa109b3d6116
kernel-free classification:
  45 transitive degree-10 groups -> order divisible by 600 -> entries 40..45
  A10 and S10 point stabilizers have no primitive degree-6 quotient
  four wreath cases have exact endpoint/intermediate indices 6 and 5
nontrivial-kernel route:
  degree-6 socles are A5 or A6 with subdegrees 1,5
  Scott twists refine into uniform permutation-compatible classes
  the actual four-point orbit forces compatible class size 5 or 10
  size 5 is the excluded degree-five row
  size 10 puts the four-point orbit in one degree-10 column fiber
  primitive degree-10 subdegrees exclude 4, so the column map factors
  proper right-factor degrees are 2 or 5; only degree 2 survives
route consequence:
  m=6 has no independent terminal producer
  global independent transverse frontier: 18 -> 12 types
  live independent decomposition degrees: 2,3,4
exact audit:
  explicit groups of orders 7200,14400,14400,28800
  endpoint stabilizers 720,1440,1440,2880
  intermediate subgroup index 5 in every case
DAG delta: one PROVED evidence node; critical target unchanged
ledger movement: zero
nonclaims:
  no degree-two deletion or payment, owner, carrier/data bridge, charge,
  u2, cap 68, endpoint, adjacent certificate, or KoalaBear row close
next route-deciding action:
  classify degree 4 using the actual quartic suborbit before any endpoint
  record expansion
compute spend: four exact groups, maximum order 28800, under tiny RAMguard;
               no Modal
```

**2026-07-29, inner-degree-4 outer A6/S6 route cut:** the complete
primitive degree-15 catalogue removes three of the four outer types.

```text
new node: rate_half_kb_m4_outer_a6s6_route_cut [PROVED]
upstream custody:
  PR #1132 head: d7232a30a5cca4a42330422415da71f06a7c5a31
  note/certificate/verifier blobs:
    13fd38f97fb7087df88fe7c212020933b409d191
    bb130d089d1ca7c0fcab04b65f66de773952ceb2
    06854e72fe35720052505c543d86bcf587f61017
  certificate payload:
    61a8db82285f22393fc2af6c1d35224d79587fa150009270d42ac33972557485
incoming m4 types: (1,16),(2,8),(4,4),(8,2)
primitive degree-15 catalogue:
  A7, PSL(4,2), A15, S15 have nontrivial subdegree 14
  A6 and S6 on two-subsets have nontrivial subdegrees 6,8
proper-factor route:
  r in {1,2,4} forces outer degree 15 to decompose
  right-factor degree 3 or 5 gives endpoint inner degree 12 or 20
  degree 12 is closed; degree 20 violates the source/RH profile
survivor:
  (r,delta)=(8,2), outer monodromy A6 or S6 on 15 two-subsets
  a five-cycle has cycle type 5^3, so the pole profile is compatible
route consequence:
  global independent transverse frontier: 12 -> 9 types
  live types: three at m=2, five at m=3, one at m=4
DAG delta: one PROVED evidence node; critical target unchanged
ledger movement: zero
nonclaims:
  the A6/S6 survivor is not deleted or paid; no owner, bridge, charge,
  u2, cap 68, endpoint, adjacent certificate, or KoalaBear row close
next route-deciding action:
  classify genus-zero A6/S6 degree-15 branch cycles with the printed 5^3
  pole cycle before imposing split source-star incidence
compute spend: exact 720-permutation two-subset audit; no Modal
```

**Same-day `m=4` genus-zero passport reduction:** the remaining outer
`A6/S6` type is reduced from arbitrary degree-15 maps to four exact geometric
passports.

```text
new node: rate_half_kb_m4_a6s6_genus_zero_passport_reduction [PROVED]
upstream custody:
  PR #1132 head: 4e33c7be8b3b29848e0ceb8fd7f50dce45fb2eed
  note/certificate/verifier blobs:
    4aeeebd65f321fcdfe070b6c78f4ce0ca1c501be
    c9be4609a28f4c4b89c099e09a359f833dbf7e1b
    beb62c55287279d095e7162fa2ac2da9ac211fec
  certificate payload:
    c9cfbbf394e479f93d8d8378d886331c8afbbaf338e6fc6b21f55e3e1c485fd7
Riemann--Hurwitz: total index 28; mandatory 5^3 pole costs 12
complete S6 class table: 11 classes reconstructed from all 720 permutations
parity-compatible residual index-16 budgets: 9
product-one generation census:
  five rows generate only order 60 or 120 and are deleted
  four rows generate the required order 360 or 720
retained three-point passports:
  A6: 5.1,2.2.1.1,4.2
  S6: 5.1,2.1.1.1.1,6
  S6: 5.1,2.2.2,3.2.1
retained four-point passport:
  S6: 5.1,2.1.1.1.1,2.2.1.1,2.2.2
A6 split-class audit: both 5-cycle classes agree
primary mutations: 12/12 rejected
independent audit: exact agreement on all tuple counts and subgroup orders
DAG delta: one PROVED evidence node; critical target unchanged
ledger movement: zero
nonclaims: no challenge-field descent, split-fiber payment, source-star
           incidence, m4 deletion, owner, endpoint, or KoalaBear row close
next route-deciding action:
  construct/classify the three rigid covers and test split zero/pole fibers
  plus quartic source-star incidence before the four-point Hurwitz family
compute spend: below one second under tiny RAMguard; no Modal
```

**Same-day first rigid `m=4` normal form:** the rational `S6 [6,5,2]`
degree-six companion has now been normalized in its unordered-pair quotient.

```text
new node: rate_half_kb_m4_s6_652_pair_quotient_normal_form [PROVED]
BelyiDB pin:
  commit 7d5b899b0741ebd505363f7f811e5737e906abee
  blob   454b284b8d09d855b1fde5c86dac2c28859f0f67
pair-curve route:
  quadratic-divisor remainder determinant -> irreducible plane quintic
  projection from its rational triple point -> one rational conic
  exact conic parametrization -> degree-15 rational map
branch fibers:
  zero:     (6,6,3)
  one:      (5,5,5)
  infinity: (2,2,2,2,1,1,1,1,1,1,1)
challenge-field result:
  order-five points = -77, 22+33sqrt(5), 22-33sqrt(5)
  all split over F_(2130706433^6); pole descent cannot delete this passport
verification:
  primary exact reconstruction plus 12/12 hostile mutations rejected
  independent Fraction polynomial/rational-function replay
DAG delta: one PROVED evidence node; critical target unchanged
ledger movement: zero
nonclaims: no split active fiber, quartic source-star incidence, m4 deletion,
           owner, endpoint, adjacent certificate, or KoalaBear row close
next action:
  construct the rigid S6 [5,6,2] and A6 [5,4,2] pair quotients, then impose
  the same-record active-fiber/source-star conditions in all three forms
compute spend: exact degree-six polynomial arithmetic under local RAMguard;
               no Modal
```

**Same-day second rigid `m=4` normal form:** the rational `S6 [5,6,2]`
companion has now been normalized through the cubic adjoints of its
unordered-pair quintic.

```text
new node: rate_half_kb_m4_s6_562_pair_quotient_normal_form [PROVED]
BelyiDB pin:
  commit 7d5b899b0741ebd505363f7f811e5737e906abee
  blob   94cff64a36672ba6bde9e6cbc1fa251230aa8001
normalization route:
  pair-remainder determinant -> irreducible plane quintic
  singular-scheme cubic adjoints plus one infinitely-near tangent
  exact resultant -> five fixed factors and one moving (1,5) factor
  moving point -> degree-15 rational map
branch fibers:
  zero:     (5,5,5)
  one:      (6,3,3,2,1)
  infinity: (2,2,2,2,2,2,1,1,1)
challenge-field result:
  order-five divisor = one Q-point plus two Q(sqrt(5))-points
  all split over F_(2130706433^6); pole descent cannot delete this passport
verification:
  primary exact adjoint/resultant reconstruction; 13/13 mutations rejected
  independent Fraction replay: exact, 0.08 seconds, about 12 MB
DAG delta: one PROVED evidence node; critical target unchanged
ledger movement: zero
nonclaims: no split active fiber, quartic source-star incidence, m4 deletion,
           owner, endpoint, adjacent certificate, or KoalaBear row close
next action:
  construct the remaining A6 [5,4,2] rigid pair quotient over its quadratic
  coefficient field, then impose the shared active-fiber/source-star gates
compute spend: exact low-degree arithmetic under local RAMguard; no Modal
```

**Same-day third rigid `m=4` normal form:** the `A6 [5,4,2]` companion over
`Q(nu)`, `nu^2-nu+4=0`, has now been normalized through both cubic-adjoint
eliminations of its unordered-pair quintic.

```text
new node: rate_half_kb_m4_a6_542_pair_quotient_normal_form [PROVED]
BelyiDB pin:
  commit 7d5b899b0741ebd505363f7f811e5737e906abee
  blob   55e23bc1ef1d939329a5a6b377d03c07f0ac9f2d
upstream custody:
  PR #1132 head: d5c0dc793bc5092561fd43021a52748f17874f72
  note/verifier/certificate blobs:
    6cadaf6cebc4c831be0d88d565c1a103bcb3ac84
    e725fde8875e74d8a2122bc777763167905dbe2a
    8d5c4c18728a2d6ae572f34c91f79147ce9251df
  certificate payload:
    efa96d466a38a43f365e9132ddbbad94b258fd7cfdb613f7e92472529ed66420
normalization route:
  pair-remainder determinant -> irreducible plane quintic over Q(nu)
  rank-eight cubic-adjoint conditions with two tangent constraints
  y- and z-resultants -> unique moving (1,5) factors
  moving coordinates -> degree-15 A6 two-subset map
branch fibers:
  zero:     (5,5,5)
  one:      (4,4,4,2,1)
  infinity: (2,2,2,2,2,2,1,1,1)
challenge-field result:
  nu has both roots in F_2130706433
  the linear-plus-quadratic order-five divisor is distinct for both roots
  all three points lie in F_(p^2), hence in F_(p^6)
  pole descent cannot delete this passport
verification:
  primary exact reconstruction plus 17/17 hostile mutations rejected
  independent Fraction Q(nu)[u] replay of T and T-1
  separate exact adjoint-resultant derivation audit
DAG delta: one PROVED evidence node; critical target unchanged
ledger movement: zero
nonclaims: no split active fiber, quartic source-star incidence, m4 deletion,
           owner, endpoint, adjacent certificate, or KoalaBear row close
next action:
  impose the shared active-fiber/source-star gates on all three rigid maps;
  treat the four-point S6 Hurwitz family as the remaining geometric family
compute spend: bounded exact local algebra under RAMguard; no Modal
```

**Same-day complete `m=4` adjacency-genus exclusion:** the outer orbital
itself has too much genus to be the degree-two image of the actual source
component in every retained passport.

```text
new node: rate_half_kb_m4_adjacency_genus_exclusion [PROVED]
upstream custody:
  PR #1132 head: b60dcda4bc84453aa72c4185c72b351fa345ea40
  note/verifier/certificate blobs:
    899729ccf9632d8df1fe12537fb30e6d02af643b
    a51ccce251177a68645c475044b3768777ca4ee5
    a0b2c8ec260da35ffdefa5a29c7aa5496af5cc79
  certificate payload:
    a0bc909a9e05c097440d318f5fe7aed052387507723fc1f3337172d3e5db7428
source geometry:
  actual outgoing component bidegree (2,4), normalization genus <=3
  birational endpoint self-correspondence component Gamma
  sole m4 type (r,delta)=(8,2), so deg(Gamma->C)=2
outer orbital:
  ordered adjacent two-subsets of six letters, degree 15*8=120
  A6 and S6 both transitive; point-stabilizer subdegrees [1,6,8]
passport index/genus rows:
  S6 [6,5,2]:             index 244, genus 3, source lower bound 5
  S6 [5,6,2]:             index 250, genus 6, source lower bound 11
  A6 [5,4,2]:             index 246, genus 4, source lower bound 7
  S6 four-point family:   index 264, genus 13, source lower bound 25
contradiction:
  p=2130706433 is odd, hence the degree-two map is separable
  Riemann--Hurwitz gives g(Gamma)>=2g(C)-1>3 in every row
route consequence:
  complete independent m4 row is empty
  global independent transverse frontier: 9 -> 8 types
  live types: three at m=2 and five at m=3
verification:
  direct induced-permutation producer plus 12/12 hostile mutations rejected
  independent bit-mask/Burnside fixed-power audit, four of four excluded
DAG delta: one PROVED evidence node; critical target unchanged
ledger movement: zero
nonclaims: no m2/m3 deletion, owner, carrier/data bridge, charge, u2,
           endpoint cap, adjacent certificate, KoalaBear row, or MCA close
next action:
  transport this closure upstream, then attack the eight m2/m3 types using
  actual quartic/source-star incidence rather than source-only rank tests
compute spend: below one second under tiny RAMguard; no Modal
```

**Same-day inner-degree-three primitive-outer router:** every `m=3`
producer is impossible or comes with an inner-degree-two decomposition.

```text
new node: rate_half_kb_m3_primitive_outer_degree2_router [PROVED]
upstream custody:
  PR #1132 head: bf173815d0a51d880c94c833be125769715f2c49
  note/verifier/certificate blobs:
    77b9a0cd08a71fbcce3d2a37151010c3f24fb80a
    c1684fd20cf6d7a7a81d83d1c4b2fec18b1eb136
    24f406d8bdb72d8562c91b28890eae59befd6d91
  certificate payload:
    0f7c0134c723875d66dd19d96f9c68c7299079b5560e63780910afc6d86f21d4
incoming m3 types:
  (r,delta)=(2,6),(3,4),(4,3),(6,2),(12,1)
outer degree: 20
complete primitive catalogue:
  PSL(2,19), PGL(2,19), A20, S20
  all four subdegree rows are [1,19]
consequence:
  no primitive outer map can support any incoming r
  every outer map has a proper right factor d in {2,4,5,10}
composite destinations:
  d=2  -> inner degree 6  -> degree 2 or impossible
  d=4  -> inner degree 12 -> empty
  d=5  -> inner degree 15 -> excluded source profile
  d=10 -> inner degree 30 -> degree 6 -> degree 2 or impossible
route consequence:
  m3 is not an independent producer; no m3 nonexistence is claimed
  global independent transverse frontier: 8 -> 3 types
  live types: m2 with (r,delta)=(2,4),(4,2),(8,1)
classification custody:
  GAP PrimGrp commit 5612e113d50ac23a7d10945383936e20440b4e14
  PRIMGRP[20] exact bytes 342
  SHA-256 cbc9ca7fda9b0de36a4034a4d59e24bb6c07aff0e54458604990919583007133
verification:
  primary exact catalogue/factor/destination audit
  independent PSL(2,19),PGL(2,19) projective-line reconstruction
DAG delta: one PROVED evidence node; critical target unchanged
ledger movement: zero
nonclaims: no m2 deletion, m3 nonexistence, owner, charge, u2, endpoint,
           adjacent certificate, KoalaBear row, or MCA close
next action:
  analyze the forced coarser block systems of an m2 producer together with
  the actual quartic/source-star incidence; primitive degree30 is impossible
compute spend: below one second under tiny RAMguard; no Modal
```

**Same-day inner-degree-two V4 outer-recurrence router:** the three live
types now have exact deck stabilizers and no primitive outer branch, while
the actual coordinate-stabilized source rows acquire a stricter defect
normal form.

```text
new node: rate_half_kb_m2_v4_outer_recurrence_router [PROVED]
upstream custody:
  PR #1132 head: d4063dcd9c56835c3916ef792e263ea720a4d397
  note/verifier/certificate blobs:
    41dc0c3dd72bc9bc2f7d2759ba3c6ac64491cb08
    774a2da946399dc28966e8f300ac9a17e6fed27b
    50d17f218bfa7d3acb211c946db0c025b9a98944
  certificate payload:
    fe8141810501fd7b3762a378210609177185972ec706bf9ac943fa398bd82d39
incoming types:
  (r,delta)=(2,4),(4,2),(8,1)
V4 stabilizer law:
  delta=|Stab_V4(Gamma)|
  (2,4): full V4
  (4,2): one of three order-two subgroups
  (8,1): trivial stabilizer
complete primitive degree-30 catalogue:
  PSL(2,29), PGL(2,29), A30, S30
  all four subdegree rows are [1,29]
outer consequence:
  every outer map has a proper right factor d in {2,3,5,6,10,15}
  endpoint destinations m'=4,6,10,12,20,30
  every destination is impossible or recurrent to m=2
source refinement when tau x 1 stabilizes Gamma:
  preserving source lift is (T,X)->(tau(T),b(X))
  q_i is supported away from both z_i and z_bar(i)
  source-star weights are equivariant
  the weight-three defect type is impossible
  with d double vertices and e fixed matching vertices:
    0<=e<=d<=3 and e=d mod 2
classification custody:
  GAP PrimGrp commit 5612e113d50ac23a7d10945383936e20440b4e14
  PRIMGRP[30] exact bytes 344
  SHA-256 1a923cc8f4428ec22864109cdc60d0c87326e8939cc1d72d217d22df2a4b8da0
DAG delta: one PROVED router; critical target unchanged
ledger movement: zero
nonclaims: no m2 deletion, owner, carrier/data/slope bridge, u2, endpoint,
           adjacent certificate, KoalaBear row, or MCA close
next action:
  write the actual source-coupled equations in the three stabilizer normal
  forms and break the recurrent decomposition tower; do not count another
  return to m2 as progress
compute spend: below one second under RAMguard; no Modal
```

**Same-day full-V4 source-genus drop:** the `(r,delta)=(2,4)` row can no
longer use source genus two or three.

```text
new node: rate_half_kb_m2_r2_full_v4_source_genus_drop [PROVED]
upstream custody:
  PR #1132 head: f6bc4a2b2a6a5b3bba98f24a520c67ca3373dbbb
  note/verifier/certificate blobs:
    d9bafcc62f9c806e0ece3fa9eba4ccb7522b9707
    6b103e5033a70edb9233d097fcf6f51b0526e129
    83e82b826ddfa2f5377e99f439be5f00900507c6
  certificate payload:
    9a2ea090568600356f27f3174aee6d08414217b26dbb8f7922931c64a151122f
input: full V4 stabilizer in the m2 r2 row
source involutions:
  eta = deck involution of Gamma->P1_X
  a   = lift of tau x 1, acting as (tau,b)
  c   = lift of 1 x tau
degree-four source cover:
  Gamma->P1_W has deck group <eta,a>=V4
conjugation:
  c fixes a
  c cannot fix eta without factoring the coefficient map through a
  quadratic source quotient, which is the excluded line/conic branch
  therefore c eta c^-1=eta*a
tame fixed-point result:
  #Fix(eta)=#Fix(eta*a)=2g+2
  #Fix(a)=2-2g
  admissible rows: (g,#Fix(a))=(0,2),(1,0)
route consequence:
  source genus 2 and 3 are empty in (r,delta)=(2,4)
DAG delta: one PROVED narrowing node; critical target unchanged
ledger movement: zero
nonclaims: no rational/elliptic deletion, outer passport, owner, carrier,
           data/slope bridge, u2, endpoint, adjacent certificate, or row
next action:
  derive an actual-source genus lower bound or classify the rational and
  elliptic bidegree-(2,2) outer correspondences
compute spend: exact finite group/fixed-point arithmetic only; no Modal
```

**Same-day r2 dihedral outer-factor reduction:** both source-genus regimes
have rational outer component and a finite four-degree factor list.

```text
new node: rate_half_kb_m2_r2_dihedral_outer_factor_reduction [PROVED]
upstream custody:
  PR #1132 theorem commit: b264da9d3309b7b42ab81a1481778d9d92ca8926
  note/verifier/certificate blobs:
    dc78b8209e263b8cf982fae4e340c84e1c225372
    a4a4156ac4057f3892145851771cc44fc0cec157
    4e389740170515d668ad1057488a484fb43cd104
  certificate payload:
    7f85c8e4bf9c1f324a705058992cd2e082a990feeb648f37189ba78d72df831c
outer genus:
  source g=0 -> C=P1 directly
  source g=1 -> a is a two-torsion translation; c and ac are reflections
                with four fixed points; V4 quotient C=P1
outer factor:
  the two degree-two projections of C have distinct involutions u,v
  <u,v>=D_n is finite because it fixes F(Y)=F(Z)
  F=G composed q_n, q_n a geometric Dickson/Chebyshev map, n|30
six-pole sieve:
  n=2: three generic order-five G poles
  n=3: two generic order-five G poles
  n=5: one generic order-five pole plus one simple totally ramified pole
  n=6: one generic order-five G pole
  n=10,15,30: impossible
source-to-outer branch passports:
  source g=0: inertia a,c,ac over three branch values
  source g=1: inertia c,c,ac,ac over four branch values
DAG delta: one PROVED finite reduction; critical target unchanged
ledger movement: zero
nonclaims: no n=2,3,5,6 deletion, locator realization, owner, carrier,
           data/slope bridge, u2, endpoint, adjacent certificate, or row
next action:
  impose the actual source and active locator divisors on the four dihedral
  factors; do not count their return to m2 as progress
compute spend: exact degree and tame ramification arithmetic only; no Modal
```

**Same-day degree-five dihedral source-star exclusion:** the exceptional
totally ramified pole profile is incompatible with the complete source
defect budget.

```text
new node: rate_half_kb_m2_r2_dihedral_degree5_source_star_exclusion [PROVED]
upstream custody:
  PR #1132 head: fe2a549c8de1de34e5ea331ff4c410145207e381
  note/verifier/certificate blobs:
    68ec312696ae2b6afc12f538e3583a8f032c58b9
    31c3f896c65baf642181405d07f320cf75e5a27f
    ba27da451743fd198efd4b335a0983ed030acbb5
  certificate payload:
    1b711c1cde8f0652ce5e713513955ecdc1789e9fd62c361bca00ae05c9b4c287
input: n=5 inside the full-V4 (m,r,delta)=(2,2,4) row
dihedral pole profile:
  one generic order-five pole of G
  one simple pole of G at the common totally ramified quotient value
source bridge:
  div(B)=psi^*(sum_i [alpha_i])
  h^-1(z_0)={w_+,w_-}, h^-1(y_0)={t_+,t_-}
  D_w=psi^*[w] has degree two for each w
star consequence:
  every point of D_(w_+) and D_(w_-) has star {t_+,t_-}
  total forced weight is 2+2=4
  complete-source defect gives maximum star weight three
result: n=5 is empty; surviving full-V4 factor degrees are {2,3,6}
DAG delta: one PROVED subcase exclusion; critical target unchanged
ledger movement: zero
nonclaims: no n=2,3,6 deletion, other m2 type, owner, charge, u2,
           endpoint, adjacent certificate, KoalaBear row, or MCA close
next action:
  impose the induced two-, three-, and six-cycle incidence on the actual
  source-star equations; do not treat recurrence as endpoint nonexistence
compute spend: exact degree-four weight arithmetic only; no Modal
```

**Same-day degree-two dihedral source-star exclusion:** regular V4 coset
incidence forces more repeated source-star mass than the quartic budget.

```text
new node: rate_half_kb_m2_r2_dihedral_degree2_source_star_exclusion [PROVED]
upstream custody:
  PR #1132 head: 36ed2ac28176fb583cbf15d16f8074b6e8a48de8
  note/verifier/certificate blobs:
    0850c2fc84a9c26bc09b8bdd32425caab0e85bf8
    af95670ec46b4054335e09eee54b98e36eb73150
    a6705b3507014434052c4c5e63209fae2d566038
  certificate payload:
    c3771a0386e955b87f6ec9f4256d9569fb5e9459036653f790691851be0f2a89
input: n=2 inside the full-V4 (m,r,delta)=(2,2,4) row
one generic G-pole:
  q_u fiber has Y-values y_0,y_1
  q_v fiber has Z-values z_0,z_1
  regular D_2=V4 incidence is K_(2,2)
source cross-edge lemma:
  each z has two unramified endpoint lifts w
  each D_w=psi^*[w] is reduced of degree two
  the diagonal lift forces one H-root over each y-value on each source sheet
weight consequence:
  2 Z-values * 2 endpoint lifts * 2 source units = 8 units
  only 2*2=4 cross star vertices are available
  min sum_v binom(w_v,2)=4, attained only at (2,2,2,2)
  complete-source defect budget is 3
result: n=2 is empty; surviving full-V4 factor degrees are {3,6}
DAG delta: one PROVED subcase exclusion; critical target unchanged
ledger movement: zero
nonclaims: no n=3,6 deletion, other m2 type, owner, charge, u2,
           endpoint, adjacent certificate, KoalaBear row, or MCA close
next action:
  analyze orientation compatibility around the n=3 and n=6 incidence
  cycles; the four-vertex pigeonhole no longer applies
compute spend: exact four-point coset and integer defect arithmetic; no Modal
```

**Same-day residual dihedral star-graph rigidity:** the two surviving
factor degrees have unique complete-source graph shapes up to relabeling.

```text
new node: rate_half_kb_m2_r2_dihedral_residual_star_graph_rigidity [PROVED]
upstream custody:
  PR #1132 head: 06a0dcb152687db4017484b215ed851bae52f1f2
  note/verifier/certificate blobs:
    11a974bf417dacdc3366c284f5f96f738137cf12
    7ad80b2d6a457cffb233f371b0f8751244e9138a
    c842c89b0d4978a12d4ede3d12fc040de6d11741
  certificate payload:
    63f6387bba81e51e0a49f409645e9493b3f128f6ab9d119be2dcc64da766b1d4
input: n=3 or n=6 inside the full-V4 (m,r,delta)=(2,2,4) row
generic dihedral incidence:
  reflection quotient incidence is C_(2n)
  every Z value sees a distinct adjacent pair of Y values
source orientation law:
  a:(T,X)->(tau(T),b(X))
  c eta c^-1=eta*a
  if D_w uses {t,s},{tau(t),tau(s)}, then D_(tau(w)) uses
  {t,tau(s)},{tau(t),s}
complete graph:
  n=3: two disjoint K_(2,2,2)
  n=6: two-point blow-up of C_6
  all 24 source-star weights are one
  every one of the 12 source labels has degree four
  complete-source defect is exactly zero
DAG delta: one PROVED rigidity node; critical target unchanged
ledger movement: zero
nonclaims: no n=3 or n=6 existence/deletion, m2 type close, owner, charge,
           u2, endpoint, adjacent certificate, KoalaBear row, or MCA close
next action:
  solve the birational-quartic coefficient realization problem for these
  two exact graphs, using the quadratic source fibers and V4 branch passport
compute spend: exact D3/D6 coset and 24-edge graph arithmetic; no Modal
```

**Same-day residual coefficient-quartic pin:** the source realization is
now one canonical pullback equation, not an arbitrary quartic interpolation.

```text
new node: rate_half_kb_m2_r2_dihedral_residual_coefficient_quartic_pin [PROVED]
upstream custody:
  PR #1132 head: 3efe818561509dcc6f2ae792f2ed1d22c7d317ae
  note/verifier/certificate blobs:
    135c1f300fda1dab365b8a287c5f01f620f2fd20
    2c69f75ef87aa084a9c868dee304b235db06db1c
    8df504a15307d229a9c3de2bb876be89819853cb
  certificate payload:
    ba9783671d9d91bbd345ebaeec4b894d96be9d8d20f1ccc7d7ee1c5847bf6c81
input: either surviving n=3 or n=6 full-V4 profile
sibling correspondence:
  v is the deck involution of C->P1_Z
  p -> (Y(p),Y(vp)) is birational onto a symmetric (2,2) curve K
endpoint normalization: h(t)=t^2, tau(t)=-t
write:
  sigma=y_0+y_1, pi=y_0*y_1
  k=A*pi^2+B*sigma*pi+C*(sigma^2-2*pi)+D*pi+E*sigma+F
source unordered-pair coordinates:
  S=t+s, P=t*s
  sigma=S^2-2P, pi=P^2
exact coefficient image:
  Q(S,P)=k(S^2-2P,P^2)
  Q=A P^4+B S^2P^2-2B P^3+C S^4-4C S^2P
    +(2C+D)P^2+E S^2-2E P+F
actual-existence consequence:
  Q has degree four and equals the irreducible rational coefficient quartic
DAG delta: one PROVED equation pin; critical target unchanged
ledger movement: zero
nonclaims: no n=3 or n=6 existence/deletion, m2 type close, owner, charge,
           u2, endpoint, adjacent certificate, KoalaBear row, or MCA close
next action:
  classify the total-delta-three singular locus and V4 branch passports of
  this six-coefficient quartic, then specialize to D3 and D6
compute spend: symbolic degree-four identity only; no Modal
```

**Same-day residual one-parameter normal form:** the relative endpoint
coordinate is now retained, reducing each residual factor to one parameter.

```text
new node: rate_half_kb_m2_r2_dihedral_residual_one_parameter_quartic_normal_form [PROVED]
upstream custody:
  PR #1132 head: 3efe818561509dcc6f2ae792f2ed1d22c7d317ae
  note/verifier/certificate blobs:
    135c1f300fda1dab365b8a287c5f01f620f2fd20
    2c69f75ef87aa084a9c868dee304b235db06db1c
    8df504a15307d229a9c3de2bb876be89819853cb
  certificate payload:
    ba9783671d9d91bbd345ebaeec4b894d96be9d8d20f1ccc7d7ee1c5847bf6c81
standard dihedral sibling conic:
  x^2+y^2-a*x*y+(a^2-4)=0
  a=-1 for n=3; a=1 for n=6
source branch-place gate:
  the pullback h(T)=Y has exactly two branch places in both source-genus rows
  therefore exactly one branch value of h lies in Br(Y)={2,-2}
  normalize that value to 2 and call the other b, with b notin {2,-2}
target transport:
  m(x)=(x-2)/(x-b), then m composed h=t^2
explicit sibling coefficients:
  A=(a-2)(a-b^2+2)
  B=-(a-2)(2a-b^2-2b+4)
  C=(a-b)^2
  D=4a^2-a*b^2-4a*b-4a+16b-16
  E=-2(a-2)(a-b)
  F=(a-2)^2
result:
  substitute these into the canonical Q(S,P); one parameter b remains
DAG delta: one PROVED normal-form node; critical target unchanged
ledger movement: zero
nonclaims: no irreducibility for arbitrary b, n=3/n=6 deletion, m2 close,
           owner, charge, u2, endpoint, KoalaBear row, or MCA close
next action:
  classify geometric reducibility in b and impose the six pole fibers and
  exact source locators on the irreducible locus
compute spend: exact symbolic coordinate transport only; no Modal
```

**Same-day residual quartic singularity atlas:** coefficient factorization
and genus are now completely classified and delete no allowed parameter.

```text
new node: rate_half_kb_m2_r2_dihedral_residual_quartic_singularity_atlas [PROVED]
upstream custody:
  PR #1132 head: 4cdfa41a1de1360155e3d350a5fe3ec99e9fe94b
  note/verifier/certificate blobs:
    89eb066c787a5c8556151d3acc6d7a39ca00e129
    4af7f4298064d1b62d526f83f150666f1df6f658
    1355c5acace3f031194abf67b227d657132c12b7
  certificate payload:
    e402c17bf8f4757f5b534f3b1a9da5faebafe6ac60956a4849f27f66202b96de
input: Q_(a,b), a in {-1,1}, b notin {-2,2}
quadratic-in-X form, X=S^2:
  discriminant=P^2(alpha P^2+beta)
  alpha=(a-2)(a+2)(b-2)^3(b+2)
  beta=-4(a+2)(a-b)(b-2)^3
constant term:
  M=(a-2)(P+1)^2 N(P)
  disc(N)=4(a+2)(b-2)^2
generic b!=a:
  Q is geometrically irreducible
  singularities: (0,-1) and P=0, S^2=(a-2)/(a-b)
  all three are ordinary nodes; total delta=3
special b=a:
  Q remains geometrically irreducible
  one node at (0,-1), one tacnode of delta two at [1:0:0]
result:
  every allowed coefficient quartic is rational and geometrically viable
  coefficient factorization/genus delete no b
DAG delta: one PROVED atlas node; critical target unchanged
ledger movement: zero
nonclaims: no six-pole/source realization, n=3/n=6 deletion, m2 close,
           owner, charge, u2, endpoint, KoalaBear row, or MCA close
next action:
  parameterize Q_(a,b) and impose the six order-five pole fibers, degree-24
  source locator, and twelve quartic row divisors
compute spend: exact degree-four derivatives and square classes; no Modal
```

**Same-day residual source-cover twist classifier:** the relative second
endpoint is no longer an untracked Mobius parameter at the branch level.

```text
new node: rate_half_kb_m2_r2_dihedral_residual_source_cover_twist_classifier [PROVED]
upstream custody:
  PR #1132 head: 4b722a5f3a03ea3074441553438e212b074de0db
  note/verifier/certificate blobs:
    838c595a8aa1ff9f9c597a8004ab4e9ebcf64953
    9050899a11af3b30f246bdc882a61c8890797565
    715c980aaf20ad2e6d5075ac3cd1da2903af7e79
  certificate payload:
    ec4c0ff7938e4176ba8d5f2a889201b5d683635538a28bed90d86240d4e67313
standard coordinates:
  u(r)=1/r, v(r)=lambda/r, mu^2=lambda
  a=lambda+lambda^-1, d=mu+mu^-1, d^2=a+2
  Z_0=r/mu+mu/r, actual Z=ell(Z_0)
quadratic-cover square class:
  m(Y(r))m(Y(vr))=(Z_0-d)^2/Q_b(Z_0)
  Q_b(z)=z^2-b*d*z+b^2+d^2-4
  W^2=m(ell(Z_0))
forced twist:
  ell^-1({2,b})=roots(Q_b)
branch evaluations:
  Q_b(2)=(b-d)^2, Q_b(-2)=(b+d)^2
genus classifier:
  g(source)=0 iff b^2=a+2
  g(source)=1 iff b^2!=a+2
DAG delta: one PROVED source-cover classifier; critical target unchanged
ledger movement: zero
nonclaims: no common degree-30 function, six-pole/source realization,
           n=3/n=6 deletion, m2 close, owner, charge, or Prize close
next action:
  impose the same degree-30 outer function on both reflection quotients and
  then pull the six order-five poles through the forced twist
compute spend: exact quadratic square classes only; no Modal
```

**Same-day degree-six common-pole exclusion:** the common degree-30 pole
divisor deletes one of the two residual dihedral profiles.

```text
new node: rate_half_kb_m2_r2_dihedral_degree6_common_pole_exclusion [PROVED]
upstream custody:
  PR #1132 head: 5bcb2b2bd0158912cb7319ef386ca2523db5436d
  note/verifier/certificate blobs:
    d7a3183be7e0524b5bf6174f4c9fb6ff2b57f30f
    ef144522020aa9f4ffdf5da08af7fbf77b002aeb
    b6c821cdf89c0e82461ff53216e7a83ac8087ff5
  certificate payload:
    224fbbaf75c0aa830c7fab8e6024a51d3454d7ce3a6260184041983806f1e3fd
input:
  n=6, so all six poles are one generic fiber of each Dickson-six quotient
  source-cover branch pair ell^-1({2,b})=roots(z^2-b*d*z+b^2-1), d^2=3
pole-sextic atlas:
  coincident involutions -> ell=+/-z, plus +/-3/(2z) only at c=27/8
  distinct commuting involutions -> c=27/8, but no second Dickson-six fiber
  order-three involutions -> c=756/125 and ell=+/-g_t,+/-g_t^2,
                              g_t=t(z+t)/(t-3z), 5t^2+27=0
twist elimination:
  reciprocal resultant=22371648 !=0 mod 2130706433
  order-three primitive norm=71132574457861006005
                             =1274367339 mod 2130706433 !=0
result:
  n=6 is empty; n=3 is the sole residual full-V4 dihedral factor profile
DAG delta: one PROVED deletion node; critical target unchanged
ledger movement: zero
nonclaims: no n=3 construction/deletion, m2 close, owner, payment, K3,
           endpoint, KoalaBear row, or Prize close
next action:
  classify six points that are two generic D3 fibers in both forced endpoint
  coordinates, then impose the common degree-ten outer and source locators
compute spend: exact binary-sextic coefficients and 7x7 resultants; no Modal
```

**Same-day degree-three geometric realization fence:** the sole residual
profile survives every abstract geometric gate simultaneously.

```text
new node: rate_half_kb_m2_r2_dihedral_degree3_geometric_realization_fence [PROVED]
upstream custody:
  PR #1132 head: fce150e3323ce37f261b21c19685f4613552dd42
  note/verifier/certificate blobs:
    f989c078611e31965e49c84c16eebd8f5ee47de7
    ea2650fb3fc0b33f2d191559476ec6f7fa9b3ac2
    7adf13b9e343c51d96cdc7c8878cf5bba15c618c
  certificate payload:
    a7f42b038261ea137b2246987dcc398bdddbf807ede6ff46f70429d5a44b2be5
special parameter: a=b=-1, d=-1, ell=identity, source genus zero
explicit maps:
  D3(y)=y^3-3y
  h(t)=(t^2+2)/(1-t^2)
  psi(x)=2/(x^2+1)
  H(t,x)=2(x^2+1)t^2-2x(x^2+3)t+(x^2+1)^2
exact realization:
  H and H(t,-x) pull back the non-diagonal D3 correspondence
  the coefficient map is birational to Q_(-1,-1)
  any two generic D3 pole fibers give six order-five poles
  all twelve row quartics divide the degree-24 complete source form
  sum_alpha div(H(alpha,x))=2 div(B)
result:
  common-function/pole/quartic/genus/star/source geometry cannot delete n=3
  the next gate is the fixed active endpoint pencil or recurrent owner
DAG delta: one PROVED route-fence node; critical target unchanged
ledger movement: zero
nonclaims: no deployed endpoint producer, owner, payment, m2/K3/row close
next action:
  compare the fixed KoalaBear source pencil with the special b=-1 model;
  if compatible, compile the induced degree-six same-record first owner
compute spend: exact rational identities only; no Modal
```

**2026-07-28, E17 cutoff-free route and V=34 endpoint close:** odd diameter
parity reduces the chamber to the one/five-odd atlas. A complete dual census,
the proper-conductor theorem, and dual exact odd-part resultants close every
surviving profile.

```text
starting local pin: 8f211958
canonical prize pin: b60ec497
upstream main pin: b13de8113a03f06b6fc22bbd2f289a8abcdf7e95
node attacked: N=256, folded profile (3,4,0), V=34 (E=17)
failed import app: ap-KqmsjnSeuKSHccRguoGspV; explicitly aborted before any
                   mathematical task and supplies no evidence
reduction app: ap-c8VmO1f95T4RM21QCIoMbA
slack result: L<=11; exactly six energy profiles
majorant policy: not invoked
parity result: (8,0,1) rejected; five one/five-odd survivors
light atlas: 14,664 normalized supports in 11+100=111 affine templates
coverage per engine: 111*binom(124,3)*64=2,203,120,896 vectors
census app: ap-nuzv6imnkUH0ElJlCLyKRy; dual exact engine agreement;
            651.958 aggregate dual worker-seconds
actual profiles: [608,1152,188,92,10], total 2,050
full conductor: [196,272,20,0,0], total 488
proper conductor: complementary 1,562 vectors discharged by theorem
norm app: ap-YS86fN9k5a8svWi6zF2boU; FLINT/PARI agreement on all 488
distinct norms: 108
exact whole-norm maximum: 2816861446662266258222239103326104068711609833031798890850684996153986296836
whole norms at or above 2^250: 16
exact odd-part maximum: 744372174442013450465816409476894770650462784978029532566873973061928116737
strict odd margin: 2*odd_max<2^250<3*odd_max; odd threshold hits 0
result: CLOSED; all five profiles and the V=34 endpoint are PROVED absent
live positive even variance frontier: V<=32
delta-star bracket movement: none; this pays one finite E1 exception chamber
new assumptions: none
upstream terminal delta: none; local result is OURS_ONLY
live compute requests: none for E17; never rerun V>=34
next route-deciding action: derive and price the exact cutoff-free E16/V32
                            router before authorizing any census
```

**2026-07-28, E16 cutoff-free route and V=32 endpoint close:** even diameter
parity reduces the chamber to the zero/four-odd atlas. A complete dual census,
the proper-conductor theorem, and dual exact odd-part resultants close every
surviving profile.

```text
starting local pin: 8770e53e
canonical prize pin: 82e5f4c4
upstream main pin: b13de8113a03f06b6fc22bbd2f289a8abcdf7e95
node attacked: N=256, folded profile (3,4,0), V=32 (E=16)
reduction app: ap-UNOcTGZLQStD1pUQnlIcQG
slack result: L<=10; exactly five energy profiles
majorant policy: not invoked
parity result: (7,0,1) rejected; four zero/four-odd survivors
light atlas: 28,863 normalized supports in 6+148=154 affine templates
coverage per engine: 154*binom(124,3)*64=3,056,582,144 vectors
census app: ap-wX3VHEQgXjopXqefRieIpQ; dual exact engine agreement;
            959.740 aggregate dual worker-seconds
actual profiles: [530,0,158,0], total 688; two routed profiles exactly empty
full conductor: [162,0,16,0], total 178
proper conductor: complementary 510 vectors discharged by theorem
norm app: ap-NKEaivIgiXPWHEwHeBgkkM; FLINT/PARI agreement on all 178
distinct norms: 78
exact whole-norm maximum: 3310692535087337739109785704249356622971820103039851493935549506897278325762
whole norms at or above 2^250: 10
exact odd-part maximum: 1655346267543668869554892852124678311485910051519925746967774753448639162881
strict odd margin: odd_max<2^250<2*odd_max; odd threshold hits 0
result: CLOSED; all four profiles and the V=32 endpoint are PROVED absent
live positive even variance frontier: V<=30
delta-star bracket movement: none; this pays one finite E1 exception chamber
new assumptions: none
upstream terminal delta: none; local result is OURS_ONLY
live compute requests: none for E16; never rerun V>=32
next route-deciding action: derive and price the exact cutoff-free E15/V30
                            router before authorizing any census
```

**2026-07-28, E15 cutoff-free route and V=30 endpoint close:** odd diameter
parity reduces the chamber to the three-odd atlas. A complete dual census, the
proper-conductor theorem, and dual exact odd-part resultants close both
surviving profiles.

```text
starting local pin: 8b7dca21
canonical prize pin: 82e5f4c4
upstream main pin: b13de8113a03f06b6fc22bbd2f289a8abcdf7e95
node attacked: N=256, folded profile (3,4,0), V=30 (E=15)
reduction app: ap-4uZGK1UWEjeAnhVm6de5UE
slack result: L<=9; exactly three energy profiles
majorant policy: not invoked
parity result: (6,0,1) rejected; two three-odd survivors
light atlas: 960 normalized supports in eight affine templates
coverage per engine: 8*binom(124,3)*64=158,783,488 vectors
census app: ap-xIQLyhRtHtlRxbQkOIS7Yp; dual exact engine agreement;
            52.945 aggregate dual worker-seconds
actual profiles: [258,36], total 294
full conductor: [64,0], total 64
proper conductor: complementary 230 vectors discharged by theorem
norm app: ap-4c65PlujVH2D5kNI12Bcac; FLINT/PARI agreement on all 64
distinct norms: 28
exact whole-norm maximum: 3003171528471974836716922425205211633163258783488230570091067301168069285892
whole norms at or above 2^250: 32
exact odd-part maximum: 1263041506267492322130816623667822529962454800313964008196082776100356004097
strict odd margin: odd_max<2^250<2*odd_max; odd threshold hits 0
result: CLOSED; both profiles and the V=30 endpoint are PROVED absent
live positive even variance frontier: V<=28
delta-star bracket movement: none; this pays one finite E1 exception chamber
new assumptions: none
upstream terminal delta: none; local result is OURS_ONLY
live compute requests: none for E15; never rerun V>=30
next route-deciding action: derive and price the exact cutoff-free E14/V28
                            router before authorizing any census
```

**2026-07-28, E14 cutoff-free route and V=28 endpoint close:** even diameter
parity reduces the chamber to the two/six-odd atlas. A complete dual census
and the proper-conductor theorem leave 736 full-conductor vectors. The inherited
odd-part threshold shortcut is false for six vectors, but exact classification
of the three distinct threshold exceptions repairs the route and closes every
surviving profile.

```text
starting local pin: c2689aab
canonical prize pin: 82e5f4c4
upstream main pin: fde7d56d0f2d8f135db4f2226e1978644a6c9f44
node attacked: N=256, folded profile (3,4,0), V=28 (E=14)
reduction app: ap-rxPXBVj2USK33LIXWpg4Lo
slack result: L<=10; exactly four energy profiles
majorant policy: not invoked
parity result: all four survive; two have two odd classes and two have six
light atlas: 288,888 normalized supports in 87+1,234=1,321 affine templates
coverage per engine: 1321*binom(124,3)*64=26,219,123,456 vectors
failed census app: ap-C2U6Lugoj5XbrqQWnS2rLs; remote path initialization
                   failed before any mathematical engine ran; no evidence
census app: ap-rQOuJb9DVQwka46OLEj4Er; dual exact engine agreement;
            7,636.622 aggregate dual worker-seconds
actual profiles: [982,714,100,40], total 1,836
full conductor: [540,184,8,4], total 736
proper conductor: complementary 1,100 vectors discharged by theorem
norm app: ap-A7rhyHWVrOpGoAZM9bOuSs; FLINT/PARI agreement on all 736
distinct norms: 262
exact whole-norm maximum: 5848948255836721605243059534285585250067895734911016890819011517212606236162
whole norms at or above 2^250: 152
exact odd-part maximum: 2924474127918360802621529767142792625033947867455508445409505758606303118081
odd threshold hits: 6 vectors, 3 distinct odd parts, all below 2^251
shortcut outcome: FALSIFIED; odd_max<2^250 is false at E14
candidate app: ap-JtCD7equumzMV4qV44ziGe; exact PARI/FLINT agreement;
               all 3 distinct threshold odd parts are composite
eligible pair-feasible prime candidates: 0
result: CLOSED; all four profiles and the V=28 endpoint are PROVED absent
live positive even variance frontier: V<=26
delta-star bracket movement: none; this pays one finite E1 exception chamber
new assumptions: none
upstream terminal delta: none; local result is OURS_ONLY
live compute requests: none for E14; never rerun V>=28
next route-deciding action: derive and price the exact cutoff-free E13/V26
                            router before authorizing any census
```

Upstream reconciliation at `fde7d56d` adds an independent replay of the four
certified Proth prime rows. Its own contract is confirmation-only and moves no
mathematical frontier, so it creates no E14 DAG edge. It is bankable submission
dossier evidence and independently pins the load-bearing rule that `r_quad`
must be located by the exact sign condition rather than the naive printed
integer-square-root formula, which is one too large in three of four rates.

**2026-07-28, E13 cutoff-free route and V=26 endpoint close:** odd diameter
parity reduces the chamber to the one/five-odd atlas. A complete dual census
and the proper-conductor theorem leave 136 full-conductor vectors. Four odd
parts cross the simple threshold, but exact classification of their two
distinct values closes every surviving profile.

```text
starting local pin: 8793e891
canonical prize pin: c90a724be07c3dc76bbc33e35b41d92504dd9a09
upstream main pin: fde7d56d0f2d8f135db4f2226e1978644a6c9f44
node attacked: N=256, folded profile (3,4,0), V=26 (E=13)
reduction app: ap-i2oKjwTWqN24exJmrNCPtQ
slack result: L<=9; exactly four energy profiles
majorant policy: not invoked
parity result: all four survive; two have one odd class and two have five
light atlas: 14,664 normalized supports in 11+100=111 affine templates
coverage per engine: 111*binom(124,3)*64=2,203,120,896 vectors
census app: ap-AhqC0lLGj9BYMLmRpKa1mj; dual exact engine agreement;
            613.766 aggregate dual worker-seconds
actual profiles: [418,252,104,46], total 820
full conductor: [112,0,16,8], total 136
proper conductor: complementary 684 vectors discharged by theorem
norm app: ap-cXvEeUhd1ym0Ep1InsluxC; FLINT/PARI agreement on all 136
distinct norms: 36
exact whole-norm maximum: 4937981356753691307652038461254907642619144628263052811320856547919621259264
whole norms at or above 2^250: 112
exact odd-part maximum: 2099233185140600860850973089797376067771315496789913419840767568645748406017
odd threshold hits: 4 vectors, 2 distinct odd parts, all below 2^251
candidate app: ap-a4p98JmkMEXvNaIRL7bXzV; exact PARI/FLINT agreement;
               both distinct threshold odd parts are composite
eligible pair-feasible prime candidates: 0
result: CLOSED; all four profiles and the V=26 endpoint are PROVED absent
live positive even variance frontier: V<=24
delta-star bracket movement: none; this pays one finite E1 exception chamber
new assumptions: none
upstream terminal delta: none; local result is OURS_ONLY
live compute requests: none for E13; never rerun V>=26
next route-deciding action: reconcile the square-mass scope question before
                            authorizing any E12/V24 computation
```

Canonical reconciliation at `c90a724b` identified square mass, not raw swap
distance, as the collision coordinate and exposed three additional `S=16`
splits outside this descent's `(3,4)` scope. The strengthened local node
`e1_collision_square_mass_reparametrization` now resolves its caveats:

```text
canonical precursor: 0acf7e8fc48666f0baa98ece396de7095bc496a0
canonical correction: c90a724be07c3dc76bbc33e35b41d92504dd9a09
local starting pin: 1c02fea6
class coordinate: alpha=sum_i(x_i-y_i)zeta^i
square mass and height: S=4a+b, H=2a+b
exact support bound: T=min(ell,2h-ell), H<=2T, even S<=4T
official finite ranges: S<=260 at N=256,ell=65; S<=132 at ell=33
S=16 feasibility: (3,4), (2,8), (1,12), (0,16) all realized at ell=33,65
all-even split: (4,0) excluded after division by two
canonical wording repair: raw distance is not unbounded at fixed N
N=512 correction: the norm floor leaves s>=2; the proved s=2 band close then
                      advances that lane to s>=3
status movement: none; this is a PROVED route-scope correction
compute decision: E12/V24 is paused; no Modal census authorized
next route-deciding action: prove an aggregate incidence/direct-image bound
                            or a finite coefficient-type reduction across the
                            exact square-mass ranges
```

Nothing in E13 is retracted: its statement is explicitly restricted to folded
profile `(3,4,0)`. The new constructions show that the other three `S=16`
splits are genuine official-size class-pair profiles, rather than artifacts
removed by the missing `ell` constraint. Since the consumer asks for the
aggregate allowance `P<=K-B*-1`, proving collision-freeness endpoint by
endpoint in a single profile is no longer the preferred route.

**2026-07-28, E1 aggregate max-fiber compiler:** the exact Euclidean Plotkin
identity converts low-square-mass collision-graph coloring into a direct E1
payload.

```text
starting local pin: 449d2662
proved node: e1_low_square_mass_plotkin_coloring_compiler
open node: e1_official_low_square_mass_collision_coloring
graph vertices: antipodal-rearrangement classes X_ell
graph edges: equal reduced E1 value and 0<S<=2ell
Plotkin color-class cap: ell+1
fiber cap under c colors: c(ell+1)
largest sufficient color counts, RowC rates 1/4,1/8,1/16:
  3268165922105543787, 210, 18885148505476
largest sufficient color counts, prize rates 1/4,1/8,1/16:
  54730211038721500, 3, 316259390691
binding row: prize rate 1/8, N=256, ell=33, S<=66
binding statement: chi(G_p(33))<=3
binding fiber cap: 102
exact image floor: 372561980747787012946133646668959839245 > B*
stronger sufficient statement: maximum low-mass collision degree <=2
falsifier: an admissible row with a certified four-chromatic subgraph
delta-star bracket movement: none; compiler proved, coloring premise open
new assumptions: none
compute decision: no broad census authorized; seek a color invariant or a
                  compact four-chromatic witness first
upstream placement: finite constants-first analogue of (Q) max-fiber flatness
```

This route bypasses the stronger `P<=K-B*-1` pair-incidence target. It does
not require injectivity and permits many modular collisions; only the
low-square-mass collision graph must satisfy its row-specific color cap.

**Same-day aggregate strengthening:** colorability is not the weakest usable
premise. Counting low-mass edges and applying the same variance identity
fiber-by-fiber gives an exact second-moment compiler.

```text
additional open node: e1_official_low_square_mass_pair_budget
per-fiber inequality: r_y^2 <= (ell+1)r_y + C e_y
global inequality: sum_y r_y^2 <= (ell+1)K + C E_low
C on RowC: 52 at N=256,ell=33; 116 at N=256,ell=65; 64 at N=512,ell=33
C on prize rows after field floor: 50, 114, 62 respectively
binding prize-rate-1/8 E_low cap:
  65127585921474870475467050631501738502567
relative cap: approximately 1.713824215 K
simple sufficient theorem: maximum low-mass collision degree <=3
comparison: degree <=2 pays both coloring and pair-budget routes; degree <=3
            pays the preferred pair-budget route
currency guard: unordered class pairs, not normalized vectors/orbits
next route-deciding action: bound common-prime low-mass neighbors of one class
```

This target is strictly more tolerant than the three-color route and much more
tolerant than full injectivity. High-square-mass collisions need no separate
enumeration: their contribution is absorbed by the Plotkin/Cauchy second
moment inequality.

**Same-day exact vector dictionary:** the aggregate edge count is now
translated without loss into the folded-kernel currency used by the existing
norm and orbit machinery.

```text
proved node: e1_low_square_mass_weighted_kernel_dictionary
exact identity: E_low=(1/2) sum_d M_ell(a(d),b(d))
M_ell: exact ordered class-pair multiplicity of one oriented folded vector
binding eligible profiles after prize field floor: 271
binding maximum-weight live profile: (a,b,S)=(4,2,18)
binding maximum live weight: 1873053318886373426584792000465260242
uniform sufficient oriented-vector cap: |D_p(33)|<=69541
preferred target: the weaker exact profile-weighted sum, not the uniform cap
orbit guard: restore orientation, stabilizers, and M_ell after normalization
status movement: none; dictionary PROVED, pair budget remains TARGET
compute decision: no census launched; first assemble proved zero profiles and
                  exact surviving orbit weights from existing certificates
```

This removes the previous ambiguity between normalized relation vectors and
actual class-pair edges. The subsequent proved prize-field-floor exclusion
uses `p>2^255` and norm parity to delete `S<=16` at `N=256` and `S<=4` at
`N=512`; RowC is unchanged. It also improves the stopping rule for a future
binding-row census: 69,541 oriented vectors suffices under worst-case live
weights, while larger inventories can still pay through the exact weighted
ledger.

**Same-day leading-profile cofactor sharpening:** combining the existing
local-reciprocity theorem with the exact prize lower endpoint gives

```text
leading binding profile: (4,2,S=18)
norm bound: R<=18^64
prize cofactor bound: m=R/p<=2013
local form: m=2^mu(1+256t), mu in {1,2,4,8,16}
field-floor cofactors: {2, 514, 1026, 1538, 4, 1028, 16, 256}
residue-degree exclusion: 1026=2*3^3*19
exact live prize cofactors: {2, 514, 1538, 4, 1028, 16, 256}
atlas contraction: 419 -> 7 on prize rows
RowC: unchanged at 419
next action: price the seven prize classes before any broad support census
```

**Same-day leading-profile variance/cofactor windows:** exact autocorrelation
parity and a row-specific logarithmic norm deficit now refine those seven
classes without a support census.

```text
proved node: e1_prize_n256_s18_variance_cofactor_windows
profile: N=256, (a,b,S)=(4,2,18)
variance: V=2E with exactly one odd positive autocorrelation coefficient
congruence: E=1 mod 4, hence V=2 mod 8
pointwise majorant:
  log x <= log 18+(x-18)/18-(x-18)^2/2367 on 0<x<=100
exact V=2 norm: R=L_(64/2^t)^(2^t),
  L_0=2, L_1=18, L_n=18L_(n-1)-L_(n-2)
V=2 verdict: excluded against the exact prize interval in all four 2-adic rows
cofactor 1538: eliminated
cofactor 1028: only V in {10,18}
other residual upper bounds:
  m=514 -> 50; m=256 -> 74; m=16 -> 178; m=4 -> 226; m=2 -> 250
all residuals: 10<=V and V=2 mod 8
live prize cofactors: 7 -> 6
RowC movement: none
compute: no Modal run and no numerical estimate; exact rational replay only
status movement: pair-budget TARGET remains open
next action: classify or exclude the two m=1028 chambers before broadening to
             the other five cofactors; preserve weighted edge multiplicities
```

**Same-day cofactor-1028 close:** the two residual chambers are now exhausted
by independent complete normalized engines.

```text
proved node: e1_prize_n256_s18_m1028_collision_exclusion
normalization: singleton positions 0,2; first singleton sign +1
support choices: binom(126,4)=10009125
signed normalized vectors: 320292000
primary engine: folded 15-pair autocorrelation, greedy balanced shards
audit engine: full 128-slot convolution, lexicographic modulo shards
primary Modal app: ap-EI0gpqKTVVsnR6sCbXZfB3
audit Modal app: ap-52RCxiNtu4Oqe2G36sJqfJ
aggregate worker-seconds: 11.552424 + 28.775821
V=10 count: 0
V=18 count: 16
V=18 norms divisible by 257: 0
cofactor conclusion: 1028=4*257 impossible
live prize cofactors: {2,514,4,16,256}
RowC movement: none
pair-budget status: TARGET; normalized emptiness is not an edge census
next action: attack m=514 in its six admissible chambers V=10,18,26,34,42,50
```

**Same-day cofactor-514 close:** the six residual chambers are exhausted, with
the divisor survivors paid by dual exact whole norms.

```text
proved node: e1_prize_n256_s18_m514_collision_exclusion
normalization: singleton positions 0,1; first singleton sign +1
signed normalized vectors: 320292000
primary census app: ap-F9OHvyBufk7R438gPvcJt1
audit census app: ap-3WkMulO32Zeoqs4U19PRBS
counts by V=10,18,26,34,42,50: 0,16,8,88,88,232
257-divisible counts: 0,4,4,48,40,88
divisor-surviving vectors: 184
FLINT norm app: ap-WpzlLsJtyHMAqRXNX4zt5K
PARI audit app: ap-BGNiOCyf6mVdcovdSsUgS0
exact-resultant agreement: 184/184
distinct whole norms: 46
candidate quotients Norm/514 in prize interval: 0
maximum quotient: 66082262884856162162140234757894655654959953149381163882659090799481192796929
cofactor conclusion: 514 impossible
live prize cofactors: {2,4,16,256}
RowC movement: none
pair-budget status: TARGET
next action: attack m=256 in V=10,18,26,34,42,50,58,66,74
```

**Same-day cofactor-256 close:** the nine residual chambers are exhausted and
their exact norms form a certified gap around the prize interval.

```text
proved node: e1_prize_n256_s18_m256_collision_exclusion
normalization: singleton positions 0,8; first singleton sign +1
signed normalized vectors: 320292000
primary census app: ap-GLhkTmrhb9jYJYJwyLWxYJ
audit census app: ap-geY02XirYKUn755jIDegx3
counts by V=10,18,26,34,42,50,58,66,74:
  0,28,52,204,212,864,956,15364,3076
residual vectors: 20756
FLINT ledger app: ap-qOUwcG4vpXLacPHsbUgmcn
PARI audit app: ap-ORclHKC4a7qVqguTzELasP
exact-resultant commitment agreement: 32/32 shards, 20756/20756 rows
V=18 quotients: all above prize interval
V>=26 quotients: all below prize interval
candidate quotients in prize interval: 0
maximum below: 79966870433624456578392518772995331447805526474703846245310288507286369992961
minimum above: 127117908459354031873489386413391045324297956117263458825602208201263580806401
cofactor conclusion: 256 impossible
live prize cofactors: {2,4,16}
RowC movement: none
pair-budget status: TARGET
next action: seek an analytic/census split for m=16; its 22 variance chambers
             are too broad for an unscoped whole-norm dump
```

**Same-day cofactor-16 high-variance close:** a profile-specific chord ledger
and a layered third moment produce the requested analytic/census split.

```text
proved node: e1_prize_n256_s18_m16_high_variance_exclusion
raw chord magnitudes: six 4s, eight 2s, one 1
profile inequality: 4L<=E+35, where E=V/2
quadratic-majorant close: V=138,146,154,162,170,178
V=130 layer profiles: 73
third-moment caps: 4702 at V=114, 5118 at V=122, 5950 at V=130
cubic Hermite contacts: (15,62) at V=114,122; (15,66) at V=130
exact field-floor threshold used: 2^(1299/5)<16p_min
m=16 residual: 10<=V<=106, V=2 mod 8
planning census app: ap-xUAM32cidKtQXwQEyFjKZM
planning census: all 320292000 normalized vectors, counts and (E,L) only
audit census app: ap-PPOc61mOxwR0pClp4jTjwI
dual count and (E,L) agreement: exact in every cell
nonzero vectors through V=106: 540332
load-bearing computation: none; theorem verifier uses exact rational arithmetic
live prize cofactors: {2,4,16}
pair-budget status: TARGET
next action: stream exact norms only for the 540332 low-variance vectors
             without storing a raw multi-gigabyte witness packet
```

**Same-day cofactor-16 close:** the bounded residual is exhausted without a
stored witness or norm dump.

```text
proved node: e1_prize_n256_s18_m16_collision_exclusion
normalization: singleton positions 0,4; first singleton sign +1
dual census universe: 320292000 signed normalized vectors
residual vectors through V=106: 540332
FLINT stream app: ap-6Mx4ggc8xnWQiKXHn8Nin3
PARI/direct-convolution audit app: ap-iL2Um5gs93niNlF87WvgLp
FLINT worker-seconds: 138.08322434
PARI worker-seconds: 875.875521412
exact multiset agreement: 64/64 fingerprint buckets
quotients below prize interval: 540024
quotients inside prize interval: 0
quotients above prize interval: 308
maximum below: 104797259883500113680505745049174573490076600644557179823872590464045041710081
minimum above: 109148549668884138628080445927205579649397021264609510361461809939220006348801
cofactor conclusion: m=16 impossible
live prize cofactors: {2,4}
pair-budget status: TARGET; normalized vectors are not weighted edges
next action: seek an analytic/census split for m=4 before any exact norm run;
             its current 28 chambers through V=226 are too broad to stream
```

**Same-day cofactor-4 high-variance close:** exact third moments and analytic
majorants isolate a small residual without a broad resultant run.

```text
proved node: e1_prize_n256_s18_m4_high_variance_exclusion
profile inequality: 4L<=E+35, with L=E mod 2
dual exact M3 frontier: every chamber V=10,18,...,162
primary direct-convolution app: ap-FWSBvehhSdCJZMGDPjEIab
audit folded-pair app: ap-TNwtdWkeeVT1yPGaLxB941
exact M3/Hermite close: V=82,90,...,162
universal-layer close: V=170,178,186,194
quadratic-majorant close: V=202,210,218,226
exact threshold: (4p_min)^5>2^1289
m=4 residual: 10<=V<=74, V=2 mod 8
load-bearing compute: two exact M3 maxima packets, about 69 worker-seconds
corroborating counts app: ap-OKdHMMiWlBCDidicP9701v
next action: stream exact norms only for the 21376 residual vectors
```

**Same-day cofactor-4 close:** the bounded residual has an exact certified gap
around the prize interval.

```text
proved node: e1_prize_n256_s18_m4_collision_exclusion
normalization: singleton positions 0,2; first singleton sign +1
residual vector count: 21376
FLINT stream app: ap-cqeedeWfHi2ZWPpADOVg8o
PARI/direct-convolution audit app: ap-UrU14R9jlfWWM2B50i9jwk
exact multiset agreement: 64/64 fingerprint buckets
quotients below prize interval: 20604
quotients inside prize interval: 0
quotients above prize interval: 772
maximum below: 107716387476569755844902778849041509815310757677547440774146432592221447900929
minimum above: 110553665570163478885905819698234426068541015284212878175575978480389082393089
cofactor conclusion: m=4 impossible
live prize cofactors: {2}
pair-budget status: TARGET; normalized vectors are not weighted edges
next action: derive the cheapest analytic/census split for the sole m=2 branch
```

**Same-day cofactor-2 high-variance close:** the same moment machinery reaches
the last cofactor after a single bounded dual frontier.

```text
proved node: e1_prize_n256_s18_m2_high_variance_exclusion
normalization: singleton positions 0,1
dual exact M3 frontier: every chamber V=10,18,...,194
primary direct-convolution app: ap-2SrwvNtxlhfJ2USNVd5yvn
audit folded-pair app: ap-uGeZVekDHwri0h2YdtA6yH
exact M3/Hermite close: V=106,114,...,194
universal-layer close: V=202,210,...,250
exact threshold: (2p_min)^5>2^1284
m=2 residual: 10<=V<=98, V=2 mod 8
dual frontier worker-seconds: 94.92468 + 58.20173
next action: stream exact norms only for the 511272 residual vectors
```

**Same-day cofactor-2 close:** the final leading-profile cofactor has an exact
certified gap around the prize interval.

```text
proved node: e1_prize_n256_s18_m2_collision_exclusion
residual vector count: 511272
FLINT stream app: ap-5RZLHmXH21jJetiYlXEvLU
PARI/direct-convolution audit app: ap-Hcr26R9gJ1DnC1bLMkYf5f
exact multiset agreement: 64/64 fingerprint buckets
quotients below prize interval: 510396
quotients inside prize interval: 0
quotients above prize interval: 876
maximum below: 107768200285002421852540903242682983183211082719077647662104106067449092858113
minimum above: 108175736216610979727225685018558899952758788007302660274771396038641324156161
cofactor conclusion: m=2 impossible
leading profile conclusion: every prize cofactor of (4,2,S=18) is impossible
pair-budget status: TARGET; later profiles and weighted edges remain open
next action: recompute the maximum-weight live profile before another census
```

**Same-day leading-profile synthesis:** the sibling cofactor certificates are
now assembled into a zero contribution and a sharper aggregate interface.

```text
proved node: e1_prize_n256_s18_profile_exclusion
exhausted prize cofactors: {2,514,1538,4,1028,16,256}
excluded profile: (a,b,S)=(4,2,18)
old maximum weight: 1873053318886373426584792000465260242
remaining eligible profiles: 270
new maximum profile: (a,b,S)=(3,6,18)
new maximum weight: 1386246316188473270092082114587711840
old sufficient oriented-vector cap: 69541
new sufficient oriented-vector cap: 93962
next integer 93963: not certified by the uniform inequality
RowC movement: none; its 419 (4,2) cofactor classes remain
pair-budget status: TARGET
next action: seek structural/norm exclusion or exact weighted pricing for
             (3,6,S=18) before any broad census
```

**Same-day profile-(3,6) arithmetic reduction:** the new maximum-weight
profile now has a finite, profile-specific interface without a support-9
census.

```text
proved node: e1_prize_n256_s18_profile_36_cofactor_windows
profile: (a,b,S,H)=(3,6,18,12)
binary multiplicities after the cofactor bound: {1,2,3,4,5,6,8,9,10}
exact prize cofactors: {2,4,8,16,32,64,256,512,514,1024,1028,1538}
variance parity: positive even; V=2 excluded by the one-lag Lucas resultant
widest residual: m=2, 4<=V<=350 even
short residuals: m=1024,1028 through V=34; m=1538 through V=12
tight first attack: m=1538 and V in {4,6,8,10,12}
Modal audit: ap-NgXdlPnSNBEljttQ9JDVKa, peak child RSS 56 MB
compute decision: no broad support-9 vector or norm census authorized
pair-budget status: TARGET
```

**Same-day profile-(3,6) cofactor-1538 close:** low variance plus exact
2-adic multiplicity reduces the shortest branch to a finite affine/XOR
classification, which is empty.

```text
proved node: e1_prize_n256_s18_profile_36_m1538_exclusion
cofactor: 1538=2*769, hence mu=1
residual energies: E in {2,3,4,5,6}
normalized singleton supports examined: 10009125
mu=1 normalized supports: 5005539
low-parity normalized supports: 27207
affine support orbits: 1969
singleton sign assignments: 63008
low-energy targets: 2216832
primary pair-plus-third XOR probes: 270453504
dual-agreed heavy supports: 16970
dual-agreed exact sign tests: 135760
verdict: no E=2,...,6 vector; m=1538 excluded
sharp boundary witness: mu=1 and E=8
remaining profile-(3,6) cofactors: 11
next attack: m=1024 (mu=10) and m=1028 (mu=2), both V<=34
Modal apps: ap-uv42wkp1cTBp9rokMZmOhz, ap-h8WimpUO8BNNLmCdSdcHi8,
            ap-B2YnLr5w19DoYthf4ZrHVO
```

**Same-day sharp product contraction and cofactor-1024 close:** replacing the
global pointwise logarithmic majorant by the exact fixed-mean/fixed-variance
product extremum turns both short branches into the existing low-energy
classification problem.

```text
proved node: e1_prize_n256_s18_profile_36_sharp_product_window
moment data: 64 positive values, mean 18, average squared deviation V
extrema: at most two values, indexed by lower multiplicity j=1,...,63
exact comparisons: 649 rational chambers for even 14<=V<=34
tight chamber: (V,j)=(14,63)
boundary audit: the V=12 envelope remains above the m=1024 floor
new windows: m=1024,1028 both V in {4,6,8,10,12}
exact certificate Modal app: ap-VUumIAvKygC1l5swGhdI4j

proved node: e1_prize_n256_s18_profile_36_m1024_exclusion
cofactor: 1024, hence mu=10
normalized singleton supports: 10009125
mu=10 supports: 32256; low-chord supports: 800; affine orbits: 68
singleton sign assignments: 2176
low-energy targets: 194816
dual-agreed heavy supports: 606; exact sign tests: 4848
verdict: no E=2,...,6 vector; m=1024 excluded
primary/audit Modal apps: ap-K9JXDDlMQ9euS1aFcApP20,
                          ap-oC0W1HKzJDE4lP3amswBRW
remaining profile-(3,6) cofactors: 10
next attack: m=1028; geometry has an E=5 witness, so test factor 257 exactly
```

**Same-day cofactor-1028 close:** the exact `mu=2` geometry is nonempty but
the engineered split prime removes every surviving vector.

```text
proved node: e1_prize_n256_s18_profile_36_m1028_exclusion
cofactor: 1028=4*257, hence mu=2
normalized singleton supports: 10009125
mu=2 supports: 2503715; low-chord supports: 20167; affine orbits: 1603
singleton sign assignments: 51296
low-energy targets: 2409344
dual-agreed heavy supports: 89224; exact sign tests: 713792
geometry: E=2,3,4,6 empty; exactly 16 normalized E=5 vectors
arithmetic: all 16 fail all 128 primitive-root tests modulo 257
verdict: m=1028 excluded
primary/audit Modal apps: ap-9YPE5CXuy9YJlmbb8kOTTL,
                          ap-vPJTFiYL24oRxWpxi0C7f1
remaining profile-(3,6) cofactors: 9
next attack: sharpen m=512,514 windows before any larger census
```

**Same-day all-cofactor bounded product contraction:** retaining the exact
pointwise cap `y_u<=144` classifies every product extremum by an upper-cap
count and at most two interior levels.

```text
proved node: e1_prize_n256_s18_profile_36_bounded_product_windows
extremum parameters: capped count k=0,...,7 and lower multiplicity j
exact rational comparisons: 11023
new inclusive variance endpoints:
  m=2:284, m=4:266, m=8:254, m=16:216, m=32:170,
  m=64:130, m=256:60, m=512:34, m=514:34
boundary audit: every preceding even variance survives this envelope
route probe/exact Modal apps: ap-fjMSdUdXuYdwoI9NyoCnUx,
                              ap-9bABu2qYhJVmkjNPhYzzKi
remaining profile-(3,6) cofactors: 9
next attack: m=512,514 in E=2,...,17; spend mu=9/mu=1 structure first
```

**Same-day cofactor-512 close:** multiplicity nine leaves a complete
radius-two mod-four search, and the surviving geometry misses the prize
interval arithmetically.

```text
proved node: e1_prize_n256_s18_profile_36_m512_exclusion
cofactor: 512, hence mu=9
complete energy window: E=2,...,17
normalized singleton supports examined: 10009125
mu=9 supports: 46592; affine orbits: 2912
singleton sign assignments: 93184
dual-agreed heavy supports: 438120; exact sign tests: 3504960
geometry: E=2,...,14 and E=16 empty; two vectors each at E=15 and E=17
arithmetic: FLINT and PARI agree on two exact norms for all four vectors
interval test: every quotient Norm/512 is below the prize interval
verdict: m=512 excluded
primary/audit/norm Modal apps: ap-hLsGuIj8T1KeuCPO9qIbK0,
                               ap-MomSd3tk9h6HHpILMXlCCx,
                               ap-YfWdAsOXwmHsyMSwhUZx6G
remaining profile-(3,6) cofactors: 8
next attack: m=514, with mu=1, E=2,...,17, and required factor 257
```

**Same-day energy-adaptive product contraction and adversarial route cut:**
integer autocorrelation supplies a variance-dependent conjugate cap, while
direct search falsifies two tempting but false modular-emptiness premises.

```text
proved node: e1_prize_n256_s18_profile_36_energy_adaptive_product_windows
analytic cap: y_u<=min(144,18+V), from L1(A)<=sum A_d^2=E=V/2
exact rational comparisons: 6273
new endpoints: m=256 has V<=46; m=514 has V<=22
imported mu=1 geometry: E=2,...,6 empty
parity-adaptive exclusions: (E,q)=(9,1),(10,2),(11,3),(11,7)
live m=514 chambers:
  (7,3),(7,7),(8,4),(8,8),(9,5),(9,9),(10,6),(10,10),(11,11)
certificate Modal app: ap-Jj1DnCEMdtU9oUi9fn6Lfb

falsified premise 1: factor 257 makes the E<=17 geometry empty
falsified premise 2: factor 257 forces E>=17
64-shard search: 5 witnesses, including one E=15 and four E=17
dual exact norms: all five Norm/514 quotients below the prize interval
search/norm Modal apps: ap-vCwCehrnyit7WrDEjorD0c,
                        ap-dle2qIanefNmtFx0fwT8nL
remaining profile-(3,6) cofactors: 8
next attack: exact factor-257 generation on the nine live m=514 chambers
```

**Same-day cofactor-514 close:** one radius-zero/radius-one engine covers all
nine live parity chambers, and two pair-table implementations agree exactly.

```text
proved node: e1_prize_n256_s18_profile_36_m514_exclusion
normalized singleton supports: 10009125
mu=1 supports: 5005539
live-stratum affine orbits: 123196
singleton sign assignments: 3942272
XOR probes: 922886080
candidate heavy supports: 883718
exact sign tests: 7069744
geometry: E8=4, E10=8; E7=E9=E11=0
factor-257 vectors: E8=2, E10=6
dual exact norms: 8 vectors, 4 distinct values, all Norm/514 below interval
verdict: m=514 excluded
atlas/primary/audit/norm Modal apps:
  ap-gX6SKtHGEzPG5OuzLcpd1h, ap-NJLlyLTa70dm5hmYYVcVW5,
  ap-qzMuyQt7EFP3pOzN8qvKaI, ap-99pSDfbXkeWx7pGRNKyEmf
remaining profile-(3,6) cofactors: 7
next attack: m=256, with mu=8 and E=2,...,23
```

**Same-day cofactor-256 close:** exact magnitude partitions and a complete
radius-three-or-less affine census remove the next branch.

```text
proved node: e1_prize_n256_s18_profile_36_m256_exclusion
exact product comparisons: 27176
product ledger: 45 live and 45 excluded (E,q,L) triples
all E=21,22,23 chambers excluded
normalized singleton supports: 10009125
mu=8 supports: 87856
affine orbits: 5920
singleton sign assignments: 189440
third-position queries: 23111680
candidate heavy triples: 2833260
exact sign tests: 22666080
product-live vectors: 54
energies: E13=8, E15=6, E17=12, E19=28
dual exact norms: 54 vectors, all valuation 8 and Norm/256 below interval
product/atlas/primary/audit/norm Modal apps:
  ap-mSa4smR2wCUZpmzvRBDzGA, ap-Q5KgAzAsdxFUQkjKY7WQHd,
  ap-N80auy8zzX09hKkYkuPnQu, ap-lHpPMgDmUlXSI5hWrdSzHP,
  ap-dCD2CvCih4t6ERJB6wOGuC
remaining profile-(3,6) cofactors: 6
next attack: m=64, with mu=6 and E=2,...,65
```

**Same-day cofactor-64 close:** exact product chambers and two complete affine
atlases remove the multiplicity-six branch. A primitive-only draft was not
promoted: audit identified the missing all-one-parity singleton supports, and
the final proof exhausts that branch after division to multiplicity three in
`Z/64`.

```text
proved node: e1_prize_n256_s18_profile_36_m64_exclusion
exact product comparisons: 128228
product ledger: 255 live and 837 excluded (E,q,L) triples
all E=47,...,65 chambers excluded
primitive atlas: 8256 affine orbits
all-one-parity atlas: 4480 affine orbits
combined affine orbits: 12736
singleton sign assignments: 407552
dual-agreed unique radius triples: 10179448632
exact sign tests: 81435589056
product-live vectors: 7191566
certified norm intervals: 7191424 below, 142 above, 0 unresolved
product/primitive-atlas/root/primary/audit Modal apps:
  ap-vGLCNU73MLJj9RDeI3qeG2, ap-jsMfCK4V0ZOgCMYLHX8R7R,
  ap-LWtv7vAuj73JwMclHhmQee, ap-Ku7oS4IA5YTB6bMTAD68xf,
  ap-8NxLniYGvXr1XY60JB2Rbb
all-one-parity atlas/primary/audit Modal apps:
  ap-AZqE2K0OIwaJ72JJ8NC3JR, ap-8bHvHbIdNO7uEIZAXHJFzz,
  ap-GXPXxEWBsDAcVHfNG5iY7a
remaining profile-(3,6) cofactors: 5
next attack: m=32, with mu=5 and E<=85 before parity-adaptive contraction
```

**Same-day cofactor-32 close:** odd singleton multiplicity removes the
imprimitive branch, and dual complete censuses separate every live norm from
the prize interval.

```text
proved node: e1_prize_n256_s18_profile_36_m32_exclusion
exact product comparisons: 173683
product ledger: 474 live and 1360 excluded (E,q,L) triples
all E=61,...,85 chambers excluded
normalized singleton supports examined: 10009125
mu=5 supports: 317440; affine orbits: 19840
singleton sign assignments: 634880
dual-agreed unique radius triples: 84923111400
exact sign tests: 679384891200
directly replayed low-energy vectors: 339892636
product-live vectors: 239131808
certified norm intervals: 239131588 below, 220 above, 0 unresolved
atlas/primary/audit Modal apps:
  ap-ZYUKwFlZR2pe1INkfddSsZ, ap-blU0kVG1XoQdz0XWxgLKwz,
  ap-JcLLKV4WPUIDrn8rhERbNh
node verifier Modal app: ap-RltPJOCiFf2VhH1gYQMtdw
remaining profile-(3,6) cofactors: 4
next attack: m=16, with mu=4 and an explicit all-one-parity branch
```

**Same-day cofactor-16 support decomposition and first branch close:** exact
multiplicity four splits exhaustively into primitive, once-divided, and
twice-divided support strata. The smallest stratum has now been removed by
dual complete censuses; this is a proved branch theorem, not a full m16 close.

```text
proved node: e1_prize_n256_s18_profile_36_m16_two_divisions_exclusion
support atlas:
  primitive mu4 in Z/128:       39936 affine orbits, OPEN
  once-divided mu2 in Z/64:      9080 affine orbits, OPEN
  twice-divided mu1 in Z/32:      903 affine orbits, PROVED empty
exact product comparisons: 295256
product ledger: 967 live and 2718 excluded (E,q,L) triples
generic third-moment pilot: 949/967 records survive (quantified no-go)
twice-divided singleton sign assignments: 28896
dual-agreed unique radius triples: 7422374296
exact sign tests: 59378994368
directly replayed low-energy vectors: 497496976
product-live vectors: 205513652
certified norm intervals: 205486644 below, 27008 above, 0 unresolved
atlas/product/primary/audit Modal apps:
  ap-7D69LSBDaIs3eLWRsy4jIg, ap-inCC4VYiLY8tmSyAF6wpQU,
  ap-1xutdz21Bfop112ugKr65k, ap-kmhgYnrF7vWYttQXorFm0w
node verifier Modal app: ap-IVF9ra2KWJyhXPplppzymj
measured direct-census projections:
  once-divided 26.819 one-CPU hours; primitive 121.464 one-CPU hours
compute decision: defer both larger exact censuses and seek analytic
  support-specific contraction before spending further budget
remaining profile-(3,6) cofactors: 4 (m=16 is only partially decomposed)
next attack: contract or structurally exclude the once-divided m16 branch;
  do not launch the primitive census under the current compute budget
```

**Same-day cofactor-16 once-divided close:** an exact subfield argument removes
all-even heavy triples, a rigorous early upper cap makes the primary census
affordable, and an independent full-interval reverse engine reproduces every
proof count on every support orbit.

```text
proved node: e1_prize_n256_s18_profile_36_m16_one_division_exclusion
once-divided quotient supports examined: 557845
exact-multiplicity-two supports: 139360; affine orbits: 9080
all-even heavy triples omitted per orbit by square norm: 30856
post-square singleton-sign distance tests: 76819415040
dual-agreed unique radius triples: 73175732492
exact sign tests: 585405859936
directly replayed low-energy vectors: 6762240640
product-live vectors: 1816625504
certified norm intervals: 1816625308 below, 196 above, 0 unresolved
primary/reverse-benchmark/projection/audit Modal apps:
  ap-6xxI9MGrLIK1n5crnIT6c3, ap-vysGPqGNw3Uo1bZm9osv0L,
  ap-mt8xdOni6TjNwFU6qkqBqE, ap-HxT2OzXtS2r4jcKWzNH2a4
node/DAG/harness verifier Modal apps:
  ap-X5QrnxnWwUrM9c7S88jt2e, ap-IIr6duTwdkDUjj6Oxo5tEa,
  ap-DTNXEczjog2rzfTDf5LYAD
m16 support status:
  primitive mu4 in Z/128:       39936 affine orbits, OPEN
  once-divided mu2 in Z/64:      9080 affine orbits, PROVED empty
  twice-divided mu1 in Z/32:      903 affine orbits, PROVED empty
remaining profile-(3,6) cofactors: 4 (m=16 remains open only on primitive)
next attack: seek analytic contraction of primitive m16; its last measured
  direct projection was 121.464 one-CPU hours and is not authorized
```

**Same-day primitive m16 contraction, primary close, and interrupted audit:**
the free Galois involution `F(X)->F(-X)` halves normalized signs; an exact
seven-coefficient Walsh ledger replaces the lagwise eight-sign energy loop;
and independent certified upper-product caps reduce the complete route from
hundreds of CPU hours to a sub-dollar primary and audit.

```text
candidate node: e1_prize_n256_s18_profile_36_m16_primitive_exclusion
status: NOT YET PROMOTED (reverse audit 61.5% complete)
primitive affine support orbits: 39936
sign representatives per heavy triple: 16 (free Galois involution)
primary Modal app: ap-tkhXMEdMpCXgm2LWUnXkEZ, COMPLETE
primary exact ledger:
  distance tests: 188651274240
  radius matches: 184336208507
  exact sign tests: 1474689668056
  low-energy representatives: 29756245802
  product-live representatives: 5651872006
  certified intervals: 5651870997 below, 1009 above, 0 unresolved
reverse benchmark/projection apps:
  ap-ATxdGYMJ3NJBvayKTp20Hc, ap-AmrikHigBcehbCZ8jxlKb3
reverse audit app: ap-bvisSxyx7641bXRImfOwy8, INTERRUPTED EXTERNALLY
reverse checkpoint:
  768/1248 batches; 24576/39936 orbits; every per-orbit comparison PASS
  product-live: 3477665782
  intervals: 3477665087 below, 695 above, 0 unresolved
remaining: 480 batches / 15360 orbits, approximately 20000--25000 CPU seconds
resume rule: wait for Modal workspace and credit; launcher skips checkpoint
promotion gate: complete reverse audit, replay all 1009 high representatives,
  source-pin the theorem packet, then run node/DAG/harness verifiers
```

**Same-day aggregate payoff calibration:** the weighted-kernel target now has
an exact profile-closure ladder. On the binding prize rate-`1/8` row, closing
all of `(3,6,S=18)` would move the coarse sufficient oriented-vector cap only
from `93962` to `106111`; closing every `S=18` profile would move it to
`249314`. Each cap is sharp for the maximum-weight inference, with the
adjacent integer failing that inference. This is route calibration, not a new
DAG node, because the committed replay awaits an enabled Modal workspace.

```text
current maximum:                 (3,6,18), cap 93962
after full profile-(3,6) close: (2,10,18), cap 106111
after every S=18 profile close:   (4,4,20), cap 249314
m16-only consequence: no cap change while m=2,4,8 remain live
packet: notes/E1_PROFILE_WEIGHT_PAYOFF_LADDER.md
replay: experiments/prize_resolution/e1_profile_weight_payoff_ladder.py
Modal wrapper: experiments/prize_resolution/e1_profile_weight_payoff_ladder_modal.py
```

Route decision: finishing the primitive `m=16` audit remains justified as a
nearly complete exact child, but it is one of four cofactor obligations and
must not be reported as moving the aggregate target by itself. After `m=16`,
prefer an aggregate count for `m=2,4,8` if it can certify at most `93962`
oriented vectors; otherwise continue exact cofactor exclusion.

Modal replay status: the 128 MB, one-container payoff verifier was rejected
before launch because the workspace had exceeded its spend limit. No task ran
and no compute was charged. The primitive audit and this tiny replay remain
paused until the account limit changes.

**Same-day `m=8` proof-only support contraction:** Lucas/Hasse parity gives a
complete classification of exact-multiplicity-three six-term supports. Their
mod-four occupancy is a permutation of `(3,1,1,1)`, so the branch is
primitive and the normalized `{0,1}` input contracts from `10009125` generic
supports to `1269760`. The free `F(X)->F(-X)` involution then halves joint
sign work from 256 to 128 representatives per heavy triple. This is an exact
draft lemma with a one-container verifier, not a DAG node, because the Modal
spend limit prevented replay.

```text
raw exact-mu3 supports:             650117120
normalized occupancy-filtered:       1269760
generic normalized input:            10009125
imprimitive branch:                         none
joint singleton/heavy sign reps:           128
packet: notes/E1_M8_SUPPORT_CONTRACTION.md
```

Next `m=8` action after account re-enable: replay the lemma, then measure the
four occupancy shards and affine orbit count. Do not start a radius census
from the generic support atlas.

**Same-day `m=2,4` proof-only support decomposition:** the Hasse-residue
classification now covers every remaining profile-`(3,6)` cofactor support.
Exact multiplicity one (`m=2`) is primitive and leaves `5005539` normalized
supports. Exact multiplicity two (`m=4`) splits into `2501824` normalized
primitive candidates and `279155` normalized once-divided quotient
candidates. In the quotient branch, `30856` all-even heavy triples per
support have square norm and are impossible; `F(-X)` acts freely on every
remaining heavy-sign orbit. All three low cofactors therefore admit 128 joint
sign representatives per surviving heavy triple.

```text
m=2: primitive mu1 in Z/128, normalized input 5005539
m=4: primitive mu2 in Z/128, normalized input 2501824
m=4: quotient mu1 in Z/64, normalized input 279155
m=8: primitive mu3 in Z/128, normalized input 1269760
packet: notes/E1_M2_M4_SUPPORT_DECOMPOSITION.md
```

Existing `m=514` classifiers share the `mu=1` predicate but their retained
atlases are chamber-filtered; they are implementation inputs, not a complete
`m=2` certificate. Replay these tiny lemmas and measure affine atlas sizes
before authorizing product or radius campaigns.

**Same-day affine Burnside completion ledger:** a six-element cycle-union DP
over every affine map of `Z/128` now determines the low-multiplicity orbit
counts without enumerating normalized supports. It independently reproduces
the full committed `m=16` split and supplies exact targets for all three
remaining cofactors.

```text
m=2 mu1 primitive:                     331359 orbits
m=4 mu2 primitive:                     159216 orbits
m=4 quotient mu1 in Z/64:               18383 orbits
m=8 mu3 primitive:                      79360 orbits
m=16 split, independently recovered: 39936 + 9080 + 903
```

The multiplicity-three affine action is free. The `m=16` promotion plan can
therefore replace a second ten-million-input atlas enumeration with canonical
representative validation plus the independent Burnside total. The verifier
is committed but unrun because of the Modal spend limit; no DAG status
changes. The rapidly increasing orbit counts also rule out launching generic
radius censuses for `m=2,4,8` before product or aggregate contraction.

**Same-day pure-dyadic orbit debit:** aggregate accounting weakens the
remaining profile-`(3,6)` obligation from emptiness to a finite orbit count.
For `m=2,4,8`, the odd row prime occurs exactly once in the norm, hence exactly
one primitive root vanishes. Translation and global sign produce exactly 256
oriented dictionary vectors per colliding full affine coefficient orbit. The
coarse profile allowance is therefore 367 such orbits; orbit 368 alone fails.

```text
oriented vectors per pure-dyadic collision orbit: 256
profile-only maximum collision orbits:             367
oriented units used at 367:                       93952
maximum-weight units left:                           10
first failing orbit count:                          368
packet: notes/E1_PROFILE_36_ORBIT_DEBIT.md
```

Route decision: future low-cofactor searches should count exact
root-incidence coefficient orbits and preserve affine canonical witnesses.
They may stop short of proving zero if the full profile-weighted ledger fits.
This is a draft algebraic compiler until its tiny Modal replay runs; no DAG
status changes.

Definition audit: `D_p(33)` is fixed-root and oriented, so the factor 256 is
not obtained by naively dividing a support-normalized count. For
`Norm(F)=2^mu p`, `v_p=1` gives exactly one simple primitive-root zero under
the order-256 Galois action. Its `b in Z/256` translates are exactly the 128
folded support shifts and their negatives. Exact multiplicity `mu<=3`
excludes the sole possible six-set translation period, shift 64, because
`1+X^64=(1+X)^64` over `F_2`. Thus 256 is restored exactly for a **full
coefficient orbit**. Singleton-support rows, heavy/sign rows before residual
stabilizer canonicalization, and bare norm-interval survivors are not units
of this ledger. The guards and required campaign fields are now explicit in
`E1_PROFILE_36_ORBIT_DEBIT.md` and `PRIZE_COMPUTE_REQUESTS.md`.

The alternative maximum-degree-three route would also pay the pair budget,
but its current repository interface has no theorem-level premise beyond the
instruction to bound neighbors of a fixed class. Until such a premise is
posed or a cheap falsifier is available, the root-incidence orbit ledger is
the more concrete route.

**2026-07-28, L1 order-one automatic-root trace cancellation:** the live
next-to-maximal order-one system no longer needs the denominator-heavy
degree-`h-1` quotient representation.

```text
node proved: l1_mersenne_hnf_order_one_full_trace_cancellation
identity:    (x_0^star)^(mj)=x_0^(-mj)=d^(mj) for every j>=1
consequence: first r reduced reciprocal equations
             <=> first r full-P trace equalities
representation delta: no division by W-x_0; no Qtilde construction
live powers: 8,16,24 at (m,h)=(8,7); 16,32,48 at (16,15)
DAG delta: one PROVED background node and two edges; no critical status flip
compute spend: none; proof-only exact algebra
open residue: eliminate the h=7 full-trace system on Psi_7=0, then impose
              pointwise Frobenius, torsion, cyclotomic remainder, inner lift
next route-deciding action: obtain a priced independent h=7 elimination
                              from a contributor; do not retry the retired
                              quotient-resultant backend
```

**2026-07-28, L1 h=7 residual conic reduction:** the smallest live
order-one curve now has an explicit low-degree model rather than a digest-only
ten-term representation.

```text
node proved: l1_mersenne_hnf_m8_order_one_conic_reduction
quadratic:   35u^2+14(11c^2+5c+11)u+120(c^4+c^2+1)=0
square form: D(c)=7(5u+11c^2+5c+11)^2
conic:       7w^2=247z^2+770z+775, z=c+c^-1
pullback:    c^2-zc+1=0 (retained, not silently split)
chart guard: t=infinity, tangent point, and 247-7t^2=0 handled explicitly
DAG delta: one PROVED background node and two edges; no critical status flip
compute spend: none; four-partition coefficient proof
open residue: intersect this model with the full-P traces, pointwise
              Frobenius, torsion, cyclotomic remainder, and inner lift
next route-deciding action: contributor-priced h=7 elimination on the direct
                              quadratic and conic-pullback models
```

**2026-07-28, L1 h=7 base-field conic branch routed:** Frobenius and the
non-prime-field invariant turn one positive-dimensional chart into a finite
packet and eliminate it on two rows.

```text
node proved: l1_mersenne_hnf_m8_order_one_basefield_conic_router
exceptional close: both z=-1 conic points
base-field identity: zeta=2-z
official reduction: zeta=-1, z=3, c^2-3c+1=0
rows closed in this branch: p=8191,131071
rows finite in this branch: p=524287,2147483647; at most two w signs each
packet equations: 7w^2=5308, theta=(w-38)/5, rho^p=-c*rho
DAG delta: one PROVED background node and three edges; no critical status flip
compute spend: none; official congruence and Frobenius proof
open h=7 residue: t notin F_p plus exact replay of at most four finite packets
next route-deciding action: eliminate the finite packets from the full-P
                              first-three trace system before pricing the
                              non-base-field parameter branch
```

**2026-07-28, L1 h=7 base-field branch closed:** the four finite packets do
not require replay. Frobenius reflection converts the whole branch to a
constant-size root-color contradiction.

```text
node proved: l1_mersenne_hnf_m8_order_one_basefield_branch_exclusion
reflection: P^[p](W)=-P(1-W)
root condition: x^n=(1-x)^n=1 for every root of P
field contraction: mu_8 colors -> mu_4 colors
surviving colors: (1,-1),(-1,1),(-1,-1)
root cap: at most 3*2=6
required roots: 7 distinct roots of the squarefree degree-seven P
result: complete t in F_p branch CLOSED on all four m=8 rows
DAG delta: one PROVED background node and two edges; no critical status flip
compute spend: none; exact Frobenius and two-adic proof
open h=7 residue: t notin F_p only
next route-deciding action: combine the non-base-field conic parameter with
                              the colored Frobenius interpolant; preserve
                              root/color assignment and avoid a 64-case
                              assignment-free shortcut
```

**2026-07-28, L1 h=7 constant-color chamber closed:** the first two
rootwise colored reciprocal coefficients already exclude the degree-zero
colored interpolant on all six reduced roots.

```text
node proved: l1_mersenne_hnf_m8_order_one_constant_color_exclusion
first coefficient: rho*c=1-alpha, alpha=epsilon*zeta in mu_8
second coefficient: 30alpha(c-1)=(alpha+1)zeta+12alpha^2
field contraction: c-1 in F_(p^2), hence zeta in {+1,-1}
norm obstruction: 12zeta*s^2+(1+12zeta)s+146-924zeta=0
trace atlas: s=2,-2,0 or s^2=2; no official characteristic survives
result: constant color on the six reduced roots CLOSED on all four m=8 rows
DAG delta: one PROVED background node and two edges; no critical status flip
compute spend: none; exact coefficient and norm proof
open h=7 residue: t notin F_p with a nonconstant, assignment-preserving
                   colored Frobenius interpolant
next route-deciding action: classify or exclude the linear color stratum;
                              otherwise derive a bounded Frobenius
                              correspondence for each nonconstant degree
```

**2026-07-28, L1 order-one linear-color chamber closed:** the pointwise
Frobenius assignment gives a degree-two color equation, independently of the
hypergeometric coefficients.

```text
node proved: l1_mersenne_hnf_order_one_linear_color_exclusion
scope: four (m,h)=(8,7) rows and one (m,h)=(16,15) row
linear ansatz: E(W)=aW+b, a!=0
pointwise color equation:
  -(b^p+a^(p+1))X^2+(1+b^(p+1))X-b=0
available roots: at most 2 unless the polynomial is identically zero
required colors: H=m-2=6 or 14 distinct values
zero-polynomial contradiction: b=0 and then 1=0
combined h=7 result: deg E>=2
DAG delta: one PROVED background node and two edges; no critical status flip
compute spend: none; rootwise assignment proof
open h=7 residue: non-base-field conic parameter with deg E=2,3,4,5
next route-deciding action: attack degree two using the same pointwise
                              color equation before generic resultants
```

**2026-07-28, L1 h=7 quadratic colors routed:** repeated fibers and the
order-one derivative constant reduce the multi-collision chamber to one even
packet with an extra scalar equation.

```text
node proved: l1_mersenne_hnf_m8_order_one_quadratic_collision_router
quadratic split: collision-free / one repeat / two antipodal repeats
affine branch: two repeated colors and S!=0 make Frobenius affine on L
marked-point gate: the affine map must permute {0,1,x_0}
affine outcome: every non-even permutation is impossible
three-pair exclusion: sum roots=-6/(c-1)!=0
two-pair equation: r(18+d-d^2)+192=0, r=rho*c, d=c-1
DAG delta: one PROVED background node and three edges; no critical status flip
compute spend: none; rootwise Frobenius and odd/even divisibility proof
open h=7 degree-two residue: six colors; one repeat; or the printed
                              two-antipodal equation
next route-deciding action: intersect the two-antipodal equation with the
                              h=7 conic, then classify its finite components
```

**2026-07-28, L1 h=7 two-antipodal chamber made univariate:** eliminating
`rho*c` produces one fixed degree-eight polynomial and a finite norm-color
audit.

```text
node proved: l1_mersenne_hnf_m8_order_one_quadratic_two_pair_univariate_reduction
collision equation: r=-192/(18+d-d^2)
univariate endpoint:
  F(d)=5d^8+10d^7-180d^6+672d^5+2862d^4
       -15516d^3+8199d^2-44172d+4860
torsion endpoint: gcd(F(X),X^(p+1)-zeta), zeta in mu_8
packet count: 4 rows * 8 colors = 32 degree-eight gcds
DAG delta: one PROVED background node and three edges; no critical status flip
compute spend: none; Modal workspace remains spend-blocked
open packet: exact gcd verdicts, recorded as CR-L1-H7-Q2-PAIR
next route-deciding action: run the cheap gcd packet when Modal is available;
                              meanwhile attack one-repeat quadratic colors
```

**2026-07-28, L1 quadratic color resultant:** pointwise Frobenius produces
one degree-six polynomial in the color variable. This closes the `h=15`
quadratic stratum and gives exact finite color shapes at `h=7`.

```text
node proved: l1_mersenne_hnf_order_one_quadratic_color_resultant
resultant: R_E(X)=U(X)^2-V(X)T(X), degree 6
h=15 consequence: 14 roots -> at least 7 colors > degree 6; CLOSED
h=7 consequence: R_E/(A A^p)^2 is the six-color multiset polynomial
collision-free shape: (X^8-1)/((X-eta)(X-theta))
one-repeat shape: (X-epsilon)(X^8-1)/product_3(X-eta_j)
DAG delta: one PROVED background node and two edges; no critical status flip
compute spend: none; exact Sylvester-resultant proof
open h=15 color degrees: 0 and 3,...,13
open h=7 quadratic work: coefficient elimination for collision-free and
                         one-repeat shapes; two-pair gcd packet remains queued
next route-deciding action: compare QCRS5 coefficients with the h=7 L
                              moments while preserving the repeated assignment
```

**2026-07-28, L1 order-one color-degree barrier:** the pointwise equations
form a Bézout pair of degrees `d` and `d+1`, giving a general low-degree
exclusion without elimination.

```text
node proved: l1_mersenne_hnf_order_one_color_degree_barrier
general inequality: H<=d(d+1) for every nonconstant degree-d interpolant
h=7 threshold: H=6, hence d>=2
h=15 threshold: H=14, hence d>=4
new close: complete h=15 cubic color chamber
DAG delta: one PROVED background node and two edges; no critical status flip
compute spend: none; pointwise Bézout proof
open h=15 color degrees: 0 and 4,...,13
next route-deciding action: attack the h=15 constant chamber with the first
                              two reciprocal coefficients; keep h=7 on its
                              degree-two collision decomposition
```

**2026-07-28, L1 h=15 constant color reduced to two gcds:** the first two
reciprocal coefficients contract the full fourteen-root packet to the trace
line of `mu_16`.

```text
node proved: l1_mersenne_hnf_m16_order_one_constant_color_reduction
first coefficient: rho*c=1-alpha
second coefficient: 182alpha(c-1)=(alpha+1)zeta+28alpha^2
field contraction: c-1 in F_(p^2), hence zeta in {+1,-1}
trace polynomial: S(S^2-4)(S^2-2)(S^4-4S^2+2)
closure packet: two quadratic gcds over F_8191
DAG delta: one PROVED background node and two edges; no critical status flip
compute spend: none; packet queued as CR-L1-H15-COLOR0
open h=15 order-one colors: two-gcd constant packet and degrees 4,...,13
next route-deciding action: obtain the two cheap gcd verdicts when Modal is
                              available; otherwise return to h=7 one-repeat
```

**2026-07-29, L1 h=15 constant color closed:** both trace gcds are unit by
small modular pseudo-remainder certificates, so no compute is required.

```text
node proved: l1_mersenne_hnf_m16_order_one_constant_color_exclusion
lower trace factors: direct nonzero values and residues 7783,1298
primitive quartic certificates: (L,M,R)=(3964,47,4509),
                                         (439,321,4947) mod 8191
result: complete h=15 constant-color chamber CLOSED
combined degree barrier: live h=15 color degrees are 4,...,13
DAG delta: one PROVED background node and two edges; no critical status flip
compute spend: none; CR-L1-H15-COLOR0 retired
next route-deciding action: return to h=7 one-repeat/collision-free degree two
```

**2026-07-29, L1 h=7 quadratic pointwise composition:** Bézout saturation at
six roots upgrades the pointwise equations to a polynomial identity and a
new equation in the HNF parameters alone.

```text
node proved: l1_mersenne_hnf_m8_order_one_quadratic_pointwise_composition
composition identity:
  A^p E^3+B^p W E^2+C^p W^2 E-W^2=A^p A^3 L
coefficient consequence: C/A=(1-rho*c)/(c-1)^2
pure HNF consequence: g(1)=(1-rho*c)^3
scope: every h=7 quadratic collision chamber
DAG delta: one PROVED background node and two edges; no critical status flip
compute spend: none; exact assignment-preserving degree argument
next route-deciding action: expand g(1) on the h=7 conic and eliminate
                              rho*c before any collision-specific work
```

**2026-07-29, L1 h=7 quadratic HNF intersection:** the new pure HNF equation
and residual conic eliminate `rho*c` into one fixed degree-fourteen endpoint.

```text
node proved: l1_mersenne_hnf_m8_order_one_quadratic_hnf_intersection
HNF quadratic: a_0(d)r^2+b_0(d)r+c_0(d)=0
residual conic: a_1(d)r^2+b_1(d)r+c_1(d)=0
univariate endpoint: R_2=(a_0c_1-c_0a_1)^2
                       -(a_0b_1-b_0a_1)(b_0c_1-c_0b_1)
degree / leader: 14 / -691200
packet count: 4 rows * 8 norm colors = 32
DAG delta: one PROVED background node and three edges; no critical status flip
compute spend: none; queued as CR-L1-H7-Q2-ALL
next route-deciding action: obtain the tiny norm-gcd verdicts when Modal is
                              available; otherwise attack color degree three
```

**2026-07-29, L1 h=7 cubic two-triple reduction:** the most concentrated
cubic color partition now has a fixed norm-gcd endpoint.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_two_triple_reduction
covered partition: 3+3
fiber identity: L=e_3^(-2)(E-alpha)(E-beta)
new quadratic: q_2(d)r^2+q_1(d)r+q_0(d)=0
univariate endpoint: R_33=(a_1q_0-c_1q_2)^2
                         -(a_1q_1-b_1q_2)(b_1q_0-c_1q_1)
degree / leader: 14 / -576000
packet count: 4 rows * 8 norm colors = 32
DAG delta: one PROVED background node and four edges; no critical status flip
compute spend: none; queued as CR-L1-H7-C3-33
next route-deciding action: route the remaining cubic multiplicity
                              partitions without a generic saturation
```

**2026-07-29, L1 h=7 cubic two-triple close:** the `3+3` endpoint closes by
an additional coefficient identity, with no external computation.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_two_triple_exclusion
new identity: rd+4(d^2+3d+3)=0
conic substitution: 32(d^2+3d+3)(2d^2+9d+9)=0
second-quadratic substitution: -8d(d+2)(2d^2+9d+9)=0
surviving candidates: d=-3/2,-3
norms: 9/4,9; neither lies in mu_8 on an official row
closed partition: 3+3 on all four h=7 rows
compute spend: none; CR-L1-H7-C3-33 retired
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: attack the two remaining three-color cubic
                              partitions, 3+2+1 and 2+2+2
```

**2026-07-29, L1 h=7 cubic three-color router:** the remaining cubic packets
with exactly three colors now have a seven-orbit bounded interface.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_color_remainder_router
raw color triples: C(8,3)=56
cyclic color orbits: 7
exact profiles: 3+2+1 and 2+2+2
profile cores after role sharding: 7*(6+1)=49
carrying equations: h=7 conic; six value-remainder coefficients;
                    three nonempty-fiber resultants; exact subresultants
row equations: adjoin d^(p+1)=zeta only to retained p-free components
compute spend: none; contributor packet CR-L1-H7-C3-3COL recorded
DAG delta: one PROVED background node and three edges; no critical status flip
next route-deciding action: derive hand eliminants from the three-color
                              remainder before requesting any large run
```

**2026-07-29, L1 h=7 cubic three-double factorization:** the symmetric
`2+2+2` profile now has a quadratic-factor endpoint.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_double_factor_reduction
factor family: F_i=W^2+u_iW+u_i^2-Uu_i+V
external roots: y_i=u_i-U
HNF identity: L=F_1F_2F_3
color constants: a_i=w+(u_i^2-Uu_i+V)(u_i-U)
color condition: one scale-free ordered difference ratio
generic degree-nine remainder: retained only as an audit for 2+2+2
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: eliminate the symmetric u_i data against the
                              six HNF coefficients and the conic
```

**2026-07-29, L1 h=7 cubic three-double symmetric compiler:** the factor
core is now square before color and norm sharding.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_double_symmetric_compiler
eliminated variables: s_1,V,s_3 and the individual u_i
retained variables: U,s_2,r,d
retained equations: cleared l_4,l_5,l_6 identities plus the h=7 conic
status of core: exact and square; dimension/unit verdict not asserted
later filters: ordered color ratio, norm color, pointwise Frobenius,
               cyclotomic divisibility, inner lift
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: clear and inspect the three explicit equations
                              for a hand resultant or low-cost remote packet
```

**2026-07-29, L1 h=7 cubic three-two-one factorization:** both exact
three-color cubic profiles now have specialized low-degree endpoints.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_factor_reduction
profile: 3+2+1
factor identity: L=FG with F the triple-color cubic
complement values: B,B,lambda B
lambda: (gamma-alpha)/(beta-alpha)
value resultant degree: 3
color-role packets: at most 7*6=42 before row sharding
generic degree-nine remainder: retained only as an independent audit
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: compile the cubic-factor resultant coefficients
                              once, then specialize the 42 lambda values
```

**2026-07-29, L1 h=7 collision-free cubic router:** the injective color
profile now has four missing-pair distance packets.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_collision_free_value_router
profile: 1+1+1+1+1+1
raw missing pairs: C(8,2)=28
cyclic-distance packets: 4 with sizes 8,8,8,4
value identity: Res_W(L,X-E)(X-1)(X-omega^delta)=X^8-1
p-free packets: 4 before row and norm sharding
compute spend: none; contributor packet CR-L1-H7-C3-INJ recorded
DAG delta: one PROVED background node and three edges; no critical status flip
next route-deciding action: route the remaining four- and five-color cubic
                              profiles by squarefree value products
```

**2026-07-29, L1 h=7 complete cubic multiplicity router:** every cubic
color partition now has a proved specialized endpoint.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_four_five_color_value_router
four/five-color identity: V_E M=(X^8-1)D
five-color packets: 35 for 2+1+1+1+1
four-color packets: 35 for 3+1+1+1; 54 for 2+2+1+1
new p-free packet total: 124
complete cubic partition status:
  3+3: proved empty
  3+2+1: cubic-factor resultant endpoint
  2+2+2: four-variable symmetric endpoint
  four/five colors: 124 missing/excess endpoints
  six colors: four missing-pair distance endpoints
compute spend: none; CR-L1-H7-C3-45COL recorded
DAG delta: one PROVED background node and three edges; no critical status flip
next route-deciding action: prioritize the smallest p-free cubic cores for
                              unit proofs before any official norm sharding
```

**2026-07-29, L1 h=7 cubic packet upstream export:** the proved local
two-triple exclusion, the `2+2+2` exceptional reductions, and the `3+2+1`
common-quadratic and role-polynomial compilers are now available for upstream review as draft PR
[#1120](https://github.com/przchojecki/rs-mca/pull/1120).  The export is
intentionally classified `LOCAL_ONLY`: it contributes an exact split-pencil
HNF stratum theorem and exact reductions but does not claim the missing
first-match-to-HNF owner bridge or any LIST/MCA row payment.

```text
local theorems:
  l1_mersenne_hnf_m8_order_one_cubic_two_triple_exclusion
  l1_mersenne_hnf_m8_order_one_cubic_three_double_linear_remainder_reduction
  l1_mersenne_hnf_m8_order_one_cubic_three_double_x0_quintic_reduction
  l1_mersenne_hnf_m8_order_one_cubic_three_double_q6x2_degree12_reduction
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_common_quadratic_compiler
  l1_mersenne_hnf_m8_cubic_three_two_one_role_polynomial_compiler
  l1_mersenne_hnf_m8_cubic_three_two_one_role_factor_compiler
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_role_weld
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_galois_role_weld
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_official_frobenius_role_split
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_scaled_quadratic_core_compiler
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_coefficient_matrix_router
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_singular_j0_univariate_reduction
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_singular_jnonzero_chart_compiler
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_linear_d_router
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_double_linear_d_router
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_doubly_singular_quadratic_quotient_router
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_parameter_reduction
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_bivariate_factorization
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_coefficient_router
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_coefficient_bivariate_compiler
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_q_quotient_router
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_quadratic_router
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_structural_consistency_compiler
  l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_structural_consistency_compiler
  l1_mersenne_hnf_m8_order_one_cubic_three_double_affine_color_compiler
  l1_mersenne_hnf_m8_order_one_cubic_three_double_affine_invariant_formula
  l1_mersenne_hnf_m8_order_one_cubic_three_double_quadratic_quotient_weld
local source commits: 3380ea30, 1c2bfd55, 8d847b9e, e10d4683, 59497c96,
                      44a9d6bb, 0dfd4714, 32b35ed4, f3a355fd, b102cee0,
                      1d9206b9, 98e8685c, 3d5f6274, bdd33eb0, 0cae55cb,
                      6be9ee69, 325c4cd6, 1db48367, e1b1a195, 021caa0a,
                      fd65c11f, 8e256f5e, 8f4bf3d0, eff918d0, f8e9854b,
                      49d1b7af, 806fa2b8, 81d1e850, cc5169fd, 46c7f677,
                      7e430949, ccdb0a55, 46530acb, 1b6ba7b6
upstream base: b13de8113a03f06b6fc22bbd2f289a8abcdf7e95
PR head: 1e31903a012285d8d099224c3ef2076fabd31338
PR state at custody refresh: OPEN, DRAFT, MERGEABLE
upstream files:
  experimental/notes/l1/l1_m8_h7_order_one_cubic_33_exclusion.md
  experimental/notes/l1/l1_m8_h7_order_one_cubic_profile_reductions.md
  experimental/scripts/verify_l1_m8_h7_order_one_cubic_33_exclusion.py
  experimental/scripts/verify_l1_m8_h7_order_one_cubic_profile_reductions.py
  experimental/scripts/l1_m8_h7_cubic_222_norm_endpoints_modal.py
  experimental/scripts/check_l1_m8_h7_cubic_222_norm_certificate.py
  experimental/scripts/l1_m8_h7_cubic_321_singular_j0_gcd_modal.py
  experimental/scripts/check_l1_m8_h7_cubic_321_singular_j0_gcd_certificate.py
  experimental/scripts/l1_m8_h7_cubic_321_fully_proportional_q_quotient_modal.py
  experimental/scripts/check_l1_m8_h7_cubic_321_fully_proportional_q_quotient_certificate.py
proof endpoint: d in {-3/2,-3}; norms 9/4 and 9 contradict mu_8 on all
                four declared Mersenne characteristics
additional endpoints: P_5 of degree 5 and R_12 of degree 12 for the two
                      exceptional 2+2+2 slopes; one degree-42 symbolic role
                      polynomial for the four-variable 3+2+1 core, split
                      either into four high-degree or twelve degree-at-most-
                      four Galois branches, and on official fields into 21
                      irreducible quadratic Frobenius branches with a printed
                      triangular ideal in (x,Y,q,d) and exact coefficient-
                      matrix determinant router; its singular J=0 arm is a
                      degree-7/degree-10 four-prime gcd packet, while its
                      singular J!=0 arm is split into an x=0 two-variable
                      endpoint and an x!=0 three-variable rational chart;
                      generic Delta!=0 has a linear-d eliminant, a
                      second conic/sixth linear eliminant, two rational
                      three-variable charts, and a packet-specific quadratic
                      quotient whose conic/role remainders eliminate d except
                      on N_1=U_1=N_0=U_0=0; that endpoint reconstructs
                      R_0,S_0 and factors F_N as an explicit quadratic in q
                      and z=(4x-15)^2; z=9 is excluded, the vanishing-leading-
                      coefficient chart has z=1575/247 and
                      q=-10(z+27)/231, and the generic q-discriminant is
                      302400z(9-z)(-200z^2+4239z-14175); its four
                      coefficient-zero equations reconstruct D,Q_0 and,
                      off one explicit denominator, G_2,H,Y from (b,q),
                      leaving one bivariate compatibility equation; the
                      retained exceptional chart has Q_0=q^2/3; exact
                      clearing leaves a generic pair of q-degrees 2 and at
                      most 6, with compatibility polynomial of total degree
                      at most 12, and explicit polynomial exceptional
                      ideals; quadratic-quotient reduction then leaves one
                      degree-at-most-58 univariate endpoint in b, plus the
                      simultaneous affine-remainder and fixed leading-
                      coefficient charts; a source-pinned four-prime factor,
                      gcd, and quadratic-field candidate packet is ready but
                      unrun; the parallel E_G=0 chart reduces to a degree-16/
                      degree-23 univariate pair off two retained singular
                      coefficient charts; the source-pinned four-prime packet
                      now also emits a four-way Bezout certificate for the
                      generic coefficient/structural gcd and a five-way
                      certificate for the exceptional coefficient/structural
                      gcd; on the generic chart,
                      substituting the reconstructed coefficients into all
                      original structural definitions yields three more
                      univariate filters of bivariate source degrees at most
                      18, 10, and 15, so the complete coefficient/structural
                      endpoint is U=Zhat_D=Zhat_Q=Zhat_R=0; on the generic
                      E_G=0 chart, three analogous filters of degrees at most
                      27, 13, and 21 give the five-way endpoint
                      V_E=X_E=Zhat_D^e=Zhat_Q^e=Zhat_R^e=0; one
                      seven-shape affine-color equation and four rational
                      three-variable packets for generic 2+2+2
replay digests:
  8d49e0b87da9b842d4b827b7feae6718e3c0e9628e9a94d33cfc8b49e901c66f
  8a07454eed5a1171fe364d34ba3f4b5be8d622e5e7bdba625ebd4766dcb15756
compute-request digest:
  d3b4aacf170e13fecdf36718f8566bd597beacf4965aa1584077dbe61db9f695
compute-certificate checker digest:
  9ba5e7ee7a66d459453f5aba312fff5649c7ee37c12264b39d29304ebc8d244f
singular-J0 gcd launcher/checker digests:
  39ccbf6493dc3a421935dbbd0b1e31e761c4e13b2c3f48eaa3c6b87d44a987e0
  a653511eb927b1627258d7c2e25e6b46439827140d1fabab743a2404e771469c
fully-proportional quotient launcher/checker digests:
  06e941be7bd231d993a63ebb83c0855f0798524a10e86249e9796f9b7a02f3c0
  9174a04da730f47d594c65dbc0f0d8d20aaa8a064cc225c51ef69e68d6baf1de
replay status: pending; local computation is prohibited and Modal is
               currently spend-blocked
status_ours: PROVED
status_his: OPEN_REVIEW
critical/upstream terminal delta: none
next upstream bridge: place the HNF cell in an exhaustive source-bound owner
                      partition before using it as a bankable route cut
```

**2026-07-29, L1 h=7 cubic `2+2+2` linear remainder reduction:** the
four-variable symmetric core now has a proof-only branch decomposition before
any Groebner or norm work.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_double_linear_remainder_reduction
scaled variables: q=dr, x=dU-3, b=d^2s_2, d
coefficient shape: one quadratic D_b plus two affine-linear remainders in b
fifth-remainder slope: -x(x^2+q/6)
exceptional branches: x=0 and q=-6x^2
generic branch: b determined; three variables remain before color sharding
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: classify the two exceptional p-free branches,
                              then form the generic three-variable eliminant
```

**2026-07-29, L1 h=7 cubic `2+2+2` x=0 quintic endpoint:** the first
exceptional branch is now finite before the unused coefficient and color
filters.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_double_x0_quintic_reduction
branch: x=dU-3=0
closed rational values: d=-2,-3/2,-3 by official norm-color obstruction
remaining polynomial: P_5=60d^5+407d^4+1147d^3+1659d^2+1218d+360
determined parameter: q=-12(5d^3+16d^2+18d+10)/(35(d+2))
finite endpoint: 32 degree-five norm gcds
compute spend: none; CR-L1-H7-C3-222-X0 recorded
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: obtain the x=0 norm verdict, while reducing the
                              q=-6x^2 exceptional branch proof-only
```

**2026-07-29, L1 h=7 cubic `2+2+2` q=-6x^2 degree-12 endpoint:** both
exceptional slopes of the fifth linear remainder now have finite norm
packets.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_double_q6x2_degree12_reduction
branch: q=-6x^2, with q!=0 and q!=d
intermediate conic: 105y^2-7(11d^2+27d+27)y+10B(d)=0, y=x^2
saturation removal: d+6y=0 is exactly q=d
remaining polynomial: R_12=105F^2+7AFE+10BE^2
degree/leader: 12 / 149868
finite endpoint: 32 degree-12 norm gcds
compute spend: none; CR-L1-H7-C3-222-Q6X2 recorded
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: obtain both exceptional norm verdicts, then
                              eliminate the generic three-variable branch
```

**2026-07-29, L1 h=7 cubic `3+2+1` common-quadratic compiler:** the second
three-color profile no longer needs two generic cubic factors or a raw value
resultant.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_common_quadratic_compiler
factor model: G=Q(W)(W-y), F-B=Q(W)(W-z), a=y-z
role equation: aQ(y)=(lambda-1)B
triangular eliminations: a, g_2, B from l_1,l_2,l_3
retained variables per role: (g_1,y,r,d)
retained equations: l_4,l_5,l_6, h=7 conic, role-color equation
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: compile/factor the five p-free equations once in
                              symbolic lambda before the at most 42 roles
```

**2026-07-29, L1 h=7 low-degree norm launcher ready:** the complete
quadratic endpoint, its independent pair specialization, and the two finite
cubic `2+2+2` exceptional endpoints now share one hard-capped replay with
partial output.

```text
launcher: experiments/prize_resolution/l1_m8_h7_low_degree_norm_endpoints_modal.py
source sha256: 502c0922832a5aba3e4700d89369f901a8292d72eeb43d1bf2a23258c1ead8b3
checker: experiments/prize_resolution/check_l1_m8_h7_low_degree_norm_certificate.py
checker sha256: 60a18a0fcb7ac7d3a9ea3ca545cd12c351fc1866ad0035c760fef5f295251607
coverage: quadratic F_8/R_2 and cubic P_5/R_12 on all four official primes
aggregate test: gcd(P,X^(8(p+1))-1) over F_p
equivalence: unit aggregate gcd iff all eight mu_8 norm-color gcds are unit
rows: 4 endpoint polynomials * 4 primes = 16
resources: one container, one CPU, 512 MB, 60-second hard timeout
partial-output boundary: one JSON row after every completed endpoint/prime
certificate: local entrypoint writes remote return with launcher digest;
             checker requires exact source, input, coverage, and 16 unit rows
launch status: READY, NOT RUN; Modal workspace remains spend-blocked
critical status delta: none
next route-deciding action: run after an explicit spend-state change; a unit
                              certificate closes both exceptional branches
```

**2026-07-29, L1 m=8 aggregate norm-gcd compiler:** the low-degree launcher
now rests on an explicit proof artifact rather than an undocumented shard
shortcut.

```text
node proved: l1_mersenne_hnf_m8_aggregate_norm_gcd_compiler
identity: product_zeta (X^(p+1)-zeta)=X^(8(p+1))-1
certificate equivalence: unit aggregate gcd iff all eight color gcds unit
compression: 32 rows -> 4 rows per fixed endpoint polynomial
hit rule: split by zeta; aggregate nonunit is not a packet witness
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: retain the 16-row launcher unchanged; execute
                              only after an explicit Modal spend-state change
```

**2026-07-29, L1 h=7 cubic `3+2+1` role polynomial:** the color-role layer
now has one exact cyclotomic input rather than 42 separate specializations.

```text
node proved: l1_mersenne_hnf_m8_cubic_three_two_one_role_polynomial_compiler
raw resultant: Res_U(C(U),C(1+lambda(U-1))), deg 49
removed diagonal: (lambda-1)^7 for gamma=beta
role polynomial: Lambda_321, degree 42 before squarefree merging
root set: all ordered distinct mu_8 role ratios modulo common scaling
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: eliminate the common-quadratic core once with
                              symbolic lambda and Lambda_321(lambda)=0
```

**2026-07-29, L1 h=7 cubic `2+2+2` affine-color compiler:** the symmetric
three-double core now includes its previously deferred color equation without
restoring the three individual double-fiber parameters.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_double_affine_color_compiler
ordered color input: Lambda_321(lambda), degree 42 before squarefree merging
affine invariants: P=e_2-e_1^2/3,
                   Q=e_3-e_1e_2/3+2e_1^3/27
safe equation: Res_lambda(Lambda_321,
               27(lambda^2-lambda+1)^3 Q^2
               +((lambda+1)(2lambda-1)(lambda-2))^2 P^3)=0
characteristic-zero squarefree color shapes: 7
shape gaps: (1,1,6), (1,2,5), (1,5,2), (1,3,4), (1,4,3),
            (2,2,4), (2,3,3)
explicit invariant polynomial:
  (T+50)(T^2-224T-578)(T^2-4T+54)(125T^2-2404T+13448)
repair: an initial five-shape draft incorrectly merged the two scalene
        reflection pairs; reflection conjugates their affine invariants
generic branch after b elimination: four equations in (x,q,d)
compute spend: none
DAG delta: one PROVED background node and three edges; no critical status flip
next route-deciding action: expand only the four-factor color radical, then
                              eliminate the overdetermined generic core
```

**2026-07-29, L1 h=7 cubic `2+2+2` affine-invariant formula:** the repaired
seven-shape color layer is now explicit in the three-variable HNF core; no
value resultant or individual fiber root remains.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_double_affine_invariant_formula
centered source variables:
  p=b-12
  eta=-xp-q(d+2)/6
  ell=x^2+q/6-2p/3
target invariants:
  P=ell^2p+6x ell eta-(4/3)x^2p^2
  Q=-8x^3(eta^2+2p^3/27)-4x^2 ell p eta
    -(4/3)x ell^2p^2+ell^3 eta
rational color factors: 4, representing 7 geometric values
generic b elimination:
  alpha=-(q-d)x(x^2+q/6)
  beta=(q-d)B_5+6dG
  b=-beta/alpha
retained variables per rational color factor: (x,q,d)
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: reduce the four explicit color factors modulo
                              the conic and the two generic compatibilities
```

**2026-07-29, L1 h=7 cubic `2+2+2` quadratic-quotient weld:** the generic
color packets are now exact denominator-free systems rather than rational
substitutions awaiting a resultant.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_double_quadratic_quotient_weld
quadratic quotient:
  p=b-12
  p^2+(3x^2-q/2)p-(3q(d^2+3d+3)/4+q^2/8)=0
power recurrence:
  U_(n+1)=V_n-aU_n, V_(n+1)=hU_n
compact invariant remainder:
  12P=(-60x^4-8qx^2+8q(d+2)x+4q(d^2+3d+3)+q^2)p
      -12xq(d+2)(x^2+q/6)
generic weld variables: (x,q,d)
equations per color packet: conic, D/M5 compatibility, M5/M6
                            compatibility, color/M5 compatibility
packet count: 4 rational packets representing 7 geometric color values
equivalence: exact on alpha=-(q-d)x(x^2+q/6)!=0
compute spend: none
compute pre-request: CR-L1-H7-C3-222-GEN; proof-producing checker and pilot
                     still missing, so no launch is authorized
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: seek hand factors in the four welded systems;
                              prepare bounded remote elimination only if not
```

**2026-07-29, L1 h=7 cubic `3+2+1` role-factor compiler:** the repaired
affine-shape calculation also factors the second three-color profile's
ordered role input over the rationals.

```text
node proved: l1_mersenne_hnf_m8_cubic_three_two_one_role_factor_compiler
A=lambda^2-lambda+1
B=(lambda+1)(2lambda-1)(lambda-2)
role factors:
  B^2+50A^3                                      degree 6
  B^4-224B^2A^3-578A^6                          degree 12
  B^4-4B^2A^3+54A^6                             degree 12
  125B^4-2404B^2A^3+13448A^6                    degree 12
product degree: 42, proportional to Lambda_321
packet count: 4 rational packets preserving all ordered roles
compute spend: none
DAG delta: one PROVED background node and three edges; no critical status flip
next route-deciding action: run the common-quadratic elimination separately
                              on these four low-degree role factors
```

**2026-07-29, L1 h=7 cubic `3+2+1` role weld:** the role variable is now
eliminated before any p-free classification.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_role_weld
R=a(3y^2+2g_1y+g_2)
S=B
lambda=1+R/S
homogeneous role inputs:
  A_0=S^2+RS+R^2
  B_0=(2S+R)(S+2R)(R-S)
welded packets: the four role factors with (A,B) replaced by (A_0,B_0)
variables per packet: (g_1,y,r,d)
equations per packet: l_4,l_5,l_6, conic, one homogeneous role factor
equivalence: exact on R*S!=0 and inherited exact-fiber saturations
compute spend: none
compute pre-request: CR-L1-H7-C3-321-GEN; proof-producing checker and pilot
                     still missing, so no launch is authorized
DAG delta: one PROVED background node and three edges; no critical status flip
next route-deciding action: seek triangular reductions among l_4,l_5,l_6
                              before posing any four-packet elimination
```

**2026-07-29, L1 h=7 cubic `3+2+1` Galois-role weld:** the ordered role
polynomial has also been split into its individual rational Galois packets,
lowering every role equation to degree at most four.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_galois_role_weld
Galois action: (a,b) -> (ka,kb), k in {1,3,5,7} modulo 8
ordered-pair orbits: 3 of size 2 and 9 of size 4
packet degrees: 2,2,2,4,4,4,4,4,4,4,4,4
total degree: 3*2+9*4=42
homogenization: widehat P_j(R,S)=S^e_j P_j(1+R/S)
candidate representation: disjunction of 12 systems, never a conjunction
variables per branch: (g_1,y,r,d)
equations per branch: l_4,l_5,l_6, conic, one degree-<=4 role equation
compute spend: none
compute pre-request: CR-L1-H7-C3-321-GEN now offers four high-degree or
                     twelve low-degree branches; a bounded pilot must choose
DAG delta: one PROVED background node and three edges; no critical status flip
next route-deciding action: seek hand reductions packet by packet, then build
                              a proof-producing bounded pilot if still needed
```

**2026-07-29, L1 h=7 cubic `3+2+1` official Frobenius split:** the
official congruence now lowers every role equation to degree two over the
base field.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_official_frobenius_role_split
official congruence: p=7 mod 8; choose s in F_p with s^2=2
rational quadratic packets: 3
rational quartics: 9, each split into two F_p quadratics
official branch count: 3+2*9=21
total degree: 21*2=42
irreducibility: lambda^p=(beta/gamma)lambda; lambda in F_p would force
                 beta=gamma, forbidden by the ordered-role saturation
candidate representation: disjunction of 21 systems, never a conjunction
variables per branch: (g_1,y,r,d)
equations per branch: l_4,l_5,l_6, conic, one quadratic role equation
compute spend: none
compute pre-request: CR-L1-H7-C3-321-GEN now compares complete 4-, 12-, and
                     21-branch representations before authorizing a route
DAG delta: one PROVED background node and three edges; no critical status flip
next route-deciding action: exploit the quadratic role relation by hand in
                              the triangular coefficient core before compute
```

**2026-07-29, L1 h=7 cubic `3+2+1` scaled quadratic core:** the official
quadratic packets now have a fully printed four-variable triangular ideal.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_scaled_quadratic_core_compiler
dimensionless variables: x=dg_1, Y=dy, q=dr, d
scaled complement/value pair: S=d^3B, R=d^3 aQ(y)
sixth coefficient: D((Y-A)V-S)=K_6, forcing D=YV!=0
reduced fourth equation:
  D(G_2^2+AU G_2-Y(A+x)V-L_4)-xK_6=0
reduced fifth equation:
  (q-d)(Y^2V^2(G_2+AU)+G_2K_6)-6dK_6D=0
transported role pair:
  R_D=DR, S_D=Y(Y-A)V^2-K_6
role input per official branch: one homogeneous quadratic Phi(R_D,S_D)
equations per branch: E_4,E_5,E_6, conic, Phi; variables (x,Y,q,d)
compute spend: none
compute pre-request: CR-L1-H7-C3-321-GEN now consumes these printed ideals;
                     launcher/checker/pilot/cost ceiling still absent
DAG delta: one PROVED background node and three edges; no critical status flip
next route-deciding action: inspect E_4,E_5 for hand resultants in x or Y;
                              only then design a proof-producing pilot
```

**2026-07-29, L1 h=7 cubic `3+2+1` coefficient-matrix router:** the two
middle coefficient equations now have a complete determinant decomposition.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_coefficient_matrix_router
linear unknowns: H=G_2+AU and K_6
matrix determinant: D*Delta,
  Delta=G_2((q-d)G_2-6dD)+x(q-d)D
generic Delta!=0: two exact Cramer equations
singular Delta=0: WJ=0, split exactly into J=0 and J!=0
x=0 equation: one explicit cubic C_0(Y;q,d)=0
singular J=0 endpoint:
  d(q^2+132q+2916)+144q=0
  q^3+126q^2+(5364-504d-72d^2)q+87480=0
  plus the h=7 conic
compute spend: none
compute pre-request: CR-L1-H7-C3-321-GEN should try the bivariate singular
                     endpoint first with a proof-producing resultant
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: seek a hand gcd of conic, F_J, and F_W; if that
                              stalls, prepare a tiny certificate-producing job
```

**2026-07-29, L1 h=7 cubic `3+2+1` singular-`J=0` univariate endpoint:**
the smallest determinant chamber is now a fixed four-row gcd packet.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_singular_j0_univariate_reduction
A(q)=q^2+132q+2916
F_J and q!=0: d=-144q/A(q), with A(q)!=0
P_W(q)=A(q)^2(q^3+126q^2+5364q+87480)
       +72576q^2A(q)-1492992q^3                    degree 7, monic
P_C(q)=A(q)^4*Conic(q,-144q/A(q))                  degree 10, leader 35
official decision: gcd_Fp(P_W,P_C), four primes
compute spend: none
compute request: CR-L1-H7-C3-321-J0-GCD; source-pinned 0.125-CPU/128 MB/30 s
                 single-container launcher and independent checker written
launcher sha256: 39ccbf6493dc3a421935dbbd0b1e31e761c4e13b2c3f48eaa3c6b87d44a987e0
checker sha256:  a653511eb927b1627258d7c2e25e6b46439827140d1fabab743a2404e771469c
run status: unrun; Modal spend-blocked, no execution authorized
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: continue the Delta!=0 and singular J!=0 hand
                              branches; launch this packet only after access
```

**2026-07-29, L1 h=7 cubic `3+2+1` singular-`J!=0` chart compiler:** the
second determinant-singular chamber now has exact lower-dimensional charts.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_singular_jnonzero_chart_compiler
forced split: x=0 iff G_2=0
x=0 chart: Y=(q+30)/12 and three coefficient equations in (q,d)
linear relation: (q^3+90q^2+3132q+57240)d
                 =8q^3+864q^2+30528q+250560
x!=0 chart: G_2!=0; define N=G_2^2+xD and Z=N+6DG_2
sixth-equation numerator:
  P=3x(6G_2+AxU-20-D)-8qx-3G_2H
exact reconstruction: d=P/(qx)
remaining determinant: q^2xN-PZ=0
reduced endpoint: five equations in (x,Y,q), including conic and one of
                  the 21 alternative quadratic role packets
field-scope catch: q,d are not forced into F_p, so role irreducibility does
                   not by itself delete either chart
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: seek a hand exclusion in the x=0 linear-d chart;
                              otherwise reduce the generic Delta!=0 branch
```

**2026-07-29, L1 h=7 cubic `3+2+1` generic linear-`d` router:** the last
broad coefficient branch now has an exact one-variable eliminant.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_linear_d_router
E_6-normalized pair:
  F_4=G_2H-xQ_6-W
  F_5=(q-d)DH+JQ_6
d degrees: both quadratic, with proportional leading coefficients
exact cancellation: 3(3F_5)+(G_2+6D)(12F_4)=C_1d+C_0
C_1!=0 chart: d=-C_0/C_1; four equations in (x,Y,q)
C_1=0 chart: retain C_1=C_0=0 and four residual equations in (x,Y,q,d)
generic guards: Delta*W!=0; no denominator component discarded
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: inspect the C_1=C_0 exceptional parameter locus
                              for a hand contradiction before any elimination
```

**2026-07-29, L1 h=7 cubic `3+2+1` generic double-linear-`d` router:** the
conic and sixth coefficient provide a second exact linear eliminant.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_double_linear_d_router
quartic cancellation: R_3=(720E_6+q Conic)/2 has degree 3 in d
quadratic reduction: R_2=R_3-44dP_4
second linear equation: 3R_2+(12q+366-176x)P_4=M_1d+M_0
first linear equation: C_1d+C_0=0
parameter determinant: Omega=C_1M_0-M_1C_0=0
C_1!=0: reconstruct d=-C_0/C_1 in three variables
C_1=0,M_1!=0: retain C_0=0 and reconstruct d=-M_0/M_1
doubly singular residue: C_1=M_1=C_0=M_0=0, with d retained
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: attack the doubly singular coefficient locus by
                              its T=G_2+6D zero/nonzero split
```

**2026-07-29, L1 h=7 cubic `3+2+1` doubly-singular quadratic quotient:**
the conic and each role packet now supply two more linear equations in `d`.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_doubly_singular_quadratic_quotient_router
quadratic quotient: d^2=((4x-21)/3)d+4R_0/q from P_4=0
conic remainder: 9q^2 Conic=N_1d+N_0 mod P_4
role remainder: 27Phi(R,S_0+qd/3)=U_1d+U_0 mod P_4
parameter determinant: Xi=N_1U_0-U_1N_0=0
N_1!=0: reconstruct d=-N_0/N_1
N_1=0,U_1!=0: retain N_0=0 and reconstruct d=-U_0/U_1
fully proportional residue: N_1=U_1=N_0=U_0=0, with d retained
role scope: one of 21 alternative official quadratics at a time
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: inspect the fully proportional role/conic locus;
                              use T=G_2+6D only inside that final residue
```

**2026-07-29, L1 h=7 cubic `3+2+1` fully-proportional parameter
reduction:** the final quotient coefficients now have explicit solutions.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_parameter_reduction
b=4x-15 is nonzero: b=0 would give N_1=630q^3!=0
conic reconstruction: R_0=-qP/(2880b)
bivariate conic endpoint: F_N=6P^2-bPQ+2880b^2T_c=0
role reconstruction: S_0=-c_1R/(2c_0)-qa_d/18
discriminant weld:
  c_0^2 disc_d(P_4)=81(c_1^2-4c_2c_0)R^2
scope fence: ambient quadratic field, so no prime-field nonsquare
             contradiction is claimed
retained d equation: P_4=0
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: combine F_N and the four coefficient-zero
                              equations before any packet-by-packet compute
```

**2026-07-29, L1 h=7 cubic `3+2+1` fully-proportional bivariate
factorization:** the conic endpoint is only quadratic in `q`.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_bivariate_factorization
coordinate: z=(4x-15)^2
factored endpoint:
  F_N/24=63(1575-247z)q^2+9240z(9-z)q
         +400z(9-z)(z+27)
excluded chart: z=9 gives -63*648q^2!=0
generic q-discriminant:
  302400z(9-z)(-200z^2+4239z-14175)
leading-zero chart: z=1575/247 and q=-10(z+27)/231
scope fence: no ambient-field square verdict
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: substitute the bivariate endpoint into
                              C_1=M_1=C_0=M_0 before any compute
```

**2026-07-29, L1 h=7 cubic `3+2+1` fully-proportional coefficient
router:** the four coefficient-zero equations now reduce generically to a
bivariate system.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_coefficient_router
M-pair reconstruction:
  D_*=3600bD, Q_*=72D_*Q_0, with D_*!=0
structural identity:
  H+G_2=(b^2+6b+105+8q)/16, A=-(b+3)/2!=0
C-pair reduction:
  E_G G_2+F_G=0, J_G G_2+D L_G=0
generic chart:
  G_2=-F_G/E_G and Theta_G=E_G D L_G-J_G F_G=0
exceptional chart:
  E_G=0 forces Q_0=q^2/3 and Q_*-24D_*q^2=0
final retained coefficient chart:
  E_G=J_G=L_G=0 with G_2 retained
scope fence: every chart retains F_b, the structural, role, P_4, and
             arithmetic-lift equations; no emptiness is claimed
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: simplify the generic bivariate compatibility
                              and the E_G=0 exceptional endpoint by hand
```

**2026-07-29, L1 h=7 cubic `3+2+1` coefficient bivariate compiler:** the
rational router now has compact denominator-free endpoints.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_coefficient_bivariate_compiler
cleared polynomials:
  F_*=D_*K_*-30bQ_*
  J_*=150bQ_*-3D_*^2-5PD_*
  Theta_*=5E_GD_*^2L_*-6J_*F_*
exact generic endpoint:
  F_b(b^2,q)=Theta_*(b,q)=0, E_G!=0
  G_2=-F_*/(600bE_G)
exceptional endpoint:
  F_b=E_G=X_*=0, X_*=Q_*-24D_*q^2
  J_*!=0 reconstructs G_2=-D_*^2L_*/(720bJ_*)
final coefficient residue:
  F_b=E_G=X_*=J_*=L_*=0 with G_2 retained
degree ledger:
  deg(Theta_*)<=12, deg_q(Theta_*)<=6, deg_q(F_b)=2
scope fence: the structural, role, P_4, and arithmetic-lift equations remain
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: factor or eliminate the small pair
                              (F_b,Theta_*) with proof-producing evidence
```

**2026-07-29, L1 h=7 cubic `3+2+1` generic q-quotient router:** the
degree-six compatibility polynomial now reduces modulo the quadratic conic
endpoint.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_q_quotient_router
quadratic coefficients:
  F_b=a_2q^2+a_1q+a_0
cleared power recurrence:
  a_2^(j-1)q^j=u_jq+v_j mod F_b, 2<=j<=6
affine remainder:
  a_2^5Theta_*=rho_1(b)q+rho_0(b) mod F_b
generic chart:
  q=-rho_0/rho_1
  U(b)=a_2rho_0^2-a_1rho_0rho_1+a_0rho_1^2=0
singular affine-remainder chart:
  rho_1=rho_0=0 with F_b retained
leading-coefficient chart:
  b^2=1575/247, q=-10(b^2+27)/231, Theta_*=0
degree ledger:
  deg_b(rho_1)<=26, deg_b(rho_0)<=28, deg_b(U)<=58
scope fence: no nonzero-resultant or root verdict; all structural, role, P_4,
             and arithmetic-lift equations remain
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: obtain a proof-producing factorization of U and
                              the gcd content of (rho_1,rho_0)
```

**2026-07-29, L1 h=7 fully-proportional quotient compute packet:** the next
route decision is source-complete but deliberately unrun.

```text
request: CR-L1-H7-C3-321-FPQ-QUOTIENT
launcher: experiments/prize_resolution/l1_m8_h7_cubic_321_fully_proportional_q_quotient_modal.py
checker: experiments/prize_resolution/check_l1_m8_h7_cubic_321_fully_proportional_q_quotient_certificate.py
work: factor degree-at-most-58 U over four official fields; certify
      gcd(rho_1,rho_0), the a_2=0 chart, every factor and the diagnostic
      degree-1/2 subset,
      gcd(U,Zhat_D,Zhat_Q,Zhat_R) by a four-way Bezout identity, and
      gcd(V_E,X_E,Zhat_D^e,Zhat_Q^e,Zhat_R^e) by a five-way identity;
      also certify and factor gcd(H,K) for the S_1=S_0 singular chart,
      flag the already-excluded A=0 factor, and list every non-A factor
      of degree at most two over the official prime field
limits: one CPU, 512 MB, 60 seconds per prime, at most four containers,
        no retries, atomic partial output
estimated cost: below $0.01
status: source-complete, syntax-only validation, unrun
launch gate: Modal workspace spend-blocked; explicit spend-access change
             required before launch
closure rule: a unit four-way gcd excludes the generic coefficient/structural
              chart for that prime, and a unit five-way gcd excludes the
              generic exceptional chart; nonunit factors still require role,
              P_4, saturation, and arithmetic-lift replay
```

**2026-07-29, L1 h=7 cubic `3+2+1` exceptional-E quadratic router:** the
parallel `E_G=0` coefficient chart now reduces to bounded univariate data.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_quadratic_router
exceptional quadratic:
  E_G=-720bq^2+(240b^2-1902b-630)q
      -40b(b^2-6b+27)
affine cancellation:
  a_2E_G-e_2F_b=S_1q+S_0
generic exceptional chart:
  q=-S_0/S_1
  V(b)=a_2S_0^2-a_1S_0S_1+a_0S_1^2=0
  X_E(b)=S_1^3X_*(b,-S_0/S_1)=0
singular charts:
  S_1=S_0=0 with F_b=X_*=0 retained
  a_2=0 with fixed b^2,q and E_G=X_*=0 retained
degree ledger:
  deg(S_1)<=5, deg(S_0)<=7, deg(V)<=16, deg(X_E)<=23
scope fence: no gcd/root or emptiness verdict; all structural, role, P_4,
             saturation, and arithmetic-lift equations remain
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: obtain proof-producing gcds for (V,X_E) and the
                              simultaneous singular coefficient charts
```

**2026-07-29, L1 h=7 cubic `3+2+1` generic structural compiler:** the
coefficient-only endpoint is now reattached to every original structural
definition before any root can be accepted.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_structural_consistency_compiler
reconstructions:
  D_c=D_*/(3600b), Q_c=Q_*/(72D_*), G_c=-F_*/(600bE_G)
  H_c=ell-G_c, Y_c=(ell-2G_c)/A-x, V_c=G_c+xY_c+Y_c^2
three structural filters:
  Z_D=Num(D_c-Y_cV_c)
  Z_Q=Num(Q_c-A G_c-x ell+20+8q/3+D_c)
  Z_R=Num(R_c-G_c(ell-G_c)+xQ_c+(A+x)D_c
          +15+23q/4+q^2/8)
degree ledger:
  deg(Z_D)<=18, deg(Z_Q)<=10, deg(Z_R)<=15
generic q reconstruction:
  Zhat_i(b)=rho_1^deg_q(Z_i) Z_i(b,-rho_0/rho_1)
complete coefficient/structural endpoint:
  U=Zhat_D=Zhat_Q=Zhat_R=0
scope fence: role-discriminant, P_4, saturations, and arithmetic lifts remain;
             no common-root or emptiness verdict
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: extend the factor packet to certify common gcds
                              with the three structural filters
```

**2026-07-29, L1 h=7 generic structural-gcd packet extension:** the existing
unrun quotient request now decides the complete generic coefficient and
structural endpoint before any role sharding.

```text
source encoding: primitive integer q-coefficient tables for Z_D,Z_Q,Z_R
runtime guards: total degrees at most 18,10,15; fixed contents are units in
                every official characteristic
bounded substitution: compute each Zhat_i mod U, so degrees stay below 58
certificate: four-way Bezout identity for gcd(U,Zhat_D,Zhat_Q,Zhat_R)
UNIT meaning: generic coefficient/structural chart excluded on that prime
HIT meaning: only common factors continue to role, P_4, saturation, and lifts
non-verdict: explicit U_IDENTICALLY_ZERO branch
limits: unchanged at four independent one-CPU, 512 MB, 60-second tasks
estimated cost: still below $0.01
status: source-complete, syntax-only validation, unrun; Modal spend-blocked
compute spend: none
DAG delta: none; this is a proof-producing request for the existing endpoint
next route-deciding action: run only after an explicit spend-access change
```

**2026-07-29, L1 h=7 exceptional-`E_G` structural compiler:** the generic
part of the exceptional coefficient chart is now reattached to every
original structural definition.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_structural_consistency_compiler
scope: E_G=0 and a_2*S_1*J_*!=0
reconstructions:
  D_e=D_*/(3600b), Q_e=Q_*/(72D_*)
  G_e=-D_*^2L_*/(720bJ_*), H_e=ell-G_e
  Y_e=(ell-2G_e)/A-x, V_e=G_e+xY_e+Y_e^2
structural filters:
  Z_D^e=Num(D_e-Y_eV_e)
  Z_Q^e=Num(Q_e-A G_e-x ell+20+8q/3+D_e)
  Z_R^e=Num(R_e-G_e(ell-G_e)+xQ_e+(A+x)D_e
            +15+23q/4+q^2/8)
degree ledger:
  deg(Z_D^e)<=27, deg(Z_Q^e)<=13, deg(Z_R^e)<=21
exceptional q reconstruction:
  Zhat_i^e=S_1^deg_q(Z_i^e) Z_i^e(b,-S_0/S_1)
complete coefficient/structural endpoint:
  V_E=X_E=Zhat_D^e=Zhat_Q^e=Zhat_R^e=0
retained charts: S_1=0, a_2=0, and J_*=0; role, P_4, saturations,
                 and arithmetic lifts also remain
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: consume the shared five-way packet after an
                              explicit spend-access change
```

**2026-07-29, L1 h=7 shared exceptional structural-gcd extension:** the
existing four-prime packet now decides both reconstructed coefficient charts
in each future container.

```text
exceptional source: V_E, cubic-cleared X_E, and primitive integer
                    q-coefficient tables for Z_D^e,Z_Q^e,Z_R^e
bounded substitution: compute X_E and each Zhat_i^e modulo V_E
certificate: five-way Bezout identity for
             gcd(V_E,X_E,Zhat_D^e,Zhat_Q^e,Zhat_R^e)
UNIT meaning: a_2*S_1*J_*!=0 exceptional coefficient/structural chart
              excluded on that prime
HIT meaning: only common factors continue to role, P_4, saturation, and lifts
non-verdict: explicit V_E_IDENTICALLY_ZERO branch
resource delta: no new containers, CPUs, memory, retries, or timeout
estimated total cost: still below $0.01
status: source-complete, syntax-only validation, unrun; Modal spend-blocked
compute spend: none
DAG delta: none; this packet consumes the two existing structural compilers
next route-deciding action: run only after an explicit spend-access change
```

**2026-07-29, L1 h=7 exceptional-`E_G` leading-chart exclusion:** the fixed
`a_2=0` chart of (FEQ8) is now closed analytically in every official
characteristic.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_leading_chart_exclusion
fixed chart:
  z=b^2=1575/247
  q=-10(z+27)/231
affine exceptional equation:
  E_G=C_b b+C_0
  C_b=-8244*3950060/(61009*5929)
  C_0=3233714400/(61009*231)
forced value:
  b=115275930/45228187
official obstruction:
  W=247*115275930^2-1575*45228187^2
   =60466872820654125
  W mod (8191,131071,524287,2147483647)
   =(6740,100974,284891,1825899718)
conclusion: E_G=0 is already impossible, so X_*=0 and all structural,
            role, P_4, saturation, and arithmetic-lift equations are
            unnecessary on this branch
scope fence: no claim about the generic exceptional endpoint, S_1=S_0=0,
             J_*=0, the ordinary coefficient chart, or another h=7 shape
checker state: exact rational primary and independent direct prime-field
               audit source-complete; AST-only local validation; intentionally
               unexecuted under the Modal-only computation rule
checker hashes:
  verify.py       4a1e82d0c0e60867674cd88373605ad35011e08199b3aab8b156a29e0c632b4c
  verify_audit.py 6c218637a0f7cacdb323b4ceea58619fe50dab7b7fde23e2e47c2c43d5d05342
upstream custody:
  PR: https://github.com/przchojecki/rs-mca/pull/1120
  commit: c82b819a71e55c830b31549fec3895d5b8c6b3d7
  combined verifier:
    8a07454eed5a1171fe364d34ba3f4b5be8d622e5e7bdba625ebd4766dcb15756
  export state at pin: OPEN, DRAFT, MERGEABLE
  replay repair: verifier note path corrected from the repository root to
                 experimental/notes/l1 before export
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: attack the retained S_1=S_0=0 exceptional chart
                              by hand while the shared gcd packet remains
                              spend-blocked
```

**2026-07-29, L1 h=7 exceptional-`E_G` singular-affine router:** the
simultaneous `S_1=S_0=0` coefficient chart is now an exact two-quartic
endpoint.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_singular_affine_router
normalization with z=b^2 and A=1575-247z:
  S_0=360bE_0
  S_1=126E_1
  (z+27)E_1-66bE_0=-3A R
  R=163b(z+27)-(40z^2+51z-2835)
unit guard:
  N(-27)=24948 mod (8191,131071,524287,2147483647)
        =(375,24948,24948,24948)
reconstruction:
  b=N(z)/(163(z+27))
quartic endpoint:
  H=N(z)^2-163^2 z(z+27)^2=0
  K=42A(z)N(z)+163(z+27)^2(-800z^2+8929z-11025)=0
  deg(H)=deg(K)=4 on every official characteristic
retained equations: A!=0, F_b=X_*=0, J_* split, structural filters, role,
                    P_4, saturations, and arithmetic lifts
scope fence: no common-root, ambient F_(p^2), or emptiness verdict
checker state: exact polynomial primary and independent prime-field sample
               audit source-complete; AST-only local validation; unexecuted
checker hashes:
  verify.py       f46dded9618644a42b670a8d3d37738ba1a0808eff70f699d29f3c84939628ab
  verify_audit.py 3c9150abef83dc540529468dfa01c76529f2e0ef3e0af82825848fef42265b76
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
next route-deciding action: add the quartic common-root/ambient-degree
                              decision to the existing bounded four-prime
                              packet without increasing its resource envelope
```

**2026-07-29, L1 h=7 exceptional singular-affine packet extension:** the
existing unrun four-prime request now decides whether the two-quartic endpoint
has any algebraic root away from the closed leading chart.

```text
source additions: primitive integer coefficient tables for
                  A=1575-247z and the quartics H,K
certificate: pairwise Bezout identity for gcd(H,K), followed by a complete
             irreducible factorization of the monic gcd
guard classification: flag every factor dividing A; these belong to the
                      separately proved exceptional leading-chart exclusion
legal classification: retain every non-A irreducible factor, at any degree
quadratic diagnostic: separately list the degree-at-most-two legal factors
EMPTY meaning: no algebraic root exists on the declared A!=0 chart
HIT meaning: every listed legal factor continues to b reconstruction,
             F_b=X_*=0, J_*, structural, role, P_4, saturation, and lifts
launcher:
  06e941be7bd231d993a63ebb83c0855f0798524a10e86249e9796f9b7a02f3c0
checker:
  9174a04da730f47d594c65dbc0f0d8d20aaa8a064cc225c51ef69e68d6baf1de
resource delta: none; four one-CPU, 512 MB, 60-second tasks, no retries,
                atomic partial output
estimated total cost: still below $0.01
status: source-complete, AST-only validation, unrun; Modal spend-blocked
compute spend: none
DAG delta: none; this consumes the existing singular-affine router
upstream custody:
  PR: https://github.com/przchojecki/rs-mca/pull/1120
  commit: 9ddfb6ac70d8e2e1fcc4660ae204510c51b333a8
  combined verifier:
    82feb2820f1539b9c3da69ebbfbf0c6b84bfede5ae357303dc828d4d3cfabd0a
  launcher/checker parity:
    06e941be7bd231d993a63ebb83c0855f0798524a10e86249e9796f9b7a02f3c0
    9174a04da730f47d594c65dbc0f0d8d20aaa8a064cc225c51ef69e68d6baf1de
  export state at pin: OPEN, DRAFT, MERGEABLE
next route-deciding action: consume the packet only after an explicit
                              spend-access change; meanwhile attack the
                              retained exceptional J_*=0 chart by hand
```

**2026-07-29, L1 h=7 exceptional-`J_*=0` affine router:** the last
coefficient chart retaining `G_2` is now an exact bounded univariate
endpoint.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_j0_affine_router
source chart: F_b=E_G=X_*=J_*=L_*=0 with bD_*!=0
exact identities:
  L_*=45bB+6E_G
  R_J+5E_G=-75bB+3(Tq-5bM)
  J_*=-D_*R_J+150bX_*
where:
  B=96q^2+(216-32b)q+3b^2+18b+315
  R_J=3D_*+5P-3600bq^2
  T=-280b^2+2241b+3465
  M=29b^2+234b+81
reconstruction: q=5bM/T
denominator guard:
  29T+280M=9(14501b+13685)
  14501^2 M(-13685/14501)=-23972710684
  residues=(3690,44145,312391,1797093080), all nonzero
univariate endpoint:
  Bhat=T^2 B(b,5bM/T)=0        degree <=6
  Ehat=T^2 E_G(b,5bM/T)=0      degree <=7
  Fhat=T^2 F_b(b^2,5bM/T)=0    degree <=10
  Xhat=T^3 X_*(b,5bM/T)=0      degree <=11
retained: G_2, structural, role, P_4, saturations, and arithmetic lifts
scope fence: no common-root, ambient-degree, emptiness, or critical closure
checker state: source-complete primary and independent audit; AST-only local
               validation; unexecuted
checker hashes:
  verify.py       49fc746508f1ae9fb996dc68d7013585128949d5972c44726ec2b94236640919
  verify_audit.py 9489a527fe1ffd9374b34cce03dcfb45e03f8160d83e1e293af26605bc10ef03
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
```

**2026-07-29, L1 h=7 exceptional-`J_*=0` packet extension:** the same
spend-blocked four-prime packet now computes a four-way Bezout gcd
certificate for `Bhat,Ehat,Fhat,Xhat`, factors the monic gcd, and classifies
the ambient endpoint.

```text
guard classification: every irreducible gcd factor dividing T is marked
                      t_zero_factor and excluded from the legal chart
legal classification: retain every non-T factor, at any degree
quadratic diagnostic: separately list the degree-at-most-two legal factors
EMPTY meaning: no legal algebraic coefficient root exists
HIT meaning: every listed legal factor continues to G_2, structural, role, P_4,
             saturation, and arithmetic-lift replay
IDENTICALLY_ZERO_FAMILY meaning: inconclusive, never closure
launcher:
  85ec64690ef625ec3f1e4f1815b95064ad85698d36e4a07826aa9ad6f51827ab
checker:
  b89c741dbe723d8ee49992f437b6973f9f0559e4cd68105428de24a72e0aef46
resource delta: none; four one-CPU, 512 MB, 60-second tasks, no retries,
                atomic partial output
estimated total cost: still below $0.01
status: source-complete, AST-only validation, unrun; Modal spend-blocked
compute spend: none
DAG delta: none; this consumes the new J-zero affine router
upstream custody:
  PR: https://github.com/przchojecki/rs-mca/pull/1120
  commit: 38b4c8b5dc08143ee7d284bd0e53b8197175ce64
  combined verifier:
    bb5af22c100f06117b1a9165c0afaad86f09576e697571ae8c0bc7e6f75bef13
  launcher/checker parity:
    85ec64690ef625ec3f1e4f1815b95064ad85698d36e4a07826aa9ad6f51827ab
    b89c741dbe723d8ee49992f437b6973f9f0559e4cd68105428de24a72e0aef46
  export state at pin: OPEN, DRAFT, MERGEABLE
next route-deciding action: continue exact hand elimination on the retained
                              h=7 endpoint while all Modal work waits
```

**2026-07-29, L1 h=7 exceptional-`J_*=0` structural compiler:** the last
coefficient chart retaining `G_2` now returns to every original structural
definition and leaves only two additional univariate filters.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_j0_structural_consistency_compiler
input: E_G=X_*=J_*=L_*=F_b=0, q=5bM/T, b(b+3)D_*T!=0
exceptional reconstruction:
  Q_0=q^2/3
  G_2=(q^2/3-x ell+20+8q/3+D_*/(3600b))/A
  H=ell-G_2, Y=(ell-2G_2)/A-x, V=G_2+xY+Y^2
remaining structural filters:
  Z_D^j=Num(D_*/(3600b)-YV)
  Z_R^j=Num(R_0-G_2(ell-G_2)+xq^2/3+(A+x)D
            +15+23q/4+q^2/8)
bivariate bounds:
  (total degree,q-degree) <= (12,6), (8,4)
after q=5bM/T:
  deg Zhat_D^j<=24, deg Zhat_R^j<=16
complete endpoint:
  Bhat=Ehat=Fhat=Xhat=Zhat_D^j=Zhat_R^j=0
retained: role-discriminant weld, P_4, saturations, arithmetic lifts
scope fence: no common-root, ambient-degree, emptiness, or critical closure
checker state: source-complete primary and independent audit; AST-only local
               validation; unexecuted
checker hashes:
  verify.py       528d69d77f27cdf4a74cda6c853474cdacb498c7ef5f051b7cb556b29171a005
  verify_audit.py af4e8a64796a0948978bcb40e913b23d9c4197262bb4f8861dbee35527c0f5e2
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
```

**2026-07-29, L1 h=7 exceptional-`J_*=0` six-filter packet:** the shared
spend-blocked request now includes the two structural numerators in the
same exact gcd/factor certificate.

```text
family: Bhat,Ehat,Fhat,Xhat,Zhat_D^j,Zhat_R^j
certificate: six-way Bezout identity, complete monic-gcd factorization,
             T-zero guard classification, and quadratic-subfield diagnostic
EMPTY meaning: no legal algebraic coefficient-and-structural root exists
HIT meaning: every listed legal factor continues to role, P_4, saturations, lifts
IDENTICALLY_ZERO_FAMILY meaning: inconclusive, never closure
launcher:
  4490ec4cfdbbf36c45c4bdaa50177b1e8b26879ab513822d20af1e644702e56a
checker:
  f1074ddb54f89bee37c2f89bf086b76c4d4a017745968c27937339ccf11a89b3
resource delta: none; four one-CPU, 512 MB, 60-second tasks, no retries,
                atomic partial output
estimated total cost: still below $0.01
status: source-complete, AST-only validation, unrun; Modal spend-blocked
compute spend: none
DAG delta: none; this consumes the new J-zero structural compiler
upstream custody:
  PR: https://github.com/przchojecki/rs-mca/pull/1120
  commit: 7ef9a407c23bedc8546427929fba05484cb166d4
  combined verifier:
    446123cea29919792b819e5b23459df6a4a8e6f62018b6402debc2bcf06febc0
  launcher/checker parity:
    4490ec4cfdbbf36c45c4bdaa50177b1e8b26879ab513822d20af1e644702e56a
    f1074ddb54f89bee37c2f89bf086b76c4d4a017745968c27937339ccf11a89b3
  export state at pin: OPEN, DRAFT, MERGEABLE
next route-deciding action: inspect whether the role and P_4 filters admit
                              a similarly exact reduction
```

**2026-07-29, L1 h=7 exceptional-`J_*=0` role/`P_4` compiler:** the role
and `P_4` layer is now an exact two-filter extension for each alternative
official role packet.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_j0_role_p4_compiler
fixed role packet:
  Phi(X,Y)=c_2X^2+c_1XY+c_0Y^2
  delta_Phi=c_1^2-4c_2c_0, c_0*delta_Phi!=0
reconstructed role values:
  R_j=A(3Y_j^2+2xY_j+G_j)
  S_j=(Y_j-A)V_j-q^2/3
role filters:
  L_Phi=18c_0S_j+9c_1R_j+c_0q(b-6)
  W_Phi=c_0^2(q^2(b-6)^2+144qR_0)-81delta_Phi R_j^2
bivariate bounds:
  (total degree,q-degree) <= (12,6), (18,8)
after q=5bM/T:
  deg Lhat_Phi<=24, deg What_Phi<=34
d reconstruction for either ambient root c_0eta^2+c_1eta+c_2=0:
  d=3(eta R_j-S_j)/q
exact P_4 payment:
  27Phi(R_j,S_j+qd/3)+c_0qP_4=U_1d+U_0
  L_Phi=What_Phi=0 iff U_1=U_0=0
complete endpoint per role:
  six coefficient/structural filters plus Lhat_Phi=What_Phi=0
alternatives: 21 official role packets, each with two eta branches
retained: every saturation on reconstructed d and all arithmetic lifts
scope fence: no eight-filter common-root, lift, emptiness, or critical closure
checker state: source-complete primary and independent audit; AST-only local
               validation; unexecuted
checker hashes:
  verify.py       0128bd70e9f7262450c0b7c87daf1ac69047ef9a3b346777a295d00a8272459d
  verify_audit.py d18fd47835f4e61fdd153deba53743b2b93cb75b89ec3916250e82ea4dc9049e
compute spend: none
DAG delta: one PROVED background node and two edges; no critical status flip
upstream custody:
  PR: https://github.com/przchojecki/rs-mca/pull/1120
  commit: ea2bd60abec747ed041493b77a135cd2e9388057
  combined verifier:
    b103bf22b73736dd51f97a03db83c07de681a20805448749cd98e96c7e13c7a6
  export state at pin: OPEN, DRAFT, MERGEABLE
next route-deciding action: decide whether to add 21 role-specific gcd
                              families to the unrun packet or attack
                              arithmetic lifts by hand
```

**2026-07-29, L1 h=7 certificate field-scope correction:** the unrun
fully-proportional packet no longer treats the role field as the coefficient
field.

```text
audited distinction: each official role root eta lies in F_(p^2), but no
                     dependency proves b in F_(p^2)
unsafe old rule: discard every common-gcd factor of degree greater than two
sound global rule: discard only factors on an already excluded guard chart;
                   global EMPTY means no legal factor remains at any degree
diagnostic retained: degree-one/two legal factors are reported separately as
                     the quadratic-subfield subset
singular guard: A=1575-247z
J-zero guard: T=-280b^2+2241b+3465
IDENTICALLY_ZERO_FAMILY: remains inconclusive
launcher:
  4490ec4cfdbbf36c45c4bdaa50177b1e8b26879ab513822d20af1e644702e56a
checker:
  f1074ddb54f89bee37c2f89bf086b76c4d4a017745968c27937339ccf11a89b3
validation: AST-only; arithmetic packet remains unrun and spend-blocked
compute/resource delta: none
DAG delta: none; this repairs certificate semantics, not a mathematical close
upstream custody:
  PR: https://github.com/przchojecki/rs-mca/pull/1120
  commit: d56f8d224271c4f2509ea75da345470fd5e0c658
  launcher/checker parity:
    4490ec4cfdbbf36c45c4bdaa50177b1e8b26879ab513822d20af1e644702e56a
    f1074ddb54f89bee37c2f89bf086b76c4d4a017745968c27937339ccf11a89b3
  export state at pin: OPEN, DRAFT, MERGEABLE
next route-deciding action: seek an actual field-descent or bounded Frobenius
                              equation before extending to 21 role families
```

**2026-07-29, L1 h=7 coefficient-field descent:** the official normalized
cubic data now have an exact generated-field bound.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_coefficient_field_degree_eight_router
official rows: p=2^t-1, t in {13,17,19,31}; n=2^(t+3)
order calculation:
  p^2=1-n/4 mod n, p^4=1-n/2 mod n, p^8=1 mod n
  hence ord_n(p)=8
field descent: P=(W+1/d)L divides W^n-1, so the normalized roots,
               d, every monic color-fiber factor coefficient, and
               b=4dg_1-15 lie in F_(p^8)
exact factor rule: an irreducible b factor is official-eligible iff its
                   degree divides 8, namely degree in {1,2,4,8}
packet schema:
  legal_factors                 all non-guard factors
  cyclotomic_field_factors      exact degree-1/2/4/8 official subset
  quadratic_subfield_factors    diagnostic degree-1/2 subset
closure semantics: cyclotomic_field_status=EMPTY excludes the official
                   chart; global_status=EMPTY is the stronger algebraic close
launcher:
  59bb96e395c4eac8ada98417bc7e68f59c905cb7dcfec9219aad71578097119b
checker:
  d25dc17b956ace1f4faa97acc533fe99492089658eb5b103bcfc70711667a609
node checker sources:
  verify.py       e4b8c4c805a8b8544012dc9e8e4b72e8ad5768f05ca2505da8d5a5c60450aae1
  verify_audit.py 01227ec4aefb12e920ff7ec0a5247c061710fecdab1ca58acc8cb87e93c908c6
validation: AST-only for all four sources; DAG, harness, joint protocol,
            orbit census, and manifest passed; arithmetic remains unrun
compute/resource delta: none; existing spend-blocked request unchanged
DAG delta: one PROVED background node and three edges; no critical status flip
upstream custody:
  PR: https://github.com/przchojecki/rs-mca/pull/1120
  commit: dae288582936d6d96a77235e91199189af1d04f1
  combined verifier:
    0c11e7f6275f81986f0f0e5df294c1498e6e7d8ac7be09cd5f9b828f978dbde7
  launcher/checker parity:
    59bb96e395c4eac8ada98417bc7e68f59c905cb7dcfec9219aad71578097119b
    d25dc17b956ace1f4faa97acc533fe99492089658eb5b103bcfc70711667a609
  export state at pin: OPEN, DRAFT, MERGEABLE
next route-deciding action: reconsider 21 role families against the exact
                              degree-1/2/4/8 survivor interface
```

**2026-07-29, L1 h=7 official-role gcd packet:** the spend-blocked
fully-proportional packet now compiles every role alternative through the
exact degree-eight field interface.

```text
shared filters per row:
  Bhat,Ehat,Fhat,Xhat,Zhat_D^j,Zhat_R^j
official alternatives:
  H1,H2,H3 and Q4+/Q4- through Q12+/Q12- (21 total)
per-role filters:
  Lhat_Phi, What_Phi
per-role certificate:
  eight-way Bezout identity, complete monic-gcd factorization,
  T-zero guard classification, legal factors, exact degree-1/2/4/8
  cyclotomic-field factors, and degree-1/2 diagnostic factors
disjunction discipline: each role is certified separately; roles are never
                       intersected
aggregate semantics:
  ALL_EMPTY    all 21 official role charts are empty for the row
  HIT          at least one role has an official-field-eligible b factor
  INCONCLUSIVE at least one eight-polynomial family is identically zero
HIT obligations: reconstructed-variable saturations, both eta roots where
                 applicable, and arithmetic lifts
launcher:
  421ef85dbe2f6a5154c348999de3cb79df182cb903d308ba3247575b3c3c2b16
checker:
  e42629a472339216a8dca3532b43300cb34202f539312458e7adca523bd2e61f
guard extension:
  for each official-field factor reduce every named guard to
  u(b)eta+v(b) modulo c_0eta^2+c_1eta+c_2
  exact statuses: BOTH_ETA_BRANCHES / ONE_ETA_BRANCH / ALL_ETA_REJECTED
  individual quotient remainders and quadratic norms preserve rejection
  reasons; the aggregate guard product is checked independently
validation: AST-only; packet arithmetic remains unrun
resource delta: none; four one-CPU, 512 MB, 60-second tasks, no retries,
                atomic partial output; completion time is unmeasured
compute spend: none; Modal workspace remains spend-blocked
DAG delta: none until a complete checked result exists
upstream custody:
  PR: https://github.com/przchojecki/rs-mca/pull/1120
  commit: 38b9766ca2421f89d5d9f735bdd5f39490658346
  combined verifier:
    8b0224fd837c02786982ed90e2e79b5d3b61b5f360551bf603af3c7bb787f50a
  launcher/checker parity:
    c5ccd14b02e0b0119fbcbbaa20f7eae7214716c13a2e9b8158cce50674bb51af
    92b6d6d9e42b15a9c476aea154bfabc57b652a5d54d203c15c79036f09051643
  export state at pin: OPEN, DRAFT, MERGEABLE
  current custody audit:
    PR #1120 was closed after manual consolidation at upstream commit
    0f7476f0; the written local algebra was retained, but the PR-local unrun
    launcher/checker packet was intentionally not imported into main
next route-deciding action: when spend access is explicitly restored, run
                              and replay all four rows; meanwhile attack the
                              remaining saturation/lift interface by hand
```

**2026-07-29, L1 h=7 J-zero outer-lift compiler:** a retained official role
candidate now has one exact finite outer replay rather than four vague lift
labels.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_j0_outer_lift_compiler
field: K=F_(p^8); eta and mu_8 lie in its quadratic subfield
normalized role enumeration:
  (beta,gamma) in (mu_8\{1})^2, beta!=gamma,
  eta=(beta-1)/(gamma-beta)                         at most 42 pairs
reconstruction:
  Q=W^2+(g_1+y)W+v
  G=Q(W)(W-y)
  F=G+aQ+B
  L=FG
  E_norm=1+(beta-1)F/B
exact color values: 1 on F, beta on Q, gamma at y
outer replay:
  zeta=d^(p+1), zeta^8=1
  W^(p+1)=tau E_norm mod L for some tau in mu_8
consequence:
  P=(W+1/d)L divides W^(8(p+1))-1
  c^p=1+zeta/d
complexity: modular powering only modulo degree-six L; no degree-n object
scope fence: no common-root, guard, norm, or congruence outcome; no inner
             lift; no other h=7 shape; no critical status flip
checker state: primary and independent audit sources written; AST-only
               local validation; unexecuted
checker hashes:
  verify.py       da75ed3e542d03bc03f97e2c0038eb03f003e871d806152f5ee8c90a6b1c3c5e
  verify_audit.py a40dcd461807ab3fbdb1ee8b16c1e2776c99b2db0f6321b2487fb6645a138191
compute spend: none
DAG delta: one PROVED background node and six edges; no critical status flip
upstream custody:
  predecessor: PR #1120 was manually consolidated at upstream 0f7476f0 and
               closed before this theorem was exported
  follow-up PR: https://github.com/przchojecki/rs-mca/pull/1121
  upstream-base: 93fba1be3f3299b0ba4708d88715377bbb656e45
  export commit: 55d3812bb1dc7a23f8573cbb9ec4f5b16aa5ed40
  accepted surface: experimental/experiments.tex plus the required
                    experimental/agents-log.md coordination entry
  validation: git diff --check; static proof review only, no TeX or
              arithmetic execution
  export state at pin: OPEN, DRAFT, MERGEABLE
next route-deciding action: compile the full inherited guard product into
                              per-factor and per-role rejection reasons
```

**2026-07-29, L1 h=7 J-zero exact guard compiler:** the retained role
interface no longer carries an unspecified bundle of saturations.

```text
node proved: l1_mersenne_hnf_m8_order_one_cubic_three_two_one_j0_guard_compiler
scaled factors:
  Qhat=X^2+(x+Y_j)X+V_j
  Ghat=Qhat(X)(X-Y_j)
  Fhat=Ghat+A Qhat+S_c
  Lhat=Fhat Ghat=d^6 L(X/d)
role identities:
  S_c=eta R_j, lambda=1+eta^(-1), R_j=A Qhat(Y_j)
collapsed common-quadratic guard:
  a B (lambda-1) Q(y)=R_j^2/d^6
exact-fiber identities:
  disc(Ghat)=disc(Qhat)Qhat(Y_j)^2
  Res(Ghat,Fhat)=lambda S_c^3
  disc(Lhat)=disc(Fhat)disc(Qhat)Qhat(Y_j)^2
             *lambda^2*S_c^6
residual exact-fiber test: disc(Qhat)*disc(Fhat)!=0
split/constant tests: Lhat(-1)!=0 and K_6=Lhat(0)!=0
finite algebraic ledger:
  b(b+3)D_*T*q*d(d+1)(q-d)*Delta*W*K_6*R_j
  *eta(eta+1)*disc(Qhat)*disc(Fhat)*Lhat(-1) != 0
semantics: evaluate after each b/eta/color reconstruction in F_(p^8);
           reject a zero entry with its exact named reason
scope fence: no common-root or guard outcome; no norm/congruence outcome;
             no inner lift, other shape, or critical status flip
checker state: primary symbolic and independent exact-rational sources
               written; AST-only local validation; unexecuted
checker hashes:
  verify.py       1b09c4d4871b8a315f84de3b090555fce98f21de5d133b8f8e3705f2edd9278b
  verify_audit.py 137e467c42b8639eb73b024f3f214698edb665b3ec5774d572ad56d403cb006e
compute spend: none
DAG delta: one PROVED background node and six edges; no critical status flip
upstream custody: not yet exported; prefer a small follow-up after PR #1121
                   is triaged
next route-deciding action: compile the degree-six outer replay for every
                              guard-surviving eta/color branch, without
                              launching while spend is blocked
```

**2026-07-29, L1 h=7 J-zero guard packet extension:** the source-complete
role packet now consumes the proved guard compiler without constructing an
extension field or selecting roots.

```text
candidate algebra:
  A_f=F_p[b]/(f), f one eligible irreducible degree 1,2,4,8
  eta relation c_0eta^2+c_1eta+c_2=0
per guard:
  reduce to u(b)eta+v(b) in A_f[eta]
  norm=v^2-(c_1/c_0)uv+(c_2/c_0)u^2
  PASS       norm!=0: both eta branches pass
  ONE_FAIL   norm=0 but (u,v)!=(0,0): exactly one branch fails
  BOTH_FAIL  u=v=0: both branches fail
aggregate:
  multiply all guard residues in the same quadratic algebra
  BOTH_ETA_BRANCHES / ONE_ETA_BRANCH / ALL_ETA_REJECTED
  row summary remains INCONCLUSIVE if any eight-filter family is
  identically zero
launcher:
  421ef85dbe2f6a5154c348999de3cb79df182cb903d308ba3247575b3c3c2b16
checker:
  e42629a472339216a8dca3532b43300cb34202f539312458e7adca523bd2e61f
checker scope: independently regenerate all guard templates, reductions,
               norms, factor ledgers, and role/row summaries
validation: AST-only; no source polynomial, factorization, or guard arithmetic
            executed locally
resource delta: none; same four one-CPU, 512 MB, 60-second tasks, no retries
completion time: unmeasured; a 60-second miss returns partial rows only
compute spend: none; Modal remains spend-blocked
DAG delta: none; no result exists
upstream custody: not exported; PR #1120 contains the historical role-only
                   hashes and was already manually consolidated
next route-deciding action: add normalized color matching and the exact
                              degree-six outer replay to guard survivors
```

**2026-07-29, colored-Frobenius HNF payoff correction:** Fable WAVE-32's
scope objection is valid. The HNF lane is finite, but its connection to the
critical L1 budget is much narrower than its node count suggests.

```text
node proved: l1_mersenne_hnf_payoff_scope_router
post-router t=p obligation lattice:
  m=4:  4 rows * {h=2}       = 4 cells
  m=8:  4 rows * {h=2,...,7} = 24 cells
  m=16: 1 row  * {h=2,...,15}= 14 cells
  total                         42 cells
embedded-family compatibility: 23 even cells; 19 odd cells
complete next-to-maximal payoff:
  h=7 on four rows plus h=15 on one row gives 42 -> 37
current J-zero cubic 3+2+1 payoff:
  no complete row/degree cell until every sibling order-one chart is paid
full t=p residual payoff:
  owner-pruned minimum width p -> p+1 only
  unfloored generic packing improvement=(n-a+p)/p<m+2<=18
scope fence:
  no wider exchange, arbitrary-target Toeplitz/Pade section, aggregate
  first-owner sum, L1 close, or prize status change
dedicated strategy note: notes/L1_HNF_PAYOFF_LADDER.md
compute spend: none
validation: proof and replay sources written; arithmetic replay not run
priority correction:
  do not extend the J-zero packet merely because another finite compiler is
  available; require a plausible full-cell close or independent upstream
  split-pencil value
next route-deciding action:
  audit the global Toeplitz/Pade and first-owner frontiers, then select the
  smallest theorem that changes a critical budget rather than one HNF chart
```

**2026-07-29, M31 adjacent quotient-rotation spectrum:** the first global-Q
audit produced an exact direct-list route verdict rather than another
conditional max-fiber statement.

```text
node proved: rate_half_m31_adjacent_quotient_rotation_product_spectrum
upstream source: integrated cyclic quotient-rotation list-floor theorem
row: Mersenne-31 ordinary LIST stress row, epsilon=2^-100
(n,k,a+): (2^21,2^20,1116023)
specialization: c=2^16, N=32, d=1, m=17, s=1911
exact 32-class product spectrum:
  16 * 8,287,155
   8 * 8,286,755
   5 * 8,286,751
   3 * 8,286,750
  total binom(31,17)=265,182,525
structured lower floor: 8,287,155
published average floor: 8,286,954
improvement: 201
budget: 16,777,215
remaining headroom: 8,490,060
two-copy comparison: B*-2M=202,905>0, but distinct product classes do not
                     share a received-word prefix and cannot be added
verdict: exact route calibration; the zero-remainder construction alone does
         not falsify or prove the adjacent row
object fence: LIST only; no MCA, U_Q upper payment, or 2^-128 claim
compute spend: none; proof by Fourier/Ramanujan sums
replay state: independent DP and Ramanujan verifier sources written, unrun
upstream custody:
  PR: https://github.com/przchojecki/rs-mca/pull/1123
  branch: agent/m31-quotient-rotation-spectrum
  commit: b6619f20f55beb9183bb0e9d591d0630c8e3f306
  state at pin: OPEN, READY FOR REVIEW
  accepted surface: experimental/experiments.tex, one agents-log entry, and
                    one stdlib-only dual replay
  replay: direct subset-product DP and independent Ramanujan-sum spectrum
          both PASS under ordinary and optimized Python
next route-deciding action: return to the surviving Pade/first-owner upper
```

**2026-07-29, M31 rank-seven two-block incidence router:** retaining both
agreement blocks replaces the weak nineteen-slice picture by a collective
middle-band locator terminal.

```text
node proved: l1_m31_rank7_zero_excess_two_block_incidence_router
source terminal: Q=147595, k=4981, proper-G zero-excess mass
exact support profile per member:
  planted q_i; external 72428-q_i
pairwise total intersection: at most 4980
constant-weight tail caps:
  q_i<=4980   -> aggregate mass <=40
  q_i>=67448  -> aggregate mass <=7
dangerous-class consequence:
  at least 2157882 distinct locators with 4981<=q_i<=67447
exact mean-degree inequality:
  (N Q-M m g)^2 <= gE(MN(m-t)+M^2(Nt-m^2))
  Nt-m^2=898676
  forbidden mass implies 23945<Q/M<24860
scope fence: no middle-band upper bound, Q=147595 payment, v4 atom,
             higher-rank theorem, row close, or Prize status change
compute spend: none; proof is analytic
replay state: two exact verifier sources written; local arithmetic unrun
next route-deciding action: attack the distinct middle-band locator family
                              through a whole-family Pade/first-owner theorem
```

**2026-07-29, M31 dense primitive decorated top-shift router:** the
middle-band terminal forces a local high-degree object rather than merely a
large aggregate.

```text
node proved: l1_m31_rank7_dense_top_decorated_shift_pair_router
exact-weight pair deficit:
  D <= (M^2(Nt-m^2)/N+M(m-t))/2
  Nt-m^2=898676
at forbidden mass:
  more than 10% of all pairs have intersection exactly t=4980
  one member has at least 215793 top neighbors
top pair normal form:
  L_i=J A, L_j=J B, deg J=4980, deg A=deg B=w+1=67448
  A C_i-B C_j=c!=0
automatic guard:
  gcd(C_i,C_j)=1, so the counted edges are primitive decorated pairs
projective compression:
  one difference direction has at most 15 line members / 14 neighbors
  forbidden mass forces at least ceil(215793/14)=15414 distinct monic
  degree-4980 divisors of the anchor support locator in the 6D direction
  space
exact sufficient successor:
  prove a source-bound local neighbor cap <=215792, or the equivalent
  fixed-support projective divisor-direction cap <=15413
scope fence: no such upper cap, upstream atom, Q=147595 payment, higher-rank
             theorem, row close, or Prize status movement
compute spend: none; proof is analytic
replay state: two exact verifier sources written; local arithmetic unrun
upstream custody:
  PR: https://github.com/przchojecki/rs-mca/pull/1124
  branch: agent/m31-rank7-dense-top-router
  head commit: 36721bfb8538bef480048db627d0ea726f8a69f0
  theorem commit: 4cd4cf79ef3a9f19dae515c27d2cc4b7126f636b
  state at pin: OPEN, DRAFT, MERGEABLE
  accepted surface: experimental/experiments.tex plus one agents-log entry
  validation: git diff --check; static proof review only
next route-deciding action: attack the first-above-threshold primitive
                              decorated equation with the Pade owner data
```

**2026-07-29, M31 fixed-support divisor-cap falsifier:** projective
compression does not by itself supply the successor upper theorem.

```text
node proved: l1_m31_fixed_support_divisor_direction_cap_route_cut
construction:
  choose a degree-4979 divisor R of the degree-72428 anchor locator
  V=span{R X,R,1,X,X^2,X^3} is 6D and common-zero-free
  J_a=R(X-a) over every remaining anchor root
exact projective divisor count: 72428-4979=67449
route verdict:
  universal geometry-only cap 15413 is false
  fixed-support/projective-code methods cannot close the terminal alone
surviving load-bearing data:
  actual received-word realization and A C_i-B C_j=c!=0 decorations
scope fence: no source-compatible list counterexample, no refutation of a
             target-sensitive cap, no row or Prize movement
compute spend: none; explicit algebraic construction
next route-deciding action: classify or pay the one-root-swap pencil after
                              imposing the decorated Pade equation
```

**2026-07-29, M31 actual-list core-shadow payment:** the one-root-swap
counterfixture is large only after the received-word semantics are erased.

```text
node proved: l1_m31_top_neighbor_core_shadow_payment
fixed degree-4979 core R:
  every matching top neighbor lies in a_0+span{R X,R}
  affine-span list cap: 241 words including the anchor
  actual top-neighbor cap: 240 across all roots and scalar labels
general core hierarchy:
  B_r=floor(C(N-k+r+1,r+1)/C(w+r+1,r+1))-1
  each fixed degree-(t-r) core supports at most B_r neighbors
dense-anchor consequence:
  215793*4980 neighbor/core incidences
  at least ceil(215793*4980/240)=4477705 distinct degree-4979 cores
route verdict:
  the 67449-direction one-plane counterfixture is paid for actual lists
  the live obstruction is cross-core aggregation/ownership
scope fence: no global core count, local cap 215792, Q=147595 payment,
             row close, or Prize movement
compute spend: none; analytic use of the proved affine-span theorem
replay state: two exact verifier sources written; local arithmetic unrun
upstream custody: PR #1124 head 36721bfb8538bef480048db627d0ea726f8a69f0
next route-deciding action: combine the core-shadow hierarchy with the
                              planted/external split and first-owner ledger
```

**2026-07-29, M31 source-head saturation:** maximal overlap saturates the
proper-`G` reduced determinant on every top edge.

```text
node proved: l1_m31_top_pair_source_head_saturation_router
top-pair source identity:
  A_i b_j-A_j b_i=(gamma_j-gamma_i) gcd(H_i,H_j)
  a_j-a_i=(gamma_j-gamma_i) C_ij gcd(H_i,H_j)/L_S
  gamma_i=[X^(d-1)]f_i, and every top edge has gamma_i!=gamma_j
head-fiber cap:
  same-head supports have intersection at most 4979
  Cauchy cap = floor(1053557*67449/154881)=458812
dangerous-family consequences:
  at least five head values
  at least 1699117 members with deg f_i=d-1
  the original 215793-neighbor anchor forces 71643276
  distinct (core,neighbor-head) pairs
  one nonzero-head anchor has at least 107897 top neighbors
  that anchor forces 2238863 degree-4979 cores and 35821804
  distinct (core,neighbor-head) pairs
route verdict:
  top-pair decoration is now a source-head difference, not a free scalar
  the live theorem is cross-head/core ownership or aggregation
scope fence: no head-spectrum bound, owner add-back, Q=147595 payment,
             row close, or Prize movement
compute spend: none; analytic source-degree saturation
replay state: two exact verifier sources written; local arithmetic unrun
upstream custody: PR #1124 head 36721bfb8538bef480048db627d0ea726f8a69f0
next route-deciding action: test the active head/projective-line owner for
                              disjoint coverage of the colored core shadow
```

**2026-07-29, M31 source-head infinity-owner route cut:** the source head is
the extended-RS evaluation-at-infinity functional, but this does not activate
the existing deletion owner.

```text
node proved: l1_m31_source_head_infinity_owner_route_cut
exact interface:
  fixing gamma is one affine hyperplane / one infinity label
  the deletion recurrence counts agreements with one fixed received label
route verdict:
  one recurrence run pays at most one gamma fiber
  changing the infinity label changes the received word
  separate runs cannot be summed as one first-match ledger
abstract no-go witness:
  assign every neighbor a private head and 4980 private cores
  head/core/colored-cell loads are all 1 for arbitrary neighbor mass
scope fence:
  no actual source counterexample and no obstruction to a new coupled
  finite/infinity or Pade owner theorem
compute spend: none; functional and incidence audit
upstream custody: PR #1124 head 36721bfb8538bef480048db627d0ea726f8a69f0
next route-deciding action: derive a source-sensitive aggregate from the
                              complete reduced-determinant/Pade family, or
                              leave M31 rank seven and attack another live
                              critical target with a closing interface
```

**2026-07-29, E1 pure-cofactor common-prime associate router:** the completed
profile-`(3,6,S=18)` cofactor campaign has a new non-computational aggregate
interface.

```text
node proved: e1_pure_cofactor_common_prime_associate_router
current residual cofactors: 2,4,8,16
m=16 residual: primitive multiplicity-four support only
fixed row/root factorization:
  (alpha)=P_r(1-zeta_256)^mu
  alpha/(1-zeta_256)^mu generates P_r
same-row consequence:
  every two normalized survivors differ by an algebraic unit of Z[zeta_256]
fixed-cofactor Cramer-Hadamard box:
  max coefficient of u and u^(-1) <= 1006,503,251,125
  for cofactors 2,4,8,16 respectively
shift/sign quotient:
  256 torsion associates per orbit
  remaining classes inject into the full rank-63 unit log lattice
  ||lambda||_1 <= 2(D+sqrt(128D)), D=log(18^64/(2^mu p))
exact maximum-weight target:
  at most 367 log-lattice points across mu=1,2,3,4
  368 orbits already exceed the complete edge budget
route verdict:
  residual maximum-weight vectors are finite bounded unit/inverse families,
  not unrelated norm-divisibility events or an unbounded unit search
scope fence:
  no associate count, lower-profile payment, E1 image bound, row close,
  or Prize status movement
compute spend: none; ideal factorization proof
next route-deciding action: count or sharply bound the inverse-pair boxes
                              or the equivalent full-unit log-lattice body,
                              while retaining both sparse profile products
                              and the exact lower-profile weighted ledger
```

**2026-07-29, E1 conductor-256 full-unit circular basis:** the unknown unit
index in the preceding route is eliminated by a published unconditional
theorem.

```text
node proved: e1_conductor256_full_unit_circular_basis
published inputs:
  Miller, Acta Arith. 164.4 (2014), Theorem 2.1:
    h(Q(zeta_256)^+)=1 unconditionally
  prime-power Kummer-Sinnott unit-index formula:
    [full units : circular units]=h+
exact consequence:
  every u in Z[zeta_256]^x has one unique form modulo mu_256
    u=product_(a=3,5,...,127) eta_a^x_a, x_a in Z
  eta_a=zeta^((1-a)/2)(1-zeta^a)/(1-zeta)
  the full log lattice is the 63-column sine-ratio lattice
route verdict:
  the E1 367-orbit target is now an explicit Z^63 sparse-associate count;
  no unknown finite-index correction or full-unit/circular-unit gap remains
scope fence:
  the full cyclotomic class number is not one; no regulator bound,
  lattice-point count, sparse-product count, lower-profile payment,
  E1 image bound, row close, or Prize status movement
compute spend: none; published theorem import and exact specialization
next route-deciding action: derive certified exponent bounds and combine
                              them with exact sparse multiplication before
                              proposing any lattice enumeration
```

**2026-07-29, E1 character-diagonal exponent router:** the requested
preflight is now theorem-level and requires no numerical search.

```text
node proved: e1_conductor256_character_diagonal_exponent_router
group coordinate:
  G=(Z/256Z)^x/{+-1}=<5>, |G|=64
  extend the 63 basis exponents to one zero-sum integer vector xi on G
exact log map:
  lambda_s=sum_t xi_t f_(s+t)
  Fourier(lambda)_j=kappa_j Fourier(xi)_(-j)
  f_t=2log|sin(pi*5^t/256)|
nonvanishing:
  every kappa_j, 1<=j<=63, is nonzero because the complete unit-log basis
  has rank 63; floating-point separation is not a premise
fixed-cofactor consequence:
  the AM-GM radius R gives explicit Fourier, L2, coordinate, and weighted
  ellipsoid bounds on the unique integer exponent vector
complete successor filter:
  certified outward kappa intervals + exact u/u^(-1) coefficient boxes +
  exact sparse multiplication in Z[X]/(X^128+1)
scope fence:
  no exponent enumeration, 367-orbit payment, lower-profile payment, E1
  image bound, row close, or Prize status movement
compute spend: none
next route-deciding action: obtain a certified eigenvalue interval table and
                              count projection; authorize enumeration only
                              if the exact sparse branch-and-bound is cheap
```

**2026-07-29, L1 balanced-pencil anchor determinant atlas:** the global
primitive exact shell now has an exact list-side bridge to the BC
split-pencil hierarchy.

```text
node proved: l1_balanced_pencil_anchor_determinant_atlas
fixed-anchor coordinate:
  Delta_0=A_0B-B_0A is an affine bijection from the monic balanced
  coefficient body to F[Z]_(<=s-1)
global Pade transport:
  choose the Bezout-dual denominator J with gcd(J,W_0)=1
  W(P-P_0)=gamma Delta_0L_0 and W=Delta_0J mod W_0
  every owner is one gcd stratum of this single affine family
global exact-shell normal form:
  Delta_0J=Q_Delta W_0+R_Delta
  W_Delta=W_0+R_Delta
  exact iff W_Delta|Omega and gcd(Delta_0,1-Q_Delta)=1
  split numerator divisibility is automatic
exact owner recovery:
  Delta_0=(D/gamma)R
  D=gcd(W_0,W)=gcd(Delta_0,W_0)
  j=s-1-deg D=k-1-deg G, h=w+1+j, deg R<=j
fixed-D payment:
  neighbor quotients lie in projective dimension r<=j+1
  Y=X+rem_X((R/gamma)J)
  root-matroid bases give
    |C_D|<=floor(C(m,r)/(h-r+1))
  exact codeword distance independently gives
    |C_D|<=floor(C(m,j+1)/C(h,j+1))
  use the smaller bound
  j=0 specializes to floor(m/(w+1)), the one-pencil moving-root cap
route verdict:
  coefficient multiplicity, owner ambiguity, and fixed-owner split
  multiplicity are closed exactly
  all owners are represented in one primitive quotient/remainder graph
  the live theorem is a row-sharp count or typed transport of that graph
scope fence:
  the number C(omega,s-1-j) of possible D owners can be exponential;
  no row reserve, L1 status, or Prize status movement
compute spend: none; exact module determinant and matroid proof
upstream custody:
  PR #1125, ready for review, head a663e68df61a49a30289ea148e6f23624b447c89
next route-deciding action: seek a received-word/Pade priority map that
                              coalesces determinant owners across D, or a
                              route cut proving such coalescence impossible
```

**2026-07-29, E1 certified character-spectrum preflight and route cut:** the
finite rank-63 unit body is now numerically certified, and its generic
enumeration is decisively unpriced.

```text
node proved: e1_conductor256_character_eigenvalue_preflight
certification:
  directed Decimal intervals only; Machin pi, Taylor sin/cos, atanh log
  no library transcendental, FFT, optional package, Modal, or floating accept
spectrum digest at 30 outward decimal places:
  6ee33c37477a58c92a087cd7dcf3c128d148a2c8d08887141ff79367aa9efb8d
spectral bounds:
  min |kappa_j|>1.7627; max |kappa_j|<24.292
  sum |kappa_j|^-1<6.556; sum |kappa_j|^-2<1.090
uniform prize body:
  D<7.539, R<77.202, max |xi_t|<=7, sum xi_t^2<=101
exact coarse zero-sum envelope:
  16616854517524950208619690062355423946568371 > 2^143
weighted-ellipsoid route cut:
  all balanced 0,+-1 vectors with up to five signs of each type lie inside
  38482585013041 explicit exponent vectors before sparse algebra
route verdict:
  reject coordinate-, L2-, and ellipsoid-first enumeration
  next theorem/generator must consume beta=u alpha and alpha=u^-1 beta
  as sparse profile equations before generating the unit-lattice body
scope fence:
  no associate count, 367-orbit payment, lower-profile payment, E1 image
  bound, row close, or Prize movement
compute spend: none; verifier runs under one second with tiny RAM
next route-deciding action: derive support propagation or a coefficient
                              recurrence from the two sparse product equations
```

**2026-07-29, E1 exact-L1 route probe prepared; Modal launch blocked:** the
stronger height shortcut is now a concrete finite optimization problem, but it
has produced no numerical evidence and no theorem.

```text
launcher: experiments/prize_resolution/e1_conductor256_l1_svp_modal.py
problem:
  minimize ||T xi||_1 over nonzero zero-sum xi in Z^64
  -7<=xi_t<=7, with cyclic/sign symmetry fixed exactly
resource cap:
  one container, 2 CPU, 2 GiB, 240 solver seconds, 280 hard seconds
proof status:
  exploratory floating MILP only; every claimed lower bound needs a separate
  rational proof certificate
route payoff:
  optimum >77.202 would make fixed-cofactor associates torsion-only;
  a vector <=77.202 would redirect work to exact sparse products
launch outcome:
  no container started and no credit spent;
  workspace ac-WIsI8fedhlHGSBu0g8EiyG reported exceeded spend limit
next action:
  run this one pilot only after the workspace is enabled; do not expand it
  into a fleet
```

**2026-07-29, E1 inverse-kernel exponent contraction:** Fourier inversion now
uses the phases discarded by the first spectral triangle bound.

```text
node proved: e1_conductor256_inverse_kernel_contraction
inverse kernel:
  q_r=(1/64)sum_(j=1)^63 exp(-2*pi*i*j*r/64)/kappa_j
certified operator bounds on sum lambda=0:
  half range(q)<0.044700
  sum |q_r|<0.802
prize-radius consequence:
  max |xi_t|<3.451, sum |xi_t|<61.92
integer contraction:
  max |xi_t|<=3, sum |xi_t|<=60, with sum xi_t^2<=101 retained
route verdict:
  feed all three bounds to sparse-first exact multiplication and the one
  capped MILP probe; generic ellipsoid-first enumeration remains rejected
scope fence:
  no shortest-unit theorem, associate count, 367-orbit payment,
  lower-profile payment, E1 close, or Prize movement
compute spend: none; 64-by-63 directed interval arithmetic with tiny RAM
next route-deciding action:
  run the single capped L1 pilot only after Modal spend access is restored;
  otherwise derive exact sparse coefficient propagation in the contracted box
```

**2026-07-29, E1 high-cofactor Schinzel collapse:** a sharp entropy bound
beats the universal height floor for three of the four residual cofactors.

```text
node proved: e1_high_cofactor_schinzel_height_collapse
for m=4,8,16:
  D=log(18^64/(m p))<6.845
sharp 64-coordinate entropy lemma:
  D<6.845 => sum|log z_a|<30.645
same-cofactor unit ratio:
  ||lambda(u)||1<61.29
Schinzel lower bound for non-torsion real units:
  ||lambda(u)||1=256h(u)>=128log(phi)>61.595
conclusion:
  each of m=4,8,16 has at most one 256-element shift/sign orbit
  T_36 <= T_36,m=2+3
  necessary residual maximum-profile fallback: T_36,m=2<=364
route verdict:
  concentrate every further associate attack on cofactor 2; do not recount
  the three analytically collapsed branches
scope fence:
  no cofactor-2 payment, lower-profile payment, E1 close, or Prize movement
compute spend: none; 63 directed entropy cases plus exact-rational replay
next route-deciding action:
  seek a cofactor-2-specific log improvement or sparse product invariant;
  the general Schinzel comparison misses only this branch
```

**2026-07-29, E1 cofactor-2 Smyth collapse:** the field-specific height route
closes the last associate family without enumeration.

```text
cofactor-2 deficit:                  D<7.539
certified entropy implication:       P<12.2
same-cofactor pair upper:             ||lambda(u)||_1<63.878
Smyth second-value lower:             ||lambda(u)||_1>256log(1.29)
                                      >65.188407
all four pure cofactors:              T_36(p,r)<=4
```

Smyth's least normalized measure `sqrt(phi)` cannot occur in
`Q(zeta_256)^+`: equality would put the Mahler measure `phi^(d/2)` in that
field and hence force `sqrt(5)` into a field unramified outside `2`. Exact
rational signs for `X^4-X^3-3X^2+X+1` certify that the second normalized
measure exceeds `1.29`. Directed Decimal and exact-rational atanh verifiers
agree on all 63 entropy side sizes and certificate digest
`ee3e59acdfed6536189c3ff18476a7c657e279729e0c906ef627c4224c245cb8`.

Effect:

```text
  the maximum-profile associate multiplicity is complete;
  no exponent-lattice or sparse-product census is needed for (3,6,S=18);
  E1 remains TARGET because lower-profile weighted charges remain.
```

Next action:

```text
  insert T_36<=4 into the exact weighted-kernel ledger, preserve root,
  orientation, stabilizer, and class-pair multiplicities, and identify the
  largest lower profile that can still exhaust the residual edge budget
```

**2026-07-29, exact profile-(3,6) E1 payment:** the four-orbit theorem is now
converted back to the official unordered edge ledger.

```text
profile-(3,6) maximum oriented vectors:  4*256=1024
profile-(3,6) exact edge charge:          709758113888498314287146042668908462080
binding residual edge budget:            64417827807586372161179904588832830040487
next profile:                             (2,10,S=18)
next dictionary weight:                  1227527050040565145269313275179180544
tight residual uniform vector cap:       104955
```

The payment restores the full 256-vector shift/sign orbit and the
dictionary's oriented-to-unordered factor. The next route is structural:
derive the `(2,10)` cofactor/prime-ideal partition, spend the existing height
collapse on each pure cofactor, and keep split primes above `257` and `769`
as separate associate families. No support-12 census is authorized before
that partition is priced.

**2026-07-29, profile-(2,10) split-prime router:** local valuation and ideal
factorization now isolate the lower profile's true obstruction.

```text
local valuations:                 mu=1,...,10
exact cofactors:                  2,4,8,16,32,64,128,256,512,1024,
                                  514,1028,1538
pure ideal families:              10
split ideal families:             3*128=384
height payment per family:        at most one 256-vector orbit
coarse total:                     T_210<=394, |D_210|<=100864
coarse profile edge charge:       61906644187645781406222007093836433195008
```

The three split branches correspond to one prime above `257` or `769` in
addition to the fixed row prime. They cannot be merged before that prime
ideal is fixed. The all-occupied envelope consumes about 96.1% of the
residual budget and is therefore diagnostic, not a final payment.

Next action:

```text
  bound split-prime occupancy by coupling F(r)=0 mod p with F(s)=0 mod q,
  or by a resultant/ideal argument; do not enumerate all support-12 vectors
  before fixing (m,Q_s)
```

**2026-07-29, profile-(2,10) cofactor-1538 close:** the largest split rational
prime is removed without a coefficient-support census.

```text
sharp moment threshold:            m=1538 => V<=4
V=0:                               wrong 2-adic norm valuation
V=2:                               L_64 mod 1538=2
V=4 finite-field screen:           640 hits over 128 roots mod 769
diagonal Galois types:              5
exact real-cyclotomic norm verdict: every Norm/1538 below p_min
profile-(2,10) envelope:            394 -> 266 orbits
oriented vectors:                   100864 -> 68096
```

The norm verifier builds the real minimal polynomial `C_64` and all five
degree-64 multiplication determinants using stdlib exact integers. No support
vector is enumerated. The remaining split cofactors are `514` and `1028`
above `257`; attack `1028` first because its moment window is `V<=12`.

**2026-07-29, profile-(2,10) cofactor-1028 high-energy contraction:** a
bounded-deviation logarithm estimate removes the two largest live energies
without computation.

```text
cofactor-1028 moment window:        E=2,3,4,5,6
integer autocorrelation bound:      E<=6 => x_u<=2 sum|A_d|<=12
pointwise majorant:                 log(1+x/18)<=x/18-x^2/925
energy-five norm bound:             log Norm<=64log(18)-128/185
exact floor verdict:                Norm<1028*p_min
remaining cofactor-1028 energies:   E=2,3,4
```

The endpoint of the majorant is paid by the positive atanh series for
`log(5/3)` with rational margin `7/44400`; the prize-floor comparison uses
the cubic lower Taylor polynomial for `exp(128/185)` and exact integer
cross-multiplication. This cancels the proposed energy-five/six support
classifier. Promote the exact energy-two/three ledgers and complete the
queued 8,385-type energy-four exact norm replay; do not enumerate supports.

**2026-07-29, profile-(2,10) cofactor-1028 energy-two exclusion:** the same
bounded-deviation method, used as a lower bound, removes the bottom energy
without a norm census.

```text
energy-two deviation interval:       -4<=x_u<=4
pointwise minorant:                  log(1+x/18)>=x/18-x^2/549
global lower bound:                  log Norm>=64log(18)-256/549
exact ceiling verdict:               Norm>1028*p_max
remaining cofactor-1028 energies:    E=3,4
```

The endpoint comparison is the positive atanh series for `log(9/7)`, with
rational margin `1/23058`; `exp(-256/549)>293/549` then clears the official
ceiling by exact integer arithmetic. The four exploratory energy-two norms
are no longer load-bearing. Promote the 329-type exact energy-three ledger
and the queued 8,385-type exact energy-four ledger to finish cofactor `1028`.

**2026-07-29, profile-(2,10) cofactor-1028 energy-three close:** a modular
resultant engine promotes the complete 329-type ledger with low local cost.

```text
signed lag triples screened:         C(63,3)*8
local/mod-257 compatible types:      329
CRT primes:                          9 exact 31-bit primes
CRT modulus bits / norm bits:        279 / at most 267
exact quotient range:                110037709021719095415927105791028375912712994655842773868558710185217329606913
                                      ..120963671460232983862280624800699787448990635276721201666721603772949806841601
official verdict:                    all 329 above p_max
remaining cofactor-1028 energy:      E=4
```

Trial division proves the CRT primes, AM-GM supplies the reconstruction
ceiling, and five prior Bareiss norms independently check the resultant
recurrence. The replay uses about 17 MiB and 1.5 seconds locally. Replace the
queued 60-container energy-four Bareiss plan with the same modular engine;
the remaining 8,385 types should fit one low-memory, sub-minute Modal worker.

The queued launcher has now been revised accordingly: 60 checkpointed
first-lag calls are serialized through one 512 MiB container, and every norm
is reconstructed by the certified nine-prime CRT engine. The prior rejected
launch allocated no container and spent no credit; do not retry until the
workspace spend limit is restored.

**2026-07-29, profile-(2,10) cofactor-514 outer-window contraction:** exact
logarithm bounds remove both ends of the wider split-prime branch.

```text
initial moment window:                E=0,...,17
energy zero:                          wrong 2-adic valuation
low logarithm minorant:               E=1,...,4 => Norm>514*p_max
high endpoint majorant:               E=14,...,17 => Norm<514*p_min
remaining cofactor-514 energies:      E=5,...,13
```

Both endpoint logarithms use two-term positive atanh sums plus geometric
tails, with rational margins `776/5736675` and `56987/30028800`. Exact
exponential comparisons pay the official interval. The next cofactor-514
step is a fixed-root mod-257 screen by integral autocorrelation shape; do not
enumerate coefficient supports before that target-level reduction.

**2026-07-29, cofactor-514 middle-shape router:** the nine-energy window is
now partitioned by autocorrelation magnitudes and filtered before any lag
census.

```text
integral magnitude profiles before:   32
energy-five sparse profile removed:   (1,1,0), above p_max
high-middle L1 boundaries removed:    (9,3),(10,6),(11,7),(12,10),(13,11)
integral magnitude profiles after:    17
E=12 and E=13 survivors:              all-unit only
```

One common high-middle deficit `69/50` and five exact atanh endpoint margins
pay the downward-closed `L1` classes; the sparse energy-five profile uses a
separate lower envelope. Next impose local multiplicity two and the fixed
primitive-root equation modulo 257 on these 17 shape families. This is still
an autocorrelation-target problem, not a coefficient-support census.

**2026-07-29, cofactor-514 parity and distinct-trace cap:** two more magnitude
profiles close without finite-field enumeration.

```text
E=8 all-even profile:                parity multiplicity contradiction
E=13 all-unit trace cap:             x_u<2551/100
certified logarithm deficit:         683/500
E=13 verdict:                        Norm<514*p_min
remaining magnitude profiles:       15
```

The trace cap uses the 13 largest distinct folded traces, rational Machin
bounds `333/106<pi<355/113`, and a quartic cosine majorant. The remaining
profiles occupy energies 5 through 12. Continue with the local lag-parity and
fixed-root mod-257 equations; energy 13 no longer needs a census.

**2026-07-29, exact profile-(2,10) E1 payment:** the weighted ledger can move
inward without waiting for complete split-cofactor emptiness.

```text
profile-(2,10) oriented envelope:    68096
exact profile charge:                41794840999781162066129578393300739162112
new residual edge budget:            22622986807805210095050326195532090878375
next profile:                         (1,14,S=18)
next dictionary weight:               1154418456451360735963226152798543872
tight residual oriented cap:          39193
```

This charge includes all 128 possible `514` ideals and all 128 possible
`1028` ideals. Their continuing refinements can add slack but are no longer
on the serial path. The active E1 frontier is now the local cofactor and
prime-ideal partition for `(1,14,S=18)`; retain the exact aggregate residual
across every later profile.

**2026-07-29, profile-(1,14) split-prime payment router:** the new active
profile inherits the square-mass-18 cofactor machinery, and the serial
obligation collapses to the queued energy-four certificate.

```text
coarse cofactors / orbits:           13 / 394
after profile-invariant m=1538:      266 orbits
m=1028 after analytic/exact leaves:  E=4 only
if E=4 is empty:                     138 orbits, 35328 vectors
current oriented cap:                39193
triggered next profile/cap:          (0,18,S=18) / 3994
```

The transport is legitimate because the consumed norm proofs depend on
square mass, local valuation, and autocorrelation, not on the split
`18=4a+b`. The revised one-container CRT job is therefore serial-path compute.
Do not spend serial effort finishing cofactor `514` before this certificate.

**2026-07-29, cofactor-1028 energy-four analytic close:** the proposed 8,385
exact resultants collapse to one cubic conjugate-moment inequality.

```text
multiplicity-four lag sets:          134720
mod-257 compatible signed types:     8385
cubic moment:                        sum x_u^3=64K
exact compatible maximum:            K=24
global logarithm deficit:            512/729
official verdict:                    Norm<1028*p_min for every type
```

The finite screen uses two independent exact formulas for `K`; the compatible
ledger digest is
`401203ca53dbd51a859b702767576b50aca05c73216194120a60eff251d1d442`.
The one-container Modal norm job is superseded and should not be launched.
Consume this close immediately in the profile-(1,14) payment.

**2026-07-29, exact profile-(1,14) E1 payment:** the analytic energy-four
close discharges the router's only pending premise.

```text
profile-(1,14) oriented envelope:    35328
exact profile charge:                20391647614756836040054426763033478955008
new residual edge budget:            2231339193048374054995899432498611923367
next profile:                         (0,18,S=18)
next dictionary weight:               1117325838856821897682125205459304448
tight residual oriented cap:          3994
```

All 128 cofactor-514 ideals are charged, so no unfinished cofactor-514
argument is hidden in this payment. The serial frontier is now `(0,18)`. Its
inherited ten pure families account for 2,560 vectors; because a complete
shift/sign orbit has 256 vectors, at most five of the 128 cofactor-514 ideal
families may survive if this profile is to fit below cap 3,994.

**2026-07-29, universal cofactor-514 product ceiling:** dependency audit of
the new frontier found that the older outer-energy leaf cited `E<=17` without
wiring a theorem that actually stated it. The missing result is now proved
profile-independently.

```text
fixed boundary energy:               E=18, V=36
feasible two-level chambers:         57
closest chamber:                     j=63 lower entries
exact verdict:                       max product < 514*p_min
monotonic extension:                 every E>=18 excluded
adjacent guard:                      E=17 envelope remains above threshold
```

The old profile-(2,10) outer leaf now consumes this theorem instead of the
profile-(4,2) variance-window node. This both repairs its provenance and
licenses transport of the surviving `E=5,...,13` route to `(0,18)`.

**2026-07-29, universal cofactor-1028 energy-window repair:** the same
dependency audit found that the four energy leaves cited a profile-specific
variance theorem that did not state their `E=2,...,6` premise. The corrected
profile-independent window is now exact:

```text
E=0:                                wrong 2-adic norm valuation
E=1:                                L_32^2 mod 1028 = 452
E=7 boundary chambers:              61, all below 1028*p_min
monotonic extension:                every E>=7 excluded
adjacent E=6 chamber:               above threshold, retained
global live window:                 E in {2,3,4,5,6}
```

All energy-two, energy-three, energy-four, and energy-five/six leaves now
consume this theorem. Thus the profile-(1,14) payment remains valid after a
strict provenance audit, and the same complete cofactor-1028 exclusion is
available at `(0,18)`.

**2026-07-29, profile-(0,18) exact router:** eighteen singleton exponents
again realize every allowed local valuation one through ten. After the
repaired global exclusions, only ten pure families and the 128 cofactor-514
ideals remain.

```text
current profile/cap:                 (0,18,S=18) / 3994
live cofactor-514 shapes:            15 at E=5,...,12
pure-family charge:                  10 complete orbits
maximum split occupancy to pay:     5 ideals
threshold vectors:                  15*256=3840
threshold charge:                   2145265610605098043549680394481864540160
threshold residual:                 86073582443276011446219038016747383207
next profile/cap:                    (4,4,S=20) / 329
```

The new exact red is `e1_profile018_m514_five_ideal_occupancy`. Attack it
falsification-first: six genuinely occupied `F`-ideals kill the threshold.
Autocorrelation roots alone are not occupied ideals; parity, all-singleton
realization, and exact norm/row compatibility must remain distinct gates.

**2026-07-29, exact Galois/norm occupancy dictionary:** diagonal Galois action
turns the five-ideal red into a cleaner exact norm-multiplicity problem.

```text
fixed-row occupied ideals O_514(p,r)
  = diagonal Galois orbits of actual profile-(0,18) collisions
    with exact norm 514p
```

Regularity gives one representative of each Galois orbit in every row-root
fiber; same-ideal height collapse makes its `Q_s` label injective. Therefore
the count is independent of `r`. A true falsifier is six realizable Galois
orbits sharing one exact official-admissible prime quotient, not six
mod-257/autocorrelation hits. Use the latter only to reject intermediate
proof routes.

**2026-07-29, mod-257 singleton-completion no-go:** the isolated finite-field
gate is provably nonselective for the active all-singleton profile.

```text
(e,sign) -> sign*3^e mod 257:       bijection onto F_257^*
explicit support:                    {0,...,15,17,78}
local multiplicity:                  1
root:                                F(3)=0 mod 257
Galois transports:                   all 128 primitive roots
example energy:                      1478, outside the live window
```

Thus a root/local screen cannot remove any split ideal in principle. Do not
fund a computation at that gate alone. The first selective object must couple
the root equation to low-energy all-singleton realization, then exact
norm/official-prime multiplicity.

**2026-07-29, cofactor-514 Hermite profile refinement:** a
profile-independent quadratic Hermite majorant improves the middle-energy
ledger without support enumeration. For deviations of mean zero, variance
`v`, and upper bound `M`, interpolation at `-v/M` and `M` reduces the norm
bound to the exact two-point distribution with those moments. Exact integer
cross-multiplication removes

```text
(E;n1,n2,n3)=(9;1,2,0):             M=10, v=18
(E;n1,n2,n3)=(11;7,1,0):            M=18, v=22
live cofactor-514 magnitude rows:    15 -> 13
```

The occupancy threshold remains five ideals. The next analytic boundary is
the all-unit energy-twelve row. Its continuous two-moment envelope misses the
field-floor comparison slightly, so a further close must spend a discrete
trace, local-multiplicity, or fixed-root constraint rather than repeat the
same moment inequality.

**2026-07-29, energy-twelve root/parity route cut:** even the combined
autocorrelation-level necessary screen is nonempty. The explicit target

```text
D={1,...,11,15},                    A_d=+1 on D
energy/profile:                     (12;12,0,0)
local parity multiplicity:          2
primitive root modulo 257:          148=3^59
uniform unit-circle floor:           Y>=4
cubic relation index:               K=378
```

survives energy, local parity, factor-257, positivity, and cubic-moment
checks. Its exact real-cyclotomic norm is divisible by 514, but the quotient

```text
81586655821452087305363431809893675164014023805430622462841107305845289913087
```

is below `p_min`. This is not an 18-singleton coefficient realization. The
example proves that the first genuinely selective gates are integral
singleton spectral-factor realization and exact norm; either may be applied
first when the candidate representation makes it cheaper.

**2026-07-29, energy-ten profile-(6,1) cubic close:** the discrete signed
relation ledger improves the generic third-moment bound just enough to remove
one more cofactor-514 shape.

```text
profile:                              (E;n1,n2,n3)=(10;6,1,0)
nested-layer sizes:                   14,2
generic layer bound:                  |M3|<=268
signed relation divisibility:         M3=0 mod 6
exact usable cap:                     M3<=264
cubic Hermite contacts:               33/2,65/2
certified verdict:                    Norm<514*p_min
live cofactor-514 magnitude rows:     13 -> 12
```

This is profile-independent and uses no coefficient realization or support
enumeration. The occupancy threshold remains five ideals. The remaining
generic layer bounds all miss the field floor, so another moment-only pass
must add genuinely sharper additive information rather than replay this
relaxation.

**2026-07-29, all-unit energy-twelve close:** the local multiplicity condition
supplies the additive information missing from the relaxed layer bound.

```text
profile:                              (E;n1,n2,n3)=(12;12,0,0)
local parity consequence:             odd number o of odd positive lags
parity-split relation cap:             M3<=510
cubic Hermite contacts:               17,40
certified verdict:                    Norm<514*p_min
live energies:                        5,...,11
live cofactor-514 magnitude rows:     12 -> 11
```

The proof counts `EEE` and `EOO` relation types separately for all six odd
values of `o`; no lag-set enumeration or coefficient realization enters. The
former `{1,...,11,15}` route-cut witness is still a valid warning about the
pre-norm screens, but its whole magnitude profile is now analytically dead.

**2026-07-29, all-unit energy-eleven close:** recursively pricing the even
part of the relation support through the `2`-power filtration sharpens the
one-step parity count.

```text
profile:                              (E;n1,n2,n3)=(11;11,0,0)
top odd-lag cases:                    o in {1,3,5,7,9,11}
dyadic recursive relation cap:        M3<=384
cubic Hermite contacts:               17,37
certified verdict:                    Norm<514*p_min
live energies:                        5,...,10
live cofactor-514 magnitude rows:     11 -> 10
```

The recurrence is an analytic upper bound on symmetric zero-sum triples in
`Z/2^k Z`; its verifier evaluates only a tiny dynamic table. The same cap
does not close energy ten, so the next step must add a different constraint.

**2026-07-29, profile-independent class-descent close:** the fixed row-prime
ideal factorization bypasses every surviving energy profile.

```text
upper field L:                       Q(zeta_256)
lower field K:                       Q(zeta_128)
[L:K]:                               2
upper primes above 257:              128
lower primes above 257:              64
extensions per lower prime:          2
published lower class index:         Z/359057
published Galois multipliers:        -1,29301
exact modular orbit size:            64
proved occupancy bound:              O_514<=2
required payment bound:              O_514<=5
profile-(0,18) orbit count:           at most 10+2=12
profile-(0,18) oriented vectors:      at most 3072
next profile/cap:                     (4,4,S=20) / 1971
next full-orbit allowance:            7
```

For fixed `P_r`, every occupied `Q_s` satisfies
`(alpha)=P_r(1-zeta_256)Q_s`, so all occupied upper primes have one ideal
class. Relative ideal norm sends them to one class in `K`. If the 64 lower
primes above 257 have pairwise distinct classes, only one lower prime occurs,
and it has exactly two upper extensions.

Bernstein's pinned S-unit talk prints the exact class index, assigns the base
prime class one, and gives the two Galois multipliers. Exact integer
arithmetic confirms that `{+/-29301^j:0<=j<32}` contains 64 classes. The
released software does not expose the load-bearing n=64 class computation.

The class-orbit theorem is proved without assuming those printed
coordinates. The Galois group `(Z/128Z)^x` is a 64-element 2-group with
exactly three nonidentity involutions `63,65,127`. The proved
conductor-256 real class-number theorem descends to real class number one at
conductor 128 by extension/norm and Weber oddness, so complex conjugation
acts by class inversion. It is therefore enough to prove that the two
explicit ideals

```text
(257,zeta_128-9)(257,zeta_128-57),
(257,zeta_128-9)(257,zeta_128-248)
```

are nonprincipal. They exclude involutions 65 and 63; either also makes the
base class nontrivial, while odd class number excludes involution 127. Every
nontrivial stabilizer would contain an involution.

The 17-primary product `q_1q_65` is now proved nonprincipal without a BNF.
Dembele identifies the class-number-17 CM field
`E=Q(i(zeta_64+zeta_64^(-1)))` and its Hilbert class field; his exact Elkies
polynomial is irreducible modulo 257. This gives a nontrivial Artin symbol at
every prime above 257, and norm descent proves `q_1q_65` nonprincipal.

For the second product put `beta=zeta_128-zeta_128^(-1)`. Both `q_1` and
`q_63` contract to

```text
p_66=(257,beta-66)
```

in the degree-32 fixed field `Q(beta)`.

This second test is closed by an explicit Kummer-style certificate. A
32-term Jacobi-sum product `alpha` satisfies

```text
(alpha)=(q_1 q_63/(q_127 q_65))^(2*21121).
```

At `r=5406977=256*21121+1`, the product of the power-residue characters for
the 32 embeddings `zeta_128 -> u^s`, `s=1,3,...,63`, kills all 31 full-unit
generators and every `21121`st power, but sends `alpha` to `500235 != 1`.
Hence `q_1q_63` is nonprincipal. Extension of a hypothetical generator of
`p_66` would generate `q_1q_63`, so `p_66` is nonprincipal as well. Two
independent tiny verifiers evaluate the Jacobi sums directly and through
coefficient polynomials.

Both involution tests, the 64-prime class orbit, the two-ideal descent, and
the exact profile-(0,18) payment are therefore unconditional.

The stronger bound is priced directly rather than routed through the older
five-ideal threshold. The proved payment leaves residual
`515126704564295620156155116913120291239`; exact adjacent comparisons give
`floor(2R/M_33(4,4))=1971`. Thus the next profile needs at most seven full
256-vector orbits, not one.

Burn-down:

```text
result:                              CLOSED
profile-specific live rows:          10 -> bypassed
proved occupancy threshold:          5 -> 2
proved next-profile cap:             329 -> 1971
proved involution tests:             q_1*q_65 Harbater; q_1*q_63 residue
new exact assumptions:               none
retired compute request:             CR-E1-QZETA128-P257-CLASS-ORBIT
next route-deciding action:          profile (4,4,S=20), at most 7 orbits
```

The first route decision at that profile is now exact. Four singleton
coefficients give the complete relevant local valuation set

```text
{1,2,3,4,5,6,8,9,10,12,16,17,18,20}.
```

The square-mass-20 field floor is much weaker than at square mass 18:

```text
m<=floor(20^64/(B_P 2^128))=1707433.
```

Local reciprocity and the global residue-degree condition leave `1133`
necessary-sieve cofactor values, including all fourteen pure powers of two.
This is not evidence for 1133 collisions; it is a certified method fence.
The former ideal-family router cannot reach seven without an additional
profile-specific exclusion. The selected positive routes are now:

1. classify the low-autocorrelation profile-`(4,4)` supports and exact
   conductor-256 resultants;
2. prove collective ideal occupancy across different cofactors; or
3. replace the serial cap by a mixed weighted payment.

Do not launch the raw profile vector census locally or on Modal. Any external
compute proposal must first quotient shift/sign and conductor symmetries,
stratify by autocorrelation energy, stream exact resultants, and carry a
declared subproblem/cost ledger in `notes/PRIZE_COMPUTE_REQUESTS.md`.

## 2026-07-29 KoalaBear cubic endpoint-cofactor narrowing

Starting pins were local `623ab5fa`, canonical prize `0b90fc9b`, and
upstream K3 PR head `fce150e3323ce37f261b21c19685f4613552dd42`. The
residual full-V4 `n=3` geometric model automatically induces a decomposable
inner-degree-six map, so the terminal `m=6` router cannot be invoked without
cycling back to the same degree-two right component.

The new PROVED
`rate_half_kb_m2_r2_dihedral_degree3_endpoint_cofactor_interpolation_compiler`
instead imports the actual endpoint source presentation. It proves that
`H | M` is equivalent to a full-support kernel of one explicit `38 x 12`
matrix. A deterministic `F_47` fixture with the exact `s=6` locator
ownership and four-edge component color fails the gate by a rank-twelve
minor of determinant `7`. The two interpolation identities also induce an
exact multiplicative transport on every source-star edge; every cycle must
have holonomy one. The fixture's six canonical square holonomies are
`11,26,17,2,41,31 mod 47`, all nonidentity, giving a local deletion witness.
Retaining all three pair gains in each of the 24 star/owner triples gives an
exact converse: a full-support kernel exists if and only if the resulting
12-vertex gain multigraph is flat. This is a deleting fixture and an exact
universal compiler, not a deployed-row deletion.

Burn-down:

```text
result:                              NARROWED
critical status delta:               none
owner/payment delta:                 none
vague active-pencil gate:            replaced by exact full-support kernel
pinned admissible packets deleted:   one
new assumptions:                     none
live compute requests:               none
next route-deciding action:          prove universal gain-graph nonflatness,
                                     falling back to full stacked rank over K
```

## 2026-07-29 KoalaBear full-V4 source-facet close

The gain-flatness action above is superseded for the full-V4 type by a
stronger source-facet contradiction.

The pinned equality-wall theorem at upstream commit
`44542e91e459364a521870ed2ebde7f6fe5055bf`, theorem blob
`356ff4b47d0bb429d11ea10382762a6e95b5ce24`, proves that the graph-free
`Q=6,s=6` packet has a six-set `I` and a five-set `K subset I` such that
the horizontal root set of the whole outgoing factor above every point over
`k in K` is exactly `I^c`. This narrow consequence is banked as the PROVED
`rate_half_kb_q6_s6_common_five_outgoing_fiber_pin`.

For the residual `n=3` full-V4 component, the exact source-star graph is
`K_(2,2,2) disjoint_union K_(2,2,2)`. The two stars over the complete
coordinate fiber of `k` jointly have a four-endpoint set `U_k`, the
complement of one deck pair `P_k`. Component divisibility forces
`U_k subset I^c`. Since `k in K subset I` and lies in the same common-pole
six-set, `k in P_k`, so `U_k=N_G(k)`. This retains the relative endpoint
twist rather than setting it to one. Hence `N_G(k) subset I^c` for all
five `k in K`, making `K` independent. This contradicts
`alpha(G)=4` and proves
`rate_half_kb_m2_r2_dihedral_degree3_source_facet_exclusion`.

Together with the prior `n=2,5,6` exclusions, the exhaustive outer-degree
split now proves
`rate_half_kb_m2_r2_dihedral_full_v4_exclusion`: the actual
`(m,r,delta)=(2,2,4)` type is empty.

Burn-down:

```text
result:                              FULL-V4 TYPE CLOSED
critical status delta:               none
m=2 stabilizer types:                3 -> 2
deleted type:                        (r,delta)=(2,4)
remaining types:                     (r,delta)=(4,2),(8,1)
owner/payment delta:                 none
new assumptions:                     none
field computation:                   none
retained audit compiler:             endpoint cofactor/gain flatness
next route-deciding action:          classify the order-two stabilizer type
```

Upstream custody: draft PR `przchojecki/rs-mca#1132`, commit
`2b0acfe0cc382fd5b399960b435887c6b20e3f82`, canonical certificate payload
`f48a46f22bc15098f5fc566e6f009d76afa4751c4fd4b4b8edaf481e619c5a01`.
The only reported check failure at the pin is unrelated Vercel deployment
authorization.

## 2026-07-29 KoalaBear coordinate-order-two route boundary

The PROVED
`rate_half_kb_m2_r4_order2_coordinate_source_facet_signature` handles the
coordinate subgroup `<tau x 1>` of the surviving order-two type. It forces
the exact component-star census

```text
(J-J,I-I,I-J)=(10,10,4),
```

forces the endpoint involution to preserve `I` and `J=I^c`, and leaves only
the two `K`-fiber pair-degree profiles

```text
(4,4),(4,4),(2,2),       (4,4),(3,3),(3,3).
```

In the allowed aligned subcase `L=I`, an exact defect-zero abstract fixture
realizes all current facet, symmetry, degree, pole-graph, and component-color
constraints. This is a method fence:
those ledgers are jointly consistent and cannot by themselves exclude the
coordinate orientation. The next coordinate attack must use the actual
interpolation/coefficient equations. In parallel, derive rather than assume
the source lift for `<tau x tau>`. The later transpose-transport theorem
routes `<1 x tau>` through a fresh `<tau x 1>` source record, so it is no
longer an independent geometry campaign. The trivial-stabilizer type remains
open, and no owner/payment ledger changes.

## 2026-07-30 KoalaBear diagonal interpolation interface

The diagonal subgroup `<tau x tau>` has a separate exact compiler. The
PROVED
`rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler` forms
one split quartic `R_p` from the two component stars over each quadratic
`psi` fiber. Diagonal stabilization transports these quartics
projectively, their product is `A^4`, and their factors retain all three
source-facet classes. They come from a bidegree-at-most-`(4,4)` endpoint
biform if and only if a concrete `35 x 12` matrix has a full-support
kernel.

This replaces the unsafe idea of transporting individual stars: the
diagonal automorphism need not descend to the source `X`-line. The next
diagonal result should prove universal kernel failure or reconstruct the
unique interpolated biform and impose the outer factor identity. No
subgroup, owner, or payment is closed by the compiler itself.

Upstream custody: draft PR `przchojecki/rs-mca#1132`, commit
`77b0971ebb443efd8487ee3809cd988ba183d00c`, canonical certificate payload
`96c47c813c41f4b268b9826ed4866e14d44c5a8187487266a3de6f550cbbf6b6`.
The packet combines the coordinate and diagonal interfaces and rejects
17 of 17 hostile mutations.

The complete facet/defect-only diagonal classifier is registered as
`CR-K3-M2-R4-DIAGONAL-FACET-SAT`. It requires a canonical completeness
router and proof-producing UNSAT certificates across both `I/L` cases,
all four pole-cycle types, ramification, and every endpoint involution.
The partial aligned `4+2` pilot is evidence only and causes no DAG move.
Do not spend additional laptop or Modal budget on unlabeled search shards.

## 2026-07-30 KoalaBear diagonal source-subfield dichotomy

The PROVED
`rate_half_kb_m2_r4_diagonal_source_subfield_dichotomy` replaces the
remaining diagonal source-descent ambiguity by two exhaustive branches.
If the diagonal automorphism preserves `K(X)`, it gives a genuine
source-line involution and, geometrically,

```text
b(X)=-X, s(X)=1/X, psi(X)=X^2, tau(Z)=1/Z,
T^2 X^4 H(1/T,1/X)=+/-H(T,X).
```

The reciprocal source coefficient spaces have dimensions eight and seven;
the common-five facets may now be imposed with individual-star transport.
If `K(X)` is not preserved, its conjugate is a second rational quadratic
subfield and the quartic `W` projection is biquadratic. Exact tame
Riemann--Hurwitz leaves only source genus zero with three inertia types, or
source genus one with two branch values of each of two inertia types.

This is a route split, not a deletion. Next attack the reciprocal
coefficient forms in the lifting branch and the two low-genus `V4`
passports in the non-lifting branch. The whole-fiber interpolation compiler
remains mandatory in both. No compute spend was used.

## 2026-07-30 KoalaBear diagonal branch coefficient compiler

The PROVED
`rate_half_kb_m2_r4_diagonal_branch_coefficient_compiler` converts the
source-subfield split into executable algebra. In the lifting branch,

```text
H=U+XV,       G=U^2-WV^2,
deg U<=(2,2), deg V<=(2,1),
```

with a common reciprocal sign on `U,V`. The two source parameter spaces
have dimensions eight and seven, and `G` is always positive reciprocal.
In the non-lifting branch, the endpoint quartic over `K(W)` must have a
completely split cubic resolvent; for the actual irreducible separable
quartic this is equivalent to its `V4` deck group.

Next substitute the three exact source-facet classes into the reciprocal
norm, and combine the split resolvent with the two low-genus passports.
Clear denominators and preserve irreducibility and outer-factor side
conditions. No computation or ledger payment was used.

## 2026-07-30 KoalaBear source-row interpolation gate

The PROVED `rate_half_kb_m2_r4_source_row_interpolation_compiler` is the
shared first algebraic gate for all surviving order-two orientations.
Twelve projective row quartics come from a unique
bidegree-at-most-`(2,4)` source form exactly when a concrete `45 x 12`
matrix has a full-support kernel. Complete-source saturation additionally
gives

```text
product_i q_i ~ B^2,       Res_T(A,H) ~ B^2,
```

or `A(X^2)^2` in the lifted diagonal normal form. This is strictly earlier
and smaller than reconstructing a generic endpoint biform. Route every
coordinate or diagonal source-facet survivor through it first, then impose
exact degree, irreducibility, deck distinction, reciprocal norm or split
resolvent, and the outer factor identity. No compute spend was used.

Upstream custody for the three source-subfield/coefficient interfaces is
draft PR `przchojecki/rs-mca#1132`, commit
`c88438d7109cf7acd7caebaf006f21c776b74d74`, note/verifier/certificate blobs
`f58c2ea9cea88dfc6be637e9f1f14e86e8862cc6`,
`7cc4eb6e0560ca5c587f91623dc407892a07e2ca`, and
`033043e7a0969ea9f98207567b890b10e3077271`, with canonical payload
`f0b751301e56989bf6fbf19cf15e5ff8faa0d7d86e76278306950a488cdf5156`.
The verifier rejects 18 of 18 hostile mutations; the only PR check failure
at the pin is unrelated Vercel authorization.

## 2026-07-30 KoalaBear coordinate coefficient normal form

The PROVED `rate_half_kb_m2_r4_coordinate_coefficient_normal_form` uses the
coordinate preserving lift to normalize `tau(T)=-T`, `b(X)=-X`. The two
source eigenspaces are explicitly

```text
A_2(W)T^2+A_0(W)+XT B_1(W)                         (dimension 8),
T A_1(W)+X(B_2(W)T^2+B_0(W))                       (dimension 7).
```

Deck distinction forces the odd-`X` part to be nonzero, and the endpoint
norm is even in `T`. Route the two exact coordinate `K`-fiber degree
profiles through the `45 x 12` source gate and then these two forms. Exact
degree, irreducibility, common-five facets, and outer-factor divisibility
remain. No compute spend or ledger payment was used.

## 2026-07-30 KoalaBear universal m2 source-facet census

The PROVED `rate_half_kb_m2_u2_universal_source_facet_census` observes that
the `(10,10,4)` category count precedes every stabilizer argument. It holds
for coordinate, diagonal, and trivial-stabilizer degree-two components.
The ten `K`-fiber `J-J` stars initially have one of five exhaustive integer
degree profiles:

```text
(0,4,4,4,4,4), (1,3,4,4,4,4), (2,2,4,4,4,4),
(2,3,3,4,4,4), (3,3,3,3,4,4).
```

This gives the first exact source-facet interface for the residual
`(r,delta)=(8,1)` trivial-stabilizer type. The later component-color cut
removes the first two profiles before the shared `45 x 12` source gate is
applied, without importing the coordinate involution pairing. No
computation or ledger payment was used.

Upstream custody for the base mixing obstruction is draft PR
`przchojecki/rs-mca#1132`, commit
`de237ba4d6ffd03bddc3d3daa7e94d0dee06eedf`, note/verifier/certificate blobs
`a1a84452ddcd2f407eefb89bea0ef6a710e9f5d2`,
`91a61152be9bb639f720554f080c01d424c5ecc8`, and
`2c8625cd0f2e51809a2696d4a69eb54fb3ec91e4`, with canonical payload
`49131c6962e551c529d0681427ef9fee0eb10ea2bb42ffa5f46db3c63710ca8c`.
The verifier pins the complete-source and source-facet parents and rejects
28 of 28 hostile mutations.

## 2026-07-30 KoalaBear universal source-row scope repair

The PROVED `rate_half_kb_m2_r4_source_row_interpolation_compiler` has a
legacy order-two identifier, but its proof is stabilizer-independent. The
upstream source reduction supplies an irreducible bidegree-`(2,4)` source
form, twelve nonzero quartic rows, and complete-source saturation for every
residual `Q=6,s=6,u=2` component before conic invariance is introduced.
Therefore the `45 x 12` full-support kernel and invariant square-resultant
tests apply to the full-V4, order-two, and trivial-stabilizer types. This
repairs the scope needed by the five-profile trivial-branch program; it
does not assert that any profile fails the kernel gate.

## 2026-07-30 KoalaBear universal component-color profile cut

The PROVED
`rate_half_kb_m2_u2_universal_component_color_profile_cut` combines the
five-profile census with Corollary 9.28's exact component edge coloring.
A source-degree-two component colors exactly four edges of the two-regular
pole graph. Its outside-`K` deficit `c_j=4-d_j` is precisely the colored
degree of the left vertex `j`, so `c_j<=2`. The two deficit partitions
`4` and `3+1` are impossible, leaving exactly

```text
(2,2,4,4,4,4), (2,3,3,4,4,4), (3,3,3,3,4,4).
```

Thus every `J` label occurs at least twice over `K`, including in the
trivial-stabilizer branch. The coordinate involution already removes the
middle row; diagonal and trivial packets retain all three until further
facet or coefficient constraints are imposed. No compute spend or ledger
payment was used.

## 2026-07-30 KoalaBear colored partial-resultant split

The PROVED
`rate_half_kb_m2_u2_colored_source_resultant_split_compiler` packages the
four colored pole roots as one squarefree quartic `C_H`. With `D_K` the
degree-ten pullback over the common five-set, `D_R=B/D_K`, and `P_I,P_J`
the two source-label sextics, every residual degree-two component satisfies

```text
Res_T(P_J,H) ~ D_K^2 C_H,
C_H Res_T(P_I,H) ~ D_R^2.
```

Moreover `c_j=deg gcd(C_H,bZ_j)`, so the three surviving profiles are read
directly from the same quartic. This compresses twelve row-product choices
to one four-edge divisor and two exact resultant equations. Classify these
quartics jointly with the `45 x 12` source gate and the coordinate/diagonal
coefficient forms. No compute spend or ledger payment was used.

## 2026-07-30 KoalaBear coordinate quotient-resultant compiler

The PROVED
`rate_half_kb_m2_r4_coordinate_colored_quotient_resultant_compiler`
specializes the colored split to the coordinate parity spaces. Star
transport makes `C_H` deck invariant, so `C_H(X)=c(X^2)` for a squarefree
quadratic `c`; its four edges are the two complete incident-edge pairs at
two right pole-graph vertices. Since `I,J` are invariant under
`tau(T)=-T`, write `P_S(T)=p_S(T^2)`. The two parity systems use

```text
Phi_+=(A_2Y+A_0)^2-WYB_1^2,
Phi_-=W(B_2Y+B_0)^2-YA_1^2,
R_S=Res_Y(p_S,Phi_epsilon),
R_J~K_5^2c,       cR_I~R_7^2.
```

This is now a pair of univariate resultant equations in the existing eight-
or seven-dimensional source spaces plus a two-fiber choice. Solve these
systems before any generic coordinate endpoint search. No orientation is
deleted and no compute spend or ledger payment was used.

## 2026-07-30 KoalaBear coordinate K-fiber Vieta-rank compiler

The PROVED
`rate_half_kb_m2_r4_coordinate_k_fiber_vieta_rank_compiler` inserts the
five actual common-`K` stars into the coordinate coefficient system. If a
a source lift `[r:s]` above `kappa=[u:v]` carries the `J`-edge `{a,b}`,
then

```text
p_kappa=ab,       q_kappa=r*s*(a+b)
```

is independent of the deck-point choice. Vieta gives an exact `10 x 8`
positive kernel gate

```text
A_0(kappa)=p_kappa A_2(kappa),
u*v B_1(kappa)=-q_kappa A_2(kappa),
```

and an exact `10 x 7` negative gate

```text
B_0(kappa)=p_kappa B_2(kappa),
A_1(kappa)=-q_kappa B_2(kappa).
```

Leading values must be nonzero at all five fibers; in particular the
negative branch excludes ramified common-`K` values. Each parity branch has
a five-by-five determinant obstruction, and the negative edge products
must also lie on one degree-`(1,1)` rational function, equivalently a
five-by-four matrix has rank at most three. Apply these cheap exact tests
before solving the colored quotient-resultant system. They delete any
failing supplied star packet but do not yet prove universal failure. No
compute spend or ledger payment was used.

Upstream custody is draft PR `przchojecki/rs-mca#1132`, commit
`780520c4399815451f30a28ec22bdff075629242`, note/verifier/certificate
blobs `f86109bbabbe1a0448e91178492651d4081d2397`,
`0a2405f848b6d032de3f77e81882ee7f04a38e0a`, and
`be6e9aaef8a3f215e61fc5f3719b50dc584fdb0f`, with canonical payload
`ba77d21b4da577dcb4eafc375d36e4df18644c6c284cf0e53a3350c4011d8a85`.
The verifier rejects 34 of 34 hostile mutations.

## 2026-07-30 KoalaBear coordinate-transpose transport

The PROVED `rate_half_kb_m2_r4_coordinate_transpose_transport` resolves
the source-presentation warning around the third order-two subgroup.
The endpoint self-correspondence `f(T)=f(W)` is invariant under
`(T,W)->(W,T)`, which conjugates `<1 x tau>` to `<tau x 1>`. For the
transposed component, rename the endpoint roles and rerun the degree-two
source reduction on the new second projection. This produces fresh primed
data `H',psi',b',I',J',L',K'`; it does not identify the old source form
with its formal transpose. The complete coordinate source-facet, 8/7-
dimensional parity, colored-resultant, and Vieta-rank chain applies to the
primed packet.

The order-two type now has only two independent geometric routes:
coordinate, covering both coordinate subgroups, and diagonal. A universal
coordinate packet exclusion will delete both coordinate subgroups. No
orientation is yet deleted, and no compute spend or ledger payment was
used.

Upstream custody is draft PR `przchojecki/rs-mca#1132`, commit
`f109a36bbf510075571b2f0a871cb6ca4420ce19`, note/verifier/certificate
blobs `750e243ea10a14fd1bd98bfa0ac45d3d5d673304`,
`5208cbdcbc3efbdd3770997134aef88472a291f3`, and
`2678444d55eaa80ed2fdd43fe745bb3748acf80c`, with canonical payload
`c064cf1971e08427b266de1f9768e98f11562998c09b8e8e828cf89cff48f297`.
The verifier rejects 38 of 38 hostile mutations.

## 2026-07-30 KoalaBear diagonal facet-mixing obstruction

The PROVED
`rate_half_kb_m2_r4_diagonal_facet_mixing_obstruction` deletes the
partition-preserving subcase of the diagonal order-two orientation. It is a
whole-fiber theorem, so it applies before the source-line/biquadratic split.
The fixed-point-free endpoint involution has exactly `c=2,4,6` crossings
between `I` and `J`, and its action on the common five-set has five exact
orbit rows:

```text
(a,b,c)=(2,0,2),(1,1,2),(1,0,4),(0,1,4),(0,0,6).
```

Here `a` counts involution pairs internal to `K`, while `b` records whether
the unique label of `I minus K` is paired into `K`. The common-`K` quartics
also split their roots between crossing and noncrossing `J` labels according
to whether the source label transports to `K`, `eta`, or `L^c`.

This changes the next diagonal action. A coordinate-style reciprocal
`I,J` locator descent is unavailable, and should not be attempted. Split the
8/7-dimensional norm equations and the biquadratic resolvent route by the
five rows, beginning with `c=2`, where four labels on each side remain
noncrossing and the transported support restrictions are strongest. A row
is closed only by inconsistency with the actual interpolation, exact degree,
irreducibility, deck distinction, and outer-factor interfaces.

The maximally mixed row sharpens further. The aligned case `L=I` is
impossible. In the near-aligned survivor, `eta` pairs into `K` and
`xi=I minus K` pairs with one label `ell in J intersect L^c`; the four
colored roots are exactly the two complete source fibers over `xi,ell`.
Their quotient locator `chi` is positive reciprocal, and both partial
resultants descend to

```text
Q_J ~ K_5^2 chi,       chi Q_I ~ R_7^2.
```

This is valid in both diagonal source-subfield branches. The `c=6` attack is
therefore one quotient system, not a search over arbitrary four-edge
divisors. The `c=2` rows remain the preferred next target because their
crossing support is smaller.

The `c=2` capacity ledger is now exact enough to expose coefficient
equations. With `J_0=J intersect tau(J)` and
`J_1=J intersect tau(I)`, the `(2,0,2)` row forces degrees four on `J_0`
and two on `J_1`. Its unique common-`K` quartic transported outside `K`
is the square `P_(J_1)^2`, while the product of the other four quartics is
`P_(J_0)^4`. In the `(1,1,2)` row, both the aligned case and the
near-aligned case with `tau(eta) in K` force
`R_(tau(eta)) ~ P_(J_1)^2` and saturate the two `J_1` labels. The unique
exception has `L!=I` and `eta,tau(eta) in J_0`, with total `J_1` incidence
between six and eight. The next low-compute step is therefore algebraic:
substitute the forced square fiber into `G=U^2-WV^2`, impose the resulting
coefficient minors, and combine them with the four-fiber fourth-power
identity. A reciprocal square fiber alone is not a contradiction.

That coefficient substitution is now exact in the source-line branch. The
PROVED `rate_half_kb_m2_r4_diagonal_c2_square_fiber_linear_cut` separates
the forced source orbit according to deck ramification. Off the branch
values of `W=X^2`, both star equations force `U(T,w)` and `V(T,w)` into
the fixed line spanned by `P_(J_1)`. The four independent linear equations
reduce the `epsilon=+1/-1` spaces from `8/7` to `4/3`, and their three
coefficient minors have the exact common reciprocal quadratic and linear
quotients printed in `(KBC2-5)`. At the ramified orbit `{0,infinity}`, only
one value of `U` is visible; the rank is two and dimensions `6/5` remain.
This ramified escape is genuine at the present interface and must not be
folded into the unramified minor calculation. Priority is now (i) seek an
exact exclusion of a common-`K` branch-value label, then (ii) apply the
four-fiber identity and `45 x 12` interpolation gate to the `4/3`-parameter
unramified forms.

The first ramified escape is now gone. In the `(2,0,2)` source-line row,
the two reciprocal ramified fibers would contribute two distinct doubled
star vertices, costing two units of complete-source defect. The four
remaining common-`K` labels are then unramified and contribute eight reduced
stars on the six possible edges of `J_0`; balancing eight units over six
vertices costs at least two more. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_202_ramified_defect_exclusion` therefore
gets defect at least four against the budget three. Every surviving
source-line `(2,0,2)` packet lies in the `4/3`-dimensional unramified
coefficient locus. The biquadratic source-cover branch and the ramified
possibility in `(1,1,2)` are not affected.

The same defect ledger closes more than the ramified subcase. In every
source-subfield branch, the square `P_(J_1)^2` consists of two identical
reduced stars, and its whole-fiber reciprocal partner is a second square on
the two crossing `I` labels. These are distinct doubled vertices and cost
defect two. Together with the exact two-unit floor from the eight `J_0`
stars, every `(2,0,2)` packet has defect at least four. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_202_defect_exclusion` therefore deletes the
entire orbit row, not merely its ramified source-line branch. The diagonal
mixing frontier drops from five rows to four:

```text
(1,1,2), (1,0,4), (0,1,4), (0,0,6).
```

Next attack the saturated `(1,1,2)` square-fiber cases with the one remaining
defect unit, while retaining the exceptional unsaturated orbit.

That saturated frontier is now finite and exact. The two reciprocal square
vertices have weight exactly two, so only one global collision remains
available. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_saturated_defect_classifier` forces four
pure `J_0-J_0` and four mixed `J_0-J_1` common-`K` edges, each `J_1` label
used twice, with at most one repetition. The `J_0` profile is one of
`(2,2,4,4),(2,3,3,4),(3,3,3,3)`. There are `1,560` labeled multiset packets
in `123` orbits under matching-preserving relabeling. In the source-line
branch, individual-star transport leaves only `96` labeled packets in `12`
orbits and forces all four mixed edges distinct. These counts are
combinatorial admissibility, not component realization. Route the twelve
source-line orbits through the coefficient/interpolation gate, the 123
branch-independent packets through the split resolvent, and keep the
exceptional `(KBDM-10)` orbit outside both queues.

The twelve source-line orbits now share one exact quotient compiler. For
`K_Lc={k in K: tau(k) in L^c}` and `Omega=tau(K_Lc)`, the four distinct
mixed common-`K` stars transport to all four universal `I-J` stars. Hence
`|Omega|=2`, both quotient fibers are unramified, and the PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_source_line_colored_quotient_compiler`
gives

```text
C_H ~ chi_Omega(psi),
Q_J ~ K_5^2 chi_Omega,       chi_Omega Q_I ~ R_7^2.
```

The quotient is explicit: `Omega=J_1` when `L=I`, while
`Omega={xi,ell}` in the near-aligned case with `tau(eta) in K`; no
`tau`-invariance of the latter pair is asserted. This replaces an arbitrary
squarefree-quartic search by two printed quadratic cases. Next combine the
aligned and near-aligned quotient systems separately with the exact `4/3`
or `6/5` reciprocal coefficient cuts. The biquadratic branch and exceptional
unsaturated orbit remain outside this reduction.

The internal common-`K` orbit now gives a scalar pre-interpolation test.
The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_source_line_odd_part_incidence_gate`
shows that this orbit cannot be source-ramified: its two ramified fibers
would spend at least two pure-edge collision units against the one-unit
residue. At either unramified fiber the two pure stars are distinct and
share exactly one `J_0` endpoint `a`, so `U(a,z)=V(a,z)=0`.

If the forced square orbit `w` is unramified, `V!=0` by source-deck
distinction and `V(T,w)~P_(J_1)(T)` pins the full reciprocal odd part.
For `q=q_0+q_1T+q_2T^2` and sign `epsilon`, define

```text
F=q_0-epsilon*w*q_2,       G=epsilon*q_2-w*q_0,
M=q_1(1-epsilon*w),
N_epsilon(a)=F+Ma+epsilon*G*a^2,
D_epsilon(a)=G+epsilon*Ma+epsilon*F*a^2.
```

The denominator is nonzero and every survivor obeys
`z=-N_epsilon(a)/D_epsilon(a)`. Thus each aligned or near-aligned
unramified record has four cheap exact tests, from two signs and two `J_0`
orbits, before interpolation. A passing record retains only two/one affine
`U` parameters after normalizing `V` and imposing `U(a,z)=0`. The
forced-ramified source branch remains open.

The apparent forced-ramified coefficient branch is now repaired by the
complete-source row ledger. At a ramified forced fiber, only the two rows
indexed by `Root(q)=J_1` vanish. Each row divides `B/z_i` and therefore has
order at most two at the double source pole, while local saturation requires
their total order to be four. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_ramified_complete_source_repair`
forces the allocation `(2,2)`, which is equivalent to

```text
U(T,0) in <q>,       V(T,0) in <q> minus {0}.
```

Thus the ramified source spaces also have dimensions `4/3`, and `(KBOI-3)`
applies with `w=0`. Geometric source ramification remains possible, but it
does not create a separate coefficient attack. Every saturated source-line
`(1,1,2)` record now passes through the same four sign/orbit incidence tests
before the aligned or near-aligned quotient identity.

The remaining `U` coefficients are now reconstructed by one internal star
pair. On the forced-square space `S_epsilon(w,q)`, evaluation at the
internal label `z` has zero kernel: otherwise reciprocity would factor
`U=chi_z(W)R(T)` and force `q=P_(J_1)` to be a reciprocal endpoint
eigenform, contrary to `tau(J_1) subset I`. The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
makes this a `3 x 3` isomorphism for the positive sign and an injective
two-plane for the negative sign.

Given internal edges `e,f`, their pinned odd-part difference fixes the
relative star scalars and therefore fixes `U(T,z)`. The positive source form
is unique; the negative form is rejected by one linear image-plane equation
or is unique, modulo source-deck conjugation. The five pure multisets have
exactly `2,2,4,2,2` compatible internal assignments. Every source-line
packet is therefore a finite list of at most eight source-deck pairs, with
no coefficient parameter left.

The PROVED
`rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
extracts a cheaper necessary condition from the first colored quotient.
For `q=P_(J_1)`, `G=U^2-WV^2`, forced label `w`, and the two mixed common-`K`
labels `k_1,k_2`, every reconstructed actual form satisfies

```text
Res_T(q,G) ~ (W-w)^4 ((W-k_1)(W-k_2))^2.           (KBQS-1)
```

The target quadratic is `tau^*q` in the aligned branch and
`tau^*chi_Omega` in the near-aligned branch. This is only a necessary
`J_1`-slice prefilter, but it replaces a degree-six partial resultant by one
quadratic-versus-quartic resultant. A light exact `F_1009` aligned fixture
tests `24` internal-pair/sign choices, reconstructs `12` positive forms, and
finds zero `(KBQS-1)` survivors. The route-deciding calculation is now to
factor the symbolic `(KBQS-1)` mismatches before evaluating `(KBQ2-2)` and
the remaining source rows on any exceptional forms.

### Compute request CR-KB-C2-112-QR-ELIM

This is the deferred exact-CAS version of that calculation; no run is
currently funded or launched. For each aligned/near-aligned branch, sign,
one of the five labeled pure multisets, and generic/ramified specialization
of `w`, do the following:

1. Substitute `(KBOI-2)--(KBOI-3)` and the unique internal-star
   reconstruction `(KBSR-2)--(KBSR-4)` into `H=U+XV`.
2. First compute and factor the coefficient residuals of `(KBQS-1)`. Only
   its exceptional locus proceeds to the coefficient residuals, with
   independent projective scalars, of

   ```text
   Res_T(P_J,H) ~ K_5^2 chi_Omega,
   chi_Omega Res_T(P_I,H) ~ R_7^2.
   ```

3. Clear only the printed nonzero denominators and saturate by label
   distinctness, `J_0 intersect J_1=empty`, nonzero star scalars, and exact
   source degree. Do not saturate by a conjectural genericity factor.
4. Return either a unit ideal/factor certificate deleting the shard, or the
   exact exceptional factor locus with a replayable witness assignment.

There are at most `2 x 2 x 5 x 2=40` independent shards. Each shard should
write partial factors before a `60 s` timeout; larger Gröbner or resultant
runs can be contributed independently. The local `F_1009` datum above is
evidence only, not a deletion or a substitute for saturation.

Upstream custody is draft PR `przchojecki/rs-mca#1132`, commit
`e6bde40cbb2e438a8a7faca333a34d8a7681c6b3`, note/verifier/certificate
blobs `a4e476ec50acca029868abc546396fca81afa97f3`,
`c3e011c7c31360d04dfa59ac2712928d341e6240`, and
`ed855d2ee936bdfcfc61937d449ec151227c0224`, with canonical payload
`66b83997ed25269d8d79e5d77291dcb3638835356cb895b827f90c9f287a86cf`.
Its verifier classifies all `10,395` fixed-point-free matchings, including
the `120/600` maximally mixed split and all three near-aligned `c=2`
matching classes, checks the exact ramified/unramified source-line ranks,
minor signs, the ramified and full `(2,0,2)` defect exclusions, and the
saturated `(1,1,2)` classifier, checks `2700/900` aligned/near quotient
rows, checks the `12` admissible internal edge pairs and exact odd-part
incidence map, verifies the ramified `(2,2)` order allocation and repaired
`4/3` dimensions, checks the `2,2,2,2,4` finite reconstruction and maximum
eight source-deck pairs, checks all three q-slice incidence patterns, and
rejects `118` of `118` hostile mutations. The latest extension report is
`przchojecki/rs-mca#1132` comment `5131961677`.

### Work-cycle burn-down: diagonal c2 square fibers

```text
starting local pin:       670c3dc5 (pre-c2 capacity refinement)
ending local theorem pin: 0d9990c030978339e15c1d930275e14ffb3be5bd
canonical prize pin:      11cea27b (unchanged)
ending upstream pin:      e6bde40cbb2e438a8a7faca333a34d8a7681c6b3
node attacked:            rate_half_band_closure via diagonal c=2
result:                   NARROWED + EXPORTED
DAG delta:                +9 PROVED nodes, +28 edges; target status unchanged
upstream delta:           c2 capacity, linear cut, 202 deletion, 112 classifier,
                          source-line quotient descent, odd-part incidence,
                          ramified coefficient repair, internal-star
                          reconstruction, and q-slice resultant in PR #1132
delta-star movement:      none
new assumptions:          none; (1,1,2) ramified and biquadratic survivors retained
live compute requests:    CR-KB-C2-112-QR-ELIM (external/deferred; 40 shards)
next route-deciding step: factor the q-slice mismatch on at most eight
                          reconstructed source-deck pairs per packet
```
