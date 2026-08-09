# PREREG — m7_falsifier_hunt (round 26)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

Round 25 (m7_complement_repose) killed the symmetric-difference
re-pose as a mystery-7 route and REGISTERED A FALSIFIER to keep the
kill checkable: **exhibit one FPC5 rate-half or large-source cell,
satisfying its node's own admissibility conditions, whose GUARDED
split members have either a nonempty common root core (kappa >= 1)
or |U| < 2d** — either puts the cell on the winning side of the
sigma < 2a threshold and reopens the route. The kill report named the
cheapest hunting ground: **the M >= 5 large-source charts legalized
by the round-25 CJ transfer audit, where the background capacity b
can approach ell** — and explicitly did not test them. Your job:
hunt there. Either outcome is bankable — a witness reopens a route on
mystery 7; a hunted-and-empty verdict hardens the kill from
"untested" to "hunted". Sources to read FIRST:
notes/pilots_20260809/m7_complement_repose/{REPORT.md,FABLE_AUDIT.md,
PREREG.md, d2_arm_a.py, d4_cj3_audit.py}; the round-25 sections on
critical/nodes/l1_fpc5_large_source_payment/statement.md and
background/nodes/l1_rootfree_rational_q_projective_packing/statement.md.

## Deliverables

**D1 — THE CHART FAMILY.** Identify which of the 71 CJ3-rescued rows
(and the wider 408-row residual grid) have M >= 5 cells that are (i)
inside the node's own admissibility (the round-24 u <= b correction =
the list threshold h >= d+g — get this exactly right; round 25 flagged
an out-of-family measurement (4,1,1) on the sibling node as a
cautionary tale), and (ii) exactly enumerable at small q under the 1G
wall. Register the accessible cell list and the q grid BEFORE
enumerating. If NO admissible cell is exactly enumerable, that is
deliverable D1's honest answer — price the cheapest reachable
approximation and STOP for re-brief rather than substituting an
uncontrolled sample.

**D2 — THE MEASUREMENT.** At each accessible cell: enumerate the
guarded split members (full contributor filters — primitivity +
whatever the node's own guards are at this M; name them from the node
text, do not import the m4_t2 guards blindly), and measure exactly:
kappa = |common core|, |U| vs 2d, the full pairwise-overlap
distribution, PENCIL_MAX, and MAXPACK where exhaustible. The round-25
measurement discipline applies: per-config data, no merged-histogram
aggregation without disaggregation (the round-25 pilot's
self-correction 2).

**D3 — THE VERDICT.** Registered in advance:
- kappa >= 1 or |U| < 2d at an ADMISSIBLE cell: the falsifier FIRES —
  the complement orientation beats the direct one there; compute both
  anticode numbers and the measured truth, and state what reopens.
- All accessible cells on the losing side: the kill hardens; report
  the margin (sigma/2a per cell) so the silence has numbers.
- Also measure: does b -> ell actually push kappa up, as the round-25
  intuition suggested? The TREND is bankable even if no cell fires.

**D4 — RED 3 MEMBERSHIP (if budget remains).** The slice-dimension
theorem (dim V = e+1, banked round 24) made the t >= 4 rows POSABLE AS
FLATS, so the large-source red's mystery-7 membership is DECIDABLE:
run the round-23b repaired method test (max-to-mean at matched
dimension) on the t >= 4 flats at one or two accessible cells. A
decided membership settles the board's one UNDECIDED red. Reuse the
fpc5_diag machinery; power-control before use, per the 23b standard.

## Escape tests (run before the main work)

- Replay d4_cj3_audit.py (expect 71/408, fraction 0.01969549 — the
  coordinator's replay was byte-identical; yours must be too).
- Reproduce one round-25 arm-A config (ell=4, q=97, seed 20260809)
  summary numbers before trusting your own enumeration code at M >= 5.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md at
  or below line 3872; do not read any other round-26 pilot dir
  (b_sparsity_pose, umin_spike_hunt, freeze_tail_law). Pass this
  clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT may
  extend a wall; document it.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no bulk
  loads; checkpoint long enumerations; background batches with
  results files for >10-min runs.
- DRAFT-ONLY: writes only in notes/pilots_20260809/m7_falsifier_hunt/;
  no dag/nodes/tools writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing; misses
  first. Name every measured functional (CATCH-19C). 2-power config
  grids where the grid is yours. No shift-0 cells. Own-repo grep
  before claiming any lemma is missing (CATCH-24A).
- Your final message IS the report. End with a compliance paragraph.

## Pilot registrations (appended by the pilot before any computation)

Appended by the Opus pilot (codename m7_falsifier_hunt) with the `Edit`
tool BEFORE any interpreter ran. Nothing below was informed by a
measurement; the arithmetic in R1 was done by hand from the node texts
and is to be VERIFIED by the D1 scan (which may add or remove rows).

### R0 — THE CHART MODEL I WILL ENUMERATE (H-CHART), stated before use

The M >= 5 large-source chart is the *faithful generalisation* of the
banked m4_t2 chart (`notes/pilots_20260807/fpc5_diag/rh_m4t2_census.py:
build_flat/census`), with the substitutions
`background block B -> the canonical background pick R (|R| = u)`,
`2 touched petals -> t touched petals`, `4 petals -> M petals`.
Explicitly, from the two node texts:

- domain = `n` points partitioned as `C` (core, `N = |C| = k-1`)
  `+ B` (background, `|B| = b`) `+ T_1..T_M` (petals, `|T_i| = ell`);
  so `N + b + M*ell = n`, i.e. `S = n-k+1 = M*ell + b`
  (`l1_fixed_support_defect_johnson_bound/statement.md:13-18`,
  `l1_joint_core_background_johnson_bound/statement.md:CJ1`).
- a CONTRIBUTOR for the cell `(X = the t touched petals, d, R)` is a
  pair `(F,W)` with `F = L_D` monic, `D subset C`, `|D| = d`,
  `deg W <= d`, `W = c_i F` on every point of every touched petal
  (exact labelled support `X`, `h = |X| = t*ell`), `W = 0` on `R`
  (background label; "every background agreement is a background root
  of `W_j`", `l1_joint_core_background_johnson_bound/proof.md:12-13`),
  `gcd(F,W) = 1` (JB1 primitivity), and — the exactness of the petal
  support — `W - c_u F` nonzero at every point of every UNTOUCHED
  petal `T_u`.
- by CRT mod `P = L_R * prod_{i touched} L_{T_i}` (deg `u + t*ell`),
  `W = rem_P(F*G)` with `G = sum_i c_i e_i` (idempotents, `G = 0`
  mod `L_R`), and the contributor condition is `deg rem_P(F*G) <= d`,
  i.e. `deg P - (d+1) = u + t*ell - d - 1` linear conditions on `F`.
- REGISTERED IDENTITY (hand-derived, to be checked by assertion in
  code): with `u = d-(t-1)ell` the codimension is `u+t*ell-d-1 = ell-1`
  at EVERY admissible cell, so `dim V = d-ell+2` and the monic chart
  has dimension `CHARTDIM = d-ell+1 = (t-2)*ell + u + 1`. Exact
  enumeration costs `q^(CHARTDIM-1) * |pool|` by the banked
  last-coordinate bucketing (`rh_bucket.enumerate_split`). The m4_t2
  cell is the `u = b = ell-3`, `t = 2`, `M = 4` member of this family
  and its codim is `ell-1` (banked) — this is the consistency anchor.
- root pool = `C` exactly (|C| = N). This is the HONEST model (D must
  lie in the core); the round-25 arm-A relaxation (pool = everything
  outside the source, then MAXPACK into N) is a second, adversarial
  reading which I will report separately if budget allows.

**If the D1 scan contradicts the `ell-1` codimension identity at any
cell, I stop and re-brief rather than patching the model.**

### R1 — ADMISSIBILITY (from the nodes' own texts) and the accessible cell list

Admissibility conditions, each with its source, evaluated at the CELL's
OWN parameters (the round-25 `(4,1,1)` cautionary tale = do not import a
sibling's family):

| id | condition | source |
|---|---|---|
| A1 | `M >= 5 (rate 1/2, 1/4), M >= 7 (1/8), M >= 15 (1/16)` | large_source statement:8-13 |
| A2 | `2 <= t < 2M-4` | large_source statement:18 |
| A3 | `d < ell*(M-2)` | large_source statement:19 |
| A4 | `e = 2d+1-t*ell >= 1` (finite reading of `max(0,2d+1-t ell) -> infinity`) | large_source statement:20 |
| A5 | `t <= M` | large_source statement:37-38 (exact fact) |
| A6 | `0 <= b < ell`, and `b > 0` for (CJ3) | JB statement:16; CJ proof:44 |
| A7 | `g = ell-b >= 1` | JB statement:17 |
| A8 | `u = d-(t-1)ell`, `0 <= u <= b` (= list threshold `h >= d+g`) | CJ1 + CJ proof:32; round-24 correction |
| A9 | `r_J = 2d-h >= 0` | CJ2 / JB2 |
| A10 | `N = k-1`, `S = n-k+1 = M*ell+b` (core/source partition) | JB statement:13; CJ proof:16 |
| A11 | `ell = floor(S/M)` i.e. the cell lies in the sieve's own ell-window `(S/(M+1), S/M]` | fpc5_exact.p7_large_source_sieve |

Two derived labels I will report but NOT use as admissibility:
`LIVE = [J_plain = d^2 - N(e-1) <= 0]` (the cell is inside the 408-row
residual, i.e. Johnson does not pay it) and
`CJ3 = [b d^2 + N u^2 - N b r_J > 0]` (the CJ rescue fires).

**DISCLOSED SCOPE LIMIT, registered in advance.** A4's node text is an
ASYMPTOTIC condition (`-> infinity`). No finite cell satisfies it; the
finite reading `e >= 1` is the only checkable one, and every exactly
enumerable cell has small `e` (3, 5 or 7 below). Any falsifier hit I
report is therefore a hit AT FINITE `e`, and I will say so in the
verdict rather than claiming the asymptotic cell.

**ACCESSIBLE CELL LIST (hand-derived; frozen here).** All have `t = 2`
or `3`, `u = b = ell-1` (the `b -> ell` end named by the round-25 kill
report), `CHARTDIM <= 4`, and `mu = C(N,d)/q^(ell-1)` (the expected
number of split members per flat) at least ~0.5. `q` = the smallest
prime `> n` unless stated.

| id | rate | M | t | ell | b=u | d | h | e | r_J | N | n | q | CHARTDIM | mu (hand) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | 1/2 | 5 | 2 | 2 | 1 | 3 | 4 | 3 | 2 | 9 | 20 | 23 | 2 | 3.65 |
| C2 | 1/2 | 8 | 2 | 2 | 1 | 3 | 4 | 3 | 2 | 15 | 32 | 37 | 2 | 12.3 |
| C3 | 1/2 | 16 | 2 | 2 | 1 | 3 | 4 | 3 | 2 | 31 | 64 | 67 | 2 | 67.1 |
| C4 | 1/2 | 5 | 2 | 3 | 2 | 5 | 6 | 5 | 4 | 15 | 32 | 37 | 3 | 2.19 |
| C5 | 1/2 | 8 | 2 | 3 | 2 | 5 | 6 | 5 | 4 | 24 | 50 | 53 | 3 | 15.1 |
| C6 | 1/2 | 5 | 2 | 4 | 3 | 7 | 8 | 7 | 6 | 21 | 44 | 47 | 4 | 1.12 |
| C7 | 1/2 | 6 | 2 | 4 | 3 | 7 | 8 | 7 | 6 | 25 | 52 | 53 | 4 | 3.23 |
| C8 | 1/2 | 5 | 3 | 2 | 1 | 5 | 6 | 5 | 4 | 9 | 20 | 23 | 4 | 5.48 |
| C9 | 1/2 | 8 | 3 | 2 | 1 | 5 | 6 | 5 | 4 | 15 | 32 | 37 | 4 | 81.2 |
| C10 | 1/4 | 18 | 2 | 2 | 1 | 3 | 4 | 3 | 2 | 11 | 48 | 53 | 2 | 3.11 |
| C11 | 1/4 | 24 | 2 | 2 | 1 | 3 | 4 | 3 | 2 | 15 | 64 | 67 | 2 | 6.79 |
| C12 | 1/8 | 42 | 2 | 2 | 1 | 3 | 4 | 3 | 2 | 11 | 96 | 97 | 2 | 1.70 |
| C13 | 1/16 | 120 | 2 | 2 | 1 | 3 | 4 | 3 | 2 | 15 | 256 | 257 | 2 | 1.77 |

`q` GRID (registered): primary `q` as tabled; a q-invariance replication
at C1 with `q = 47` and at C2 with `q = 67` (roughly `2n`). No cell uses
`u = 0` (the degenerate zero-background pick) — the "no shift-0 cells"
rule, read at this node.

CONFIG GRID (2-power, mine): `nconfig = 256` at CHARTDIM 2, `64` at
CHARTDIM 3, `8` at CHARTDIM 4. Seeds: `20260809` primary, `424242`
replication. Layout per config: uniformly random partition of the `n`
domain points into `C,B,T_1..T_M`; `M` distinct nonzero labels; touched
set `= {T_0..T_{t-1}}`.

If the D1 scan shows a listed row is NOT admissible, or shows the
enumeration is not exact under the wall, that row is DROPPED and
reported as a miss. If ALL rows drop, D1's honest answer is "no
admissible cell is exactly enumerable", I price the cheapest
approximation and STOP for re-brief.

### R2 — REGISTERED FUNCTIONALS (CATCH-19C)

Per (cell, config): `NSPLIT_S` (split-only root sets), `NSPLIT_G`
(guarded: primitivity + untouched-petal nonagreement), `KCORE` =
`|intersection of all guarded root sets|`, `UNION` = `|union|`,
`ANN_SIGMA = UNION-KCORE`, `ANN_A = d-KCORE`, `ANN_ACO = ANN_SIGMA-ANN_A`,
`OVL_HIST` (FULL pairwise overlap distribution, reported PER CONFIG —
no merged histogram without disaggregation, per round-25
self-correction 2), `OVL_MAX`, `OVL_MEAN`, `PENCIL_MAX` (largest number
of members sharing a common `(d-1)`-subset), `AC_DIRECT`, `AC_COMP`
(the two (PC3') orientations at the measured `(sigma,a,delta)`),
`MAXPACK` (max subfamily with union <= N), and two functionals of mine,
named here:
- `FIRE_SIGMA` = `[ANN_SIGMA < 2*ANN_A]` on the full guarded family
  (the exact round-25 threshold; note for `m = 2` members
  `ANN_SIGMA = 2*ANN_A` identically, so `FIRE_SIGMA` is never fired by
  a 2-member degeneracy — registered in advance);
- `SUBFIRE_MAX` = the largest subfamily of size >= 3 whose own
  `(sigma,a)` satisfies `sigma < 2a` (exhaustive when `NSPLIT_G <= 18`,
  otherwise reported as a lower bound with the search flag).
Also `FIRE_KCORE = [KCORE >= 1]` and `FIRE_UNION = [UNION < 2d]`, the
two literal flags of the registered falsifier.

### R3 — POWER CONTROL (registered, round-23b standard)

Every guarded arm is matched by a RANDOM arm: a uniformly random
subspace of `F_q[X]_{<=d}` of the SAME dimension `d-ell+2`, same `q`,
same `d`, same pool `C`, same split filter, same config count. Any
falsifier firing in the guarded arm that is not at least `3x` the
random arm's rate (over >= 32 configs) is reported as a SMALL-NUMBERS
ARTEFACT, not structure. I also compute the exact hypergeometric
reference `P[KCORE >= 1]` and `P[FIRE_SIGMA]` for `m` uniform random
`d`-subsets of an `N`-set, conditioned on the measured `m`.

### R4 — PREDICTIONS (numeric windows, registered before compute)

- **P1 (D1 nonempty).** >= 6 of C1..C13 survive the admissibility scan
  AND enumerate exactly under the 1G/5min wall. Window 6-13. p = 0.9.
- **P2 (codim identity).** The syndrome rank is exactly `ell-1` at every
  surviving cell (so `dim V = d-ell+2`), 0 exceptions. p = 0.85.
- **P3 (KCORE, conditional).** At the `u = b = ell-1` cells, the
  fraction of configs with `NSPLIT_G >= 3` that have `KCORE >= 1` lies
  in `[0.05, 0.60]` — against round-25's `0/63` at the m4_t2 cells.
  p = 0.6. (Unconditional `KCORE >= 1` will be much higher purely
  because `m` is small; I register the conditional as the real test.)
- **P4 (the decisive one, FIRE_SIGMA).** At least one accessible cell
  has >= 1 config with `NSPLIT_G >= 3` and `FIRE_SIGMA` true. p = 0.5.
  Window on the rate over `NSPLIT_G >= 3` configs: `[0.02, 0.40]`.
- **P5 (power control).** The guarded `FIRE_SIGMA` rate does NOT exceed
  `3x` the matched random-flat rate at any cell (i.e. any firing is a
  small-numbers artefact). p = 0.6. REFUTATION of P5 = a structural hit.
- **P6 (b -> ell trend).** Along the ladder C1 -> C4 -> C6
  (`r_J/d = 2/3, 4/5, 6/7`), `OVL_MEAN/d` is non-decreasing and
  `FIRE_KCORE` rate is non-decreasing. p = 0.55.
- **P7 (cap tightness).** `OVL_MAX = r_J` (the (CJ2)/(JB3) cap) is
  ATTAINED at >= 1 config at >= 3 of the surviving cells. p = 0.7.
- **P8 (guard deletion, the round-25 mechanism).** `NSPLIT_G/NSPLIT_S`
  lies within `+/-0.15` of `(1-1/q)^{ell*(M-t)}` (the untouched-petal
  nonagreement heuristic) times the primitivity survival `~(1-1/q)^d`;
  and `OVL_MEAN_G <= OVL_MEAN_S`. p = 0.6.
- **P9 (escape test 1).** `d4_cj3_audit.py` replays with 71 rows,
  `fraction_of_residual_d_mass_rescued = 0.01969549`, hypothesis
  failure ledger `0/1/0/82/0/0/0`. p = 0.97.
- **P10 (escape test 2).** `d2_arm_a.py 4 97 32 20260809 <out> 240 full`
  reproduces `configs_used = 32`, `FRAC_PAIRS_OVERLAP_0` merged
  `= 0.7157 +/- 0.0002`, `configs_with_KCORE_ALL_positive = 0`,
  `PENCIL_MAX_hist = {"1": 32}`, `MAXPACK_hist = {"4": 30, "3": 2}`.
  p = 0.95. AND my generalised code in COMPAT MODE
  (`M=4,t=2,u=b=ell-3`, arm-A pool + arm-A sampling order) reproduces
  the same `NSPLIT`/`OVL_HIST` per config. p = 0.8.
- **P11 (D4 / red-3 membership, if reached).** The `t >= 4` flats'
  max-to-mean ratio at matched dimension sits within the band already
  measured for the m4_t2/m4_t3 reds, i.e. red 3 is IN mystery 7.
  p = 0.6, with the 23b power control run FIRST.

### R5 — ESCAPE / STOP RULES

- E1: codim != `ell-1` at any cell -> STOP, re-brief (model wrong).
- E2: `d4_cj3_audit.py` replay not byte-identical -> STOP, report.
- E3: `d2_arm_a.py` replay off -> my machinery reuse is unsound; STOP.
- E4: no admissible cell exactly enumerable -> D1's honest answer,
  price the cheapest approximation, STOP (no uncontrolled sample).
- E5: `FIRE_SIGMA` fires at >= 3x the random-flat rate -> the falsifier
  FIRES structurally; I then compute both anticode numbers against the
  measured truth and state exactly what reopens.

### R6 — TWO-STAGE REGISTRATION, disclosed

The cell list above was derived BY HAND from the node texts before any
interpreter ran, and is frozen. The D1 scan is a pure-arithmetic
verification of it (no measurement); if it adds admissible cells I will
report them as additions and register their `q`/config grid in a dated
sub-block below BEFORE enumerating them.

### R7 — ADDITIONS after the D1 arithmetic scan (registered before any enumeration)

D1 outcome (pure arithmetic, `d1_cells.txt`): **all 13 registered cells
pass A1-A11**, the codim identity `= ell-1` holds at all 13, all 13 are
`LIVE` (`J_plain <= 0`), and **`CJ3` fires at NONE of them**. The
independent broad scan (rate x ell 2..7 x b x M x t x u, `CHARTDIM<=4`,
`mu>=0.5`, `cost<=3e7`) finds **1470 accessible admissible cells**, of
which only **4** have `CJ3` firing, `max e = 7`, `max r_J/d = 6/7`. My
registered ladder therefore already contains the extremal
root-sharing shapes; two families are missing and are added here.

**(A) THE u-TREND LADDER** — D3's explicit question ("does `b -> ell`
push kappa up?"). The trend variable at `t = 2` is
`r_J/d = 2u/(ell+u)`. Ladder at FIXED `rate 1/2, ell = 4, b = 3, M = 8,
q = 71, N = 33, n = 68`:

| id | u | d | e | r_J | r_J/d | CHARTDIM | mu | cost/config | nconfig |
|---|---|---|---|---|---|---|---|---|---|
| T1 | 1 | 5 | 3 | 2 | 0.400 | 2 | 0.663 | 2343 | 256 |
| T2 | 2 | 6 | 5 | 4 | 0.667 | 3 | 3.095 | 166353 | 64 |
| T3 | 3 | 7 | 7 | 6 | 0.857 | 4 | 11.94 | 11811063 | 8 |

(T3 is the >10-min rung: background job with a results file, per the
RAM-discipline rule.)

**(B) THE FOUR CJ3-FIRING CELLS** — the only accessible cells where the
CJ rescue actually pays, so the measured truth can be compared against
BOTH anticode orientations AND the (CJ4) bound `m <= N b ell / J`:

| id | rate | M | t | ell | b | u | d | e | r_J | N | n | q | CHARTDIM | mu | CJ4 `m <=` | nconfig |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| K1 | 1/2 | 5 | 2 | 3 | 1 | 1 | 4 | 3 | 2 | 14 | 30 | 31 | 2 | 1.042 | 21 | 256 |
| K2 | 1/4 | 12 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 7 | 32 | 37 | 2 | 0.946 | 7 | 256 |
| K3 | 1/8 | 28 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 7 | 64 | 67 | 2 | 0.522 | 7 | 256 |
| K4 | 1/4 | 12 | 3 | 2 | 1 | 1 | 5 | 5 | 4 | 7 | 32 | 37 | 4 | 0.568 | 3 | 8 |

**(C) MODEL AMENDMENT, registered before use.** For cells with `u < b`
(T1, T2 only) the canonical background pick `R` is a PROPER subset of
`B`, and a contributor with background-agreement set `A` (`|A| >= u`)
lies in the flat of every `R subset A`. The CELL is therefore the UNION
over all `C(b,u)` choices of `R`; I enumerate all of them and dedupe by
root set (the object the anticode instrument acts on). Per-`R`
breakdown reported. For every other cell `u = b`, `R = B` is unique and
this is a no-op.

### R8 — SECOND ADDITION (registered before enumerating F1/F2 and before the real-row pricing)

The falsifier FIRED at C8 (`FIRE_SIGMA` in 7/8 configs). Inspecting the
cell arithmetic — NOT the measurement — gives an exact sufficient
condition, registered here as a claim to be tested, not assumed:

> **(FALS-1)** every guarded root set is a `d`-subset of the core `C`,
> so `|U| <= N`. Therefore `N + kappa < 2d ==> sigma < 2a`; in
> particular `2d > N` with `kappa = 0` fires the falsifier at the whole
> cell, with no enumeration.

Registered consequences to test:
- **P13.** C8 has `N = 9 < 10 = 2d`; its matched sibling C9 (identical
  `(t,ell,b,u,d)`, `M = 8`, `N = 15 >= 2d`) must NOT fire. Already
  observed at nconfig 8; to be re-checked at 256/8.
- **P14.** The number of the 408 real residual rows whose CJ-admissible
  `d`-window contains a `d` with `2d > N` is > 0. Window `[1, 408]`,
  point guess ~150. p = 0.7. (Round 25's kill rationale asserts the
  opposite for "every mystery-7 cell of ours".)
- **P15.** At the real rows both orientations are nevertheless VACUOUS
  (`log2 AC > 0.5*N`), so the firing is not load-bearing. p = 0.7.
  REFUTATION of P15 = a real reopening with a usable bound.
- **Additional accessible LIVE cells with `2d > N`** (pure-arithmetic
  scan, 4 in total, two already registered as C8/K4):

| id | rate | M | t | ell | b | u | d | e | r_J | N | n | q | CHARTDIM | mu | 2d-N | nconfig |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F1 | 1/4 | 15 | 3 | 2 | 1 | 1 | 5 | 5 | 4 | 9 | 40 | 41 | 4 | 3.07 | 1 | 64 |
| F2 | 1/8 | 35 | 3 | 2 | 1 | 1 | 5 | 5 | 4 | 9 | 80 | 83 | 4 | 1.52 | 1 | 32 |

C8 and K4 are re-run at 256 configs (a disclosed 2-power ENLARGEMENT of
the registered CHARTDIM-4 grid of 8, justified by measured cost; larger
grids can only sharpen, and the nconfig-8 runs are kept and reported).

### R9 — THIRD ADDITION: the measured overlap law and its singleton consequence (registered before the row computation)

MEASURED, at 24/24 runs with 0 violations and ATTAINED at every cell
with `NSPLIT_G >= 2`: the guarded overlap maximum is NOT the (JB3)/(CJ2)
cap `r_J`, it is

```
lam = r_J - |R_1 cap R_2|  <=  r_J - max(0, 2u-b),
and at u = b (R = B forced)   lam = d - ell   exactly.
```

This is not new mathematics — it is the node's own `(CJ2)`
(`h+|I|+|R|<=2d`, `l1_joint_core_background_johnson_bound/proof.md:19`)
read as a bound on `|I|` instead of summed, plus the observation that
`u = b` forces `R_1 = R_2 = B`. Two consequences registered here as
claims to be TESTED (I will grep the repo for prior statements first —
CATCH-24A / hard law 5):

- **(SHARP)** `|D_1 cap D_2| <= r_J - max(0,2u-b)`; at `u=b` this is
  `d-ell`, strictly better than `r_J` whenever `b > 0`, so the anticode
  `delta` is `>= ell` rather than `>= g = ell-b`.
- **(SING)** `|D_1 cup D_2| = 2d-|D_1 cap D_2| >= h + max(0,2u-b)` and
  `D_1 cup D_2 subset C`, so **if `h + max(0,2u-b) > N` the cell is a
  SINGLETON** (`m <= 1`), with no Cauchy-Schwarz and regardless of the
  sign of `(CJ3)`'s `J`.

- **P16.** (SHARP) has 0 violations over every run (24/24 already
  observed) and is attained wherever `NSPLIT_G >= 3`. p = 0.9.
- **P17.** The number of the 408 real residual rows with a nonempty
  `(SING)` sub-window is > 0; window `[0, 408]`, point guess ~80,
  concentrated at rates 1/4, 1/8, 1/16 (at rate 1/2 the arithmetic
  `t <= M-2` makes `h+b > N` impossible — hand-checked). p = 0.6.
- **P18.** The `(SING)` d-mass is NOT already covered by `(CJ3)`
  (i.e. `J <= 0` on most of it), so it is a genuine addition. p = 0.6.
- **P19 (falsifier test of my own claim).** A cheap accessible cell with
  `h + max(0,2u-b) > N` must show `NSPLIT_G <= 1` in EVERY config. Any
  config with `NSPLIT_G >= 2` REFUTES (SING) and I withdraw it. p = 0.85.

**(D) ADDITIONAL PREDICTION P12** (registered before enumerating T1-T3,
K1-K4): along T1 -> T2 -> T3 the mean pairwise overlap normalised by
`d` rises monotonically and `OVL_MAX` tracks the (CJ2) cap `r_J`
exactly; and at K1-K4 the measured cell size `m` is at least `3x`
below the (CJ4) bound (i.e. CJ4 is loose by >= 3x). p = 0.65 each.

