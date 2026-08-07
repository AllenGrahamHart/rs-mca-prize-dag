# PRE-REGISTRATION — MYSTERY 2 (F2): the 8.60 R-locality deficit (round 22)

Round 22, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: mystery 2's sharpest
open edge. The tail-count criterion of record binds at ZERO flat
margin (binding layer c* = 1/ln2 - 1), and the known local route
loses a factor 8.60 to R-locality. Diagnose whether that factor is
STRUCTURAL (a proved floor for R-local arguments) or an artifact of
the specific estimate — and in either case say what mystery 2
actually needs.

## 0. Sources (quote verbatim first — use the NODES OF RECORD, not
memory; constants have been force-corrected before)
- background/nodes/f2_z1_mass_knife_edge/ — statement + the three
  forced-correction addenda (CATCH-T3 constant 4.0; route-(b)
  sizing struck; the tail-count criterion of record with the
  binding layer c* = 1/ln2 - 1 at zero flat margin; the R-locality
  deficit factor 8.60). Quote the criterion and the deficit
  derivation with file:line.
- notes/pilots_20260806/tail_count/ — the round-20 pilot that
  normalized the criterion; its verifier is the baseline.
- background/nodes/f2_o1_status_split/ + addenda — the (O1) status
  of record (FALSE as posed; the finite target Z(L) <= 1 + N^3
  under calibration (C); the Z_1 window [2^17.98, 2^22.75]).
- notes/pilots_20260806/f2_repose/ — the re-pose of record.

## 1. Deliverables
- (D1) THE DEFICIT MADE EXACT: re-derive the 8.60 factor from the
  node of record. WHERE does R-locality lose it (which inequality,
  which layer)? Decompose the loss into named per-step factors
  whose product is 8.60; verify the decomposition numerically at
  the binding layer.
- (D2) THE SHARPENING ATTEMPT: attack the single lossiest step at
  toy rows (2-power grids, p = 1 mod N', NO shift-0 cells —
  CATCH-19B). Can any R-local improvement (longer windows, higher
  moments, better union structure — name each attempt) beat its
  factor? Prediction registered per attempt before computing.
- (D3) THE STRUCTURAL TEST: formulate the class of R-local
  arguments precisely (what "R-local" quantifies over — window
  length, moment order, locality radius), then either (a) exhibit
  an R-local estimate beating 8.60 at toy scale (the deficit is an
  artifact — quantify the best factor achieved), or (b) prove a
  toy-scale floor: NO estimate in the formalized class beats
  factor X > 1 (state X honestly; a floor at toy scale is evidence,
  a proved floor uniform in the row is a theorem — label which you
  get).
- (D4) THE GLOBAL INPUT: if the factor looks structural, name the
  weakest NON-local input that would close the gap (a global
  cancellation, a spectral bound, an ensemble average — with the
  exact statement it must have and what supplies it in the banked
  campaign, if anything). This becomes mystery 2's next brief.

## 2. Falsifiers / honesty
- Zero flat margin means ANY loss kills the route — but do not
  equate "this route dies" with "the criterion is false"; keep the
  criterion / route / factor distinction explicit throughout.
- If (D1) finds the 8.60 constant itself wrong (a forced
  correction), that is a first-class deliverable: derive the right
  constant, show the arithmetic, flag for the coordinator — do NOT
  edit the node.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260807/f2_rlocality/. Never edit
  dag.json/nodes/tools; no git; no Modal. COMPUTE LAW: every
  python3 invocation via tools/ramguard tiny|local -- python3 ...
  (literal --), from repo root, INCLUDING file patching and JSON
  peeking. 2-power toy grids (CATCH-Z6); no shift-0 cells
  (CATCH-19B). Name every measured functional (CATCH-19C).
  Verbatim quotes with file:line. No REPORT.md — your final message
  IS the report. QUARANTINE: do not read
  notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line 2487
  (the "ROUND 22 LAUNCHED" marker); do not read the other round-22
  pilot dirs (l1_ell_sweep, ge_floor_falsifier, bb_nu_transport);
  PASS THIS QUARANTINE CLAUSE VERBATIM to any subagent you
  dispatch.

---

# PILOT REGISTRATIONS (Opus 5, round 22, 2026-08-07)

Appended BEFORE any computation. Nothing below was run, peeked at, or
tuned first. Priors are my honest pre-computation credences.

## A. Notation fixed for this pilot (all functionals NAMED — CATCH-19C)

    L        := log2 p            (= 63.999999355 at the official row)
    R/S      = 1/L                (saturation, statement.md:15)
    d(c)     := -2 log2|cos(pi c/p)|,  cost(u) := sum_{s<S} d(c_s(u))
    log2 P(u) = S - cost(u)                    (tail_count THEOREM 1)
    eta_c    := 2^c - 1                        (tail_count THM 11 / route_b Lemma 5)
    I_FLAT(c)  := flat-model rate of {P >= 2^{cS}}, per S
                  (= sup_th(th c - Lambda(th)), Lambda = log2 C(2th,th) - th;
                   I_FLAT(c*) = c* by COROLLARY ZM; I_FLAT(1) = L exactly at finite p)
    J_FLAT(eta):= flat-model rate of {V_1/|H| >= eta}, per S
                  (= sup_th(th eta - log2 I_0(th ln2)); J_FLAT(1) = L at finite p)
    I_INSTR(c) := exponent per S actually certified by the ONE executable
                  R-local instrument (Lemma 5 AM-GM -> V_1 -> Z-2 moment
                  N_k <= (2k-1)!!|H|^k -> Chebyshev, k <= R):
                  = log2(e) eta_c^2                 if eta_c^2 <= 1/L   (free-k branch)
                  = (1/L) log2(e eta_c^2 L)         otherwise           (k = R branch)
    DEF_INSTR(c) := c / I_INSTR(c)          [THE INSTRUMENT DEFICIT AT LAYER c]

Four named per-step loss factors (D1 decomposition), each >= 1 unless stated:

    THETA(c) := c / I_FLAT(c)                      [LAYER factor: requirement vs truth]
    AMGM(c)  := I_FLAT(c) / J_FLAT(eta_c)          [Lemma-5 linearization loss]
    GAUSS(c) := J_FLAT(eta_c) / (log2(e) eta_c^2)  [Gaussian/(2k-1)!! moment-shape loss]
    CAP(c)   := log2(e) eta_c^2 * L / log2(e eta_c^2 L)   [LOCALITY CAP k <= R loss]

    IDENTITY CLAIMED: DEF_INSTR(c) = THETA(c) * AMGM(c) * GAUSS(c) * CAP(c).

## B. D1 registrations (the deficit made exact)

- **P1 (arithmetic).** `L / log2(e L)` at `L = 63.999999355` reproduces
  `8.60` to `8.599 +- 0.005`. Prior 0.95.
- **P2 (WHERE it lives).** `8.60` is NOT a layer-free constant: it is
  exactly `DEF_INSTR(1)`, i.e. the instrument's deficit at layer `c = 1`
  and nowhere else; equivalently it is the multiplicative failure margin
  of COROLLARY 8's inequality `log2(e log2 p) >= log2 p`
  (`tern_route_b/PROOFS.md:409`). Prior 0.85.
- **P3 (the layer error — a candidate FORCED CORRECTION).** The node
  applies `8.60` at the BINDING layer `c* = 1/ln2 - 1`
  (`statement.md:76-84`), but `DEF_INSTR(c*) != 8.60`. I predict
  `DEF_INSTR(c*) = 6.32 +- 0.03`. Prior 0.80.
- **P4 (the third number).** `tail_count/PROOFS.md:441-443`'s own two
  stated numbers have ratio `0.443/0.116 = 3.81`, which is neither 8.60
  nor `DEF_INSTR(c*)`; the `0.116` is `I_INSTR(1)`, not `I_INSTR(c*)`.
  I predict `I_INSTR(c*) = 0.0701 +- 0.0005` (not 0.116). Prior 0.80.
- **P5 (decomposition at c = 1).** `THETA(1)*AMGM(1)*GAUSS(1)*CAP(1)`
  reproduces `8.599` to better than 0.5%, with
  `THETA(1) = 1/64`, `AMGM(1) = 1.000`, `GAUSS(1) = 44.36 +- 0.5`,
  `CAP(1) = 12.41 +- 0.05`. Prior 0.70.
- **P6 (decomposition at c*).** `THETA(c*) = 1.000` (zero margin),
  `AMGM(c*) = 2.29 +- 0.06`, `GAUSS(c*) = 1.04 +- 0.02`,
  `CAP(c*) = 2.65 +- 0.05`, product `= DEF_INSTR(c*)` to better than 1%.
  Prior 0.70.
- **P7 (the lossiest step at the binding layer).** LOCALITY CAP (`CAP`),
  narrowly ahead of `AMGM`. Prior 0.55 (a coin-flip between these two;
  I register CAP).
- **P8 (worst layer).** `min_c DEF_INSTR(c) ~ 5.97 +- 0.10` attained near
  `c = 0.30`; `DEF_INSTR` is NOT monotone. Prior 0.6.

## C. D2 registrations (the sharpening attempts — one prediction each,
   all registered before running)

- **A1 "DROP-AMGM" (type/binomial-moment bound on the cost sum directly,
  no Lemma 5, no `V_1`).** Named functional `I_TYPE(c) := (k/S) *
  min{D(nu||mu) : E_nu[d] <= 1-c}` (`D` in bits, `mu` uniform on `F_p`).
  PREDICTION: removes `AMGM` entirely but is WORSE overall — I predict
  `I_TYPE(c*) ~ 0.0069` at `k=R` and `~0.0138` at `k=2R`, i.e. deficit
  `64` / `32`, far worse than 6.32. **A1 FAILS.** Prior 0.65.
- **A2 "TRUNCATED-MOMENT" (one-sided k-th moment on `min(X_s,-M)`-truncated
  cost sum, `k = 2R`).** Named `I_TRUNC(c) := (1/L) log2((1+c)^2 L /
  (2 Var(d)))`. PREDICTION: `I_TRUNC(c*) = 0.051 +- 0.004`, deficit
  `8.6 +- 0.7` — WORSE than 6.32. **A2 FAILS.** Prior 0.55.
- **A3 "NO-POSITION-ENTROPY" (repair of tail_count THEOREM 10: replace the
  union bound `|U_c| <= C(S,R) m^R` by the binomial-moment bound
  `Pr[N_A >= m] <= E[C(N_A,R)]/C(m,R)`).** Named `I_BINOM(c) :=
  max_delta (1/S) log2[ C((1-delta)S, R) / (C(S,R) rho(D)^R) ]`,
  `D = (1-c)/delta`, `rho(D) = (2/pi) arccos(2^{-D/2})`.
  PREDICTION (two parts): (i) the position entropy `H(1/L)` CANCELS, so
  THEOREM 10's verdict "dies at EVERY p / no threshold in p" is an
  ARTIFACT of the union bound, not a property of the supply — prior 0.75;
  (ii) even repaired it is far short: `I_BINOM(c*) = 0.0017 +- 0.0005`,
  deficit `~260`. **A3 FAILS numerically but corrects a banked verdict.**
  Prior 0.60 on the number.
- **A4 "HIGHER MOMENTS k > R".** PREDICTION: `N_k <= (2k-1)!!|H|^k` FAILS
  at `k = R+1` on toy rows (banked at G2: `N_2 = 1104 > 768`,
  `tern_route_b/PROOFS.md:399-401`); I re-measure at G1 and G4 and predict
  failure at `k = R+1` there too. **A4 FAILS (the cap is sharp).** Prior 0.85.
- **A5 "LONGER WINDOW" (raise R at fixed S).** PREDICTION: `DEF_INSTR`
  improves like `L/log2(...)` only if `R/S` may exceed `1/L`, which
  saturation forbids (Z-NOGO). At admissible `R/S = 1/L` there is no
  gain. **A5 FAILS structurally, not numerically.** Prior 0.90.
- **A6 "BEST-OF" control.** `min over A1..A5 and the banked instrument of
  the deficit at c*`. PREDICTION: the banked instrument (6.32) wins; no
  attempt beats it. Prior 0.65.

## D. D3 registrations (the formalized class and the floor)

**FORMALIZED CLASS (this is what I will prove floors against).**

> `k-LOCAL(k)`: an upper bound `B` on `Pr_u[cost(u) <= (1-c)S]` is
> `k-LOCAL` iff `B` is valid for EVERY random vector `X = (X_1..X_S)` on
> `F_p^S` whose every `k`-subset marginal is uniform on `F_p^k`.
> QUANTIFIES OVER: the locality radius `k` (how many coordinates any one
> certificate may see); the moment order (a derived quantity, `<= k`);
> the window length (enters only through which `k`-wise marginals are
> uniform). NOT quantified over: anything using the identity of the code.
>
> `OPT_k(c) := max { Pr[cost <= (1-c)S] : X has k-wise uniform marginals }`
> `I_LOC_k(c) := -(1/S) log2 OPT_k(c)`   (the class's best exponent)
> `FLOOR_k(c) := c / I_LOC_k(c)`         (NO k-LOCAL bound beats this)

The object supplies STRICTLY MORE than `R`-wise uniformity (THEOREM Z-2
adds `l1`-restricted moment matching to order `2R`) and STRICTLY LESS
than `2R`-wise uniformity (the MDS value code is exactly `R`-wise
independent, dual distance `R+1`). So `k = R` and `k = 2R` BRACKET the
object's actual supply, and I will report both.

**LIFTING LEMMA (to be proved, then used).** Every exchangeable
`k`-wise-independent Bernoulli(`rho`) law on patterns `{A,B}^S` lifts to a
`k`-wise-uniform law on `F_p^S` with `Pr[all coordinates in A]` equal to
the pattern law's `Pr[all ones]`, provided `|A|` and `|B|` admit `k`-wise
uniform codes of length `S`. Consequently `OPT_k(c) >= OPTPAT_k(rho,S)`
where `OPTPAT` is the (tiny) two-bin pattern LP
`max{ Pr[N=S] : E[C(N,j)] = C(S,j) rho^j, j = 0..k }`, `rho = rho(1-c)`.

- **P9 (the sharpest falsifier of "8.60 is structural").** At `c = 1`,
  `OPT_R(1) = p^{-R}` EXACTLY, so `FLOOR_R(1) = 1`: `R`-locality costs
  NOTHING at `c = 1` — which is precisely the layer where `8.60` was
  computed, and precisely the layer already PROVED outright by
  tail_count THEOREM 12. Prior 0.85.
- **P10 (the floor at the binding layer, official parameters).** Via the
  LIFTING LEMMA and the Hermite/Chebyshev-system asymptotics of `OPTPAT`,
  `FLOOR_R(c*) = 6.2 +- 0.4` and `FLOOR_{2R}(c*) = 3.5 +- 0.3`. Prior 0.50
  (I am least confident here).
- **P11 (near-optimality).** `DEF_INSTR(c*) = 6.32` lies within 5% of
  `FLOOR_R(c*)`: the banked instrument is essentially OPTIMAL in
  `R-LOCAL(R)` at the binding layer, and at most `~1.8x` from
  `R-LOCAL(2R)`. Prior 0.45.
- **P12 (exact small-row LP validation).** The FULL exchangeable LP at G1
  (`p=17, S=8, R=2`, alphabet folded to 9 cost classes, 12870 states) is
  solvable exactly; its optimum at `c = 1` equals `p^{-R} = 1/289` to
  `1e-9`, and at intermediate `c` it EXCEEDS the lifted two-bin value
  `OPTPAT` (the lifting lemma is a valid but not sharp floor). Prior 0.70.
- **P13 (L-dependence).** `FLOOR_k(c*)` grows with `L`; measured across
  toy rows with different `L` the growth is consistent with `Theta(L /
  log2 L)`, NOT `Theta(L)`. Prior 0.55.

## E. D4 registration (the global input)

- **P14.** I predict the weakest sufficient NON-local input is a
  **box/smoothness count for the value code at exponential scale**:
  `#{u : #{s : f_u(zeta^s) in A} >= (1-delta)S} <= p^{R} rho(A)^{Theta(S)}`
  for a single interval `A` — i.e. "no codeword of `C*` is unusually
  smooth", at a strength no `k`-wise statement can give because it
  quantifies over `Theta(S)` coordinates at once. I predict NOTHING in
  the banked campaign supplies it (Weil vacuous by 26.000 bits; Poisson
  circular), and that the only banked object of the right locality is the
  constant-weight Z-FLOOR cell. Prior 0.6.

## F. Falsifiers / honesty clauses (mine)

1. If `L/log2(eL) != 8.60 +- 0.01`, P1 dies and the node's constant is
   wrong in a way I did not predict — I report that instead.
2. If the four-factor product misses `DEF_INSTR` by more than 2% at
   either layer, the decomposition is WRONG and I report it as wrong, not
   as "approximately right".
3. If the G1 full LP returns `> p^{-R}` at `c = 1`, my LP is mis-built
   (tail_count THEOREM 12 is a proof that `p^{-R}` is exact) — I retract
   the LP and report the failure.
4. A floor computed at toy rows or by asymptotics is EVIDENCE, not a
   theorem. A floor uniform in the row would need the LIFTING LEMMA plus
   an exact `OPTPAT` at official `S`; I do not expect to have the latter
   and will label `FLOOR` values as ASYMPTOTIC/EVIDENCE unless proved.
5. CRITERION / ROUTE / FACTOR stay distinct: nothing here bears on
   whether the tail-count criterion is TRUE, only on what `R`-local
   instruments can certify.
6. Calibration clause (`statement.md:92-98`) honoured: no toy is evidence
   about `Z_1` at the official row. Toys here verify IDENTITIES and LP
   OPTIMA only.
7. Grid: 2-power `2N` only (CATCH-Z6, automatic since `S = 2^{e_p-1}`);
   `Lambda = {1,3,...,2R-1}` so exponent `0` never occurs (CATCH-19B,
   asserted in code); every measured functional named above.
8. If any prediction misses I report it as a MISS, not absorbed.

