# Wave-18 fresh-context replay audit + master integration — v7 full-prize-resolution (HGE4 quarter-cap + XR shell compression + c1c2 one-antipodal ladder + DSP8 parity HOLD)

Auditor session 2026-07-21 (agent a5e4b3c, 79/79 replays, 5/5 mutations, validator
PASS at pin). Catch numbering LOCAL (w18-C#). Master integration same session;
ONE refusal-grade custody conflict HELD for the maintainer (the DSP8 parity
package).

## PINS
- **v7 pin**: prize-codex-resolution-v7-20260719, HEAD at audit start =
  **b5e5e884** ("Ledger XR extension family collisions"), no drift.
- **base** = wave-17 pin **173cd994**. Range = 46 commits.
- **master** at integration start: **62afe118** (wave-17 close, 994/2186).

## VERDICT LINE
**NOTHING CLOSES. NO CRITICAL-SURFACE STATUS EVENT.** +35 nodes (all PROVED,
HGE4 7 / XR 13 / c1c2 14 / DSP8 1), 0 removed, 0 per-node status flips; edges
+107 at pin (0 removed, 0 kind-changed), of which **105 imported + 2 HELD**
(the parity req pair). Fan-ins all ev: norm_gate_count 15->22,
adjacent_crossing 95->109, xr_highcore 29->42, dsp8_correlation_bound 22->23.
Zero new Modal launches; no vendored imports.

## CLUSTER VERDICTS

### HGE4 (7 nodes) — the width cap COLLAPSES AGAIN: floor(2m/7) -> m/4-1.
Chain: Kummer midpoint pencil router -> trace-power gate -> gcd compiler ->
**cyclotomic-norm quarter-width exclusion: E_h^prim(m,p)=0 for m/4 <= h < m/3**
(kills the whole Kummer near-third strip incl. cell (32,9,5)'s necklace debit
286) -> Haar swap router (near-quarter band h=m/4-d) -> **swap-norm exclusion:
the swap class is EMPTY whenever m^(h-1) >= h^(m/4)** (band 1 <= d <=
floor(m/(2s))-1; d <= ~2.68e10 at 2^41; both parities of the Haar band empty)
-> Vandermonde-defect band (cubic-sharpened; ~5.5e9 (m,d) cells deleted).
**NEW EXACT RESIDUAL (ERT4'''')**: per level m=2^r >= 16, p == 1 mod m,
p > m^2: `sum_(h=4)^(m/4-1) E_h^prim(m,p) <= (21/2)m^2` — OPEN. The live
lower quarter = 3 zones: VDE band (no primitive pair), rest of swap-norm band
(free class only, swap dead), deeper widths (free AND swap open). Nonclaim of
record: "the proved exact-level cap is m/4-1". Neither wave-17 residual piece
CLOSES: the aggregate is open, and the swap class dies only down to
h ~ (m/4)(1-2/s), not globally. The wave-17 WIP kummer node is now a full
committed packet.

### XR (13 nodes -> xr_highcore_collision_count) — route compressed, frontier UNMOVED.
Pays: collapsed-face exclusion (|X| >= a+3); first shell = single
quadratic-pullback Mobius-involution chart class; Maxwell-deficit router;
**primitive full-core rank-two EMPTY on all shells 2 <= d <= ~2.2e7/1.9e7/4.5e6
(caps 384/448/960), endpoint exact**; **(P3E5): no primitive full-core trade of
ANY rank on the first shell |X|=a+3 at any prize row**; circuit-arity
compression to 4/5 blocks (Segre atlas); three-anchor dual-GRS3 ledger;
four-anchor quadric-centroid atlas; dual support-extension iff; received-pair
alternating router (converse honestly scoped); per-row extension count closed;
pairwise packing ledger. **P-A first-open selector ranks UNCHANGED: 5,5,5 /
17,17,15**; P-B untouched (zero file changes, in-deg 24). No #158-type
quantifier slips (all 13 statements scope full-core primitivity vs proper
local circuits). xr_highcore has NO verify.py — md-only import, clean.

### c1/c2 (14 nodes -> adjacent_crossing) — one-antipodal gate ladder; NO chamber closed.
C2-PAR split: exact-one-antipodal reducer + (P,Z) product/ratio circuit;
Fourier ladder; negation syndrome (support >= 3H+1); collision router (generic
all-distinct-weight quartic excluded at min support; exactly one colliding
pair, (4*gamma-alpha^2)^3 = 8*alpha^3*beta^2); Euler cube-resultant gate;
endpoint torsion Xi^(2^39)=1; infinity-cell quartet gate; Stepanov cap
#Y_a <= 355,106,851 < 2^29 on all official fields; collision-or-high-support
router; degree-defect globalization (floors 3H+1/3H+3/3H+7). "Neither circuit
is yet proved empty"; none of the 13 budget-3 chambers closes; **nonclaim
intact** (budgets 1-2 exact; B*>=3 open; no MCA/CA claim; "no Modal run is
authorized" — scoped contributor requests instead).

### DSP8 — 1 clean node IMPORTED; the parity package HELD (w18-C1, REFUSAL-GRADE).
IMPORTED: nodal_trace_orbit_energy_router (honest disclaimers; own-packet pins;
+1 ev -> correlation_bound). **HELD ENTIRELY — the parity package** (commits
9f9da6e0/1facf392): it REWRITES (not annotates) the statements of
joint_star_depth_pareto_compiler and single_quotient_endpoint_compiler
(odd-row C_E table replaced in place; SQE chain renumbered; (319/153)n^2 ->
(29/153)B_par(n)) AND the two master-held statements correlation_bound +
official_order_template_survivor (file AND dag string), adds 2 req edges
(affine_coset_pair_cubic_preimage_stepanov -> joint_star, single_quotient),
and ships a single_quotient verifier with a **NEGATIVE MARKER PIN asserting
the old (319/153) formula is ABSENT** — irreconcilable with custody #155
(annotate-never-rewrite) without maintainer ratification of supersession.
HELD pieces: 2 req edges, 2 node re-takes, 4 statement rewrites (2 dag
strings). MAINTAINER DECISION: ratify the supersession (then land the package
atomically per the audit's coupling list) or keep held. Note the wave-17
dated-addenda item for correlation_bound/official statements is FOLDED INTO
this same decision (landing them now would create three-way divergence).

## GOVERNANCE
- 3c9726b3: PURE INSERTION into notes/PRIZE_COMPUTE_REQUESTS.md (contributor
  handoff template + a policy line ">= $1 / unknown / could-exceed-balance =>
  do not launch" — a TIGHTENING, compatible with master's w17-C1 annotation).
  References upstream PR przchojecki/rs-mca#999 (contributor-compute PR —
  watch item). NOT auto-adopted (master's file diverges deliberately;
  reconciliation folded into the roadmap-divergence deferral).
- 8f779e3b: restores the focused verifier_replay.json ledger after 9f9da6e0
  overwrote it — bookkeeping, part of the held parity package's lineage.
- **ZERO new Modal launches** (no new app_ids/*_modal.py/result.json in range;
  remote_launchers 10 everywhere). UPSTREAM_IMPORT_LEDGER unchanged.

## MASTER INTEGRATION RECORD (this session)
- +35 background node folders from pin b5e5e884; +105 edges (2 parity req
  edges HELD); dag 994->1029 nodes, 2186->2291 edges (pin has 2293).
- Pose re-takes (reverse-consumer-pins): norm_gate_count
  {attack,claim_contract,frontier,statement,verify} + dag statement string
  (the m/4-1 nonclaim travels with the pose); adjacent_crossing
  {attack,dependency_subdag,frontier,statement,verify} (dag string unchanged
  this wave; 109-entry incoming pin). Master-unique route lines on
  norm_gate_count (minting-era claim_contract/frontier prose) preserved as
  dated PROVENANCE ADDENDA per custody #104.
- xr_highcore_collision_count: 5 md files taken (frontier bookkeeping aligning
  text with the known 5,5,5/17,17,15 ranks); no verify.py; dag string unchanged.
- Statement-string holds maintained: the ~14 carried master corrections + the
  4 parity-package rewrites (joint_star, single_quotient, correlation_bound,
  official_order_template_survivor).
- 3 kind-hold edges: still req on master (unchanged at pin — no new conflict).

## VERIFICATION (in place, on master)
- Validator PASS: 1029 nodes / 2291 edges; PROVED 845, TARGET 68, CONDITIONAL
  41, CONJECTURE 15, PROVABLE 27, REFUTED 26, WALL 7.
- New-node battery **70/70 PASS**. Both re-taken poses PASS (norm_gate 441
  monotonicity cases; adjacent_crossing status PASS at 109 brackets). Belyi
  auditor PASS against the new statement.
- Consumer blast-radius **160/160 PASS** (adjacent_crossing 85, norm_gate 22,
  xr_highcore 17, dsp8_correlation 21, joint_star 2, single_quotient 1,
  official 12). Held parity nodes' own verifiers PASS on master's held state.
  Mobius amber PASS.
- Manifest refreshed: scripts 704->774 (+70), proof_assets 955->1025,
  remote_launchers 10; VERIFIER_MANIFEST_PASS. (774 vs pin's 775 = the
  pre-existing one-script gap, recorded at wave-17.)
- No Modal re-pin (all wave-18 verifiers are bounded local cert/algebra
  checks; audit independently replayed 79/79 at pin + 5/5 mutations).

## OPEN / DEFERRED
- **w18-C1 (NEW): the DSP8 parity package** — maintainer ratify supersession
  or keep held (includes the folded wave-17 addenda item).
- w17-C1 (three Modal screens + sub-$1 policy) — still open.
- Upstream PR #999 (contributor compute) — watch.
- w15-C1 kind-changes, roadmap divergence, KB #107 harness fix — carried.
- INFO: pre-existing duplicate edge petal_descent_classification_bridge ->
  petal_g1_k4_scale_reserve (base=pin=master); the one-script manifest gap.
