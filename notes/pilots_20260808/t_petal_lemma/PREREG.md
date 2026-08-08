# PRE-REGISTRATION — THE T-PETAL OVERLAP-CAP LEMMA: PROVE OR REFUTE (round 24)

Round 24, 2026-08-08. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: the board's highest
single-lemma leverage, doubly confirmed. THE LEMMA: for two
distinct primitive members (F, W), (F', W') of the t-petal slice,
|Z(F) cap Z(F')| <= e - 1 (e = 2d+1-t*ell the flat dimension
parameter). PROVED verbatim at t = 2 (the cofactor determinant,
2s = e-1) and t = 3 ((PJ2) via the mu-basis). If it lands at
t >= 4: the entire precomputed Johnson sieve becomes legal (408
residual rows -> the t < M, J > 0 cells removed at a stroke),
mystery 7's undecided red is decided, and red 3 gets its first
real instrument. If it is FALSE at some t >= 4: equally decisive —
the sieve is illegal and red 3's re-pose must route around it.

## 0. Sources (quote verbatim first)
- The two proved cases: the t = 2 cofactor determinant
  (l1_fpc5_ratehalf_m4_t2_joint_support_distance (JD1) and the
  two_full_petal slice reduction) and t = 3
  (pma_three_petal_projective_johnson_bound (PJ2) +
  pma_three_petal_mu_basis_reduction) — quote the proofs' actual
  mechanisms with file:line; identify EXACTLY what each uses that
  might not generalize (the mu-basis is a THREE-petal object; the
  cofactor determinant is a TWO-petal object).
- critical/nodes/l1_fpc5_large_source_payment/statement.md +
  round-23/23b addenda (the 408-row residual; the missing t >= 4
  injection; H3: t <= M always).
- notes/pilots_20260807/fpc5_diag/ (fpc5_exact.py — the sieve
  that consumes the lemma, coordinator-replayed) and
  notes/pilots_20260807/mf_wall_adversary/ (the 142/266 split).

## 1. Deliverables
- (D1) THE PROOF ATTEMPT, structured: (a) write the t-petal slice
  system explicitly (t congruences L_i | (W - c_i F) on (F, W),
  deg <= d); (b) attempt the syzygy/cofactor-determinant argument
  at general t — derive where the t = 2 mechanism (the resultant
  of the two cofactor relations) does or does not extend when
  there are C(t,2) pairwise relations; (c) attempt the mu-basis
  route — does a t-petal analogue of the 3-petal mu-basis exist
  (the module of syzygies of t forms — its expected rank/degrees
  by Hilbert arithmetic), and does (PJ2)'s argument only need the
  degree bound? Every step PROVED or labelled with the exact gap.
- (D2) THE REFUTATION ATTEMPT (mandatory, in parallel): exhaustive
  toy search for violating pairs at the smallest t = 4 cells
  (build the 4-petal slice explicitly at toy (ell, q) — the
  round-23 bucketing machinery adapts; REUSE rh_bucket.py /
  ls6_bucket.py); search pairs for |Z(F) cap Z(F')| >= e.
  Register the cells and the escape test in advance. A violating
  pair is a full falsification of the lemma — verify exactly,
  reproduction script, headline.
- (D3) THE PAYOFF EXECUTED (only if (D1) lands a proof): re-run
  the sieve (fpc5_exact.py) with the lemma flagged legal at the
  proved t range; print the NEW residual row count vs 408; state
  exactly which cells die. If the proof covers only some t range
  (e.g. t <= T0), print the residual under partial legality.
- (D4) THE VERDICT: PROVED (with the write-up at proof standard —
  the coordinator replays and mints) / REFUTED (witness + what
  red 3's re-pose must become) / PARTIAL (the exact t range +
  the named gap + the next decisive step).

## 2. Falsifiers / honesty
- The refutation search runs REGARDLESS of proof progress — a
  proof believed before the search completes is not banked.
- Toy search maxima are lower bounds; exhaustiveness claims only
  where the enumeration is complete (declare completeness class
  per cell).

## 3. Rules
- DRAFT ONLY in notes/pilots_20260808/t_petal_lemma/. Never edit
  dag.json/nodes/tools; no git; no Modal; stdlib only. COMPUTE
  LAW: every python3 invocation via tools/ramguard tiny|local --
  python3 ... (literal --), from repo root, INCLUDING file
  patching and JSON peeking. 2-power grids where yours to choose;
  official-arithmetic-shaped cells where the object demands
  (declare which); name every measured functional (CATCH-19C).
  Verbatim quotes with file:line. No REPORT.md — your final
  message IS the report. QUARANTINE: do not read
  notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line 3173
  (the "ROUND 24 LAUNCHED" marker); do not read the other
  round-24 pilot dirs (z_ceiling_assault, kernel_window_hunt,
  c2pp_gb_probe); PASS THIS QUARANTINE CLAUSE VERBATIM to any
  subagent you dispatch.


# PILOT REGISTRATIONS

Appended 2026-08-08 by the Opus pilot BEFORE any computation (no
python3 has been run at the time of this append; only file reading
has occurred). Sections 0-3 above are the coordinator's brief; this
section is mine and is binding on what follows.

## R0. State of knowledge at registration time (declared, not hidden)

I did the section-0 source read FIRST, as the brief orders. Two
things were established by reading alone, before any computation,
and I register them here so that nothing below can be mistaken for
a post-hoc reconstruction:

- **(R0a) I derived the general-`t` proof by hand from the two
  proved cases.** The mechanism is the 2x2 cross-determinant
  `Delta = F W' - F' W`: each `L_i` divides `Delta` because
  `W = c_i F` and `W' = c_i F'` mod `L_i`; hence
  `Lambda = prod_i L_i` divides `Delta`; `deg Delta <= 2d` so the
  cofactor has degree `<= 2d - t*ell = e - 1`; common core roots
  are roots of the cofactor because core and petals are disjoint.
  Nothing in this uses `t = 2` or `t = 3`.
- **(R0b) A subtraction sweep (hard law 5) found the argument
  ALREADY PROVED IN THIS REPO at arbitrary support size**, in
  `background/nodes/l1_fixed_support_defect_johnson_bound/`
  ((JB3), status PROVED, with `verify.py`). The board's belief that
  "NO mu-basis / overlap-cap theorem exists for t >= 4"
  (`critical/nodes/l1_fpc5_large_source_payment/statement.md:30-32`)
  is therefore a **bookkeeping failure, not a mathematical gap**.

Consequently the honest shape of this pilot is NOT "find a proof"
but "(i) confirm the banked general-`t` proof line by line, (ii)
confirm the FPC5 `t >= 4` slice actually satisfies its hypotheses,
(iii) run the mandatory refutation search anyway, (iv) execute the
payoff". I register that reframing now rather than discovering it
later.

## R1. Proof-attempt plan, with checkpoints (D1)

Each checkpoint is PASS/FAIL and is reported whatever it returns.

- **(C1) Slice write-out.** Write the `t`-petal slice explicitly:
  `V = {(F,W) : deg F, deg W <= d, L_i | (W - c_i F), i=1..t}`,
  `L_i` pairwise coprime monic of degree `ell`, `c_i` in `K`,
  petals disjoint from the core `C`. Record `e = 2d+1-t*ell` and
  the expected dimension `e+1` (`2(d+1) - t*ell`).
  PASS iff the write-out matches the `t=2` and `t=3` node
  definitions verbatim at `t=2,3`.
- **(C2) Cross-determinant divisibility.** Prove
  `Lambda | (F W' - F' W)` for any two members. PASS iff proved
  with no `t`-dependent step.
- **(C3) Nonvanishing.** Prove `F W' - F' W != 0` for distinct
  primitive members. Register in advance the exact hypothesis this
  needs; if it needs `deg F = d` monic rather than `deg F <= d`,
  SAY SO and use the monic form.
- **(C4) Degree ledger.** `deg cofactor <= 2d - t*ell = e-1`.
- **(C5) Transfer to the common core roots.** Common roots of
  `F, F'` lie off the petals, hence are roots of the cofactor.
  PASS iff core/petal disjointness is the only extra hypothesis.
- **(C6) Syzygy/mu-basis route, honestly adjudicated.** State
  whether the `t=3` mu-basis is NEEDED (my prediction, registered
  now: it is NOT; it is a detour, and (PJ2) is the image of (C2)-(C5)
  through the (DET) identity). PASS iff I can exhibit the
  identity `Delta = kappa * H_12 * Lambda` that makes (PJ2) a
  corollary. FAIL if the mu-basis contributes an irreplaceable step.
- **(C7) Rank arithmetic at t >= 4 (the registered danger).** The
  syzygy module of `(L_1..L_t)` has rank `t-1`, so the `t=3`
  dimension formula `dim V = e+1` need NOT survive at `t >= 4`.
  Register in advance: **if `dim V != e+1` at `t >= 4`, does the
  overlap cap still hold?** My prediction: YES, because (C2)-(C5)
  never mention the dimension. This is the single most likely place
  for me to be wrong and I will report the measured `dim V` at
  every computed cell whether or not it equals `e+1`.
- **(C8) Hypothesis-transfer audit.** The banked (JB1) hypotheses
  are: `F = L_D` monic of degree exactly `d`, `D subset C`,
  `deg W <= d`, `gcd(F,W)=1`, `W(x)=alpha(x)F(x)` on `X`, `X`
  disjoint from `C`, and **both members carry the SAME labelling
  `alpha`**. The `t`-petal slice is the sub-case `alpha = c_i` on
  petal `i`. PASS iff every one of these holds in the FPC5
  large-source `t >= 4` cells; any that fails is a GAP and is
  reported as such, not waved through.

## R2. Refutation search (D2) - cells, functionals, escape test

Runs to completion **regardless of proof progress**. A proof
believed before the search completes is not banked.

**Object.** `q` prime (the object demands a finite field; I use
prime fields so the arithmetic is stdlib-exact). Petals
`P_1..P_t` pairwise disjoint subsets of `F_q^*` of size `ell`,
`L_i = prod_{x in P_i}(X-x)`; labels `c_1..c_t` distinct in `F_q`;
core `C` disjoint from every petal, `N = |C|`.
`V` computed as an EXACT kernel over `F_q` (rref, no floating
point). `e = 2d+1-t*ell`.

**Grid declaration (CATCH-19C).** `q` must be prime, so a 2-power
grid is not available on `q`. On the free geometric parameters I do
NOT use a 2-power ladder either, and I declare why: the lemma is a
per-cell algebraic identity with no asymptotic content, so an
EXHAUSTIVE sweep of a full small window is strictly more
informative than a sparse ladder. Window registered now:
`t in {4,5,6}`, `ell in {1,2,3}`, `d` over the whole upper strip
`d < t*ell <= 2d` (equivalently `e >= 1` and `t*ell > d`),
`q in {11,13,17,19,23,29,31,37,41,43}` subject to
`q > N + t*ell + 1`, `N in {d, ..., d+6}`.

**Registered functionals (CATCH-19C), named before measurement:**
- `NMEM`   = number of distinct primitive split members of the
             cell (F monic degree `d`, `d` distinct roots in `C`,
             `gcd(F,W)=1`).
- `MAXOVL` = max over distinct member pairs of
             `|Z(F) cap Z(F')|`.
- `CAP`    = `e-1`, the claimed bound.
- `SLACK`  = `CAP - MAXOVL` (may be negative; negative IS the
             refutation).
- `DIMV`   = exact `dim_K V` (to test C7 against `e+1`).
- `DIVOK`  = 1 iff `Lambda * L_I` divides `F W' - F' W` for EVERY
             checked pair (`I` the common root set).
- `DEGCOF` = max over pairs of `deg((F W' - F' W)/Lambda)`.
- `NJOHN`  = the (JB4)/(PJ4) prediction
             `floor(N(d-CAP)/(d^2-N*CAP))` where the denominator
             is positive, compared against `NMEM`.

**ESCAPE TEST (registered in advance, binding).**
The lemma is REFUTED at `t` iff a cell in the registered window
produces a pair of distinct primitive members of the SAME cell
(same petals, same labels) with `|Z(F) cap Z(F')| >= e`, i.e.
`SLACK < 0`, verified exactly (integer arithmetic mod a prime,
no sampling) and reproduced by a standalone script. Any such pair
is a full falsification and becomes the headline.

**POWER CONTROL (mandatory - a search that cannot fail is not a
search).** The same searcher is run on three deliberately BROKEN
arms, and I register now that the search is uninformative unless
at least one broken arm produces `SLACK < 0`:
- `BRK-PRIM`: drop the `gcd(F,W)=1` filter.
- `BRK-DISJ`: let the core overlap a petal.
- `BRK-LABEL`: pair members drawn from cells with DIFFERENT label
  vectors (so they do not share `alpha`).
If all three broken arms still show `SLACK >= 0`, I will report the
search as HAVING NO POWER rather than as confirming the lemma.

**Arm 3 (identity arm, no split requirement).** Independently of
the split enumeration, draw random pairs from `V` at larger
`(t, ell, d, q)` and check `DIVOK` and `DEGCOF <= e-1` directly.
This tests the proof's engine at `t` well beyond the exhaustive
window.

## R3. Completeness classes (declared per cell, per falsifier 2)

- **CLASS-E (exhaustive).** Every projective point of `V` is swept
  (directly, or by the round-23 last-coordinate bucketing which is
  exhaustive by construction) and ALL member pairs are compared.
  Only CLASS-E cells may carry an "exhaustive, no violating pair"
  claim.
- **CLASS-B (bucketed-exhaustive).** Swept by the `ls6_bucket` /
  `rh_bucket` last-coordinate trick; exhaustive over the chart iff
  the script's own `swept == q^(dim-1)` check passes. Reported with
  that check's value.
- **CLASS-S (sampled).** Random draws only. Maxima from CLASS-S
  cells are LOWER BOUNDS on `MAXOVL` and can only ever refute,
  never confirm.

## R4. Payoff (D3) and verdict (D4)

- Payoff runs ONLY after the refutation search has completed and
  returned no violating pair. It re-runs `fpc5_exact.py`'s sieve
  with the lemma flagged legal at the proved `t` range and prints
  the NEW residual row count against the standing 408, naming
  exactly which cells die.
- Verdict is PROVED / REFUTED / PARTIAL-with-exact-`t`-range. No
  status flips, no closure claims; the coordinator replays and
  mints. If the answer is "already banked", the deliverable is the
  citation plus the hypothesis-transfer audit (C8), and I will say
  plainly that the pilot's contribution is bookkeeping, not
  mathematics.

## R5. Self-correction protocol

Every place where a prediction registered above turns out wrong is
stated in the final report in plain language, with the registered
prediction quoted next to the measurement.
