# wz_falsifiers.md — F-round 1 pre-registration against WCL-ZONE-COVERAGE

- **Date:** 2026-07-13 (written BEFORE any census computation; the only
  arithmetic below is design arithmetic — binomial sums and Poisson design
  targets — no orbit enumeration has been run at pose time).
- **Target node:** `dli_wcl_zone_coverage` (status TARGET, zero F-rounds).
- **Predicate under attack (verbatim source):**
  `critical/nodes/dli_prime_weighted_large_block_support/notes/M3_ENDPOINT_EXCEPTION_COVERAGE.md`
  section "M3 CORRECTED POSE" (lines 94-118): for every official row R and
  every level L=1..34,
  `W_cl(R,L) = sum_O 2*N_L*2^(-w(O)) <= 1/32`, `N_L = 256L`, sum over the
  COMPLETE set of reduced primitive signed-shift orbits O with
  `L+1 <= w(O) <= L+5`, after generated-field normalization and first-owner
  de-duplication of multiplier shadows and level lifts.
- **Repos are READ-ONLY.** All artifacts land in this scratchpad with prefix
  `wz_`.

## 0. Normalizations adopted (pinned, per house catch #137)

Every convention below is pinned to a repo source; the enumerator reuses the
M2 code shapes verbatim where they exist.

1. **Row family.** Analogue rows are generated prime-field full-half-section
   rows `(q, n'=2N, L)` with `q ≡ 1 (mod n')`, balance `2^N >= q^L`, aspect
   `N >= 16L` — exactly the C1' row family
   (`C1PRIME_LEVEL_SCALED_POSE.md` lines 9-13).
2. **Mass convention / N_L mapping.** The analogue ledger is the C1'
   level-scaled ledger `W_cl(q,N,L) = sum_(primitive O, L+1<=w<=L+5)
   2N*2^(-w)` (`C1PRIME_LEVEL_SCALED_POSE.md` lines 20-24; implemented at
   `m2_c1prime_level_scaled_modal.py` line 187). The WCL-ZONE mass
   `2*N_L*2^(-w)` with `N_L=256L` is this same row-native `2N` mass
   specialized to the production tower, which has `N=256L`
   (`C1PRIME_LEVEL_SCALED_POSE.md` line 35). So the analogue-to-official map
   is the C1' aspect family itself; NO separate re-scaling of the mass is
   applied to analogue rows. Applying the literal official `N_L=256L` to a
   small-N analogue row would multiply every ledger by `256L/N` and make any
   nonempty analogue ledger fail trivially — that is pre-declared a
   testability artifact, not a kill (NK-iv below).
3. **Pinned embedding (generated-field normalization).**
   `omega = g^((q-1)/n') mod q`, `g` = smallest primitive root of `q` —
   exactly `primitive_root()` + `omega` of `m2_c1prime_level_scaled_modal.py`
   lines 31-45, 72 and the census pin in `ORBIT_CENSUS_SUMMARY.md` line 5.
4. **Vanisher / level conditions.** A signed vector `v` supported on
   half-section positions `y in [0,N)`, signs in {+1,-1}, first nonzero sign
   +1, is a level-L vanisher iff
   `sum_y v_y * omega^((2l-1)y) ≡ 0 (mod q)` for ALL `l = 1..L`
   (M2 script lines 73-93). The ambient ring is `R_N = Z[z]/(z^N+1)`
   (half-section folding `z^N = -1`), as in `pro_reply_round7_fulfilment.md`
   section 4.2.
5. **Reduced signed-shift orbits.** Orbit = closure under the 2N signed
   shifts with wraparound sign flip; reduced representative = lexicographic
   minimum (`orbit_key()`, M2 script lines 48-64, reused verbatim with N a
   parameter).
6. **Primitivity.** A vanisher is primitive iff no proper signed sub-vector
   is itself a level-L vanisher (all L equations zero) — M2 script lines
   96-131, reused verbatim.
7. **Multiplier-shadow first-owner de-duplication.** Within one (row, level)
   window, orbit `P_j` is a shadow of orbit `P_i` iff there exists a ternary
   `m in R_N` (all coefficients in {0,±1}) with `P_i * m = ±z^s * P_j` in
   `R_N`. Detection is the round-7 procedure
   (`pro_reply_round7_fulfilment.md` section 4.2): invert the NxN left
   multiplication matrix of `P_i` modulo the auxiliary prime `p0 = 1000003`
   (fall back to the next auxiliary primes if singular), solve for `m` for
   each of the 2·2N signed-shift targets, accept only if the unique modular
   solution is ternary AND the product identity re-verifies exactly over Z.
   First-owner order: sort orbits by (weight, orbit-key lex); the earliest
   member of each shadow-connected component owns; later members are dropped
   from the deduplicated ledger. NOTE: no repo script implements this
   de-duplication inside W_cl itself (M2 counts shadow orbits when
   primitive); this operationalization is frozen HERE, and any divergence
   from a future canonical version is a finding, not silent drift.
   Shadow de-dup is computed for cells with 2..24 orbits; cells with >24
   orbits (super-volume, NOT-A-KILL zone anyway) are flagged
   `shadow_dedup=SKIPPED` and use the undeduplicated ledger as an upper
   bound. Shadow de-dup keeps >=1 owner per component, so it can never
   empty a nonempty window — the emptiness observable (below) is invariant.
8. **Level-lift first-owner de-duplication.** The census lift identity
   (`ORBIT_CENSUS_SUMMARY.md` item 5; validated 57/57) is the exponent
   doubling `D: R_N -> R_2N`, `y -> 2y`, which maps level-1 vanishers of the
   `(q,N)` row identically to level-1 vanishers of the `(q,2N)` row (with
   the pinned embeddings, `omega_{4N}^2 = omega_{2N}` identically). First
   owner = minimal admissible N. De-dup applies only where the smaller row
   is itself admissible (balance `2^N >= q^L`, aspect `N >= 16L`); ownership
   against inadmissible rows is declared vacuous. In this round it is active
   only on the C cells (N=64 rows own against their N=32 companions, both
   admissible for q < 2^32); for A cells the would-be owner row N=16 fails
   balance at every A band (q > 2^16), so lift de-dup is vacuous there —
   stated, not silently skipped.
9. **Exactness.** All verdict-path arithmetic is exact: python ints mod q
   for vanisher checks, `fractions.Fraction` for every W_cl and for the
   comparison to 1/32. Floats appear only in Poisson design predictions,
   never in a kill-line verdict on a single cell. Every ledger census
   asserts nonemptiness of its enumeration stream (#137 discipline), and
   every claimed vanisher is re-verified by an independent pure-python
   modular sum before being counted.

## 1. Pre-hoc structural analysis (recorded before computing)

(a) **Quantization / emptiness equivalence.** The minimum possible nonzero
contribution to W_cl(R,L) at official aspect is one orbit at w = L+5:
`2*256L*2^-(L+5) = 16L/2^L`. `16L/2^L <= 1/32` iff `2^L >= 512L`, i.e. iff
`L >= 13`. So for official levels L = 1..12, WCL-ZONE is EQUIVALENT to "the
primitive window ledger is EMPTY", and for L >= 13 it tolerates growing
orbit counts. At analogue aspect (N=32, L=1: min mass 1; N=32, L=2: min mass
1/2; N=64, L=1: min mass 2) the analogue predicate `W_cl <= 1/32` is ALSO
equivalent to emptiness. The honest cross-scale observable is therefore the
EMPTINESS indicator and the exact W_cl value, and the round tests the
volume-law scaling of both.

(b) **Volume heuristic (the null model).** For a random row, the expected
number of signed level-L vanishers of weight w is `C(N,w)*2^(w-1)/q^L`; the
expected orbit count is `lambda_orb(q,N,L) = sum_(w=L+1)^(L+5)
C(N,w)*2^(w-1) / (2N*q^L)` and the expected ledger is
`E[W_cl] = sum_w C(N,w) / (2 q^L)`. P(nonempty) ~ `1 - exp(-lambda_orb)`.
At the official rows (N=256L, q ~ 2^256-ish, q^L ~ 2^256L) these predictions
are ~2^-200 or smaller — WCL-ZONE is exactly the claim that the official
rows are not exceptions to this null.

(c) **Forced-family channel.** Because n' = 64 and 128 are 2-powers,
`z^N + 1 = Phi_2N(z)` is irreducible, so NO fixed integer vector can vanish
at infinitely many primes in these analogue towers: strictly q-independent
forced families are algebraically impossible in this round's cells. At the
official tower n'_L = 512L has odd part odd(L), where `z^256L + 1` factors
and the channel is a priori live; however the pure odd-cyclotomic
subgroup-sum construction (folded d-term progressions, d odd, d | n'_L) is
excluded at every official level: such a relation needs weight d in the
window (d <= L+5) and survival of all levels l <= L (which forces
d > 2L-1), while d | 512L with d odd forces d | L <= L — contradiction for
every L >= 1. Recorded as a pre-hoc positive structural check; COMPOSITE
forced constructions remain unprobed by this round (round-2 material).

## 2. Cells and scales (frozen row sets)

All primes are chosen by the deterministic rule "the first K primes
q ≡ 1 (mod n') with q >= 2^b", generated in-script by deterministic
Miller-Rabin. Windows are always `w in [L+1, L+5]`.

- **PC (positive controls, banked M2 rows):** L=1, N=32,
  q in {193, 449, 769, 1409, 3137, 5569, 7937, 12289}; L=2, N=32,
  q in {193, 257, 449, 577}. The direct (M2-shape) engine must reproduce all
  60 banked primitive orbit counts and all 12 banked W_cl fractions of
  `m2_c1prime_level_scaled_results.json` EXACTLY.
- **A cells (q-scaling, L=1, N=32, n'=64):** bands b = 17, 19, 21, 23,
  K = 48 primes each. Design lambda_orb ~ 3.9, 0.97, 0.24, 0.061.
- **B cells (q-scaling, L=2, N=32, n'=64):** bands b = 10, 12, 14,
  K = 24 primes each. Design lambda_orb ~ 3.7, 0.23, 0.014. (At b=10 the
  "band" spans >1 octave because such primes are sparse; predictions are
  per-prime, so this cannot bias the ratio test.)
- **C cells (n'-scaling, L=1, N=64, n'=128):** bands b = 21, 23, 25, 27,
  K = 10 primes each. Design lambda_orb ~ 9.4, 2.35, 0.59, 0.15. Each C
  prime also gets its admissible N=32 companion row enumerated for
  level-lift de-duplication.

Engines: `direct` = the M2 enumerator shape (chunked support×sign matmul);
`mitm` = meet-in-the-middle on split supports (sorted-support split, A-side
carries the leading +1 sign; for L=2 the match key combines both level
values as val1*q+val2 < 2^54, exact in int64). The two engines are
set-semantically identical; `direct` is validated against the 12 banked
cells, `mitm` is validated against `direct` on all 12 PC cells and one
N=64 cross-check prime (first q ≡ 1 mod 128 >= 2^14). Bands then run on
`mitm`.

## 3. Controls (required to trip / required to match)

- **PC-match:** all 12 banked cells reproduce exactly (else KILL-3
  integrity, round INVALID).
- **Mutation control M-1 (primitivity off):** at (q=7937, L=1) disabling the
  primitive filter must change the w=6 count from 126 to 224, and at
  (q=193, L=1) from 4497 to 4712 (banked M1 full spectra vs banked M2
  primitive counts; `eex_findings.md` RUN 5/6 confirm the same deltas).
  Not tripping => enumerator broken => INVALID.
- **Mutation control M-2 (shadow solver trips somewhere):** at (q=7937,
  L=1), the round-7 ternary-multiplier solver with the two w=3 orbits as
  owners must either (i) find at least one in-window shadow among the
  w=4..6 orbits, or (ii) find none — in case (ii) the solver is additionally
  run on a synthetic pair (P, (1+z)P reduced) which MUST trip; if the
  synthetic also fails, shadow de-dup is declared broken and all deduped
  ledgers INVALID (raw ledgers still stand).
- **Lift control (required to trip):** every C prime whose N=32 companion
  window is nonempty must have every companion orbit's doubling reappear in
  its N=64 enumerated vanisher set (the lift is an exact identity; a single
  miss = enumerator incompleteness = INVALID).
- **Nonemptiness guards:** the A(b=17), B(b=10), C(b=21) bands have design
  lambda_orb >= 3.7 and must each contain at least one nonempty cell;
  an all-empty saturated band = silent-census failure (#137) = INVALID.

## 4. Kill lines (frozen)

Let, per band B of a cell family: `Phat(B)` = fraction of primes with
nonempty POST-DEDUP window ledger; `Ppred(B)` = mean over the band's primes
of `1-exp(-lambda_orb(q))`; `Wbar(B)` = mean exact W_cl (post-dedup);
`Epred(B)` = mean of `sum_w C(N,w)/(2q^L)`; `rho(B) = Phat/Ppred`;
`rho_W(B) = Wbar/Epred`.

- **KILL-1 (forced structure).** Trips iff EITHER
  (1a) some band with `Ppred <= 0.25` and >= 10 primes has `Phat >= 0.75`
  (binomial false-trip probability < 4e-4 per band), OR
  (1b) one identical reduced orbit key recurs at >= 3 distinct primes
  (within a cell family), each occurrence re-verified by independent exact
  modular arithmetic. Either way the witness orbits are banked with full
  reproduction data. Meaning: a q-robust orbit family in the window; it
  lifts structurally to official rows, where (per 1(a)) a single orbit at
  any level L <= 12 refutes WCL-ZONE. Verdict: KILLED (structural, at
  analogue scale; official-row lift argued, not proved).
- **KILL-2 (scaling anomaly / upward trend).** For a cell family with >= 3
  surviving bands: trips iff `rho(B)` (or `rho_W(B)`) is strictly increasing
  across ALL its bands AND `rho(top)/rho(bottom) >= 4` AND the top band has
  >= 3 nonempty (resp. nonzero-W_cl) primes. Meaning: exceptional mass
  decays qualitatively slower than the q^-L volume law; extrapolated to the
  official aspect the ledger is then not expected empty and, by the
  quantization fact 1(a), any nonzero official ledger at L <= 12 exceeds
  1/32 — i.e. the analogue of "monotone upward trend in W_cl across >= 3
  scales at fixed level extrapolating above 1/32 at official scale" for an
  emptiness-quantized predicate. Verdict: KILLED (scaling).
- **KILL-3 (integrity, not a predicate kill).** Any PC mismatch,
  mitm/direct disagreement, or failed required-to-trip control => round
  INVALID for the affected engine/cells; fix or mark DEFERRED. Never
  reported as a kill of WCL-ZONE.

## 5. What does NOT count as a kill (pre-declared finite-size artifacts)

- **NK-i:** any W_cl magnitude in super-volume cells (lambda_orb >= 1):
  volume-forced mass, `ORBIT_CENSUS_SUMMARY.md` item 4; official windows
  are >= 2^200-fold sub-volume.
- **NK-ii:** nonzero analogue ledgers as such. Quantization (1(a)) makes
  every nonempty analogue cell exceed 1/32 automatically; only structure
  (KILL-1) or scaling (KILL-2) counts.
- **NK-iii:** sporadic single-prime accidents (7937-style) with counts
  consistent with the per-band Poisson tail at design lambda, however large
  their individual W_cl — unless their pattern recurs (then KILL-1b).
- **NK-iv:** applying the literal N_L=256L mass to analogue rows (see 0.2).
- **NK-v:** O(1) wobbles in rho from sub-2N orbit sizes or the Poissonized
  orbit approximation — absorbed by the 4x margin in KILL-2.
- **NK-vi:** mutation-control deltas (they are supposed to differ).
- **NK-vii:** the banked M2 rows' large W_cl values (super-volume PCs).

## 6. Verdict rules

- **KILLED:** KILL-1 or KILL-2 trips (with all controls green).
- **SURVIVED:** no kill line trips, all controls green, >= 3 bands survive
  in >= 2 cell families. Evidence weight to be stated: scales q up to
  ~2^27, n' in {64,128}, L in {1,2} only; the round cannot rule out
  official-row-specific accidents (the A1-PROD density-vs-row gap), L >= 3
  structure, odd-n' forced families (round 2), or composite forced
  constructions.
- **MIXED / DEFERRED:** control failures confined to one engine/cell
  family, or Modal shard losses leaving < 3 bands in every family.

## 7. Compute plan (Modal only; sharded; app ids recorded in wz_results.md)

Shards, each one `modal_run_script.py` call of `wz_census_modal.py` with
`--args "<shard-name>"`: `pc_l1` (PC L=1 direct+mitm+M-1+M-2),
`pc_l2a`/`pc_l2b` (PC L=2, 2 primes each, direct+mitm), `band_a` (A bands,
mitm), `band_b` (B bands, mitm), `band_c` (C bands + companions + lift
dedup, mitm), `xcheck64` (one N=64 prime, direct vs mitm; DEFERRED-able).
Failures shrink scope per section 6; nothing is rescued locally.
