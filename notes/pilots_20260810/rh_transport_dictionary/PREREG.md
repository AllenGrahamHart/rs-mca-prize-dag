# PREREG — rh_transport_dictionary (round 31)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/slack_recursion/REPORT.md` (round 29)
2. `notes/pilots_20260810/slack_recursion/MINT_PACKAGE.md`

## Mandate

Round 29 resolved the supply side of RH-AC into a MODEL CRITIQUE
gated on one named object: THE (t,M) TRANSPORT DICTIONARY. The t=1
toy model is provably unfaithful (the razor lives at coset scale
t = 2^34; naive transport over-satisfies by ~115 bits; C(127,64)
matches NEITHER coset formula). Theorems A/B (the product-word
realization of Graham-Sloane and the matching upper bound) are exact
at t=1; NOTHING is known at t > 1. Every supply-side razor claim in
the lane is gated on this dictionary. YOUR JOB: build its first
entries.

## Deliverables

**D1 — THE FAITHFUL MODEL, POSED.** Define exactly what a
(t,M)-faithful supply model must preserve to license transport to
the razor's t = 2^34 coset scale (which quantifiers, which counting
unit, which normalization). Pre-register the definition BEFORE
measuring; state the C(127,64) puzzle as its first test case.

**D2 — SMALL-t EXACT MEASUREMENTS.** At t = 2, 3, 4 (and higher if
cheap) on small admissible scale ladders: measure the exact
arbitrary-word supply maximum in the coset-faithful setting.
Checkpointed batches; exact integers; results files.

**D3 — THE TRANSPORT LAW.** From D2: does the t=1 Theorem A/B pair
generalize (a product-word family per coset, a matching upper
bound)? Derive the candidate (t,M) law, test it against every
measured point, and against C(127,64) — if the puzzle resolves
(the value matches the law under the right reading), say which
reading; if not, the law is wrong and say so.

**D4 — THE RAZOR VERDICT, HONESTLY SCOPED.** What do D1-D3 license
about t = 2^34? State the extrapolation gap exactly; pre-registered
falsifier for the law; zero-power declaration on anything the
small-t window cannot see. Misses first. DO-NOT-INHERIT WARNING:
the round-27/28 banked supply lines contain two corrected errors
(the "same fate likely" line; the ratio transport) — read the
corrections in the crossing_location addenda before quoting
anything.

## Constraints (binding)

- COMPUTE LAW: never bare python3. `tools/ramguard tiny -- python3 ...`
  (256M/60s) for peeks, `tools/ramguard local -- python3 ...` (1G/5min)
  for real runs, from the repo root, literal `--`. RAMGUARD_TIMEOUT
  may extend walls; document each use. Stdlib only. No Modal, no
  network, no git.
- RAM DISCIPLINE: file-at-a-time reads; NEVER open dag.json;
  checkpointed background batches with results files for >10-min
  runs.
- WRITE SCOPE: ONLY inside
  notes/pilots_20260810/rh_transport_dictionary/. No dag/, nodes/,
  tools/ edits. No git. Never touch any path containing
  prize-codex-.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  Never read the sibling round-31 dirs (rh_overlap_cap,
  rh_type2_stratum, rh_e_axis_audit). Round-30 and earlier pilot
  dirs are readable (slack_recursion's scratch/ scripts especially —
  copy before running).
- BLIND PRIORS: after reading ONLY the two anchors, append "## Pilot
  registrations" (expected (t,M) law shape, P(C(127,64) resolves
  under the law), expected surplus trend in t) BEFORE any further
  read.
- REPORT: REPORT.md in your dir; MISSES-FIRST; every quantifier
  claim quoted file:line (CATCH-24C); own-repo greps before novelty
  claims (CATCH-24A); zero-power declarations on max-quantified
  claims.

## Pilot registrations

Written after reading ONLY the two named anchors
(`slack_recursion/REPORT.md`, `slack_recursion/MINT_PACKAGE.md`) and
BEFORE any further read, grep, or computation. Everything below is
derived from those two files plus my own algebra; no banked razor
derivation has been consulted yet.

### R0 — frame and notation (fixed here, used unchanged in the REPORT)

`n` with `4 | n`, `q` prime with `q = 1 mod n`, `D = mu_n subset F_q`,
`k = n/2`, `C = RS[n,k]` (evaluations of `deg < k`), excess `t >= 1`,
agreement threshold `a = k + t`, slack budget `m = n - a`.
`H = mu_M subset mu_n` for `M | n` is the coset subgroup; `n' = n/M`,
`k' = k/M`, `a' = a/M`, `D' = mu_{n'}`. Round 29's dictionary
identification, which I adopt as the working hypothesis to be tested
rather than assumed, is `t = M` (the excess equals the coset scale).

Functionals (all counting units named explicitly, per D1):

```text
F_LIST(y)    = #{ f in C : agree(y,f) >= a }                (codeword unit)
F_SUBSET(y)  = #{ A subset D : |A| = a, y|_A in C|_A }      (subset unit)
F_ORB(y)     = # H-orbits of listed codewords                (orbit unit)
PLATEAU(n)   = C(n/2-1, n/4)                                 (slack-0 cap)
MAXWORD_LIST(n,t)      = max over ALL y in F_q^n of F_LIST(y)
MAXWORD_LIST_H(n,t,M)  = max over H-INVARIANT y of F_LIST(y)   (level-n count)
MAXWORD_LIST_Q(n,t,M)  = max over y' in F_q^{n'} of F_LIST_{n'}(y')  (quotient count)
GAIN(y,M)    = F_LIST_n(lift of y') - F_LIST_{n'}(y')        (lift-gain)
PSUM(n',a')  = max_s #{ A' subset D' : |A'| = a', prod A' = s }
SURPLUS(n,t,M) = log2( supply / plateau ) in the SAME unit and SAME level
```

### R1 — D1 registered BEFORE measuring: what "(t,M)-faithful" must mean

A supply model is **(t,M)-FAITHFUL** iff it fixes, and preserves under
transport, all five of:

1. **Word quantifier (Q1).** Which `y` the max ranges over: (a) all of
   `F_q^n`; (b) `H`-invariant ("coset/dressed") `y` only; (c) a named
   sub-family. (a) and (b) are different objects and (b) <= (a).
2. **Counting unit (Q2).** `F_LIST` (codewords) vs `F_SUBSET` (subsets)
   vs `F_ORB` (H-orbits). Theorem C already shows `F_SUBSET` is not
   comparable across slack strata; I add that `F_LIST` and `F_ORB`
   differ by a factor up to `M` under transport, which at `M = 2^34` is
   34 bits — larger than the whole razor need.
3. **Level of the comparison (Q3).** Supply and plateau must be counted
   at the SAME level (both at `n`, or both at `n' = n/M`). A supply
   counted at level `n` against a plateau counted at level `n'` is
   the transport error I most expect to find.
4. **Normalization (Q4).** `SURPLUS` in bits is `log2(supply/plateau)`
   with both terms in the same unit and level; any per-coset or
   per-point normalization must be declared.
5. **Excess law (Q5).** Whether the razor's excess is literally `t = M`,
   and whether `a = k + t` with `M | a` (which requires `M | k`).

**First test case (registered now).** The banked razor plateau
`C(127,64)` must be reproduced by the model's own plateau formula under
a stated reading. Candidate readings, registered before looking:

* **R-A**: `C(127,64) = PLATEAU(n') = C(n'/2-1, n'/4)` with `n' = n/M = 256`;
  then the razor's `N = 128` is `k/M = n/(2M)` (the QUOTIENT DIMENSION),
  `h = 64 = N/2 = n/(4M)`, and with `M = 2^34` the model scale is
  `n = 2^42`, `k = 2^41`, `a = 2^41 + 2^34`.
* **R-B**: `C(127,64) = C(128,64)/2`, a half-of-central-binomial count.
* **R-C**: `C(127,64) = C(n'-1, n'/2)` with `n' = 128` — the Theorem-C
  degenerate (distance-1) `F_SUBSET` shape, i.e. the razor plateau is a
  SUBSET count, not a LIST count.
* **R-D**: none of the above; the razor plateau is not a model plateau.

### R2 — registered candidate transport law (the (t,M) law shape)

**LAW-QUOT (my primary).** For `M | n`, `M | k`, `t = M`, and
`H`-invariant `y`: the level-`n` problem restricted to `H`-invariant
data is EXACTLY the level-`n'` problem with excess `t' = 1`.
Reason registered in advance: an `H`-invariant `f` of degree `< k` is
`g(X^M)` with `deg g < k/M = k' = n'/2`; an `H`-invariant agreement set
is a union of `M`-cosets, so `agree = M * agree'`, and
`M*a' >= k + M` iff `a' >= k' + 1`, i.e. `t' = 1`.
Consequences registered:

```text
MAXWORD_LIST_H(n, M, M)  = PSUM(n', a')            (lower, Theorem A lifted)
                        <= 2 C(n', a')/n'           (upper, Theorem B lifted)
PLATEAU_coset(n,M)       = PLATEAU(n') = C(n'/2-1, n'/4)
SURPLUS(n, t=M)          = SURPLUS(n/M, t=1)        (QUOTIENT-INVARIANCE)
```

with `PSUM(n',a') = C(n',a')/n'` exactly when `gcd(a',n') = 1`, and
strictly larger otherwise (registered refinement: the rotation argument
of Theorem A only equidistributes when `gcd(a',n')=1`).

**LAW-SYM (my secondary, for `t` NOT a coset scale).** For maximal-slack
words the agreement condition is `t` vanishing conditions
`W_s(y,A) = 0`, `s = 0..t-1`, on the top `t` interpolant coefficients.
At `t = 1` the single condition is the CYCLIC one (`prod A` prescribed,
`n` classes, `q`-independent). At `t >= 2` I predict the extra `t-1`
conditions are `F_q`-valued, not cyclic, so the arbitrary-word supply at
`t >= 2` is `q`-DEPENDENT and of order `C(n,a)/(n q^{t-1})` for the
natural generalisation `y = x^{-t} + c x^{k}` — a collapse, not a
plateau. Explicit registered instance for `M = 2`: the lift of the
quotient product word is `Y = X^{n-M} + c X^{n/2}`, whose level-`n`
agreement sets are `{A : sum_{x in A} 1/x = 0}` intersected with one
product-type condition; every `H`-invariant `A` satisfies the first
condition automatically (the `x, -x` pairs cancel), so
`GAIN >= 0` with the excess `q`-dependent and `-> 0` as `q` grows.

**Upper-bound law (registered).** Distinct codewords agree in
`<= k-1 = a-t-1` points, so the full agreement sets form a
constant-weight-`a` binary code of minimum distance `2(t+1)`, hence
`MAXWORD_LIST(n,t) <= C(n, a-t)/C(a, t)` (this is Theorem B at `t=1`).
Registered corollary: at `n = 8`, `t >= 2`, `2a - n = 2t > k-1 = 3`,
so `MAXWORD_LIST(8,t) = 1` for every `t >= 2` — `n = 8` has ZERO POWER
for any `t`-trend.

### R3 — predictions with windows (misses to be reported first)

* **P1** (replication, tol 0). Exhaustive over all `y mod C` at
  `n=8, t=1`, at `q = 17` and `q = 41`: `MAXWORD_LIST = 7`. conf 0.85.
* **P2** (structure). Same census: the maximisers are exactly the
  product-word class `x^{-1} + c x^{4}` up to the code and scaling, with
  flat profile `{5:7}`. conf 0.7.
* **P3** (reduction). LAW-QUOT's invariant reduction verified exactly at
  `(n,M) = (16,2)`: invariant listed codewords at level 16 are in
  bijection with the level-8 list, for every tested `y'`. conf 0.90.
* **P4** (lift-gain). For the lifted product word at `(16,2)`:
  `F_LIST_16 = 7 + G(q)` with `G(17) >= 1` (window `[1,120]`) and
  `G(97) = G(113) = 0`. `P(G(97) = 0) = 0.60`.
* **P5** (the law holds). Every measured coset-faithful point equals
  `PSUM(n',a')` exactly (not merely within the factor 2 band). conf 0.75.
* **P6** (gcd refinement). At `(n,M) = (24,4)`: `n'=6, a'=4`,
  `gcd(a',n')=2`, `C(6,4)/6 = 2.5` is not an integer; predict
  `PSUM = 3` and the measured coset-faithful max `= 3`. conf 0.60.
* **P7** (surplus trend in `t`). `SURPLUS(n,t=M) = SURPLUS(n/M,1)`, hence
  STRICTLY DECREASING in `M` at fixed `n`. Registered values (bits):
  `(32,2) = 4.352`, `(32,4) = 1.222`, `(24,2) = log2(66/10) = 2.722`,
  `(24,3) = 1.222`, `(16,2) = 1.222`, `(16,4) = 0`. conf 0.70.
* **P8** (the `C(127,64)` puzzle). `P(resolves under a clean reading of
  the law) = 0.45`, split R-A 0.25, R-C 0.10, R-B 0.02, other 0.08.
* **P9** (razor verdict). Under LAW-QUOT the razor-scale surplus is the
  `n' = 256` surplus, i.e. `+120.49` bits — transport in `t` does NOT
  remove the over-satisfaction; the unfaithfulness must then live in the
  WORD QUANTIFIER (Q1) or the COUNTING UNIT (Q2), not in `t`. conf 0.60.
* **P10** (`q`-dependence). The arbitrary-word (non-coset) supply max at
  `t >= 2` is `q`-dependent; at `t = 1` it is `q`-independent. conf 0.70.
  Test: sampled maxima at `(16,2)` for `q = 17` vs `q = 97`.

### R4 — pre-registered falsifiers

* **F-LAW.** LAW-QUOT is REFUTED if any measured `H`-invariant word at a
  tested `(n,M)` has level-`n` invariant list size different from its
  quotient list size, or if the coset-faithful max exceeds
  `2 C(n',a')/n'`, or falls below `PSUM(n',a')`.
* **F-GAIN.** "Coset-faithful = quotient" as a SUPPLY statement is
  refuted if `GAIN > 0` persists at the two largest tested `q` at a fixed
  `(n,M)` (i.e. is structural, not field noise).
* **F-RAZOR.** The R-A reading is refuted if the banked razor derivation
  fixes `N = 128` as the block length (not the quotient dimension), or
  fixes `h` other than `N/2`.
* **F-SURPLUS.** Quotient-invariance is refuted if any measured
  `SURPLUS(n,M)` differs from `SURPLUS(n/M,1)` by more than 0 bits.

### R5 — fallback rules (registered so I cannot slide)

1. If the measurements refute LAW-QUOT, I report the refutation as the
   headline and do NOT rescue the law by re-reading the quantifier.
2. If `C(127,64)` fails every reading, I say the dictionary has NO first
   entry on the plateau axis and scope D4 accordingly.
3. Any claim I cannot measure at `n <= 24` gets an explicit ZERO-POWER
   declaration naming the price of the missing measurement.
4. I do not claim F2 fires or fails; the deliverable is a dictionary.

### R6 — route prices (registered before spending)

* `n=8` exhaustive census over `y mod C`: `q^4` classes (`q=17`: 83.5k,
  `q=41`: 2.83M) x 56 subsets — `tiny`/`local`, minutes.
* `n=16` per-word exact `F_LIST`: 8008 `a`-subsets x O(a t) — ~0.2 Mops
  per word; sampling budget <= 2000 words per field.
* `n=24, t=1`: `C(24,13) = 2.50M` subsets per word — `local`, one word
  at a time, checkpointed.
* `n=24, t=3`: `C(24,15) = 1.31M` subsets per word — same.
* `n=32` per-word exact: `C(32,18) = 471M` — DEAD in Python; registered
  now as a zero-power zone, to be covered by the reduction theorem plus
  quotient measurement only.
