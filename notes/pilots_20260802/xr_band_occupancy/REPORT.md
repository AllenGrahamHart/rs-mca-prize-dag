# Pilot report: band occupancy attack (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored). Coordinator verification and adopted posture:
FABLE_AUDIT.md alongside.

---

# Band Occupancy pilot — proof attack, adversarial constructions, ledger sharpness

## VERDICT

**The occupancy lemma is not closable from the banked toolkit, but it REDUCES.** Four new theorems; the decisive one converts **96.9% of the ledger's cost** into a **single-word Reed-Solomon list-size bound** — a statement of the same species as the prize's own positive target #1, not a new species. Empirically the falsifier **F1 did not fire**: the best admissible construction (a new, exact *sunflower* family) gives **N_d = floor((n-k+1)/(h-d)) — exactly linear in n**, matched at all 15 data points, a factor ~3e21 below the 0.68n^2 requirement at the prize rows. On sharpness, the master inequality is **exactly tight** (slack 1.000) on the single-core family and slack exactly 2.0 on the max-N_d family — **no weaker occupancy bound is available**, correcting the banked "arbitrarily lossy" caveat in the direction that matters.

Two corrections to banked claims: **re-selection freedom does occur** (Route S is un-killed), and the banked gate **omits the (0:1) pencil direction**.

## 1. THEOREMS (all verified, 0 violations on 76 admissible fixtures)

Notation: pencil words `w_z = u + zv` (`z in F_q`), `w_inf = v`; projections `pi_z(f,g) = f + zg`, `pi_inf(f,g) = g`; `D_z := ker pi_z = {(-zg, g)}` is k-dimensional. Standing hypotheses: (H1) k-packing [banked]; (H2) below cascade; (H3) **tangent gate**: for every `z in P^1(F_q)` and codeword c, `agr(c, w_z) <= A`.

**THEOREM 1 (unified fibre strip).** If distinct band pairs P, P' at depths d, d' satisfy `pi_z(P) = pi_z(P')` for some `z in P^1(F_q)`, then `|Z_P u Z_P'| <= A`, hence `|Z_P ^ Z_P'| >= k+d+d'-h`, and with (H1) **`d + d' <= h-1`**.
*Proof.* c := pi_z(P) = pi_z(P') agrees with w_z on Z_P u Z_P' (on Z_P: c(x_i) = f+zg = u_i + z v_i); (H3) caps the union at A; then (k+d)+(k+d') - |Z^Z'| <= k+h with |Z^Z'| <= k-1. QED

Contains banked Theorems 4+5 + corollary, but: (i) z need not be live; (ii) neither pair needs a live slope; (iii) **extends to z = 0 and z = inf** (pairs sharing their f- or g-component — not covered by the banked statements); (iv) needs the gate at one direction only. Banked T4's uniqueness = `{D_z}` is a **partial spread** of C x C.

**THEOREM 2 (component multiplicity; high-depth injectivity) — the designated lever, discharged.** Fix `z in P^1(F_q)`, codeword c, `a := agr(c, w_z) <= A`. Depth-d band pairs with `pi_z(P) = c` number at most `M(a,d) <= C(a, h-2d)/C(a-k-d, h-2d)`, and **M = 1 whenever 2d >= h**. Hence for every `d >= ceil(h/2)`, `P -> pi_z(P)` is injective on depth-d band pairs for EVERY z, so

> **N_d <= min_{z in P^1(F_q)} #{c in C : agr(c, w_z) >= k+d}.**

*Proof.* pi_z(P) = c forces Z_P inside S := agr(c, w_z), |S| = a. Cores are (k+d)-subsets of S; complements have size a-k-d; the k-packing转 |comp ^ comp'| <= a-k-2d-1 <= h-2d-1; each complement contains C(a-k-d, h-2d) subsets of size h-2d, distinct across members. If 2d >= h the bound forbids two distinct members. Finally agr(pi_z(P), w_z) >= |Z_P| = k+d. QED

**THEOREM 3 (spread-coset form — keyed on RAYS, not slopes).** Band pairs subordinate to a live ray (z,c) lie in the single coset pi_z^{-1}(c); two live rays with distinct slopes determine at most one band pair. **The slope-keyed version is FALSE**: 15 of 76 admissible fixtures carry a slope with two distinct exact-A rays; per-ray: 0 violations in 105 fixtures.

**THEOREM 4 (partial linear space).** The live-slope sets {Lam_P} of band pairs with L_P >= 2 are lines of a partial linear space on Gamma_band (two lines meet in <= 1 point): Sum_P C(L_P,2) <= C(|Gamma_band|,2). Each slope carries at most one line of depth >= ceil(h/2) (T1 with d = d'), so Sum_{d >= ceil(h/2)} N_d <= |Gamma_band|/2 and the high-depth part of Sum_P L_P equals |Gamma_band^hi| exactly.

**PROPOSITION 5 (no-go for every slope-side route).** T4 gives N_d <= |Gamma_band|.M_d/2, so the occupancy lemma would follow from |Gamma_band| <= 1.32n^2 — **n/6 times STRONGER than the program's own open P-B budget**. The lemma cannot be obtained by counting slopes; it must be proved on the codeword-pair side.

## 2. THE HEADLINE — the reduction

At the prize rows **96.91 / 96.91 / 96.81%** of Sum_d L(d) sits at depths d >= ceil(h/2) (exact divisor-block arithmetic; the banked pricing tables reproduced exactly as validation). With Theorem 2:

> **The binding half of the band occupancy lemma is implied by: some pencil member w_z has at most 0.80 / 0.686 / 0.660 . n^2 codewords at agreement >= tau = k + ceil(h/2).**
> tau = 1.0078k / 1.0156k / 1.0156k — i.e. **0.8-1.6% above the rate** — with the Johnson agreement at 2k / 2.83k / 4k, so tau sits at **25-50% of the Johnson radius**.
> The residual low band (d < ceil(h/2), 3.1% of the cost) is free at any bound up to n^2: it then costs only 0.518 / 0.605 / 0.649 n^3 of the 13n^3 headroom.

This is a lane-level re-routing: the open heart is no longer a bespoke two-variable anti-concentration statement but the classical single-word RS list-size problem just above capacity — the species of positive target #1 (L1 / #106 Q_1 <= n^B). And it is weaker than it looks: the min over z means it suffices that ONE of the q+1 pencil members has a small list.

**Deza corollary (proved sub-case).** At d = (h-1)/2 (all six rows have odd h), T1 forces every pairwise-interacting clique of depth-d band pairs to be an equidistant family with lambda = k-1 exactly, so **Deza's theorem** applies: each clique is a sunflower (size <= L(d)+1, linear in n) or has at most (k+d)^2-(k+d)+1 = 0.0635/0.0161/0.0040 n^2 members — 10x to 170x inside the target. Bounds cliques, not N_d; a covering argument is missing.

## 3. WHICH ANGLES DIE, AND WHY

| angle | verdict |
|---|---|
| (a) dimension count / interpolation + k-packing | DEAD (log2 ~ 7.1e11 vs target 83 at prize 1/16); the L >= 2 "disjoint residual" upgrade fails — the structured points are not exclusive to a pair |
| (b) ray rigidity / the L >= 2 constraint | **THE ONE THAT WORKS** — Theorem 2, terminating in the list-size statement. Per-slope line multiplicity = 1 for d >= h/2 but 2^{2.8e10} at d = 1 |
| (c) moment / double counting on k-sets | DEAD — m_i (pairs through a coordinate) bounded by nothing banked; W-collision moments bound rays through a k-set, not cores; routed through them the bound is C(n,k)-scale |
| (d) interaction strip as packing | quantified: removes nothing from N_d (non-interacting families unconstrained); its payoff is T2 + the Deza clique bound |
| first-moment / heuristic | B* = 2^122 exactly at RowC and 0.933 x 2^128 at prize; at pinned field size a uniformly random pair passes the gate and E[#(depth-d pair, 2 live slopes)] = 2^{-1.37e12} at prize 1/16. **The lemma is true on average with astronomical room; its entire content is the adversarial worst case** — no probabilistic argument will reach it |

## 4. ADVERSARIAL CONSTRUCTIONS AND THE GROWTH LAW

**New construction — the SUNFLOWER family.** m cores of size k+d through a common (k-1)-set, at d = (h-1)/2 (h odd). Both differences of any two interpolated pairs vanish on the common set, hence are constant multiples of its vanishing polynomial => proportional => the two pairs share a slope, and by T1 the ray there has support Z_i u Z_j of size exactly k+2d+1 = A — **a live slope for free, no planted blocks**. Every core carries L_P = m-1 live slopes, exactly the line cap. Admissibility needs the C(m,2) forced slopes distinct.

Verified exhaustively admissible at (n,k,t) = (16..64, 3, 3) [d=1] and (16..52, 3, 5) [d=2]: N_d matches floor((n-k+1)/(h-d)) at ALL 15 points; |Gamma_band| = C(m,2) exactly; ledger slack exactly 2.00. **Growth law: N_d exactly LINEAR** (log-log fits 1.07, 1.17, excess = the additive constant); |Gamma_band| quadratic (n^2.19, n^2.53). Best over 105 fixtures: N/n = 0.4844, N/n^2 = 0.0076 and DECREASING in n. Other attacks worse: multi-sunflowers N/n <= 0.375; pushing the share to k points fails the gate exactly as T1 predicts (8 T1 "violations", ALL on inadmissible fixtures); hill-climbing N/n <= 0.19, N = 0 at q = 401.

> **F1 NOT FIRED.** No admissible construction with N_d ~ n^2. Transported to the prize rows the family gives N_d = 2(n-k+1)/(h+1) = 384/448/960 vs required 0.68n^2 = 3.3e24 — margin ~3e21. Degrees-of-freedom heuristic agrees: each band pair with two live slopes consumes 2h-2 of the received pair's 2n parameters, N <~ n/(h-1).

## 5. SHARPNESS OF THE MASTER LEDGER

Over 59 admissible fixtures with band mass, (Sum N_d L(d)) / |Gamma_band| ranges from **1.000** (banked single-core V1 — exactly tight) to 20.6, with **exactly 2.000 on the entire max-N_d sunflower family** (each slope on exactly two lines). **The master inequality is attained**: lossy generically, tight in the worst case — a slope-counting reformulation buys at most a factor 2, not a weaker occupancy bound. Corrects banked caveat 1. Empirically |Gamma_band| ~ n^2 while N_d ~ n and L(d) ~ n: the ledger's product shape is right.

## 6. FILE INVENTORY

`occlib.py` (engine: exhaustive scan extended with the (0:1) direction, occupancy quantities, machine checks of T1-T4; bandlib imported read-only, banked directory byte-identical) . `val.py`/`val.json` (banked V1 reproduced incl. the gate's rejection of seed 3) . `theory.py`/`theory.json` (exact six-row arithmetic: pricing validation, Johnson regime map, first-moment exponents, ledger mass split) . `reduce.py`/`reduce.json` (reduction constants, Deza bound, sunflower law, growth fits) . `battery.py` + `battery_{sun,odd5,multi,climb}.json`, `climb.log` . `aggregate.py`/`aggregate.json` (105 fixtures, 76 admissible, 0 violations of k-packing/T1/T2/T3/per-ray/line-cap/fibre-identity on admissible fixtures). No commits; nothing outside the directory; nothing m2-related; all under ramguard.

## 7. HONEST CAVEATS

1. **Nothing here proves the occupancy lemma.** The reduction moves 97% of its cost to an RS list-size bound at 25-50% of Johnson — open "beyond-Johnson" territory. At least one variable simpler, side-condition-free, and the form the literature attacks.
2. The low band still needs N_d <~ 20-25 n^2 per depth (equivalently Sum_{d<h/2} N_d <= 0.054 n^3).
3. **Literature risk, flagged not resolved**: Ben-Sasson-Kopparty-Radhakrishnan-style subspace-polynomial constructions give superpolynomial lists slightly beyond Johnson on ADDITIVE-subspace evaluation sets; the prize domain is multiplicative, where transfer is not obvious — NOT checked against notes/literature_map_20260726. **The sharpest falsifier direction for the reduced statement; must be checked before the reduction is banked.**
4. **Regime mismatch worse than scale**: A/sqrt(kn) = 0.504/0.357/0.254 at prize rows but 0.78-1.08 across the banked battery (at/above Johnson, where lists are provably small — the toy regime cannot in principle exhibit the blow-up). New shapes reach 0.43-0.77. The sunflower arithmetic is parameter-free and extrapolates; the ABSENCE of better constructions does not.
5. The sunflower is verified only at d = (h-1)/2, odd h; general-d N_d ~ n/(h-d) is the point-budget heuristic.
6. **The banked gate is incomplete**: bandlib's scan never tests the (0:1) direction. Added here; 0/76 admissible fixtures fail it (no banked fixture retroactively invalidated) — but Theorem 2's z = inf instance needs the gate stated pencil-wide.
7. **Re-selection freedom is real**: 15/76 admissible fixtures carry a slope with two distinct exact-A rays (birthday collisions among the C(m,2) forced band slopes — appears precisely when the band is populous). The banked "Route S has no purchase" claim is REFUTED at toy scale; every rigidity/coset statement must be keyed on rays, never slopes.
8. Deza bounds cliques, not N_d; the covering argument is missing.
9. Hill-climbing was shallow (single-coordinate, <= 300 iterations, n <= 28).
