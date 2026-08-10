# PREREG — b_sparsity_pose (round 26)

Coordinator brief, written before dispatch. The pilot appends its own
registrations (predictions, thresholds, escape tests) BELOW the brief
BEFORE any computation.

## Mandate

The user ratified (2026-08-09) the mystery-5 narrowing: **(b)
o(1)-sparsity primary, (a) exhibit-scoped fallback, (c) withdrawn**
(decision record: critical/nodes/integer_code_distance_cert/statement.md,
final section). Your job: turn (b) from a slogan into a conjecture of
record that can be attacked, priced, and someday proved.

## Deliverables

**D1 — THE POSE.** State (b) in weakest usable form. Constraints:
- It must be exactly what the measured suppression law asserts and no
  more: bad-prime density o(1) in admissible windows, uniformly in
  v_2 (round-25 ground truth: BADFRAC flat across v_2 at h=8
  exhaustive; K=1 population law at h=64 after the LAW-2 cofactor
  split; W_TOP density ~2^-112). Sources to read FIRST:
  notes/pilots_20260809/large_v2_hunt/{REPORT.md,FABLE_AUDIT.md} and
  the round-25 addendum on integer_code_distance_cert.
- Name the quantifiers exactly (which windows, which h, what "o(1)"
  is measured against — vector count? prime count? orbit count?).
  Round 24's lesson (CATCH-24C): the filter bar must be named per
  consumer. State which consumer(s) of integer_code_distance_cert
  need which form, by reading their statements.
- PRE-REGISTER at least two falsifiers with power controls (the
  round-23 rule: an unpowered falsifier is not a falsifier). At
  least one must be reachable this round; run it.

**D2 — LAW 2 GENERAL-w (named gap 1).** Round 25 proved
Norm(1+2v) = 1 + 2h*v_{h/2} (mod 4h) for w = 1+2v (nodd = 1) by
Newton's identities. Attempt the general-w form (the nodd >= 3
strata). The machine-check harness exists
(notes/pilots_20260809/large_v2_hunt/d3_thm.py — reuse, do not
rewrite). A proved general form hardens the (b) instrument; a
counterexample to any natural generalization is equally bankable.
Register your candidate formula BEFORE testing it.

**D3 — BOX DEPTH (named gap 2).** Box realization of 2-adic norm
classes is measured only to depth 2^17. Push the depth as far as the
1G wall allows (register the target depth + the expected-if-uniform
class counts first). A gap between realized and available classes at
depth D would be STRUCTURE — exactly what (b)'s uniformity needs to
know about.

**D4 — VERDICT.** Is the pose self-consistent with every banked
measurement (h=8 exhaustive, h=64 ladder, the four Proth rows, the
E1-128 certificate)? Any tension is a finding, not a failure.

## Escape tests (run before the main work)

- Reproduce the h=8 pooled BADFRAC 0.1115 and the W_TOP 2^-112
  density from the banked data/scripts (calibration, not discovery).
- Verify the LAW-2 identity suite still passes (0 violations) before
  building on it.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md at
  or below line 3872; do not read any other notes/pilots_20260809/
  round-26 pilot dir (b_sparsity_pose is yours; umin_spike_hunt,
  freeze_tail_law, m7_falsifier_hunt are not). Pass this clause to
  any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root
  /home/u2470931/smooth-read-solomin/prize — including file patching
  and JSON peeking. RAMGUARD_TIMEOUT may extend a wall; document it.
  Harness Write/Edit tools are fine for authoring.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json (use
  node.json shards + grep); no bulk directory loads; checkpoint any
  run that could exceed its wall; background batches with results
  files for >10-min runs.
- DRAFT-ONLY: no edits outside notes/pilots_20260809/b_sparsity_pose/;
  no dag.json/nodes/tools writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing; report
  misses first. Name every measured functional (CATCH-19C). No
  shift-0 cells (CATCH-19B). Own-repo grep before claiming any lemma
  is missing (CATCH-24A).
- Your final message IS the report (the coordinator persists it
  verbatim). End with a compliance paragraph.

## Pilot registrations (appended by the pilot before any computation)

Opus pilot, 2026-08-09, written BEFORE any computation in this session.
No python3 has been invoked at the time of writing; only file reads
(this brief; large_v2_hunt/{REPORT,FABLE_AUDIT,PREREG}.md;
integer_code_distance_cert/{statement,status_ruling}.md;
lattice_cone_certificate/conditional.md; generator_economy/statement.md
lines 85-112; u2_per_row_certifier/statement.md;
kernel_lattice_reframing/statement.md;
dli_norm_gate_energy_ceiling/statement.md;
e1_folded_no_vector_certificate_256_payload/{PRO_W3_e1_density,retired_proof}.md;
e1_official_typicality_or_certificate/statement.md;
e1_open_cell_control_payload/statement.md; plus greps).
Everything below is binding; deviations are recorded as explicit
self-corrections in the final report.

### R0 — objects and named functionals (CATCH-19C)

`N' = 2^m >= 16`, `h = N'/2`, `R_h = Z[x]/(x^h+1) = Z[zeta_{N'}]`,
`BOX_h = {-2..2}^h`, `Norm(w) = prod_{j odd mod N'} w(zeta^j) = det(mult_w)`.

- **ODDBOX_h** := `{w in BOX_h : Norm(w) odd} = {w : sum_i w_i odd}`.
- **CEIL(h)** := `(4h-3)^{h/2}`  (candidate proved ceiling, LEM-1 below).
- **BAD(N')** := `{p odd prime : exists w in BOX_h \ {0} with p | Norm(w)}`.
  By the banked fold reduction (`kernel_lattice_reframing` PROVED +
  round-22 `integer_code_distance_cert` addendum lines 54-57) this is
  exactly the set of row primes whose kernel lattice `K_p` carries a
  non-cyclotomic ternary vector of support `<= 2l'`, for ANY support
  bound `2l' <= N'` (the fold of a full-support ternary vector is still
  in `BOX_h`, so the count below is uniform in `2l'`).
- **W_ADM** := `(2^{N'}, CEIL(h)]`; at `N'=128`, `(2^128, 253^32]`.
  **W_DEP** := `[2^166, 2^172)`. **W_TOP** := `[2^244, 253^32]`.
- **PI(W)** := `#{p prime in W : p = 1 mod N'}`;
  **PI_v(W)** := same with `v_2(p-1) >= v`.
- **BADCOUNT(W)** := `#(BAD ∩ W)`; **BADDENS(W)** := `BADCOUNT(W)/PI(W)`;
  **BADDENS_v(W)** := `#(BAD ∩ W ∩ {v_2(p-1) >= v}) / PI_v(W)`.
- **CLASSES(h)** := number of distinct values of `Norm` on `BOX_h`;
  **ORB(h)** := the norm-preserving group `<-1, x, Gal>` of order `<= 2h^2`.
- **RPRIME(y,h)** := `floor(log_y CEIL(h))` = max number of prime factors
  `> y` (with multiplicity) of any box norm.
- **VSPARSE(N')** := `sup{v : the proved upper bound on BADDENS_v(W_ADM)
  is < 1}` — the `v_2` level at which the counting proof goes vacuous.
- **s(w)** := `((Norm(w)-1)/(2h)) mod 2` for odd `Norm(w)` (the LAW-2 bit).
- **sigma(u)** := `s(lift_{0/1}(u))` for `u in F_2[x]/(x^h+1)` of odd weight.
- **REAL(D)** := `#{Norm(w) mod 2^D : w in ODDBOX_h}` (realized 2-adic
  classes at depth `D`); **AVAIL(D)** := `2^{D-m}` = `|(1+2hZ)/2^D|`.
- **Mcc(D)**, **Mcol(D)** := coupon-collector and collision estimators of
  `REAL(D)` from `n` samples.
- **BADFRAC8(v)** := round-25's h=8 exhaustive functional, reused verbatim.

### R1 — D1: the pose I will state, and the theorem I will attempt

**CONJ-B (the pose, weakest usable form) — to be stated in full in the
report; registered skeleton:** for every 2-power `N' >= 32` and every
window `W` inside `W_ADM(N')` of length `>= 1` dyadic octave,
`BADDENS_v(W) <= eps(N')` with `eps(N') -> 0` as `N' -> infinity`,
UNIFORMLY in the `v_2`-stratum `v`. The consumer bar is named per
consumer (CATCH-24C): `lattice_cone_certificate/conditional.md:41-45`
needs a per-row certificate for EACH assigned knife-edge row, so
sparsity serves it only under the row-SELECTION reading; the
`generator_economy` GE-WEAK universal reading (statement.md:104-112) is
the one (b) actually replaces.

**Attempted theorem (registered as an attempt, not an assumption):**

- **LEM-1 (ceiling).** For `w in ODDBOX_h`: `0 < Norm(w) <= (4h-3)^{h/2}`.
  Route: banked `dli_norm_gate_energy_ceiling` LN4 (PROVED:
  `Norm <= E^{h/2}`, `E = sum a_i^2`) plus parity (`sum w_i` odd forces
  at least one `|w_i| = 1`, so `E <= 4(h-1)+1 = 4h-3`).
  PREDICTION: 0 violations, h=8 exhaustive (`MAXNORM = 614656 <= 29^4 =
  707281`) and random samples at h=16,32,64.
- **LEM-2 (pigeonhole).** If `y >= CEIL(h)^{1/2}` then every box norm has
  at most ONE prime factor `> y`, with multiplicity. PREDICTION:
  `CEIL(64)^{1/2} = 253^16 = 2^127.7 < 2^128` = the `W_ADM` floor, so
  `RPRIME = 1` on all of `W_ADM` at `N'=128` with a margin I predict lies
  in `[0.2, 0.4]` bits; and the margin is NEGATIVE for `h >= 128`, so
  general `N'` needs `RPRIME = ceil(log2(4h-3)/8)`.
- **THM-SPARSE (counting bound).**
  `BADDENS(W) <= RPRIME * CLASSES(h) / PI(W)`.
  Numeric predictions at `N'=128`, `W = W_ADM` (to be computed):
  `log2 BADDENS <= -93 +- 3` without orbit reduction and `<= -106 +- 3`
  with the full `2h^2 = 8192` orbit reduction.
- **VSPARSE prediction:** `VSPARSE(128) in [108, 118]`. Consequence I
  predict and will check: the four deployed Proth rows (`v_2 = 92,93,95,97`)
  are INSIDE the proved range; the E1-128 pinned field (`v_2 = 200`) is
  OUTSIDE it (covered instead by its per-row certificate).

**PRIOR-ART SUBTRACTION, stated before computing (hard law 5, fifth
surface).** The same union bound already exists in our own repo as a
RETIRED attempt:
`background/nodes/e1_folded_no_vector_certificate_256_payload/retired_proof.md`
— height bound `|Norm| <= N'^d = 2^448` at `N'=128`, `r_N = 1`,
`E S_p <= 2^-87.4`, `Pr[S_p>0] <= p^-0.350`; its script is OFF DISK
(catch #61, restore item open). The route is also named as ask (A)(i) in
`PRO_W3_e1_density.md:33-39`, and the open payload node is
`e1_open_cell_control_payload` (CONDITIONAL). I therefore claim NO
novelty for the union bound itself. My registered increments, each to be
checked: (i) LEM-1 replaces `2^448` by `2^255.5` (192 bits at N'=128;
`r_N` 4 -> 2 at N'=256); (ii) the orbit reduction (predicted 13 bits at
h=64); (iii) the `v_2`-graded form and `VSPARSE`; (iv) a restored,
runnable arithmetic script. PREDICTION: recomputing the retired numbers
reproduces `2^-87.4` and `p^-0.350` to within 1 bit.

### R2 — D1 falsifiers, with power controls (round-23 rule)

- **F1 (RUN THIS ROUND; exhaustive, full power).** h=8 exhaustive census.
  CONJ-B's proof machinery is falsified if (a) any odd box norm exceeds
  `29^4 = 707281`; or (b) any odd box norm has two prime factors
  `> 29^2 = 841` (counted with multiplicity); or (c) `BADCOUNT` in any
  dyadic window of `W_ADM(16) = (2^16, 707281]` exceeds
  `RPRIME * CLASSES(8)/|ORB(8)|`. Power: exhaustive over all `5^8`
  vectors, so a single violation is detected with certainty.
- **F2 (RUN THIS ROUND; the uniformity-in-`v_2` clause).** Cochran-
  Armitage trend test of `BADFRAC8(v)` against `v = 4..12`, stratified by
  dyadic window. FALSIFIED if `|Z| >= 1.96`. Power control: I will
  report, before interpreting, the per-step multiplicative trend the test
  detects at 80% power given the realised counts; round 25's stratified
  chi^2 gave `p = 0.07` (marginal), so this re-test is registered as a
  genuine second look, not a formality. A significant DECLINE supports a
  `v_2`-restriction (the withdrawn (c)); a significant RISE would be a
  new finding against the pose's uniformity clause.
- **F3 (RUN if budget allows; consistency).** At h=64, on `2^14` sampled
  odd box norms, check that after stripping the `2^17`-smooth part the
  remaining cofactor never exhibits two distinct prime factors `> 2^128`
  (checkable form: the cofactor is `> 2^256` never, and any cofactor with
  a proven-composite `> 2^256` part is a LEM-1 violation). Power:
  consistency only; it cannot detect a rare violation.
- **F4 (registered; NOT reachable this round).** A full-radius kernel
  enumeration at any of the four deployed Proth rows returning a
  collision. Under CONJ-B this has probability `<= 4 * 2^-29 ~ 2^-27`
  (heuristic rate) or `<= 4 * 2^-21` (my proved `v_2 >= 92` bound). It
  would not formally refute CONJ-B, but I register it now as the
  decisive practical falsifier so the pose cannot be retro-fitted.

### R3 — D2: LAW 2 for general `w`, candidates registered BEFORE testing

Reuse `large_v2_hunt/d3_thm.py` as the check harness (do not rewrite).
Registered chain:

- **P1 (homomorphism).** `s` is a group homomorphism from the odd-norm
  residues mod `4h` to `F_2`; equivalently `s(w1 w2) = s(w1) + s(w2)`,
  and `s(w)` depends only on `w mod 4h`. Confidence 95%.
- **P2 (the reduction).** Write `u = w mod 2` (a unit of
  `F_2[x]/(x^h+1)`, `sum u_i = 1`), `uhat` its 0/1 lift, and
  `z = ((w - uhat)/2) mod 2`. Then
  **`s(w) = sigma(u) + (u^{-1} z)_{h/2} mod 2`**,
  where `u^{-1}z` is computed in `F_2[x]/(x^h+1)` and `(.)_{h/2}` is the
  coefficient of `x^{h/2}`. Confidence 85%. This specialises to round-25
  LAW 2 at `u = 1` (`sigma(1) = 0`, `z = v mod 2`) and to its rotated
  corollary at `u = x^j`.
- **P3 (GUESS-G, the closed form for `sigma`).**
  `sigma(u) = #{(i,j) : i<j, u_i = u_j = 1, i+j = h/2 mod h} mod 2`.
  Confidence 45%. Derivation of record: squaring the 0/1 lift gives
  `lift(u)^2 = lift(u(x^2)) + 2c`, `c = sum_{i<j} u_iu_j x^{i+j}`
  (negacyclic), and `s(lift(u)^2) = 0`, which forces
  `sigma(u(x^2)) = ((u(x^2))^{-1} c)_{h/2}` — GUESS-G is the simplest
  form consistent with that constraint and with `sigma(x^j) = 0`.
- **Protocol.** Exhaustive determination of `sigma` on all odd-weight 0/1
  `u` at h=4 (8 vectors) and h=8 (128), and on `2^12` sampled `u` at
  h=16, 32, 64; then verify P2 by random `w` at h=4..64. FALSIFIER for
  each of P1/P2/P3: one counterexample. If P3 fails I fit `sigma` on
  h=4,8 and re-test the fit out-of-sample at h=16,32,64 — a fit that
  fails out-of-sample is reported as a MISS, not repaired again.
- Registered honest note: a counterexample to any of these is as bankable
  as a proof, and I will report it first.

### R4 — D3: box depth of 2-adic norm classes

Banked baseline: all `2^10 = 1024` classes realised mod `2^17`
(round 25). Registered targets:

- Sample `n = 2^20` distinct `w` uniform on `ODDBOX_64` (registered
  seeds `20260809, 26026, 1049, 2099`), compute `Norm(w) mod 2^48` by the
  tower recursion carried out modulo `2^48` (Kronecker-packed if the
  benchmark demands it). If the benchmark shows `n = 2^20` will not fit
  the 1G/5-min wall I drop to `n = 2^18` and document the benchmark;
  larger `n` only as a background job writing a results file.
- Depth ladder `D in {12,16,20,24,26,28,30,32,36,40,44,48}`. No `D = 7`
  cell (that is the trivial one-class baseline; CATCH-19B).
- **Prediction P-D3a:** `REAL(D) = AVAIL(D) = 2^{D-7}` EXACTLY for every
  `D <= 23` (at `n = 2^20`, expected uncovered `= M e^{-n/M} < 0.01` for
  `M <= 2^16`). This extends the banked realisation depth from `2^10`
  classes to `2^16` classes.
- **Prediction P-D3b:** for `D` in `24..28` the observed distinct count
  matches the uniform coupon-collector value `M(1 - e^{-n/M})` within
  `4 sigma`; for `D in {32,36,40}` the collision estimator
  `Mcol = n(n-1)/(2 * #collisions)` is consistent with `2^{D-7}` within a
  factor 2 wherever `#collisions >= 5`.
- **FALSIFIER (structure!):** `Mhat(D) <= AVAIL(D)/2` at `3 sigma` for any
  `D` in the ladder. That is exactly the "gap between realized and
  available classes" the brief calls STRUCTURE.
- **Stretch (registered, may not be reached):** a PROOF of full
  realisation from `Norm(1+2v) = sum_k 2^k c_k(v)` (`c_k` = char-poly
  coefficients of `v`), by exhibiting a triangular family in
  `v in {-1,0,1}^h`.

### R5 — process

Draft-only in `notes/pilots_20260809/b_sparsity_pose/`; every python3
through `tools/ramguard tiny|local -- python3` from the repo root
(including JSON peeks and file patching); any `RAMGUARD_TIMEOUT` use
documented in the report; checkpoints to `./state/`; stdlib only; no
git, no Modal, no edits to `dag.json`, `nodes/`, or `tools/`; no status
flips. Misses reported before hits; every measured functional named
above. QUARANTINE HELD: I do not read
`notes/pilots_20260802/CAMPAIGN_LEDGER.md` at or below line 3872, and I
do not open the other round-26 pilot dirs (`umin_spike_hunt`,
`freeze_tail_law`, `m7_falsifier_hunt`); this clause is passed verbatim
to any subagent (I plan to spawn none).
