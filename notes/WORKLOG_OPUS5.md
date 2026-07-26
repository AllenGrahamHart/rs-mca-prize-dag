# WORKLOG — Opus 5 repo worker

Standing brief: `notes/OPUS5_WORKER_GOAL.md`.

---

## 2026-07-26 — session 1

Basis: prize master `dd9b862d` → `e8628ecc`; upstream read-only at
`origin/main = b13de811` (unchanged this session; open queue #1087–#1105, all
holmbuar/scottdhughes, no triage movement since 07-25).

### Landed

**1. Q0 CLOSED — orbit-count reconciliation (`210dd4ef`).** Not drift: two orbits
with different roots, both exact.

| name | root | census |
|---|---|---|
| MATH ORBIT | {`mca_grand`,`list_grand`} | 260 = 201 PROVED / 36 CONDITIONAL / 23 TARGET |
| SUBMISSION ORBIT | `prize` | 275 = 213 / 38 / 24 |

Difference = a 15-node packaging spine (12 PROVED; the 2 CONDITIONALs are `prize`
and `packaging` themselves; the 1 TARGET is `submission_quality_paper_dossier`).
`275 − 260 = 15` is definitional. The math orbit is what `critical_dag.json`, the
SVG/site, `verify_prize_dag.py`'s partition law and
`verify_critical_harness_coverage.py` measure; the submission orbit is the
ledger's baseline and equals the dominator set `verify_prize_dag.py` already
prints as "CRITICAL open nodes (on EVERY route to the prize)".

So the r1 header's *"supersedes 201/36/23"* and the fact-check's *"the brief's
201/36/23 is indeed stale"* are **both wrong** — a confirmed-the-number,
never-checked-the-definition miss. New `tools/verify_orbit_census.py` pins both
censuses, the spine **by name**, containment, the 23-math-leaf count, and
cross-checks `orbit/critical_dag.json` for staleness/label drift; 6 mutation
controls, all caught. Corrected: `CONVERGENCE_LEDGER_R1.md` (header, DONE, C3-3,
ownership split, C3-6), `joint_graph_lean.md`, `plan_harvest_jointgraph.md`,
`completeness_critic.md`, `factcheck_summary.md`, `OPUS5_WORKER_GOAL.md`, and
`PRIZE_RESOLUTION_ROADMAP.md` §4 — which carried the same wrong-root mislabel
("req-closure of `prize` = 260 nodes").

*Consequence banked for C3-3:* of "the 38 CONDITIONALs" exactly **36** are
mathematical; `prize`/`packaging` discharge as consequences, not hypotheses.

**2. Renderer nondeterminism fixed (`e8628ecc`).** Two rebuilds from a
byte-identical `critical_dag.json` emitted different HTML/SVG — ~1900 lines of
phantom diff every time the standing site-refresh rule fired. Cause:
`ring = {v: lrank(v) for v in crit}` iterates a **set**, seeding each ring's
membership list in `PYTHONHASHSEED` order; `spread()` then re-sorts in place and
`list.sort` is stable, so ties inherited the random order through 40 relaxation
sweeps. One `sorted()`. Verified byte-identical across `PYTHONHASHSEED=1,2,3`.
Data layer was never affected.

**3. H1/S3 replay — GF list compilers vs the thirteen chambers (`<this commit>`).**
Artifact `critical/nodes/rate_half_list_adjacent_crossing/verify_affine_span_chamber_replay.py`
(stdlib, exact integers, 8 mutation controls, all caught); record in that node's
`notes/affine_span_chamber_replay_20260726.md` + a statement addendum.

- **Headline (negative): the compilers kill NONE of the thirteen chambers, so the
  ledger's S3 promotion test does not fire and H1 stays ev-wired.** The chambers
  are edge-degree patterns of the *locator* pencil; the compilers constrain the
  *codeword* affine span. No map between them exists in the node. What is owed is
  a lemma computing the affine rank `s` (ideally `d_1,d_2,b`) of the four
  codewords from a chamber's edge degrees.
- **Positive by-product:** no three list members at agreement `a` are collinear
  whenever `n-K+1 > floor(3(n-a)/2)` — proved directly, independently of the
  compiler. At the official row it fires for all `a >= 1,466,015,503,701 =
  3n/4 − 183,251,937,963` (1.83e11 steps of headroom) and reproduces the
  compiler's `s=1` caps. Hence four list members at `3n/4−1` have `s ∈ {2,3}`.
- **Trap recorded:** pinning `d_j` at the MDS floor makes the rank-flat cap look
  like it forces `b=0` at `s=2` — a rigidity theorem that isn't. It holds only at
  minimum support; the `b`-budget grows to ~4.5e10 at `d_2=3n/4`.
- **Banked artifact:** the cited-but-never-banked `RS[F_17,F_17^*,8]` four-codeword
  witness at agreement `11 = 3n/4−1`, now exact integers (12 exist in the
  normalized branch). Affine rank 3, weights `(9,12,14)`, `z=2,g=2,b=0`, all six
  pairwise agreements exactly `K−1=7` (every difference minimum-weight), no
  triple collinear. **Both compilers give cap 8 against actual list size 4** —
  neither is within a factor of two of tight on the only concrete configuration
  on record.
- **Citation repair:** the ledger's H1 pins `:498/:439/:583` are in
  `experimental/grande_finale.tex`, *not* `proximity_prize_results_v4.tex` (none
  of the four labels exists there); and `thm:single-mds-circuit-ray` is
  `RS_MCA_Paving_v9.2.tex:1514`, not `:421`.

### Plan-of-record changes

- **Lean deferred behind the informal proof (user decision, banked in ledger §6).**
  Formalization follows a complete, stable informal proof. C3-5 pilot, Phase
  0(a)/(b), Phase 1, C3-6 `lean_ready` audit → **PAUSED**, gating nothing.
  Two measured facts support it independently: the upstream Lean lane is not
  greenfield (**447 `.lean` files; ~92 Lean-titled PRs — holmbuar 55, LegaSage 29,
  scottdhughes 6, manifoldcontrol 2, us 2**), and C3-5's pilot object (the corridor
  certificates) is **latifkasuli's #275**, merged 2026-07-05 and cited in v4 as
  `Corridor26`.
- **A5 registry defect (fix owed in Part 2).** The occupied-territory map omits
  **LegaSage entirely (121 PRs, 29 Lean, thresholds/C9 lane)** and **latifkasuli
  entirely (27 PRs, corridor + a `formalize:` census program)**, and describes
  holmbuar without noting he is the repo's principal formalizer. Two of the three
  lanes the ledger wanted to push into were unmapped, so both read falsely CLEAR.
  Part 2 must be re-derived from per-author sweeps, not the open-PR queue.

### Not done / deferred

- **Q1 (E-1 corridor prime), Q2 (E-2 Proth replay):** deprioritized under the
  user's redirect — exports close zero reds by construction. E-1 recon is banked
  above and the lane is currently clear (no open corridor PR), but it is an
  addendum to latifkasuli's packet and must credit #275.
- **M-1 (rate-half seam {2^39, 2^39+1}):** scoped, not attempted. The A=3 residual
  reduces cleanly — with `j = e−m`, failure ⟺ slack `h <= 4j`, equivalently a
  lower bound on the capacity deficit `C >= O + 16m·j + 4m`; at `e=m` the whole
  question is whether the sharp-cap stratum `h=0` (`T = 4m+1`) can occur. This is
  a genuine research grind behind 121 proved supporting nodes, not a one-session
  item; the ledger's "one session" estimate looks optimistic.

### Open questions for the planner

1. **Registry rebuild** — want me to re-derive A5 Part 2 per-author (all
   contributors, not just this week's active two)? It is cheap and two lanes are
   currently mismapped.
2. **S3's missing lemma** — is "affine rank from chamber edge degrees" worth
   posing as its own node? Without it H1 can never promote past ev, and the
   ledger's burn-down counts H1 as one of only two red-movers.
3. **M-1 sizing** — given (2), the ledger's claim that r1 closes "at most two
   reds" now looks like at most one (the M-1 seam), and that one is not a
   one-session item. Worth re-pricing r1's burn-down before the next wave.

### Validators

`verify_prize_dag` PASS · `verify_crosswalk` PASS (31 rows) ·
`verify_critical_harness_coverage` PASS (proved=201) ·
`verify_orbit_census` PASS (math 260, submission 275, spine 15) ·
`run_all_verifiers --refresh-manifest` PASS (scripts 1117).

Upstream actions: none (read-only reconnaissance only; no PR opened).
