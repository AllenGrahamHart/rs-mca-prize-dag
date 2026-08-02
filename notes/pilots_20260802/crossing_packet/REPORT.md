# Pilot report: crossing one-packet theorem (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored). Coordinator verification and adopted posture:
FABLE_AUDIT.md alongside.

---

# Crossing lane — one complete packet theorem, mutation suite, contract requirements

## 0. Headline

The split-section inverse classification is **TRUE and provable at its smallest instance**, with an exact q-free cardinality, a closed-form template, a ceiling, and — verified exhaustively — it is the **unique maximiser** among all rank-one sections. So the replacement framing survives its first test (F1 not triggered).

It then **dies one step up**: at the very next section (w=2, agreement k+2) the analogous monomial word's exact shell is 30 at q=17, 9 at q=97, 7 at q>=241, 8 at q=81 — **q-dependent, certified exactly**. The q-independence of the packet is a w=1 phenomenon, and w=1 is by construction the bottom of the band (agreement k+1), which is why the packet prices at **zero** on the frontier ledger.

## 1. The theorem (PK1)

**Row (H0).** `F = F_q`, `n | q-1`, `beta` an n-th power in `F^*`, `H = {x : x^n = beta}` (n distinct nonzero points — the official multiplicative-coset shape, `Omega(Z) = Z^n - beta` as in the banked Toeplitz node), `1 <= k <= n-2`, `C = RS[F,H,k]`, `r := n-k-1 >= 1`, agreement `a = k+1`, so the section codimension is `w = a-k = 1`.

**Hypotheses.**
- **(H1) section structure (pure-product / rank-one window).** The received word `u` has interpolant `U == lambda(X^(n-1) + c X^k) mod C`, `lambda != 0`. Equivalently: its shell-(k+1) Toeplitz window `(u_(n-1),...,u_k)` is supported on its two extreme coordinates with `u_(n-1) != 0`. (Shells are invariant under `U -> lambda U + R`, `deg R < k` — (CT4) of `background/nodes/l1_exact_shell_complement_toeplitz_normal_form`; verified as IS3.)
- **(H2) affine target.** `c != 0`.
- **(H3) realizability.** `gamma := (-1)^(r+1) c` satisfies `gamma^n = beta^r`.
- **(H4) equidistribution guard.** `gcd(r, n) = 1`. *(At rate 1/2, `n = 2k`, this is exactly "k even"; it holds at the razor row `n = 2^41, k = 2^40`.)*
- The **exactness (gcd) guard** of (CT5) is **not** a hypothesis: it is automatic here (Lemma 4).

**Conclusions.**
- **(A) Ceiling.** No codeword agrees with `u` in `>= k+2` positions. *(Uses only H1-H2.)*
- **(B) Fence.** If instead `c = 0` — the same homogeneous Toeplitz row — no codeword agrees in `>= k+1` positions.
- **(C) Complete classification.** The exact shell at `k+1` is exactly the single packet `Pi(n,k,gamma) = { P_T : T subset H, |T| = r, prod_{x in T} x = gamma }`, and `T -> P_T` is a bijection onto it.
- **(D) Template.** `P_T = [ c X^k (M - X^r) + beta (M + c)/X ] / M`, where `M = prod_{x in T}(X - x)` (necessarily `M(0) = -c`). The division is exact and `deg P_T < k`.
- **(E) Exact q-free cardinality.** `|Pi| = C(n, r)/n` — independent of `q`, of `beta`, of `char F`, and of `gamma`.
- **(F) Complete shell census of the word.** `shell_(k+1) = C(n,r)/n`, `shell_k = C(n,k) - (k+1)C(n,r)/n`, all other shells `0`.
- **(G) Operational q-independence (index form).** Write `H = (x_0 omega^i)_{i in Z/n}`. The word with `c = (-1)^(r+1) x_0^r omega^s` has packet index family exactly `{ T subset Z/n : |T| = r, sum T == s (mod n) }` — **the same finite combinatorial family for every admissible `(q, beta, omega)`**.

"Bounded" means: **one** packet; descriptor `(row, template-id, s)` of `O(log q + log n)` bits. The packet's *cardinality* is astronomical — that is the point (it is a large fibre); what is bounded and q-free is the taxonomy, the template and the counting formula.

## 2. Proof

Notation: `M = sum_{j<=r} m_j X^j` monic, `Omega = X^n - beta`.

**Lemma 1 (locator normal form; = the banked (CT1)-(CT5), reproved self-contained).** For `k < a <= n`, `w = a-k`, `r' = n-a`, the codewords of exact agreement `a` are in bijection with monic `M | Omega`, `deg M = r'`, satisfying `[Z^d](U.M) = 0` for `d in [n-w, n-1]`, together with the exactness guard `gcd(Q_M, M) = 1`.
*Proof.* If `P` has agreement set `A`, disagreement `T = H\A`, put `M = prod_{x in T}(X-x)` (monic, splits, divides `Omega` since `Omega` is squarefree as `p does not divide n`). `(U-P)M` vanishes on all of `H`, so `(U-P)M = Omega.W` with `deg W <= r'-1`. Hence `MP = MU - Omega W`, of degree `<= r'+k-1 = n-1-w`. Writing `UM = sum_d c_d X^d` and reducing mod `Omega` (`X^(n+j) == beta X^j`), the reduced coefficients agree with `c_d` on `d in [r', n-1] superset [n-w, n-1]`, so the degree condition is exactly `c_d = 0` on the window. Conversely, given such an `M`: because `M | Omega`, `M` divides `S := UM mod Omega`, and the window conditions give `deg S <= r'+k-1`, so `P := S/M` has `deg P < k` and `(U-P)M == 0 mod Omega`, i.e. `U-P` vanishes off `T`; agreement is exactly `a` iff `U-P` has no root in `T`, i.e. `gcd(Q_M,M)=1` with `Q_M = (U-P)/(Omega/M) = W`. QED

**Lemma 2 (the rank-one row).** For `U = X^(n-1) + cX^k` and `deg M = r'`, `[Z^(n-1-i)](UM) = [i=0].m_0 + c.m_(r'+w-1-i)`.

**Lemma 3 (ceiling, conclusion A).** Let `a >= k+2`, so `w >= 2` and `r'+w-1 = n-k-1 > r'`. The `i=0` condition reads `m_0 + c.m_(r'+w-1) = m_0 = 0`. But `M | Omega` has all roots in `H subset F^*`, so `m_0 = +-prod(roots) != 0`. Contradiction; the section is empty, hence so is the shell. (The `i = w-1` condition independently reads `c.m_(r') = c != 0`.) QED

**Lemma 3' (fence, conclusion B).** For `c = 0` the only condition at any `w >= 1` is `m_0 = 0`, again impossible. So every shell above `k` is empty while the homogeneous functional is *identical* to the `c != 0` case. QED

**Lemma 4 (the exactness guard is automatic).** At `w=1`, the single condition is `m_0 = -c`. The quotient of `UM` by `Omega` is `W = (M - m_0)/X`. For any root `x in T`, `W(x) = (0 - m_0)/x = c/x != 0`. Hence `gcd(Q_M, M) = 1` always. QED

**Lemma 5 (subset-product level sets and equidistribution).** `m_0 = (-1)^r prod_{x in T} x`, so the condition is `prod T = (-1)^(r+1) c = gamma`. All r-subset products lie in `x_0^r mu_n = {y : y^n = beta^r}`, giving (H3) as the exact realizability criterion. If `gcd(r,n) = 1`, the `mu_n`-action `T -> omega T` multiplies the product by `omega^r`, and `omega -> omega^r` is an automorphism of `mu_n`, so the action is transitive on the target coset while the product map is equivariant: every fibre has cardinality `C(n,r)/n`. QED

**Assembly.** (C) is Lemmas 1+2+4+5; injectivity because `T` is recovered from `P` as its disagreement set. (D) is the explicit computation `MP = UM - Omega.W = cX^k(M - X^r) + beta(M - m_0)/X` with `m_0 = -c`. (E) is Lemma 5. (F): conservation `sum_b C(b,k).shell_b = C(n,k)` pins `shell_k`. (G) is Lemma 5 in index coordinates. QED

**Official-row corollary.** At `n = 2^41, k = 2^40`: `r = 2^40-1`, `gcd(r,n) = 1`, the theorem applies, `|Pi| = C(2^41, 2^40-1)/2^41`; the poly-size chain `C(n, n/2-1) >= 2^n/(2(n+1))` gives `log2|Pi| >= 2,199,023,255,467 >> 128` (chain verified exactly for all even `n in [6,218]`). The smallest rate-1/2 row where `|Pi| > 2^128` is `n = 140, k = 70`.

## 3. Scope theorem (PK2) — why it does not lift, and the q-dependence one step up

For a monomial window `{n-1, n-1-s}` at shell `a`, exactly **one** of the w conditions is a product condition; the other `w-1` are vanishing conditions on lower elementary symmetric functions of `T` — subset-**sum**-type. At `w = 2` (`U = X^(n-1) + cX^(k+1)`, agreement `k+2`, `r_2 = n-k-2`):

    exact shell at k+2 = { T : |T| = r_2, prod T = (-1)^(r_2+1) c, sum T = 0 }.

The `sum T = 0` clause is a vanishing sum of n-th roots of unity — characteristic-dependent (Lam-Leung structured solutions plus accidental ones). Measured exactly at `n=16, k=8, r_2=6`:

| q | 17 | 81 (char 3) | 97 | 113 | 193 | 353 | 577 | 241...977 (13 primes) |
|---|---|---|---|---|---|---|---|---|
| #{T : sum T = 0} | 472 | 120 | 136 | 72 | 72 | 72 | 72 | 56 |
| max exact shell at k+2 | 30 | 8 | 9 | 7 | 9 | 7 | 7 | 7 |

The structured floor `C(8,3) = 56` (three antipodal pairs) is present at every `q`; everything above it is accidental and q-dependent. Calibration: accidental solutions appear when `C(n,r)` is large relative to `q` — at official rows `C(n,r)/q ~ 2^(2^41-256)`, i.e. **the official regime is the q-dependent regime**; the small-q fixtures are simply the only exactly-certifiable witnesses of it.

Consequence: within the monomial-window family, a q-free packet exists only at `w = 1`, i.e. only at agreement `k+1`. Any frontier movement needs `w >= 2`.

## 4. The inverse direction

Exhaustive scan of **every** affine Toeplitz w=1 section at `n=8, k=4, r=3` (all `q^3` affine hyperplanes) at `q = 17, 41, 73` (IS1): max **gcd-guarded** fibre = `7 = C(n,r)/n`, attained by **exactly the 8 pure-product sections**; next attained guarded size is **5** (6 never occurs) — a clean spectral gap; the **raw** (unguarded) count reaches **21** (3x the true list). Two-support windows at `n=16` (IS2): only the constant-coefficient support reaches `715 = C(16,7)/16`, and it is the only q-free profile. The general-`n` inverse threshold is NOT proved (caveat 2).

## 5. Verification record

All under `tools/ramguard local -- python3` (inverse scan needs `RAMGUARD_TIMEOUT=25m`); exact arithmetic; JSON checkpoints.

| script | checks | result |
|---|---|---|
| `verify_packet_theorem.py` | 1002 | PK1_VERIFICATION_PASS |
| `verify_mutations.py` | 46 | MUTATION_SUITE_PASS |
| `verify_inverse_scan.py` | 17 | INVERSE_SCAN_PASS |

PK1 coverage (independent brute force, no use of the proof): `n=8,k=4`: all 8 `s`, both `beta`, over `F_17, F_41, F_73, F_89, F_97, F_113` AND extension fields `F_9, F_25, F_49` (three characteristics, non-prime included) — every row shells `{4: 35, 5: 7}` with ZERO slack; `n=16,k=8`: `{8: 6435, 9: 715}` over three fields; cross-field identity of index families recorded; official-row arithmetic verified.

## 6. Mutation suite

| # | mutation | exact witness | moral |
|---|---|---|---|
| **M1** | `c -> 0` (**the rank-one Toeplitz fence**) | identical homogeneous row; shell(k+1) jumps `C(n,r)/n -> 0` (`7->0`, `715->0`) | the fibre is a property of the affine position, never of the homogeneous map; a descriptor omitting the target collides fibres 0 and C(n,r)/n |
| **M2** | drop realizability | `q=17,c=3` etc.: shell(k+1) = 0 | packet empty unless the target lies in the product coset; one-exponentiation test |
| **M3** | drop `gcd(r,n)=1` | `n=10,k=5` (`gcd=2`), 6 primes: shell alternates `22,20,...`; formula `21` NEVER attained | the single cardinality formula dies (splits into gcd classes); q-independence itself survives; ceiling unaffected |
| **M4** | `w = 1 -> 2` | 20 fields: shell at `k+2` = `30/9/8/7` by field; control: w=1 fibre = 715 at every one | **the packet bound is q-dependent one step up** |
| **M5** | drop splitness | `q=17,n=8`: affine section has 289 points, exactly 7 split; exact division precisely there | a section is not a fibre (41x inflation); no rank/profile proxy computes the packet (the retired PE-envelope fence, re-certified) |
| **M6** | drop exactness guard (at `w=0`) | unguarded section = all 70; guard fails on exactly 35; failure <=> agreement > k (0 mismatches) | sections count subsets, packets count codewords |
| **M7** | per-shell vs threshold | shells 35 + 7, threshold 42 | per-shell caps do not compose (the audit's 35+7=42, live) |
| **M8** | same-word trap (F_17 witness) | agreements 12/11/11 reproduced; census `{8:7995, 9:420, 10:6, 11:2, 12:1}`; window NOT pure-product | the traps live outside the classified word class, at the Johnson anchor |
| **M9** | generic window | `U = X^7+X^6+X^4`: shell sizes `2,2,0,0,0,0` across q; index families DIFFER between q=17 and q=41 | **succinctness killer**: no template exists for generic sections; certificate must enumerate |

## 7. Contract requirements (for the coordinator's draft)

**SAFE half (`a = k+2`, list = 0):** descriptor `(q, beta, n, k)` + word-class `(window support, lambda, c)`; certificate size `O(log q + log n)`; verifier O(1) field ops (support pattern + `c != 0` + PK1(A)). Shells are invariant mod C, so certify the class `[U]`, never the low part R.

**UNSAFE half (`a = k+1`, list = C(n,r)/n > B*):** descriptors + packet index `s` + a SYMBOLIC count `C(n,r)/n` + a poly-size derivation of `count > B*`. Verifier: `gcd(r,n) = 1`; one exponentiation for realizability; the count-vs-budget comparison WITHOUT expanding the binomial (at the razor row the count has ~2^41 bits — the contract must admit a counted-object primitive with a checkable inequality chain). Optional one-member spot check through the template in `poly(n, log q)`.

**Must be forbidden by the succinctness clause (all brute-force):** enumerating received words (`q^n`), the fibre (`2^n`), split divisors (`C(n,r)`), member-by-member guard discharge (must come from a theorem, as in Lemma 4), any per-shell claim without a ceiling or compatibility theorem.

**Raw vs guarded must be pinned:** the certified quantity is the guarded/first-owner exact-shell count (raw over-reports 21 vs 7 at n=8).

**Operational q-independence must be defined as:** the packet's INDEX FAMILY (subsets of Z/n) and cardinality formula depend only on `(n, k, template-id, s)`; testable by replaying the family in two characteristics. A packet with merely equal cardinalities whose members move with q fails (M9) and is not succinctly certifiable.

**B* = 0 scope pin:** PK1's safe clause holds verbatim at B* = 0; the unsafe clause holds for every B* < 2^128 once n >= 140 at rate 1/2 — a budget-uniform same-word calibration instance for the pin, no separate branch needed.

**Descriptor-collision kill line:** the descriptor must include the affine target (M1).

## 8. Pre-registered falsifier verdicts

- **F1 (q-dependent at the smallest instance) — NOT TRIGGERED** (9 fields, 4 characteristics, identical index families).
- **F2 (necessarily non-succinct) — NOT TRIGGERED, with a mandatory clause** (symbolic counts + inequality derivations must be admissible; generic sections have no template at all — succinctness is a property of the packet CLASS).
- **F3 (traps evade) — NOT TRIGGERED within scope** (the classification is exhaustive for its word class; the traps live outside it; PK1 covers ~q^k(q-1).n of q^n words).
- **NEW F1' (q-dependence at the NEXT instance) — TRIGGERED**: the w=2 shell differs across certified fields. The q-free packet is a codimension-one product-section feature, existing only at agreement k+1.

## 9. Frontier accounting and subtraction (hard law 5)

- **Frontier movement: ZERO.** The packet sits at agreement `k+1`, far below the banked unsafe frontier; U(q), S(q) unchanged (single-word statement).
- **The lower-bound half of PK1 is NOT new**: it is the `d=1` pigeonhole of `critical/nodes/rate_half_cyclic_rotated_prefix_floor` pushed to the boundary `c=1, s=0` its own hypothesis excludes — and that boundary is upstream (holmbuar #1101 Thm 2.1/4.1 per the literature map). Dominated on the ledger by the floor.
- **What IS new:** the upper half — exactness (equality vs pigeonhole), the CEILING (nothing above k+1 — a safe-side same-word statement the floor family cannot produce), the automatic exactness guard, the injective closed-form template, the q-free index family; plus PK2 and the exhaustive inverse maximality. Adjacent in-tree object checked and distinct: `pma_exact_periodic_owner`.

## 10. File inventory

`packet_lib.py` (367) . `verify_packet_theorem.py` (300, 1002 checks) . `verify_mutations.py` (513, 46 checks) . `verify_inverse_scan.py` (276, 17 checks) . `checkpoints/{packet_theorem,mutations,inverse_scan}.json`. Replay: `tools/ramguard local -- python3 <script>` (inverse scan: `RAMGUARD_TIMEOUT=25m`).

## 11. Honest caveats

1. PK1 is a single-word theorem (bounds L(u,.) for one word class, never max over words); moves neither frontier.
2. The inverse classification is proved exhaustively only at n=8 (+ two-support windows at n=16); the general-n inverse threshold is conjectural (an inverse theorem for character sums over split-divisor sets, not attempted).
3. The w=2 q-dependence is certified at small q; the official-regime claim rests on the counting heuristic C(n,r)/q ~ 2^(2^41-256), flagged as such. What IS exact: no q-free formula can give the w=2 count (it differs across certified fields).
4. Field scope: split multiplicative-coset domains only (the official shape); prime fields + F_9, F_25, F_49, F_81.
5. PK1 (A)/(B) do not need the gcd guard; only the cardinality (E) does — stated separately so the contract does not over-hypothesize the safe clause.
6. The contract draft itself is out of scope here; section 7 is requirements only.
