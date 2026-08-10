# PREREG — nonpoly_flank_census (round 27)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

The witness-hunt recon (2026-07-12, recorded in
rate_half_band_closure's statement of record and its
notes/witness_hunt_20260712/ scripts) established the band's supply
anatomy INSIDE the fiber reduction: for POLYNOMIAL received words the
complete list bijects with a truncated-locator moment-map fiber, the
generic-core law holds exactly in vivo, THEOREM CAP pins the char-0
supply at the C(127,64) plateau, and seven candidate mechanisms died.
Its HONEST OPEN FLANK, verbatim: "non-polynomial received words
(planted-hybrid at giant slack) are outside the fiber reduction and
uncensused — the named residual hunt space. Sporadic escape hatch
priced at ~2^-5.2 per razor row." Your job: census the flank. Either
outcome is decisive-grade: a count anomaly on the flank FIRES the
node's pre-registered falsifier (structural surplus direction); a
clean census extends the window law to the last uncovered word class;
a REDUCTION THEOREM (non-poly words reduce to poly + bounded
correction) would close the flank by proof and is the best outcome.

## Deliverables

**D1 — THE FLANK, PARAMETERIZED.** From the fiber-reduction's exact
hypothesis (read the witness-hunt scripts + the statement record):
state precisely which received words escape it. Parameterize the
escape class (the planted-hybrid family at giant slack is the named
representative — is it the whole class?). Register the
parameterization and the census design BEFORE running: which scaled
rows (reuse the window-law campaign's 3-scale ladder shape: ~200
primes, q to 2^40 was the poly-side standard), which functionals
(exact band-analogue counts vs the first-moment model), what
deviation threshold (Poisson tolerance, pre-registered, two-sided —
the node's falsifier fires EITHER direction).

**D2 — THE CENSUS.** Run it. Exact counts, per-cell data, no merged
histograms without disaggregation. The poly-side counts at the same
cells are your matched control (the window law reproduced them —
your machinery must too, as its own calibration).

**D3 — THE REDUCTION ATTEMPT.** Try to prove the flank empty or
absorbed: a non-polynomial received word's band count decomposes as
(polynomial part, covered by the fiber reduction) + (correction,
bounded by X). Even a partial reduction (a sub-class absorbed)
shrinks the named hunt space. If the reduction fails structurally,
name the obstruction exactly.

**D4 — THE PRICE CHECK.** Verify the ~2^-5.2 sporadic-escape price
per razor row from its source (find it in the banked docs — where
does the number come from?), and re-derive it under your D1
parameterization. If the flank class is bigger than the price
assumed, the price changes — that is a finding.

## Escape tests (before the main work)

- Reproduce two poly-side window-law cells from the banked
  witness-hunt machinery (SCRATCH COPY) — exact match required.
- Verify the generic-core law fiber = C(N-r, h) + Poisson at one
  banked in-vivo cell.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4062; do not read the other round-27 pilot dirs
  (pincer_formalization, staircase_extension, cancellation_recon).
  Pass this clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT
  documented per use.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY (the round-26 lesson).
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads; checkpoint long runs; background batches with results
  files for >10-min runs.
- DRAFT-ONLY: writes only in
  notes/pilots_20260809/nonpoly_flank_census/; no dag/nodes/tools
  writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C). 2-power
  config grids where the grid is yours. Own-repo grep before
  claiming anything is missing (CATCH-24A).
- Your final message IS the report. End with a compliance paragraph.

## Pilot registrations (appended by the pilot before any computation)

Pilot: nonpoly_flank_census (Opus, round 27). Everything below was written
after reading only: the four banked witness-hunt scripts, the node
statement/QUALITY/node.json, and `rate_half_arbitrary_line_syndrome_router`.
No computation of any kind has been run at the time of writing.

### R0 — Reading of record (sources, verbatim anchors)

- Fiber reduction, exact hypothesis (rh_c3_fiber_mtm_v2.py:6-9): "for
  received word Y = X^k * L_T0 (deg k+t), list members at agreement >= k+t
  on mu_n biject with size-(k+t) subsets S whose locator matches Y's top
  t+1 coefficients."
- Full-fiber instrument (rh_band_witness_census_modal.py:31-35): the table
  over all c in F_q^t is "the EXACT full list count of the received word
  X^k * L_{T0(c)} for polynomial words".
- Price source located BEFORE computing (rh_c1_c2_zerosum_n64.py:194):
  "at q ~ 2^40 sporadic = 0 -> at razor q ~ 2^256 expected ~
  C(255,128)/q ~ 2^-5.3." QUALITY.md:31-32 quotes it as "~2^-5.2/row".
  D4 is therefore a *verification + slice-grading* task, and I register in
  advance the hypothesis (H-D4) that 2^-5.2 and 2^-5.3 are the same
  quantity at the two ends of the razor slice (lg q = 255.900 vs 256.000).
- Distinct, NOT-in-scope flank: `rate_half_arbitrary_line_syndrome_router`
  (PROVED) owns the *received-LINE / MCA-pair* flank (syndrome pairs mod
  C^2, toy (7,6,3,4) seven-slope witness). That is a different object from
  the LIST-side word flank this pilot censuses. I will not conflate them
  and I claim nothing about it.

### R1 — D1: the escape class, parameterized (registered before computing)

Domain D = mu_n (order-n multiplicative coset), C = RS_k, rate 1/2,
agreement level a = k + t. Every received word is the evaluation of a
unique Y with deg Y <= n-1, so "non-polynomial" cannot mean "not a
polynomial". I register the following exact reading of the flank:

- **(E0) deg Y < k**: Y is a codeword; list count 1. Trivially covered.
- **(E1) k <= deg Y < a**: list count 0 (an agreement set of size a would
  force deg(Y-f) >= a). Trivially covered.
- **(E2) deg Y = a (SLACK ZERO)**: this is *exactly* the fiber
  reduction's hypothesis. Modulo adding codewords and scaling, such a word
  is determined by its top coefficients (y_a=1, y_{a-1},...,y_k), i.e. by
  a point c in F_q^t — which is precisely the banked instrument-2 domain.
  So the poly side is censused COMPLETELY, not just for the shape
  X^k L_T0.
- **(E3) deg Y = a + delta, delta >= 1 (POSITIVE SLACK)**: THE ESCAPE
  CLASS. Registered parameterization: `delta in [1, n-1-a]` (the slack),
  and within each stratum the word class is
  `W in F_q^{t+delta}` (top coefficients y_{a+delta}=1, y_{a+delta-1},
  ..., y_k modulo C and scaling; exactly q^{t+delta} classes).
  "Giant slack" = delta large. The *planted-hybrid* family is the
  sub-class {W : list count >= 1} (equivalently W = top part of some
  V_A u with |A| >= a); it is **NOT the whole class** — it is the support
  of the count functional. My census is over the whole stratum, so the
  planted-hybrid family is covered as a subset and reported separately.

Registered structure statement (to be tested, not assumed). Write
`L_A(z) = prod_{x in A}(1 - x z)` and `W(z) = z^d Y(1/z) mod z^{t+delta+1}`.
Then f is a codeword at agreement >= a for Y iff Y - f = V_A u with
|A| >= a, u monic of degree d - |A|, iff

```text
L_A(z) * uhat(z) = W(z)   mod z^{t+delta+1},
uhat a polynomial of degree <= delta with uhat(0) = 1.       (FL1)
```

so the escape class is "the same moment-map fiber, quotiented by a
degree-<=delta unit factor". Counting *subsets* A of size exactly a gives
Phi_a; counting *codewords* gives L; they differ for delta >= 1 (a
codeword whose agreement set has size j contributes C(j,a) subsets). The
list count is the prize-relevant one and is what I measure.

### R2 — Named functionals (CATCH-19C)

Per cell `(n, k=n/2, q, t, delta)`, a = k+t, d = a+delta, K = q^{t+delta}
word classes:

- `F_LIST(W)` := #{codewords f : |{x in D : Y_W(x) = f(x)}| >= a} — the
  exact list count of word class W. THE decisive functional.
- `F_MEAN` := (1/K) * sum_W F_LIST(W).
- `F_MAX`  := max_W F_LIST(W).
- `F_HIST(l)` := #{W : F_LIST(W) = l} (full per-cell disaggregation; no
  merged histograms).
- `F_TAIL(l)` := #{W : F_LIST(W) >= l}.
- `F_SUBSET(W)` := Phi_a(W) = #{A subset D, |A| = a, (FL1) holds} — the
  subset (fiber-analogue) count, reported alongside F_LIST so the
  dedup gap is visible.
- `F_PLANTED` := #{W : F_LIST(W) >= 1} / K (the planted-hybrid density).
- `F_SUM(N,h,q,v)` := #{S subset mu_N, |S| = h, sum(S) = v mod q} — the
  quotient-level prescribed-sum multiplicity (the C1-mechanism flank).
- `F_SPOR(N,h,q)` := F_SUM(...,0) - C(N/2, h/2) — the q-sporadic excess
  (the D4 price's object), and its prescribed-sum generalization
  `F_SPORV := max_v F_SUM(v) - C(N/2, h/2)`.

### R3 — Model of record (first moment), registered as exact formulas

- **M1 (mean law, delta-independence).** I predict, and will test as an
  identity, that for every delta >= 0

```text
F_MEAN(n,k,q,t,delta) = mu(n,k,q,t,d)
   := sum_{i=a}^{min(n,d)} (-1)^{i-a} C(i-1,a-1) C(n,i) q^{k-i}.
```

  (Derivation registered: #{P monic of degree d with a prescribed i-subset
  of D among its roots} = q^{d-i}; inclusion-exclusion; every term carries
  q^{d-i}/q^{t+delta} = q^{k-i}, which is delta-free. The ONLY
  delta-dependence is the truncation `min(n,d)`.) Window: EXACT equality
  in integer arithmetic (tolerance 0). A miss is either a machinery bug or
  a false theorem, and I will say which.
- **M2 (Poisson background).** Off the structured cells, F_LIST is modelled
  Poisson(mu) with mu = F_MEAN; model tail `M_TAIL(l) = K * P(Pois(mu) >= l)`.
- **M3 (structured plateau, the poly-side law extended).** Define
  `plateau(s) := C(n/M - 1, k/M)` at the finest dyadic `M | k` with
  `M > s` (0 if no such M exists). Banked poly-side checks: cell A
  (n=32,t=5) -> M=8 -> C(3,2)=3; cell B (n=32,t=3) -> M=4 -> C(7,4)=35;
  razor row -> M=2^34 -> C(127,64). I predict the FLANK law
  `plateau_flank(t,delta) = plateau(t+delta)`.

### R4 — Predictions with numeric windows (registered before computing)

- **P1 (mean law).** F_MEAN = mu exactly in every cell, every delta.
  Window: 0. Two-sided by construction.
- **P2 (flank max = poly max at shifted slack).** For every cell,
  `F_MAX = max(plateau(t+delta), B_pois)` where `B_pois` = least l with
  `K*P(Pois(mu) >= l) <= 0.05`. Registered numeric predictions of
  plateau(t+delta) (computed by hand now, before any run):
  - n=8,k=4,t=1: delta=0 -> 3 (M=2); delta=1,2 -> 1 (M=4); delta>=4 -> 0.
  - n=16,k=8,t=1: delta=0 -> 35 (M=2); delta=1,2 -> 3 (M=4); delta=4 -> 1.
  - n=16,k=8,t=2: delta=0,1 -> 3 (M=4); delta=2 -> 1 (M=8).
  - n=32,k=16,t=3 (cell B): delta=0 -> 35; delta=1,2,4 -> 3; delta=8 -> 1.
  - n=32,k=16,t=5 (cell A): delta=0,1,2 -> 3; delta=4 -> 1.
  ANOMALY (surplus, FIRES the node falsifier) if F_MAX exceeds that value
  by more than B_pois in any cell; ANOMALY (deficit) if
  F_MAX < plateau(t+delta) in a starved cell (q^t > C(n,a)).
- **P3 (dedup gap).** `F_SUBSET >= F_LIST` always, with equality iff every
  list member has agreement exactly a. I predict the structured argmax
  words have `F_SUBSET = C(r,t)*F_LIST + background` for an integer r >= t
  (r = #D-roots of the truncated word). Window: the identity
  `F_SUBSET = sum_j (#members with agreement j) * C(j,a)` must hold
  EXACTLY (tolerance 0) wherever both are measured.
- **P4 (prescribed-sum law, the C1-flank).** For N a 2-power, h = N/2,
  in char 0: writing v in Z[zeta_N] in the power basis
  `{zeta^0,...,zeta^{N/2-1}}` with coordinate vector c,
  `F_SUM(v) = C(N/2 - |J|, (h - |J|)/2)` if all c_j in {0,+-1} and
  |J| := #{j : c_j != 0} has the same parity as h, else 0. Hence
  `max_v F_SUM(v) = C(N/2, h/2)` attained ONLY at v = 0. Windows: exact
  equality at every v, at N = 8 and 16 exhaustively, over a large-q ladder
  where the char-0 regime holds. ANOMALY (surplus) if any v != 0 attains
  or exceeds C(N/2,h/2) in char 0 — that would be a NEW priced family and
  fires the falsifier.
- **P5 (sporadic price).** Over a ladder of ~200 primes q = 1 mod N,
  total `F_SPOR` (and `F_SPORV`) matches the first-moment sum
  `sum_q (C(N,h) - char0)/q` within a factor 4 either way; and
  `F_SPOR = 0` at every q > C(N,h) (starved). Two-sided: a sustained
  (>= 3 consecutive q, or >= 3 scales) excess or deficit beyond that
  window fires the falsifier.
- **P6 (price re-derivation).** I predict D4 resolves as: the banked
  number is `C(255,128)/q` with `lg C(255,128) = 250.675...`, giving
  `2^-5.225` at lg q = 255.900 and `2^-5.325` at lg q = 256.000, i.e.
  QUALITY.md's 2^-5.2 = bottom of slice, the script's 2^-5.3 = top.
  Window: +-0.02 bits on each end. And I predict the D1 re-derivation
  does NOT multiply the trial count (the sporadic event is a property of
  (q, N, h) alone, independent of the received word and of delta), so the
  price is unchanged by the flank; the only correction is P4's
  prescribed-sum generalization, which I predict changes nothing because
  v = 0 is optimal.

### R5 — Census design (what will actually run)

Escape tests first: (i) SCRATCH COPY of `rh_c3_fiber_mtm_v2.py`, run
unmodified, cells A and B — exact match to the banked deduped qcore 3 and
35 required; (ii) generic-core law `fiber = C(N-r,h) + Poisson` at one
in-vivo cell (T0 spread over r cosets).

Then, three-scale ladder (2-power grid, mine):

- **S1 (exhaustive stratum census)**: n = 8 and 16, k = n/2,
  q = 1 mod n primes, t in {1,2}, delta in {0,1,2,4} (2-power grid; delta
  truncated per cell by cost). EVERY word class W enumerated; exact
  F_LIST, F_HIST, F_MAX, F_MEAN, F_SUBSET, F_PLANTED. delta = 0 is the
  matched poly-side control at the identical cells.
- **S2 (targeted structured/flank probes)**: n = 32, cells A and B,
  delta in {0,1,2}, exact F_LIST by half-DP + uhat-sum + inclusion-
  exclusion dedup; plus random-W background samples for calibration.
- **S3 (quotient-level prescribed-sum census)**: N in {8,16,32}, h = N/2,
  ladder of ~200 primes q = 1 mod N up to 2^40 (matching the poly-side
  standard), exhaustive at N = 8,16 and probe-based at N = 32. Measures
  F_SUM, F_SPOR, F_SPORV.

### R6 — D3 (reduction) claims to be attempted, stated in advance

- **(RED-1)** `L = sum_{i>=a} (-1)^{i-a} C(i-1,a-1) Phi_i` with
  `Phi_i = sum_{uhat, deg <= d-i} F^{(t+delta)}_i(W * uhat^{-1})`, i.e.
  the flank count is a signed q^delta-fold sum of *polynomial-side* fibers
  at deeper truncation t+delta. ("non-poly = sum of poly + dedup".)
- **(RED-2)** In the coset universe, the flank's structured supply at
  slack delta equals the poly-side supply at effective slack t+delta
  (M > t+delta), hence is non-increasing in delta and capped by the poly
  side — THEOREM CAP extends to the whole flank.
- **(RED-3)** The dedup correction is exactly the factor C(r,t) of P3 and
  is a subset-count artifact carrying NO extra codewords.
If any of these fails I will name the obstruction exactly rather than
weaken the claim.

### R7 — Compliance

Quarantine acknowledged (CAMPAIGN_LEDGER.md line >= 4062 not read — I
located a `planted-hybrid` hit at line 4068 by grep line numbers only and
did not open it; the other three round-27 pilot dirs not read, not
listed). All interpreter runs via `tools/ramguard tiny|local -- python3`
from the repo root, with every RAMGUARD_TIMEOUT use documented in the
report. Writes confined to
`notes/pilots_20260809/nonpoly_flank_census/`. Banked scripts run only
from scratch copies under `scratch/`. Stdlib only, no Modal, no git.

