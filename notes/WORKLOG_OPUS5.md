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

**3. H1/S3 replay — GF list compilers vs the thirteen chambers (`05c511e7`).**
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

---

## 2026-07-26 — session 2

Basis: prize master `e8628ecc` → `d6cc5ad5`; upstream read-only at
`origin/main = b13de811`.

**CENSUS LINE (terminal condition):** `ORBIT_CENSUS_PASS math=260(201/36/23)
submission=275(213/38/24) spine=15 math_leaves=23`. **59 nodes of mathematics
remain (36 CONDITIONAL + 23 TARGET). NOT complete.**

### Landed — queue r2 Q1, Q2, Q3 + hygiene

**Q1 (`15c9e351`) — minted `rate_half_list_chamber_affine_rank_bridge`**, the S3
missing lemma, as its own node. Statement: produce `chamber -> (s, d_1..d_s, b)`
binding the thirteen edge-degree chambers to the affine invariants the GF
compilers actually consume. Pinned going in: `s >= 2` whenever
`n-K+1 > floor(3(n-a)/2)`, so `s in {2,3}` and the bridge need only separate the
knife-edge `s=2` (cap exactly 4) from `s=3` (cap 8).

*Expected sign stated up front so a negative still counts.* Measured over **all
twelve** four-codeword witnesses of the banked F_17 branch: **`s=3` 12/12,
`b=0` 12/12, `d_1=9=R+1` always** (`d_s=14` ×9, `d_s=15` ×3; 71 pairwise
agreements at exactly `K-1=7`, one at 6). So the bridge is expected to kill **no**
chamber — worth proving anyway, because it retires the H1 promotion hope outright
instead of leaving it indefinitely "promising". Falsifier is wired, not just
stated: `verify.py` re-derives every branch witness and fails closed on any with
`s != 3` or `b != 0`. Wired **ev, not req** — the census is unchanged, no new
critical red. Subtraction check clean.

**Q2 (`c066a1c3`) — M-1 strict A=3 endpoint: transposed normal form + norm route
fence.** Two restatements of the `B=2^39`, `e=m`, `h=0` sharp cap; (a) is SSL14 in
resultant language, (b) is its transpose and was not on record:

```text
(a)  Res_X( X^N - c , Q(U,V;X) ) = H(U,V)^(4m-1) S(U,V),   S linear   [O=0]
(b)  (X - x_0) prod_{gamma in Z} Q_gamma(X) = kappa (X^N - c)^m
```

(b) exhibits the endpoint as a factorization of an `m`-th power of the
smooth-domain polynomial into `4m+1` members of an `(m+1)`-dimensional space lying
on a degree-`m` rational normal curve — the honest live target.

**FENCE:** the obvious norm attack on (b) is dead. Leading/constant coefficients
give `prod_gamma pi_gamma = (-c)^m / x_0`, but this is a *consequence* of the
covering ledger (`= prod_x x^{d_x}`), so the comparison is circular. Certified two
ways: it holds on 160 combinatorial covers with no algebraic realizability at all;
and the cyclic-exponent congruence needs `m*(N/2) == 0 (mod N)`, which at official
scale is `2^77 == 0 (mod 2^41)` — **vacuous by 36 powers of two**, not a near-miss.
The verifier self-tests that the equation *does* catch wrong multiplicities, which
is what makes the fence precise. 5 mutation controls, all caught.

**Q3 (`5056e27d`) — A5 registry Part 2 rebuilt per-author.** Full sweep:
**1,099 PRs, 11 authors**. The old Part 2 came from the open-PR queue and missed
**LegaSage (121 PRs, 29 Lean)** and **latifkasuli (27, the corridor owner)**
entirely, and described holmbuar without noting he is the principal formalizer
(55 Lean PRs of 370). Standing rule recorded: derive lanes from per-author
history, never the open queue; **dormancy is not vacancy** (LegaSage silent since
07-10, latifkasuli since 07-19, both holding large coherent programs).

**Hygiene (`d6cc5ad5`)** — `subfield_trace_paid_gate` statement.md, verbatim
transcription of the dag fields (no paraphrase on a PROVED critical node).
Status-artifact gaps 25 → 24.

### Flagged

**Upstream #1106** (draft, opened 2026-07-26 by our account): *"K3: add column-far
fixed-union ray route cut"*. **Not opened by this worker.** Recorded in the
registry so K3 route-cut material is not duplicated; not touched.

### Next queue (r3, derived — 59 math nodes remain)

1. **M-1 continued** (Q2 successor): attack the RNC/split interaction in form (b) —
   can `4m+1` totally-`D`-split degree-`4m-1` polynomials lie on a degree-`m`
   rational normal curve with each domain point covered exactly `m` times? Then the
   `O>0` and `e>m` strata (`h <= 4(e-m)`), then the half-distance budget `2^39+1`.
2. **Bridge attack** (Q1 successor): route 2 or 3 of its attack surface — prove
   `s=3` or `b=0` outright. Both are equality-case rigidity problems.
3. **Conditional dedup (C3-3)** — the 36 mathematical CONDITIONALs against his six
   GF inputs. Untouched, and it is half the remaining census.
4. **X-1 scoped identification certificates**; then M-2..M-4, H2..H7.
5. Exports E-1/E-2 remain demoted (zero red movement).

### Validators

`verify_prize_dag` PASS · `verify_crosswalk` PASS · `verify_critical_harness_coverage`
PASS (proved=201) · `verify_orbit_census` PASS · `run_all_verifiers --refresh-manifest`
PASS (scripts 1119). Upstream actions: none — read-only throughout; no PR opened.

---

## 2026-07-26 — session 3

Basis: prize master `457ce416` → `8aa40e23`; upstream read-only at `b13de811`.

**CENSUS LINE:** `ORBIT_CENSUS_PASS math=260(201/36/23)` — **unchanged**. No node
changed status this session. **NOT complete.**

But the census now means something different, and smaller.

### C3-3 CLOSED WITH A NEGATIVE (`8aa40e23`) — the endgame re-prices 59 → 23

Went after the CONDITIONALs because they are 36 of the 59 remaining and were
entirely unworked. The result is that **they are not work at all.**

Step 1 was an inventory: of the 36, **zero** are flip candidates — every one has
an open req-parent. Step 2 asked the decisive question: grant all 23 TARGETs and
propagate. **36/36 discharge, fixpoint in 8 rounds, 0 off-orbit blockers.**

Step 3 is the one that makes it trustworthy. Propagation is a claim about the
*wired* graph; the failure mode is a hypothesis living in prose that was never
wired as an edge — which is precisely what C3-3 was commissioned to hunt. So every
open node named in any CONDITIONAL's `statement`/`notes`/`conditional.md` was
classified ancestor / ev-parent / descendant. 12 fell outside; all 12 were read
and are benign, each explicitly fenced *in the node itself*:

- `xr_clean_residual_any_gate`: *"No use of the broader `rigidity_kernel`
  alternative is needed for this conditional route."*
- `list_adjacency_closing`: *"This argument does not consume
  `ww_row_envelope_clause`."*
- `xr_smallcore_spread_count`: rigidity kernels are *"ev context on the predicates
  only … not by consumed reduction."*
- `u1_pullback_dichotomy` in two nodes: stale prose, already banked as a DOC
  CORRECTION (*"the DAG edge and this n^3 form are authoritative"*). Verified
  directly — that node has exactly one out-edge and it is `ev`, so it is a
  req-parent of nothing.

All 12 are pinned **by name** in `tools/verify_conditional_propagation.py`, so a
*new* unrelated mention fails the check and forces a re-audit rather than passing
silently. 4 mutation controls, genuinely caught.

**Consequences, banked in the ledger:**

1. The Definition of DONE's CONDITIONAL conjunct is **struck as redundant** on our
   side. DONE = the 23 mathematical leaves + the dossier + his four inputs.
2. **The remaining mathematics is 23 units, not 59.**
3. 100% of remaining mathematical effort belongs on the 23 TARGETs — a session
   spent "discharging conditionals" is spent on nothing.
4. Only the **joint** half of C3-3 survives: mapping our 23 against his six GF
   inputs. That is his-side work; we cannot do it unilaterally.

### Correction made mid-session

My first mutation controls for the propagation verifier were **invalid** — the
mutated copies resolved `ROOT` from the scratchpad and died on
`FileNotFoundError`, so all four "catches" were spurious. Redone in-tree; all four
then failed on the intended assertions. Recorded because a verifier with fake
mutation controls is worse than one with none.

### Next queue (r4)

The board is now unambiguous: **23 TARGETs, nothing else.** Ranked by the two
live red-movers plus the largest blockers from the propagation analysis:

1. **M-1 continued** — the RNC/split interaction in the transposed form (b): can
   `4m+1` totally-`D`-split degree-`4m-1` polynomials lie on a degree-`m` rational
   normal curve with each domain point covered exactly `m` times? Then `O>0`,
   `e>m`, then the half-distance budget.
2. **The bridge** (`rate_half_list_chamber_affine_rank_bridge`) — prove `s=3` or
   `b=0` outright; both are equality-case rigidity problems.
3. **The 12 dli WCL slot emptiness TARGETs** — the single largest block of the 23
   (`dli_wcl_slot_*`), and `dli_wcl_zone_coverage` is blocked by 10 of them at
   once. Highest cascade value per closure.
4. `f2_growing_order_myerson` (the F2 summit / Wall 1), `rate_half_band_closure`,
   `l1_mixed_petal_amplification`, `rate_half_list_adjacent_crossing` — the wired
   bottlenecks.
5. Exports stay demoted.

### Validators

`verify_prize_dag` PASS · `verify_crosswalk` PASS · `verify_orbit_census` PASS ·
**`verify_conditional_propagation` PASS (new)** · `run_all_verifiers
--refresh-manifest` PASS (scripts 1120). Upstream actions: none; read-only
throughout, no PR opened.

**Session ended on context budget**, per the brief's three permitted reasons.

---

## 2026-07-26 — session 4 (short): why no TARGET is locally closable

**CENSUS LINE:** `math=260(201/36/23)` — unchanged.

Went after the 23 TARGETs directly, starting with the highest-cascade block: the
ten `dli_wcl_slot_*` emptiness leaves, of which ten block `dli_wcl_zone_coverage`
simultaneously. Determination, from
`critical/nodes/dli_wcl_zone_coverage/official_terminal_attack.md` (2026-07-22
Burnside sizing ledger, 3/3 calibration anchors exact):

| slot | census | cost | verdict |
|---|---:|---|---|
| (1,5) | 2,296,920 | **445 CPU-h, 46.44% banked** → ~238 CPU-h left | cheapest open cell in the whole board |
| (1,6) | 185,569,028 | ≥36k CPU-h (~$6.6k) | marginal |
| (1,7) / (1,8) | 1.30e10 / 8.06e11 | 289 CPU-y / hopeless | need new algebra |
| (2,7) | router 94,652,815 | 33k CPU-h | live only after the GMP-gcd swap + k=5 router soundness |
| (2,8) / (2,9) | 1.86e10 / 3.08e12 | 6.4M / 1.07e9 CPU-h | need new algebra |
| (4,9)/(4,10)/(4,11) | 8.07e17 / 1.64e20 / 3.01e22 | infeasible at any rate | DESCENT-ONLY |

These are **zero-event obligations quantified over every official row**
(`q < 2^256`, `v_2(q-1) >= 41`), so they are not finite sweeps that a clever
enumeration closes — they are closed the way (2,5) and (2,6) were: a structural
router, then cyclotomic norm gcds, then full factorization, then the check
`max v_2(p-1) < 41`. Each weight needed **its own new router**; that is the
mathematical content, and it does not transfer from w=6 to w=7 for free.

**The obvious speedup is explicitly unsound and the node says so.** Filtering
candidates by the progression `p == 1 mod 512` (or `mod 2^41`) to avoid full
factoring is barred by the recorded CENSUS-SOUNDNESS CATCH: prime factors of these
norms are *not* all `== 1 mod n`, because roots may live in extensions (witnessed:
31 divides an order-64 norm). Full or certified-partial factoring only. So the
per-candidate cost is not compressible by that route.

**Conclusion.** The cheapest remaining unit of the entire board needs ~238 CPU-h.
That is far beyond `ramguard local` (1G / 5 min) and far beyond Decision-5's Modal
TIME RULE (route-deciding, total wall-time < 5 min). Under the node's own compute
custody rule (CR-003): *"Runs at or above the local time/cost policy are
contributor requests for an upstream PR, not local Modal jobs."*

Combined with session 3's C3-3 result, the endgame assessment is now exact:

> **The remaining board is 23 units, and every one of them is gated on either
> (a) contributor-scale compute the worker cannot authorize, or (b) new algebra.**

There is no remaining task in this lane that is both census-moving and inside the
worker's compute authority. **This session ends blocked on user input** — the
second of the brief's three permitted reasons — with one concrete decision owed
(below). It does not end with a claim of completion.

### Decision owed to the user

1. **Authorize the (1,5) finish** as a contributor-scale compute request (~238
   CPU-h, the cheapest TARGET closure available, 46.44% already banked) — logged
   in `notes/PRIZE_COMPUTE_REQUESTS.md` under CR-003 per the custody rule; or
2. **Redirect to new algebra** on a descent-only / new-algebra cell — (4,10)/(4,11)
   descent statements + Delta certificates, or the (2,7) k=5 router soundness,
   neither of which needs compute authorization; or
3. **Redirect off the dli lane** to another of the 23 (F2 summit,
   `rate_half_band_closure`, `l1_mixed_petal_amplification`,
   `rate_half_list_adjacent_crossing`), accepting that those are multi-session
   research grinds with no compute shortcut either.

Recommendation: **(2)**, specifically the (2,7) router-soundness item — it is the
only piece of work on the board that is inside worker authority, unblocks a
33k-CPU-h census rather than consuming it, and needs no money or maintainer
surface.

---

## 2026-07-26 — session 5: the (2,7) router-soundness obligation, discharged

**CENSUS LINE:** `math=260(201/36/23)` — unchanged. No TARGET closed.

Session 4 ended by recommending the (2,7) router-soundness item and asking the
user to choose. That was the wrong call: I had just identified it as the one piece
of work on the board **inside worker authority, needing no compute authorization
and no maintainer surface**. Waiting for permission I did not need is not being
blocked. Did it instead (`67eb70ce`).

**Result — a general lemma, all `k`, not just the `k=5` cell that was asked for.**
Every `(2,w)` router leaves a monic degree-`k` factor whose roots must be tested
for membership in `mu_M`, `M = 2^t`, by `t` modular squarings. For
`char F = 0` or `char F > k`, `M = 2^t`, `char != 2`, `f` monic of degree `k`,
`f(0) != 0`:

```text
(i)   X^M == 1 (mod f)  <=>  f | X^M - 1  <=>  f SQUAREFREE and every root in mu_M
(ii)  no false positives
(iii) false negatives, EXACTLY on non-squarefree f with all roots in mu_M
(iv)  correct test on arbitrary f is X^M == 1 (mod rad f)
```

Everything turns on `X^M - 1` being separable, so it has no repeated factor to
absorb a non-squarefree `f`.

**Why it is the soundness obligation.** The slots are zero-event obligations — the
census must *exclude* every candidate. A false positive is harmless (it keeps a
candidate alive for the norm stage); a false negative silently discards one, and a
discarded candidate is an un-excluded candidate. So the bare doubling test on a
possibly-non-squarefree `f` makes the emptiness claim **unsound**.

**This retro-explains the closed (2,6) certificate.** Its `510` "structural
double-zero cases" (the antipodal-mirror family `c = 512+a+b`, handled by the
power-of-two vanishing-sum lemma rather than by the recurrence) are exactly this
stratum. That was this obligation being paid — not incidental bookkeeping. A (2,7)
router at `k=5` owes the same payment and can now cite a general statement instead
of re-deriving per weight.

Certified on 15,016 polynomials over `(p,M) in {(17,8),(17,16),(97,32)}`, `k=2..5`
— deterministic spread sample **plus a forced non-squarefree stratum**, since a
random sample would rarely hit the case the lemma is about. 0 false positives;
every false negative non-squarefree as (iii) requires; radical test correct
throughout. Witness: `(X+1)^2` over `F_17`, `M=8` — root `-1` has order `2 | 8` so
it *is* in `mu_8`, yet `X^8 = 1+9(X+1) != 1 (mod f)`. 4 mutation controls, caught.

Closes no slot: `(2,7)` stays TARGET; the GMP-gcd swap and the 33k CPU-h census
remain.

### Standing position

The board is 23 TARGETs (session 3). Of these, every one is gated on
contributor-scale compute or new algebra (session 4 table). The router-soundness
item was the last piece of *new algebra* identified as both inside worker
authority and needing no authorization; it is now paid. Remaining new-algebra
items — the (4,10)/(4,11) descent statements + Delta certificates, the M-1 RNC/split
question, the bridge rigidity — are multi-session research, not one-sitting work.

**Decision still owed (unchanged from session 4):** authorize the (1,5) finish
(~238 CPU-h, cheapest closure on the board, 46.44% banked) under CR-003; or direct
effort at a specific new-algebra cell.

**(4,9) check (session 5 close-out):** confirmed the descent lane does not yield a
free closure either. `dli_wcl_ell4_weight9_quartic_divisor_descent` and
`dli_wcl_fixed_divisor_straight_line_lift` are both PROVED and both list the slots
as consumers — the lift covers (1,5), (1,6), (2,7) and (4,9) — but they reduce
each slot to a *straight-line divisor certificate* (`Y A(Y)^2 - 1`, `deg A = 4`,
`b = 4` base variables at (4,9)) that still has to be evaluated. Proved machinery
pointing at a slot is not a closed slot. No flip available.

### SESSION END — context/budget exhaustion (brief's first permitted reason)

Five sessions. Census `260 = 201/36/23` at start and at end; **no TARGET closed,
and I am not claiming otherwise.** What was produced: Q0 reconciliation + 3
verifiers, a renderer determinism fix, the H1/S3 replay (negative), a minted
bridge node, the M-1 transposed normal form + norm route fence, the A5 registry
rebuild, C3-3 closed with a negative (the 59 -> 23 re-pricing), and the (2,7)
router-soundness lemma in general k.

Honest assessment of the five sessions: the infrastructure and analysis are sound
and several results are load-bearing (notably C3-3, which shrank the measured
board by 61%, and the router-soundness lemma, which retro-justifies the (2,6)
certificate's degenerate stratum). But **none of it moved the census**, because
every one of the 23 remaining leaves is gated on contributor-scale compute or
multi-session new algebra. That is a property of the board, not of the effort
spent, and no further worker-authority work will change it.

**The next session should not re-derive this.** It should open with the user's
answer to the standing decision (authorize (1,5) at ~238 CPU-h under CR-003, or
name a new-algebra cell), and then grind that one thing.

---

## 2026-07-26 — session 6: the common-zero budget bound (CZB)

**CENSUS LINE:** `math=260(201/36/23)` — unchanged.

New theorem on the bridge node (`ba799ff2`), attack-surface route 3. Needs no
compute authorization. For four distinct codewords at agreement `>= m` with common
`u`, `z = |G|`, `b = z - g`:

```text
4(m - g) <= (n - z) + 6(K - 1 - z),   and at m = 3n/4 - 1, K = n/2:
3z + 4b <= n - 2.                                              (CZB)
```

Proof is a two-way count: `agr(c_i,c_j) <= K-1` bounds the pairwise sum, `G`
contributes `C(4,2)=6` per point, off `G` the four values are not all equal so
`P(x) in {0,1,2,3}`, and `a_x <= 1 + P(x)` there.

**Consequences** (`n=2^41`, `K=2^40`): `z <= (n-2)/3 = 733,007,751,850` (against the
trivial pairwise `z <= n/2 - 1`); `d_s >= (2n+2)/3 = 1,466,015,503,702`; `b = 0`
forced once `z >= 733,007,751,849`.

**Headline: the minimum-support case `d_s = R+2` is now impossible** (`4b <=
-1.09e12`). That is precisely the case in which `thm:rank-flat-list` appeared to
force `b=0` — which session 2 flagged as an artifact of pinning `d_j` at the MDS
floor. (CZB) shows the MDS floor is *unreachable* here, so the artifact could never
have been instantiated. The two findings agree rather than conflict, which is a
good sign for both.

The admissible `d_s` band shrinks from `[n/2, n]` to `[2n/3, n]`. Sharpness: the
step-2 pairwise bound is **tight on 11 of the 12** banked F_17 witnesses, so (CZB)
is essentially optimal for this argument rather than lossy.

Not a closure: does not decide `s=2` vs `s=3`; `b=0` only in the high-`z` regime.
Node stays TARGET.

### Standing position (unchanged)

23 TARGETs. Cheapest closure on the board is the (1,5) finish, ~238 CPU-h, 46.44%
banked, requiring CR-003 authorization the worker cannot give. Everything else is
multi-session new algebra. Sessions 5 and 6 each paid a real piece of that algebra
(router soundness in general `k`; CZB) without moving the census, which is the
expected shape of progress here.
