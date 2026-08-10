# PREREG — rh_farca_upper (round 32)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/rh_overlap_cap/REPORT.md` (round 31 — LB1
   and the residuals of record)
2. `background/nodes/rate_half_ca_hankel_minimal_index_budget/statement.md`

## Mandate

THE SAFE HALF'S OBJECT OF RECORD (R-UPPERBOUND): prove
B_ca^far(k+2^34) < 2^128 at the razor rows. Round 31 killed every
overlap-statistics route and gave the two-sided window: LB1's floor
B_ca^far(k+2^34) >= n-a+1 = 2^39.9773 vs the 2^128 budget — 88.02
bits of room, and NO upper bound of any kind exists in the open
bracket [k+2^34, 3n/4) (the Hankel layer's scope is a > 3n/4 only).
Wave 57 moved the bracket top to a_94 ~ 0.7109n by the Haboeck
direct-MCA route (its m-ladder is capped at m=95 by the field cap —
that route CANNOT reach further down). YOUR JOB: the first upper
bound on B_ca^far inside the open bracket.

## Deliverables

**D1 — THE ROUTE MAP.** Three candidate routes, price each with
file:line reads before attacking: (a) R-LINEDEGREE — anchor at one
bad slope; B <= 1 + t*r where t = #T1-lines through it =
|L(f_2, a-s)|, a single-word list at agreement >= 2a-n = 2^35;
budget t <= 2^88 suffices. What list-size instruments reach
agreement 2^35 at n = 2^41 (deep list regime)? (b) THE HANKEL
MOVING-KERNEL BRANCH — round 29 flagged it ABSENT ("the a > 3n/4
discharge is itself incomplete — a residual sentence, no node");
determine what the moving-kernel argument IS and whether it extends
below 3n/4 with a worse constant. (c) THE (GNF)/CATALECTICANT
route — the anchor node's characteristic-free apolar/Kronecker
machinery at minimal index r < 2^39: what exactly stops it at
r = n-a > 2^39 for a < 3n/4, and is the obstruction quantitative
(a worse bound) or structural (no bound)?

**D2 — THE STRONGEST PARTIAL.** Prove the best upper bound you can
on ANY sub-object: per-line (done: r+1, tight), per-anchor-stratum
(T2's per-stratum weights), bounded-line-count subclass, or a
conditional bound under a named hypothesis with a falsifier. Even
B_ca^far(k+2^34) <= 2^X for X < 216 (the current trivial payload
bound) would be the first movement.

**D3 — SCALED MEASUREMENTS.** At small scales: the TRUE B_ca^far(a)
across the bracket interior vs LB1's floor n-a+1. Is the floor
TIGHT in the interior (as it is at the a > 3n/4 endpoint)? If
measured B_ca^far = n-a+1 exactly at every reachable cell, the
working conjecture (B_ca^far = n-a+1 everywhere) is worth posing
with falsifiers — it would put the crossing at -lo immediately.
Pre-register expectations BEFORE running.

**D4 — VERDICT + the honest frontier.** Misses first; zero-power on
what small scales cannot see; every quantifier claim file:line.
DO-NOT-INHERIT: the T5/overlap-cap route is REFUTED (round 31) —
do not resurrect it; the P0 correction (far-CA binding on the whole
bracket) is the frame.

## Constraints (binding)

- COMPUTE LAW: never bare python3; ramguard tiny/local from repo
  root, literal `--`; RAMGUARD_TIMEOUT documented; stdlib only; no
  Modal/network/git.
- RAM DISCIPLINE: file-at-a-time; NEVER open dag.json; checkpointed
  batches.
- WRITE SCOPE: ONLY notes/pilots_20260810/rh_farca_upper/. No dag/,
  nodes/, tools/ edits. No git. Never touch prize-codex-*.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md;
  never read siblings (rh_fr_algebraic, rh_haboeck_seam,
  rh_residuals_close); round-31 and earlier readable.
- BLIND PRIORS: after the two anchors only, append "## Pilot
  registrations" (route ranking with P(first movement this round),
  P(floor tight in the interior), expected X) BEFORE any further
  read.
- REPORT: REPORT.md (harness-refused fallback: return verbatim; in
  all cases ALSO return verbatim as final message); MISSES-FIRST;
  CATCH-24C file:line; CATCH-24A greps; zero-power declarations;
  banked scripts from scratch copies only.

## Pilot registrations

Written after reading ONLY the brief above, `rh_overlap_cap/REPORT.md`
and `rate_half_ca_hankel_minimal_index_budget/statement.md`, and
BEFORE any grep, any `ls`, any other file, and any interpreter
invocation. All arithmetic below is done by hand from the two anchors;
where I give a numeric window it is a prediction to be checked by
`d1_prices.py`, not a measurement.

### R0 — the frame I am carrying in (stated so it can be falsified)

Razor row: `n = 2^41 = 2,199,023,255,552`, `k = 2^40`, `R = n-k = 2^40`,
`sigma = 2^34`, `a = k+sigma = 1,116,691,496,960`,
`r = n-a = 2^40-2^34 = 1,082,331,758,592`, `r+1 = 2^39.9773`,
`2a-n = 2^35`, `a/n = 0.5078125` exactly, `3n/4 = 0.75n`,
`sqrt(nk)/n = 2^-0.5 = 0.70710678…`.

Two classical radii are, I claim, the whole story of this bracket:

- **UD** (unique decoding) `r <= (d-1)/2 = R/2` ⟺ `a >= n-R/2 = 3n/4`.
  I register the prediction that the Hankel layer's "`a > 3n/4`" scope
  IS the unique-decoding radius, not an artifact of the (MI1)/(MI2)
  constants.
- **JN** (Johnson) `a > sqrt(nk) = 0.70711n`. I register the prediction
  that every incidence/counting instrument in this problem (slope-level
  Fisher, core-level Fisher, k-subset counting, anchored list bounds)
  has its threshold at exactly `a = sqrt(nk)` (up to `k` vs `k-1`), and
  that this is why wave 57's frontier sits at `0.7109n`, just above JN.

The razor `a = 0.5078n` is below BOTH. Registered consequence: I expect
to hand back a **route map with two named walls and no unconditional
bound on the full object**, not a first movement.

### R1 — route ranking, P(first movement this round)

Ranked by P(this route yields ANY unconditional upper bound on
`B_ca^far(k+2^34)` this round):

1. **(b/c) the Hankel/GNF layer, used by STRATIFICATION rather than by
   extension** — 0.55. Mechanism registered in advance: column-farness
   at radius `r` implies column-farness at every radius `r' < r`
   (it is a `>` on one number), so the banked corollary applies to the
   *near stratum* of a razor-row pair at `r' = R/2-2` and bounds
   `#{bad slopes of error weight <= 2^39-2}` by `2^39-1`. This bounds a
   STRATUM, not `B_ca^far`, and I register in advance that I will not
   dress it up as more.
2. **(c) the GNF/catalecticant route extended below `3n/4`** — 0.10.
3. **(b) the moving-kernel branch extended below `3n/4`** — 0.08.
4. **(a) R-LINEDEGREE** — 0.03 (see PR-C: I expect to prove it vacuous).

P(first unconditional upper bound on the FULL `B_ca^far(k+2^34)`,
by any route, this round) = **0.12**. P(a conditional bound with a
named hypothesis and a falsifier) = 0.70.

### R2 — P(floor tight in the interior)

P(`B_ca^far(a) = n-a+1` for all `a` in the open bracket, i.e. the
working conjecture is TRUE) = **0.20**.
P(my measurements at reachable cells show max `> r+1`) = **0.80**.
These are consistent: I expect the small cells to be in a different
regime from the razor (PR-G), so a measured excess is weak evidence
against the conjecture at the razor. I register the discount now.

### R3 — expected X

If anything lands: near-stratum `X_near = 39.0` (bound `2^39-1`).
For the full object I register **no X** and predict the honest answer
is "no unconditional bound exists in the repo after this round either".
P(X < 216 on the full object) = 0.12; conditional on landing, expected
X in `[39, 88]`.

### Numeric / structural predictions (windows fixed now)

- **PR-A (structural, not quantitative).** In the open bracket
  `r > R/2`, so the syndrome pencil `M(Z)` of shape `(R-r) x (r+1)` is
  **wide** (`R-r < r+1`): its kernel is nonzero at EVERY slope, and the
  witness/locator is not unique (2r+1 > R = d-1). Prediction: the
  obstruction to (c) is **structural** (uniqueness fails at the UD
  radius), not a worse constant. P = 0.75.
- **PR-B (a scope clash I expect to find).** Read literally in the wide
  regime: generic rank `rho <= R-r = a-k = 2^34`, hence
  `A = R+1-2rho >= 2r-R+1 = 2^40-2^35+1 = 1,065,151,889,409 > 0`, hence
  `(MI1) (A+s)e <= d = rho-s` forces `e = 0` (as `A > rho >= d`), hence
  the `e=0` branch would give `T <= rho <= 2^34 = 17,179,869,184` —
  **contradicting LB1's `r+1 = 1,082,331,758,593`** by a factor
  `63.0` (window [62.9, 63.1]). P(the literal reading does contradict
  LB1) = 0.65; P(the contradiction resolves against LB1 rather than
  against an unstated tall-pencil hypothesis) = **0.15**.
- **PR-C (route (a) is vacuous, quantitatively).** The anchored line
  degree is a single-word list at agreement `a-s`, worst case
  `2a-n = 2^35 = 34,359,738,368`. Predictions: (i) `2a-n < k` by a
  factor `2^5 = 32` exactly, so the k-subset counting bound
  `|L| <= C(n,k)/C(A,k)` is VOID (`C(A,k) = 0`); (ii) `2a-n < sqrt(nk)`
  by a factor `2^5.5 = 45.25`, so Johnson is VOID; (iii) even the best
  case `A = a` is below `sqrt(nk)` by the factor `1.3924`. Hence no
  list-size instrument of either species reaches ANY agreement in the
  whole bracket. P = 0.85.
- **PR-D (second level).** The core-level Fisher threshold is
  `sqrt(n(k-1)) = 1,554,944,255,987` (window ±2) while column-farness
  caps cores at `a-1 = 1,116,691,496,959`; ratio in **[1.3924, 1.3925]**.
  Prediction: the core-Fisher route is dead **even at the maximal core**,
  i.e. dead for a structural reason (`a < sqrt(nk)`), and it revives
  exactly at `a > sqrt(n(k-1))` — the JN wall again. P = 0.8.
- **PR-E (a one-line structural lemma I expect to prove).** Two distinct
  T1-lines have distinct difference-codewords `v_P != v_Q`, and their
  cores satisfy `E_P cap E_Q subset Agr(v_P,v_Q)`, so
  `|E_P cap E_Q| <= k-1`. Hence two MAXIMAL cores (`|E| = a-1`) coexist
  iff `2(a-1) <= n + (k-1)` ⟺ `a <= (n+k+1)/2 = 3n/4 + 1/2` — i.e.
  **exactly on the closed interior of the bracket, and never above the
  UD radius**. P(provable as stated) = 0.70; P(verified at a small cell)
  = 0.60.
- **PR-F (the partial I expect to land).** UB-NEAR:
  `#{CA-bad slopes of a razor-row column-far pair with agreement
  >= n-(R/2-2) = 3n/4+2} <= 2^39-1 = 549,755,813,887`, with
  `128 - 39 = 89.0` bits of margin (window [88.9, 89.1]). Registered as
  a **stratum** bound obtained by scope-monotonicity of a banked node,
  and I pre-register that CATCH-24A may well find it banked already
  (P(banked somewhere in-repo) = 0.35).
- **PR-G (D3 expectations, fixed before any run).** Define
  `rho_cell = C(n,n-a) / q^{a-k-1}`, the expected number of CA-bad
  slopes of a uniformly random 2-plane. Predictions: (i) `rho_cell` at
  the razor is `< 2^-6e11` (astronomically sub-1); (ii) every
  exhaustively reachable small cell has `rho_cell >= 1`; (iii) at
  `(n,k,a,q) = (7,2,4,11)` the measured max over ALL column-far
  2-planes lies in **[6,12]**, i.e. **exceeds `r+1 = 4`**;
  (iv) `a-k = 1` cells are degenerate (`rho_cell = C(n,a)` independent
  of `q`) and must be excluded — I register in advance that round-31's
  `(8,4,5)` and `(6,3,4)` type cells are `a-k = 1` and therefore have
  **zero power** for the razor. P(iii) = 0.8.
- **PR-H (the crossing).** I register that I will NOT claim the crossing
  moves. Even `B_ca^far = n-a+1` exactly would give `2^39.9773` against
  the `2^128` budget with 88.02 bits of room — but that is a
  CONJECTURE, and the round's deliverable is not permitted to inherit
  it as a bound.
- **PR-I (the 2^216 target).** Prediction: the a-set counting bound
  (`for a column-far pair, each `a`-subset carries at most ONE bad
  slope, because both syndromes vanishing on it is exactly
  column-closeness') gives `T <= C(n,a) = 2^{2.199e12}`, which is
  worse than `2^216` by ~10 orders of magnitude in the exponent.
  Hence NO counting-over-`a`-sets argument can reach `X < 216`.
  P = 0.90. I also predict I will have to grep for the provenance of
  `2^216` and that it is NOT of the form `C(n,a)`.

### Zero-power declarations (registered in advance)

1. Sampled negatives prove nothing; any "no configuration found" is
   reported as a sampled negative with its sample count.
2. Constructions are LOWER bounds only; no constructed maximum is
   reported as an upper bound.
3. Exhaustive plane enumeration is only possible in the `rho_cell >= 1`
   regime; the razor's regime (`rho_cell << 1`) is **not exhaustively
   reachable at any cell inside the compute law**, and I register that
   in advance rather than discovering it as a result.
4. `a-k = 1` cells have `rho_cell` independent of `q` and are declared
   zero-power for the razor before any run.

### Compute plan

`d1_prices.py` (tiny, exact integers, all thresholds/ratios above);
`d3_planes.py` (local, exhaustive 2-plane enumeration in syndrome
space via RREF Schubert cells, per-plane cost `C(n,n-a)` projections,
checkpointed to a results file). Stdlib only. No banked script is run;
anything reused is re-implemented in my own directory.
