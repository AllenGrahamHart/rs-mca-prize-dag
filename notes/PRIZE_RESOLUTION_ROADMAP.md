# Prize Resolution Roadmap — r3, the date-free plan of record

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
  Surviving HGE4 levels now start at `m=128`. This is a real zero-debit level
  close, but one small level is not yet the D1 uniform HGE4 purchase.
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
  genuinely wild and unanchored maps; pay growing signed
  layout/core-defect/petal polarity; and handle arbitrary petal locators
  outside one common pencil. Dense support on a source petal is not sufficient
  to supply the anchor. The `F_9` additive right-component fixture proves that
  wild uniqueness needs extra multiplicative-domain geometry.
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
  Fixed `kappa` is polynomial across all tame anchored maps. The exact
  pullback frontier is therefore the nonpositive gate, unbounded `kappa`,
  wild decomposition, or missing whole-petal anchor.
  `l1_pullback_coverage_kernel_tradeoff` then removes `kappa` as a separate
  mechanism: exactly `kappa=max(0,k-sb)`, and every listed word satisfies
  `kappa<=max(0,z-ell+1)`. Hence `z<=ell-1+K` automatically supplies the
  router's `kappa<=K` hypothesis. The exact pullback frontier is now the
  nonpositive Johnson gate, growing partial-loss excess, wild decomposition,
  or missing whole-petal anchor.

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

- **Counts** (refreshed from `dag.json`, the single source of truth): critical
  surface 201 PROVED / 36 CONDITIONAL / 23 open
  mathematical red leaves; req-closure of `prize` = 260 nodes. The separate
  submission dossier is a target artifact rather than a mathematical leaf.
- **Wired bottlenecks** (no alt, no upstream substitute):
  `l1_mixed_petal_amplification`, `rate_half_list_adjacent_crossing`,
  `rate_half_band_closure`, + the dossier. There is NO MCA-only resolution
  (F1 pole pricing imports the base-row list threshold).
- **The true critical path:** `l1_mixed_petal_amplification` — in the
  irreducible core under every wiring including the RK world, wired into
  both grands, and the longest-stalled core leaf.
- **Minimal win sets:** unconditional = all 23 mathematical leaves + dossier
  (pure AND). `list_grand` alone = {l1, adjacent_crossing}, closing its five
  conditional ancestors. The former `17/20` RK-prune and direct-prune counts
  predated the N11 truth ruling and are retired pending a fresh route-surgery
  audit; do not cite them. The former worst-word route is retired.
- **Clean-rate scope (Conflict-4 resolved):** the proved
  `f1_pole_same_rate_scope_router` pins that base-field and tower pole pricing
  preserve `(D,kappa)` and hence the RS rate. The clean-rate MCA/list
  milestone therefore excludes both rate-half mathematical leaves. The global
  all-rate F1 dependency remains correct for the full prize. On the corrected
  board the clean-rate milestone contains 21 of the 23 mathematical leaves;
  the two excluded leaves are the rate-half band and list-adjacent targets.
- **Concentration risk:** 12 of 23 leaves and 3 of 5 demotion triggers live
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
premise; the current clean milestone is 21/23 mathematical leaves. N6 harness
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
