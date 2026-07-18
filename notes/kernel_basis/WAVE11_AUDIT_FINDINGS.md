# Wave-11 fresh-context replay audit — v5 low-budget list close + budget-three program

Auditor session 2026-07-18. Catch numbering LOCAL (w11-C#). READ-ONLY both repos.

## PINS

- **v5**: /home/u2470931/smooth-read-solomin/prize-codex-resolution-v5-20260718, branch
  codex/full-prize-resolution-v5-20260718. HEAD pinned at start = **b8366bca** ("Prove
  quadratic scrolls are full rank"). Scope d5a89194..b8366bca = **18 commits**:
  - **CODEX-ORIGINAL (13 non-merge)**, in first-parent order: 38147e72 (six-matrix
    reduction), ac338180 (all-arity low-budget close), 78efdeb0 (certificate generator),
    d729a4ee (split pencils), 3b178a95 (Plucker edge gate), 4d3af98c (split fibers),
    9ecd7a4b (path Mobius residual), then post-merge 67fa5f06 (path/cycle branches),
    d0cd50cf (split-member residues), e2ca2a30 (K4 chamber), 7d27349b (linear chambers),
    cdb54a9a (quadratic chambers), b8366bca (scroll full rank).
  - **MERGE (Codex-performed)**: 451a6e33 "Merge canonical wave-10 into resolution
    branch" (second parent = master HEAD f6f77b99).
  - **MASTER-AUTHORED (4, in-range via the merge)**: 6825aa85 (wave-10 audit banked),
    b57eb4fb (wave-10 imported), 0d3246e2 (orbit rebuild), f6f77b99 (wave-10
    re-pin 238/238).
- **master**: /home/u2470931/smooth-read-solomin/prize, HEAD f6f77b99 (= the merge's
  second parent; v5 merged master's exact current HEAD).
- **WORKTREE DIRTY AT AUDIT START (w11-C5)**: uncommitted mods to
  critical/nodes/rate_half_list_adjacent_crossing/{attack,claim_contract,
  dependency_subdag,frontier,statement,verify.py}, dag.json,
  notes/PRIZE_RESOLUTION_ROADMAP.md, plus UNTRACKED new node folder
  background/nodes/rate_half_list_budget_three_quadratic_scroll_primitive_module/.
  All content reads used `git show b8366bca:<path>`; the drift is WAVE-12 SCOPE
  (it continues the scroll program: "primitive module" = the next node).
- v4 retired: zero new commits (not re-checked beyond the task statement).

## VERDICT LINE

- CLUSTER 1 (low-budget close, ac338180 + 78efdeb0 + the wave-10 base):
  **IMPORT-CLEAN. The budget set is NOT extended (still B* in {1,2}); the ARITY set is:
  the {1,2} crossing a_L = 3n/4 is now DETERMINED FOR EVERY common-support interleaving
  arity m >= 1 — an unconditional theorem (rate_half_list_low_budget_all_arity_crossing,
  PROVED) resting only on master-PROVED rate_half_list_low_budget_exact_crossing +
  list_subsqrt_interleaving_collapse. B* in {1,2} (i.e. every official field
  2^128 < q < 3*2^128) is now a COMPLETE list-prize determination (LIST and
  INTERLEAVED_LIST objects), not an ordinary-list partial.** The certificate generator
  (78efdeb0) is an artifact-semantics PROVED node + fail-closed tool
  (tools/rate_half_list_low_budget_certificate.py); refusal behavior machine-checked
  (8/8 refusals + tamper trip). Hand-traces sound; replays PASS; constants reproduced.
- CLUSTER 2 (budget-three program, 38147e72 + d729a4ee + 3b178a95 + 4d3af98c + 9ecd7a4b
  + 67fa5f06 + d0cd50cf + e2ca2a30 + 7d27349b + cdb54a9a + b8366bca):
  **IMPORT-CLEAN — and the decisive answer is: BUDGET 3 IS NOT DETERMINED AT PIN, and
  the program does not claim it is. What is now PROVED is the complete BOUNDED
  EDGE-GEOMETRY CLASSIFICATION of any hypothetical 4-codeword witness at the Johnson
  predecessor 3n/4-1: every such witness lies in one of exactly THIRTEEN edge-degree
  chambers — NINE nondegenerate base-field split-unit Grassmann-line chambers
  (exceptional degrees {3,4,5,6,8}) and FOUR full-rank balanced Grassmann scrolls (the
  rank-deficient scroll branch is EMPTY, b8366bca). The fourth-member residue question
  is closed (all 13 printed pencils exact-three at d=2^39; cycle exact-two). Remaining
  open for B*=3: official-subgroup arithmetic in all 13 chambers (exclude the normal
  forms or construct one and consume its list) — and even a full close of all 13 only
  proves L_1(3n/4-1) <= 3, i.e. moves the SAFE point down by exactly ONE agreement
  step; the B*=3 crossing bracket stays [k+2^34, 3n/4] (gap ~ 2^39). Zero new TARGET or
  CONJECTURE poses minted. All 12 nodes PROVED with honest reduction-not-exclusion
  scope lines; two exact F_17 witnesses (rank-11 order-8 fence; rank-23 d=4 full-domain
  path witness) block pairwise-MDS-only and member-count-only routes.**
- CLUSTER 3 (effect on master's objects): **rate_half_list_adjacent_crossing stays
  TARGET; its pose is NOT narrowed — the binding open content remains exactly (RHL-ADJ)
  for B*>=3, with the proved preamble strictly grown (arc CLEAN, zero claim
  walk-backs). list_adjacency_closing/list_safe/list_grand: UNTOUCHED by wave-11
  commits (all divergences vs master are persisting wave-10 residue). The band node:
  untouched by wave-11 commits; its QUALITY.md carries a REPEAT in-place edit from the
  merge resolution (w11-C1). Both wave-10 status refusals HOLD at pin (packaging
  CONDITIONAL, descriptor TARGET; the merge ADOPTED master's refusals): zero status
  diffs on all 717 shared nodes.**

## THE MERGE (451a6e33) — resolution quality

The merge adopted master's wave-10 import as canon: all 23 master-imported nodes
(safe-side 6, Hankel 12, XR 5) enter v5; packaging/descriptor statuses resolve TO
MASTER (the two apparent "flips" in the net range delta are exactly the refusal
adoption — the packaging/list_safe watch is SATISFIED); the big dag statement fields
(band 8819, list_safe 132, packaging 115, harness, dossier_partial, f3_h3 red 2344)
resolve to master. Residue (all wave-10-era, none created by wave-11 commits):

| item | pin vs master | class |
|---|---|---|
| descriptor -> packaging [req] | PIN-ONLY | w10-C1 refused edge persists (hardens the amber, no discharge risk; master must NOT adopt) — w11-C3 |
| m_handling -> list_safe, m_sweep -> list_safe | duplicate req AND ev copies at pin | merge produced both kinds — dag hygiene defect, w11-C2 |
| list_adjacency_closing -> list_grand | req on master, ev at pin | w10-C6 choice persisting — master's req stands unless maintainer accepts |
| mca_quadratic_prize_rows -> rate_half_band_closure [ev] | PIN-ONLY | benign ev wiring (v5 24a56ac8); surface, optional |
| rate_half_cyclic_rotated_prefix_floor dag stmt | 657 -> 494 | merge kept v5's shrunk field; master canonical |
| ~40 master-node FILES (packaging, band_closure, list_safe, floors, f3_h3 red, compiler/harness/dossier, ...) | v5 wave-10 in-place rewrites persist at file level | w10-C4 set unreconciled in v5's tree — will re-surface at every merge (w11-C4) |

## DAG-STATUS-DELTA TABLE — Codex-original commits (per-commit; w11_dag_delta.py,
full output w11_dag_delta_output.txt)

Net d5a89194 -> b8366bca: 694 -> 731 nodes (+14 Codex-original, +23 via master merge);
1305 -> 1402 edges; **0 removed; NET STATUS FLIPS IN CODEX-ORIGINAL COMMITS: ZERO**
(the 2 net flips descriptor PROVED->TARGET, packaging PROVED->CONDITIONAL occur AT THE
MERGE and equal master's refused state — refusals adopted, not violated).

| commit | dag delta (all new nodes PROVED) |
|---|---|
| 38147e72 | NEW rate_half_list_budget_three_intersection_reduction; ev -> adjacent_crossing |
| ac338180 | NEW rate_half_list_low_budget_all_arity_crossing; req <- {low_budget_exact_crossing, list_subsqrt_interleaving_collapse}; ev -> {list_grand, list_large_m_scope_closure} |
| 78efdeb0 | NEW rate_half_list_low_budget_certificate_generator; req <- {compiler, descriptor(->demoted to ev at merge), all_arity, exact_crossing}; ev -> list_grand |
| d729a4ee | NEW ..._split_pencil_normal_form; req <- intersection_reduction |
| 3b178a95 | NEW ..._plucker_edge_gate; req <- split_pencil_normal_form |
| 4d3af98c | NEW ..._split_fiber_atlas; req <- split_pencil_normal_form |
| 9ecd7a4b | NEW ..._path_mobius_transversal; req <- split_fiber_atlas |
| 451a6e33 | MERGE (see above; also demotes descriptor->cert_generator req->ev) |
| 67fa5f06 | NEW ..._cycle_bimobius_transversal (req <- plucker, fiber_atlas) + NEW ..._path_power_two_witness |
| d0cd50cf | NEW ..._residual_transversal_atlas (req <- path_mobius, plucker, fiber_atlas) |
| e2ca2a30 | NEW ..._k4_grassmann_line (req <- plucker, residual_atlas) |
| 7d27349b | NEW ..._linear_grassmann_atlas (req <- k4_line, fiber_atlas) |
| cdb54a9a | NEW ..._quadratic_scroll_atlas (req <- linear_atlas, plucker) |
| b8366bca | NEW ..._quadratic_scroll_full_rank (req <- scroll_atlas) |

All 14 wire ev into rate_half_list_adjacent_crossing (the two Cluster-1 nodes also/
instead into list_grand + list_large_m_scope_closure). Statement-field growth on
adjacent_crossing per commit (449 -> 577 net) = pose preamble growth, arc-monotone.

**NODE-ID COLLISION CHECK (w10-C8 precedent): CLEAN — none of the 14 new ids exist on
master (machine-checked).** The untracked working-tree node id
(rate_half_list_budget_three_quadratic_scroll_primitive_module) also has no master
collision today; re-check at wave-12 pin.

## CLUSTER 1 — DETAIL

1. **rate_half_list_low_budget_all_arity_crossing (ac338180) — HAND-TRACED SOUND.**
   (LA12): L_m(3n/4) <= B* < L_m(3n/4-1) for every arity m>=1, B* in {1,2}. Safe side:
   L_1(3n/4) <= B* <= 2 (master's wave-10 theorem) => L_1^2 <= 4 < q; master's
   collapse theorem (checked at source: 1<=L<q => L <= L_m <= floor(L(q-1)/(q-L)); the
   floor equals L exactly when L^2 < q — I verified the cap arithmetic exhaustively for
   L<50, q<200, two-sided) gives L_m = L_1; L_1=0 edge case handled separately
   (component-wise). Unsafe side: diagonal tuples (c,...,c) against the repeated
   received word preserve the B*+1 explicit predecessor witnesses. No inference to
   B*=3 "merely because its Johnson anchor has the same value" — the trigger/scope
   hygiene sentence is present and correct.
2. **rate_half_list_low_budget_certificate_generator (78efdeb0)** — deterministic
   fail-closed artifact node. verify_audit: positive=4, refusals=8/8, tampering=1/1.
   Depends on master's compiler (PROVED) via req and descriptor via ev (post-merge; the
   pre-merge req was demoted AT the merge, consistent with master's descriptor-as-
   ev-of-consumers doctrine — keep ev on import). Minor note w11-C6.
3. Constants: safe 3n/4 = 1,649,267,441,664; radius n/4 = 549,755,813,888 = 2^39;
   window B* in {1,2} <=> 2^128 < q < 3*2^128 — all independently reproduced.

## CLUSTER 2 — DETAIL

### Hand-traces (full re-derivations, own algebra)

- **Six-matrix reduction (38147e72), the foundation — SOUND.** Re-derived: incidence
  identities (1)-(2) => (3)-(4) => (5) => n_0=0 and the six raw patterns; the
  (0,2,0,0) exclusion (T = 4d-2 forced vs T >= 4d-1 from a zero-singleton pair); the
  d-free labeled feasibility condition p_ij <= s_i+s_j+p_i+p_j+1-(n_1+n_2); the
  matrix construction (spanning-tree rows, 8d-4 rows x 6d cols, kernel <-> witness
  equivalence both directions). INDEPENDENT EXHAUSTIVE ENUMERATION (my own code)
  reproduces EXACTLY six labeled types with the stated shapes.
- **Split-pencil normal form (d729a4ee) — SOUND.** Re-derived (SP1) (locator of
  S_i cap S_j = J A_k A_l e_ij), (SP2) via the cocycle g_ij+g_jk=g_ik and J A_l
  cancellation, (SP3)-(SP4) (multiplicity bookkeeping exact), and EVERY ROW of the
  constant-degree ledger (t-d, delta, deg b) for all six types — exactly three
  quadratic slots (pendant 13,23; K_4-e 23).
- **Plucker gate (3b178a95) — SOUND.** (PG1) re-derived from the three triangle
  identities; all six minors checked (the 34-minor uses PG1); (PG2) coordinatewise;
  (PG3) N_2=A_2 b_01, N_3=A_3 b_01 and the partition identity; deg R ledger
  (4,4,6,8,3,5) recomputed.
- **Split-fiber atlas (4d3af98c) — SOUND.** (SF1) dichotomy: delta=0 forces deg
  g_ij = 2d-1 hence c_i != c_j and exact edge degree; delta=1 resolves by leading-
  coefficient cancellation. Pendant both-linear exclusion: c_1=c_3 & c_2=c_3 =>
  c_1=c_2 contradicts delta_12=0. (SF3) cap floor(4d/h) from disjoint root sets.
- **Path/cycle/residual transversals (9ecd7a4b, 67fa5f06, d0cd50cf) — SOUND
  (normal depth).** Fibers from the triangle identities (at x in T_k the k-locator
  vanishes and the identity becomes the Mobius/graph formula); injectivity of
  c(X-a)/(X-b); root caps r+|E| via the elementary pencil observation; per-branch
  |E| bookkeeping checked (K_4-e 2+4=6 @ d>=8; K_4 2+5=7 @ d>=9; triangle 1+4=5 and
  1+2=3; pendant 2+3=5 with the e_13-root nonconstancy argument; path <= 2 resp. <= 4);
  the 13-pencil accounting 1+0+2+4+2+4 matches the atlas triangle table; all
  thresholds << 2^39. The d0cd50cf "Close" title is backed: it closes the
  fourth-member RESIDUE question, crossing explicitly disclaimed.
- **K4 line + linear atlas (e2ca2a30, 7d27349b) — SOUND (normal depth).** B wedge B = 0
  <=> PG1; line form w wedge (u+Xv); the constant annihilator of <w,u,v> gives the
  four-term split-unit relation; support/no-subsum from pairwise-coprime monic split
  locators. Nine-chamber census independently reproduced.
- **Scroll atlas + FULL RANK (cdb54a9a, b8366bca), the finish — SOUND.** Balanced
  basis h=(q/ell)X trick checked (the only quadratic slot rebalanced; the other
  coordinate stays affine-linear because b_02 is constant in pendant chambers);
  U_1 wedge V_1 != 0 from the exact-quadratic edge; det C = c^2(e_1 d_1 - a_1 f_1)
  RE-COMPUTED BY COFACTOR EXPANSION and verified by exact identity testing (60
  random Fraction points), including the K_4-e branch det C = -b_01^3 [X^2]b_23 with
  c [X^2]b_23 = L_02 L_13 - L_03 L_12 from PG1. Pendant: L_02=0, L_12 L_03 != 0
  (exact linear edges). Hence rank C = 4 always: the rank-deficient scroll branch is
  EMPTY and (QFR4) C^{-1}A = (alpha, X alpha, beta, X beta)^T holds in all four
  quadratic chambers.

### The #137-style completeness question — ANSWERED POSITIVELY

Chamber coverage is NOT merely asserted: (i) the six-type census is machine-
enumerated in the node verifier (raw compositions + canonical orbits) AND
independently re-enumerated by this audit (identical result); (ii) the 13-chamber
census follows from the per-type delta vectors by the (SF1) dichotomy — machine-
checked in the atlas verifier and independently re-derived here via leading-
coefficient class enumeration (3+4+2+1+2+1, pendant both-linear excluded); (iii) the
9/4 linear/quadratic partition is recomputed from the same census. The chambers are
NECESSARY conditions (rows "do not assert that every chamber is realized") — coverage
is of witness-space, which is the direction the safe-side program needs.

### Witness/fence checks (all my own code)

- Order-8 fence RS[F_17,mu_8,4]: subgroup verified, agreements 4x5, incidence
  (0,1,2,0) with n_3=5, matrix 12x12 rank 11 — REPRODUCED.
- d=4 path witness RS[F_17,F_17^*,8]: agreements 4x11, all printed blocks, 28x24
  matrix rank 23, ALL SIX normal-form quotients (q_01..q_23)=(8,4,1,13,10,15+14X)
  reproduced by my own polynomial division, PG1 AND PG3 verified on the witness data,
  first-pencil fully-split member count = exactly 3 — REPRODUCED.
- The order-16 proper-subgroup search (F_97, 3,830,400 assignments, 0 witnesses) is a
  notes-level negative exploration; result.md properly disclaims ("does not promote a
  claim"). Not load-bearing — and it IS deterministically replayed by the node's
  verify_audit.py (proper_F97_assignments=3830400 witnesses=0 on replay).

### Verifier replays (ramguard tiny, pinned mini-tree w11_tree/)

**29/29 PASS**: 14 node verify.py + 14 verify_audit.py + the TARGET node's verify.py
(honest nonclaim "Budgets one and two are exact; the adjacent crossing remains open
for B*>=3" printed at pin). External mutation controls TRIP 3/3 (req->ev edge
demotion, parent status flip, corrupted witness codeword — all AssertionError).
Independent checks: **w11_checks.py 41/41 PASS.**

### Arc check: CLEAN

Zero status flips in Codex-original commits; every statement/frontier deletion
in-range is the "next step" guidance paragraph superseded by the sharper
post-progress version (e.g. b8366bca replaces the two-branch rank dichotomy with
"the rank-deficient branch is empty" — a strengthening). No claim weakened, no
refuted predicate conditioned on, no conjectural input anywhere in the chain: every
req parent of the 14 nodes is master-PROVED or in-chain. Roadmap/ledger entries
honest ("strict reduction, not an exclusion ... or a safe-side proof"); dag counts
(731/1402/563 PROVED) match forensics.

## CLUSTER 3 — MASTER-OBJECT EFFECTS

- **rate_half_list_adjacent_crossing (TARGET, master-shared)**: determined set
  extends ARITY-wise ({1,2} now complete list-prize determinations); pose unchanged
  in binding content (B*>=3); the B*=3 residual is now sharply the 13-chamber
  subgroup arithmetic. v5's in-place file evolution (statement 449->577 + frontier/
  attack/claim_contract/verify growth over 13 commits) lands on master as ONE dated
  addendum (w10-C4 pattern), master text preserved.
- **list_adjacency_closing / list_grand / list_large_m_scope_closure**: no wave-11
  touches; the all-arity node partially DELIVERS list_large_m_scope_closure's
  transport content for B* in {1,2} unconditionally (ev-wired, no flip attempted —
  correct). Master's conditional texts can cite the new node in a dated addendum.
- **rate_half_band_closure**: untouched by wave-11 commits; QUALITY merge defect
  w11-C1 (below).
- Custody of every master-shared file v5 touched post-merge: ONLY
  rate_half_list_adjacent_crossing/* (in-place, addenda on import), dag.json,
  roadmap/ledger/manifest/replay-json (append-style), and
  rate_half_list_low_budget_exact_crossing/{statement.md,dependency_subdag.md}
  (ac338180, near-append consumer/child update — import as dated addendum).

## CATCHES

- **w11-C1 (custody, REPEAT violation, from the merge resolution)**:
  critical/nodes/rate_half_band_closure/QUALITY.md gate-3 constant line re-edited IN
  PLACE (8,594,128,895 -> 17,179,869,183=2^34-1) — the exact line master restored at
  wave-10, while the in-file w10-C7 note ("log blocks are append-only — the original
  line stands above") still sits below it. The pin file is self-contradictory. The two
  new dated blocks (QUADRATIC LOW-FIELD SLICE, OPTIMIZED CYCLIC FLOOR) are proper
  appends. Repair: master's file canonical; never propagate the line edit; flag the
  pattern to Codex.
- **w11-C2 (dag hygiene)**: duplicate-kind edges at pin — m_handling->list_safe and
  m_sweep->list_safe exist as BOTH req (master's) and ev (v5's a47b87c0) copies.
  Merge artifact. Do not import; Codex should deduplicate.
- **w11-C3 (refused-edge persistence)**: descriptor->packaging [req] retained through
  the merge despite master's recorded ev-of-consumers demotion (w10-C1 mechanism).
  With descriptor TARGET it now HARDENS packaging's amber (no discharge risk), but
  master must not adopt it; Codex should drop it at next reconciliation.
- **w11-C4 (merge residue, informational)**: the w10-C4 in-place-rewrite set (~40
  master node files: packaging, band_closure, list_safe, list_adjacency_closing,
  list_grand, both floors, f3_h3_mobius_excess_half, compiler/harness/dossier_partial,
  mca_quadratic_prize_rows, ...) persists at FILE level in v5's tree even though dag
  fields were resolved to master. No new wave-11 violations, but the divergence
  re-surfaces at every merge; recommend a one-time v5-side reconciliation to master's
  post-import files.
- **w11-C5 (procedural)**: v5 worktree dirty at audit start (post-pin drift incl. the
  untracked quadratic_scroll_primitive_module node) — excluded from scope; wave-12
  re-pins.
- **w11-C6 (minor)**: certificate_generator is a PROVED artifact-semantics node whose
  verifier imports tools/prize_row_descriptor.py (master carries the tool as content
  while descriptor stays TARGET) — coherent under master doctrine ONLY with the
  descriptor edge as ev (which is the pin state post-merge). Keep ev on import.

## IMPORT SURGERY SPEC (exact; all content at pin b8366bca; statements MERGED never
replaced; master deps verified PROVED: rate_half_list_low_budget_exact_crossing,
list_subsqrt_interleaving_collapse, compiler, rate_half_list_integer_johnson_safe_anchor)

### A. Cluster 1 (low-budget all-arity + certificates)

1. NEW NODE FOLDERS verbatim: background/nodes/rate_half_list_low_budget_all_arity_
   crossing/ (8 files), background/nodes/rate_half_list_low_budget_certificate_
   generator/ (9 files); tools/rate_half_list_low_budget_certificate.py.
2. Dag: 2 PROVED entries + edges {low_budget_exact_crossing -> all_arity req;
   list_subsqrt_interleaving_collapse -> all_arity req; all_arity -> list_grand ev;
   all_arity -> list_large_m_scope_closure ev; all_arity -> cert_generator req;
   low_budget_exact_crossing -> cert_generator req; compiler -> cert_generator req;
   descriptor -> cert_generator **ev** (per w11-C6); cert_generator -> list_grand ev}.
3. rate_half_list_low_budget_exact_crossing (master node): dated addendum = the
   ac338180 consumer-line + dependency_subdag deltas.
4. list_large_m_scope_closure + list_grand conditionals: one dated addendum each
   noting the B* in {1,2} branches are now UNCONDITIONALLY delivered at every arity by
   the new node (no status change).
5. Manifest entries (2 verify.py + 2 verify_audit.py + the tool); merge the
   incremental_verifier_replay.json delta rows.

### B. Cluster 2 (budget-three program, 12 nodes)

1. NEW NODE FOLDERS verbatim: background/nodes/rate_half_list_budget_three_{
   intersection_reduction, split_pencil_normal_form, plucker_edge_gate,
   split_fiber_atlas, path_mobius_transversal, cycle_bimobius_transversal,
   path_power_two_witness (incl. notes/search_order16_proper.py + result json),
   residual_transversal_atlas, k4_grassmann_line, linear_grassmann_atlas,
   quadratic_scroll_atlas, quadratic_scroll_full_rank}/.
2. Dag: 12 PROVED entries; 12 ev edges into rate_half_list_adjacent_crossing; req
   chain exactly as in the per-commit table above (14 internal req edges).
3. rate_half_list_adjacent_crossing (master critical node): ONE dated addendum
   "BUDGET-THREE BOUNDED EDGE GEOMETRY (wave-11 audited)" carrying the pin
   statement.md/frontier.md/attack.md/claim_contract.md/dependency_subdag.md bodies
   merged onto master's imported text (superseded guidance paragraphs marked, not
   deleted); verify.py updated to the pin version (its checks grew monotonically);
   dag statement field: append pin text per house convention.
4. Import note (mirror of w10-H5): the 12 nodes classify the HYPOTHETICAL witness at
   the Johnson predecessor; they do NOT move the proved bracket [k+2^34, 3n/4] for
   B*=3, and a full 13-chamber close would move the safe endpoint by exactly one step.
5. Manifest entries for 12 verify.py + 12 verify_audit.py.

### C. Refusals / non-imports

- Do NOT adopt: descriptor->packaging req (w11-C3); the m_handling/m_sweep ev
  duplicates (w11-C2); the list_adjacency_closing->list_grand req->ev demotion
  (master's req stands; w10-C6 decision unchanged); the QUALITY.md gate-3 line edit
  (w11-C1); the cyclic-floor dag-statement shrink (master's 657-char field stands);
  any file from the w11-C4 merge-residue set.
- OPTIONAL surface: mca_quadratic_prize_rows -> rate_half_band_closure ev edge.

### D. Wave-12 watches

- The post-pin drift: quadratic_scroll_primitive_module (untracked) + uncommitted
  adjacent_crossing edits — the scroll-module subgroup arithmetic is the live lane.
- Watch for: any claim that closing chambers moves the B*=3 bracket by more than one
  step; any "exclusion" language on the nine split-unit or four scroll chambers
  without official-subgroup arithmetic; a premature adjacent_crossing flip (needs
  BOTH a new safe point AND a matching predecessor witness — currently unavailable
  for any B*>=3).

## PROCEDURAL LOG

- One compute-law slip early: a bare `python3 -c` JSON parse inside a pipe (manifest
  shape probe) — flagged, no incident; all subsequent Python under tools/ramguard
  tiny from the scratchpad. No Modal needed (all replays fit tiny).
- At audit close the v5 HEAD had MOVED to 98305002 (2 post-pin commits: 74e700e6
  "Refine quadratic scrolls to primitive modules" — the formerly-untracked
  primitive-module node committed — and 98305002 "Reduce maximal budget-three
  fields"; worktree now clean). NO contamination (all content reads used
  `git show b8366bca:`). Post-pin range b8366bca..98305002+ is WAVE-12 SCOPE;
  expectation: scroll-module subgroup arithmetic + a field-cap reduction on B*=3 —
  watch the w11-D wave-12 items above.
- Deliverables beside this file: w11_checks.py (41/41 PASS — own-code six-type
  enumeration, both F_17 witnesses incl. all six quotients + PG1/PG3 on live data +
  exact-3 pencil count, 13-chamber census, scroll determinant identity testing,
  collapse arithmetic, dag hygiene/collision checks), w11_dag_delta.py +
  w11_dag_delta_output.txt + w11_dags/ (16 per-commit dag dumps), w11_dagcmp.py
  (pin-vs-master shared-subgraph comparison), w11_mutate.py + w11_mut/ (mutation
  trips 3/3), w11_tree/ (pinned replay mini-tree; 29/29 verifier replays),
  w11_shared_modified.txt (custody surface).
