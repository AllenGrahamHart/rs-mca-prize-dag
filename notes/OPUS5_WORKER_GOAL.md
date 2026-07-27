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

## LIVING QUEUE — I re-derive this every session (last: 2026-07-26, session 7)

**Board:** 23 TARGETs. The 36 CONDITIONALs carry zero independent work — all
discharge by propagation once the TARGETs close (`tools/verify_conditional_propagation.py`).
So the remaining mathematics is **23 units, not 59**.

**Closed and not to be re-derived:** Q0 orbit reconciliation; C3-3 conditional
dedup (negative — see `assumption_dedup.md`); the A5 Part-2 per-author registry
rebuild; the WCL cost table; the router-soundness lemma (general `k`); E-1.

**Now:**
1. **E-2 Proth-row replay audit** → upstream PR. Precondition: refresh the stale
   crosswalk pins (9262f63c-era labels → v4 labels at the current pin). Their
   theorem; we confirm and close nothing. The deliberate down-payment on O-2.
2. ~~**s=2 equality case / the bridge**~~ **ANSWERED NEGATIVELY 2026-07-26.** The
   rank-flat compiler can NEVER exclude four codewords at this row: `s=2` gives cap
   `4` at the pinned `d_2`, and `s=3` has minimum cap `6` over the entire admissible
   region. So no chamber transport helps, the S3 promotion test can never fire, and
   **H1 is permanently ev-wired — the ledger's burn-down loses one of its two claimed
   red-movers.** Structural reason: the compiler needs `d_1` well above the MDS
   floor, and the razor bracket pins `d_1 in {R+1,R+2}` precisely because four
   codewords agreeing in `>= 3n/4-1` places force minimum-weight differences.
   *Node retirement to a route fence is surfaced to the user, not decided here.*
3. **M-1 strict A=3 endpoint** — the RNC/split interaction in the transposed form.
   Norm/parity routes fenced.

**STANDING LANE FENCE (2026-07-27) — applies to BOTH the WCL descent lane and the
rate-half endpoint lane.** Global multiplicative invariants (resultants, norms,
`mu_N`-products, quadratic characters, abc/Mason-Stothers) are **forced by the
defining identity** on these configurations and carry no information — they are
consequences, not constraints. Six routes have now died this way: the strict-endpoint
norm identity, the s=2 composition/divisibility route, the log-derivative count, the
symmetric realization, counting/(MI2) saturation, and the (4,9) Res/`mu_N`/character
family. **Attack local structure instead**: root-by-root incidence, ramification
profiles, the double-root pattern of `P+1`, chamber-level data. Do not spend another
session on a global product.
4. ~~**(4,11) / (4,10) descent statements**~~ **DONE 2026-07-27 — and the whole
   `ell=4` lane is now ONE question.** Both minted PROVED with verifiers. The three
   cells unify (`notes/ell4_uniform_form_20260727.md`):

   > `(4,w)` holds iff `w` distinct `rho_i in mu_2048` have `e_1=e_3=e_5=e_7=0`,
   > plus `e_w = 1` for **odd** `w` only.

   The quartics/quintics `A,E,B` are **outputs**, not unknowns — so the elimination
   ideal, `Delta` certificate and resultant routes were all fighting a
   reparametrisation. `(4,10)` needed no dilation at all (my "sub-tuple router"
   prediction was wrong). Rigorous lemma banked: reducedness forces `S_1 != 0` in
   `Z[zeta_2048]` via Lam–Leung, which validates the norm-gcd method and explains
   the closed `(2,6)` certificate's 510 exceptional cases. The honest bound
   `p <= w^1024` is far too weak to close anything.

   **What is genuinely left here:** a quantitative bound on `w`-subsets of `mu_2048`
   with four vanishing odd symmetric functions. Four routes are fenced (abc,
   `Res`, `mu_N`-product, character) and the existence witness proves **no
   structural argument can work**. This needs Weil/Deligne-scale machinery.
   *Recommend a lane change rather than more turns here.*

5. ~~**(4,11) THEN (4,10) descent statements + Delta certificates**~~ — order matters,
   and it is the reverse of the numeric order. Parity dichotomy (2026-07-26): the
   (4,9) global-dilation normalisation needs `w` invertible mod `N_ell = 512*ell`, a
   2-power, hence `w` **odd**. `(4,11)` is odd so (4,9)'s machinery transfers
   verbatim; `(4,10)` is even and carries an index-2 obstruction needing a new
   sub-tuple router first (the pattern of the closed (2,5)/(2,6) routers). Same
   dichotomy makes `(1,8)`/`(2,8)` index-**8** and structurally the hardest cells.
5. **X-1 scoped identification certificates**; then M-2..M-4, H2..H7, E-3..E-6.

**Standing:** per-session upstream-delta sweep and Codex harvest; watch triage of
holmbuar #1097/#1099/#1101 (never race); re-pin crosswalk aliases when upstream
vocabulary moves; `tools/publish_site.sh` after DAG updates (outward-facing —
surface first).

**Blocked, not mine:** any census requiring contributor-scale compute — (1,5) at
~238 CPU-h, (1,6), (2,7), (2,8), (2,9), the ell=4 cells. No budget; do not
re-propose, and never chain small runs to simulate one.

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
5. **Subtraction check before EVERY mint — WIDENED 2026-07-27.** The papers are
   NOT enough: PR #1106 was dominated by a theorem living only in a merged
   contributor note, and the miss cost a retracted "ready for review". Search
   ALL FOUR surfaces before claiming any new statement:
   (a) `git -C ../rs-mca grep -i "<keyword>" origin/main -- experimental/proximity_prize_results_v4.tex experimental/grande_finale.tex`
   (b) `git -C ../rs-mca grep -ril "<keyword>" origin/main -- 'experimental/notes/**'` (merged contributor notes — the #1106 blind spot)
   (c) `git -C ../rs-mca show origin/main:experimental/agents-log.md | grep -i "<keyword>"`
   (d) the external canon in `notes/literature_map_20260726/LITERATURE_MAP.md`.
   Compare BOUND STRENGTH and HYPOTHESIS STRENGTH, not just topic: a weaker
   hypothesis with a better constant dominates you even when the statements look
   different (that is exactly what happened at #1106).
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
