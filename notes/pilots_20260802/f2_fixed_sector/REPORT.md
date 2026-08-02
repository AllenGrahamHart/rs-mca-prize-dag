# Pilot report: F2 fixed sector vs the parity-pure class (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(entities restored). Coordinator verification and posture:
FABLE_AUDIT.md alongside.

---

# F2 FIXED SECTOR vs THE PARITY-PURE CLASS — the obligation is DISCHARGED NEGATIVELY

**HEADLINE (F1 fires, five independent ways).** The fixed sector **does not absorb the parity-pure class, and cannot**. One line: **-1 in mu_{2^24}**, so the fixed sector is ITSELF antipodally closed, and a parity-pure frequency degenerates it exactly as it degenerates every rung. Routing K1 to the fixed sector routes it to a sector that is IN class K1. The proposed case split's second branch has no argument behind it: the "already-PROVED fixed-sector argument" covers a sector that is (i) sign-dead at these frequencies, (ii) capped at the identical log2 p ceiling, (iii) reachable from a rung only through a scalar offset that provably cannot break that ceiling (the base sweep over all 2p offsets: ratio <= 1.000 always), (iv) 2^-16 of the group, and (v) on the trace-zero sub-class, outside the k=1 theorem's own hypotheses (Lemma A's non-vacuity k != 0 fails outright). Digest: F2_FIXED_SECTOR_ABSORPTION_ALL_PASS (V1-V11).

## 1. Reconstruction (cited)

f2_k1_contraction_theorem (PROVED): prime-field rows, n >= 512 and n >= 3 sqrt(p); every p-FREE moment condition; analytic input = the monomial subgroup Gauss sum (Lemma A, needs k != 0); currency = Halasz/CMMM giving rho <= 3.71/p, i.e. **log2 p ~ 31 bits per condition — nothing more**; fixed sector mu_{2^24} in the analytic regime; **the joint/ladder version is NOT proved** (campaign log #67: "FIBER-conditional contraction does not transfer automatically"; the frequency-space struct ledger is the remaining content; consumed by f2_conditional_close's conditional bucket).

## 2. Absorption verdicts

**K1**: the census factorises T(c) = F(c) . prod M_j(c). NEW exact identity: **F(c) = prod over fixed pairs of (2 + zeta^s + zeta^-s)** — totally positive (verified 470/470 K1 frequencies, four primes) — so **eps_c = +1 on the whole K1 class at every sector**: no signed content anywhere. Danger (a) answered twice: the fixed-sector fold is a COARSENING of every rung fold (K1 at rung j ==> K1 at every lower rung AND the fixed sector — proved + measured, 100% of parity-pure frequencies give the fixed sector all-Delta-even, flat = 0 exactly); and on the trace-zero line the fixed-sector character is identically zero — F(c) = 2^{n_0} exactly, contraction 0.000 bits in both currencies, the k=1 theorem vacuous there. Danger (b): the fixed sector's own 1/p ceiling ladder saturates at exactly log2 p (max deviation 1.6e-5 bits, incl. p = 12289 — the k=1 theorem's own empirical stage); the base-channel sweep over ALL 2p offsets never exceeds the ceiling; head-to-head at equal size, no structural advantage (ratio 0.63-1.27).

**K2 is not an independent class**: exact pullback identity (111/111) — [rung-j factor at g(x^{2^d})] = [rung-(j-d) factor at g]^{2^d} on BOTH sectors; the fixed sector is coset-trivial (total death) at K2, not a refuge. K2 = a descent obligation with ramification factor 2^d; the terminal step can lose antipodal structure and produce a genuine sign (1/40 cases at p=641) — must be named.

**Fourth kill — the dual seam**: K1 frequencies annihilate the symmetric (pair-union) sub-census (odd power sums vanish on pair-union blocks, 60/60) — the "Frobenius-fixed AND symmetric sectors PROVED chain" bucket carries no K1 cancellation either. The block-side and frequency-side decompositions are exact duals; the two proved buckets cover complementary things and NEITHER covers K1.

## 3. Budget arithmetic (exact, official row)

Total 1/43 budget over 16 rungs = 1.278e10 bits; K1 delivers 16 x log2 p = 495.8 bits; K2 delivers 0; the ENTIRE fixed sector's most generous capacity = n_0 = 1.678e7 bits. **Shortfall = 762.03x the whole fixed sector** (10922x at 1/3); from rung 8 a single rung's deficit exceeds the whole fixed sector. In the lane's carry currency the fixed capacity is 0 (C7). Annealed reading: per-pair constant exactly 2 (parity-pure) vs (4/pi)^2 generic — the class's first-moment mass is exactly the alignment bound's RHS scale: dead heat, zero structural margin.

## 4. Composition theorem shape + the replacement obligation

**Theorem A (per-sector parity trichotomy, proved, elementary)**: every sector is antipodally closed; per sector G / K1 / K2 as above; coarsening one-directional (downward). **Theorem B (no absorption, proved)**: any composition of the form "generic -> slice theorem; parity-pure -> fixed sector" is FALSE, independently of PP5.0. Seams for the draft: per-sector trichotomy composes by product/convolution (= PP5.0, unfrozen); coarsening one-way; the pullback terminal sign; symmetric-blocks-perp-odd-frequencies duality (S4).

**Replacement obligation (constructive)**: K1 must be paid by MASS, not cancellation: (O1) first-moment target E_{c in K1}[exp S_c] <= 2^{n/2 + o(n)} (2^{n/2} = the exact independent-value scale); (O2) the same at fixed b (the Hamming-slice fence forbids (O1) alone); (O3) PP5.0 must carry the pullback ramification 2^d. A moment computation over a LINEAR SUBSPACE of frequency space — the campaign's own struct-ledger shape.

**DAG impact: none negative.** The parity-pure class already lives in f2_conditional_close's CONDITIONAL bucket; the amendment's proposed move to a PROVED bucket cannot happen; one escape closed, replaced by a sharper obligation.

## 5. Prediction vs measurement

Frozen PREREG, 9 predictions: P2/P3/P4/P5/P7/P8/P9 confirmed (three exactly). **P1 refuted as stated (self-catch)** — corrected to the stronger totally-positive normal form, rate 1.000. P6 partial: per-element constants exact; the product-level 2^{n/2} statement is banked as a labelled first-moment heuristic.

## 6. Falsifier verdicts

**F1 FIRES maximally** (absorbed by nothing banked; exact hypothesis failures named: Lemma A non-vacuity on the trace-zero class; per-condition/fixed-functional scope with the joint ladder open). **F2 FIRES** (762x; single-rung from rung 8; 0 bits in carry currency). F3 does not fire.

## 7. Files

PREREG.json (frozen) . core.py . run_composition.py . ladder.py . official_budget.py . verify.py (V1-V11 ALL PASS). results/: C1-C7 JSONs + prediction-vs-measurement + verify log. No commits; nothing outside the directory; deployed-windows imported read-only (V10 cross-check reproduces its rung-1 window exactly); nothing m2-related.

## 8. Honest caveats

- The log2 p ceiling statement is in the carry/slice currency; in the plain subset currency parity-pure terms show Theta(n)-scale magnitude cancellation at small scale (~0.66 bits/element at n=64) — the modulus field, which satellite 18 already prices as unable to pay the frequency count. The sign-field kill (eps = +1) is currency-independent.
- Exact data: V_b/ladder to m <= 128, p <= 12289; Z[zeta_p] to n <= 256, p <= 641. Official scale enters via pure arithmetic (-1 in mu_{2^24}, sector sizes, ratios) + the one-line coarsening law.
- Coarsening proved by derivation, measured one level (a two-rung numerical instance needs F_{p^4}, not built).
- P6 product-level = first-moment heuristic; the "dead heat" conclusion inherits that status.
- The budget table rides the deployed pilot's window reconstruction (2x ambiguity flagged there); the RATIOS are robust (shortfall halves or doubles only).
- Nothing mintable; no status flips; F2A.1 and PP5.0 unchanged.
