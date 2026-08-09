# REPORT.md — nonpoly_flank_census (round 27) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task ada97dab53f92c0a7, 2026-08-09. Pilot: Opus. No edits.

## VERDICT — the flank is **not clean**: a real, char-0, two-field structural surplus over the slack-0 plateau, but the node's pre-registered falsifier does **not** fire

**The flank is now parameterized, censused, and it is non-empty.** The banked THEOREM CAP ("within the coset/dressing/perturbation universe the char-0 supply is capped at the C(N−1,h) plateau") is **scope-limited to slack 0**: off that stratum the exact maximum is strictly larger, at two scales, in two independent fields.

| cell | poly side (slack 0) | flank | surplus |
|---|---|---|---|
| n=16, t=1, δ=1, **exact max over all 1.036·10⁸ word classes** (q=10177 **and** q=10193) | 35 | **F_SUBSET = 46** (argmax = the antipodal-pair-locator word, W₁=0), **F_LIST = 39** achieved | +0.156 bits (achieved) / ≤ +0.394 bits (bound) |
| n=8, t=1, δ=1, exhaustive census, q = 73/97/113/241 (constant ⇒ char-0) | 3 | **5** | +0.737 bits |
| n=16, t=1, δ=6 (**maximal slack = arbitrary received words**), 120 locator words × 2 fields | 35 | **67** (identical word, identical count at q=10177 and q=65537); a further draw reached 83 at q=65537 | +0.94 bits (2-field) / +1.25 bits (1-field) |
| razor row requirement | C(127,64)=2^123.1714 | needs 2^127.900…2^128.000 | **+4.7286…+4.8286 bits** |

**What did NOT deviate.** The node's falsifier is about the *first-moment model*, sustained across ≥3 scales, either direction. It is intact: the mean law held **exactly in 58/58 exhaustive cells**, F_MAX ≤ B_pois in **every** exhaustive cell, and the sporadic ladder is empty in every starved row (203 primes at N=8, 14 starved rows at N=16 including q≈2^40). So: **window law confirmed and extended to the flank; supply-cap claim refuted off slack 0.** The surplus is 2 scales, not 3, and it is a max/supply phenomenon, not a first-moment one.

## D1 — the escape class, parameterized (registered before computing)

Every received word is a polynomial, so "non-polynomial" cannot mean what it says. Exact reading: with a = k+t, deg Y &lt; k ⇒ list 1; k ≤ deg Y &lt; a ⇒ list 0; **deg Y = a is exactly the fiber reduction's hypothesis**, and the banked instrument-2 domain c ∈ F_q^t *is* the complete parameterization of that stratum modulo C and scaling — the poly side is censused completely, not just for the shape X^k L_T0.

**THE ESCAPE CLASS = positive slack** δ = deg Y − a ∈ [1, n−1−a], with word classes W ∈ F_q^{t+δ} (q^{t+δ} of them). The admissibility condition is (FL1) `L_A(z)·û(z) ≡ W (mod z^{t+δ+1})`, deg û ≤ δ — the same moment-map fiber quotiented by a degree-≤δ unit. **The planted-hybrid family is NOT the whole class**: it is the support sub-class {W : list ≥ 1}. **Giant slack saturates at δ = n−1−a, where the flank is literally the set of arbitrary received words** — i.e. the banked census measured the maximum on one stratum of a family whose top stratum is the prize's own list-side object.

Escape tests (scratch copies, run unmodified): banked `rh_c3_fiber_mtm_v2.py` replayed **exactly** — cell A fiber = 3 at all 11 primes incl. q≈2^40; cell B → 35 in every starved row (`data/escape_test_1_rh_c3_replay.txt`). Generic-core law verified in vivo with my own machinery on **all 120** two-point words at n=16: r=1 → 3 = C(3,2), r=2 → 1 = C(2,2), zero background (`data/escape_test_2_generic_core.json`); the banked cell-B generics 15/5 = C(6,4)/C(5,4) agree.

## D2 — the census

- **S1 (exhaustive strata)**: 58 cells, n=8 and n=16, t ∈ {1,2,3,4}, δ ∈ {0,1,2,4}, every word class enumerated with exact list counts, per-cell histograms disaggregated (`data/s1_n8.json`, `s1_n16.json`). δ=0 is the matched control at identical cells and reproduces the plateau exactly.
- **S2 (deep-starved probes)**: 900+ exact word probes at q up to 2^40 (`s2_probe16.json`, `s2_probe_argmax.json`, `s2_locscan.json`), plus **exact maxima over the entire word space** at n=8 (1.002·10⁸ classes) and n=16 (1.036·10⁸ classes, two fields) (`s2_maxscan_*.json`).
- **S3 (quotient level)**: 203 primes at N=8 and 63 at N=16 to 2^40, plus N=32 probes at q≈2^40 (`s3_quotient_price.json`).

Backgrounds are not in play at the decisive cells: B_pois = 13 (n=16 scan, μ=1.124) and 4 (n=8 scan, μ=0.0056) against observed 46 and 6; random words return 0.

## D3 — the reduction attempt: three theorems proved, one refuted (by my own census)

**Proved and verified.**
1. **Mean law (delta-independence).** Total distinct P over the stratum = Σ_{i=a}^{min(n,d)} (−1)^{i−a} C(i−1,a−1) C(n,i) q^{d−i}; every term carries q^{k−i}, which is delta-free. **58/58 exact integer matches**; the only δ-dependence is the min(n,d) truncation, visible exactly where predicted. *The first-moment model transfers to the flank with zero correction.*
2. **Window-shift reformulation (the useful form of the reduction).** In the complement coordinate B = D∖A the condition is linear: `[z^j](W·L_B)=0` for j ∈ **[δ+1, δ+t]**. The poly side is the window [1,t]; **the flank is the same width-t window shifted by δ**. This is the exact sense in which non-poly = poly + correction, and it is what makes the flank computable.
3. **Dedup law.** F_SUBSET = Σ_j (#members at agreement j)·C(j,a) held with tolerance 0 wherever measured; the structured C(r,t) multiplier is a pure subset-count artifact carrying no extra codewords (e.g. the n=16 argmax word: 46 subsets → 19 codewords, profile 16×agr-9 + 3×agr-10).
4. **Prescribed-sum theorem (P4), the C1-flank freedom, closed.** For N a 2-power, h-subsets of μ_N with sum v have multiplicity C(N/2−|J|,(h−|J|)/2) in the power basis, so **max_v is at v=0 only**. Verified exhaustively in char 0 at N=8 and N=16 (every v, no exception) and by exact probes at N=32, q≈2^40 (mult(0)=12870=C(16,8); two-root targets 3432=C(14,7); single-root and random targets 0). **Prescribing a nonzero quotient sum is a strict loss** — that escape route is closed at three scales.

**Refuted: my registered RED-2 / P2** ("flank supply = plateau(t+δ), hence dominated by the poly side"). **Named obstruction, exactly:** in complement coordinates the flank's admissible set is a **δ-dimensional affine subspace** {w : [z^j](W·L_B)=0, j∈[δ+1,δ+t]}, not a point. A subspace can meet several structured fibers at once, and dedup removes only those extra members whose agreement exceeds a. The n=16 maximiser is explicit and clean: **W = L_{{x,−x}}, the antipodal-pair locator** (condition e₂(B)=x²), identified independently at q=10177 and q=10193.

**Scaling, honestly conflicted (the sharpened residual).** The δ=1 mechanism's analytic model, n·C(n/4−1,n/8−1)/C(n/2−1,n/4), matches the data at n=8 (2.67 vs 1.67) and n=16 (1.37 vs 1.11–1.31) and then **collapses**: 0.174 at n=32, 2^−9.5 at n=64, 2^−500 at n=2^11 — this mechanism cannot reach 4.83 bits. But the **maximal-slack** surplus went the other way over my two scales (+0.74 → +0.94/1.25 bits). Two points, both lower bounds, different mechanisms: **the scaling of the arbitrary-word maximum is undetermined and is now the named residual.** n=32 at t=1 is out of reach for stdlib Python (C(32,15)=5.7·10⁸ per word); this is the one place a Modal-class run would decide the question.

## D4 — the price: source found, verified, and re-derived

**Source (found before computing, registered in the PREREG):** `critical/nodes/rate_half_band_closure/notes/witness_hunt_20260712/rh_c1_c2_zerosum_n64.py:194` — *"at q ~ 2^40 sporadic = 0 -&gt; at razor q ~ 2^256 expected ~ C(255,128)/q ~ 2^-5.3."* QUALITY.md:31–32 quotes it as ~2^−5.2/row.

**Verified exactly.** lg C(255,128) = 250.67284. Price = C(255,128)/q = **2^−5.2272 at lg q = 255.900** and **2^−5.3272 at lg q = 256.000**. So the two banked figures are the *same quantity at the two ends of the razor slice* — QUALITY.md quotes the bottom, the script the top. (My registered P6 predicted −5.225/−5.325, ±0.02: **hit**, error 0.002.) Deficit replay: 4.7286/4.8286 bits, C(127,64) = 2^123.1714 — the banked 4.73–4.83 reproduced exactly.

**Re-derived under D1.** The sporadic event is a property of (q, N, h) alone — it does not depend on the received word or on δ — so **the flank does not multiply the trial count and the price is unchanged**. What *does* change is the price's role: (i) P4 closes the prescribed-nonzero-sum generalization (v=0 optimal at 3 scales), so no flank-widened version of the hatch exists at the quotient level; (ii) the number is a *first moment on the count of sporadic members*, while closing the band needs 2^127.948 members — the hatch sits **133.3 bits** from mattering, and the banked R1c kill line (27× floor) is the correct operational form. The price stands; it was never the binding route, and the flank does not make it one. The binding route is the slack-graded supply above.

## Predictions vs outcomes (misses first)

- **P2 — MISS (registered, surplus direction).** Predicted F_MAX = max(plateau(t+δ), B_pois). Observed a q-stable structural excess over plateau(t+δ) at n=8 and n=16. RED-2 refuted with the obstruction named.
- P1 — HIT, tolerance 0, 58/58 cells.
- P3 (dedup identity) — HIT, tolerance 0, every cell measured.
- P4 (prescribed-sum law) — HIT exactly, N=8/16 exhaustive char-0, N=32 by probe.
- P5 (sporadic ladder) — HIT: 0 sporadic in every starved row (incl. q≈2^40); ladder total 188 vs first-moment 406 (ratio 0.46, inside the registered [1/4,4] window); argmax over v = 0 in every starved row.
- P6 (price) — HIT within 0.002 bits of the registered window.
- Structured-word law, the surviving half of RED-2 — HIT: struct words give exactly plateau(t+δ) at n=16 for t=2,3,4 (3, 3, 1 / 1 / 1).

## Self-corrections

1. **My own registered reduction (RED-2/P2) is refuted by my own census.** Reported at the top, not buried.
2. **I nearly reported 46 as a list surplus.** 46 is the *subset* count; the list count at that word is 19. Corrected: the exact two-field bound is F_LIST ≤ 46; the best *achieved* F_LIST at δ=1 is 39 (&gt; 35).
3. **Withdrawn: n=8, δ=2, F_MAX=7.** At q=73–113 that value is Poisson-consistent (K·μ⁷/7! ≈ 1.8–9.4); the deeply-starved probe gives 5. Only q-stable, deeply-starved values are used as structural.
4. **Cross-field comparison of rng-drawn words in the first probe batch is invalid** — `randrange(q)` shifts the RNG stream, so "the same" locator row is a different word in a different field. Every char-0 claim here uses field-independent words (struct_*, locScan_*, explicit W).
5. The maximal-slack "83" is a single-field observation; the two-field-confirmed maximal-slack value is 67. Both are lower bounds on the arbitrary-word maximum.

## Compliance

QUARANTINE honoured: `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was never opened at or below line 4062 (its only `planted-hybrid` hit is at line 4068, located by grep line numbers alone and not read); the other round-27 pilot dirs (pincer_formalization, staircase_extension, cancellation_recon) were never read or listed. No subagents were spawned. COMPUTE LAW: every interpreter invocation, including all JSON peeks and one-liners, ran as `tools/ramguard tiny|local -- python3 …` from the repo root; `tiny` (60 s default) for peeks/summaries; `local` with documented RAMGUARD_TIMEOUT for batches — 900 (escape test 1), 1500 (S1 n=8), 3000 (S1 n=16), 3000 (probe16), 2400 ×2 (max scans), 2400 (quotient+price), 2400 (argmax probe), 3000 ×2 (locator scans), 900 (escape test 2); no run hit its wall, no OOM. BANKED SCRIPTS ran only from scratch copies (`scratch/rh_c3_fiber_mtm_v2.py`, md5 identical to the banked file, unmodified; `rh_c1_c2_zerosum_n64.py` copied and read only). RAM discipline: file-at-a-time reads, `dag.json` never opened, pair counts capped at 3·10⁶ per cell, all long batches backgrounded to results files. DRAFT-ONLY: every write confined to `notes/pilots_20260809/nonpoly_flank_census/` (PREREG registrations appended before any computation; `scratch/` 4 new scripts; `data/` 12 result files); no dag/node/tools edits, no git, no Modal, stdlib only. Own-repo grep run before every "missing" claim (CATCH-24A) — it is how the price source and the PROVED `rate_half_arbitrary_line_syndrome_router` (the *received-LINE / MCA-pair* flank, a different object, explicitly not conflated and not claimed on) were found. Every measured functional is named in PREREG §R2; all grids are 2-power; no merged histograms.
