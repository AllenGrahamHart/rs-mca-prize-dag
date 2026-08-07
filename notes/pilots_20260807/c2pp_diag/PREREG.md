# PRE-REGISTRATION — MYSTERY 3 DIAGNOSIS: C1'/C2'' (round 23)

Round 23, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: mystery 3 (the
C1/C2'' cancellation structure on the dli lane) is the STALEST board
item — C2'' was posed but never attacked, and this mystery never got
the full diagnosis pipeline that well-posed mysteries 5 and 6 in
round 21. Run it: consumer contract, obstruction made exact,
mandatory adversarial attack on C2'', cross-lane matrix, weakest
re-pose.

## 0. Sources (quote verbatim first — the history is long; the
statements of record are in the nodes, the campaign history in the
pilot dirs)
- critical/nodes/dli (or the dli-successor node carrying the
  B-WEAK floor re-pose — locate by grep; quote the current
  statement + status + the F-round refutation record: both frozen
  conditions refuted, dli back red).
- The C1' calibration + the C2'' pose: notes dirs from the
  self-tennis and F-round campaigns (notes/pilots_2026* — grep for
  C2'' / C1' / SELF_TENNIS / dli tennis; also the kernel-basis
  program's honest-refusal record for dli).
- The floor-campaign B-WEAK re-pose (joint endpoint budget,
  pre-registered falsifier) — quote it; check whether its
  falsifier was ever run.
- Consumers: which critical nodes require the dli-lane result
  (dag edges) — quantify what they need.

## 1. Deliverables
- (D1) THE STATE RECONSTRUCTION, honest and compressed: what
  C1/C2 claimed, why the F-round killed the amber (the exact two
  refuted conditions with file:line), what C1' salvages, what
  C2'' poses. One page, no archaeology beyond what changes
  decisions.
- (D2) THE CONSUMER CONTRACT: what the chain actually needs from
  this mystery, quantified (the weakest sufficient form). Has the
  need CHANGED since the F-round (wave 47/48 re-wirings)? Check
  the current dag edges, not memory.
- (D3) C2'' MADE EXACT + THE MANDATORY ADVERSARIAL ATTACK: state
  C2'' precisely; then attack it at toy scale with a registered
  escape test BEFORE any positive work — the F-round pattern
  (frozen conditions refuted by construction) is the prior: expect
  refutation and design the attack to find it. If C2'' survives a
  genuine attack, say exactly what the attack could and could not
  reach.
- (D4) CROSS-LANE MATRIX (applies/fails-because per cell): the
  ternary suppression instruments, the constant-weight/prescribed-
  sum machinery (U2), Z-2 moments, the WCL slot certificates —
  does anything banked since the F-round change the mystery's
  standing?
- (D5) THE RE-POSE OF RECORD (floor-campaign style): the weakest
  form with a pre-registered falsifier, or an honest report that
  the mystery is correctly posed as-is and what its next decisive
  test costs.

## 2. Falsifiers / honesty
- If the adversarial attack refutes C2'': that is the expected
  productive outcome — report the witness with a reproduction
  script; the coordinator re-poses.
- Census evidence is evidence, never proof; label throughout.
  Respect the node's calibration clauses (no toy-to-official
  inference without a stated transport).

## 3. Rules
- DRAFT ONLY in notes/pilots_20260807/c2pp_diag/. Never edit
  dag.json/nodes/tools; no git; no Modal. COMPUTE LAW: every
  python3 invocation via tools/ramguard tiny|local -- python3 ...
  (literal --), from repo root, INCLUDING file patching and JSON
  peeking. 2-power toy grids (CATCH-Z6); no shift-0 cells
  (CATCH-19B); name every measured functional (CATCH-19C).
  Verbatim quotes with file:line. No REPORT.md — your final
  message IS the report. QUARANTINE: do not read
  notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line 2786
  (the "ROUND 23 LAUNCHED" marker); do not read the other
  round-23 pilot dirs (cw_shared_target, fpc5_diag,
  ge_lattice_cert); PASS THIS QUARANTINE CLAUSE VERBATIM to any
  subagent you dispatch.

# PILOT REGISTRATIONS

Appended 2026-08-07 by the c2pp_diag pilot BEFORE any computation.
Everything below is fixed in advance: hypotheses, the C2'' adversarial
escape test, toy-cell declarations, numeric predictions. House Law #1.

## P0. CORRECTION TO THE BRIEF'S PREMISE (registered before computing)

The brief says C2'' "was posed but never attacked". That is FALSE on
the record. C2'' (`dli_c2pp_joint_reserve`) has survived TWO
pre-registered adversarial rounds:

- Round 1 = M1, 2026-07-13 (Modal sharded n=64 tower census).
- Round 2 = c2r2, 2026-07-13/14, packet banked at
  `critical/nodes/dli_c2pp_joint_reserve/notes/c2r2_fround2_20260713/`.

`critical/nodes/dli_prime_weighted_large_block_support/conditional.md:8-10`
states verbatim: "**(P1) C2''** — the 21-bit joint reserve at the posed
/33 junction convention (`dli_c2pp_joint_reserve`; pose
`notes/C2PP_POSED_20260710.md`; F-round state 2: rounds M1 + the
2026-07-13/14 round both survived)."

What the brief is remembering is a DIFFERENT event: the 2026-07-07
F-round that refuted the two FROZEN conditions C1 and C2 (the
predecessors), recorded at
`critical/nodes/dli_prime_weighted_large_block_support/notes/F_ROUND_CONJECTURE_FALSIFICATION.md:106-110`.
C1' and C2'' are the successors of that kill. My round is therefore
F-ROUND 3 on C2'', and it must NOT replay F-a/F-b/F-c — a third
replay of a twice-survived falsifier battery is not an attack. I
register a NEW falsifier family below (F-d) aimed at the part of the
claim the first two rounds structurally could not reach.

## P1. HYPOTHESES (registered)

**H1 (STATEMENT GAP).** The node's statement of record is strictly
stronger than the clause the two F-rounds defended, and the dag wires
the stronger one.

- Node headline (`critical/nodes/dli_c2pp_joint_reserve/statement.md:9-19`,
  and `node.json:8`): `A(R) = product_j E_U[rho_j]`,
  `X(R) = q^(-t+H) W_cen(R)`, claim `X(R) <= 2^21 A(R)`.
- Pose clause (ii)
  (`critical/nodes/dli_prime_weighted_large_block_support/notes/C2PP_POSED_20260710.md:35-36`):
  `E_U[ prod_j rho_j ]_reduced  <=  2^R_joint * prod_j E_U[ rho_j ]`,
  with `_reduced` = AFTER clause (i) coset routing and clause (iii)
  accident pricing.

These coincide only if the clause-(i) reduction is multiplicatively
neutral. H1 asserts it is not, and names the gap functional
`coset_leakage` (P2 below). Under the packet's own transport
(`m4_assembly_verifier.py::gate_calibration`, cited at
`.../c2r2_fround2_20260713/c2r2_falsifiers.md:34-40`: one junction
ratio `x` stacked over 33 junctions, charge `x**33`, overflow iff
`x > 2^(21/33) = 1.554406...`), the headline is EXACTLY
`prod_j raw_ratio_j <= 2^21`.

**H2 (CLAUSE-(ii) VACUITY AT THE HIGH-LOSS ROWS).** The object that
clause (ii) bounds — `bulk_ratio` — is identically 0 precisely at the
rows where the joint loss is large, so both survived rounds scored
margin on cells where the phenomenon is absent.

Evidence prompting H2 (banked, quoted, not yet re-measured by me):
- `.../notes/F_ROUND_CONJECTURE_FALSIFICATION.md:87-88`: raw ratio
  **4.25** at (t=2, q=8353) and **8.40** at (t=2, q=32801).
- `.../notes/C2PP_POSED_20260710.md:73-78`: "the bulk object it
  constrains measures 0.998 / 1.010 / 0 / 0 / 1.033 / 1.066 / 0.760 /
  0 at the 8 exact rows ... At the four sparse rows the stripped
  conditional mass is IDENTICALLY ZERO".
  Row order is `CAL_ROWS` at
  `.../c2r2_fround2_20260713/c2r2_local.py:27-29` =
  [(2,97),(2,193),(2,8353),(2,32801),(3,97),(3,193),(4,97),(4,193)],
  so the two zeros at indices 2,3 sit exactly on the 4.25 and 8.40
  rows.
- `.../c2r2_fround2_20260713/c2r2_local.py:93`:
  `bulk_rows = [(b, lab, t, q) for (...) in search if b > 0]` — the
  F-b scoring set DROPS every row with `bulk_ratio == 0`, i.e. drops
  the two high-loss rows by construction. H2 predicts F-b's banked
  `x_max = 1.0662` therefore comes from a low-loss row.

**H3 (COSET GROWTH UNCHARGED).** The raw per-junction factor grows
with q and the growth is carried by the k=0 coset column
(`.../F_ROUND_CONJECTURE_FALSIFICATION.md:92-95`: "Geometric mean 2.14
> the 1.57/junction budget; the ratio GROWS with q. ... the
correlation is carried by (a) the k=0 COSET class — null states
over-weight it"). F-a's kill rule reads only the coset-STRIPPED,
accident-priced `bulk_ratio`
(`.../c2r2_falsifiers.md:49-60`), so no F-round has ever scored the
coset column's own q-trend. H3 asserts that trend is real and
unbounded in the toy grid.

## P2. NAMED FUNCTIONALS (CATCH-19C)

All computed by the banked M1 kernel
`critical/nodes/dli_prime_weighted_large_block_support/notes/m1_dli_m1_tower_census_modal.py::decompose_row`
(lines 550-607), read-only, exact integer censuses.

Reused verbatim from that kernel (names unchanged):
1. `raw_ratio`     := `ratio` = E[sc|null]/E[sc] (k=0 included both
   sides). This IS the per-junction factor of X(R)/A(R).
2. `stripped_mean_ratio` (r1) := k=0 removed from BOTH sides.
3. `stripped_mass_ratio` (r2).
4. `bulk_ratio` := k=0 AND accident classes removed from both sides.

NEW functionals introduced by this pilot (named here, first use):
5. `coset_leakage`  kappa := `raw_ratio` / `stripped_mean_ratio`.
   The exact multiplicative factor clause (i) routes away. Reported as
   NaN when `stripped_mean_ratio` is 0 or NaN, and the NaN case is
   itself a finding (total coset confinement), never silently dropped.
6. `coset_mass_share` sigma := cs[0] / s_null = fraction of the
   CONDITIONAL mass sitting in the coset column.
7. `uncond_coset_share` sigma_u := asum[0] / s_all = the same share on
   the UNCONDITIONAL side. (sigma vs sigma_u is the like-for-like
   test: routing is multiplicatively neutral iff sigma == sigma_u.)
8. `headline_junction_bits` b_raw := log2(`raw_ratio`); the packet
   transport charges `33 * b_raw` against the 21-bit reserve.
9. `clause_ii_vacuity` := boolean, TRUE iff
   (`bulk_ratio` in {0, NaN}) AND (`raw_ratio` > 1.554406).
10. `reserve_usage_raw` := 33 * log2(`raw_ratio`) / 21.
11. `reserve_usage_bulk` := 33 * log2(`bulk_ratio`) / 21 (the banked
    F-b path, recomputed as my positive control).

## P3. THE C2'' ADVERSARIAL ESCAPE TEST (F-d), REGISTERED IN ADVANCE

New falsifier family **F-d (COSET-ROUTING NEUTRALITY)**. It attacks the
clause-(i) reduction, which F-a/F-b/F-c all presuppose and none test.

F-d FIRES (= the headline as written in `statement.md`/`node.json` is
refuted at toy scale, transport clause stated) iff BOTH:

- (F-d-1) there exists a measured row with `raw_ratio` > 1.554406
  (= 2^(21/33)) AND `clause_ii_vacuity` TRUE — i.e. the packet's own
  33-junction transport overflows the 21-bit reserve on the headline
  object at a row where the object clause (ii) constrains is empty;
  AND
- (F-d-2) routing is NOT multiplicatively neutral there:
  `coset_leakage` > 1 + 1e-3, or `coset_leakage` is NaN because the
  stripped conditional mass vanishes while the coset mass does not
  (sigma = 1 > sigma_u).

**ESCAPE (C2'' survives F-d) iff ANY of:**
- (E-a) `raw_ratio` <= 1.554406 at every measured row (no headline
  overflow under the packet transport); or
- (E-b) `coset_leakage` == 1 within 1e-3 at every row where
  `raw_ratio` > 1.554406 (routing multiplicatively neutral, so
  stripping is free and the headline is equivalent to clause (ii)); or
- (E-c) sigma == sigma_u within 1e-3 at those rows (the coset column
  carries the same share on both sides, so it cancels in X/A).

If F-d fires I will ALSO state, explicitly, what it does NOT reach
(see P6).

## P4. TOY CELLS DECLARED IN ADVANCE

Grid = the 8 banked b2b TEST-1 calibration rows, verbatim `CAL_ROWS`
from `.../c2r2_fround2_20260713/c2r2_local.py:27-28`:
(t,q) in {(2,97), (2,193), (2,8353), (2,32801), (3,97), (3,193),
(4,97), (4,193)}, all at n = 32.

- CATCH-Z6: n = 32 = 2^5, h = 16 = 2^4 — 2-power grid, asserted in code.
- CATCH-19B: VACUOUS here and I say so rather than silently skipping
  it — the b2b nested-tower census has no shift parameter. The index
  k is the profile-class WEIGHT, and k=0 is the coset column, which is
  the object under study, not a shift-0 cell.
- theta = 2.0, the pose convention
  (`C2PP_POSED_20260710.md:19-20`). I will spot-check theta in {2,3,4}
  and report insensitivity or its failure.
- Junction convention /33, reserve 21 bits, allowance
  2^(21/33) = 1.554406 — the pinned display, catches #108/#164.

I add NO new q-scales in this round. This is deliberate and I register
the reason in advance: the two survived rounds already went WIDER; the
open question H1-H3 is not about width, it is about WHICH FUNCTIONAL
is scored on cells that are already banked. If F-d fires on the banked
grid, width is irrelevant to the finding.

POSITIVE CONTROL (required to pass before any F-d read): reproduce the
banked 8-row `raw_ratio` values via `m1.BANKED_F2B_RATIOS` and the 8
pose `bulk_ratio` values {0.998, 1.010, 0, 0, 1.033, 1.066, 0.760, 0}
and their GM 0.967. If the control fails, no F-d verdict is issued.

MUTATION CONTROL (required to trip): recompute `reserve_usage_bulk`
over the F-b search rule `if b > 0` and confirm it reproduces the
banked ~14.53% usage; then recompute WITHOUT the `b > 0` filter, with
vacuous-bulk rows scored at their `raw_ratio`, and confirm the usage
changes. If the two agree, H2 is wrong and I say so.

## P5. NUMERIC PREDICTIONS (registered BEFORE running)

- **PR1**: at (2,8353) and (2,32801), `bulk_ratio` in {0, NaN} while
  `raw_ratio` > 1.554406. Confidence HIGH (banked).
- **PR2**: `coset_mass_share` sigma >= 0.90 at both those rows.
  Confidence MEDIUM-HIGH.
- **PR3**: `coset_leakage` at (2,8353) = 4.25 / 2.752 = **1.544**
  +/- 0.02 — i.e. JUST BELOW the 1.554406 allowance. (2.752 is the
  banked stripped junction ratio at t=2,q=8353,
  `.../C2PP_POSED_20260710.md:85-88`.) Confidence MEDIUM; a sharp
  numeric commitment.
- **PR4**: `coset_leakage` at (2,32801) > 1.554406. Confidence LOW —
  this is the genuinely uncertain call and the one that decides
  whether the coset column ALONE overflows the reserve.
- **PR5**: `raw_ratio` at (4,97) and (4,193) reproduces 2.82 / 3.57
  (`.../F_ROUND_CONJECTURE_FALSIFICATION.md:90`). Confidence HIGH.
- **PR6**: F-b's banked `x_max = 1.0662` originates from the (3,193)
  row (pose bulk 1.066), NOT from a high-loss row. Confidence HIGH.
- **PR7 (the honest escape prediction)**: F-d will NOT produce a kill
  under the node's OWN pre-declared falsifier list, because raw
  unstripped ratios are pre-declared NOT-falsifiers at
  `.../C2PP_POSED_20260710.md:64-67` and
  `critical/nodes/dli_c2pp_joint_reserve/attack.md:12-14`. So the
  expected outcome is a STRUCTURAL finding against the statement of
  record and the wiring, not a node kill. Confidence HIGH. I register
  this so I cannot later inflate a structural finding into a refutation.

## P6. WHAT F-d CANNOT REACH (registered in advance)

- No official-row inference. The node's calibration clause is
  respected: toy rows at n=32 are NOT evidence about official rows
  absent a stated transport. The ONLY transport I use is the packet's
  own pinned arithmetic (`x**33` vs `2**21`), and I use it exactly as
  F-b used it — on a different functional. Any claim beyond "under the
  packet's own transport, on the banked toy rows" is out of scope.
- F-d cannot show clause (ii) is FALSE. If clause (ii) is vacuous at
  the high-loss rows, vacuous is not false. The finding would be that
  clause (ii) does not IMPLY the headline, not that clause (ii) fails.
- F-d cannot settle whether the packet's exact staircase account
  legitimately moves the coset mass onto the A(R) side. It can only
  show whether A(R) AS DEFINED in the node (`prod_j E_U[rho_j]`,
  unconditional) already contains it. If it does not, the fix is a
  re-statement, and the re-statement is D5's job, not a kill.
- No status flip, no closure claim. Verdicts + artifacts only.

## P7. COMPUTE + SCOPE DISCIPLINE

Every python3 invocation goes through `tools/ramguard tiny -- python3`
or `tools/ramguard local -- python3` from the repo root, literal `--`,
stdlib only. All artifacts land in
`notes/pilots_20260807/c2pp_diag/`. No edits to dag.json, nodes/, or
tools/. The M1 kernel module is loaded READ-ONLY with
`sys.dont_write_bytecode = True` exactly as
`.../c2r2_fround2_20260713/c2r2_local.py:20` does, so no .pyc is
written into the node tree.

