# PRE-REGISTRATION — C2''-r3: A REACHABLE FALSIFIER + THE GB-5 ESCALATION (round 25)

2026-08-09. Coordinator brief; pilot appends registrations BEFORE
any computation. MANDATE: round 24 killed both registered C2''
falsifiers as tests (G-b vacuous by theorem; G-a at 2^203 states).
The pose needs a REACHABLE falsifier, and GB-5 (the first
non-stacked datapoint: R3_W = 11.34 bits over 4 junctions vs the
2.545-bit window-scaled reserve, 4.5x) needs escalation.

## Sources
- critical/nodes/dli_c2pp_joint_reserve (the round-23/24 addenda:
  C2''-r3's exact form; the vacuity theorem; the freeze law — the
  official row lives ENTIRELY pre-saturation, log2 q in [41, 256]
  vs n/t = 256; the census squaring law).
- notes/pilots_20260808/c2pp_gb_probe/ (REUSE: gb_probe.py the
  checkpointed instrument, verify_law.py, the J = 4 exact-depth
  scan; the middle-peaked shape; the closed-form saturation law).

## Deliverables
- (D1) THE REDESIGNED FALSIFIER, drafted with its power analysis:
  it must be (i) evidence-bearing under the binding symmetric
  not-evidence clause (genuine sequential conditioning, no
  stacking), (ii) REACHABLE (depth <= 4 exact, or an analytic
  form), (iii) POWERED (able to separate a true C2''-r3 world from
  a false one at reachable scale — run the power control on a
  synthetic pair BEFORE proposing). Candidate shapes to price:
  a pre-saturation GROWTH criterion at fixed depth (the freeze law
  confines the official q-range to pre-saturation — a depth-4 sum
  growing superlinearly in log q across >= 4 pre-saturation
  octaves at >= 2 tower shapes); an analytic bound on the
  junction sum via the U-induced skew law; a shape criterion
  (the middle-peak location drifting with q).
- (D2) THE GB-5 ESCALATION, executed: deeper/wider pre-saturation
  windows via the q-free structure — the round-24 instrument at
  J = 4 across MORE tower shapes (n, t) and MORE pre-saturation
  q-octaves; the target functional is R3_W vs the window-scaled
  reserve (registered: at what (n, t, q) grid does the 4.5x grow,
  saturate, or shrink?). NO J -> 33 transport; growth-shape
  evidence only.
- (D3) THE ANALYTIC ATTEMPT: the closed-form saturation law gave
  Z_j^inf exactly; attempt the PRE-saturation analogue (the
  binomial-skew census as a function of log2 q below n/t) — even
  a two-term expansion would make the official-row junction sum
  estimable for the first time.
- (D4) VERDICT: the falsifier of record (drafted + power-tested)
  for coordinator adoption; the escalated GB-5 dataset + its
  shape; the analytic form or its named obstruction.

## Rules
QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md at
or past line 3731 (the "ROUND 25 LAUNCHED" marker); do not read the
other round-25 pilot dirs; PASS THIS CLAUSE VERBATIM to any subagent.
RAM DISCIPLINE (binding): file-at-a-time reads; never load dag.json
whole (grep it or read node.json shards); no bulk directory reads.
COMPUTE LAW: every python3 via tools/ramguard tiny|local -- python3
(literal --) from repo root, INCLUDING file patching and JSON
peeking; checkpoint long runs to YOUR OWN dir across the walls.
DRAFT ONLY in your own dir; never edit dag.json/nodes/tools; no git
writes; no Modal; stdlib only. Name every measured functional
(CATCH-19C); 2-power grids where yours to choose (CATCH-Z6); no
shift-0 cells (CATCH-19B). Verbatim quotes with file:line. No
REPORT.md — your final message IS the report.

# PILOT REGISTRATIONS

Appended 2026-08-09 BEFORE any computation: at the time of this
append no script existed in this directory and no `python3` had been
run by me. Opus pilot, round 25. Everything below (including the
closed forms in P3) was derived BY HAND from the sources and is
registered as a PREDICTION to be verified or refuted by exact
census. Where a hand-derived number happens to match a number
printed in the round-24 REPORT I say so explicitly — that is a hand
cross-check against banked text, not a measurement.

## P0. Definitions and quotes (verbatim, not reconstructed)

**(P0-a) The claim.**
> `    sum_{j=1}^{33} log2( E_U[rho_j | state_{<j} null] / E_U[rho_j] ) <= 21.`
> — `critical/nodes/dli_c2pp_joint_reserve/statement.md:94`

**(P0-b) The falsifier clause is OPEN.**
> `**G-a's depth is UNREACHABLE:** >= 8 consecutive junctions costs 2^203
> census states (every extra junction squares the census); a testable
> falsifier needs a reachable depth or an analytic form — the falsifier
> clause of C2''-r3 is OPEN for redesign (coordinator: next-round item).`
> — `critical/nodes/dli_c2pp_joint_reserve/statement.md:127-131`

**(P0-c) The object to escalate.**
> `**THE FIRST NON-STACKED DATAPOINT on the r3 object (GB-5):** R3_W =
> 11.34 bits over 4 consecutive junctions at (n=32, t=16) vs the
> window-scaled reserve 21*4/33 = 2.545 bits — a factor 4.5`
> — `critical/nodes/dli_c2pp_joint_reserve/statement.md:143-147`

**(P0-d) The freeze law as banked (round 24).**
> `**GB-3** **The freeze law.** Every census freezes exactly once
> `log2 q >= n/t`.` — `notes/pilots_20260808/c2pp_gb_probe/REPORT.md:97`

**(P0-e) The official schedule and its admissible q.**
> `- **scope:** the banked official DLI production schedule (`n = 2^41`,
>   `t = 2^33`, 34 blocks / 33 junctions, `N_j = 256 L_j` uniformly), and any
>   official-admissible modulus `q` (odd prime, `v_2(q-1) >= 41`, `q < 2^256`).`
> — `background/nodes/dli_official_support_forcing/statement.md:5-7`

**(P0-f) The official-scale ledger constants I will try to REPRODUCE
from the toy law** (this is the anchor that makes the analytic
attempt about the official row rather than about a toy):
> `  "support_to_constraint_ratio": 256,`
> `  "coset_stratum_cells": 128,`
> `  "coset_stratum_size": "2^128",`
> `  "coset_stratum_probability": "2^-2199023255424",`
> `  "coset_term_log2_formula": "2^33*(log2 q - 256) + 128",`
> `  "exceeds_2^21_iff": "256 - log2 q < 107/2^33 = 1.24556e-05"`
> — `notes/pilots_20260802/c2pp_nullity_structure/results/official_scale.json:78-83`

**(P0-g) The instrument I reuse verbatim** (`gb_probe.py`
`level_vectors`, `junction_vectors`, `mitm_null_count`, `binom_alpha`,
`skew_alpha`, `subset_alpha`, `get_zeta`, `q_ladder`, `log2_int`) and its
`rho_j` convention (declared divergence D-10 of round 24, inherited
verbatim and re-declared here):
> `**`rho_j` convention (declared divergence, D-10 below):** I take
> `rho_j(M) := q^{L_j} P_U[ block j holds | m_{j+1} = M ]` with the
> `U`-induced (binomial) skew law` — `notes/pilots_20260808/c2pp_gb_probe/PREREG.md:235-237`

All round-24 divergences D-1…D-11 are inherited and re-declared
unchanged. I add:
- **D-12 WINDOW = TOWER.** Several of my cells have `W` = ALL the
  junctions of their toy tower (`J = D-1`), not a sub-window. I will
  say which, because "4 of 4" and "4 of 33" are different scopes.
- **D-13 ANALYTIC EXTENSION.** Where I evaluate a closed form at
  `(n,t)` beyond the exactly-censused cells, that is the LAW being
  extrapolated, not a measurement. Every such number is labelled
  `[law]`.

## P1. THE TELESCOPING LEMMA (registered before computing; to be
asserted in code and brute-force checked at n = 16)

> **LEMMA (the junction sum is a difference, not a sum).** With
> `N_{>j}` the accumulated conditioning of round 24's P1 lemma and
> `E_j := {block j holds}`, one has `N_{>j-1} = E_j AND N_{>j}`, hence
> for `W = {w0, ..., w1}`
> ```
> R3_W = log2 P[N_{>w0-1}] - log2 P[N_{>w1}] - sum_{j in W} log2 P[E_j]
>      = log2 ( P[ AND_{j in W} E_j | N_{>w1} ] / prod_{j in W} P[E_j] ).
> ```
> So `R3_W` is EXACTLY the excess of the conditional joint over the
> product of marginals; it is 0 iff the blocks are conditionally
> independent; and the whole sum is determined by TWO level censuses
> and `J` block censuses.

Consequences registered now: (i) at `W` = the whole tower this reads
`R3_full = log2 P[x fully null] - log2 P[N_{>m-1}] - sum_j log2 P[E_j]`,
i.e. **C2''-r3 is exactly the statement that the joint nullity
probability exceeds the independent-block heuristic by at most 21
bits**; (ii) the measurement problem moves from "J consecutive
junctions" (which squares per junction) to "level censuses", which
is what makes a reachable falsifier possible at all.

## P2. Named functionals (CATCH-19C), all fixed before any run

Let `n = 2^s`, `t = 2^m` (`m < s`), `e := n/(2t)`, `h_lev = n/2^lev`,
`T_lev = t/2^lev`, `u_lev = 2^lev`, `Lam := log2 q`,
`sigma(u,M) := sum_{c=0}^{u} C(u,c)^M`, `c_k := 2^k - log2 C(2^k, 2^{k-1})`
(`c_0 := 1`), `S_m := sum_{k=1}^{m} c_k 2^{-k}`.

| name | definition |
|---|---|
| `Zlev(n,t,lev,q)` | exact weighted level census (round-24 `Z[lev]`) |
| `Blk(n,t,j,q)` | exact block-marginal census (round-24 `Pblk_count`) |
| `Csub(n,t,lev,q)` | exact coset/subset census (round-24 `C_j`) |
| `Zinf(n,t,lev)` | **CLOSED FORM CANDIDATE** `sigma(u_lev, 2T_lev)^e` |
| `Cinf(n,t,lev)` | **CLOSED FORM CANDIDATE** `2^e` |
| `Binf(n,t,j)` | **CLOSED FORM CANDIDATE** `C(2^{j+1},2^j)^{h_{j+1}}` |
| `Exc(n,t,lev,q)` | `log2( Zlev / Zinf )` — the CENSUS EXCESS, `>= 0` |
| `LamStar(n,t,lev)` | `(n - log2 Zinf)/T_lev` — predicted crossover |
| `alpha(n,t,lev)` | fitted `-d log2 Zlev / d Lam` in the deep band |
| `R3_W(n,t,q)` | round-24 `R3_W`, reused verbatim |
| `R3inf_W(n,t)` | `R3_W` evaluated on the closed forms |
| `RATIO_W` | `R3_W / (21*J/33)` — the GB-5 ratio (the "4.5x") |
| `CosetTerm(Lam)` | `e + T_0*(Lam - n/t)` at level 0 (the official ledger's coset term, in my variables) |
| `PeakJ` | `argmax_j term_j` — the middle-peak location |

## P3. THE HAND-DERIVED CLOSED FORMS (registered as predictions)

**(C-1) The frozen stratum is the `e`-PERIODIC stratum.** The
constraints at level `lev` are `f(zeta_h^r) = 0`, `r = 1..T`, on
`f = sum_i M_i X^i`, `deg f < h`. Over `Z` the lcm of the minimal
polynomials of `zeta_h^r`, `r = 1..T` (`h` a 2-power) is
`prod_{a=0}^{floor(log2 T)} (X^{h/2^{a+1}} + 1) = (X^h - 1)/(X^e - 1)`
with `e = h/(2T) = n/(2t)`, independent of `lev`. Hence the
Z-exact states are exactly the `e`-periodic ones, giving
`Zinf = sigma(u, h/e)^e = sigma(u, 2T)^e` and `Cinf = 2^e`.
At `lev = 0` this is the official ledger's coset stratum:
`e = n/2t = 128` cells, size `2^128`, probability `2^{128-n}` —
**it must reproduce `official_scale.json:79-81` exactly** or C-1 is
wrong.

**(C-2) The block marginal has NO nonzero frozen stratum.** At
junction `j` the constraints are `f(xi^u) = 0`, `xi` of order
`h_j = 2 h_{j+1}`, `u` odd, `deg f < h_{j+1}`; the minimal polynomial
of `xi^u` is `X^{h_{j+1}} + 1`, of degree `> deg f`, so `f = 0` is the
only Z-exact skew. Hence `Binf = C(2^{j+1},2^j)^{h_{j+1}}`.

**(C-3) The saturated junction sum, EXACT closed form:**
```
R3inf_full(n,t) = e*(1 - log2 C(2t,t)) + n * S_m .
```
Hand-check against banked text (not a measurement): at `n=32, t=16`
this gives `11.34`, and the round-24 REPORT prints `R3_W = 11.3367`
(`REPORT.md:48`). Registered per-junction hand values for that cell:
`(0.99996, 6.5323, 2.8518, 0.9544)`.

**(C-4) The refined FREEZE LAW.** Saturation is per LEVEL, not per
tower: `LamStar(lev) = (n - log2 Zinf(lev))/T_lev ~= (n/t) * c_lev`,
with `c_lev ~= 0.5*lev + 0.326`. Round-24's `Lam >= n/t` is the
`lev = 0` case. Hand-check against banked text: `S1` predicts
`LamStar(1) = 11.3` vs printed `sat q = 65537` (`Lam = 16`);
`S2 -> 11.3` vs `4129` (`12.0`); `S3 -> 15.0` vs `262337` (`18.0`);
`S4 -> 22.6` vs `16777601` (`24.0`). Predicted ORDERING matches;
predicted ONSET is 2-5 bits low at every cell, so **C-4 as an onset
formula is already suspect and I register it as such** — the
measured onset is systematically LATER than the crossover, which is
exactly the pre-saturation tail this pilot must characterise.

**(C-5) The deep-pre-saturation limit of the junction sum.** With
`Zlev ~ 2^n q^{-T_lev}` and `Blk ~ 2^n q^{-L_j}` (`L_j = T_{j+1}`), the
telescoping lemma gives `R3_W -> 0` identically (the `Lam` terms
cancel exactly). Registered corollary: **if the official row is deep
pre-saturation at every level, the C2''-r3 junction sum is ~0, and
the GB-5 4.5x is a SATURATION artefact with no official-row scope.**

## P4. THE THREE CANDIDATE FALSIFIER SHAPES, PRICED

**(G-c) THE DECAY-EXPONENT FALSIFIER — my primary candidate.**
Statistic: `alpha(n,t,lev)`, the slope `-d log2 Zlev/d Lam` measured
in the band where `Exc >> 0` (deep pre-saturation). Registered null
(the law the official ledger implicitly assumes): `alpha = T_lev`
exactly. **G-c FIRES iff `alpha >= 1.10 * T_lev` at `>= 3` cells
spanning `>= 2` distinct `T`.** Why it bears on the official row:
the level-0 crossover sits at `Lam = (n - e)/alpha_0`; at
`alpha_0 = T_0 = t` that is `Lam = 256 - 128/2^33`, i.e. exactly the
top of the admissible band (`official_scale.json:83`), but at
`alpha_0 = 1.1 T_0` it drops to `Lam = 233`, putting the whole band
`Lam in [233, 256]` INSIDE the saturated regime where the ledger
already scores `"exceeds_2^21": true`
(`official_scale.json:181-183`). Reachable: single-level censuses,
no window. Powered: see P5.

**(G-d) THE PRE-SATURATION GROWTH CRITERION** (the brief's first
shape). Statistic: `R3_W(q)` at fixed depth across `>= 4`
pre-saturation octaves at `>= 2` tower shapes; FIRES iff `R3_W` grows
superlinearly in `Lam`. Priced BEFORE running: by C-5 the growth is
bounded by the saturated ceiling `R3inf_W`, so this criterion can
only fire inside the transition, and I register the reachability
finding in advance — **multi-junction cells with a non-empty
pre-saturation band require `(n/t) c_lev > log2 n`, which at
`J >= 2` leaves only `(n=32,t=4,W={0,1})` with 1-2 admissible q.**
G-d is therefore registered as REACHABLE-BUT-STARVED and is not my
primary; I will report its 1-2 points honestly.

**(G-e) THE SHAPE / MIDDLE-PEAK DRIFT CRITERION.** Statistic:
`PeakJ` and the profile `term_j`. Registered prediction from C-3:
`PeakJ = 1` for the whole `t = n/2` family, `term_0 -> e` exactly, and
the deepest term `-> ~e`. FIRES iff `PeakJ` drifts with `q` inside a
tower (which would mean the shape is a `q` artefact, not structure).
Cheap; reported as a secondary.

## P5. THE POWER CONTROL (registered design; RUN BEFORE PROPOSING)

Our measurements are EXACT INTEGERS: there is no sampling noise, so
"power" means **do the two worlds differ at a REACHABLE cell**, and
by how many bits. Synthetic pair, both generated on the reachable
grid of P6:
- **World T** (C2''-r3 safe): `Zlev = Zinf + round(2^n q^{-T})`.
- **World F1** (floor inflation `kappa`): `Zlev = 2^{kappa*h} Zinf + round(2^n q^{-T})`.
- **World F2** (decay deficit/excess `delta`): `Zlev = Zinf + round(2^n q^{-T(1+delta)})`.
- **World F3** (intermediate stratum): `Zlev = Zinf + round(2^n q^{-T}) + round(2^{n/2} q^{-T/2})`.
Statistic S = (exact floor match) + (fitted `alpha` vs `T`) +
(fitted crossover vs `LamStar`), with the G-c firing rule.
**Registered power numbers to produce:** for each world, the minimal
parameter (`kappa`, `delta`) DETECTABLE at the reachable grid
(`kappa_det`, `delta_det`) and the minimal parameter that BREAKS the
official reserve (`kappa_brk`, `delta_brk`). The falsifier is
declared POWERED against a world iff `param_det <= param_brk`, and
UNDERPOWERED otherwise — and I will report the underpowered
directions as the falsifier's declared blind spot rather than hiding
them. **A shape that is underpowered against every false world is
not proposed.**

## P6. THE ESCALATED GB-5 GRID (registered before running)

Cost model (round-24 MITM): `cost(Zlev) = (2^lev+1)^{n/2^{lev+1}}`,
`cost(Blk_j) = cost(Z_{j+1})`; a window `W` costs `cost(Z_{w0})`.
Budget: `<= 2^22` dict entries per half. `q` grid: 2-power backbone
`k = 6..32` (CATCH-Z6), plus a QUARTER-OCTAVE refinement
`k in {k0, k0+1/4, ...}` (least prime `= 1 mod n` at each `2^k`) inside
`[log2 n, LamStar+2]` where a transition is predicted — registered as
a deliberate refinement of the 2-power grid, justified by the
predicted transition width `1/T` octaves.

Registered cells (`R3` = window measurement, `L` = level-law cell):
- `R3` J=4: `(32,16,W=0-3)` — the GB-5 cell, re-measured.
- `R3` J=3: `(16,8,W=0-2)`, `(32,8,W=0-2)`, `(32,16,W=1-3)`, `(64,32,W=2-4)`.
- `R3` J=2: `(16,4,W=0-1)`, `(32,4,W=0-1)`, `(64,16,W=2-3)`, `(128,64,W=4-5)`.
- `R3` J=1 controls: `(32,2,W=0)`, `(64,8,W=2)`, `(128,16,W=4)`.
- `L` (wide pre-saturation band, `T=1`): `(32,2,lev=1)`, `(64,4,lev=2)`,
  `(64,8,lev=3)`, `(128,16,lev=4)`, `(256,32,lev=5)`.
- `L` (`T=2`): `(32,4,lev=1)`, `(64,8,lev=2)`, `(64,16,lev=3)`, `(128,32,lev=4)`.
- `L` (`T=4,8`): whatever the cost scan says is reachable; I register
  IN ADVANCE that I expect `T >= 4` with a non-empty band to be
  UNREACHABLE, and will report the wall rather than fake the ladder.
CATCH-19B: every measured cell has `T >= 1`, `h >= 2`, `L_j >= 1` by
construction of the window, never by post-hoc filtering.

**Registered GB-5 shape question and predictions.** `RATIO_W` at
saturation: hand-computed `[law]` values `2.49 (n=16)`, `4.45 (n=32)`,
`7.86 (n=64)`, `13.8 (n=128)`, `24.5 (n=256)` for the `t = n/2`
family — **PR-F: the 4.5x GROWS, roughly linearly in `n`, at
saturation**; and **PR-E: it SHRINKS to ~0 (or goes negative) in
pre-saturation**, so the escalation's verdict should be that the
4.5x is regime-dependent and the official regime is the second one.

## P7. THE ANALYTIC ATTEMPT (D3) — registered plan

1. Verify C-1/C-2/C-3 exactly at every saturated cell (all `e`, not
   just `e = 1` as in round-24 V4).
2. Fit the two-term pre-saturation form
   `Zlev(q) = Zinf + kappa * 2^n * q^{-alpha}` on the `L` cells;
   registered prediction `alpha = T`, `kappa = 1`.
3. If (2) holds, evaluate the resulting `R3_full(Lam)` at the official
   `(n,t)` over `Lam in [41,256]` and compare with 21 — the first
   estimate of the official junction sum, labelled `[law]`.
4. Reproduce `official_scale.json:79-83` from the toy law as the
   external anchor; report any discrepancy as a catch.

## P8. Predictions (scored either way)

- **PR-A** the telescoping lemma holds exactly (brute force `n=16`).
- **PR-B** `Zinf = sigma(u,2T)^e` and `Cinf = 2^e` exact at every
  saturated cell, every `e`.
- **PR-C** `Binf = C(2^{j+1},2^j)^{h_{j+1}}` exact at every saturated cell.
- **PR-D** `alpha = T` in the deep pre-saturation band.
- **PR-E** `R3_W -> 0` in deep pre-saturation (C-5).
- **PR-F** `RATIO_W` grows ~linearly in `n` at saturation.
- **PR-G** `PeakJ = 1` for the `t = n/2` family at every `n`;
  `term_0 -> e`; no `q`-drift of `PeakJ` inside a tower.
- **PR-H** the toy law reproduces `official_scale.json`'s `128`,
  `256`, `2^-2199023255424` and `2^33*(log2 q-256)+128` exactly.
- **PR-I** POSITIVE CONTROL, GATING: round-24's `BANKED_F2B` 8/8
  bit-exact reproduction still passes with my reuse of the
  instrument. If it fails, no read is taken.

## P9. What this pilot cannot reach (registered in advance)

- `J >= 5` exact: walled at `3^16` half-states (level 1 of `n=64`).
- Multi-junction DEEP pre-saturation: walled (P4/G-d).
- The official knife-edge: the ledger's own criterion is decided at
  relative precision `107/2^33 ~ 1.2e-8` in `Lam`; **no toy at
  `T <= 2` resolves that**, so no reachable falsifier can settle
  C2''-r3 at the official row's exact `q`. What a reachable
  falsifier can settle is the FORM of the law the ledger uses. I
  register this as the declared blind spot BEFORE measuring.
- Census evidence is evidence, never proof. No status flip, no
  closure claim, nothing written outside this directory.
