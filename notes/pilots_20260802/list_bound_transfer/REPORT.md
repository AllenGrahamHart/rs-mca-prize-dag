# Pilot report: list-bound transfer gate (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored; the full literature table and construction
details are in the pilot's checkpoints). Coordinator verification and
adopted posture: FABLE_AUDIT.md alongside.

---

# List-bound transfer pilot — the mandatory literature gate on the band-occupancy reduction

## VERDICT: **V1 — the reduced statement is FALSE.** Route T's high band needs a different split.

Two independent refutations, at all six rows, both inside the standing hypotheses:

**(R1) The generic refutation (first moment, exact).** At the prize rows with q at the official cap, a uniformly random pencil is ADMISSIBLE — inside the tangent gate and below cascade, both with wide margin (max-agreement excess ~0.55-0.82 h; joint-explanation excess ~0.41 h) — and every member carries ~2^(10^11) codewords at tau. Required: 2^81.5. Minimum log2 q for gate-admissibility: 209.26/141.93/176.58 — all below the 2^256 cap and the banked q >= 2^250 pin, so the whole official field range is in the refuting regime. E[L] validated against exhaustive censuses at five toy rows (2-5% accuracy).

**(R2) The explicit refutation (exact, certified, no probabilistic step).** The **MC (multiplicative-coset) construction** — which additionally supplies what the first moment cannot: a PROVED ceiling, so the tangent gate holds with certainty.

## 1. Literature pass

Full table in the pilot's text with access notes per row. Key rows: BKR (STOC'06/IT'10) — subspace polynomials on the WHOLE FIELD, agreement ratio a/k >= q, zero multiplicative content; Guruswami-Rudra (IT'06) — whole field, k <~ sqrt(q); Justesen-Hoholdt (IT'01, PAYWALLED — used via restatements) — the domain-agnostic counting bound; Cheng-Wan; **BCHKS25 (ePrint 2025/2055) section 7 — multiplicative subgroups via x -> x^c fibres, agreement exactly k+2c, needs sumset conjectures/Mersenne primes**; Shangguan-Tamo (constant at 1.01k). **Corrections to the brief's citations recorded**: 2025/2055 is Ben-Sasson-Carmon-Habock-Kopparty-Saraf (NOT Goyal-Guruswami) and its Omega(n^1.99) counts exceptional z on an F_2-subspace AT Johnson — not a list bound, not our regime; 2308.13424 is an alphabet-size bound.

**Why BKR does not transfer and what does**: F_{q^m} has q^{v(m-v)} subspaces; F_q^* has exactly ONE subgroup per order (~sigma(n) coset objects — polynomial). BCHKS route around via subset-plus-sumset hypotheses; **MC routes around unconditionally: vary the subset of the QUOTIENT group, constrain by a PRODUCT, which equidistributes exactly on a multiplicative coset**.

**Subtraction (hard law 5) — the mechanism is ours and banked**: `e22_tail_coset_locator_algebra` (PROVED — the locator factorization G(X^M) IS the MC mechanism); `rate_half_cyclic_rotated_prefix_floor` (PR #1051 — MC is its s=0, d=1 boundary case, pushed off rate 1/2, with the q^{d-1} loss removed by exact equidistribution); crossing PK1 is the c=1, s=0 boundary (MC's w=2 count reproduces PK1's measured w=2 shell exactly). **New here**: the exact q-free count with no q denominator; the ceiling at general w; the pencil theorem; the KEY LEMMA; the refutation.

## 2. The MC construction (Q1)

Word u = X^{n-1} + c X^{k+w-1} on H = x_0 mu_n; r' = n-k-w.

- **MC-1 (window classification, all w)**: codewords at agreement >= k+w <-> {T : |T| = r', e_1 = ... = e_{w-1} = 0, prod T = gamma}; exactness guard automatic; agreement EXACTLY k+w; injective.
- **MC-2 (ceiling)**: nothing at >= k+w+1 (m_0 = 0 impossible). Buys the tangent gate UNCONDITIONALLY.
- **MC-3 (the family)**: M | n, M | r', w <= M: coset unions of mu_M have e_1 = ... = e_{M-1} = 0 for free (banked e22); with gcd(m,N) = 1 the product equidistributes (PK1 Lemma 5): **exactly C(N,m)/N members, q-free**.
- **MC-4 (structured-floor completeness, n a 2-power, char 0)**: iterated Lam-Leung forces the structured solutions at excess w to be EXACTLY the mu_{2^ceil(log2 w)}-coset unions — MC is the maximal structured family.

**Exact censuses** (verify_mc.py, theory-free brute force, 161 checks 0 fails): formula matches at large q at four shapes; ceiling held at EVERY fixture and field. Constructive verification at scale (verify_scale.py, 3571 checks 0 fails): n = 32-96, F_97/F_193 + extension fields F_25/F_49/F_81.

**Prize-row arithmetic**: take w = M = h-1 — NOT a coincidence: at all three prize rows h-1 is the UNIQUE power of two in [ceil(h/2), h]. MC count at agreement A-1 >= tau: **2^197.13 / 2^130.18 / 2^163.77** vs required 2^81.7/2^81.5/2^81.4 — **excess +115.5 / +48.7 / +82.4 bits**. (RowC: +172 / +105 bits.) MC beats volume counting where volume is negative (RowC 1/8, 1/16). The structured zone extends to d/n ~ 0.0078 — the entire Route-T window sits inside it.

## 3. The pencil question (Q2) — settled: NO exclusion

**MC-5 (shift pencil)**: v = u/X mod Omega (same c) — EVERY member w_z (all q+1) admits the ENTIRE MC family; min over P^1 >= C(N,m)/N. Pre-registered, measured exhaustively over all q+1 members (verify_pencil.py, 30 checks 0 fails): min = MC exactly at large q, at two shapes; the control (c_1 != c_2) has min = 0 via the (0:1) direction — exactly the direction the occupancy pilot found the banked gate omits. Mechanism found exactly: the mixed-member exactness quotient fails at -beta/alpha in T, giving agreement k+w+1 = A (inside the tangent gate).

**Hypothesis audit**: non-degeneracy ✓, tangent gate ✓ (ceilings proved), global genericity ✓ (joint_max = A-1 < A), k-packing automatic. **(H2) below-cascade in the <= A-2 reading FAILS by exactly one step — and at the prize rows this is 2-adically forced.** That gap is closed by (R1) (a random pencil is below cascade with ~60% margin and still has E[L] = 2^(10^11)) and by the pre-registered toy search: 23/25 random pencils below cascade with min in [9,20] tracking E[L]; hill-climbing restricted below cascade reaches min = 22; **C3 ("large pencil min forces a cascade event") FALSIFIED**.

## 4. The incidence-theorem attempt — two real theorems, and why V3 dies

- **THEOREM I (pencil mass identity)**: sum over z in F_q of agr(c, u+zv) = n for EVERY codeword c (fibres of (c-u)/v partition H); with zeros: = q.e(c) + (n - |Z|). Corollaries: #{z : agr >= a} <= floor(n/a); for a > n/2 the members' lists are PAIRWISE DISJOINT. Verified exhaustively (4004 checks, 0 fails; 681+791 distinct codewords over an MC pencil, 0 duplicates).
- **KEY LEMMA (pencil support dichotomy)**: for |S| = a >= k, the top-(a-k) interpolant coefficients are LINEAR in the word: I_S(w_z) = A(S) + z.B(S). Either A = B = 0 (u|_S and v|_S BOTH codewords — a joint pair explanation of size a, i.e. a cascade event at depth a-k — and ALL q+1 members use S), or AT MOST ONE member has a codeword with agreement support S. **Below cascade <=> distinct pencil members never share an agreement set.**
- **Why V3 dies**: the only averaging route the pencil supports is exactly as strong as the first moment (rank-one is w-1 conditions: count ~ C(n,a)/q^{w-1}, bound ~ E[L] = 2^{6.9e11}). No poly(n) trade-off law can be true: MC exhibits min = C(N,m)/N under (H1)+(H3)+non-degeneracy; the random pencil exhibits min ~ 2^(10^11) under those plus below-cascade.

**Diagnosis of the reduction**: Theorem 2 (N_d <= min_z L(w_z, k+d)) is CORRECT BUT ASTRONOMICALLY LOSSY — it bounds a two-slope object by a one-slope object, discarding ~2^{1.6e12} of structure (the occupancy pilot's own first moment for the two-slope object is 2^{-1.37e12}; the one-slope object is 2^{+2e11}). **The occupancy lemma may well be true; the list bound it was reduced to is false. The reduction cannot be repaired by sharpening the list bound — the two-live-slope condition must be kept.**

## 5. Answers

**Q1**: worst-case single-word lists at tau on multiplicative domains are astronomically superpolynomial — via the subgroup-vanishing mechanism already banked in our tree (e22, #1051), independently present in BCHKS25 section 7, here made exact, q-free, all-rate, ceiling-controlled. **Q2**: the pencil does NOT exclude simultaneous blow-up — explicitly (MC shift pencil) and generically (first moment).

## 6. File inventory

lbt_lib.py . verify_mc.py (161) . verify_pencil.py (30) . verify_scale.py (3571; RAMGUARD_TIMEOUT=9m) . incidence.py (4004) . search_below_cascade.py (26) . prize_arith.py . dsweep.py . first_moment.py (+ validation + q_thresholds). **7792 machine checks, 0 failures.** Nothing outside the directory; no commits; nothing m2-related.

## 7. Honest caveats

1. **Refuting the reduced statement does not refute the occupancy lemma** — it refutes Theorem 2 as a route. Route T's high band needs a split retaining the two-live-slope structure.
2. (R1)'s "typical word" needs an unverified concentration step (second moment sketched, not carried out); **(R2) has no probabilistic step and is the certified half**.
3. The MC shift pencil sits exactly one step outside the <= A-2 below-cascade reading (2-adically forced at prize rows); the single-word half is refuted unconditionally regardless; the pencil half unconditionally under (H3)+genericity, and under (H2) via (R1) + the toy search.
4. **"Strip-free" could not be found defined; coordinator adjudication needed on: (a) which below-cascade reading is binding; (b) whether depth d = h-1 — where MC produces >= 2^130..197 pairwise non-interacting band pairs on an explicit gate-admissible pair — is inside the band or is the cascade tier. IF INSIDE THE BAND, MC REFUTES THE OCCUPANCY LEMMA ITSELF. The single highest-value item to adjudicate.**
5. Novelty limited and localized (mechanism banked + BCHKS-independent; new: ceiling at general w, exact q-free count, pencil theorem, KEY LEMMA, the refutation).
6. Justesen-Hoholdt paywalled (used via restatements); BKR journal text unread.
7. Exhaustive censuses to n <= 24; n <= 96 constructive only; MC-4 is char-0 and bounds the structured part only (accidental excess only makes lists larger).
8. n = 2^41 figures use Stirling for log2 C; exact integers everywhere n <= 4000 and for all MC counts.
