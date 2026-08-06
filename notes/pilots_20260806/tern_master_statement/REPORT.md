(Coordinator-persisted verbatim from the pilot's final message, 2026-08-06.)

Clean re-run reproduces 92,263 checks / 0 FAIL exactly, failclosed exits 1. Reporting.

---

# THE TERNARY MASTER STATEMENT — round 19 pilot report

**Bottom line: the unification is real, it is exactly specifiable, and it pays twice — once with a new instrument at I3, once by collapsing three banked thresholds into one inequality. It closes nothing.**

Machine checks: **92,263 checks, 0 FAIL**, all seven stages exit 0, `failclosed` exits 1 by construction. Exact integer / finite-field arithmetic, Python stdlib only, no floating point in any proved statement. All execution via `tools/ramguard tiny|local -- python3`; no bare `python3` at any point, including file patching.

## M1 — THE MASTER OBJECT: **PASS, with two reported non-specializations**

`T(P,Λ) := {ε ∈ {0,±1}^M : Σ_j ε_j θ_j^l = 0 ∀ l ∈ Λ}`, target carried as a **weight parameter** ω (existence / count / mass), never conflated — per CATCH-Z1.

**PROPOSITION HS (proved):** for `P` = the half-system `(ξ^j)_{j&lt;h}` of `μ_n`, `n=2h`, and `Λ ⊆ (Z/n)*`: `T(P,Λ) = T(P,Λ*)` with `Λ* = ⟨p⟩Λ`, and `T` is exactly **the ternary words of the negacyclic F_p-code of length h with defining set Λ\*, of codimension g = |Λ\*|**. That single sentence is the master object.

Dictionaries (all exact): **I1** = `(h=S=2^{e_p−1}, Λ={1,3,…,2R−1}, g=R, ω=2^{−U})`; **I2** deep stratum = `(h=L=n/w, Λ={1}, g=δ_a, ω=C(L−U,(r'_a−U)/2))`; **I3** = `(h=n/2, Λ={odd s ≤ w−1}, g=|Z_w^odd|, ω=2^{h−U})`.

Two failures reported rather than forced, exactly as pre-registered:
- **I2's EXISTENCE reading does not specialize.** DSA needs `U` even and `U ≤ r'_a` — not conditions on `T`. Only the *mass* reading specializes (the LEMMA TC weight is 0 unless they hold).
- **I3 specializes only onto its ODD-condition sub-object.** By LEMMA OE the even conditions live on `σ ∈ {0,1,2}^h` — a different instance at half length over a larger alphabet. Every banked I3 instrument (SP-COVER, SP-TERNARY, LEMMA AB) uses only odd conditions, so the master object covers the whole instrument set but **not** the predicate `p | N(I_S)`. This is CATCH E-2's self-similarity with the recursion named; the "+1" instance is the recursion itself.

## M2 — THE SHARED SPINE: **all four proved**

**(i) CZ-M (char-0 emptiness).** `T` = the ternary vectors of the lattice `Φ_n·Z[X]_{&lt;N−φ(n)}`; `T={0}` **iff N=φ(n) iff n is a 2-power**, for *all* integer coefficients, needing only one unit in Λ. The 2-power half is the banked Z-basis argument (cited). New: the complement — this is the **exact master form of CATCH-Z6**, upgrading a grid rule to a rank statement with a closed count `3^{N−φ(n)}−1`. Reproduces CATCH-Z6's banked 8 / 8 / 80 exactly.

**(ii) CS-M — yes, CS reads VERBATIM**, for *any* Frobenius-stable `Λ ⊆ (Z/n)*`, with `|Z_w^odd| → |Λ*|` and `(r'−a_{n/2}(S)) → wt(ε)`. **No window or consecutivity hypothesis is needed.** The three real hypotheses: `P` a half-system (used twice — nonzero char-0 lift, and `j−j'=h` impossible in the second moment), `Λ` ⊆ units (even `l` have no `σ_l`; they *are* the next stratum), `n` a 2-power. The hinge is **LEMMA BR: `r' − a_{n/2}(S) = wt(A−B)` exactly** — CS2's archimedean quantity *is* the ternary support size. Verified exhaustively (65,536 subsets at n=16) plus 4,000 at n=32. CS-M itself: 30 cells, 11,752 checks, 0 fail, and **sharp — tightest margin 0.0000 bits in 18 cells**. The archimedean half is banked in the DLI lane and is cited, not claimed.

**(iii) ROT-M.** `T` stable under `−1`, the negacyclic shift `R` of order `n`, and the dilates `D_m` for `m ∈ Stab(Λ*) ⊇ ⟨p⟩`. Contains LEMMA ROT as the case `Λ={1}`. 4,057 checks, every orbit size divides `n`.

**(iv) Z-FLOOR-M, with its exact scope.** Holds for **any** finite `X ⊆ Z^M` and **any** map. With `X={0,…,k−1}^M` it floors the mass whose weight is the **difference multiplicity** `Π_j(k−|ε_j|)`; ternary is `k=2`. So it is alphabet-agnostic in precisely that sense and **not weight-agnostic** — it says nothing about I2's constant-weight crossing weight. That is the exact boundary, and the value test stays inside it.

## M3 — INSTRUMENT MATRIX: **19 instruments, each with a verdict**

MASTER: Z-FLOOR, LEMMA Z/char-0 (as CZ-M), CS, LEMMA AB (= HS + BR), SP-COVER (`g=h ⟹ T={0}`), LEMMA COS/SP-UNIFORM, SP-TERNARY, LEMMA ROT, LEMMA OE (the alphabet recursion), LEMMA TWO, Z-1 and Z-2 (**prefix-only**). SUBSUMED: DSA — Z-FLOOR-M gives a *count* where DSA gives existence. INSTANCE-ONLY with named obstruction: LEMMA TC (it *is* the weight, a constant-weight fibre, not a statement about `T`), LEMMA STRAT/DS/FREE (statements about 0/1 sets upstream of `T`), Z-NOGO. CITED: the DLI AM-GM ceiling; SPD (banked vacuous).

## M4 — THE VALUE TEST: **PAYS TWICE; two honest zeros**

**(a) PAYS — THEOREM I3-FORCE.** If `|Z_w^odd|·log₂p &lt; n/2` then `C_odd` contains a nonzero ternary vector, hence a `strat=0` set meeting every odd window condition — so **SP-COVER and SP-TERNARY, the entire odd-condition exclusion mechanism, provably cannot exclude there.** This is the *first existence/forcing instrument on the (ES) object*, which had only exclusion instruments and a banked-dead Ax–Katz route. At `n=2^41, w=2^34` it fires on every `δ=1` admissible row with `log₂p &lt; 128` — the tower rows, never the `e=1` rows, reproducing the banked dichotomy. It **strengthens CATCH E-3 from "SP-COVER is vacuous" to "SP-COVER provably fails, on a named row set."** Verified: fires in 16 cells, a codeword present in every one, **0 falsifications** of the pre-registered killer P4. *Scope stated plainly: this is a no-go on a METHOD, not a refutation — it produces no bad set and does not touch `p | N(I_S)`.*

**(b) PAYS — THEOREM MT, the master threshold.** One quantity, `g·log₂p` vs `h`, governs `T`: below `h` existence is forced with `|T| ≥ 2^h/p^g`; at `g=h` the module is trivial; and any nonzero `ε` has `wt ≥ p^{2g/h}`. **The three banked thresholds are this one inequality:**
- **I1:** `h − g·log₂p = −46.0249` bits at `R=4,294,967,340` and `+17.9751` at `R−1` — the banked knife-edge constants reproduced **to four decimals** from the master threshold alone. And `h/g = 63.999999344 = log₂p`: I1's saturation `R/S = 1/log₂p` says precisely that **the F2 object sits ON the threshold**.
- **I2:** `h/g = n/w = L` at the deep stratum vs DSA's `p^{δ_a} &lt; 2^{L−2}` — the same inequality to within 2, at all six `w`.
- **I3:** stratum 0 has `h/g = n/w = L` — **the same number as the deep stratum**, two strata the banked work treats by unrelated arguments at unrelated lengths.

The banked four-face seam (CATCH-Z3 / `f2_o1_status_split`) is entirely F2-internal; MT adds two lanes. **COROLLARY MX:** in the forcing regime CS can only prove `wt &lt; 4` — the norm mechanism and the pigeonhole mechanism are *never* simultaneously informative, which is why route (a) is dead at I1 structurally rather than numerically.

**(c) ZERO — SP-COVER at I1.** Vacuous, by exactly the factor `log₂p ≥ 39` (coverage needs `R ≥ S`; the object has `R/S = 1/log₂p`). Quantified zero, as pre-registered.

**(d) ZERO — CS at I1.** Transfers cleanly, gives `wt ≥ p^{4R/n} = 4.0000` against the banked `2.0000`; both annihilated by Z-1's `2R+1 = 8.6e9`. **The transfer pays nothing** — but it exposes a wrong constant of record (below).

**(e) ZERO — Z-1 at I3.** Transports (prefix-only), gives `U ≥ w` for `strat=0` bad sets — `2^30` stronger than CS at `w=2^34` — but a *lower* bound on `U` weakens CS-EXCL rather than helping, and the census bound is vacuous at prize scale.

## M5 — NODE DRAFT: delivered

`NODE_DRAFT.md` (proposed id `tern_master_threshold`), with proved/per-instance/open scope explicitly separated. **DRAFT ONLY — the coordinator mints.**

## CATCHES

- **CATCH-T1** the master threshold (three lanes, one inequality).
- **CATCH-T2** `r'−a_{n/2}(S) = wt(A−B)`. `PROPOSITION TAUT` uses CS3 with LEMMA AB live and still discards the quantity as `≤ r'`.
- **CATCH-T3 — a wrong constant of record, against a banked statement and a minted node.** `f2_sl1_powersums/PROOFS.md:271` uses `|N(α)| ≤ w^{n/2}`; the banked sharp ceiling (`dli_c1_ternary_relation_norm_sandwich/statement.md:27-28`) is `w^{N/2}` with `N=n/2`, i.e. `w^{n/4}` — **the square root**. So the recorded dead-route constant `w ≥ p^{2R/n} = 2.0000` should read `p^{4R/n} = 4.0000`, propagating into the minted `f2_z1_mass_knife_edge/statement.md:59-61`. **No verdict changes** (dead either way); two banked statements had simply never been placed side by side.
- **CATCH-T4 — citation drift.** `z1_ternary_mass/PROOFS.md:56-59` and `:383` cite the norm route as `f2_sl1_powersums/PROOFS.md:262-266`; it is at `:271-274` (262-266 is the Z-basis paragraph).
- **CATCH-T5** CATCH-Z6 has a closed form: rank `N−φ(n)`, count `3^{N−φ(n)}−1`.
- **CATCH-T6** complementarity (MX).
- **CATCH-T7** I2's existence reading does not specialize.

## HONEST RESIDUALS AND MISSES

1. **Nothing is closed.** The I1 mass bound `Z_1 ≤ 2^{o(m)}` at `k=e`, the I2/I3 mid-range primes, and CC-sparsity are all untouched. The master statement reorganizes and transports; it resolves no open question.
2. **REGISTERED EXPECTATION MISSED (reported, not buried).** I predicted shifted-Λ counterexamples to the `2ℓ+1` law and found **zero**. My grid is 2-power `n` only; the banked record notes exactly 1 of its 43 shifted counterexamples is at 2-power `2N` ("a thin sample"). So my grid cannot see the scope failure and **I do not get to claim the prefix hypothesis is load-bearing at 2-power orders** — open at master level, exactly as at I1.
3. **Blind convergence, credited not claimed.** The one-framework object *and* the mass/census functional identity are independently pre-registered by the live sibling `tern_small_scale_laws` (its D3, `Sct = 2^N(Z−1)`). I claim neither as novel. The subtraction sweep is what caught this.
4. **The AM-GM ternary ceiling is banked in the DLI lane** — CS-M's archimedean half is cited, not mine.
5. I3's specialization is partial (odd conditions only); the recursion is named but not carried out. `δ&gt;1` rows at I3 and the `δ_a&gt;1` orbit refinement are uncovered. All checks are `n ∈ {8,16,32}` against official `n = 2^39–2^41`; CS-M/CZ-M/ROT-M/Z-FLOOR-M are proved for all `n` and only *verified* at toy scale.
6. **Disclosure:** I ran one `ls` of `tern_unification_adversary/` to confirm write-isolation; I read none of its files and its contents played no part in this work.

**Files** (all writes confined to my directory; no commit, no push, no node/dag/tools edit): `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/tern_master_statement/{PREREG.md, PROOFS.md, NODE_DRAFT.md, check.py, tern_lib.py, VERIFY_LOG.txt, *.out}`

result: Ternary master statement built and verified (92,263 checks, 0 FAIL): T(P,Λ) = ternary words of a negacyclic code, all three round-18 instances specialize exactly (two reported partials), spine proved (CZ-M/CS-M/ROT-M/Z-FLOOR-M), and the value test PAYS TWICE — a first existence instrument at I3 that proves SP-COVER/SP-TERNARY must fail on named tower rows, and THEOREM MT collapsing I1's knife edge, I2's DSA boundary and I3's stratum-0 boundary into one inequality g·log₂p vs h (reproducing the banked −46.0249/+17.9751 to four decimals); 7 catches including a wrong banked constant (2.0000 should be 4.0000); nothing closed.
