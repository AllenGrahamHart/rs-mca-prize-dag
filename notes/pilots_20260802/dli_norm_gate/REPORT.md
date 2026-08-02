# Pilot report: DLI norm gate (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored). Coordinator verification and adopted posture:
FABLE_AUDIT.md alongside.

---

# DLI norm gate: L13 formalized, the C1/C2'' census bridge, and the official-scale router

## HEADLINE

**The two lanes are not "converged on the same machinery" — at junction 0 they are the SAME OBJECT.** A C2'' junction-0 skew solution at (n, t=2, q) *is* a C1 ternary relation at 2N = n, verbatim, and the two censuses are byte-identical where they overlap. Consequences:

1. **L13's forward direction is a two-line theorem** (LN1), upgrading to q^o | Norm for an o-constraint block (LN2) — which is what the DLI tower actually has.
2. **The measured 1/phi(n) is not a Chebotarev conjecture. It is an exact counting identity plus an explicitly bounded correction** (LN7/S1-S3): #sol/#norm-divisible = mbar/phi(n) where mbar is the mean number of primes above q dividing the element — = 1 exactly whenever q^{o+1} > maxnorm. **0 violations in 1930 measured rows** across n = 16, 32, 64, 128 and o = 1, 2, 3.
3. **The AM-GM ceiling transfers verbatim** (it never used ternariness — only sum a_i^2), giving an exact integer official criterion: **at every official junction, a skew solution of energy E requires q <= E^128.** At the C2'' named 256-bit exhibit: **every junction-0 solution has |S_0| >= 4**.
4. **A new unifying law for the whole banked WCL ladder: the norm fence is q > w^128 (unconditional) / q > c_w^64 (C1 doubling law), independent of the window index ell.** The official cap 2^256 = 4^128 **exactly** — which is why weights <= 3 were cheap, weight 4 needed a 1.4-billion-polynomial enumeration, and **no open slot (all have w >= 5) can ever be reached by the norm gate.**

## 1. The proved lemmas (full proofs in the pilot's text; summaries here with the load-bearing steps)

Setting: n = 2^s, h = phi(n) = n/2, q odd prime with n | q-1, zeta in F_q of exact order n; Z[zeta_n] = Z[x]/(x^h+1); Norm = Res(., x^h+1).

- **LN0 (splitting).** q unramified, Frob trivial iff q == 1 mod n, so q splits into h distinct degree-1 primes; Galois acts SIMPLY TRANSITIVELY on them. pi: Z[zeta_n] -> F_q, zeta_n -> zeta; p = ker pi. *Ramification caveat stated exactly: admissibility n | q-1 is load-bearing for LN2.*
- **LN1 (forward L13).** G inside the basis range [0, h), eps in {+-1}^G, alpha = sum eps_i zeta_n^i. If sum eps_i zeta^i = 0 in F_q then q | Norm(alpha) != 0. *Proof: alpha in p; N(p) = q divides N((alpha)).* The basis-range hypothesis is ESSENTIAL (opposite pairs fold to zero otherwise — exactly the banked "no opposite pairs" clause); the DLI tower's junction cells satisfy it BY CONSTRUCTION.
- **LN2 (o-fold upgrade).** If the sum vanishes at zeta^{ui} for every u in U, |U| = o, then q^o | Norm(alpha). *Proof: sigma_u^{-1}(p) pairwise distinct by simple transitivity.* The official schedule's U_j = {odd u : u.2^j <= t} satisfies the hypothesis at every junction.
- **LN3 (computational form).** q | Norm <=> some odd-exponent evaluation vanishes; q^{m} | Norm for m = #hits. Makes the measurement determinant-free (verified vs Bareiss + sympy: 0 mismatches, 810 exhaustive + 33,120 sampled).
- **LN4 (ENERGY ceiling — the C1 sandwich Claim 2 generalized).** For nonzero integer-coefficient alpha: 1 <= Norm(alpha) <= E^{h/2}, E = sum a_i^2. *The banked proof verbatim with w -> E; ternariness was never used.* 0 violations over exhaustive [-3,3]^4, all ternary at h=8, 20,000 random [-4,4]^8; reproduces every banked maxnorm.
- **LN5 (junction router).** At junction j: a solution forces q^{L_j} <= Norm <= E^{phi(h_j)/2}. Contrapositive kills states.
- **LN6 (multiplicity bound).** m <= log(maxnorm)/log q. 0 violations in 1930 rows; near-sharp (m = 4 attained where the bound is 4).
- **LN7 (THE SPLITTING LAW — identity, not conjecture).** With H_U(alpha) = {a : aU inside Z(alpha)}: **(S1)** phi(n).#sol_w = sum |H_U| over W_w (double-count via sigma_a, which is a SIGNED PERMUTATION of the basis and so bijects W_w); **(S2)** ratio = mbar/phi(n) >= 1/phi(n), equality iff multiplicity <= 1 throughout; **(S3)** q^{o+1} > maxnorm(phi(n), w) forces ratio = 1/phi(n) EXACTLY.

## 2. Splitting statistic at scale — data vs pre-registration

PREREG.json frozen before measurement. Scans: n=16 (all 64 admissible q <= 4000, w 1-8 exhaustive, + U = {1,3}, {1,3,5}), n=32 (20 primes, w 1-8, 3.29M vectors/row, + o > 1), n=64 (10 primes, w 1-6, 58M vectors/row), n=128 (7 primes, w 1-4). **Consolidated: S1 0/1930 violations; S2 0/143; S3 0/143; LN6 0/1930.** All 53 deviating rows have max_m >= 2 and fail S3's condition — not one exception. Deviation always upward, ratio.phi in [1, 2]. The C2'' pilot's own {17, 97, 113} observations reproduce exactly (97, 113 exact at 1/8; 17 deviates because 17^2 = 289 < maxnorm(8,5) = 529). o = 2,3 rows with solutions: every one exactly 1/phi(n).

**Verdict: the "Chebotarev-flavoured equidistribution conjecture" is not needed and is the wrong frame** — Galois equidistributes EXACTLY (S1 is an identity); the deviation is a multiplicity effect bounded by the norm ceiling.

## 3. The census bridge

**3.1 The dictionary is an identity**: junction 0 at t=2 has U_0 = {1}, columns v_i = zeta^i over i in Z/(n/2) — a skew solution IS a C1 ternary relation at 2N = n (same admissibility, same half-section, same Norm). Only the stratification differs (C1 by weight, C2'' by support).

**3.2 Same primes, independent code path**: the skew census at 2N=16 is byte-identical to the banked C1 census (same 11 primes, same minimal weights); 2N=32 w<=3/w<=4/w<=5 censuses identical (5 / 24 / 160 primes). Three independent implementations now agree. **The C2'' L13 primes {17, 97, 113} are precisely the first three C1 census primes** — L13 was, unknowingly, evaluated on C1 census points.

**3.3 The 70529 coincidence appears verbatim on the C2'' side** (it must — the objects are equal): the banked witness has Norm = 70529 exactly, annihilates exactly one primitive root (m = 1, as S3 requires).

**3.4 The skew-norm ladder IS the C1 norm ladder** (every value matches; AM-GM attained exactly at s in {1,2,3,7}). **F1 does not fire.**

**3.5 New exact table — the ell = 2 (U = {1,3}) skew census at 2N = 32** (complete, w <= 8): w <= 4 EMPTY (independently reproducing dli_wcl_newton_short_window_exclusion at a different order); w=5 {97}; w=7 {97,193,257}; w=8 {97,193,257,449,577}. The candidate->confirmed gap (13 -> 3 at w=7) freshly measures the "alignment cost beyond divisibility" (~RESULTANT_GATE_SUMMARY's 10x). *Self-audit note: the first run reported "empty at all weights" due to a sieve bound bug (maxnorm^{1/o} instead of maxnorm); caught by the cross-check against the splitting scan, fixed, rerun. Recorded because a wrong empty census is exactly the dangerous false negative.*

## 4. The router threshold and its OFFICIAL pricing

Official pins: n = 2^41, t = 2^33, 33 junctions, ell_j = 2^{32-j}, N_j = 256 L_j uniformly. LN5 with phi(h_j) = 256 L_j:

> **q^{L_j} <= E^{128 L_j} <=> q <= E^128, INDEPENDENTLY of j.** No floats: E >= E_min(q) := min{E : E^128 >= q} at every official junction.

E_min: 2 at q up to 2^128; 3 above; **4 for all q > 3^128 = 2^202.875** — including the C2'' named exhibit q = 2^256 - 191315023233023 and the production window q ~ 2^255.9 (53 bits of margin).

> **Theorem (official support forcing).** For every official q > 3^128, every t-null state satisfies |S_0| = 0 or |S_0| >= 4; at junction j, any state whose unsaturated cells (all c_i = 1) number at most 3 admits NO admissible skew.

**Correction to the task's phrasing**: the router does not merely make Rem vanish — the whole local ratio vanishes (rho_j = 0, so Rem_j = -q^{delta_j} exactly). **It kills states.** Honest pricing of o = 1: the single-constraint fence excludes only E = 1 at official scale — ALL the strength is LN2's q^{L_j} at the fixed 256:1 ratio. Tower validation at real junctions j = 0,1,2 with bounded non-ternary skews: LN2/LN4/LN5 0 violations; 2,053 states predicted empty by the router, 0 solutions found in them.

## 5. THE WCL NORM FENCE — a unifying law for the banked ladder

The WCL slot family (order M = 512 ell, o = ell) gives the fence q^ell > maxnorm(256 ell, w): **unconditional q > w^128; conditional (C1 doubling law) q > c_w^64 — both independent of ell** (the 512:2 = 256:1 ratio again). Consequences:

1. **The banked weight-3 ambient exclusions (11M + 89M polynomial enumerations) follow in two lines** from LN2+LN4 for every q > 3^128 (honest scope: the banked nodes cover ALL q < 2^256; the fence covers the top of the range).
2. **4^128 = 2^256.0000 — exactly the official cap.** A complete structural explanation of why weight 4 needed a 1,398,341,120-polynomial enumeration while weight 3 did not. Conditional on the C1 doubling law at w=4 up to N=256 (verified to 2N=128; mechanism refuted, pattern stands), the fence becomes 14^64 = 2^243.7 and the (1,4) slot follows in two lines — **a concrete new consumer for the C1 lane's conjecture.**
3. **DECISIVE NEGATIVE: no open WCL slot (all have w >= 5) can ever be reached by the norm gate** (even conditionally: 23^64 = 2^289.5 > 2^256). **Do not spend effort pushing max-norm bounds at the open slots.** The remaining lever is a COUNT bound (Minkowski second minimum, per RESULTANT_GATE_SUMMARY).

## 6. The reserve test

Full junction-0 rho distribution recomputed independently over all 2^{phi(n)} supports: **exact ground-truth match on all C2'' rows** (min/max/mean as exact rationals; the (32,3,97) mean differs only by a documented stratum convention with identical numerator). R1 aggregate identity exact everywhere. R2: the binomial model's mean is exact once 1/phi is replaced by mbar/phi (1.0000 at the max_m = 1 row); ceiling valid; **variance under-dispersed ~2x** (solutions cluster within supports — reported as a limitation). **R4: the "588x blindness" is fully accounted for** — every extreme rho sits at a minimal-weight census support (rho = q^o . skewcount/2^{|G|}; the worst case (32,97,U={1,3}) at support size 5 = the ell=2 census minimal weight of 97). **The C2'' "invariant blind, worst case 588x" is the C1 census's low-weight witnesses, priced exactly.** A currency identity flagged: the junction-0 reserve mean = (q^o/(2^phi - 1)) x the weighted signed-vanisher orbit sum — the SAME object the raw-ledger guardrail says C1' consumes. **R3 DIES with a scored pre-registration MISS**: the q-independent norm multiset does not determine rho (332/409 = 81% ambiguous classes — worse as a fraction than L12's 51%, against the pilot's own prediction); rho depends on WHICH prime divides — the Galois-position data — which is exactly why the splitting factor exists.

## 7. Falsifier verdicts

**F1 — NOT TRIGGERED** (the ceiling transfers verbatim; norms bounded by energy; router validated at real junctions).
**F2 — TRIGGERED against the naive form and REPLACED by something stronger** (the deviation is systematic, upward, exactly = mbar/phi(n), an identity + bounded correction; vanishes identically under S3's condition — the conjecture is discharged as a theorem).
**F3 — NOT TRIGGERED** (exact ground-truth reproduction; the extremes fully explained). Caveats kept: variance ~2x under-modelled; the norm multiset alone under-determines rho. Both are refinements of the arithmetic account, not non-arithmetic structure.

## 8. File inventory

`PREREG.json` (frozen first) . `scripts/`: core.py (self-test 4/4), bridge.py, splitting.py (6 stages), ladder.py (official pricing + WCL fence), reserve.py (stages a-h), tower.py, pair_census.py, analysis.py . `results/`: selftest, bridge, ladder, tower, pair_census(+log), splitting_* (6 scans + logs), reserve_* (4), analysis. 1.4 MB. All under ramguard; nothing outside the directory; no commits; nothing m2-related.

## 9. Honest caveats

1. The C2''(t=2) = C1 identification is proved at junction 0; at j > 0 the SHAPE is proved (LN1-LN5 general, tower-validated) but the census identification is junction-0.
2. The E >= 4 statement needs q > 3^128 (covers the production window; formally official q can be as small as ~2^41, where E_min = 2).
3. The (1,4) two-liner is conditional on the C1 doubling law at w=4 to N=256 — a verified pattern whose proposed mechanism (imprimitivity) is REFUTED; extrapolation flagged as such.
4. Scale: exhaustive to n=128 at w<=4, n=64 at w<=6, n=32 at w<=8; official statements are exact consequences of proved lemmas.
5. o > 1 splitting measured only for U = {1,3}, {1,3,5} at n <= 32 (9 nonempty rows — small sample).
6. R3's pre-registered prediction FAILED (recorded as a miss).
7. R2's variance wrong by ~2x (mean/ceiling account, not a distributional fit).
8. A real bug found and fixed mid-pilot (pair-census sieve bound), caught by a cross-check; recorded.
9. Junction count follows the banked official_scale.json (33 junctions); a 34th-block reading gives E_min = 16 at the exhibit — not used in headlines.
10. Norm(alpha) != 0 needs the support inside the basis range — true by construction in the tower; THE hypothesis that would break everything if a future seam folded cells onto opposite pairs.

---

**[CORRECTION OF RECORD 2026-08-02, from the mint-prep audit]:** the
persisted artifacts (analysis.json + the six splitting_*.json) record
**1960 rows / 63 deviating** (the text above says 1930/53) and
tower.json sums to **2,453 router-empty states** (text says 2,053).
The artifacts are the record. Additionally: of the 63 deviating rows,
54 have a banked maxnorm and none satisfies S3's condition; the 9
n=128 rows leave S3 UNTESTED there (not confirmed). No verdict
changes.

**[SECOND CORRECTION OF RECORD 2026-08-02, from the WCL count-bounds
pilot]:** the closing line "the remaining lever is a COUNT bound
(Minkowski second minimum...)" mis-transfers the lever: in
RESULTANT_GATE_SUMMARY it was posed for the M-BOUND (multiplicity),
where it is sound once restated over the ring action; for the
ZERO-EVENT WCL slots it is structurally wrong (all Z-minima of a
relation lattice are equal — the shift is a free isometry — and the
banked 256-bit engineered witness caps every v_2-blind bound at
kappa <= 1.507 vs the needed 3.97-8.73). Slot closures must be
v_2-aware (the sparse-certificate route). See
notes/pilots_20260802/wcl_count_bounds/.
