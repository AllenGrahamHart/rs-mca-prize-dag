# Pilot report: P-B |Gamma| exposure (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored). Coordinator verification and adopted posture:
FABLE_AUDIT.md alongside. REPORT ONLY — all adjudications with the
coordinator/maintainer.

---

# P-B |Gamma| EXPOSURE

## HEADLINE

1. **The standing finding's premise is refuted for exactly the pencils that matter.** FM3's official-scale extrapolation (Gamma_hi empty, so Gamma_lo = Gamma) is a statement about *random* supports and is **correct for the random supply**. It is **false for every split-fibre pencil**: a proved+measured **self-collision identity** — the pencil's exact-A witness set is exactly {S_J : J in C(F-g, a)} with |S_J ^ S_J'| = g + m|J^J'| — makes adjacent label sets meet in A - m, and the split-fibre range m <= h forces A - m >= K. **Every planted slope is high-core and contributes ZERO to Gamma_lo, at every q.** Measured at 4 shapes x 25 primes (100 points): |Gamma_lo| = 0 exactly wherever the random supply is 0 (= 1 exactly where it is 1). P-B's obligation is |Gamma_lo| <= 8n^3, and the split-fibre family (kill line K1) **cannot** attack it.

2. **The residual, construction-free exposure is real and confined to ONE row.** With the planted part discharged, |Gamma_lo| = random live slopes = min(q, C(n,A)/q^{h-1}). The exact criterion for a row to admit an over-budget q is **C(n,A) > (8n^3)^h . 2^{128(h-1)}**. **RowC 1/4 satisfies it by +156.45 bits; no other row does.** Exposed window q in [2^192.29, 2^200.11) — 7.82 binary orders wide, densely populated by primes == 1 mod 1024 — inside which the row meets its own MCA budget B* = floor(q/2^128) while a generic pencil has up to 2^64.29 = 2.63e9 x 8n^3 live low-core slopes. **RowC 1/16 misses exposure by 2.31 bits** and consumes **58.6% of the whole 8n^3 budget** at its worst admissible q — the sharpest near-miss in the ledger.

3. **The exposure is decided by an unresolved q-scope ambiguity (F3 fires).** Under the banked *envelope* pins (RowC q >= 2^250) every row is supply-safe with >= 49 bits of slack. Under `official_row_primes_pinning` (**PROVED**, verdict `no_fixed_official_primes`, requiring certificates *"uniform over the complete admissible family"*), q ~ 2^193 is admissible at RowC 1/4 and the window is live.

## 1. THE q-PIN LEDGER

Row constants (banked; sources: `dyadic_profile_evaluation/proof.md:79-86`, `audit_consumption_replay_20260710.py:98`, `verify_brief4_lowcore_program_arithmetic.py:64-69`):

| row | n | k | A | h | 8n^3 |
|---|---|---|---|---|---|
| RowC 1/4 | 2^10 | 2^8 | 261 | 5 | 2^33 |
| RowC 1/8 | 2^10 | 2^7 | 133 | 5 | 2^33 |
| RowC 1/16 | 2^10 | 2^6 | 67 | 3 | 2^33 |
| prize 1/4 | 2^41 | 2^39 | 558,345,748,481 | 2^33+1 | 2^126 |
| prize 1/8 | 2^41 | 2^38 | 283,467,841,537 | 2^33+1 | 2^126 |
| prize 1/16 | 2^41 | 2^37 | 141,733,920,769 | 2^32+1 | 2^126 |

**TWO banked q-specifications, not one:**

- **(P1) Universal admissibility** — `background/nodes/official_row_primes_pinning/statement.md:3,8-19` (PROVED; "no hidden finite list of official row primes"; certificates must be family-uniform or exhibit-scoped) + `official_row_primes_reframe.json` (`no_fixed_official_primes`) + `tools/prize_row_descriptor.py:16-18,74-81` (q < 2^256, k <= 2^40, n | q-1). **q is a RANGE; no pinned prime at any row.**
- **(P2) Clean-anchor ENVELOPE pins** — RowC B* = 2^122 (`tangent_clean_anchor_route_classification/statement.md:39` + three verify.py constants), induced interval I_C = [2^250, 2^250 + 2^128 - 1] (`e1_pair_feasible_prime_field_reduction/proof.md:23`; corroborated `identity_prefix_clean_anchor_route_classification/statement.md:52-53`); prize B* = 317494674775468773183020924238786383963, q ~ 2^255.9 (`proof.md:41-42`).

**Neither reading gives any row q_max < 8n^3** (q >= 2^250 >> 2^33 at RowC; ~2^255.9 >> 2^126 at prize). The coordinator's "safe by field size" conjecture is NOT realized at any row; |Gamma| <= q-1 is never binding. **Safety, where it holds, comes from witness supply.**

**Thresholds** (C = C(n,A); mean total witnesses C/q^{h-1}; mean |W_z| = C/q^h): L1 soundness floor q^h >= C.2^128; L2 no-competition floor q^h >= C; L3 P-B supply floor q^{h-1} >= C/8n^3. Exposed window = [L1, L3), non-empty iff **C(n,A) > (8n^3)^h . 2^{128(h-1)}** (exact integers at RowC; rigorous entropy bracket at prize, gap ~4e11 bits vs 41-bit bracket width).

| row | log2 C | margin vs criterion | lg L1 | lg L3 | window |
|---|---|---|---|---|---|
| **RowC 1/4** | **833.452** | **+156.452** | 192.290 | 200.113 | **[2^192.29, 2^200.11)** |
| RowC 1/8 | 565.734 | -111.266 | 138.747 | 133.183 | EMPTY (5.56 bits) |
| RowC 1/16 | 352.687 | **-2.313** | 160.229 | 159.844 | EMPTY (**0.386 bits**) |
| prize 1/4 | 1.7975e12 | -3.843e11 | 209.257 | — | EMPTY |
| prize 1/8 | 1.2192e12 | -9.626e11 | — | — | EMPTY |
| prize 1/16 | 7.5839e11 | -3.325e11 | — | — | EMPTY |

Smallest P-B-style constant valid at EVERY admissible q = 2^{(log2 C - 128(h-1))/h}: RowC 1/4 **2^64.290 = 2.63e9 x 8n^3 (EXPOSED by 31.29 bits)**; RowC 1/8 fits (22.25 bits slack); RowC 1/16 fits (**0.77 bits**); prize rows fit (44.7 / 112.1 / 77.4 bits). Supply at the P2 pin: 2^-167 .. 2^-9.7e11 — at the pinned q a generic pair has NO live slope; every live slope at official scale is planted. Cross-check: B*/8n^3 = 3.7321 at prize rows = "29.86 n^3", independently reproducing `xr_target_budget_audit/proof.md:13`.

## 2. THE |Gamma| LAW — PRE-REGISTERED, MEASURED, CORRECTED

**Instrument**: `census.py` re-implements the banked MITM identity with dict accumulators (q pushed to 2^31); **cross-validates bit-exactly against all 12 banked k1_Q*.json** (totals, live slopes, full per-slope histograms): CROSSCHECK PASS. Construction/checks imported read-only from the banked pilots; the two O(q) strip loops replaced by exact O(n)/O(1) equivalents, asserted verdict-identical below q = 20000. 4,200 banked checks replayed, all PASS.

**Ladder**: 4 shapes x 25 primes == 1 mod 32, q in [193, 2147483713], spanning mean |W_z| from 1.3e4 down to 4e-11 — through and far past the official low-density regime (the gap K1 caveat 3 and FM3 caveat 4 both flagged). Shapes: S1 (32,2,8,2,10), S2 (32,2,8,3,11), S3 (32,2,16,2,18), S4 (32,4,8,5,13 — the official m=4,h=5 shape).

**Frozen predictions scored** (PREDICTIONS.json frozen before any run): C1 naive witness law FAILS 10/32 (worst 26.79x — ignores the planted family); C2 PASS 100/100; C3 Poisson random law PASS 19/19 where applicable; C4 FAILS 4/4 (converges to a different, larger, exactly-predictable number); **C5a FAILS 0/79 — the HEADLINE: retention never rises at low density (0.0000-0.2286); the pre-registered expectation was wrong, in P-B's favour**; C5b PASS 7/8 (reproduces K1).

**Corrected law (validated 0.47-1.30 over all 100 points):**

    witnesses(q) = C(F-g, a) + C(n,A)/q^{h-1}        (F = n/m)
    |Gamma|(q)   = N_split(F,g,a) + q(1 - e^{-C/q^h})   capped by q
    |Gamma_lo|(q) = (random live slopes) ONLY

N_split closed-form and exact (char-0 slope count via the Z-basis of Z[zeta_F]): witnesses C(14,4)=1001, C(15,5)=3003, C(14,8)=3003, C(7,3)=35 — measured 1001/3003/3003/35; slopes 706/1611/1394/27 — measured 706/1611/1394/27. **4/4 exact on both.**

**The mechanism — (SF-SELFCOLLISION), the load-bearing result:** |S_J ^ S_J'| = g + m|J^J'| (verified pair-by-pair, 7.0M pairs, zero deviations). Max over J != J' is g + m(a-1) = A - m, and m <= h (`pb_split_fibre_pilot.py:233`) forces A - m >= K. Measured max pairwise cores 8/9/16/9 vs K = 8/8/16/8 — equal to A-m and >= K at every shape. Consequence measured on S1: Gamma_lo is EXACTLY the random part (0 where random supply 0; 1 where it is 1). At S4 — the official shape — intended_is_first_match = 6/6 at EVERY q: the planted witnesses ARE the normative first matches, and Gamma_lo is still 0. First-match minimality is moot in the no-competition regime.

**Is split-fibre |Gamma|-optimal?** Yes for |Gamma| (plants C(F-g,a) witnesses q-independently), **worthless for |Gamma_lo|**. The audit's M = 129,948,699,009 is a Sidon SUB-family (needed for the energy-producer refutation), ~2^152 smaller than the pencil's true slope count; neither the full family nor the Sidon sub-family can enter Gamma_lo — Sidon-ness does not remove adjacent pairs, and adjacency alone is fatal.

## 3. THE SINGLE-FIELD REALIZATION QUESTION

**Availability**: fibre width unique per row (m | n, m <= h < 2m): m = 4,4,2 (RowC), 2^33,2^33,2^32 (prize); optimal (F,a,g=1) IDENTICAL at RowC and prize: (256,65), (256,33), (512,33) — matching the tree's own remark (`qfloor_clean_anchor_norm_threshold_route_cut/statement.md:20`).

| row | split-fibre witnesses | distinct char-0 slopes | vs 8n^3 | vs B* | max core | Gamma_lo |
|---|---|---|---|---|---|---|
| RowC 1/4 | C(255,65) = 2^204 | **2^189** | > 2^33 | > 2^122 | 257 >= 256 | **0** |
| RowC 1/8 | 2^137 | 2^134 | > | > | 129 >= 128 | **0** |
| RowC 1/16 | 2^172 | 2^171 | > | > | 65 >= 64 | **0** |
| prize rows | 2^204 / 2^137 / 2^172 | 2^189 / 2^134 / 2^171 | > 2^126 | > 2^127 | >= K | **0** |

**Single-field realizability**: collisions of z_J mod p are norm-divisibility events in Z[zeta_F] with coefficients in {-2..2}; each pair kills <= 4-10 primes above 2^250 while the RowC window holds ~2^111 admissible primes (PNT in AP). **A family of ~2^55 distinct-slope members is realizable in ONE admissible prime, rigorously — 22 binary orders above 8n^3.** The full 2^189 needs only a standard random-map heuristic (2^189 << sqrt(2^250), no birthday obstruction).

**Answers**: for **|Gamma|** (all bad slopes): YES at every row and every admissible q — but this is a ROW-SOUNDNESS item, not P-B: the tree already records the gap (`xr_agreement_raise_quotient_safe_sum_fence/statement.md:31-41`, "one active summand already exceeds B*", needing a "sharper distinct-slope image/coalescing theorem"); the pilot's contribution is the matching LOWER bound (2^189 char-0 / 2^55 rigorous single-field). Belongs to the maintainer. For **|Gamma_lo|** (P-B's obligation): NO from any split-fibre construction at any q (self-collision); **YES from the plain random supply at RowC 1/4 only**, q in [2^192.29, 2^200.11).

**The named exposure**: RowC 1/4, q in [L1, L3) with L1 = 7676891232383518777053470249149749493066190349264182433950 (2^192.29), L3 = 1737898502031414277584835791914552418242270719663671405377577 (2^200.11) — the only place in the six-row ledger where a globally generic pencil's low-core live-slope count exceeds 8n^3. At the window floor: count 2^64.29 while B* = q/2^128 = 2^64.29 exactly met; |W_z| = 2^-127, every live slope carries exactly one witness — first-match minimality cannot help. A P-B-saving theorem must beat the first moment by 31 bits at this row.

**The candidate discharge argument (PB-SUPPLY), statement-shaped for Pro**: hypotheses (H1) admissibility; (H2) soundness floor q^h >= C.2^128; (H3) supply floor q^{h-1} >= C/8n^3; (H4) no-concentration: low-core live slopes <= C/q^{h-1}. Then |Gamma_lo| <= 8n^3. Status: (H1) = the banked admissibility scope; (H2) implied by any sane "sufficiently large"; (H3) NOT implied by (H2) at RowC 1/4 (the 7.82-bit gap) but implied at the other five (RowC 1/16 by 0.386 bits) and at all six under the envelope pin; **(H4) is the whole content** — false for |Gamma| (split-fibre), TRUE for |Gamma_lo| on the entire split-fibre family via (SF-SELFCOLLISION), now a proved elementary lemma. The discharge reduces P-B to (H4) restricted to non-split-fibre concentration + the (H3) decision at RowC 1/4; the adversarial surface shrinks from "any construction" to "any construction whose planted family is a distance->=4 constant-weight code" — which the split-fibre recipe provably cannot produce (m <= h is exactly the obstruction).

## 4. FALSIFIER VERDICTS

**F1 — PARTIAL FIRE, does NOT reach the target.** |Gamma| = 2^189 >> 8n^3 by construction at every row — but 0 in Gamma_lo (measured at 100 points, explained by the lemma). Kill line K1 is **closed for this construction class, for a structural reason (m <= h), not a selector reason**. What fires is the construction-free exposure at RowC 1/4 only, live iff the (P1) scope governs.
**F2 — FIRES.** The naive law fails (C1 10/32, C4 4/4); corrected law validated; the exposure analysis IS run on the corrected law. C5a's 0/79 failure is in P-B's favour.
**F3 — FIRES, precisely.** (P1) vs (P2) answer the exposure question oppositely at RowC 1/4. Not contradictory (P2 is inside P1's family) but the governing scope for P-B is a coordinator/maintainer call. `official_row_primes_pinning` is itself PROVED and explicitly requires family-uniform certificates absent a transport theorem — if P-B is family-uniform, (P1) applies and the window is real.

## 5. FILE INVENTORY

`qpin_ledger.py` -> QPIN_LEDGER.{json,log} . `census.py` (bit-exact crosscheck vs all 12 banked k1_Q*.json) . `predict.py` -> PREDICTIONS.json (frozen) . `measure.py` -> MEASURE_S{1,2,3,4}.json (4x25 ladder; FastCase asserted verdict-identical to the banked Case below q=20000; 4,200 banked checks PASS) . `construction.py` -> CONSTRUCTION.{json,log} (self-collision verified pair-by-pair; N_split 4/4; official-row evaluation; single-field prime-counting bound) . `score.py` -> SCORE.json. Nothing outside the directory; imports read-only; no commits; nothing m2-related; all under ramguard.

## 6. HONEST CAVEATS

1. The model is the lane's monic degree-A pencil; if P-B's (u,v) are arbitrary words the first-moment law is unchanged but the split-fibre analysis is not restated.
2. Toy-scale contamination: at n=32 random supports also collide at core >= K; at official scale that correction vanishes (Pi ~ 2^-693 at RowC 1/4, q = 2^192) — an FM3-type extrapolation, in the UNFAVOURABLE direction for P-B.
3. N_split is a char-0 count; single-field rigorous only to ~2^55; 2^189 rests on a random-map heuristic. Matters for row-soundness, not for the Gamma_lo conclusion (0 regardless).
4. **RowC 1/16 is 2.31 bits from exposure and consumes 58.6% of the budget at its worst admissible q. Treat its safety as FRAGILE** — any few-bit correction to A, h, the epsilon convention, or the floor modelling flips it.
5. The (H2) soundness floor is the pilot's operationalization of "sufficiently large"; if the tree pins a different lower bound, L1 moves (window closes entirely only if the floor exceeds 2^200.11).
6. (SF-SELFCOLLISION) is proved for the split-fibre recipe only; whether another globally generic pencil can plant a distance->=4 constant-weight family above 8n^3 is exactly the residual (H4).
7. Nothing here is proved about P-B; the 156-bit and 2.31-bit margins are exact integer facts; the exposure VERDICT depends on the F3 scope call.
