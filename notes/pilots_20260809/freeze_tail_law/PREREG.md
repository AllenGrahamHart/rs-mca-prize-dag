# PREREG — freeze_tail_law (round 26)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

Round 25 (c2pp_falsifier_redesign) made C2''-r3 measurable via the
telescoping lemma and left ONE named residual obstruction: **the
freeze-tail cutoff law** — the second census term is not a pure
q^{-T} power law; it steepens near freeze and terminates in an exact
integer cutoff (measured freeze scales 14.5, 15.5, 18, 21, 22, 34, 67
versus the naive n/T). Your job: fit it, then prove it. Sources to
read FIRST: notes/pilots_20260809/c2pp_falsifier_redesign/
{REPORT.md,FABLE_AUDIT.md,PREREG.md,ckpt.json (the phase-C level
census rows — file-at-a-time, it is 35KB)}; the round-25 addendum on
critical/nodes/dli_c2pp_joint_reserve/statement.md.

## Deliverables

**D1 — THE FIT.** From the banked 275 exact level-census rows (plus
new rows where the grid is thin — reuse c2lib.py/escalate.py phase
machinery, do not rewrite), characterize the excess
Zlev(q) - Zinf near freeze: the steepening exponent, the cutoff
location as a function of (n, t, lev, e), and the integer at which it
terminates. Register a candidate functional form BEFORE fitting;
report the fit residuals against it honestly.

**D2 — THE PROOF ATTEMPT.** The excess counts non-frozen strata; the
cutoff is where the LAST non-frozen stratum dies. Attempt an exact
characterization: which stratum is last, and why does its census hit
zero at an integer scale? (Round 25's e-periodic classification of
the FROZEN stratum is the template — the closed form came from
cyclotomic factorization; the near-freeze strata should factor the
same way.) A proved cutoff law would (i) close the named obstruction,
(ii) make PR-D's alpha = T an actual theorem on its domain, and
(iii) potentially extend G-c's licensed range from log2 q <= 232
toward 256 — state exactly how far, if it lands.

**D3 — S_inf = 1/ln 2 (mint candidate).** Round 25 found
S_inf = sum_{k>=1} 2^{-k}(2^k - log2 C(2^k, 2^{k-1})) = 1/ln 2 to
full double precision. Prove it (it smells like Stirling telescoping:
log2 C(2m, m) = 2m - (1/2)log2(pi m) + O(1/m), summed against 2^{-k}).
A three-line proof mints R3inf_full(n, n/2) -> 0.4427 n as a theorem.
If the proof needs more than elementary analysis, say so and bank the
partial.

**D4 — THE (232, 256] QUESTION.** Round 25's per-level freeze law
says only levels 0/1 matter in the undecidable band. Price exactly
what a targeted exact census there would cost with the telescoping
lemma + your cutoff law (state the census size as a function of
log2 q) — is the band reachable after all? A pricing, not a run.

## Escape tests (run before the main work)

- Replay escalate.py phase A (PR-A) from a fresh scratch checkpoint —
  the lemma your work builds on (coordinator got PASS; you must too).
- Reproduce the reserve-break scale 255.999999987544 and the ledger
  rebuild (analytic.py runs read-only in place).

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md at
  or below line 3872; do not read any other round-26 pilot dir
  (b_sparsity_pose, umin_spike_hunt, m7_falsifier_hunt). Pass this
  clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT may
  extend a wall; document it.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no bulk
  loads; checkpoint long runs; background batches with results files
  for >10-min runs.
- DRAFT-ONLY: writes only in notes/pilots_20260809/freeze_tail_law/;
  read c2pp_falsifier_redesign/ freely but write NOTHING there; no
  dag/nodes/tools writes; no git; no Modal; stdlib only.
- Register predictions (incl. your candidate cutoff form) with
  numeric windows BEFORE computing; misses first. The symmetric
  not-evidence clause binds: toy silence is never official-row
  evidence in either direction; every official-scale number is
  labelled [law] with its licensed range.
- Your final message IS the report. End with a compliance paragraph.

## Pilot registrations (appended by the pilot before any computation)

Pilot: Opus, codename `freeze_tail_law`, round 26. Everything below was
written after reading only the round-25 sources named in the brief
(`REPORT.md`, `FABLE_AUDIT.md`, `c2lib.py`, `escalate.py`, `analytic.py`)
and round-24's `gb_probe.py`, and BEFORE any fit, census or numerical
experiment of my own.

**Disclosure (pre-registration hygiene).** Before writing this section I
ran one structural peek at `c2pp_falsifier_redesign/ckpt.json` under
`tools/ramguard tiny` that printed only the top-level key names and the
number of q-rows per phase-C cell (11 cells, 275 rows). No census value,
no freeze scale and no fit output was read. I count that as reading a
source, not as computing, but I declare it.

### P0 — the object, restated exactly

For `n, t` powers of two, `lev >= 0`, put `u = 2^lev`, `h = n/2^lev`,
`T = t/2^lev >= 1`, `e = n/(2t)`, so that `h = 2Te`. For a prime
`q = 1 mod n` and `zeta` of exact order `h` in `F_q`, the banked level
census (`gb_probe.level_vectors` + `mitm_null_count` + `binom_alpha`) is

    Zlev(q) = SUM over c in {0..u}^h with  SUM_i c_i zeta^{r i} = 0 (mod q)
              for r = 1..T,   weighted by  PROD_i C(u, c_i).

Write `C(X) = SUM_i c_i X^i`. The condition at frequency `r` is
`C(alpha) = 0 (mod q)` at `alpha = zeta^r`, of exact order
`d_v = h/2^v` where `v = v_2(r)`; `v` runs over `0..tau`,
`tau = log2 T`, and the number of imposed frequencies at valuation `v`
is `g_v = T/2^{v+1}` for `v < tau` and `g_tau = 1`.

### P1 — CANDIDATE FUNCTIONAL FORM OF THE CUTOFF (the registered law)

**L1 (cutoff theorem, registered as a claim with proof sketch).** A
non-frozen `c` (i.e. not `e`-periodic) fails `Phi_{d_v} | C` for some
`v <= tau`; then `Res(Phi_{d_v}, C) = Norm(C(zeta_{d_v}))` is a NONZERO
rational integer, `q^{g_v}` divides it (the `g_v` imposed roots are
distinct mod `q`, `Phi_{d_v}` splits with distinct roots since
`q = 1 mod n` and `q` is odd), and Hadamard bounds it by
`(a_v sqrt(m_v))^{m_v}` with `m_v = h/2^{v+1} = deg Phi_{d_v}` and
`a_v = u 2^v` (the reduction `C mod (X^{m_v}+1)` is an alternating sum
of `2^{v+1}` coefficients each in `[0,u]`). Hence

    log2 q  <=  B(n,t,lev) := max_{0<=v<=tau} (m_v/g_v) * (lev + v + 0.5*log2 m_v)

and **`Zlev(q) = Zinf` for EVERY prime `q = 1 mod n` with
`log2 q > B(n,t,lev)`.** The cutoff is an exact integer because it is a
maximum of finitely many nonzero integer norms over a finite box.

**Registered per-cell numeric values of `B` for the eleven banked
phase-C cells** (computed by hand from the formula above, before
looking at any census value):

| cell (n,t,lev) | u | h | T | e | tau | **B** | naive n/T |
|---|---|---|---|---|---|---|---|
| (32,2,0)  | 1  | 32 | 2 | 8 | 1 | **32** | 16 |
| (32,2,1)  | 2  | 16 | 1 | 8 | 0 | **20** | 32 |
| (32,4,0)  | 1  | 32 | 4 | 4 | 2 | **20** | 8  |
| (32,4,1)  | 2  | 16 | 2 | 4 | 1 | **20** | 16 |
| (64,4,2)  | 4  | 16 | 1 | 8 | 0 | **28** | 64 |
| (64,8,2)  | 4  | 16 | 2 | 4 | 1 | **28** | 32 |
| (64,8,3)  | 8  | 8  | 1 | 4 | 0 | **16** | 64 |
| (64,16,3) | 8  | 8  | 2 | 2 | 1 | **16** | 32 |
| (128,16,4)| 16 | 8  | 1 | 4 | 0 | **20** | 128 |
| (128,32,4)| 16 | 8  | 2 | 2 | 1 | **20** | 64 |
| (256,32,5)| 32 | 8  | 1 | 4 | 0 | **24** | 256 |

**L2 (which stratum is last).** The argmax above is `v* = tau - 1` when
`T >= 2` and `v* = 0` when `T = 1`. Registered claim: the LAST
non-frozen stratum is `S* = {c : Phi_{d_v} | C for all v != v*,
Phi_{d_{v*}} nmid C}`, carrying exactly ONE residual mod-`q` condition
(`g_{v*} = 1` in both cases), and it is the unique stratum whose
entropy-to-condition ratio is maximal.

**L3 (negacyclic reduction, `T = 1` only).** For `T = 1` (so `h = 2e`)
the whole census collapses onto `A = C mod (X^e + 1)`, `A_i = c_i -
c_{i+e} in [-u,u]`, with Vandermonde weight `C(2u, u+A_i)`:

    Zlev(q) = SUM over A in [-u,u]^e with SUM_i A_i zeta^i = 0 (mod q)
              of PROD_i C(2u, u + A_i)
            = mitm_null_count([(zeta^i,)]_{i<e}, skew_alpha(2u), q, 1).

`A = 0` reproduces `Zinf = C(2u,u)^e = sigma(u,2)^e`. This turns an
`(u+1)^{h/2}`-state MITM into a `(2u+1)^{e/2}`-state one.

### P2 — PREDICTIONS, with numeric windows (misses reported first)

- **PR-1 (reduction is exact).** L3 reproduces the banked `Zlev` bit-exactly
  on every banked q-row of the five `T = 1` cells
  {(32,2,1),(64,4,2),(64,8,3),(128,16,4),(256,32,5)}. Window: **0
  mismatches**; any mismatch refutes L3.
- **PR-2 (cutoff theorem holds on banked data).** Among all 275 banked
  phase-C rows, the number with `log2 q > B(n,t,lev)` AND
  `Zlev > Zinf` is **exactly 0**. Any such row refutes L1.
- **PR-3 (the bound is not vacuous).** Let `Lmax(cell) = max{log2 q :
  banked row has Zlev > Zinf}`. Predict `Lmax <= B` for all 11 cells
  (implied by PR-2) and additionally `B - Lmax <= 12` bits for **at
  least 6 of the 11** cells.
- **PR-4 (exact integer cutoff).** For the five `T = 1` cells the exact
  cutoff `Q*(cell) = max{q prime, q = 1 mod n : Zlev(q) > Zinf}` is
  found by scanning `q` downward from `2^B` with the L3 census.
  Predict `log2 Q* in [0.5*B, B]` for every one of the five, i.e.
  (32,2,1) in [10,20]; (64,4,2) in [14,28]; (64,8,3) in [8,16];
  (128,16,4) in [10,20]; (256,32,5) in [12,24].
- **PR-5 (the measured "freeze scales" 14.5..67 are grid artefacts).**
  Every reported freeze scale is the FIRST tested grid point above the
  cell's true cutoff, not the cutoff. Predict: for each cell,
  `freeze_reported >= Q*` and `freeze_reported` is the smallest grid
  point of round 25's ladder exceeding `log2 Q*`. Window: holds for
  **>= 5 of the 7** reported freeze scales.
- **PR-6 (steepening, and the tail-cleaned refit).** The pure power law
  `log2(Zlev - Zinf) = n + log2 kappa - alpha*Lam` with `alpha = T`,
  `|log2 kappa| < 2` is a DEEP-BAND law only (`Lam <= LamStar`); the
  local slope over the last two decades before `Q*` exceeds `T` by
  `>= 15%` in **>= 3** cells. Refitting `alpha` on points with
  `Lam <= LamStar` only, predict
  `max |alpha/T - 1| in [0.00, 0.05]` over cells with `>= 4` fit
  points (round 25 got 0.0668 with a contaminated window).
- **PR-7 (licensed range).** With `eps := max|alpha/T - 1|` from PR-6,
  G-c's F2-powered range becomes `log2 q <= 256/(1+eps)`. Predict the
  new bound lands in **[243.8, 253.5]** (round 25: 232.7). I do NOT
  predict it reaches 256; `eps -> 0` is unattainable from toys.
- **PR-8 (S_inf).** `S_K := sum_{k=1..K} 2^{-k} c_k` with
  `c_k = 2^k - log2 C(2^k, 2^{k-1})` satisfies the EXACT identity
  `S_K = K - 2^{-K} log2((2^K)!)` (telescoping of
  `2^{-k} log2 (2^k)! - 2^{-(k-1)} log2 (2^{k-1})!`), hence by Stirling
  `S_inf = log2 e = 1/ln 2` and
  `log2 e - S_K = 2^{-(K+1)} log2(2 pi 2^K) + O(4^{-K})`.
  Predict: the identity holds to `< 1e-12` for `K = 1..18`, and the
  ratio `(log2 e - S_K) / (2^{-(K+1)} log2(2 pi 2^K))` is within
  **1%** of 1 for `K >= 12`.
- **PR-9 (D4 pricing).** Predict the official `(232,256]` band is NOT
  reachable by exact census: the cheapest reduced census at level
  `lev` for `n = 2^41, t = 2^33` costs at least
  `(2^{lev+1}+1)^{n/2^{lev+2}}` states, minimised over admissible
  `lev` at `>= 2^{2^{30}}` — no cutoff law changes this, because the
  official row at `log2 q <= 256` sits at `Lam <= LamStar(0) = 256`,
  i.e. entirely INSIDE the deep band, never in the freeze tail.
  Predicted answer to "is the band reachable after all": **NO** by
  census; the band moves only through PR-7.

### P3 — declared divergences

- **D-15 (root convention for new rows).** For NEW q-rows I may pick
  `zeta` as `x^{(q-1)/h}` for a random `x` instead of round-24's
  `least_primitive_root` convention, because `least_primitive_root`
  trial-divides `q-1` (C25-8). The census is INVARIANT under the choice
  of primitive `h`-th root: the index map `i -> s i mod 2m` on the
  negacyclic algebra permutes coordinates with signs and the weights
  `C(2u, u+a)` are even in `a`. I will verify agreement with `get_zeta`
  on at least 3 banked rows before using it.
- Escape tests are run before the main work, as briefed; they are
  replays of round 25, not new measurements.

