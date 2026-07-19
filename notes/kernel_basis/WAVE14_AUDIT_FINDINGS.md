# Wave-14 fresh-context replay audit — v6 H3 double-accident coupling + exceptional resultant chain + deleted-pair Legendre + intermediate Hensel

Auditor session 2026-07-19. Catch numbering LOCAL (w14-C#). READ-ONLY both repos.
INCREMENTAL — written as the audit proceeds.

## PINS

- **v6**: /home/u2470931/smooth-read-solomin/prize-codex-resolution-v6-20260718,
  branch codex/full-prize-resolution-v6-20260718. HEAD pinned at audit start =
  **dce7460c** ("Pin the exceptional middle-Hankel factor", 07-19 11:53).
- **master**: /home/u2470931/smooth-read-solomin/prize, HEAD **db0c1229**
  ("wave-13 re-pin 382/382 PASS complete", 07-19 06:48) — the wave-13 import
  has LANDED on master; master carries the wave-13 nodes with the D1-D4
  repairs and the two refusals.
- Scope = fb1d8bfb..dce7460c = **28 commits** (verified count), 07-19
  06:08..11:53.
- **WORKTREE MOVED DURING AUDIT (procedural; third occurrence, cf. w11-C5,
  w13 log)**: one post-pin commit **8f91ed84** ("Resolve the exceptional
  Hankel kernel plane", 12:01) landed within minutes of the pin. PIN STANDS;
  all reads via `git show dce7460c:`; all replays in the pinned mini-tree
  w14_tree/ (git archive of dce7460c). dce7460c..HEAD = WAVE-15 SCOPE; the
  Hankel exceptional lane is still hot.

## VERDICT LINE

- **CENTERPIECE (C36 / f3_h3_mobius_excess_half): NOT CLOSED — REDUCED/
  REFORMULATED, and honestly so.** The node stays TARGET at pin; the range
  n^2<=p<=6^(n/4) is unchanged; every new node carries explicit nonclaims.
  What the five H3 nodes deliver:
  (a) The H3 double-accident coupling suite (4 nodes) builds a NEW fixed-order
  sieve on the C36' route: a positive Y_18 target forces the row prime p to
  divide the norm of an explicit nonzero coupled ideal
  (alpha_F, alpha_G, theta, lambda) with norm <= 6^(n/4)/4, so all Y_18>0
  primes lie in a finite explicitly-generated set; the zero-coupling locus is
  exactly the binary telescoping family {x,y,z}={q,-q,-q^2}, w=q^4 (3(n-4)/2
  anchors); odd-saturation syzygies collapse the generator types to one
  coupling cross. Explicit nonclaims: no efficient candidate construction, no
  survivor bound, no ideal-index lower bound.
  (b) The distance-six split-pencil router is an EXACT reformulation of the
  wave-13 analytic residual: the E=6 disjoint-support moment
  D_6,25^0+(17/10)D_6,25^A <= (223/20)n^2 becomes the integer correlation
  10J_25^0+17J_25^A <= 892n^2 (J=8D; factor checked) between disjoint split
  members of the quadratic pencil Q_(t,r)(X)=X^2-(1+r-t)X+r and the affine
  subgroup-line fiber {z: 1-t(1-z) in H\{1}}, with the exact split-pair pin
  (X-r)Q_(t,s)-(X-s)Q_(t,r)=t(s-r)X. "This router supplies no estimate for
  (DSP8)" — verbatim nonclaim.
  **EXACT RESIDUAL AT PIN (C36 lane)**: (i) analytic route — bound the
  split-pencil / line-fiber correlation (DSP8); (ii) fixed-order route —
  an efficient official-order template generator + survivor bound for the
  coupling-cross ideal sieve (recorded as updated CR-001, deferred).
  All five nodes' load-bearing algebra HAND-RE-DERIVED by the auditor
  (valuation ladder 2^{v_2(a)}, involution descent to {q,-q,-q^2,q^4},
  zero-count 3(n-4)/2, CBS2 norm 2^(2^r-1), syzygies CBS4/CM2/CM3, the
  ideal-equality chain CM5, partial-matching bound CM6, DSP1-DSP8 incl. the
  cubic difference and the factor-eight orientation count): ALL CORRECT.
- **Core-one/Hankel (9-node exceptional resultant chain): NEITHER
  active-trace system closed** (sub-audit A, SOUND, zero catches). The
  chain is an exact normal-form reduction of ONE stratum of the D_*=1
  active-exceptional-trace system (b=0, c=z=1, X_1=1, eps_0=0); D_*=0
  wholly untouched; the c=2 profile and z=0 stratum untouched. Residual:
  the corrected complement square in triangular form + pinned
  middle-Hankel factor, still owing division gates, degree boxes,
  cofactor products, splitting. No band-budget movement; band TARGET;
  post-pin 8f91ed84 continues the lane (wave-15 scope).
- **Deleted-pair (4 Legendre + 4 generic-Euler nodes): REDUCED, not
  closed** (sub-audit B, SOUND). "Legendre" = Legendre POLYNOMIALS (not
  symbols): the scalar gate collapses to sigma=2H_{4M-1}(t) with
  H_n(r^4)=r^{2n}P_n(...); trace eliminated; residual = TGR7 gcd
  triviality (12 triples: 3 branches x 2 torsion signs x 2 s-signs,
  degree <= 2^36) for every official p, with a proved torsion-necessity
  fence blocking torsion-free shortcut proofs. The official batch is
  DEFERRED as compute request **CR-002-L** ("theorem/algorithm request,
  not a request to start containers") — honest deferral, no census
  smuggled. Intermediate lane bonus: TWO genuine exclusions (maximal
  intermediate antipodal floor EMPTY; the 4,581,298,449-degree band
  [91,625,968,980, 96,207,267,428] EMPTY); stratum open above
  v >= 96,207,267,429.
- **Replays (main thread)**: H3 9/9 PASS (5 verify.py + 4 verify_audit.py;
  split-pencil router has no verify_audit.py); mutation controls 3/3 TRIP
  (statement zero-count corruption; DSP8 constant corruption; req-parent
  status flip — tripped by BOTH the node verify.py and the tree validator,
  an improvement over the wave-13 division-of-labor pattern). Global
  validator at pin: PASS, 822 nodes / 1622 edges. Manifest: ALL 1072
  entries hash-verified at pin (0 missing, 0 stale).
- **NO NEW STATUS FLIPS**: per-commit scan over all 28 commits = ZERO
  status flips among shared ids (incl. transient); 28 node adds, 0 removes.
  No fourth packaging flip attempt; the wave-13 REFUSED packaging PROVED
  persists as inherited branch state (base->pin identical; pin-vs-master
  flip = the old refused one; import continues to strip it).
- **GOVERNANCE: ZERO new Modal launches** — all 28 roadmap increments state
  "no Modal compute"; remote_launchers unchanged at 10; no new result.md /
  app ids anywhere in-range. New governance object instead: deferred
  request CR-002-L with explicit cost-refusal language ("no reasonable
  cost envelope", "official batch is unauthorized here and likely well
  above the current sub-$1 budget"). The "current sub-$1" phrase again
  normalizes the UNRATIFIED override (#260 annotation duty recurs at
  import). The maintainer ratify-or-veto backlog stays at 9 jobs (no new).

## DAG-DELTA HEADLINE (w14_dag_delta.py; output w14_dag_delta_output.txt)

Net vs master db0c1229 AND vs base fb1d8bfb: **794 -> 822 nodes (+28, ALL
PROVED, 0 removed)**; 1555 -> 1622 edges (+67). 1:1 commit->node. The 28:

- 5 f3_h3_* (4 double_accident coupling suite + disjoint_distance_six_
  split_pencil_router) -> 5 ev into f3_h3_mobius_excess_half (32->37)
- 9 rate_half_ca_hankel_a1_core_one_exceptional_only_* (linear req chain)
  -> 9 ev into rate_half_band_closure (44->53)
- 14 rate_half_list_budget_three_antipodal_* (4 generic_deleted_pair_* +
  4 generic_euler_* + 6 intermediate_*) -> 14 ev into
  rate_half_list_adjacent_crossing (45->59)

STATUS FLIPS vs base: NONE. vs master: only the inherited refused
packaging. Node-id collisions: none (f3_h3_double_accident_derivative_ideal
is a pre-existing wave-10 node, distinct from all new ids). Duplicate-edge
hygiene: only the pre-existing both-sides petal pair (x2). All new-node req
parents exist on master's dag (13 external parents verified present) — no
smuggled poses at wiring level.

File custody (w14_custody.txt): 226 paths = 209 adds (EXACTLY the 28 node
folders: 13 x 8 files incl. verify_audit.py [9 hankel + 4 H3 coupling],
15 x 7 files WITHOUT verify_audit.py [14 antipodal + the split-pencil
router]; 13*8+15*7=209 verified — w13-A3 asymmetry persists on the
antipodal lane and now also one H3 router) + 17 M
(the two consumer node folders' md files + pose verify.py, band
statement/proof, dag.json, 2 notes files, verifier_manifest.json). No
orbit renders, no experiments/, no background/nodes/packaging touches.

## THE ONE IN-RANGE SHARED-NODE DAG MUTATION (w14-C1)

Full-dag field sweep base->pin: EXACTLY ONE shared node changed in ANY
field — **f3_h3_mobius_excess_half.attack_surface rewritten in place
AGAIN** (the w13-D1 pattern recurring on the same field, second
occurrence). Pin text: content-honest (adds the double-accident
nonzero-coupling gate as a fixed-order alternative, keeps the E=6
preferred target, KEEPS the broader-alternatives + M35 sentences, adds
"Its nonzero-entry count is not an ideal-index bound" + "Every prime
outside this finite candidate set has Y_18=0" — both claims proved
in-range). But master's field is the wave-13-REPAIRED version (original
negative framing + dated [WAVE-13 ADDENDUM]); the pin edit builds on the
UNREPAIRED wave-13 pin text. REPAIR AT IMPORT (mandatory): keep master's
field verbatim and append a dated [WAVE-14 ADDENDUM] carrying the pin's
new sentences. Full three-way texts banked in w14_attack_surface_texts.txt.

## CONSUMER-FILE #104 SWEEP (f3_h3_mobius_excess_half, main thread)

- statement.md: pure append (+26; the DSP normalization block, "It remains
  open" retained, "This router supplies no estimate" nonclaim). UNDATED.
- attack.md: pure appends (+74, two mid-file blocks; honest "not an
  independence or ideal-index lower bound"). UNDATED.
- frontier.md: pure appends (+31; "No correlation bound is yet proved").
  UNDATED.
- dependency_subdag.md: pure append (+5 rows for the 5 new ev edges).
- claim_contract.md: +20/-4 — the 4 deletion lines are two in-place
  EXTENSIONS in living fields (proved-dependencies list extended;
  "current proof route" paragraph extended with the DSP8 equivalent and
  the double-accident template guidance). FALSIFIER PRESERVED VERBATIM
  ("one exact official row with 17X_18>300n^2"). New-open-content range
  line UNCHANGED. Same class as w13-D2 -> addendum-ize at import.
- Undated appends = w13-D3 recurrence -> date all blocks at import (w14-C2).

## GOVERNANCE DETAIL

- notes/PRIZE_RESOLUTION_ROADMAP.md: PURE APPEND (0 deletion lines), 28
  increment paragraphs. Counts quoted in the paragraphs (e.g. "795 nodes
  ... 628 PROVED") are branch-true and INCLUDE the refused packaging
  discharge — at import annotate as at wave-13 C.1 (master-true PROVED is
  one lower throughout).
- notes/PRIZE_COMPUTE_REQUESTS.md: header table rows updated in place
  (living planning doc; CR-001 re-titled "high-excess / double-accident
  certificate", CR-002 readiness updated), large honest additions:
  CR-002-L deferred batch spec (cleared branch polynomials B_0/B_1/B_2,
  PASS/FAIL artifact contract, "explicit prohibition on a
  root-by-characteristic sweep", 4,495,441-moduli x 2^40-roots cost
  refusal); CR-001 double-accident template/checker/certificate spec
  (replays both syzygies; "reconstruct but do not factor the full
  rectangle").
- **w14-C3 (import hazard, must-handle)**: the Legendre-collapse node's
  verify.py PINS FOUR MARKERS INSIDE notes/PRIZE_COMPUTE_REQUESTS.md
  (B_0/B_1/B_2 formulas + "root-by-characteristic"). A PROVED node's
  replay is thereby coupled to a governance notes file that import policy
  annotates/edits (#260). The import must land those exact markers (the
  CR-002-L block) in master's compute-requests file IN THE SAME COMMIT as
  the node, or the node's verify fails on master. Flag to Codex: node
  verifiers should not pin planning-file content (notes are living,
  maintainer-annotated); pin request text in the node's own folder instead.
- Modal governance enumeration (#260 follow-on): NEW apps this range:
  NONE. Backlog unchanged: 9 jobs awaiting ratify-or-veto.

## CLUSTER VERDICTS

### Cluster H3 (main thread) — SOUND / IMPORT-ELIGIBLE WITH REPAIRS (C1, C2)

All five nodes hand-traced at depth; every load-bearing identity
re-derived independently (details in VERDICT LINE). Verifier quality high:
the joint router's verify.py is a genuine exact toy-row fixture
(n,p)=(32,1153) with exact-division integrality proofs, real cyclotomic
norms via Bareiss, p-divisibility + 6^(n/4)/4 bounds, AND a built-in
negative control (wrong-target quotient must have nonzero coupling).
Dep statuses pinned in node verifiers (downgrade tripwires confirmed by
mutation M3). Nonclaims verbatim in all five statements. Consistency with
the wave-13 payment node checked: P>=25 class threshold (DSP7/DSP8) vs the
router-side P>=19/Y_18 sieve are separate lanes, correctly not mixed;
U(t)=(P(t)+D(t))/2>=10 arithmetic verified; D_6,25 definition in the
payment node (unordered-disjoint-edge x ordered-quotient records) makes
the factor-eight J=8D exact.

Independent auditor cross-checks (w14_checks.py, ALL PASS under ramguard
tiny): (1) zero-locus count brute-forced = 3(n-4)/2 at n=8,16,32
(6/18/42, matching the node verifier's printed anchors); (2) CBS2
|Norm(c_a)|=2^(2^r-1) for every a at n=16 by exact Bareiss norms;
(3) DSP3 P(t)=2|S_t|-diag(t) over ALL targets of the toy row (32,1153);
(4) toy-row 3x2 coupling rectangle: char-0 zeros form a partial matching
(one genuine zero found — CM6 non-vacuous). Audit.md quality: the matrix
node's audit explicitly fences the mr-min(m,r) count against
independence/index misuse; the split-pencil audit states "cannot promote
C36'".

### Cluster A — Hankel exceptional-only chain (sub-audit A) — SOUND /
IMPORT-CLEAN; closes NOTHING; zero catches, 4 observations

- **TRACE-SYSTEMS VERDICT: NEITHER of the two wave-13 active-trace
  systems is closed.** The 9-node chain attacks ONLY the D_*=1
  active-exceptional-trace system, and within it only ONE
  already-enumerated stratum of the master-audited ACR6 classification:
  the profile b=0, D_*=1, c=z=1, X_1=1, epsilon_0=0 ("exceptional-only":
  one zero-trace bad row, no exceptional incidence, sole active factor =
  the exceptional trace E_a=E_Z). **D_*=0 is untouched**; the z=0 stratum
  and the c=2 (epsilon_0=1) profile of D_*=1-active are untouched. NO new
  case split introduced (#137: the stratum selection reuses the
  master-audited enumeration; all parity facts used hold for every e).
- **What it delivers**: an exact reduction/normal-form chain — factor
  descent (q_0|P_X, corrected square), infinity-coefficient pin,
  two-sided resultant saturation (exact ledger Tr-1=e*n_X), unit
  resultant collapse (Res(Q,B_1)=c_X*q_bar, exponent D_0-n_X=1 exact),
  reciprocal resultant descent + Bezout normalization (literal Bezout
  certificate at X^{D_0-1}), full complement + reciprocal-square
  triangularization (FU+P_cl*L=R_X; FRS3/FRS4 with converse verified),
  middle-Hankel factor pin (adj M = c_H*E*q*q^T, omission count O=1 at
  gamma_0). Every load-bearing identity re-derived by the sub-audit;
  the formal-degree Sylvester lemma stack machine-verified (~1600
  randomized exact trials, 0 failures).
- **EXACT RESIDUAL AT PIN**: the exceptional-only stratum survives as
  the corrected complement square in triangular form — allocate
  F,U,W_vee,S; recover L,G,K_vee,V_vee via FRS5; still owed: the
  P_cl-division and two E-division gates, FRS3, degree boxes, Hankel
  cofactor products (with the pinned factor), splitting, irreducibility.
  Plus the untouched c=2 profile, z=0 stratum, and ALL of D_*=0.
  **No band-budget movement**: nothing touches {2^39, 2^39+1} or the
  beyond-2^167 brackets; rate_half_band_closure TARGET at pin. The
  post-pin 8f91ed84 confirms the lane continues (wave-15).
- **Unconditionality: CLEAN** — all external req parents PROVED on
  master; no new poses; no planning-prose deps; zero
  EXPERIMENTAL/pilot/Modal references in the 9 packets.
- **Replays 18/18 PASS** (9 verify + 9 verify_audit); scripts read-only,
  no network/subprocess; **mutations 5/5 TRIP** (statement exponent; dag
  parent flip; ev->note edge-kind flip; proof coefficient; omission
  count).
- **Consumer hygiene: PASS** — band statement/proof pure tail appends,
  all 9 sections DATED 2026-07-19, each ends with what remains open;
  manifest 18/18 hashes match.
- Observations (no catches): A-O1 substring-marker asserts don't trip
  suffix EXTENSIONS (fail-closed for deletions/replacements only);
  A-O2 verify scripts check packet coherence + fixtures, math weight in
  prose (fully hand-traced); A-O3 the HFP "residual generator = Q of the
  descent" interface assertion rests on master-audited AIR8/AIR9 —
  make the seam explicit at formalization; A-O4 exact-degree claims
  valid under the declared biform convention.
- Compute-law slips (self-reported): two trivial bare-python3 uses,
  self-caught; all substantive compute lawful.

### Cluster B — deleted-pair + generic Euler + intermediate + pose contract
(sub-audit B) — SOUND / IMPORT-CLEAN; deleted-pair REDUCED not closed

- **DELETED-PAIR VERDICT: REDUCED.** The wave-13 residual (uniform
  rejection over every official p and every lift ratio r of all three
  pairing branches) is NOT delivered — the sublocus stays open. What
  landed is a genuine compression: the CCG2 scalar gate collapses to the
  exact closed form sigma=2H_{4M-1}(t) with the LEGENDRE-POLYNOMIAL form
  H_n(r^4)=r^{2n}P_n((r^2+r^{-2})/2) (**"Legendre" = polynomials, NOT
  symbols** — w14-B4); the Chebyshev/Gegenbauer router reposes primary
  gap + torsion + gates as six unsquared linear-sign branches; the trace
  gcd router eliminates the trace variable — each branch nonempty iff
  gcd(C, G_eps mod C, E_(j,s) mod C) != 1, degree <= L=2^36 (TGR7); the
  torsion fence proves (via three exact M=1 certificate rows, Pocklington
  replayed) that any uniform-rejection proof MUST retain r^(32M)=1 in the
  rejection ideal — a strategy fence against torsion-free shortcuts.
  **EXACT RESIDUAL AT PIN**: for every official p = 1 mod 2^40 and each
  torsion sign epsilon (eps=-1 iff ord(r)=2^40), prove the TGR7 gcd
  triples are trivial for all j in {0,1,2} and both s with s^2=-eps
  (12 triples counting eps x s; "six" per torsion sign — w14-B1 wording).
  Consumer text verbatim: "Uniform proof that these six gcds are one
  remains open." Nothing rejected per-p yet; no census smuggled.
- **Generic Euler filters: SOUND** — four new necessary gates (Euler
  divisor remainder; cubic norm via Res identities with honest q=2 mod 3
  vacuity caveat; coupled gate N_Q=N_U^4; maximal-field character shard =
  a #137-COMPLETE case split e in {1,2} x (p mod 3), p != 3 forced by
  q >= 3*2^128). No silent character-triviality assumptions (only cubic/
  quartic characters used — orthogonal to the 2-adic congruence).
- **Intermediate lane: SOUND with real content — two GENUINE exclusions**:
  (i) 079f8a71: the maximal intermediate antipodal floor is EMPTY (V^2|P,
  4YDW=UA-3T^2, G | J=dA^3+27T^7 with multiplicities, deg J=18 < v);
  (ii) dee4bf3c: the band v in [91,625,968,980, 96,207,267,428]
  (4,581,298,449 degrees) is EMPTY; stratum remains open above
  v >= 96,207,267,429. Both "exclusion" titles earned; the three Hensel
  gates + cube-part router are now vacuously-scoped audit tools
  (w14-B3, dag redundancy not unsoundness). No official-range narrowing;
  TARGET stays TARGET.
- **POSE CONTRACT (KB #90): PASS** — pin verify.py pins all 14 ids +
  PROVED + per-node phrases; replay PASS; 34 physical deletion lines ALL
  classified benign (superseded guidance / resolved-open-item restated
  stronger; ZERO retractions); nonclaim "Budgets one and two are exact;
  the adjacent crossing remains open for B*>=3" survives verbatim; no
  refused text reintroduced.
- **Unconditionality: PASS** — all 6 external req parents PROVED on
  master; zero Modal/pilot references in the 14 folders; no
  planning-prose deps (NOTE: main-thread w14-C3 about the verify.py
  pinning notes/PRIZE_COMPUTE_REQUESTS.md markers stands — that pin is a
  same-commit import coupling, not a proof dependency).
- **Replays 15/15 PASS** (14 nodes + consumer); verify_audit.py 0/14
  (w14-C4 confirmed); **mutations 4/4 TRIP** (statement constant; dag
  req-parent flip; consumer expected-phrase tamper; sign flip).
- Catches: w14-B1 (wording: "six" counts per torsion sign; complete
  problem is 12 triples), w14-B2 (ILB4 cites the dependency's
  statement-level pin for a proof-level generalization — generalization
  independently re-derived TRUE, minor), w14-B3, w14-B4 (above).
- Compute-law slips (self-reported): two bare-python3 heredoc JSON
  one-liners (scratchpad-only), self-caught; all replays lawful.

## REPLAY GRAND TOTAL (verified counts)

- Node replays: **42/42 PASS** (main thread H3: 9 = 5 verify + 4
  verify_audit; sub-audit A: 18 = 9+9; sub-audit B: 15 = 14 + consumer
  pose verify). Plus: global validator PASS at pin (822/1622); manifest
  1072/1072 hash-verified; auditor independent cross-checks
  w14_checks.py 4/4 PASS; sub-audit A lemma stack ~1600 randomized
  exact trials 0 failures; sub-audit B spot-check script ALL PASS.
- Mutation controls: **12/12 TRIP** (main 3 — one tripping at BOTH node
  and tree level; A 5; B 4). Fail-open vigilance note: A-O1 (substring
  asserts don't catch suffix extensions) logged as hygiene, not a trip
  failure.
- Per-commit scan: 28/28 commits, 0 status flips, 28 adds 1:1.

## CATCHES (consolidated)

- **w14-C1 (#104, MUST-REPAIR AT IMPORT)**: f3_h3_mobius_excess_half dag
  attack_surface rewritten in place a SECOND time (only shared-node field
  change in the whole range). Restore master's repaired field + dated
  WAVE-14 addendum. (Detail + full texts above.)
- **w14-C2 (#104, minor)**: all mobius md appends undated; claim_contract
  route-field in-place extensions (falsifier preserved). Dated-addenda at
  import (w13-D2/D3 recurrence).
- **w14-C3 (import hazard)**: Legendre-collapse verify.py pins markers in
  notes/PRIZE_COMPUTE_REQUESTS.md — same-commit import coupling; ask Codex
  to stop pinning planning files from node verifiers.
- **w14-C4 (coverage, w13-A3 recurrence)**: the 14 new antipodal-lane
  folders + the split-pencil router ship verify.py only (no
  verify_audit.py); the 13 hankel/H3-coupling folders have both. The
  asymmetry Codex was asked to close persists on the antipodal lane.
- **w14-B1 (wording, minor)**: trace_gcd_router headline "six ... gcd
  tests" counts per torsion sign; the complete first-rejection problem
  is 12 gcd triples (3 branches x 2 epsilon x 2 s-signs).
- **w14-B2 (citation hygiene, minor)**: low_band_exclusion ILB4 cites the
  dependency's statement-level pin (floor v=(2^38-4)/3) for a
  proof-level generalization to general v; the generalization was
  independently re-derived TRUE by the sub-audit.
- **w14-B3 (observation)**: the three Hensel gates + cube-part router
  are scoped to the maximal floor that 079f8a71 proves empty —
  vacuously-scoped audit tools, honestly labeled; dag redundancy only.
- **w14-B4 (observation, terminology)**: "Legendre" in the deleted-pair
  lane = Legendre POLYNOMIALS, not symbols — keep future residual
  discussion unambiguous.
- **A-O1 (hygiene)**: substring-marker asserts in the hankel chain
  verifiers fail closed on deletions/replacements but NOT on suffix
  extensions; recommend exact-line or anchored asserts at import.
- **A-O3 (formalization seam)**: HFP's "residual generator = descent Q"
  interface assertion rests on master-audited AIR8/AIR9; make explicit.
- (positive) No new Modal; no packaging flip attempt; roadmap pure-append;
  manifest fully verified; zero shared-node dag drift beyond C1; band
  appends fully dated (better #104 hygiene than the mobius lane); pose
  contract delivered same-range (no wave-12-style first-replay hazard).

## IMPORT SURGERY SPEC (all content at pin dce7460c; statements MERGED
never replaced; final subject to cluster A/B verdicts)

### A. Node imports

1. H3 lane (5 nodes): background/nodes/{f3_h3_double_accident_low_distance_
   joint_ideal_router, f3_h3_double_accident_nonzero_coupling_ideal_router,
   f3_h3_double_accident_coupling_batch_odd_saturation,
   f3_h3_double_accident_coupling_matrix_odd_saturation,
   f3_h3_disjoint_distance_six_split_pencil_router} verbatim; dag entries
   PROVED; edges: 5 ev -> f3_h3_mobius_excess_half + internal req wiring +
   req from master parents {f3_h3_cutoff18_double_accident_reduction,
   f3_h3_low_distance_ideal_star_router, f3_h3_shifted_product_sidon,
   f3_h3_low_distance_quotient_incidence_router,
   f3_h3_distance_six_support_overlap_payment} exactly as at pin.
   REPAIRS: (i) w14-C1 — do NOT adopt the pin attack_surface string;
   master field + dated WAVE-14 addendum; (ii) w14-C2 — mobius statement/
   attack/frontier/dependency_subdag pin additions land as ONE dated
   addendum block per file; claim_contract changes as dated addendum with
   master's route text preserved as prefix.
2. Hankel lane (9 nodes) — CLEARED BY SUB-AUDIT A (zero catches): the
   exceptional_only chain folders verbatim; 9 ev -> rate_half_band_closure;
   the internal req chain + req from master
   {..._active_partition_incidence_reconstruction,
   ..._middle_adjugate_factorization} exactly as at pin. Band
   statement/proof pin appends adopt as-is (already pure appends, dated).
   Optional at import (A-O1): harden substring marker asserts to
   anchored/exact-line form.
3. Antipodal lane (14 nodes): the 4+4+6 folders; 14 ev ->
   rate_half_list_adjacent_crossing; req from master parents
   {..._parity_reduction, ..._fourth_root_gap_reduction,
   ..._constant_coefficient_gate, ..._generic_canonical_span_criterion,
   ..._intermediate_hensel_certifier, ..._maximal_field_degree_collapse}.
   **POSE-CONTRACT PAIR RULE (KB #90, MANDATORY SAME-COMMIT)**: take the
   pin critical/nodes/rate_half_list_adjacent_crossing/{verify.py,
   statement.md} with the 14 nodes (statement appended onto master text
   per #104) — CLEARED BY SUB-AUDIT B: pin pair replays PASS, all 34
   physical deletion lines in the consumer md set classified benign
   (superseded guidance / resolved item restated stronger; zero
   retractions), the B*>=3 nonclaim survives verbatim. The attack/
   claim_contract/frontier/dependency_subdag pin bodies land as dated
   addenda onto master text (their deletions are in-place supersessions —
   preserve master originals as prefix per #104).
4. notes/PRIZE_COMPUTE_REQUESTS.md: import the pin additions INCLUDING the
   CR-002-L block in the SAME COMMIT as the Legendre-collapse node
   (w14-C3), with the standing maintainer annotation that "current sub-$1
   Modal policy" refers to the UNRATIFIED override (#260).
5. Roadmap: append the 28 increment paragraphs with the packaging-count
   annotation (branch counts include the refused discharge).
6. Manifest: merge +41 scripts / +56 assets + the 3 changed hashes (pose
   pair + f3_h3 statement.md); NOTE: if C1/C2 repairs alter imported file
   bytes, recompute those hashes rather than adopting the pin's.

### B. REFUSALS (carried forward, nothing NEW to refuse in-range)

1. packaging PROVED (inherited wave-13 w13-C1): keep master CONDITIONAL;
   strip the inherited dag status at import; count annotations per above.
2. The Modal budget-override roadmap paragraph: unchanged in-range;
   remains REFUSED-until-ratified (#260).

### C. Wave-15 watches

- 8f91ed84 ("Resolve the exceptional Hankel kernel plane") landed minutes
  post-pin — the exceptional chain continues; expect more band-lane nodes;
  the band has no pose contract of its own (wave-13 note), so watch
  whether one appears.
- The CR-002-L deferred batch: if a future commit LAUNCHES it (Modal or
  local), that is the trigger for the #260 governance test — the request
  text itself says it must not run under the current budget.
- w14-C3 class: watch for more node verifiers pinning notes/ files.

## PROCEDURAL LOG

- Pin taken at dce7460c; drift began within minutes (8f91ed84); all reads
  pinned; replays in w14_tree/ (git archive).
- Sub-audits A (hankel chain) and B (antipodal lane + pose contract)
  launched as parallel background agents under the same laws.
- Main-thread compute: all under ramguard tiny; one self-caught path slip
  (a grep ran against a nonexistent file with `|| echo 0` masking the
  error — corrected, and noted as a fail-open lesson; no conclusions were
  drawn from the bad output).
- Deliverables: w14_findings.md (this file), w14_dag_delta.py + output,
  w14_percommit_scan.py + output, w14_node_field_diff.py + output,
  w14_attack_surface_dump.py + texts, w14_manifest_sweep.py + output,
  w14_custody.txt, w14_tree/ (pinned), w14_mut/ (mutation copy),
  w14_checks.py (assembling).

---

# APPENDIX — SUB-AUDIT REPORTS (verbatim, as returned)

(Sub-audit A = core-one/Hankel exceptional chain; Sub-audit B =
deleted-pair/generic-Euler/intermediate/pose-contract. Reports below are
the agents' final messages, unedited.)

## SUB-AUDIT A — core-one/Hankel exceptional-resultant chain

VERDICT: SOUND / IMPORT-CLEAN. No catches. 4 observations. Replays 18/18
PASS. Mutation controls 5/5 TRIP. Compute-law slips: 2 (self-reported).

Q1 — Commit->node map confirmed 1:1 (deb03922=factor_descent ...
dce7460c=hankel_factor_pin), each commit touching only its node dir, band
appends, dag.json, notes, manifest — all pure insertions. Which system is
attacked: only the D_*=1 active-exceptional-trace system, and within it
only one stratum of the master-audited ACR6 classification: b=0, D_*=1,
c=z=1, X_1=1, epsilon_0=0 — one zero-trace bad row x_0 with no exceptional
incidence, no active domain traces, sole active factor = exceptional trace
E_a=E_Z ("exceptional-only"). D_*=0 untouched; z=0 stratum and c=2
(epsilon_0=1) profile untouched. #137: no new case split — selects an
already-enumerated master-audited stratum; parity facts (r=2e+1, D_0=8e+7
odd, n_X=8e+6 even, reversal sign -1) hold for every e. Non-coverage
stated explicitly everywhere.

Q2 — All load-bearing identities re-derived independently, all check:
EFD (q_0|P_X, J=(H-A(gamma_0))/p_0 exact degree D_0-r, gcd(E,Q)=1,
trace-free deg contradiction cannot be re-imported); EIR
leading-coefficient identities at X^{D_0}, X^{D_0+r-2}, X^{D_0+r-1},
v_inf correctly allowed to vanish; ERS exact ledger Tr-1=e*n_X
((4e+1)(2e+1)-1=e(8e+6)) closing both degree ledgers; EUR
Res_X(Q,B_1)=c_X*q_bar with exact exponent D_0-n_X=1, cross-check
Res(Q,W)Res(Q,B_1)=a^{m+D_0}; RRD formal-degree Sylvester lemma stack
machine-verified (w14_a_lemmas.py, ~1600 randomized exact trials incl.
degenerate leading/trailing coefficients, 0 failures); RRD5 coprimality
(f|q_bar and f|Delta_inf force f=E, refuted by Delta_inf != 0); RBN
literal Bezout certificate at X^{D_0-1}; FRC/FRS reversal identities
FU+P_cl*L=R_X, FRS3/FRS4 with converse and second-complement redundancy
verified, FRC4 double-checked by an independent route; HFP adj M=c_H E
q q^T via omission count O=1 at gamma_0, primitivity, top row/column via
q_r=E*q_bar. No division by possibly-zero quantities; exact-degree
claims valid under the declared biform convention.

Q3 — The chain closes NOTHING: 9-step exact reduction/normal-form chain
on one stratum. Residual at pin (chain's own words): "Classifying that
corrected square remains open"; "Classifying this corrected square and
the separate c=2 active profile remains open"; the classifier "still owes
the cofactor-product equations, triangular reconstruction, degree boxes,
and splitting". Untouched: c=2, z=0, all of D_*=0. Nothing reduces the
band budget set {2^39, 2^39+1} or closes any band residual; band TARGET
at pin; post-pin 8f91ed84 confirms the lane continued.

Q4 — Unconditionality clean: all external req parents PROVED on master;
base->pin delta = 9 nodes + 19 edges (1 parent-req + 8 chain-req + 1
MAF-req + 9 ev), no status changes, no removed edges, no new poses; zero
EXPERIMENTAL/pilot/Modal references; no refuted-predicate conditioning.

Q5 — Replays 18/18 PASS (9 verify + 9 verify_audit, pinned tree, ramguard
tiny); scripts read-only (json/pathlib/random only; no writes, network,
subprocess). Mutations 5/5 TRIP (ERS exponent corruption; req-parent
status flip; ev->note edge-kind flip; proof coefficient replacement
lambda=c_H E -> c_H q_bar; omission count O=1->0). Observation O1:
substring asserts do not trip suffix EXTENSIONS.

Q6 — Band statement.md/proof.md: single tail hunks, pure appends, zero
deletions, all 9 sections dated 2026-07-19, each ends with what remains
open. Manifest 18/18 entries present with matching sha256.

Observations: O1 substring-marker weakness; O2 verify scripts check
packet coherence/fixtures, math weight in prose (fully hand-traced); O3
HFP interface assertion rests on master-audited AIR8/AIR9 — make seam
explicit at formalization; O4 biform-convention degree claims.
Compute-law slips: one bare python3 heredoc dag read; one accidental
empty-stdin bare python3. No Modal; nothing deferred.

## SUB-AUDIT B — deleted-pair Legendre chain / generic Euler / intermediate / pose contract

Q1 — CENTRAL ANSWER: REDUCED (not CLOSED, not UNTOUCHED). The wave-13
residual (uniform rejection over every official p and lift ratio r of all
three pairing branches) is NOT delivered; the sublocus stays open. The
compression: legendre_collapse (7450bb6b) — CCG2 coefficient collapses to
sigma=2H_{4M-1}(t), H_n(t)=[z^n]((1-z)(1-tz))^{-1/2},
H_n(r^4)=r^{2n}P_n((r^2+r^{-2})/2). "Legendre" = LEGENDRE POLYNOMIALS, not
symbols. Re-derived by hand (reversal identities, ord C >= m+1,
sigma=4[z^a]BC=2[z^a]F^2), numeric confirmation at M=1,2,3 x three t.
Nonclaim explicit: does not prove uniform failure of (LCC6).
chebyshev_gegenbauer_sign_router (4d40b791) — exact reposing: primary gap
= C_L^{1/4}(x)=0 (Gegenbauer), torsion = T_{8L}(y)=epsilon,
tH^2=epsilon P_{2L-1}(x)^2, three squared gates split into six unsquared
linear-sign branches via epsilon(A-sB)(A+sB), s^2=-epsilon; verified by
hand + 376-cell forward+reconstruction sweep over F_97. trace_gcd_router
(812e4a0c) — eliminates the trace: branch nonempty iff gcd(C, G_eps mod C,
E_(j,s) mod C) != 1 (TGR7), degree <= L=2^36, trace reconstruction TGR6
with proved-nonzero denominators. torsion_necessity_fence (9a05c925) — a
strategy fence: three exact M=1 certificate rows (primary gap + one gate
hold but r^32 != 1) prove any uniform-rejection proof must retain
r^(32M)=1 in the rejection ideal; rows + Pocklington factor tree fully
replayed. EXACT RESIDUAL: for every official p = 1 mod 2^40 and each
torsion sign epsilon (eps=-1 iff ord(r)=2^40), prove the TGR7 gcd triples
trivial for all j in {0,1,2}, both s. Consumer verbatim: "Uniform proof
that these six gcds are one remains open." No per-p case analysis or
census smuggled — nothing is rejected yet.

Q2 — Soundness PASS (w14_b_spotcheck.py ALL PASS): Legendre collapse;
fence rows; Chebyshev/Pell/composition identities; Euler divisor gate
incl. the unstated-but-real deg T=1 cancellation re-derived (deg S=3r+1
exact because e_2 != 0); cubic norm gate Res(V,T)Res(V,U)^3=(-d)^v,
d=(2^13)^3, v = 2 mod 3, honest q = 2 mod 3 vacuity caveat; coupled gate
N_Q=N_U^4; character shard a genuine #137-complete split (e in {1,2} x
p mod 3, p != 3 since q >= 3*2^128) with honest ambient-vs-descended
fence. Character triviality: only cubic/quartic characters, orthogonal to
the 2-adic congruence; nothing silently assumes a nontrivial symbol.

Q3 — Intermediate lane: hensel gates quadratic/cubic/quartic — forbidden
coefficients of C_u=C_*V(q); universal series V=1-q/3+q^2/3-(35/81)q^3+
(154/243)q^4 re-derived exactly; degenerate branch <= 2 candidates;
honest that A=B=C=D=0 not proved empty. cube_part_router — exact
polynomiality classifier, careful multiplicity bookkeeping.
residual_square_gcd_gate (079f8a71) — GENUINE EXCLUSION: maximal
intermediate floor EMPTY (V^2|P, P'=U^2W, 4YDW=UA-3T^2, G|J=dA^3+27T^7
with multiplicities, lead(A) != 0 since p does not divide 4(3*2^37-1),
deg J=18 < v). low_band_exclusion (dee4bf3c) — band v in
[91,625,968,980, 96,207,267,428] (4,581,298,449 degrees) EMPTY (deg J=7t,
7t>3t+12 for t>=5, t=3 unreachable, v >= ceil((7r-14)/10)=96,207,267,429).
Exclusion titles earned; stratum NOT closed; official range NOT narrowed.

Q4 — Pose contract PASS: pin verify.py pins all 14 ids + PROVED + ev
edges + per-node statement phrases; replays PASS in pinned tree. 34
physical deletion lines all classified (attack 12, statement 7, frontier
8, claim_contract 3, dependency_subdag 3, verify 1): superseded guidance /
resolved-open-item restated stronger; ZERO retractions. Nonclaim survives
verbatim: "Budgets one and two are exact; the adjacent crossing remains
open for B*>=3." No refused text reintroduced.

Q5 — Unconditionality PASS: all 6 external req parents PROVED on master;
no planning-prose deps; no refuted-predicate conditioning; zero
Modal/app-id/result.json/experimental/pilot references in all 14 folders;
fence primality is a self-contained Pocklington replay.

Q6 — Replays 15/15 PASS (14 nodes + consumer); verify_audit.py 0/14
(w13-A3 asymmetry continues, lane-specific). Mutations 4/4 TRIP
(deg J=18->19; req-parent flip; consumer expected-phrase tamper; Legendre
condition sign flip). Copy deleted; repos untouched.

Catches: w14-B1 ("six" counts per torsion sign; complete problem = 12
triples); w14-B2 (ILB4 statement-level citation for a proof-level
generalization — re-derived TRUE, minor); w14-B3 (Hensel gates + cube
router vacuously scoped after 079f8a71 — dag redundancy, honestly
labeled); w14-B4 (Legendre-polynomials branding note).
Compute-law slips: two bare python3 heredocs (scratchpad JSON only),
self-caught. No Modal; nothing deferred.
