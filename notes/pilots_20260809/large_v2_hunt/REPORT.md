# REPORT.md — large_v2_hunt (round 25) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task a36eb38525ff7e4e1, 2026-08-09. Pilot: Opus. No edits.

All runs complete. Here is the report.

---

# ROUND 25 — THE LARGE-v₂ WINDOW HUNT: report

**Verdict (D4): option (c) is NOT viable as posed. It is not theorem-backed — the mechanism is PROVED ABSENT — and at threshold v₂ ≥ 41 it is heuristically FALSE by ~2⁹⁸ predicted counterexamples. It cannot be repaired by raising the threshold: any threshold that retains the four deployed Proth rows leaves ~2⁴⁵–2⁴⁹ predicted counterexamples, and the only threshold that works (v₂ ≳ 136) excludes every deployed row and retains only the E1-128 pinned field, which is already certified per-row. Recommend (a) exhibit-scoped or (b) o(1)-sparsity — (b) is *positively* supported by the same measurements (bad-prime density in W_TOP ≈ 2⁻¹¹²).**

Registrations were appended to `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260809/large_v2_hunt/PREREG.md` lines 65–225 before any computation. Quarantine held: `CAMPAIGN_LEDGER.md` never opened at any line; the four other round-25 pilot dirs never opened.

---

## D1 — the v₂ ground truth at h = 8 (exhaustive)

**Calibration C1 reproduced exactly.** Full 5⁸ census: 390,624 nonzero norms, 1450 distinct, MAXNORM = 614656 = 28⁴, 536 bad primes, largest 463249, and **all nine dyadic densities match `ge_floor_falsifier/REPORT.md:130` to the printed digit** (1.00, 0.964, 0.920, 0.672, 0.281, 0.069, 0.013, 0.003, 0.000).

**The v₂ profile that round 22 never computed** (m = 4 baseline, since p ≡ 1 mod 16):

| v₂(p−1) | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13+ |
|---|---|---|---|---|---|---|---|---|---|---|
| bad primes | 274 | 125 | 74 | 38 | 11 | 8 | 4 | 1 | 1 | **0** |
| all p ≡ 1 (16) | 2398 | 1214 | 604 | 294 | 152 | 77 | 38 | 11 | 11 | 10 |
| **BADFRAC8(v)** | .114 | .103 | .123 | .129 | .072 | .104 | .105 | .091 | .091 | — |

**Answer to the brief's structural question: neither favoured nor disfavoured — the suppression is *exactly* the prime-density suppression, with no norm-structure component.** Pooled BADFRAC8 = 0.1115; every per-v value lies inside its binomial 95 % CI. Stratified inside dyadic windows (so size cannot confound): χ² = 18.56 on ~11 df (p ≈ 0.07). The tail ratios of the bad set are 0.489, 0.523, 0.460, 0.397, 0.560, 0.429, 0.333, 0.500 — geometric at ½, i.e. the 2^−(v−m) density condition and nothing else.

**MAXV2BAD8 = 12, attained by p = 12289 = 3·2¹²+1** — the Kyber NTT prime — with EXCESS 8 over baseline. I re-verified it independently of the census: w = (−1,−1,−2,−1,2,2,1,−1), ‖w‖₁ = 11, Norm = 12289 exactly, and an explicit kernel certificate ρ = 4134 of order 16 with s = 1. **So the toy analogue of option (c) is false by exhaustive exhibition at every threshold ≤ 12**, and becomes true only at v₂ ≥ 13 — matching the law VSTAR = m + log₂(#bad · K) = 4 + 8.74 = 12.74.

---

## D2 — the targeted h = 64 ladder

**Coverage.** 3,608,601 (`lad`) + 16,557,420 (`turbo`) odd-norm box vectors this round, pooled with the 1,224,000 banked round-24 samples: **21,390,021 distinct box vectors = 2²⁴·³⁵**, i.e. 2⁻¹²⁴ of the 5⁶⁴ box (2⁻¹¹¹ of its 2h² orbit classes). Pooled admissible-window prime hits: **1,260,697**. Families FAM-A/B/C3/C5, 12 registered seeds, checkpointed across the 5-minute walls. Pipeline recall cross-check: my FAM-B hit rate 0.1390 reproduces round-24's 0.1395.

**The suppression curve.** P(v₂ ≥ v) · 2^(v−7) is flat to ±3 % across v = 9…22 and LADRATIO ≈ 0.500 at every rung — **no bend, out to v₂ = 26**:

```
 v      count   P(v2&gt;=v)     K        LADRATIO
 9     116156   1.844e-1   0.7374      0.5273
12      14419   2.301e-2   0.7362      0.5005
16        930   1.498e-3   0.7672      0.5041
20         55   8.408e-5   0.6888      0.4530
24          2   4.759e-6   0.6238      0.7500
26          1   7.932e-7   0.4159      0.2500     MAXV2HIT = 26
```

**The pooled K ≈ 0.736 is an instrument artefact, not a property of bad primes.** Splitting FAM-B hits by cofactor (`d2_split.py`): **all 2947 cofactor-1 acceptances have v₂(p−1) = 7 exactly** — forced by LAW 2 below — while restricted to cofactor &gt; 1, K = 0.936, 1.029, 1.053, 1.080, 1.010, 0.917 for v = 8…13. **The population law is exactly the density heuristic, K = 1.**

**Independent high-statistics V1 test at the real h.** For every prime p ≡ 1 mod 128 below 2¹⁷ I counted incidences p | Norm(w) against the per-prime null n·(1−(1−1/p)⁶⁴): **14,691,689 incidences over v₂ = 7…16.** Ratio flat at 0.998 in every bin; homogeneity **χ² = 3.75 on 8 df (p = 0.88)**; trend **d(RATIO)/dv = +0.00009 ± 0.00028 (0.3 σ)**. A per-level suppression larger than 0.06 % is excluded at 2σ — over the 34 levels from 7 to 41 that bounds any structural factor to within 4 %.

**The graded ladder (turbo instrument).** New identity used here: if N = c·p with p ≡ 1 mod 2^L and c &lt; 2^L then **c = N mod 2^L is determined**, so a rung-L probe is one mask plus one divisibility test and costs only the tower norm. Rungs are the brief's L ∈ {8,12,16,24,32,41}; no rung at the trivial baseline 7 (CATCH-19B); cofactor coverage is complete for c &lt; 2^41 (every observed cofactor was &lt; 2³³).

| L | c-congruence met | in W_ADM | p PRIME | expected (fit) | power |
|---|---|---|---|---|---|
| 8 | 2,272,193 | 2,272,193 | 122,849 | — | — |
| 12 | 478,802 | 478,802 | 26,750 | — | — |
| 16 | 38,907 | 38,907 | 2,260 | — | — |
| **24** | **261** | **261** | **10** | 304 | — |
| **32** | **2** | **2** | 0 | 1.78 | P(0)=0.17 |
| **41** | **0** | **0** | **0** | **0.005** | **needs 627× more samples for 3 expected** |

**The v₂ ≥ 41 silence is calibrated to be uninformative**: the experiment had essentially zero power there (expected count 0.005). The 95 % Poisson upper bound is 1.81 × 10⁻⁷ per box vector, against a predicted rate of ~3 × 10⁻¹⁰ — a 2⁹ deficit. Registered honestly in advance and confirmed: **this silence is not evidence for (c).**

**Witness protocol (standing).** MAXV2HIT = 26, verified fail-closed: w ∈ {−2..2}⁶⁴, ‖w‖₁ = 125, S = 247, p = 209 bits, p ≡ 1 mod 128, v₂(p−1) = 26, cofactor 197633, BPSW + 64 MR, **norm recomputed by Bareiss determinant of the multiplication matrix (independent of the tower recursion)**, and kernel membership ρ of exact order 128 with odd s = 99. Standalone zero-import reproduction `repro_v2_r25.py` prints **OVERALL: PASS**. Negative controls fail closed on all four corruptions (flipped coordinate, shifted prime, out-of-box entry, wrong quotient order). Best witness inside the brief's c ≤ 2¹² criterion: **v₂ = 25**, cofactor 1153 ≡ 129 mod 256. **So option (c) is dead by exhibition for every threshold ≤ 26.**

---

## D3 — the mechanism: **PROVED ABSENT**, plus one new proved law

**LAW 1 (NORMLAW, elementary — subsumes the conductor-128 local-reciprocity route in three lines).** Norm(w) &gt; 0 (K totally complex). For odd p with p^e ‖ Norm(w), the residue degree f = ord(p mod N′) divides e and p^f ≡ 1 mod N′; hence Norm(w) = ∏(p^f)^(e/f) ≡ 1 mod N′ whenever it is odd. Verified: f | e on every h = 8 box norm; **0 violations** of Norm ≡ 1 mod 2h at h = 8 (exhaustive, 195,312 odd-norm vectors) and at h = 8/16/32/64 on random non-box vectors with large coefficients.

**The local-reciprocity route proves the OPPOSITE of what (c) needs.** The repo's own PROVED node states an **equality**, not an inclusion — `background/nodes/e1_n256_local_norm_cofactor_collapse/proof.md:17`: `Norm_(Q_2(zeta)/Q_2)(O_K^*)=1+256 Z_2`. The conductor-128 analogue is likewise an equality, so the local norm map is **onto** 1 + 128ℤ₂: local reciprocity gives v₂(Norm−1) ≥ 7 and **proves nothing stronger is forced**. Measured confirmation: box norms hit all 128 classes mod 2¹⁴ and all 1024 classes mod 2¹⁷, with **zero** norms outside 1+128ℤ₂.

**LAW 2 (NEW — the v₂(Norm−1) refinement round 24 flagged as the load-bearing novel part).** For h a power of two and any v ∈ ℤ[x]/(xʰ+1),
&gt; **Norm(1 + 2v) ≡ 1 + 2h·v_{h/2} (mod 4h)**

by Newton's identities with p_k = Tr(v^k) = h·(v^k)₀, plus (v²)₀ ≡ v₀ + v_{h/2} (mod 2). Tested as an identity with arbitrary integer coefficients: **0 violations at h = 2, 4, 8, 16, 32, 64.** Corollaries, all verified:
- For box w with exactly one odd coordinate at position j: **v₂(Norm−1) ≥ 8 ⟺ w_{(j+32) mod 64} = 0** — 0/3000 violations.
- **FAM-B is pinned: v₂(Norm(w)−1) = 7 identically** — 3000/3000, and independently **0 rung-8 events in ~7 × 10⁶ FAM-B samples** while FAM-C3/C5/A fire at ~46 %.
- **Cofactor law**: a FAM-B hit with v₂(p−1) ≥ 8 forces cofactor ≡ 129 mod 256 — **360/360** on the banked round-24 witnesses.

**Why this does not rescue (c).** The pinning is family-local and free to evade: nodd = 3 restores the full geometric law at a cost of 2 bits of LOGNORM (median 231 → 229). And there is no 2-adic/archimedean tension to build an obstruction on — conditioning FAM-C3 on v₂(Norm−1) ≥ g leaves the LOGNORM distribution **flat**: mean 228.54, 228.54, 228.61, 228.63, 228.41, 228.56, 228.59, 228.47 for g ≥ 7…14, and P(LOGNORM ≥ 244) flat at ~2.4 × 10⁻³. Large v₂ costs nothing in norm size.

**Verdict: PROVED ABSENT.** No structural v₂ obstruction exists; (c) cannot be made theorem-backed by this route.

---

## The decision number (CSTAR / VSTAR)

Inputs are measured or proved: orbit size 2h² = 8192 **verified** (8192 distinct vectors, 0 norm mismatches); sampled vectors carry **distinct** norms and **distinct** accepted primes (12000/12000, 498/498 — unlike h = 8, where 269 vectors share each norm); uniform-box rate 0.1634.

| window | log₂ #bad primes | with v₂ ≥ 41 | with v₂ ≥ 92 |
|---|---|---|---|
| W_ADM 2¹²⁸..253³² | 132.0 (measured) / 134.1 (heuristic) | **2⁹⁸** | 2⁴⁷ |
| W_TOP 2²⁴⁴..253³² | 130.2 | 2⁹⁶ | 2⁴⁵ |
| deployed band 2¹⁶⁶..2¹⁷² | 129.8 | 2⁹⁶ | 2⁴⁵ |

**VSTAR ≈ 139 raw, ≈ 136 after the honest h = 8 haircut** (the estimator over-predicts the toy by 7.1× = 2^2.83; stated, not hidden). The two independent estimators (empirical rate vs Mertens/lattice heuristic) agree within 4×.

Row inventory, verified: **E1-128 pinned field v₂ = 200**; deployed Proth rows **v₂ = 92, 93, 95, 97** at 167–171 bits. `critical/nodes/integer_code_distance_cert/status_ruling.md:17-19` puts exactly those four rows inside this route's residue. They sit ~40–47 bits *below* VSTAR.

---

## Registered predictions vs outcomes

| | outcome |
|---|---|
| **V1** conditional-badness independence | **CONFIRMED** twice — h = 8 exhaustive (flat, all CIs contain the pooled value) and h = 64 with 14.7 M incidences (χ² = 3.75/8 df, slope 0.3σ) |
| **V2** MAXV2BAD8 ≥ 12, specifically 12289 bad | **CONFIRMED** exactly. Low-confidence (~7 %) sub-prediction that 65537 is bad: **did not land** (65537 is not bad) |
| **V3** geometric ladder, no bend | **CONFIRMED** to v₂ = 26, ratio 0.500; constant corrected (below) |
| **V4** the v₂ = 7 excess is a prime-count artefact | **PARTLY WRONG** — it is LAW 2 (a theorem) plus an acceptance-rule artefact |
| **V5** MAXV2HIT ∈ [28, 33] | **MISSED LOW: 26.** The law was right (7 + log₂(K·hits) = 26.9); my *coverage* forecast was wrong |
| **V6** CSTAR ∈ [125, 150] | **CONFIRMED**: 132.0 / 134.1 |

## Self-corrections

1. **My registered structural fact R0 was FALSE.** "Every odd prime factor of a box norm is ≡ 1 mod N′" fails: 18 of the 554 odd prime divisors at h = 8 are not (3, 5, 7, 23, 31, …). Repaired: e_p is a multiple of the residue degree f_p and p^{f_p} ≡ 1 mod N′ — which still yields NORMLAW, and restricting to f = 1 gives exactly the 536 of the round-22 ground truth. Verified explicitly.
2. **My registered GATE was dead on arrival.** Pre-filtering on v₂(Norm−1) ≥ 8 finds nothing in FAM-B because LAW 2 pins it at 7. Caught before use; the registered *ungated* control stream became the main ladder, and I replaced the gate mid-run with the cofactor-congruence rung test (a strictly better instrument, derived from the same law). Deviation from R2, recorded.
3. **K corrected twice**: registered 0.64 → measured pooled 0.736 → re-interpreted as an artefact; the population constant is 1.00.
4. **V5 missed low** — 12 shards on 14 logical cores ran at ~⅓ the single-shard benchmark, and half the budget went to the rung instrument.
5. The "OUTSIDE" flags at v ≥ 13 in the h = 8 binomial table are a normal-approximation artefact at zero counts (10 primes, 1.1 expected bad, 0 seen, P = 0.33) — **not** evidence of suppression.
6. ~50 minutes lost to a process-management error when switching instruments (the first `pkill` left driver subshells respawning shards).

## What none of this settles

The hunt covers 2⁻¹²⁴ of the box — silence bounds only the sampled region. The count is a heuristic expectation, calibrated at h = 8 but extrapolated across the R/λ₁ = 1 threshold (2.46 at the toy vs 0.551 at the prize cell), so it is not a proof. LAW 2 is proved for w = 1 + 2v (hence nodd = 1); the general-w formula for v₂(Norm−1) is a **named open gap**. Local surjectivity is about O_K^* in the completion; that the finite box realises every 2-adic class is measured only to depth 2¹⁷ — a second **named gap**. No result here shows a v₂ ≥ 41 witness can be *exhibited*, only that ~2⁹⁸ are predicted to exist.

## Artifacts (all draft-only, in my own dir; no dag/node/tool edits, no git)

`/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260809/large_v2_hunt/` — `PREREG.md` (registrations at 65–225), `d1_h8.py`, `d1b_calib.py`, `d1c_test.py`, `d2_split.py`, `d3_law.py`, `d3_thm.py`, `d3_surj.py`, `d3_cof.py`, `d3_tension.py`, `collide.py`, `bench.py`, `lad.py`, `turbo.py`, `drive.sh`, `drive2.sh`, `analyze.py`, `pick.py`, **`repro_v2_r25.py`** (standalone, PASS), `state/*.json` checkpoints, `logs/`.
