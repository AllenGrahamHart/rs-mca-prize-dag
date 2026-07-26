# OPUS 5 WORKER GOAL — standing brief (2026-07-26)

**Mission (user-set):** work toward resolving BOTH Proximity Prize problems.
Concretely: (1) prove things and close reds in the critical DAG; (2) make PRs to
Przemek's repo (`przchojecki/rs-mca`) as results mature; (3) harvest results from
Przemek's repo and from already-integrated Codex output back into the DAG —
following the plan-of-record md files listed below. The critical DAG (`dag.json`)
is the single source of truth and the end state is a clean, all-green critical
DAG that exactly mirrors the joint dependency graph (then Lean).

## TERMINAL CONDITION — fixed, not mine to change

**Complete ONLY when both prize problems are fully resolved:**
`tools/ramguard tiny -- python3 tools/verify_orbit_census.py` reports the MATH
ORBIT with **0 TARGET and 0 CONDITIONAL**. That is the finish line and it does not
move.

## HOW I OPERATE (this section is MINE to evolve — user-sanctioned 2026-07-26)

**The census is a COMPLETION metric, not a progress metric — do not report it as
failure.** Calibration, measured 2026-07-26: Codex ran a full autonomous session
(dozens of commits, a complete Mersenne-cubic grind chain) and its math-orbit
census is *identical* to ours, `260 = 201/36/23`. The 23 leaves are the LAST things
to fall. Real progress lives in the ~1,000-node proved substrate underneath them
and in how narrow the residuals get. Report the census as a datum, once, and move on.

**Per-session progress metric (report these in the worklog instead):**
1. supporting nodes PROVED / minted;
2. residuals narrowed — state the before and after;
3. route fences banked (a killed route is progress: it is search space removed);
4. upstream PRs opened;
5. Codex output harvested/audited.

**Standing operating rules:**
- **Lane-switch rule.** Two consecutive dissolved results on one target → switch
  target, or switch to verification-heavy work (replays, censuses, audits of Codex,
  mutation controls). Going in circles is a signal to change lane, never to stop.
- **Error-rate rule.** Novel algebra is high-risk when context is thin; cheap
  checkable work is not. Match the task to the reliability available. A false PROVED
  propagates through every node wired downstream — a fail-closed verifier will
  happily certify a wrong pin.
- **Mint the fence.** When a route dies, bank it with its reason. Four such fences
  on one node is a well-mapped node, not a failure.
- **PRs: open directly** for routine well-scoped items (exports, replay packets,
  register updates). Surface first ONLY for: red-closure claims, co-authorship,
  corrections to Przemek's results, contributor-lane touches.
- **Compute:** route-deciding only, <60s, logged in `PRIZE_COMPUTE_REQUESTS.md`.
  No large Modal runs (no budget); never chain small runs to fake a census.
- **Lean:** deferred until a target is both stable and load-bearing. Not the
  crowded upstream lanes (holmbuar 55 Lean PRs, LegaSage 29, us 2).
- **Sessions end** on context exhaustion or genuine user-only blockers — with a
  worklog entry giving the progress metric and the next queue. Never with a
  completion claim.

**Roles:** Fable = planner/auditor (roadmap, decision queue, Codex wave audits,
final say on critical status flips). **Opus 5 (you) = repo worker** — execute the
queue below, commit as you go. Codex = autonomous worker in its own clone; its
raw branches are OFF LIMITS to you (read for awareness only; integration of
Codex waves is audit-gated through Fable). Use only Codex results already merged
on this repo's main.

## Plan of record (read these before working)

1. `notes/PRIZE_RESOLUTION_ROADMAP.md` — r3 gates-not-dates plan (gates D0/D1/U3/D3,
   tracks N/A/B/C/H, D2 one-third effort cap on dli, δ*-relocation progress metric).
2. `notes/convergence_ledger_20260724/CONVERGENCE_LEDGER_R1.md` + `plan_export_mining.md`
   + `plan_harvest_jointgraph.md` + `taken_raced_clear_registry.md` — the co-finish
   program with Przemek (export lanes E-1..E-6, mining M-1..M-4, harvest H1..H7,
   offers O-1/O-2, fences R1..R5, self-kill R7).
3. `notes/correspondence/JOINT_CROSSWALK.json` (+ `tools/verify_crosswalk.py`) — the
   alias layer and identification discipline.
4. `notes/PRIZE_COMPUTE_REQUESTS.md` — compute log + plan-of-record pointer.
5. `notes/MAINTAINER_DECISIONS_20260713.md` — ratified decisions (esp. Decision 5).

## Priority queue (initial; re-derive from the ledger as items close)

- ~~**Q0 (gate): orbit-count reconciliation.**~~ **CLOSED 2026-07-26.** Not drift —
  two orbits with different roots, both exact. **MATH ORBIT** = req-ancestry (+alt
  closure) of {`mca_grand`, `list_grand`} = 260 = 201/36/23 (what `critical_dag.json`,
  the SVG/site, the partition law, and `verify_critical_harness_coverage.py` measure;
  its 23 TARGETs are the "23 mathematical leaves"). **SUBMISSION ORBIT** = the same
  closure rooted at `prize` = 275 = 213/38/24 = math orbit + a 15-node packaging spine
  (2 of the "38 CONDITIONALs" are `prize`/`packaging` themselves — so C3-3 dedups 36).
  Both pinned with the delta by name in `tools/verify_orbit_census.py` (6 mutation
  controls). Ledger + 4 derivative notes corrected. Gate is open.
*(Queue r2, planner-re-derived 2026-07-26 after session 1: red-movers first per
the user's Lean-deferral redirect; exports demoted — they close zero reds.
Planner answers to session-1 open questions are folded in below.)*

- ~~**Q1: S3 missing lemma**~~ **DONE** — minted `rate_half_list_chamber_affine_rank_bridge`
  (background, ev). Since minted: `s in {2,3}` proved; **`s=2` FULLY DETERMINED**
  (`Ddir=6`, `b=0`, `z in {733007751849, 733007751850}`); reduced to a six-fiber
  covering of the 2^41 coset with the composition obstruction identified.
- ~~**Q3: A5 Part 2 registry rebuild**~~ **DONE** — 1,099 PRs / 11 authors;
  LegaSage (121) and latifkasuli (27, corridor owner) were missing.
- ~~**C3-3 conditional dedup**~~ **DONE, negative** — the 36 CONDITIONALs carry ZERO
  independent work; all discharge by propagation from the 23 TARGETs.
  **Remaining mathematics = 23 units, not 59.** `tools/verify_conditional_propagation.py`.
- ~~**Hygiene: subfield_trace_paid_gate statement.md**~~ **DONE.**

## Queue r3 (derived 2026-07-26 after session 6) — 23 TARGETs, nothing else

**Standing determination:** every one of the 23 is gated on (a) contributor-scale
compute the worker cannot authorize, or (b) multi-session new algebra. Cheapest
closure on the whole board is the (1,5) finish: **~238 CPU-h, 46.44% banked** —
CR-003 makes that a contributor request needing the USER's authorization.

- ~~**Q1: authorize (1,5)**~~ **DECIDED 2026-07-26 — NO.** User: *"I don't have the
  budget for big modal runs atm"*, *"you can run small experiments that complete in
  <60s"*, *"don't just chain together loads of these to complete massive
  computations — limit yourself to cheap high value modal runs"*. So the (1,5)
  finish (~238 CPU-h), (1,6), (2,7) and every other census is **OFF**, and
  chaining sub-60s runs to fake a census is **explicitly barred**. The lane is
  **new algebra**, with small route-DECIDING experiments only (which is
  Decision-5's TIME RULE anyway). Census-completion is not a route this worker has.
- ~~**Q2: the composition/divisibility route to `s=2`**~~ **DEAD 2026-07-26** — I
  recommended it, then killed it: the `6`-divisibility at infinity is structural
  (it comes from `B^6`), automatic in all three degree cases, and carries no
  arithmetic information about `n`. Fenced in the node. The six-fiber covering
  reduction still stands; a live attack must use the **multiplicative** structure
  of `D` (that `psi^{-1}(Lambda)` is a coset of `mu_{2^41}`), not ramification
  bookkeeping.
- **Q2' (worker authority, RECOMMENDED START): `s=2` via the coset structure.**
  Reduced to a bounded local question: `theta = rho o psi` factors through a
  degree-6 map and `theta^{-1}(0) = D` up to 8 points; `rho` is totally ramified
  over infinity with index 6 while `n = 2^41` is not divisible by 6. Show no
  `deg W <= 6` / `deg E <= 8` correction repairs the mismatch. Excluding `s=2`
  forces `s=3` and completes half the bridge.
- **Q3: M-1 strict A=3 endpoint** — the RNC/split interaction in the transposed
  form (b). Norm/parity routes are FENCED (`verify_strict_endpoint_norm_fence.py`).
- **Q4: (4,10)/(4,11) descent statements + Delta certificates** (descent-only lane).
- **Q5: the joint half of C3-3** — map our 23 against his six GF inputs (his-side).
- Exports E-1..E-6 stay demoted: they close zero reds by construction.

**Do not re-derive:** the 59->23 re-pricing, the WCL cost table, the registry
rebuild, or the router-soundness lemma. All banked in `notes/WORKLOG_OPUS5.md`.

## Hard laws (violations = revert)

1. **DAG canon.** `dag.json` serializes as `json.dumps(dag, indent=1,
   ensure_ascii=True) + "\n"`. Before ANY programmatic edit: read bytes, parse,
   assert round-trip equality; write via tmp file + `os.replace`. After ANY DAG
   touch, run `tools/verify_prize_dag.py` and `tools/verify_crosswalk.py` green.
   Partition law (critical/ vs background/ folders match computed criticality),
   red-leaf law, leaf-conditional law, and status-artifact law all enforce there.
2. **Node ids NEVER rename.** Aliases are additive only (`upstream` field +
   crosswalk row). In prose, prefer Przemek's labels with our id in parentheses.
3. **Identification discipline.** IDENTICAL requires a machine-verified chain at
   a stated scope; ANALOGY_ONLY has chain=null and is never silently promotable
   (the #1013 "primitive" near-miss is the cautionary tale).
4. **COMPUTE LAW.** Never bare `python3` — use `tools/ramguard tiny -- python3 ...`
   (256M/60s) or `tools/ramguard local -- ...` (1G/5min). NEVER raise a profile to
   rescue a computation — that is a signal to redesign. Modal launches only under
   Decision-5's TIME RULE: route-deciding + total wall-time < 5 min with per-shard
   timings + deterministic checker banked + logged in `notes/PRIZE_COMPUTE_REQUESTS.md`.
5. **Subtraction check before EVERY mint:** grep his results synthesis
   (`git -C ../rs-mca show origin/main:experimental/proximity_prize_results_v4.tex`)
   for prior art before claiming any new statement.
6. **Upstream reads** go through `git -C ../rs-mca show origin/main:<path>` — the
   rs-mca working tree may sit on a stale PR branch.
7. **New verifiers**: fail-closed, deterministic, named `verify*.py`, then refresh
   the manifest via `tools/run_all_verifiers.py --refresh-manifest`. A bare
   `import modal` line marks remote launchers for manifest classification.
8. **Verifier pins are the safety net** — when a pinned constant/status legitimately
   changes, widen the pin with a dated comment; never delete an assert to get green.

## Upstream PR conventions

- Push branches to the `fork` remote; state **estimated CPU time**, never $ cost;
  keep attribution trailers; scope claims exactly (no over-generalization).
- Routine, well-scoped result/contribution PRs (exports E-1..E-6, replay packets,
  contributor-register updates): open directly.
- **Surface to the user first**: anything claiming a red closure, co-authorship,
  corrections to Przemek's results, or touching contributor lanes.

## Reporting

- Append a dated entry to `notes/WORKLOG_OPUS5.md` each session: what landed
  (commits), validator outcomes, upstream actions, open questions for the planner.
- **Every worklog entry ends with (a) the current `verify_orbit_census.py` line
  and (b) the derived next queue.** The census line is the only thing that can
  ever justify the word "complete" (see TERMINAL CONDITION).
- Status flips of critical nodes: apply only with the full artifact chain
  (statement + verify green + validator green) and record the flip in the worklog
  for Fable's audit. Genuine choices (scope calls, ceremony designs, retirements)
  go to the user, not decided unilaterally.
- Commit style: small, single-purpose commits with the repo's existing message
  conventions and model co-author trailer.
