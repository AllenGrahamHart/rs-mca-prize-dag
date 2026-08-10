# PREREG — slack_recursion (round 29)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

THE SUPPLY SIDE'S LAST NUMBER. Round 28's maxscan_algorithm decided
the delta=1 flank branch (COLLAPSE at four scales) and named the
route to the remaining one: the MAXIMAL-SLACK curve (arbitrary
received words — the round-27 sampled values 67 > 46 at n=16,
GROWING over two scales while delta=1 died) is undecided, and "the
parity theorem may apply recursively (E on one parity class is
itself an e2 one level down), which is the only visible route to
n=128" — and to the maximal-slack object. YOUR JOB: close the
supply side entirely. Read first:
notes/pilots_20260810/maxscan_algorithm/{REPORT.md, FABLE_AUDIT.md,
scratch/ms_exact.py, scratch/ms_strat.py, MODAL_REQUEST.md};
notes/pilots_20260809/nonpoly_flank_census/{REPORT.md} (the
maximal-slack sampled measurements and their word classes); the
round-28 addenda on
critical/nodes/rate_half_band_crossing_location/statement.md.

## Deliverables

**D1 — THE RECURSION, FORMALIZED.** The round-28 note is one line;
make it a theorem or kill it: does the parity factorization apply
to E restricted to one parity class (i.e., is the restricted E an
e2-type functional one level down, enabling the s <= n/4 stratum
ceiling to iterate)? Register the exact statement and the expected
reduction factor BEFORE proving. If it lands: the n=128 antipodal
scan prices at what? (Register the price.)

**D2 — MAXIMAL SLACK, EXACT AT n=32.** The round-27 measurement
was 120 sampled locator words at n=16 (67 two-field). Design the
exact computation of the ARBITRARY-WORD maximum at n=32 — the
object is max over ALL received-word classes (every delta stratum,
not just delta=1) of the agreement->=a count. Routes: (a) the
delta-stratified union (the window-shift reduction makes each
delta stratum a shifted-window problem — the round-27 proved
reduction; sum/max over delta with the round-28 machinery per
stratum); (b) direct subspace-closure (ssparse-style F_LMAX
generalization — check its cost at n=32); (c) the recursion from
D1 if it lands. Register prices; run the best; two fields; exact.

**D3 — THE SUPPLY VERDICT.** With delta=1 decided and D2 measured:
state the complete supply-side picture — the arbitrary-word max at
n = 8/16/32 (exact), its trend vs the 4.83-bit razor need, and
whether ANY supply-side mechanism remains that could matter at
razor scale. If D2's number still grows: that is a real finding —
characterize the maximizer class (which delta, which structure)
and what it would need to reach the razor need. If it collapses
like delta=1: the supply side of the band question is CLOSED as
evidence, and say so with the margin.

**D4 — THE MINT PACKAGE (if budget remains).** The parity theorem
+ the STRAT_1 closed form + (if D1 lands) the recursion, drafted
as a self-contained mint note (statement, proof, verification
harness pointers) for the coordinator's mint queue.

## Escape tests (before the main work)

- Replay ms_exact.py at n=8,16 (SCRATCH COPY; coordinator got
  IDENTICAL at 8/16/32/64) — your machinery must match before
  extending it.
- Reproduce the round-27 maximal-slack sampled values (67 at n=16,
  two fields) from the banked nonpoly machinery (SCRATCH COPY).

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4474; do not read the other round-29 pilot dirs
  (collinearity_object, list_profile_bound, k_extremal). Pass this
  clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT
  documented per use.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads; checkpoint everything; background batches with
  results files for >10-min runs. Beat walls BY DESIGN, never by
  relaxation.
- DRAFT-ONLY: writes only in notes/pilots_20260810/slack_recursion/;
  no dag/nodes/tools writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C).
  Two-field confirmation for structural claims. Own-repo grep
  before claiming anything is missing (CATCH-24A).
- Your final message IS the report. End with a compliance
  paragraph.

## Pilot registrations (appended by the pilot before any computation)

**All of §R0-§R6 below was written BEFORE any interpreter ran.** Only
file reads (this PREREG, maxscan REPORT/FABLE_AUDIT/ms_exact.py/
ms_strat.py, nonpoly REPORT + nf_probe.py, the band node statement)
preceded it.

### R0 — the framework I am working in (derived from primary text, before computing)

n = 2^r, D = mu_n subset F_q, q = 1 mod n, k = n/2, t = 1,
a = k+t = n/2+1, m := n-a = n/2-1 = |B| for B = D\A.
Received word Y, deg Y = a+delta, delta in [0, n-1-a] = [0, m-1].
W(z) := normalized reversal of Y truncated mod z^{t+delta+1}, W_0 = 1.

Re-derived from scratch (agrees with the round-27 window-shift
theorem): multiplying (FL1) by l_B and using l_A l_B = 1 - z^n,

  A admissible  <=>  [z^{delta+1}]( W(z) * l_B(z) ) = 0,
  l_B(z) = prod_{b in B} (1 - b z),  c_i(B) := [z^i] l_B = (-1)^i e_i(B).

So at t=1 the delta-stratum condition is ONE linear functional
lambda on (c_0..c_{delta+1}) with lambda_{delta+1} = W_0 != 0, and
**the union over ALL delta strata is exactly the set of all nonzero
linear functionals on (c_0,...,c_m)** (top nonzero index j = delta+1).
This is the exact reading of D2's "all delta strata".

### R1 — named functionals (CATCH-19C)

- `F_SUBSET(W)` = #{B : |B| = m, [z^{delta+1}](W l_B) = 0} (= # admissible a-subsets A).
- `F_LIST(W)` = # distinct codewords f = Y - L_A u (# distinct P = L_A u).
- `AGRPROF(W)` = multiset of agreements j = #roots of P in D; dedup law F_SUBSET = sum_j m_j C(j,a).
- `PLATEAU(n)` = C(n/2-1, n/4) (slack-0 max; both F_SUBSET and F_LIST there).
- `LOCSUB_delta(n)`, `LOCLIST_delta(n)` = max of F_SUBSET / F_LIST over the LOCATOR family W = l_S, |S| = t+delta (round 27's family; Y = X^k L_S at maximal slack).
- `MAXWORD_SUB(n)`, `MAXWORD_LIST(n)` = max over ALL words (all delta, all W) of F_SUBSET / F_LIST.
- `RATIO_SUB/RATIO_LIST(n)` = MAXWORD_*/PLATEAU; `SURPLUS` = log2 RATIO.
- `BOXFRAC(n)` = fraction of parity-class-restricted contributing nodes satisfying the level-2 (recursion) constraint — D1's reduction factor.
- `SLACKCEIL`: agreements lie in [a, a+delta] (deg P = a+delta), hence F_SUBSET <= F_LIST * C(a+delta, a).

### R2 — THE OBJECT CORRECTION I am registering BEFORE measuring (the pilot's main risk)

The razor need (2^127.9 vs C(127,64) = 2^123.17) is a **list-size**
need, and PLATEAU is a **list** count. F_SUBSET is only an upper
proxy, and I claim the proxy DEGENERATES at high slack:

**(T2) DEGENERACY THEOREM (registered as a prediction, to be tested
exactly at n=8 over all words).** The word Y = f + c(X^n-1)/(X-u)
(Hamming distance 1 from the code) has deg Y = n-1 = a + (m-1),
i.e. it is a legal MAXIMAL-SLACK word, with word class
W(z) = sum_{j<=m} u^j z^j, and it has
  F_SUBSET = C(n-1, a)   and   F_LIST = 1.
Predicted: MAXWORD_SUB(n) = C(n-1,a) exactly (21 at n=8, 5005 at
n=16, 265182525 at n=32) — a TRIVIAL maximum with list size ONE.
Consequence: round 27's maximal-slack "67 > 46 growing" compares
F_SUBSET across strata with different C(j,a) inflation factors
(SLACKCEIL) and is therefore CONFOUNDED; the supply object of record
must be MAXWORD_LIST.

### R3 — D1: the recursion, stated exactly, and my prediction

Round-28 note: "E on one parity class is itself an e2 one level
down". Exact statement (level n = 2M, M = 2K, omega = zeta^2 of
order M, rho = omega^2 of order K):

  (REC-STRONG) In the parity-restricted problem (S contained in the
  even pairs, S = {2u : u in U}), the level-M parity theorem applies
  to E'(U,sigma) = sum_{u<u'} s_u s_u' omega^{u+u'} against the
  level-n target equation E' - omega_T = c, forcing U into a single
  level-M parity class, and hence the stratum ceiling to iterate
  (s <= n/8), giving cost 3^{K/2} in place of 3^K.

**PREDICTION P7: REC-STRONG IS FALSE.** Reason registered in
advance: splitting the equation over Z[rho] + omega Z[rho], the
odd component reads X''Y'' = -sum_j d_{2j+1} rho^j, whose RHS is
NOT zero — omega_T ranges over ALL {-1,0,1}-coefficient vectors of
length K, not only the even-power ones (that is exactly where the
level-M problem differs from the level-n restricted problem: the
level-M T-part uses rho^j only). The correct surviving statement is

  (REC-BOX) X'' Y'' lies in the {-1,0,1}-coefficient box of Z[rho],
  where X'' = sum_{v: 2v in U} s ρ^v, Y'' = sum_{w: 2w+1 in U} s rho^w.

Registered numbers: BOXFRAC(32), BOXFRAC(64) in [1/20, 2/3] (i.e.
the box prunes by LESS than 20x); a level-2-parity-split
counterexample EXISTS at n=32 or n=64 (confidence 70%). If
REC-STRONG were true instead, n=128 would price at ~3^16 = 43M
nodes ~ 5 min. Under REC-BOX I register the price as
**>= 10^4 core-hours (Modal-class) and therefore DEAD**, plus the
decision-value note: the delta=1 verdict is already decided at four
scales, so an n=128 delta=1 point has ~zero decision value.

### R4 — D2 routes, priced BEFORE building (the brief's three routes re-priced)

- (a) delta-stratified union, exhaustive over all words: cost
  q^delta * C(n,m) per stratum with the round-28 dense-counter trick.
  n=16, q ~ 10^4: delta=1 = 1.1e8 (banked, 4 min); delta=2 = 1.1e12
  **REJECTED**; n=32 delta>=2 **REJECTED** (>= 5.7e12).
- (b) direct subspace closure / F_LMAX at n=32: one pass over
  C(32,15) = 5.66e8 subsets with an 16-term dot product per subset
  = 9e9 ops **REJECTED for a family scan** (~3-6 h/word, 1.8e7
  rotation orbits).
- (c) the D1 recursion: predicted dead (R3).
- **(d) MY ROUTE, not in the brief: exact-by-exhaustion at n=8 over
  the ENTIRE word space** (enumerate P = L_A * u, |A| = a, u monic
  of degree <= n-1-a; hash by the coset key = coefficients of
  degrees k..n-1; count per key = F_SUBSET, distinct P per key =
  F_LIST). Cost 56*(1+q+q^2) items: 3e5 at q=73, 7e5 at q=113.
  This settles MAXWORD_SUB(8) and MAXWORD_LIST(8) EXACTLY over all
  received words and all delta, at three fields.
- **(e) MY ROUTE at n=16: the locator ladder, ORBIT-EXHAUSTIVE.**
  The rotation group mu_16 acts simultaneously on S and B, so
  LOCSUB/LOCLIST are constant on rotation orbits: 715 orbits at
  delta=6 (11440/16), and Sum_{j=2}^{7} C(16,j)/16 ~ 1645 orbits for
  the whole ladder. Cost = 11440 precomputed c(B) vectors x 8 mults
  x ~1645 words = 1.5e8 ops (minutes). F_LIST is then computed with
  the banked nf_probe instrument on the top words only, descending
  by F_SUBSET until max-F_LIST-so-far >= the next F_SUBSET (exact
  by the F_LIST <= F_SUBSET sieve). Two fields.
  VALIDITY CHECK for using the locator family at n=16: at n=8,
  compare route (d)'s all-word maximum against the locator maximum.

### R5 — predictions with numeric windows (misses reported first)

- **P1** ESCAPE-1: ms_exact scratch replay at n=8,16 gives exactly 6 and 46, per-stratum identical. Tol 0.
- **P2** ESCAPE-2: I reproduce the round-27 maximal-slack value 67 at n=16 in two fields. I predict 67 is F_SUBSET and that the SAME word has F_LIST in [8, 40] (point estimate 20), with a non-flat AGRPROF (some agreement > a).
- **P3** MAXWORD_SUB(8) = 21 = C(7,5) exactly (window [21, 30]), maximizer class = the distance-1 / fully-split words Y = c L_R, |R| = n-1, with F_LIST = 1. At n=16 the distance-1 word measures F_SUBSET = 5005, F_LIST = 1 (tol 0).
- **P4** MAXWORD_LIST(8) = 6 (window [5, 10]); RATIO_LIST(8) = 2.0 (window [1.67, 3.33]); attained at delta <= 2 with point estimate delta = 1.
- **P5** LOCSUB_6(16) (orbit-exhaustive over all 715) >= 67; point estimate 83; window [67, 200].
- **P6** max over the WHOLE n=16 locator ladder of F_LIST is attained at delta = 1 with value 39 (window [35, 60]); and LOCLIST_6(16) <= 35 = PLATEAU (window [1, 35]).
- **P7** as in R3 (REC-STRONG false; BOXFRAC in [1/20, 2/3]; n=128 dead).
- **P8** SUPPLY TREND: RATIO_LIST(8) in [1.67, 3.33] and RATIO_LIST(16) in [1.0, 1.7] — i.e. DECLINING; combined with the banked delta=1 collapse at n=32/64 the supply side closes with margin >= 3 bits at n=32 against the +4.83-bit razor need.
- **P9** TWO FIELDS: every structural n=16 value identical at q=10177 and q=12289; every n=8 value identical at q=73, 97, 113 (char-0).
- **P10** COST: the literal D2 ask ("exact arbitrary-word max at n=32") is (i) TRIVIAL under F_SUBSET (= C(31,17) = 265,182,525 by T2) and (ii) out of stdlib reach under F_LIST (>= 3 core-hours for ONE maximal-slack word; >= 10^6 core-hours for the family). I register this as the answer to the pricing part of D2 rather than as a computation I will run.

### R6 — thresholds and stopping rules

- A supply-side surplus matters only if RATIO_LIST >= 2^4.7286 = 26.5 at razor scale; any measured RATIO_LIST <= 4 at n=8/16 that DECLINES with n is reported as CLOSING evidence with the margin in bits.
- Background control: at n=16, q ~ 10^4, mean per fiber = 11440/q = 1.12, banked B_pois = 13; I treat any value <= 13 as background and require two-field equality for every structural claim.
- If P2 comes back with F_LIST = 67 (i.e. a flat AGRPROF), R2's correction is WRONG and I report that first as the headline miss, and the maximal-slack curve stays alive.

## Outcomes (appended AFTER the computations; the report is the record)

R6's fallback fired: **P2 came back with 67 = the banked F_LIST maximum**,
so R2's confounding hypothesis was half-wrong (T2 is exactly true and does
explain the OTHER banked number, F_SUBSET = 2054 = 2002 + 52), and the
maximal-slack curve stayed alive — and then grew.

| reg | outcome |
|---|---|
| P1 | HIT tol 0 (6, 46; and my re-implementation reproduced 1974 / {1:630, 3:1344}) |
| P2 | **MISS** — 67 is F_LIST, not F_SUBSET (F_SUBSET at that word = 349) |
| P3 | HIT tol 0 (21 at 3 fields, 5005 at 2 fields, F_LIST = 1) |
| P4 | window HIT, point MISS (7, not 6; at delta = 2, not delta = 1) |
| P5 | MISS as written (LOCSUB_6 = 5005, not in [67,200]); the intended quantity LOCLIST_6 = 111 lands in the window |
| P6 | **MISS** (max is at maximal slack, not delta=1; 111 over the locator family, 715 over all words) |
| P7 | HIT (REC-STRONG refuted, 88 counterexamples at n=32; n=128 dead). BOXFRAC(32) = 0.366 in window; BOXFRAC(16) = 0.802 outside |
| P8 | **MISS, and the headline** — the trend GROWS (+1.22, +4.35, +11.42, +26.46 bits), it does not decline |
| P9 | HIT (all structural values identical across fields; the two field-dependent locator cells delta=3,4 correctly flagged non-structural) |
| P10 | superseded — the n=32 arbitrary-word maximum needed no computation: it is a theorem, pinned within 1 bit |


