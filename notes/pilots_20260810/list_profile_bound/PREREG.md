# PREREG — list_profile_bound (round 29)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

THE THEOREM TARGET under the new working hypothesis. Round 28's P0
correction established: RH-AC's open content is the FAR-CA crossing
on [k+2^34, 3n/4) — the Hankel layer applies only above 3n/4, and
the PROVED simple-pole floor puts B_ca^far(k+2^34-1) >= 2^216
against B* = 2^128 (88 bits unsafe at the bracket bottom). The
working hypothesis of record is a_RH = k + 2^34 + O(1). What is
MISSING is the safe half just above: an UPPER bound on the max list
profile (equivalently B_ca^far, equivalently F_LMAX at razor
parameters) at agreements sigma = 2^34 + c that crosses below
B* = 2^128 for explicit small c. The round-28 measured decay of the
exact max profile is 2.8074 bits per unit of a at the one exactly
computed scaled cell (0.6865 * log2 q) — at that rate the 88 unsafe
bits clear in ~32 units; the certified worst-case lower bound on the
decay ratio (0.1451) clears them in ~217 units. Either would pin
a_RH = k + 2^34 + O(100) — the question is what is PROVABLE. Read
first: notes/pilots_20260810/ssparse_endpoints/{REPORT.md,
FABLE_AUDIT.md} (the P0 chain, the decay ladder, the named
downward bias); the round-28 addenda on
critical/nodes/rate_half_band_crossing_location/statement.md; the
far-CA machinery above 3n/4 (rate_half_ca_hankel_fullrank_branch,
split_pencil_equivalence, far_ca_rider_reduction — their proofs
state their own domains); apolar_origin's mechanism C (min-weight
coset uniqueness, the type-1/type-2 dichotomy — proved legal on
both official profiles; a candidate instrument BELOW 3n/4).

## Deliverables

**D1 — THE POSE.** State the target theorem precisely: for
admissible razor rows, an explicit function UB(sigma) with
B_ca^far(k + sigma) <= UB(sigma) and UB(2^34 + c) < 2^128 for an
explicit c. Name what each candidate consumer needs (CATCH-24C):
adjacency_closing needs the pair (the PROVED floor at k+2^34-1
already supplies the unsafe half IF the crossing lands at k+2^34+c
with the safe half at that exact index). Register at least one
falsifier with power (what measured object would show NO such UB
exists at small c — i.e. the profile is FLAT above 2^34; note this
is exactly what (RH-AC-hi) would need, already facing the 2^40
flatness demand — quantify the link).

**D2 — THE INSTRUMENT SURVEY (own-repo first, CATCH-24A hard).**
What in-repo machinery gives max-list-profile UPPER bounds at
agreements just above k + 2^34? Candidates to check: (a) apolar's
mechanism C ported below 3n/4 (its legality margins were computed
at the official profiles — do they hold at sigma = 2^34?); (b) the
QMU/QMP minimal-support species; (c) Johnson-type bounds at these
radii (the banked Johnson machinery is elsewhere in the lane — its
domain?); (d) the far-CA rider reduction pushed below its stated
domain (it needs L_2(2tau) at 2tau = 2^35 << k — the round-28
report says hopeless; verify or refute that pricing); (e) anything
the greps surface. For each: domain, what it yields at
sigma = 2^34 + c, and the gap to 2^128.

**D3 — THE ATTACK.** Prove what is provable. If a full UB theorem
is out of reach, the bankable partials: (i) UB on a sub-stratum
(e.g. the tangent-free or pole-restricted part); (ii) a
conditional UB (on a named standard hypothesis); (iii) the exact
scaled-cell program — extend the round-28 measured-decay cell to a
LADDER (register the cells; the named downward bias must be
quantified per cell, not waved at) giving the decay law with error
bars, as the evidence base for the pose. The zero-power
declaration binds: no mean-model quantity enters any verdict.

**D4 — THE CONSTANT.** Under whatever lands, pin the working
hypothesis's O(1): the explicit c with a_RH <= k + 2^34 + c
(conditional or unconditional), and the margin ladder. If nothing
pins c, state the sharpest honest bracket and what closes it.

## Escape tests (before the main work)

- Replay ssparse's d4_margins.py (SCRATCH COPY; coordinator got
  the ladder reproduced) — your baseline numbers.
- Verify the P0 chain's two scope quotes yourself (the Hankel
  r < R/2 lines) — you build on them.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4474; do not read the other round-29 pilot dirs
  (collinearity_object, k_extremal, slack_recursion). Pass this
  clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT
  documented per use.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads; checkpoint long runs; background batches with
  results files for >10-min runs.
- DRAFT-ONLY: writes only in
  notes/pilots_20260810/list_profile_bound/; no dag/nodes/tools
  writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C). The F3
  zero-power declaration binds. Own-repo grep before claiming
  anything is missing (CATCH-24A — five firings and counting).
- Your final message IS the report. End with a compliance
  paragraph.

## Pilot registrations (appended by the pilot before any computation)

Pilot: Opus, codename `list_profile_bound`, round 29. Everything below was
written BEFORE any interpreter run, any grep, and any measurement. Sources
read first (primary text only, no computation): the brief above;
`ssparse_endpoints/{REPORT.md,FABLE_AUDIT.md}`;
`critical/nodes/rate_half_band_crossing_location/statement.md` (all four
round-28 addenda + the working-hypothesis block);
`background/nodes/rate_half_mca_sparse_layer_reduction/statement.md`;
`background/nodes/rate_half_far_ca_rider_reduction/statement.md`;
`background/nodes/rate_half_cyclic_simple_pole_mca_floor/{statement,proof}.md`;
`background/nodes/rate_half_ca_hankel_{split_pencil_equivalence,fullrank_branch,fixed_kernel_branch}/statement.md`.

### R0 — FUNCTIONALS NAMED (CATCH-19C)

Every number I report is one of these. `n = 2^41`, `k = 2^40`, `R = n-k = k`,
`a = k+sigma`, `r = n-a = k-sigma`, `B*(q) = floor(q/2^128)`.

- `B_CAFAR(a)` — max, over column-far received pairs, of the number of finite
  CA-bad slopes (the object of `(MS1)`). THE TARGET.
- `F_LMAX(n,k,a)` — max, over words, of the number of degree-`<k` codewords
  agreeing with the word on `>= a` coordinates (the max list profile).
- `M_LINE(e)` := `1 + r/(a-e)` — my claimed cap on the number of slopes
  sharing one code pair whose jointly-explained set has size `e`.
- `E_MIN` := `2a-n = 2*sigma` — forced minimum core size.
- `E_UNIQ` := `(a+k)/2 = k + sigma/2` — claimed core size above which the
  code pair is unique.
- `THETA_STAR(sigma)` := `a^2/n` — the Fisher/Johnson pairwise-overlap
  threshold (the "quasi-random overlap" value).
- `THETA_ALG` := `k-1` — the MDS pairwise cap on codeword agreement.
- `GAP_FISHER(sigma)` := `THETA_ALG - THETA_STAR(sigma)`.
- `F_JOHN(theta)` := `(a-theta)/(a^2/n - theta)` — the Fisher slope/codeword
  bound under pairwise-overlap cap `theta` (valid when `a^2/n > theta`).
- `SIGMA_JOHN` := least `sigma` with `a^2/n > k-1`, i.e. the classical
  Johnson-radius entry point at rate 1/2.
- `GAMMA_ONELINE` := least `a/n` with `3a-2n >= k` (my one-line threshold).
- `GAMMA_FISHLINE` := least `a/n` with `(2a-n)^2/a > k-1` (my line-count
  threshold).
- `UB_RIDER(sigma)` := `1 + (r+1)*L_2(2*sigma)` — the banked (RR2)/(RR4)
  rider bound; `L_2(e)` = max # code pairs jointly explaining on `>= e`.
- `DEFICIT(q)` := `log2( B_CAFAR_floor(k+2^34-1) / B*(q) )` — the unsafe
  margin at the bracket bottom, where `B_CAFAR_floor = L(q-n)/(q-n+kL)`.
- `F_DECAY(cell)` — measured bits of drop of the exact `F_LMAX` per unit of
  `a`, at a named scaled cell.
- `CAP_COMB(n_s,k_s,a)` — the q-independent combinatorial ceiling on
  `F_LMAX` at a scaled cell (the named downward bias's magnitude).
- `C_STAR` — the pinned constant in `a_RH = k + 2^34 + c`.

### R1 — D1 POSE SKELETON (registered form of the theorem target)

**(UB-far).** There is an explicit non-increasing `UB : Z -> Z` and an
explicit constant `c` such that for every admissible razor row
(`n=2^41`, `k=2^40`, `D` a multiplicative coset of order `n`, `q` prime,
`q = 1 mod n`, `2^255.9 < q < 2^256`) and every integer `sigma >= 2^34 + c`,

```text
B_CAFAR(k+sigma) <= UB(sigma) < 2^128 <= B*(q).
```

Consumer bars I will check (CATCH-24C, and the round-28 lesson: read the
consumers' consumers): `adjacency_closing` needs the PAIR
(unsafe at `a-1`, safe at `a`) — the PROVED simple-pole floor already
supplies the unsafe half at `k+2^34-1`, so `(UB-far)` at `c=0` would close
the pair exactly; `mca_safe` needs the safe half AT the located index (the
same moving bar); `(MS2)` says the safe half needs BOTH `B_CAFAR <= B*`
and `S_sparse <= B*`.

**Registered falsifier with power — (FLAT).** The measured object: the
exact max list profile `F_LMAX` (equivalently `B_CAFAR`) at consecutive
agreements above `k+2^34`. (FLAT) fires iff the profile's average decay
over the first `c+1` units is below `88/(c+1)` bits per unit for every `c`
in the small range, i.e. iff no `UB` with small `c` exists. Link to the
already-refuted-modulo-transport `(RH-AC-hi)` flatness demand, to be
quantified in PRED-13: `(RH-AC-hi)` needs average decay
`<= 2.1528e-10` bits/unit over `532,575,944,705` units; `(UB-far)` at `c`
needs `>= 88/(c+1)` bits/unit over `c+1` units. The two demands are
nested: (FLAT) at small `c` is a strictly WEAKER demand than `(RH-AC-hi)`,
so refuting `(RH-AC-hi)` does NOT refute (FLAT). That asymmetry is the
falsifier's power and I register it as the thing to quantify.

### R2 — D2 INSTRUMENT PRIORS (own-repo first; CATCH-24A assumed against me)

For each candidate I register the prior BEFORE grepping. I assume the
instrument EXISTS until a grep says otherwise.

- (a) apolar mechanism C ported below 3n/4 — prior: domain mismatch
  (it is stated at the A=1 / A=3 half-distance profiles and bounds
  supports/slopes there, not `B_CAFAR` at `a ~ n/2`); PRED-10.
- (b) QMU/QMP minimal-support species — prior: A=1 core-one face only,
  same domain problem.
- (c) Johnson-type bounds at these radii — prior: OUT OF DOMAIN by the
  classical rate-1/2 Johnson entry point; PRED-4.
- (d) far-CA rider reduction (RR4) pushed below its domain — prior:
  round-28's "hopeless" is CORRECT and I will quantify how hopeless;
  PRED-9.
- (e) the Hankel layer's own branches — prior: the full-rank branch
  (`<= r+1`) and the fixed-kernel branch (`<= rho`) both need `r < R/2`
  (`a > 3n/4`); a THIRD branch ("pencils whose generic kernel moves
  nontrivially with Z", named as remaining in
  `fixed_kernel_branch/statement.md:37`) is, I predict, still OPEN, so
  even the `a > 3n/4` discharge may be incomplete. PRED-8b: I predict I
  find either an open node or no node for the moving-kernel branch.
- (f) whatever else greps surface. PRED-8.

### R3 — D3 ATTACK PLAN (what I will try to prove, in order)

- **T1 (sunflower rigidity).** For a column-far pair at `a = k+sigma`,
  `sigma >= 1`, with a fixed choice of nearest codeword per bad slope: the
  bad slopes partition their pairs among code pairs ("lines"); for a line
  `P` with `>= 2` slopes, `E_P` (its jointly explained set) satisfies
  `E_P = A_lambda cap A_mu` for EVERY pair on `P` and `E_P subset A_lambda`
  for every slope on `P`; the petals `A_lambda \ E_P` are pairwise
  disjoint; hence `m_P <= M_LINE(e_P) = 1 + r/(a-e_P)` and
  `2*sigma <= e_P <= a-1`.
- **T2 (stratified rider).** `B_CAFAR(a) <= 1 + sum over lines through one
  fixed slope of r/(a-e_P)` — a per-code-pair weight `r/(a-e)` replacing
  (RR1)'s blanket factor `r+1`. At the minimum core size the weight is
  exactly 1, so T2 improves (RR1) by the factor `r+1 = 2^40` on that
  stratum.
- **T3 (Fisher sub-stratum, unconditional).** If all pairwise overlaps are
  `<= theta < a^2/n`, then `#slopes <= F_JOHN(theta)`. Numbers in PRED-5.
- **T4 (elementary unconditional far-CA threshold).** For
  `a >= (2n+k)/3 = 5n/6` all bad slopes lie on ONE line, hence
  `B_CAFAR(a) <= n-a+1`; and for `a/n > GAMMA_FISHLINE` the number of
  lines through a slope is Fisher-bounded, giving a finite `B_CAFAR`.
  PRED-6, PRED-7.
- **T5 (the exact obstruction).** State, with exact integers, the single
  inequality that separates the toolbox from the target:
  `THETA_ALG` (what the algebra forces) vs `THETA_STAR` (what Fisher
  needs). PRED: the gap is `GAP_FISHER(2^34)` and it is of the same order
  as the whole open bracket.
- **T6 (conditional UB).** State a UB conditional on a named bound for
  `L_2(e)` (or for the number of lines), via T2.
- **T7 (the ladder).** Exact `F_LMAX` at scaled cells, with `CAP_COMB`
  computed at every cell so the named downward bias is quantified PER
  CELL rather than waved at.

### R4 — CELL LADDER (registered before running)

Scaled cells `(n_s, k_s = n_s/2, q)` with `D` a multiplicative coset of
order `n_s` (so `n_s | q-1`), agreements `a_s = k_s + sigma_s`:

- C1 `(8, 4, 17)` — the round-28 anchor, `sigma_s in {1,2,3}` (replay).
- C2 `(8, 4, 41)`, C3 `(8, 4, 97)` — q-dependence at fixed `n_s`.
- C4 `(12, 6, 13)`, C5 `(12, 6, 37)` — `sigma_s in {1,2,3}`.
- C6 `(16, 8, 17)` — `sigma_s in {1,2,3,4}` if reachable; declared
  optional and I will report it as NOT MEASURED if it does not fit the
  compute law.

Registered in advance: the trivial two-codeword threshold is
`2*a_s - n_s > k_s - 1`, i.e. `sigma_s > (k_s-1)/2`, above which
`F_LMAX = 1` exactly; at the razor row the same threshold is `a >= 3n/4`,
which I register NOW as my explanation of where the PROVED bracket top
`3n/4` comes from (to be checked against the repo's own HD1 text).

### R5 — PREDICTIONS WITH NUMERIC WINDOWS

- **PRED-1 (escape).** Scratch replay of `ssparse_endpoints/d4_margins.py`
  reproduces: slack `114.6503`, floor `2^216.0000`, deficit `88.0000`
  bits, flatness factor `2^40.11`, span `532,575,944,705`. Window: all
  five exact to the printed digits.
- **PRED-2 (escape).** Both Hankel scope quotes present verbatim:
  `fullrank_branch/statement.md` line ~10 `r<R/2`, and
  `split_pencil_equivalence/statement.md` lines ~44-46
  `R=k=2^40 and r=B*(q)-1<=R/2`. Window: 2/2 CONFIRMED.
- **PRED-3.** `DEFICIT(q) = 88.0000 +- 0.01` bits INDEPENDENTLY of `q`,
  checked at both bracket endpoints `q ~ 2^167` and `q ~ 2^256`; reason
  registered in advance: the floor saturates at `(q-n)/k` and the budget
  is `q/2^128`, so the ratio is `2^128/k = 2^88` with `q` cancelling.
- **PRED-4.** `SIGMA_JOHN = sqrt(n(k-1)) - k`; window
  `SIGMA_JOHN / 2^34 in [30, 36]` (my point estimate `31.9`, i.e.
  `2^39.245`).
- **PRED-5.** `F_JOHN(n/4) <= 31` at `sigma = 2^34` (window `[28,34]`);
  `F_JOHN(ceil(a^2/n)-1)` at `sigma = 2^34` equals
  `549,621,596,161 = 2^39 - 2^27 + 1` (window: exact, +-1).
- **PRED-6.** `GAMMA_ONELINE = 5/6` exactly, and the resulting
  unconditional bound is `n/6 + 1 = 366,503,875,926` (window: exact).
- **PRED-7.** `GAMMA_FISHLINE = (9+sqrt(17))/16 = 0.8201941` (window
  `+-1e-6`).
- **PRED-8.** ZERO of the surveyed in-repo instruments delivers a finite
  `B_CAFAR` upper bound at any `a < 3n/4`. Window: 0 of `>= 6`.
  Falsified by a single grep hit with a domain reaching `sigma < 2^39`.
- **PRED-8b.** The Hankel moving-kernel branch is OPEN or absent (window:
  I find no PROVED node covering it).
- **PRED-9.** `log2 UB_RIDER(2^34) > 5e14` (point estimate
  `512*(2^40-2^35) = 5.629e14`); window `[5e14, 6e14]`.
- **PRED-10.** apolar mechanism C yields nothing at `sigma = 2^34`
  (window: 0 usable; either margin `<= 0` or an explicit domain
  mismatch).
- **PRED-11.** `c_meas = ceil(88/2.8074) = 32` (window `[31,33]`);
  `c_cert = ceil(88/0.4074) = 216` (window `[205,225]`);
  `c_family = ceil(88/126.5240) = 1` (window `[1,1]`).
- **PRED-12.** At session end the sharpest UNCONDITIONAL `c` is the
  bracket itself, `c_uncond = 2^39 - 2^34 = 532,575,944,704`; I register
  now, at >80% confidence, that I will NOT beat it. If I do beat it, that
  is the round's result and I will say so first.
- **PRED-13.** Falsifier power ratio at `c = 32`:
  `(88/33) / 2.1528e-10`; window `log2 in [33.3, 33.9]`.
- **PRED-14.** T1/T2 (sunflower rigidity + stratified rider) are NOT
  already in-repo. Window: 0 hits on a grep for the sunflower/common-core
  statement. If hit, I subtract and claim nothing.
- **PRED-15 (ladder).** `F_LMAX(8,4,5) = 7`, `F_LMAX(8,4,6) = 1`,
  `F_LMAX(8,4,7) = 1` at `q=17` (round-28 replay); `F_LMAX(8,4,5) = 7`
  also at `q = 41, 97` (window: exactly 7, i.e. q-independent);
  `F_LMAX(12,6,9) = 1` exactly (trivial threshold);
  `F_LMAX(12,6,7) in [8,40]`; `F_LMAX(12,6,8) in [2,12]`.
- **PRED-16 (the bias, quantified).** At cell C1 the measured decay
  `2.8074` bits equals `log2 CAP_COMB(8,4,5)` exactly, i.e. the cell is
  SATURATED at its q-independent combinatorial ceiling and therefore
  carries ZERO information about the `q`-scaling of the decay. Window:
  `|F_DECAY(C1) - log2 CAP_COMB(8,4,5)| < 1e-3`. If this holds it is a
  correction to round-28 item 5's ratio transport and I will report it as
  a MISS-class finding against the inherited number, first.

### R6 — COMPLIANCE PLAN

Compute law: every interpreter run as
`tools/ramguard tiny|local -- python3 ...` from the repo root with
`RAMGUARD_TIMEOUT` set and recorded per call. Banked scripts run from
SCRATCH COPIES ONLY. Writes confined to
`notes/pilots_20260810/list_profile_bound/`. Quarantine: I will not open
`notes/pilots_20260802/CAMPAIGN_LEDGER.md` at or below line 4474 and will
not read `collinearity_object`, `k_extremal`, `slack_recursion`. No
subagent. F3 zero-power binds: no mean-model quantity enters any verdict.

