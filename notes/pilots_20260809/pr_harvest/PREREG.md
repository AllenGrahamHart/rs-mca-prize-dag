# PRE-REGISTRATION — PR RE-HARVEST vs THE CURRENT BOARD (round 25a)

2026-08-09. Coordinator brief; the pilot appends registrations
BEFORE any computation. MANDATE: the upstream queue has no new PRs,
but OUR BOARD has changed since the last triages (2026-07-27
lit-map; 2026-08-03 maelcar audit): mystery 7 exists (the
dimension-uniform split-locator max-to-mean wall); the FPC5 J-sieve
is LEGAL at every t (the overlap cap = (JB3)); red 3's t >= 4 rows
are POSABLE (dim V = e+1); the constant-weight instrument cluster
is the mystery-2+4 convergence point; CONJECTURE Z-CEILING exists
(C >= 1.7681); the family-uniform emptiness is FALSE with the
narrowing pending. Re-triage the external PRs against THIS board
and execute the never-run action items.

## 0. Sources
- The prior triages (READ FIRST — do not redo what they settled):
  notes/pilots_20260803/maelcar_audit/AUDIT.md (verdicts F1-F11 +
  the action list; items 1-3 executed as SOL_TARGET_4; items 6, 8
  NEVER RUN) and notes/literature_map_20260726/ (ACTIONS.md first).
- The PRs: maelcar's #1145-#1148 via the LOCAL refs in
  /home/u2470931/smooth-read-solomin/rs-mca (branches pr1145..pr1148;
  read file-at-a-time with `git -C <repo> show pr114X:<path>` — NO
  checkouts, NO bulk reads; RAM discipline is binding).
- The current board: the round-23/24 addenda on the three FPC5
  reds, l1_fixed_support_defect_johnson_bound (the JB identification),
  the dli_wcl_slot_* battery, x4_primitive_star_u1_coverage + the
  SP crosswalk (upstream_sp_coefficient_scale_quotient_sieve),
  f2_z1_mass_knife_edge round-24 update, roadmap section 12 r5.

## 1. Deliverables
- (D1) EXECUTE the two never-run action items from the 08-03 audit:
  (#6) THE THEOREM-J CHECK: translate #1146's ell=11 exact-five row
  to our (n, k, s) coordinates and test s^2 > n(k-1) — does our
  newly-LEGAL J-sieve dominate, partially dominate, or miss their
  S6 <= 20 result? Exact arithmetic, both directions stated.
  (#8) THE BRIDGE STATUS: does rate_half_list_chamber_affine_rank_
  bridge (or a successor) now exist / have the locator-to-codeword
  map that would let #1148's hull-rigidity atlas be priced for our
  M31/LIST lane? If yes, run the hypothesis match; if no, state
  what the bridge must supply.
- (D2) RE-TRIAGE #1145-#1148 against the NEW board objects
  (mystery 7 / the legalized sieve / posable red-3 rows / the
  constant-weight cluster / Z-CEILING / the WCL slot battery):
  for each PR, a claims-to-lanes matrix (applies / fails-because /
  newly-relevant-since) — flag ONLY genuinely new matches; the
  prior verdicts stand unless a named board change re-opens them.
- (D3) HARVEST CANDIDATES, concretely: for each match, the exact
  import shape (ev-satellite node / instrument transport / a
  replayed certificate) + what must be verified before adoption
  (the house law: upstream enters PROVED only when OUR replay
  earned it). Execute the CHEAP replays now (their Python
  auditors re-ran clean on 08-08; anything beyond needs listing,
  not running).
- (D4) A one-pass scan of the REMAINING open queue (#1121-#1143,
  ours + Scott's) for anything the current board makes newly
  load-bearing that the waves have not already absorbed — expected
  answer "nothing" (ours came from our DAG; Scott's are absorbed);
  verify, don't assume.

## 2. Rules
- DRAFT ONLY in notes/pilots_20260809/pr_harvest/. Never edit
  dag.json/nodes/tools; no git writes; no Modal; stdlib only.
  COMPUTE LAW: every python3 via tools/ramguard tiny|local --
  python3 (literal --) from the prize repo root, INCLUDING file
  patching and JSON peeking. RAM DISCIPLINE: file-at-a-time git
  show; no checkouts; no directory-wide loads. Reading the sibling
  checkout /home/u2470931/smooth-read-solomin/rs-mca is PERMITTED
  (read-only). Do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  Verbatim quotes with file:line. No REPORT.md — your final message
  IS the report, with every claim labelled (PROVED-replayed /
  MATCHED / CANDIDATE / NOT-OUR-LANE-still).

---

# PILOT REGISTRATIONS

Appended 2026-08-09 by the Opus pr_harvest pilot BEFORE any `python3`
ran. Everything above this header is the coordinator's brief; everything
below is mine. Orientation reads that preceded this append (declared, so
nothing here is post-hoc): `notes/pilots_20260803/maelcar_audit/AUDIT.md`
(all 556 lines), `critical/nodes/l1_program_frontier/statement.md`,
`background/nodes/l1_fixed_support_defect_johnson_bound/statement.md`,
`notes/roadmap/sections/12-r3-2-board-revision.md:487-540` (the r5
mystery-7 promotion), `notes/pilots_20260808/t_petal_lemma/REPORT.md`,
`notes/pilots_20260808/z_ceiling_assault/REPORT.md`,
`notes/pilots_20260807/cw_shared_target/FABLE_AUDIT.md`, and
`git diff --name-only main...pr114X` on the four branches (file NAMES
only; no file contents from the PRs read yet).

## R0. A FRAMING CORRECTION TO THE BRIEF, REGISTERED BEFORE COMPUTING

The brief calls audit action items #6 and #8 "NEVER RUN". Item #6 was
in fact **already run on 2026-08-07** and its result is banked on the
node: `critical/nodes/l1_program_frontier/statement.md:24-43`
("**Domination check resolved (2026-08-07).**" ... "Theorem J does not
cover #1145/#1146."). I register this *before* re-deriving anything, so
that my contribution is not mistaken for a first execution.

Therefore I re-scope D1(#6) into three parts and predict each:

- (#6-a) **AUDIT the banked 08-07 resolution** by re-deriving it from
  #1145/#1146's own note (not from the addendum), on every one of the
  six certified padded rows.
- (#6-b) **THE ACTUALLY-NEW TEST.** The 08-07 check used *Theorem J*'s
  functional `s^2 - n(k-1)`. The named board change since is that the
  **defect-side** Johnson functional `(JB3)/(JB4)` of
  `l1_fixed_support_defect_johnson_bound` is now known legal at EVERY
  `t` (round-24 addendum, `statement.md:84-98`). That is a *different*
  functional and it was never applied to their row. Running it is the
  genuinely new work.
- (#6-c) the direction the audit never stated: does anything of THEIRS
  dominate the JB sieve on the rows where the JB sieve is vacuous?

## R1. THE THEOREM-J TRANSLATION PLAN + PREDICTED OUTCOME

**Translation (registered):** background-free coset sunflower at
`ell = 11`, row parameters `(tau, m)`; the six certified padded rows are
`(tau,m) in {(6,8),(6,9),(6,10),(7,9),(7,10),(8,10)}`
(`AUDIT.md:54-55`). Dictionary to `(n,k,s)`:

```text
k - 1 = m*ell,     s = (m+1)*ell,     n >= (m+tau)*ell     (minimal support domain)
```

**P1a (Theorem J clause 2, ordinary Johnson).** On the minimal domain,

```text
s^2 - n(k-1) = ell^2 * (1 - m(tau-2))
```

predicted EXACT values (ell=11, ell^2=121):

```text
(tau,m)=(6, 8):  121*(1-32) = -3751
(tau,m)=(6, 9):  121*(1-36) = -4235
(tau,m)=(6,10):  121*(1-40) = -4719
(tau,m)=(7, 9):  121*(1-45) = -5324
(tau,m)=(7,10):  121*(1-50) = -5929
(tau,m)=(8,10):  121*(1-60) = -7139
```

all six strictly negative; enlarging `n` only decreases it. PREDICT:
**Theorem J clause 2 MISSES all six rows.**

**P1b (Theorem J clause 1, unique decoding).** `2s > n+k-1` becomes
`2(m+1)ell > (2m+tau)ell`, i.e. `tau < 2`. PREDICT: **fails for every
certified row (all have tau >= 5); clause 1 misses too.**

**P1c (verdict, registered in advance):** *neither dominates nor
partially dominates — Theorem J MISSES*. If P1a/P1b come out as
predicted this is a CONFIRMATION of the banked 08-07 addendum by an
independent re-derivation, not a new result, and I will say so.

## R2. THE NEW TEST — (JB4) APPLIED TO #1146's ROW (the board change)

Mapping registered in advance (to be checked against their note, not
assumed): `N = |C| = k-1 = m*ell`; petal support `X` = the `tau` fibres,
`h = |X| = tau*ell`; `d` = defect degree; background-free means `b = 0`,
`g = ell = 11`, so the list threshold `h >= d+g` gives `d <= (tau-1)*ell`.
Then `(JB2)` `r_J = 2d - tau*ell` and `(JB4)` fires iff
`J := d^2 - N*r_J > 0`, i.e. `d^2 - 2*m*ell*d + m*tau*ell^2 > 0`.

**P2a (the crossover).** The sieve fires exactly for `d` below the
smaller root `d* = m*ell - sqrt(m^2 ell^2 - m*tau*ell^2)`. Predicted at
`tau = 6`:

```text
m= 8:  d* = 88 - sqrt(7744) = 88 - 44     = 44      (exact integer)
m= 9:  d* = 99 - sqrt(3267) ~ 99 - 57.157 = 41.843
m=10:  d* = 110 - sqrt(4840) ~ 110-69.570 = 40.430
```

so the sieve is LEGAL-AND-NONVACUOUS for `d <= 43 / 41 / 40` and vacuous
on `44..55 / 42..55 / 41..55` respectively (upper limit `d <= 55`).

**P2b (the bound at the boundary).** At `m=8, tau=6, d=43`:
`r_J=20`, `J=1849-1760=89`, `(JB4)` gives `|Z| <= 88*23/89 = 2024/89 =
22.74...`, i.e. `<= 22`. PREDICT: **the JB sieve is WEAKER than their
`S_6 <= 20` at the top of its range but of the same order**, and
strictly stronger well below it (predict `<= 6` at `d = 40, m = 8`).

**P2c (the verdict I predict).** **PARTIAL DOMINATION IN ONE DIRECTION
ONLY, and it is OURS that is partial:** our newly-legalized sieve covers
the low-defect range with a field-independent, `ell`-uniform bound;
#1146 covers *all* `d` including the sub-Johnson tail `d in [d*, 55]`
where our functional is undefined — but only for 2 of 252 supports and
only at `ell = 11`. Predicted headline: *neither dominates; they are
complementary on disjoint `d`-ranges.*

**P2d (falsifier, registered).** If `J > 0` holds at `d = 55` for any
certified row, P2a/P2c are wrong and the JB sieve dominates #1146
outright. I predict this does NOT happen.

**P2e (hypothesis-transfer audit, registered as the place I am most
likely to be wrong).** `(JB1)` needs: `F = L_D` monic with `D subset C`;
`deg W <= d`; `gcd(F,W) = 1` (primitivity); `W = alpha F` pointwise on
`X` with `alpha` the received word; `X` disjoint from `C`. I predict
**H-PRIM (`gcd(F,W)=1`) is the one that fails to transfer cleanly** to
their coset-sunflower family, because their `Gamma` is a fixed
five-term lacunary polynomial and nothing in their setup imposes
primitivity of the member pairs. If it fails, the whole of R2 becomes a
CANDIDATE ANALOGY, not a comparison, and I will report it as such.

## R3. THE #1148 BRIDGE STATUS (audit item #8) — PLAN + PREDICTION

Steps: (i) locate `background/nodes/rate_half_list_chamber_affine_rank_bridge`
and read its statement/addenda; (ii) grep the whole `nodes` surface for a
successor supplying a locator-to-codeword incidence map (search terms:
`locator`+`codeword`, `incidence`, `chamber`, `crossing`, `atlas`); (iii)
if absent, state exactly what the bridge must supply.

**P3a.** PREDICT **NO** — no locator-to-codeword map exists and no
successor node has been minted since 2026-08-03; the fence still stands
and #1148 still cannot be priced for M31/LIST.
**P3b.** PREDICT the missing object is: *a map sending a split
degree-479 locator in the flat to the codeword(s) whose error support it
is, with a cardinality-preserving (or cardinality-bounding) fibre count*
— i.e. the pricing needs `#codewords <= f(#split locators)`, and the
fence's 08-03 finding was that the repo has no such `f`.

## R4. THE RE-TRIAGE MATRIX SKELETON (D2)

One row per (PR, board-object) pair. Board objects, named:

```text
B1  mystery 7 (dimension-uniform split-locator max-to-mean wall)
B2  the J-sieve legalized at every t via (JB3)/(JB4)
B3  red 3's t >= 4 rows posable (SLICE-DIMENSION THEOREM dim V = e+1)
B4  the constant-weight instrument cluster (mystery-2 + mystery-4
    convergence on ONE OBJECT, two targets)
B5  CONJECTURE Z-CEILING (round-24 re-posing, C >= 1.7681) + THEOREM RC
B6  the family-uniform emptiness FALSIFICATION (N'=256), narrowing pending
```

Verdict vocabulary, fixed in advance: **APPLIES** (a named board change
makes their claim load-bearing for a named node of ours) / **FAILS-
BECAUSE** (re-opened and re-closed, with the reason) / **NEWLY-RELEVANT-
SINCE** (adjacency created by a named board change, not yet load-bearing)
/ **NOT-OUR-LANE-still** (prior verdict stands; no named change touches
it).

**P4a (the one match I expect to find).** `#1148 x B1`: their theorem is
literally *"the affine hull of 16 monic degree-479 split locators meets
the split locus in exactly those 16"* — a **max-to-mean statement about
split locators in a linear flat of projective dimension 15**, which is
mystery 7's object verbatim. PREDICT **NEWLY-RELEVANT-SINCE (B1)**, and
that it pairs with our own opposite-direction PROVED
`l1_m31_fixed_support_divisor_direction_cap_route_cut` (6-dim flat,
67,449 split divisors) to give the **first two-point calibration of the
dimension-uniformity question**: one flat of dim 6 with 67,449 split
members, one of dim 15 with 16. PREDICT this does NOT close mystery 7
and does NOT flip any status — it is an instrument calibration.
**P4b.** PREDICT `#1146 x B2` = **APPLIES (partial, complementary)** per R2.
**P4c.** PREDICT `#1145 x B3` = NOT-OUR-LANE-still (their slices are
coefficient-support slices, not `(F,W)` saturated slices) — but I flag
in advance that I could be wrong here and will test the `dim V = e+1`
shape against their 465/630-cell counts before saying so.
**P4d.** PREDICT `#1147 x B5` and `#1147 x B4` = NOT-OUR-LANE-still
(Paper-D quartic trades share no object with ternary kernels or with
constant-weight BCH populations).
**P4e.** PREDICT `#1147 x SOL_TARGET_4` is UNCHANGED-AND-STILL-OPEN: the
bridge `T_4^{smooth,ordered} = 2n T_sm` and flag F10 stand; no board
change since 08-03 touches them; the decisive row `(256,769)` is still
not run. I will re-check whether F10 was ever acted on and say so.
**P4f (registered non-expectation).** I do NOT expect any of the four
PRs to move `#1148 x B6` or `#1145/#1146 x B4`.

## R5. THE REPLAY LIST (house import law)

I will re-run, from a `git show`-extracted copy inside my pilot dir only,
the auditors whose OUTPUT my claims depend on — nothing else:

```text
must-run (my claims rest on them):
  R5.1  pr1146: experimental/scripts/audit_p04cw_parity_uniform_S6_theorem.py
        (the S_6 <= 20 constant I am comparing against)      ~83 s expected
  R5.2  pr1148: .../C_verify_SP01zxab_full_affine_hull_synthesis.py
        (the 16-in-dim-15 numbers mystery 7 would calibrate on)  ~46 ms
  R5.3  pr1148: .../A_verify_SP01zxaa_Schur_power_profile.py
        (the (16,136,509) profile = the flat's dimension datum)  ~20 s
  own:  R5.4  my own exact-rational (JB4)/(Theorem J) evaluator, stdlib
        Fraction only, from their note's parameters.
list-only, NOT run (compute law / cost):
  L1  all #1148 partition sieves (10,694,457,224 normals; C++/HPC)
  L2  #1145 p04cu_ell11_exact_five_spectrum_probe.cpp (the census)
  L3  #1146 derive_p04cw_*.py SymPy reduction stages (exhaustiveness)
  L4  #1147 p06b3v_product_pair_and_cross_ratio_probe.cpp (max C_r=5789)
  L5  the decisive SOL_TARGET_4 row N=256,q=769 (C(256,4)=174,792,640)
```

If an extraction turns out to need a certificate JSON larger than ~20 MB
I will SKIP the replay rather than break RAM discipline, and label the
dependent claim UNREPLAYED.

## R6. THE QUEUE SCAN (D4) — method + predicted answer

Method: `gh pr list` read-only if the CLI authenticates; otherwise the
local record (`notes/PR_SWEEP_20260803.md`, the wave-integration notes,
and the local `pr1140/pr1141/pr1144b` refs). For each of #1121-#1143 I
check only one question: *does a NAMED board change from R4's B1-B6 make
it load-bearing in a way the waves did not already absorb?*
**P6.** PREDICT **"nothing"** — ours came from our own DAG (so they are
absorbed by construction) and Scott's were absorbed in waves 19-24. I
register in advance that a null result here is the expected result and
will not be dressed up.

## R7. COMPLIANCE PINS

All `python3` via `tools/ramguard tiny|local -- python3` from
`/home/u2470931/smooth-read-solomin/prize`. Stdlib only. No Modal. No
git writes. All writes confined to
`notes/pilots_20260809/pr_harvest/`. PR files read one at a time with
`git -C ../rs-mca show pr114X:<path>`; no checkout; no bulk directory
read; `dag.json` never loaded whole (grep / shard reads only).
`notes/pilots_20260802/CAMPAIGN_LEDGER.md` not read, and the quarantine
clause is passed verbatim to any subagent. No status flip and no
adoption into `dag.json` will be claimed. This registration block was
appended with the `Edit` tool (no `python3` involved), so the compute
law is not engaged by the append itself.
