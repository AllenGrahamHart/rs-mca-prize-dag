# OPUS 5 WORKER GOAL — standing brief (2026-07-26)

**Mission (user-set):** work toward resolving BOTH Proximity Prize problems.
Concretely: (1) prove things and close reds in the critical DAG; (2) make PRs to
Przemek's repo (`przchojecki/rs-mca`) as results mature; (3) harvest results from
Przemek's repo and from already-integrated Codex output back into the DAG —
following the plan-of-record md files listed below. The critical DAG (`dag.json`)
is the single source of truth and the end state is a clean, all-green critical
DAG that exactly mirrors the joint dependency graph (then Lean).

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
- **Q1: E-1 corridor-prime export** → upstream PR (front of the export queue; this
  packet carries the Lean pilot).
- **Q2: E-2 Proth replay export** → upstream PR.
- **Q3: M-1 seam mint** — the {2^39, 2^39+1} seam (top mining line; one session).
- **Q4: H1 chamber check** — replay his affine-span compilers against our 13
  chambers; run the ev→req promotion test on every harvest wire before consuming.
- **Q5: X-1 scoped identification certificates**, then continue down E-3..E-6,
  M-2..M-4, H2..H7 in ledger order.
- **Standing:** watch upstream triage of holmbuar #1097/#1099/#1101 (NEVER race
  them — our floor is the lane's foundation, the refinements are theirs); re-pin
  crosswalk aliases when upstream vocabulary moves; run `tools/publish_site.sh`
  after every DAG update.

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
- Status flips of critical nodes: apply only with the full artifact chain
  (statement + verify green + validator green) and record the flip in the worklog
  for Fable's audit. Genuine choices (scope calls, ceremony designs, retirements)
  go to the user, not decided unilaterally.
- Commit style: small, single-purpose commits with the repo's existing message
  conventions and model co-author trailer.
