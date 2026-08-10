# PREREG — rh_residuals_close (round 32)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/collinearity_object/REPORT.md` (round 29 —
   the three named residuals)
2. `notes/pilots_20260810/rh_type2_stratum/REPORT.md` (round 31 —
   the re-priced (ii) and the m=1 disjointness)

## Mandate

THE RESIDUAL-BUDGET CLOSEOUT ROUND. The budgets {2^39, 2^39+1}
program has residual (ii) at 9/4 (owned by the algebraic-FR track,
NOT yours). YOUR JOB is everything else on that ledger: (i) THE
w* TILING GAP — the 1-or-3-integer gap per m between apolar's
one-third and T4's two-thirds of the w* window; (iii) m = 1 — now
known STRUCTURALLY DISJOINT from (ii) (round 31 proved j = 0 forced
at m = 1), so what exactly does the q = 17 fence still block, and
can m = 1 be closed outright? PLUS the bookkeeping that three
rounds of results have left unreconciled.

## Deliverables

**D1 — RESIDUAL (i), THE TILING GAP.** Reconstruct exactly which
w* integers per m are covered by neither apolar's (AO1) third nor
T4's top two-thirds (quote both coverage statements file:line —
and NOTE: round 31's (NEWCAP) moved the window top to 7m-1, which
may change the gap's location or existence). Close the gap
(extend either instrument by the 1-3 integers) or name the exact
obstruction per integer.

**D2 — RESIDUAL (iii), m = 1.** With the round-31 disjointness in
hand (no non-minimum-weight type-2 stratum at m = 1): enumerate
what remains open at m = 1 (the q = 17 fence's actual content — the
hypothesis fails by exactly one, boundary term 4*sigma_W, round
29). Is m = 1 closable by direct exhaustion at q = 17 (the ONLY
admissible field forcing m = 1)? If yes, run it (it is small);
if no, say exactly why.

**D3 — THE LEDGER RECONCILIATION.** Three rounds changed the
budget picture without one text holding it all: LB1 gives
B_ca^far(3n/4) >= 2^39+1 (budget 2^39 unattainable at the TOP);
the budgets' territory is q in [2^167, 2^167+2^129) (RPFC-proved
prime-only); (NEWCAP) re-priced (ii); the wave-57 fences fixed the
(FR) route. Write the CURRENT residual-budget state as one exact
table: per budget (2^39 / 2^39+1), per bracket region, what is
proved / open / dead, with every claim file:line. This table is
the draft of the eventual statement addendum (coordinator-gated).

**D4 — THE T3-GUARD SKIP FRACTION (the round-31 cheap follow-up).**
One run: instrument the round-29 21,832-configuration census's T3
guard (theta*n < a*a) and measure the actual skip fraction — was
the "0 violations" validation largely vacuous, as bank 2 inferred
structurally? Copy the banked scripts into your dir; report the
exact fraction.

## Constraints (binding)

- COMPUTE LAW: never bare python3; ramguard tiny/local, repo root,
  literal `--`; RAMGUARD_TIMEOUT documented; stdlib only; no
  Modal/network/git.
- RAM DISCIPLINE: file-at-a-time; NEVER open dag.json; checkpointed
  batches with results files.
- WRITE SCOPE: ONLY notes/pilots_20260810/rh_residuals_close/. No
  dag/, nodes/, tools/ edits. No git. Never touch prize-codex-*.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md;
  never read siblings (rh_fr_algebraic, rh_farca_upper,
  rh_haboeck_seam); round-31 and earlier readable.
- BLIND PRIORS: after the two anchors only, append "## Pilot
  registrations" (P(residual (i) closes), P(m=1 closes by
  exhaustion), expected T3 skip fraction) BEFORE any further read.
- REPORT: REPORT.md (harness-refused fallback: return verbatim; in
  all cases ALSO return verbatim as final message); MISSES-FIRST;
  CATCH-24C file:line; CATCH-24A greps; zero-power declarations;
  banked scripts from scratch copies only.

## Pilot registrations

Appended with the Edit tool after reading EXACTLY the two named
anchors (`collinearity_object/REPORT.md`,
`rh_type2_stratum/REPORT.md`) and BEFORE any other read, any grep,
any `ls`, and any interpreter invocation. All arithmetic below was
done in-head from the two anchors; none of it has been checked by
machine at registration time.

### R0 — notation I will use (from the anchors)

`rho = 4m-1`, `N = 16m`, `R = 8m`, `R1 = R+1 = 8m+1`, `e = m`,
`A = 3`, `a = w*`, `s = R1-a`, `T = T_1 + T_2` under the failure
hypothesis `(SAT3)` `T = rho+2 = 4m+1`; `d_x <= e = m` and
`sum_x (m-d_x) = 1+O` `(SAT4)`; `CAP(m,a) = floor((N-a)e/s)`;
`T1cap(m,a,O) = min(m+1, floor(a/(a-rho)), floor((am+O)/rho))`;
`AO1 = T1cap + CAP`; `p_gamma = |S_gamma \ W|`,
`j_gamma = p_gamma - s` (round 31's weight excess);
`RIG = a-1-2s`; official `m = 2^37`, budgets `{rho+1, rho+2} =
{2^39, 2^39+1}`.

### R1 — blind priors (the three the brief demands)

- **P(residual (i), the tiling gap, CLOSES this round) = 0.25.**
  Decomposed: P(I can name the gap exactly, as integers, at the
  official profile) = 0.92; P(the gap survives (NEWCAP), i.e.
  round 31 did not accidentally kill it) = 0.85; P(I close it by
  extending an instrument with a *proof*, not a measurement) =
  0.25; P(I close it by measurement only, and say so) = 0.30.
- **P(m = 1 CLOSES by direct exhaustion at q = 17) = 0.45.**
  Decomposed: P(a complete exhaustion at `m=1` is computationally
  feasible inside one `local` run) = 0.80 (see R3 for the search
  I intend); P(the exhaustion returns EMPTY, i.e. no `T = rho+2`
  configuration exists at `m=1`) = 0.30 — I think it is more
  likely that the `q=17` fence IS a realized `T = 5`
  configuration, because round 29 already exhibits three pairwise
  disjoint collinear locator triples there
  (`(4,6,16),(8,10,15),(9,12,13)`, `collinearity_object/REPORT.md:52`)
  and `AO1(m=1) = 2+3 = 5 = rho+2` exactly; P(m=1 is instead
  closed as VACUOUS for the prize, because the official profile
  has `m = 2^37` and no instrument is inductive in `m`) = 0.55.
  These are not mutually exclusive; the reported outcome will say
  which branch fired.
- **Expected T3-guard SKIP FRACTION (round-29 21,832-config
  census, guard `theta*n < a*a`) = 0.85**, registered window
  `[0.55, 0.99]`, and I register the qualitative call: **the
  "0 violations" validation IS largely vacuous** (P = 0.75).
  Sub-registration: P(skip fraction is exactly 1.0000, i.e. the
  guard never fired at all) = 0.20.

### R2 — the gap arithmetic, computed blind and registered as a prediction

From the two anchors: T4's hypothesis `2s <= a-1` with
`s = 8m+1-a` reads `a >= (16m+3)/3`; `(AO1)` closure needs
`AO1(a) <= rho+1 = 4m`. Registered blind:

- **P1.** The AO1 side closes exactly `a <= (16m-2)/3` and the T4
  side exactly `a >= (16m+4)/3` when `m ≡ 2 (mod 3)`, so the gap
  is the SINGLE integer `a = (16m+1)/3`.
- **P2.** Gap size is a function of `m mod 3`, not of anything
  else: **1 integer at `m ≡ 2`, 3 integers at `m ≡ 1`, and I
  predict 2 integers (NOT 0) at `m ≡ 0 (mod 3)`** — round 29's
  measured `m ∈ {2,4,8,40}` contains **no** `m ≡ 0 (mod 3)`
  (2,4,8,40 ≡ 2,1,2,1), so its "never 0" is untested there.
  Registered as a live CATCH against the anchor.
- **P3.** Official `m = 2^37 ≡ 2 (mod 3)`, so the official gap is
  ONE integer, `w* = (2^41+1)/3 = 733007751851`.
- **P4.** At that `a`: `s = (8m+2)/3`, `CAP = 4m-2`,
  `floor(a/(a-rho)) = 3`, `AO1 = 4m+1 = rho+2` — **the gap
  integer fails by EXACTLY ONE**, the same signature as the
  `q=17` fence. At `a = (16m-2)/3`: `CAP = 4m-3`, `T1cap = 3`,
  `AO1 = 4m = rho+1` (closes).
- **P5.** `2s - (a-1) = 2` at the gap integer: T4 fails there by
  exactly 2 points, i.e. `RIG = -3`. Round 29 measured
  `F_COLL = s+1` down to `RIG = -6`, so the gap integer is
  INSIDE round 29's measured-but-unproved band. Prediction: the
  obstruction is "T4 by 2", i.e. the two degree-`2s` polynomials
  differ by `sigma_W * (quadratic)` instead of `sigma_W *
  (constant)`.
- **P6.** A one-unit improvement of the per-slope spend floor
  (`p_gamma >= s+1` for every type-2 slope, i.e. NO
  minimum-weight type-2 slope at the gap `a`) closes the gap
  integer: needed `p* > (32m^2-m)/(12m-6) = s + (7m+4)/(12m-6)`,
  and `(7m+4)/(12m-6) < 1`. So residual (i) and residual (ii)
  are the SAME missing inequality at different `a`.
- **P7.** `(NEWCAP)`'s `w* <= 7m-1` does NOT kill the gap
  (`7m-1 > (16m+1)/3` for all `m >= 1`), and does NOT move it.
  A sharpened `(NEWCAP)` of the form `w* <= (16m-2)/3` would
  close residuals (i) AND (ii) together; the required
  strengthening factor is `(7m)/(16m/3) = 21/16 = 1.3125`.

### R3 — the m=1 exhaustion I intend (registered before running)

At `m=1`: `N=16`, `R=8`, `R1=9`, `rho=3`, `e=1`, `a=w*=6`,
`s=3`, `T=rho+2=5`, `T1cap = floor(6/3) = 2`,
`CAP = floor(10/3) = 3`, `AO1 = 5 = rho+2`. `d_x <= e = 1`
forces the five supports to be **pairwise disjoint**, and
`T*rho = 15 <= N = 16` is feasible only at `m=1` (round 31's R4
reading). Registered search: fix `D = F_17^*` (order 16); for
every ordered pair of disjoint triples `(S_1,S_2)` put
`W = S_1 u S_2` (`|W| = 6 = w*`); for each further triple `S_i`
disjoint from `W`, the codeword `kappa_i` of the `[16,8,9]` RS
code supported on `Z_i = W u S_i` is UNIQUE up to scale
(shortened dimension `|Z_i| - R = 1`), so
`kappa_{i,x} = c/sigma'_{Z_i}(x)`; the five slopes are
simultaneously supported iff the normalized restrictions
`kappa_i|_{S_1}` agree across `i` and likewise `kappa_i|_{S_2}`.
Cost: `C(16,3)*C(13,3) = 160160` pairs x `C(10,3) = 120`
candidates ~ `1.9e7` cheap checks — one `local` run. Registered
predictions: **P8** the exhaustion completes under
`RAMGUARD_TIMEOUT=290`; **P9** the number of matching groups of
size `>= 3` is `> 0` (P = 0.70) and if `> 0` the round-29 fence
triple `(4,6,16),(8,10,15),(9,12,13)` appears among them
(P = 0.55); **P10** `q = 17` is NOT the only field with `m=1`
(`16 | q-1` also at `q = 97,113,193,241`), so the brief's
"ONLY admissible field forcing m=1" needs a second admissibility
condition that I will locate and quote or else flag as an
overclaim.

### R4 — D3 ledger predictions

- **P11.** `LB1`'s `B_ca^far(3n/4) >= 2^39+1` makes budget `2^39`
  dead at the TOP of the bracket, so the surviving live cell is
  budget `2^39+1` over `q in [2^167+2^128, 2^167+2^129)`, and the
  sliver `[2^167, 2^167+2^128)` carries budget `2^39` only.
  Registered window: the reconciled table has between 4 and 12
  rows and **at least one cell that is DEAD by LB1** (P = 0.6).
- **P12.** At least one of the three rounds' numbers is
  inconsistent with another when written side by side (P = 0.5);
  if so I report it as a CATCH rather than silently picking one.

### R5 — route order (registered, so deviations are visible)

D1 (gap arithmetic, exact integers) -> D2 (`m=1` exhaustion) ->
D4 (the cheap census re-run) -> D3 (ledger, written last because
it must quote the other three). If a wall is hit, D3 is written
from what exists and the shortfall is declared.

### R6 — zero-power declarations, registered in advance

1. Any `m = 1` / `q = 17` result has **zero power** over the
   official profile `m = 2^37` unless an instrument is inductive
   in `m`; I will state explicitly whether closing `m=1` moves
   either budget, and I expect the answer is NO.
2. The gap arithmetic is EXACT INTEGER arithmetic on banked
   formulas; it has zero power over whether those formulas are
   *correct* — it inherits `(AO1)`, `(SAT1)-(SAT4)` and T4's
   hypothesis wholesale.
3. Round 29's `F_COLL = s+1` down to `RIG = -6` is a **sampled**
   measurement at `N in {16,32}`; if I use it to argue the gap
   integer is "empirically fine", that is a heuristic and gets
   no theorem status.
4. The T3 skip fraction is a property of one banked census's
   configuration grid, not of the mathematics; a high skip
   fraction weakens that census's validation and nothing else.
5. Any novelty claim gets a CATCH-24A own-repo grep first; the
   `7m-1`, `5.04e22`, `(AO1)`, `(C2)`, `(OV)` objects are
   already known to be banked (round 31's subtraction table) and
   I will not re-claim them.

### R7 — compliance plan

Every interpreter invocation `tools/ramguard tiny|local -- python3`
from the repo root with literal `--` and explicit
`RAMGUARD_TIMEOUT`, counted and reported. Stdlib only. `dag.json`
never opened. Writes only inside
`notes/pilots_20260810/rh_residuals_close/`. Quarantine:
`notes/pilots_20260802/CAMPAIGN_LEDGER.md` never opened; the three
round-32 siblings (`rh_fr_algebraic`, `rh_farca_upper`,
`rh_haboeck_seam`) never read or listed — every recursive grep
carries a `grep -vE` filter for them and for `prize-codex-`. No
subagents, no git, no network.
