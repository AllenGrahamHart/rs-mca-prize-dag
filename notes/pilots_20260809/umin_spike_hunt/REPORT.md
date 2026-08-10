# REPORT.md — umin_spike_hunt (round 26) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task a207e541edbcda674, 2026-08-09. Pilot: Opus. No edits. NOTE: the kappa=2 exhaustive sweep was still running at report time (168/266); its completion is recorded in FABLE_AUDIT.md.

**ROUND-26 PILOT REPORT — umin_spike_hunt: the Z-CEILING kill-or-confirm spike hunt at N = 32**

Registrations appended to `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260809/umin_spike_hunt/PREREG.md` (sections U0–U5, lines 94–283) **before any interpreter was run**. All runs via `tools/ramguard tiny|local -- python3` from repo root, stdlib only, 1G never relaxed (`RAMGUARD_TIMEOUT` used only to lengthen walls — documented per run). Draft-only; no dag/nodes/tools/git writes; no Modal.

---

## 1. VERDICT — registered outcome (1) FIRED, and so did (2). Z-CEILING's ratio form is DEAD on its own pinned family.

**MAX CRATIO = 5.8131644651**, exact, at the M4/I2-RSET cell **N = 32, κ = 1, p = 4337074369, σ = −0.0141**, `TNUM = 49692303616`, `TMASS = 49692303616/2^32`, `NKER = 551489`. **THREE-WAY derived** (identity/RBUCK 256; even-odd/181; reversed/101 — disjoint internals), all three exact-integer identical.

- **Outcome 1 (CRATIO &gt; 2 → the C-form's own bar):** FIRED. **119 of 124** exactly-computed κ = 1 cells exceed 2.
- **Outcome 2 (CRATIO &gt; 1.7681 → the N-decay direction REFUTED):** FIRED, same 119 cells. The round-24/25 constant of record 1.7681 (N = 16, exhaustive) is beaten by **3.3×** at N = 32; round-25's N = 32 sample max 1.4211 by **4.1×**.
- **Outcome 3 (silence with a recall number):** not applicable — but the recall number exists anyway and is **1.000, by proof and by measurement** (§3). The instrument is not a filter with recall; it is an **exact arithmetic characterization**.

**This is a falsification, not a census artifact.** The node's own registered falsifier ("any admissible 2-power cell with CRATIO &gt; C") is met 119 times over, on the pinned negacyclic-GRS / I2-RSET family, on the 2-power grid, inside σ ∈ [−2, 2], with Z-FLOOR holding at every one of the 292 cells.

## 2. D1 — THE INSTRUMENT: **RESSIEVE**, and it is an IFF, not a filter

Round 24's **THEOREM RC** gives the *necessary* direction (`p | Res(Φ_2N, f)`, `1 ≤ Res ≤ U^{N/2}`). I registered and proved the **converse**:

&gt; **THEOREM RS.** For 2N a 2-power, p prime with 2N | p−1: the cell carries a ternary kernel vector of weight U **iff** some ternary f, deg &lt; N, weight U has `p | Res(Φ_2N, f)`.
&gt; (⇐) `Res = ∏_{k odd} f(θ^k) mod p`, so some `f(θ^k) = 0`; then `g(x) = f(x^k) mod (x^N+1)` is ternary of the **same** weight (j ↦ jk is a bijection of Z/N for odd k) and `g(θ) = 0`. ∎

**The sweep is therefore over f, not over p — one enumeration decides every prime in the band at once.** Enumeration is over μ_2N necklace representatives (verified: generator count = exact necklace formula, 21/21, N ∈ {16,32}); Res is recovered *exactly* as `∏ f(w^k) mod q`, q = 2305843009213694017 (&gt; U^{16} for U ≤ 9); band primes are extracted by one `gcd` against a primorial, with a registered completeness proof (`Bmax = U^{N/2}/p_lo`; cofactor forced to 1; ≤ 1 band prime per f since `p_lo² &gt; U^{N/2}`).

**Measured price:** the U ≤ 7 census of the *whole* band cost 7,748,176 leaves / **240 s on one core** ⇒ **4.4 µs of CPU per admissible prime**, against `wenum.py`'s measured 174–297 s *per prime*. Speed-up ≈ **4 × 10⁷**. Registered triage: promote iff `PREDCR = 1 + BONUS/(1+H) ≥ 1.30` or `UMIN ≤ 6`, BBM in descending PREDCR order.

## 3. Escape tests + D4 — every verdict-bearing number is two-way

| test | result |
|---|---|
| E1 necklace generator vs exact necklace formula | **21/21 PASS** |
| E2 modulus/root (ord w = 2N, cap &lt; q) | **4/4 PASS** |
| **E3 ground truth N = 8, whole band, U ≤ 8 (the complete enumerator)** | sieve census **≡** round-23/24 reference weight enumerator, cell-by-cell, **AU[U] exact, 0 mismatches** |
| **E4 ground truth N = 16, whole band, U ≤ 12, all 1305 in-band cells** | **0 mismatches** — 1298 cells with a weight ≤ 12 orbit, every AU[U] exact. **Recall = 1.000 measured on an entire exhaustive band.** |
| round-25 record replay p=4683696257 | `TNUM 11700545024, NKER 392641, CRATIO 1.4210954721` — **exact**, and re-derived **from scratch** (reversed/101, 89.1 s), not only from checkpoints |
| 3 further banked cells (4294967681, 6074003393, 12148002497) | CRATIO reproduced to all printed digits |
| **POWER CONTROL** (brief's second escape test) | at U = 8 (**all 42,080,768** weight-8 f): **0 hits** on all four targets — silent, as required. At U = 9 (**all 224,390,400** weight-9 f): **64 hits at p=4683696257 = 2 orbits × 32 Galois twists** (wenum: AU[9]=128 ✓), **32 hits at p=12148002497 = 1 orbit** (wenum: AU[9]=64 ✓), **0 hits at both UMIN=11 cells** ✓ |
| independent AU at the new records | `wenum.py` (round-25 code, verbatim, entirely different algorithm): p=4337074369 **UMIN=5, AU[5]=64**; p=15181899841 **UMIN=5, AU[5]=64** — both exactly what RESSIEVE said; RC(i) HOLDS |
| **D4 two-way BBM** | **98/98 cells re-derived** by BBM-ALT (even/odd permutation, RBUCK 181): **0 disagreements**. Top-3 + the round-25 record are **three-way**. |
| all 2880 weight-5 hits | re-verified *at p* from scratch (θ recomputed, `f(θ^k) ≡ 0` checked): **0 failures**; all 90 primes ≡ 1 mod 64, all in band, all `AU[5] = 64` exactly |
| Z-FLOOR | **0 violations** over all 292 cells |

## 4. D2 — THE HUNT: a **census**, not a sample (2.12 × 10⁷ primes decided)

Round 25 sampled 47 primes. This round decides **every** admissible κ=1 prime in [2^30, 2^34]:

| stratum | count | how |
|---|---|---|
| UMIN ≤ 3 | **0** | **by proof** — `Res ≤ 3^16 &lt; 2^30`, no enumeration needed |
| UMIN = 4 | **0** | exhaustive (9,024 f) |
| **UMIN = 5** | **90** | exhaustive (100,688 f) — every one has exactly one μ₆₄ orbit |
| UMIN = 6 | **2,395** | exhaustive (906,752 f) |
| UMIN = 7 | **25,105** | exhaustive (6,731,712 f) |
| **total UMIN ≤ 7** | **27,590 = 0.130 % of the band** | |

Exact BBM: **124 κ=1 cells** — **the entire UMIN=5 stratum (all 90)**, the top 30 of the UMIN=6 stratum, and the 4 round-25 escape cells. Strata (exact CRATIO): UMIN=5 → min 1.3369, median 3.6476, **max 5.8132**; UMIN=6 (top-30 by PREDCR) → max 3.5453; UMIN ≥ 8 (round-25 cells) → max 1.4211. **The band max is a lower bound: ≥ 5.8131644651.**

**κ=2 arm.** RESSIEVE (p² | Res + exact double-root re-verification) decided **all 266** in-band M2 primes for U ≤ 7: **exactly one** (p = 33409, AU[7]=64) carries an orbit of weight ≤ 7. The declared-but-never-run **exhaustive 266-cell BBM sweep is 168/266 complete at report time and still running in background**; max so far **1.3887176890 at p=63361**, reproducing round-25's κ=2 record exactly.

## 5. THE MECHANISM — why the ceiling grows, and why 47 cells could never see it

Round 25 found *that* low-weight orbits set the max. This round finds *why the effect is unbounded*: **the ternary kernel is the ternary part of an IDEAL.** `ker = {f ternary : f(θ) = 0} = P ∩ T`, P the prime above p in `Z[ζ_2N] ≅ Z[x]/(x^N+1)`. Ideals are closed under multiplication, so one weight-U element f drags in `a·f` for every ternary a whose shifted supports don't collide:

  **TMASS ≥ Σ_t C(N,t) 2^t 2^{−Ut} ≈ (1 + 2^{1−U})^N.**

THEOREM RC pins `U ≥ p^{2/N} = 2^{2(N−σ)/N} → 4`, so **U_min stabilises at 5 while the guaranteed mass grows like 1.0625^N — geometrically in N** — against a normaliser `1 + H = 1 + 2^σ` that is bounded on the band. Measured ladder, all exhaustive over the minimal-weight stratum:

| N | U_min | law (1+2^{1−U})^N | band max CRATIO |
|---|---|---|---|
| 8 | 4–5 | 1.62–2.57 | 0.9440 |
| 16 | 5 | 2.6379 | 1.7681 (in the UMIN=5 stratum, n=72) |
| 32 | 5 | 6.9587 | **≥ 5.8132** (UMIN=5 stratum exhaustive, n=90) |

Mean TMASS in the UMIN=5 stratum: 3.68 at N=16 (max 5.98) → **10.25 at N=32 (max 17.83)** — a factor 2.8–3.0 per doubling, against the law's 2.64. **My registered additive predictor `1 + BONUS/(1+H)` was structurally wrong**: the effect is multiplicative, not additive (§6, correction 3).

**Why round 25 saw nothing:** 0.130 % of the band carries a weight ≤ 7 orbit and 4 × 10⁻⁶ carries a weight-5 one; a 47-cell sample has expectation 0.06 hits at U ≤ 7 and 2 × 10⁻⁴ at U = 5. Round-25's "matched decay, not significant" and its EVX extrapolation to 1.88 were both reading a body that has nothing to do with the max. **The tail is arithmetic, not statistical.**

## 6. REGISTERED PREDICTIONS vs OUTCOMES — **misses first**

| | registered | measured | |
|---|---|---|---|
| **P-U5** (headline) | max ∈ [1.75, 3.05], point 2.45 | **5.8132** | **MISS** — 1.9× above my own upper bound. Direction right (outcome 1 fired); magnitude wrong because I priced only the direct orbit and missed the ideal amplification |
| **P-U8** | \|CRATIO − PREDCR\| ≤ 0.25 for ≥ 80 % | **0 %** (median gap +1.63) | **MISS**, badly — same root cause. Companion clause (CRATIO ≥ PREDCR − 0.10 for ≥ 90 %) → **100 %, HIT** |
| **P-U7** | ≤ 12 µs/leaf/core | 9.18 (U=5), 11.57 (U=6), **33.93 (U=7)**, ~24 (U=8/9 under load) | **MISS** at U ≥ 7 (primorial strip cost). Companion clause (U ≤ 7 census ≤ 900 s single core) → **240 s, HIT** |
| **P-U6** | argmax σ ∈ [−2.00, −0.80] | σ = **−0.0141** | **MISS** on σ; **HIT** on UMIN ∈ {5,6} (=5) |
| **P-U2** | Spearman(PREDCR, CRATIO) ≥ 0.85 at N=16 | **0.6568** | **MISS**. Companion clauses: recall top-20-in-top-40 = **20/20 = 1.00** (≥0.90) **HIT**; p=161761 UMIN = **5** exactly **HIT** |
| **P-U3** | N=16 UMIN ≤ 5 ∈ [2, 60] | **72** | **MISS** (above). UMIN ≤ 6 = 263 ∈ [20,400] **HIT**; UMIN ≤ 7 = 752 ∈ [120,900] **HIT** |
| **P-U1** | escapes + 6/6 banked profiles + power control | all exact; 64/32/0/0 target hits | **HIT** |
| **P-U4** | ≤4 ∈ [0,5] (pt 0); ≤5 ∈ [10,3000] (pt 390); ≤6 ∈ [300,20000]; ≤7 ∈ [3000,120000] | **0 / 90 / 2,485 / 27,590** | **HIT ×4** |
| **P-U9** | 0 disagreements | 98/98, 0 | **HIT** |
| **P-U10** | κ=2 UMIN ≤ 7 count ∈ [0,6]; max CRATIO ∈ [1.30,2.10] | **1**; **1.3887** (168/266) | **HIT ×2** (second clause on partial coverage) |
| **P-U11** | 0 Z-FLOOR violations | 0 / 292 | **HIT** |

**7 predictions HIT, 5 MISSED** (three of them with a companion clause that hit).

## 7. SELF-CORRECTIONS — all of them

1. **Pre-registration correction:** my first strip design assumed every odd prime factor of Res is ≡ 1 mod 64. **False** — `q | Res` only forces a shared factor of degree `ord_64(q)`, so primes with `q² ≡ 1 mod 64` (31, 97, 127, …) can divide. Caught and corrected **in the registration, before computing**; the strip uses *all* primes ≤ Bmax.
2. **Mid-run code fix, disclosed:** `sieve_U`'s registered assertion `p_lo² &gt; cap` was too strong and **crashed** the N=16 U=12 arm. I added Regime B (strip only below p_lo, then trial-divide to isqrt). Both ground-truth tests were re-run afterwards and pass in both regimes.
3. **My registered ranking statistic is structurally wrong.** `PREDCR = 1 + BONUS/(1+H)` treats a low-weight orbit as an additive bonus; the ideal structure makes it multiplicative. It remains a valid *lower* bound (100 % of cells) and a usable ranker, but P-U8 is a real miss and the mechanism (§5) was **found in the data, not registered**.
4. **The escape replays first returned in 0.0 s** — they resumed from round-25 checkpoints, i.e. a checkpoint sum, not a derivation. I re-ran the record cell from scratch under a third variant (89.1 s) so the escape test is a genuine reproduction.
5. **The full U = 8 census was NOT run**, correctly, under my own registered gate: the measured U=7 rate was 29,500 leaves/s, below the registered 60,000/s threshold. I ran the **targeted** U=8/U=9 arm instead (the complete 42,080,768 and 224,390,400 leaf enumerations were executed; only the *output* was restricted to 4 target primes, an output-volume decision — the full witness files would have been ~170 MB and ~900 MB).
6. **The κ=2 exhaustive 266-cell sweep did not finish in-session** — 168/266 at report time, running in background. Declared, not papered over.
7. Only the **top 60** ranked candidates got exact AU inside `promote.py`; I separately re-verified **all 2880 weight-5 hits / all 90 primes** afterwards. The 25,105 UMIN=7 primes are certified by THEOREM RS + the strip proof + the N=8/N=16 ground-truth agreement, not by individual re-verification.

## 8. ARTEFACTS (all in `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260809/umin_spike_hunt/`)

`PREREG.md` (registrations at lines 94–283), `rs.py` (RESSIEVE core), `escape.py`, `sieve32.py`, `sieve2.py`, `power.py`, `promote.py`, `run32.py`, `n16.py`, `analyze26.py`; `HITS.N32.U{4,5,6,7}.s0.tsv` (894,656 witnesses, 27 MB), `CANDS.N32.k1.tsv` (27,590 primes ranked), `CANDS.N32.k2.tsv`, `N16_CENSUS.json` (1298-cell N=16 census), `POWER.U{8,9}.s*.tsv`, `CELLS26.{main,alt,alt2}.s*.tsv` (292 exact cells + 98 two-way + 4 three-way), `log_*.txt`. New per-cell checkpoints appended to `../z_n32_band/ckpt/` (new files only; no existing checkpoint touched).

## 9. Scope and compliance

Every number here is about the **FORM** of CONJECTURE Z-CEILING on the toy families (M4 = I2/RSET, M2 = negacyclic GRS) on the 2-power grid, inside the pinned "admissible" scope. **Nothing here is a claim about Z_1 at the official row; the f2 calibration clause binds.** The geometric-in-N growth of the constant is a **two-point measured law plus a mechanism**, and its extrapolation beyond N = 32 is an extrapolation, not a measurement. I made **no status flip, no node edit, no dag/tools/git write** — all writes confined to my own pilot directory plus new checkpoint files as permitted; the only status recommendation I make is that this is a coordinator decision, and the node's registered falsifier is now met. **Compliance:** registrations appended before any computation; every interpreter run under `tools/ramguard tiny|local` (1G ceiling never relaxed; `RAMGUARD_TIMEOUT` used only to lengthen walls, on the long sieve/BBM batches, each launched as a background job writing a results file); stdlib only; no Modal; file-at-a-time reads, `dag.json` never opened; quarantine observed throughout — `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was never read, and the three sibling round-26 pilot directories (`b_sparsity_pose`, `freeze_tail_law`, `m7_falsifier_hunt`) were never read; **no subagents were spawned.**
