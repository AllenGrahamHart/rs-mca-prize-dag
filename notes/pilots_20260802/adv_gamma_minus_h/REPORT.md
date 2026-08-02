# Pilot report: adversarial attack on Gamma-in--H (Opus 5, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(entities restored). Coordinator verification and posture:
FABLE_AUDIT.md alongside. 383 machine checks, 0 verification failures,
1 pre-registered prediction falsified (recorded).

---

# ADVERSARIAL VERDICT ON Gamma subset -H: **SPLIT — proved at j=1, REFUTED at j>=2**

- **j = 1: K3.** Gamma subset -H is now a THEOREM (two lines given the banked locator normal form), unconditional in n, k, w, q, beta, char. The band-adjudication caveat 1 CLOSES. **Bonus: the MC shift pencil's tangent gate is proved unconditionally** — band-adjudication caveat 2 and list_bound_transfer's Q2 close too, with no q-threshold.
- **j >= 2: K2.** FALSE as stated: 18 gate-intact certified counterexamples (headline |Gamma| = 2.20n, 24 slopes outside -H^j, incl. extension fields F_121/F_361 and w < M / odd-n corners). The excess is governed by X = C(n,A)/q^w — numerically IDENTICAL (to two decimals, all three prize rows) to the gate-admissibility threshold the construction already assumes; log2 X at q = 2^250 is -3.5e11 to -9.3e11. **A lemma amendment, not a re-pricing.**
- **K1 (superlinear extras): NOT FIRED. The ratified fold-in stands.**

## 1. THEOREM X (classification frame)

Exact-A codewords of a mixed member correspond (banked Lemma 1) to monic M | Omega with window conditions LINEAR in z: alpha_i + z.beta_i = 0. At j = 1, with N := (X+z)M, i.e. S := T u {-z} (one point freed from H): e_1(S) = ... = e_{w-1}(S) = 0, e_{r-1}(S) = 0, prod(S) = gamma — **MC-1's own system with one free point plus one extra equation** (coset unions satisfy it for free). Verified against theory-free brute force (400 random shapes + full sweeps, 0 mismatches).

## 2. THEOREM Y (j = 1) — the caveat closes

prod(S) = gamma and prod(T) in x0^{r-1} mu_n force **-z in gamma.x0^{-(r-1)}.mu_n — one coset of mu_n**. Hence |Gamma| <= n UNCONDITIONALLY, and the coset = -H exactly under realizability (gamma^n = beta^r, which holds whenever the MC family is non-empty). Proved corollaries: the mixed-member ceiling (delta >= 2 forces m_0 = 0, impossible), the (0:1) ceiling, the pencil max = exactly A (the tangent gate as a THEOREM at every q), the automatic exactness guard, and joint_max <= A-1 from MC-2 alone. Machine-checked on every solution of every j=1 fixture (1374 solutions across 7 fixtures incl. F_49/F_121/F_169, beta != 1, super-critical X up to 358). **De-realized control**: twisting c off the product coset moves Gamma to a DIFFERENT coset, still |Gamma| <= n — "subset -H" is exactly realizability; "|Gamma| <= n" is unconditional.

## 3. The j >= 2 refutation

For every j: z = +-1/e_j(T^{-1}) (checked on 100% of solutions). At j = 1 this IS the product condition; at j >= 2 it is a sum of j-fold products of inverses — NOT coset-confined. Certified counterexamples (theory-free Lagrange re-derivation of all codeword pairs): control (j=1, n=20, q=41): |Gamma| = 20 = n, 0 outside; headline (j=3, q=41): |Gamma| = 40 = 2n, 20 outside; (j=3, q=101): 44 = 2.2n, 24 outside — all with gate intact, joint_max = A-1, genuine MC pencils. 18 in all across j in {2..5}, four beta exponents, prime + extension fields. Nuance pinned: at n=21 |Gamma| = n but 7 slopes sit outside -H^j — **the cardinality bound is more robust than the set claim; state separately**.

## 4. Pricing — the ratified fold-in survives

The excess index X = C(n,A)/q^w tracks extras within ~4x (X < 1 -> zero extras at every fixture; reliable escapes from X ~ 10). Critical log2 q = 209.26/141.93/176.58 at the prize rows — **identical to the published gate-admissibility thresholds: caveats 1 and 2 were always ONE hypothesis, not two.** At q = 2^250, log2 X = -3.5e11/-9.3e11/-3.1e11. Occupancy pricing: proved n/2 vs required 2^86 — margin -46 bits (a TOTAL confinement failure would have cost +163 bits, which is why the attack was worth running); Gamma_casc at -85.7 bits vs 13n^3. **The N_{h-1} <= n/2 verdict and the x1.3403/1.1480/1.0689 B_tan overflow stand unchanged.** Recommended amendment: state the confinement as the j=1 coset theorem + realizability, with j >= 2 inheriting from the already-assumed gate inequality.

## 5. Collateral findings for the band adjudication

1. Non-MC exact-A rays exist in its own fixtures (78 vs 70; 1016 vs 688) — invisible to |Gamma| (Theorem Y confines them) but they COMPETE in first-match selection, so measured selected counts are LOWER than the MC prediction (safe direction; definitions item 8 should say so explicitly).
2. The q=17, n=16 fixture is degenerate (-H = F_17^*, the claim vacuous there): effective banked coverage was 5 fixtures, not 6.

## 6. Honest caveats

1. Proof reach: THEOREM Y + ceilings proved for ALL parameters at j=1 (official rows verbatim); at j >= 2 nothing is proved — the X < 1 model is a calibrated first moment over a deterministic instance; a hard unconditional |Gamma| bound at j >= 2 is open.
2. Pre-registered D2 FAILED (predicted escapes from X >= 2; zero at X = 4.76) — weakens the calibration constant, not the refutation (18 explicit instances).
3. Round-1's index explanation was falsified and honestly left in the docstring; the falsification forced the structural analysis.
4. Toy scale n <= 32; six-row arithmetic exact except Stirling on log2 C (error < 25 bits vs ~1e12).
5. w = M >= 4 super-critical unreachable by search (covered by identity + argument, not counterexample).
6. gcd(j,n) > 1 classes not attempted beyond confirming BP(2)'s gate break.
7. Novelty narrow: the (X+z) factorisation, THEOREM Y, the ceilings, the z = +-1/e_j identity, the refutation, and the caveat-unification; the frame and coset mechanism are banked.

Files: advlib.py, t1-t6 + checkpoints (6 JSONs). 383 checks; t4 (50) and t6 (10, CERTIFIED) coordinator-replayed. Nothing outside the directory; no commits; nothing m2-related.
