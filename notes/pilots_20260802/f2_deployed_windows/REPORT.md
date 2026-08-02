# Pilot report: F2 deployed windows (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored; long tables preserved). Coordinator
verification and adopted posture: FABLE_AUDIT.md alongside.

---

# F2 DEPLOYED WINDOWS — the lane's new heart, answered

**HEADLINE (F1 fires, maximally and structurally).** The deployed windows of the actual F2 tower are **not merely bad, they are the worst class — at every rung, at every frequency of the banked model — and no window-selection step can repair it, because the deployed window is not a choice at all.** The obstruction is exactly one mode (k = p), it is convention-invariant, weight-general and rung-uniform, and it caps the b-resolved cancellation at log2 p ~ 31 bits per rung against a budget of ~1.95e5 bits at rung 1 (a **6293x shortfall**, growing to 2^18 x at rung 16). The escape exists but it is in **frequency space, not coordinate space**, and it is a *case split*, not a selection: the (H-flat)-violating frequencies are exactly two parity-pure linear subspaces, and on them the moving sector carries **no signed content at all**, so they must be routed to the already-PROVED fixed-sector argument rather than to the slice theorem.

Digest: `F2_DEPLOYED_WINDOWS_VALIDATION_ALL_PASS` (A1-A8, replayable under ramguard local).

## 1. Window reconstruction

Tower (citations in the pilot's table): official prime KoalaBear-shaped, p-1 = 2^24 . 127, e = v_2(p-1) = 24 (`notes/f2_campaign/F2_CAMPAIGN_LOG.md:2036`); n a 2-power ~2^40, ambient N = 2^41; fixed sector mu_{2^24} in the analytic regime (PROVED, campaign log entry #75, :1394-1410); rung j: n_j = 2^{24+j}, q_j = p^{2^j}, j = 1..16, descent = the quadratic extension (entry #76, :1412-1430); ord_{2^40}(p) = 2^16 exactly (:2158-2160); t ~ 7e10 conditions.

**The deployed window is uniquely determined — no coordinate freedom.** Rung j processes the complete set of genuine Frobenius pairs of mu_{n_j}: m_j = 2^{22+j} pairs (rung 1: 2^23). The banked pilots' window constructors all carve sub-windows of the FULL group mu_{p^2-1}, which no rung processes.

**Genuine ambiguities flagged**: per-rung window not written down anywhere (nested vs new-part reading — budgets reported under both); per-rung frequency set absent (c defined once, globally); "rung" overloaded three ways; q = p^k not officially pinned; orientation labelling is a modelling convention (see section 6/E9).

## 2. THE ANTIPODAL LAW (the finding) — exact, rung-uniform

**Lemma.** p odd, e = v_2(p-1) >= 2, n_j = 2^{e+j}, q_j = p^{2^j}. Then (i) v_2(q_j - 1) = e + j [LTE]; (ii) mu_{n_j} ^ F_{q_{j-1}} = mu_{n_{j-1}}; (iii) **every y of order exactly n_j satisfies y^{q_{j-1}} = -y** (q_{j-1} - 1 = 2^{e+j-1}.odd and y^{2^{e+j-1}} = -1).

**Consequence.** The rung-j Frobenius pairs are ANTIPODAL {y, -y}. For the linear character x -> psi(cx): s^- = Tr(-cy) = -s^+, hence Delta_i = 2 sigma_i^+ — **EVEN, for every i, every c, every rung**. Every deployed window is parity-homogeneous (beta_min = 0), mode k = p exactly slice-dead (|R_p| = 1, flat = 0), (H-flat)/(H-spread) fail identically. At rung 1 the genuine elements are exactly the trace-zero elements — the class F2A.5 rated a measure-zero accident is, at the deployed subgroup, THE ENTIRE WINDOW at 100% of frequencies.

**Verification**: A1 (LTE at the KoalaBear prime rungs 0..16 + 11 official-shaped primes, 0 violations); A1b (moving-level exponents 25..40 reproduced); A2 (508 genuine elements, all y^p = -y, Tr(y) = 0); A3 (all-Delta-even at EVERY frequency: exhaustive 1640/272/9312 c at p=41/17/97 + samples; max flat = 0.0 exactly).

**Not a proxy artefact (A5, exact Z[zeta_p], true weights)**: on an antipodal coordinate A_i(p) = B_i(p) exactly, so |e_b(p)| = E_b for every b; with hhat_p(p) = 2 (A6) the k=p mode deposits +-E_b/p into every slice. The 1/p floor is weight-general.

**The degeneracy law, censused**: n_ord/gcd(n_ord, p-1) == 2 <=> all Delta even at every c — 194 (p, n_ord) rows, 0 violations. The official rung-j subgroup satisfies the law at every j.

## 3. Flatness census

**Parity-defect certificate (new, exact):** for odd k, grouping Delta by residue mod p: max_{k odd} |R_k| <= D/n with D = sum_d |#even - #odd| per class. Corollary (A8): the FULL-group window has D = ((p-1)/2)^2 exactly, so **flat(full group) >= (p+1)/(2p) > 1/2** — a PROVED (H-flat) certificate, 6x the 1/43 threshold — but for a window the tower does NOT deploy. The deployed window: D = m, bound degenerates, flat = 0 exactly.

**The exact 1/p ceiling ladder** (exact-integer V_b, worst central-band slice): -log2 rho_b saturates at log2 p across the ENTIRE central band — to 4 decimals at m = 128 (p=257: 8.0054-8.0055 vs log2 p = 8.0056). eta = log2(p)/m -> 0: **the cancellation exponent is constant in m; the budget's linear term can never be earned**. Crossover m* = 43 log2 p = 1333 at official p; deployed m_1 = 2^23 — 6293x past it at rung 1.

**Frequency-support classification** (multi-condition character s = Tr(sum_l c_l x^l), f = f_even + f_odd by parity of l): K1 (f_even = 0 — THE PILOTS' MODEL) all Delta even, rho ~ 1/p; K2 (f_odd = 0) Delta = 0, rho = 1 exactly (total death); G (both parts) flat med 0.55-0.60, eta 0.14-0.31, 0 dead windows, 100% clear 1/43, never reach 1/3.

## 4. THE MECHANISM

**No upstream mechanism guarantees (H-flat) at deployed windows, and window selection is impossible in principle**: the coordinate set is the complete pair set (no choice), and "all Delta even" is inherited by every sub-window. What controls flatness is the FREQUENCY's parity support. Theorem candidates: **(T1) the antipodal descent lemma — proved** (with corollary -log2 rho_b <= log2 p + o(1), independent of m); **(T2) the parity-defect certificate — proved, exact** (mintable-shaped, but for the undeployed full-group window); (T3, open) generic-frequency flatness ~0.55-0.60 uniform in p and m — needs an incomplete-character-sum bound over the 2-Sylow coset half-system, not attempted.

**Corrected hypothesis shape for the theorem draft**: (H-flat*) — max over odd k != p of |R_k| bounded, PLUS an explicit exceptional-owner clause for k = p carrying its exactly-known +-E_b/p (Krawtchouk at n_o = 0). F2A.2 finding 7's "pre-registered exceptional owner: mode k=p on the trace-zero line" anticipated this — the finding here is that at deployed windows the exceptional owner is NOT exceptional, it is UNIVERSAL.

## 5. Scaling — per-rung budget table (official shape)

p ~ 2^31, m_j = 2^{22+j}: 1/43 budget grows 1.95e5 (rung 1) -> 6.39e9 bits (rung 16); the deployed K1 ceiling is 31 bits at every rung; shortfall 6.3e3x -> 2.1e8x (doubling per rung). All 16 deployed rungs together deliver 16 x 31 = 496 bits. Deployed flatness does not degrade — it is 0 everywhere; the MARGIN degrades. Generic-frequency flatness is stable (~0.59) in both p and m (m to 512, p to 18433). Startup deficit 15.5 -> 23 bits, irrelevant next to the ceiling. **1/3 is unreachable at deployed windows for any window size** (needs flat >= 0.924 at beta = 1/2; measured max 0.76).

## 6. The selection step and its exact cost

Selection is impossible in coordinate space; in FREQUENCY space the degenerate class is exactly {c : even-part trace-zero on the sector} — codim_j = min(m_j, t/2) F_p-conditions. Excluding it by population counting pays for itself ONLY from rung 13 up (at rung 1 it saves 0.025% of the allowance). **The constructive resolution**: in K1 the census term factors with a POSITIVE REAL moving-sector contribution (no signed content); in K2 the orientation is inert. The architecture needs a **frequency-space case split**, not window selection: generic frequencies -> the slice theorem (1/43 only); parity-pure frequencies -> the already-PROVED fixed-sector argument. **NEW UN-DISCHARGED OBLIGATION: nobody has checked the fixed sector mu_{2^24} covers the parity-pure class.**

## 7. Falsifier verdicts

- **F1 — FIRES maximally**: every deployed window at every rung is parity-homogeneous with flat = 0 exactly; unavoidable within the banked tower definition; not repairable by any window selection (coordinate-uniform degeneracy). Minimal repair = (H-flat*) with k = p as a named universal owner + the frequency-space case split.
- **F2 — FIRES in the p-direction only**: deployed flatness is identically 0 (no degradation to measure); the margin shortfall doubles per rung (6.3e3x -> 2.1e8x). Generic-frequency flatness stable at 0.59 +- 0.03.
- **F3 — FIRES and locates the freedom exactly**: the coordinate set is rigid; the FREQUENCY is free, and that is where flatness is decided. The implicit selection step already exists — the silent modelling decision in f2model.py/slicecore.py to use the single linear character, which places the ENTIRE banked F2A.2/A.5/A.5b pilot family inside the degenerate class K1 whenever the subgroup is the deployed one (invisible until now because those pilots always instantiated the FULL group, where flat ~ 0.61).

## 8. File inventory

Code: `tower.py` (rungs + antipodal law + LTE) . `deployed.py` (window builder, parity-defect certificate, Lambda/M_p/kappa) . `census.py` (stages orders|degen|scaling) . `moment.py` (K1/K2/G) . `verify.py` (A1-A8 ALL PASS) . `experiments.py` (stages classes|bandlim|slice|budget|scaling|classes2|residual) . `floor_ladder.py` . `selection.py` . `convention.py` . `probe0.py`. Results: 13 JSONs incl. `degeneracy_law.json` (194 rows), `E8_floor_ladder.json`, `E9_convention.json`. All under ramguard; nothing outside the directory; no commits; nothing m2-related.

## 9. Honest caveats

- Per-rung window/frequency set reconstructed from entry #76 (nowhere explicitly defined); a different reading changes m_j by 2x but CANNOT change the antipodal law.
- The law needs 2-power n and the subgroup one level above the fixed part — both hold at official rows by the campaign's own pins; fails if n has an odd part.
- Convention dependence measured (E9): "all Delta even" (hence every headline) is INVARIANT under orientation flips; max_{k != p}|R_k| is NOT (the banked half-system labelling converges to 2/pi ~ 0.637 as an artefact; random flips decay ~2.9/sqrt(m)). No residual-flatness number is banked as structural; the honest statement: after removing the labelling artefact, k = p is the SOLE obstruction (A7: residual flatness obeys the incomplete-Gauss-sum scale sqrt(p) ln p / m).
- Proxy scope: V_b magnitudes ride the balanced-weight proxy; the structural results (antipodal law, A_i(p) = B_i(p), |e_b(p)| = E_b, hhat_p(p) = 2) are exact with true weights.
- Extrapolation: exact V_b to m <= 128, p <= 641; flatness to m = 1024, p = 18433; official scale enters only via the LTE law (verified at the actual KoalaBear prime, all 16 rungs), the exact k=p identity, and the analytic M_p slope.
- Section 6's selection-cost arithmetic is planning-grade (pessimistic composition; PP5.0 unfrozen).
- NEW OBLIGATION OPENED, NOT DISCHARGED: the fixed sector absorbing the parity-pure class.
- Nothing mintable; F2A.1 seam and PP5.0 unchanged.
