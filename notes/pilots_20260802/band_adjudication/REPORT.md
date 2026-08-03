# Pilot report: band adjudication (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored). Coordinator verification and adopted posture:
FABLE_AUDIT.md alongside. This resolves the campaign's top
adjudication (d = h-1) with a priced recommendation; the decision is
ratified by the coordinator/maintainer.

---

# BAND ADJUDICATION — d = h-1, and whether the band proper is safe

**HEADLINE.** Three independent layers, all pointing the same way, and the resolution is NOT the binary the queue expected:

1. **d = h-1 is the CASCADE TIER, definitionally** (core = A-1 = k+t-1 is xr_pencil_cascade's hypothesis threshold), and the cascade forcing DOES fire on the MC pairs in its exact proved shape.
2. **The MC pairs are real** — new LEMMA MC-6 proves the MC family IS a family of joint codeword pairs at depth h-1 (the list-bound pilot only measured joint_explanation_max) — **but they do not populate N_{h-1} under the banked semantics**: all forced slopes collapse into -H, so |Gamma| = n and N_{h-1} <= n/2 — **46 bits below** the 18.5n^2 requirement. **MC refutes the occupancy lemma under NEITHER classification.**
3. **The MC received pair is not in scope at all**: it is QUOTIENT-PERIODIC at scale M = h-1, M | gcd(n,k) on all six rows, so **P3 fires** in the banked first-match strip order — before the tangent strip and before the generic branch. MC is literally the banked q_recursion "paid quotient mass from STRUCTURED pairs"; its completions satisfy P_T = X^{M-1} G_T(X^M) — the confinement node's own conclusion, verified 0 violations.

**The band proper is PROTECTED** (THEOREM BP), and the MC pair produces one genuinely new official-parameter fact: it **overflows the printed B_tan column n-A+1 by x1.3403 / 1.1480 / 1.0689**, upgrading the payment audit's F_17 toy witness to the actual six rows.

## 1. Classification — the exact chain

**1.1 The depth <-> core dictionary**: |S_z ^ S_z'| = |Z_P| exactly (banked T2 fibre identity), so core = k+d. Band proper = cores [k+1, A-2] = depths [1, h-2]; **cascade tier = core A-1 = depth h-1** (`xr_pencil_cascade/statement.md:9`); >= A is nongeneric (the sourced ceiling). **d = h-1 is the unique cascade-tier depth in the generic branch; "extend the ledger to [1,h-1]" is a scope change, not a bug fix.**

**1.2 The cascade forcing fires — exactly.** NEW LEMMA MC-6 (proved + verified 0 violations at 13 fixtures): for u = X^{n-1} + cX^{k+w-1} with w = M | k, every MC completion satisfies **P_T = X^{M-1}.G_T(X^M)** (coefficient matching against the coset locator's gap; the ceiling forces joint agreement EXACTLY k+w) — hence for every 1 <= j <= M-1 the shift v = u/X^j makes (P_T, P_T/X^j) a codeword pair of joint agreement exactly A-1. This is the banked `confinement` conclusion; only the "hence the family is joint" step is new. LEMMA MC-7: the direction map is zeta_{P_T}(i) = -x_i^j, injective on T at j=1 — each of the n-A+1 off-core points upgrades exactly one distinct slope to agreement exactly A: **the cascade's proved multiplicity-upgrade shape verbatim, here exact**.

**1.3 The multi-pencil scoping flag — confirmed and quantified.** Each pencil individually SATURATES the injection bound |T| <= n-A+1 with equality (constructively realizing the payment audit's 1.0000 six-row ratio); the union over all 2^130-2^197 pencils is NOT the sum — it is exactly -H, size n. **A single MC pair has |Gamma| = n, overflowing the printed B_tan slot by x1.3403 / 1.1480 / 1.0689** — the first cascade-tier overflow witness at exact official-row parameters. The correct aggregate statement: the union of all forced slope sets of one MC pair is -H.

**1.4 MC does NOT populate N_{h-1} — the decisive step.** (a) Slope confinement: Gamma subset -H, |Gamma| <= n (verified exhaustively). (b) Selection exclusivity: two depth-(h-1) cores in one A-support give |Z^Z'| >= 2(A-1)-A = k+h-2 >= k, violating the banked k-packing — each live slope serves AT MOST ONE cascade-tier pair (= the banked occupancy T4; shorter k-packing proof, no tangent gate needed). Hence Sum L_P <= |Gamma| <= n and **N_{h-1} <= n/2**. Measured: N_{h-1}(selected) = 3 where |MC| = 7 (never the family size).

| reading of L_P | N_{h-1} for MC | vs required |
|---|---|---|
| **SELECTED support (BANKED)** | <= n/2 = 2^40 | **-46 bits (safe)** |
| "any exact-A ray" (NOT banked) | = |MC| = 2^130-2^197 | +44 to +111 bits (refuted) |

**The definition is load-bearing and must be pinned** (definitions item 8).

**1.5 The layer that removes the question: MC is QUOTIENT-PAID.** u = X^{M-1}F(X^M), the word is mu_M-equivariant, every T is K_M-stable, P_T folds, mu_M permutes family and Gamma (104 checks, 0 fails — the full `confinement` configuration). P3 (quotient-periodic at M > 1, M | gcd(n,k)) fires with M = h-1 on ALL SIX ROWS (h-1 = 2^33 | 2^39 etc.); P0-P2 do not fire first. **The MC pair is QUOTIENT-PAID at T3, charged to B_quot_ub(A), and never reaches the generic branch.** Its mass descends to the quotient row where h' = 2 and the band proper is empty (third instance of the t=2 blindness genre).

## 2. THEOREM BP (band-proper protection from coset constructions) — proved

At the six-row shape (n = 2^N, h odd, h-1 = n/scale a power of two):

**(1) 2-adic depth exclusion.** A coset-union core complement forces M | d and (structured-floor completeness) M = 2^ceil(log2 d) >= d, hence **M = d, a power of two**. Structured depths in [1,h] are the powers of two; **the unique one in [ceil(h/2), h] is h-1; the band proper's upper window [ceil(h/2), h-2] contains NONE** — at all six rows. Excess h is not structured (h odd), so no live ray's agreement set is a coset union.

**(2) Slope confinement.** On the shift class v = u/X^j (the unique class keeping the whole family joint, since X^{M-1} | P_T), zeta_P(i) = -x_i^j with mu_g-coset fibres, g = gcd(j,n) | M: every forced ray has agreement exactly (k+d)+g. g < h-d: NO live slope (invisible to occupancy). g = h-d: live, |Gamma| <= n/(h-d), and with exclusivity **N_d <= n/(2(h-d)) — LINEAR in n**. g > h-d: the tangent gate breaks (P2 fires; leaves the generic branch).

**(3) Six-row conclusion.** g is a power of two; h odd makes h-d ODD for every even d, so g = h-d forces g = 1, i.e. d = h-1; d = 1 admits no shift. **No coset construction is productive at ANY band-proper depth: N_d^{coset} = 0 for all d in [1, h-2].** COROLLARY: the band-occupancy lemma survives with its ORIGINAL scope [1, h-2]; the MC/coset class does not fire F1.

Verification: 135 + 66 checks, 0 fails, including the h-EVEN positive control (n=20,k=4,h=6,d=4: the mechanism IS real — 10 live slopes, N_d = 2, still linear |Gamma| = n/(h-d)) — the protection at official rows is PARITY, not impossibility. Independent corroboration that the occupancy frontier is linear (the same law as the sunflower family, via a different mechanism).

## 3. Priced outcomes (exact; row pins recomputed and cross-checked against banked band_arith.json)

**Outcome (ii) — fold d = h-1 into the band column [1, h-1]:** cost = one added term L(h-1) = n-A+1 = **4.26 / 4.26 / 4.39%** of the extended column at the prize rows; the uniform N_d requirement tightens 0.8272 -> 0.7919 n^2 (etc.) — nothing structural. MC margin: -46 bits under the banked reading.

**Outcome (i) — keep d = h-1 as cascade tier:** the tier needs its own charge, req N_{h-1} <= 18.6/15.9/14.8 n^2, and by exclusivity |Gamma_casc| = Sum L_P EXACTLY, so the requirement is equivalent to |Gamma_casc| <= 13n^3 = **86.61% of the entire 16n^3 target** — self-financing at target level (cannot be both refuted and leave room for the rest).

**A single MC pair costs |Gamma| = n** — negligible against either column (-86 bits vs 13n^3) — while overflowing the printed B_tan slot by x1.34/1.15/1.07.

**B_tan re-baseline trip test:** charging the tier through B_tan consumes the same 13n^3 as the third column but EXHAUSTS the 0.858-bit retuning headroom exactly (X <= 13, not one more) and fires re-surgery trigger 4. **The third-column route strictly dominates.**

**RECOMMENDATION (decision = coordinator/maintainer):** take outcome (ii) — fold d = h-1 into the band column, in the third generic column, NAMING the tier explicitly ("cascade tier, d = h-1") so the cascade forcing stays citable as structure. Reasons: 4.3% cost; closes the A-1 scope hole (currently counted zero times) without touching B_tan (trigger 4 never fires, the 0.858 bits survive); needs no new theorem (the extension term is exact by exclusivity); makes [1,h-1] one uniform obligation instead of an obligation plus an unpaid stratum whose only candidate payer is refuted in-tree.

## 4. Definitions list for the coordinated edit

1. core(z,z') := |S_z ^ S_z'| = |Z_P| (T2); depth d := core - k; pin the symbol k (not K).
2. band (proper) := cores [k+1, A-2] = depths [1, h-2]; never "band" for [k+1, A-1].
3. cascade tier := core A-1 = depth h-1 (the unique generic-branch cascade depth).
4. **generic core ceiling** (new name needed) := all distinct-slope selected-support cores <= A-1 — the SOURCED unconditional property (genericity + strip forcing); this is what standing hypothesis lists should say.
5. **below cascade** := the cascade tier is EMPTY (max joint pair agreement <= A-2) — STRICTLY STRONGER than genericity and NOT available in the generic branch; the band ledger's hypothesis line must be corrected to item 4 (its theorems only use k-packing + the tangent gate, so the extension costs nothing in proof). The KEY LEMMA's "cascade event" usage renames to "joint-explanation event".
6. **strip-free** := none of P0-P3 fires (incl. P2 single-slope over-agreement and P3 quotient-periodicity at any M > 1, M | gcd(n,k)). Decisive here: **the MC pair is NOT strip-free (P3)**.
7. live slope := exact-A max agreement, over all of P^1 incl. (0:1); selected support = the ONE first-match exact-A ray.
8. L_P counts SELECTED supports containing Z_P; N_d = #{depth-d pairs, L_P >= 2}. Add the non-example: under "any exact-A ray", MC's N_{h-1} jumps n/2 -> 2^197. Load-bearing.
9. Gamma_casc = DISJOINT union of the Lambda_P (k-packing exclusivity): |Gamma_casc| = Sum L_P exactly — the ledger is TIGHT at the cascade tier.
10. structured/coset family := core complement a mu_M-coset union, M = 2^ceil(log2 d); THEOREM BP(1): structured => d is a power of two.

## 5. Falsifier verdicts

F-BAND: NOT FIRED (zero structured depths in the band-proper upper window at all six rows; low-band powers of two give L_P = 0). F-MC-BAND: NOT FIRED under banked semantics (-46 bits); fires only under the un-banked reading (escalated to a definitions item). F1: still not fired (the coset class obeys the same linear law). My pre-registered P1-P8, R1-R7, S1-S4: all confirmed (348 checks); Q1/Q3/Q6 FAILED AS STATED and were corrected + re-checked (|Gamma| = |union| — a single-member family gives exactly n-A+1, constructively reproducing the payment audit's saturation; char-p accidental extras at n=18 where MC-4's hypotheses fail). C-OVERFLOW (new): FIRES — x1.34/1.15/1.07 on all six rows.

## 6. File inventory

mclib.py (exhaustive pencil engine, covers (0:1)) . exp_mc_occupancy.py (109) . exp_ledger_charge.py (160) . exp_quotient_periodicity.py (104) . exp_band_proper.py (135) . rows.py (66) . priced_table.py . checkpoints/*.json. **574 machine checks, 0 residual failures.** Nothing outside the directory; no commits; nothing m2-related.

## 7. Honest caveats

1. **Gamma subset -H is toy-verified, not proved at scale** (no proof that mixed members lack exact-A codewords outside the forced set; exhaustive at n = 16/18/20, 6 primes) — the sharpest falsifier direction against the section-1.4 verdict; queued for internal adversarial review.
2. Official-scale gate-admissibility of the MC pencil rests on the list-bound pilot's Q2 (toy-verified here).
3. MC-4 is char-0 + 2-power; BP's exclusion direction is unconditional divisibility, but char-p accidental non-coset families occur (observed at n = 18, outside the six-row shape). BP protects against COSET-type attacks — the adjudicated question — not all conceivable families.
4. BP(2) covers the shift class only (the unique fully-joint class); general v heuristically empty but unproved.
5. **Whether P3 formally fires depends on the quotient convention ("syndromes descend"), not written out in-tree** — the single load-bearing unverified step in section 1.5; the section-1.4 verdict does NOT depend on it. Adjudicate with the quotient-convention owner.
6. Toy scale (n <= 20, q <= 241); the 2-adic arithmetic and six-row pricing are exact integers.
7. Novelty narrow and localized (MC-6, MC-7, THEOREM BP, the |Gamma| = n overflow); the folding, syndrome-folding, k-packing, exclusivity, line cap, T2, and the A-1 ceiling are banked.
8. One two-line text-edit patch ran under bare python3 (no computation); all numerical work under ramguard.

---

[COORDINATOR AMENDMENT 2026-08-02, from the adv_gamma_minus_h adversarial
pilot (banked, coordinator-replayed) — THEOREM Y supersedes caveats 1-2:
(i) at j = 1, Gamma subset -H is a THEOREM (coset confinement
-z in gamma.x0^{-(r-1)}.mu_n + realizability), unconditional in n,k,w,q,
beta,char, and the MC shift pencil's tangent gate is proved
unconditionally — caveats 1 and 2 CLOSE with no q-threshold; (ii) at
j >= 2 the set claim is REFUTED (18 gate-intact certified
counterexamples, headline |Gamma| = 2.2n), and the excess is governed by
X = C(n,A)/q^w — numerically identical to the gate-admissibility
threshold already assumed, so caveats 1-2 were ONE hypothesis, not two;
(iii) the cardinality bound |Gamma| <= n is unconditional at j = 1 and
more robust than the set claim — state them separately. Lemma wording of
record: "confinement = the j=1 coset theorem + realizability; j >= 2
inherits from the gate inequality X < 1."]

[COORDINATOR AMENDMENT 2 (2026-08-03, gamma_j2_close pilot, banked):
lemma wording of record UPDATED — confinement = THEOREM Y +
realizability = the E_1 = 1 case of the unconditional REDUCTION
|Gamma_j| <= n . E_j (THEOREM D), E_j the mu_n-coset count of
e_{j-1}(T^{-1}); structured part confined to -H^j (THEOREM E). The
prize rows have w = M hence j <= w-1, a regime with NO gate-intact
excess ever exhibited (39 rows to X = 4.44); every banked
counterexample has w = 2 < M, j >= w. The "inherits from X < 1"
clause is a CALIBRATION, not a theorem: X >= 1 is necessary (min
1.045) but NOT sufficient. Residual = bound E_j (consumer needs
<= 29.6 n vs trivial 2^209) — one symmetric function's coset spread,
attached to the unified structured-liveness kernel. Named obstruction
to any X < 1 proof: the one-parameter averaging gap (q^{w-1} short).]
