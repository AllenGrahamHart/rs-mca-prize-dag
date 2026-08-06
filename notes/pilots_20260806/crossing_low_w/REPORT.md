(Coordinator-persisted verbatim from the pilot's final message, 2026-08-06.)

# ROUND 18 — the LOW-w CROSSING CORE: the deep stratum is where (ES) DIES, not where it is saved

**Verdict in one line: the brief's lift-constraint conjecture is FALSE for a structural reason — at the binding (deepest) stratum there are NO lift constraints at all — and following that refutation up gives THEOREM DSA, an unconditional pigeonhole proof that the (ES) crossing instance is FALSE at 10 of the 19 admissible (class,e) pairs outright, with an explicit verified witness at n = 2^41; the recorded prime rows survive and are re-priced from a 0.089-bit failure to a 53–61 bit margin by a new functional (3^L, not 2^{n_a} and not C(n_a,r'_a)).**

## 0. What was run

All from `/home/u2470931/smooth-read-solomin/prize` under the ramguard law (`local` profile; note `tiny`'s 256M cannot even import numpy). Files, all inside my dir, nothing else touched (`find` confirms **0** files modified outside it), no commits:

- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/crossing_low_w/PREREG.md` — coordinator brief + my registrations **X0–X9, appended before any computation**
- `.../crossing_low_w/PROOFS.md` — the derivations, verbatim `file:line` for every statement relied on
- `.../crossing_low_w/low_w_lib.py` — exact machinery (char-0 arithmetic in `Z[X]/(X^h+1)`, `F_p` roots of unity, strata, the ternary collapse)
- `.../crossing_low_w/toy_gate.py` — stages `strat / biject / fibre / accident / census / oddeven / orbit`
- `.../crossing_low_w/prize_exhibit.py` — stages `row / search / verify / coverage / wcover`
- `.../crossing_low_w/eps_found.json` — the witness; `.../toy_*.out`, `.../prize_*.out` — outputs

**1,565,906 checks, 0 failures**, every stage exit 0. Fail-closed proven, not asserted: both `failclosed` stages inject a false check and exit 1.

## 1. (G1) THE w' = 2 PRINCIPAL QUESTION, STATED EXACTLY — LEMMA DS

> **LEMMA DS.** `n = 2^41`, `w = 2^v`, `r' = 2^40 − w`, `a = v−1`, `n_a = 2^{42−v}`, `L = n_a/2 = 2^{41−v}`. Then `r'_a = r'/2^a = L − 2` (uniformly in `v`), the surviving condition set is the single index `t = 1`, and
> ```
> {S ∈ W_w : strat(S) ≥ v−1}  ↔  {S' ⊆ Z/2L : |S'| = L−2, p_1(S') = 0}
> ```
> is a bijection **with no side condition**. `S` is structural iff `S'` is a union of antipodal pairs `{j, j+L}`.

At `v = 34` this is the brief's instance: `(n_a, r'_a, L) = (256, 126, 128)`, structural family `C(128,63) = 2^124.149`.

So, answering the mandate literally: the **admissible members** at the reduced instance are all `S' ⊆ Z/256` of size 126; the **structural family** there is the antipodal-pair unions (LEMMA Z at `t = 1`); and **"no accidents"** means: *every* `S'` of size 126 with `Σ_{j∈S'} θ^j = 0` in `F_{p^{δ_a}}` is an antipodal-pair union. The obligation is **not** coprimality — it is the transported count statement, and LEMMA STRAT's "the reduced ideal is principal" is exactly the statement that this obligation is one equation, not a system.

The balance frame is not used anywhere in this section (PREREG F5 self-check, §7 of PROOFS.md).

## 2. (G2) THE n_a = 256 INSTANCE — the brief's conjecture is REFUTED, and I registered that refutation in advance

**LEMMA FREE.** *At the deepest stratum the number of surviving lift constraints is **0**.* The only `s ∈ [1, w−1]` divisible by `2^{v−1}` is `s = 2^{v−1}` itself, which **is** the reduced condition; every other `s` is killed identically by LEMMA STRAT (1), independently of `S'`. So every non-structural reduced solution lifts, freely.

*Gate (mandatory, passed before any prize claim):* `toy_gate.py biject`, **81,005 checks, 0 failures**, at all three mandated shapes `(n,n_a) = (32,8), (64,8), (64,16)`. Membership of the lift in `W_w` — decided by **direct evaluation of all `w−1` conditions, no lemma used** — is identical to `p_1(S') = 0` in every one of the ~40,000 cases. At `(64,16)`, `p = 193`: 72 members = 72 reduced solutions vs 56 structural, i.e. **16 non-structural members**, each verified against all 7 conditions and confirmed to fail in char 0.

**Where the brief's intuition IS right — LEMMA OE (new).** With `ε_j = [j∈S'] − [j+L∈S']` and `σ_j = [j∈S'] + [j+L∈S']`:
```
p_t(S') = Σ_j ε_j θ^{tj}            (t ODD)
p_t(S') = Σ_j σ_j (θ²)^{(t/2)j}     (t EVEN)
```
ODD conditions see only `ε`; EVEN conditions see only `σ` and are literally the next stratum's conditions. The brief's "un-collapsed even-index conditions" is a **real mechanism at every shallower stratum — and vacuous exactly at the one that binds**, because the deepest stratum has a single, odd, condition. (Verified: `oddeven`, **1,108,832 checks, 0 failures**, exhaustive over all `2^8` and all `2^16` subsets.)

**LEMMA TC — the corrected pricing.** The condition depends on `S'` only through `ε ∈ {0,±1}^L`, with fibres `C(L−U, (r'_a−U)/2)` summing to `C(2L, r'_a)` (verified exhaustively at `L = 4,8,10` for every `r'_a`, and in closed form to `L = 128`). Hence the primitive object is `ε`, of which there are `3^L` — **not** `2^{n_a}` (global) and **not** `C(n_a,r'_a)` (per-weight):

| functional | requirement on `log2 p` at `v=34` |
|---|---|
| GLOBAL (ES-G) | **256** — fails by the width of the admissible sliver |
| PER-WEIGHT (retired) | **251.628** |
| **TERNARY (this pilot)** | **202.875** |
| TERNARY, orbit-corrected | **194.875** |

**The per-weight functional mis-prices this stratum by 48.75 bits**, because it counts fibred objects as independent.

## 3. (G4) THE CATCH — THEOREM DSA: accidents provably EXIST, with a verified prize-row witness

> **THEOREM DSA (unconditional, no balance).** If `p^{δ_a} < 2^{L−2}` then there is `ε ∈ {0,±1}^L`, `ε ≠ 0`, with `Σ_j ε_j θ^j = 0`, `U(ε)` even, `2 ≤ U ≤ r'_a`; hence `W_w` contains a **non-structural** member and `|W_w| > C(n/M, r'/M)` — **(ES) is FALSE at that row.**

*Proof:* pigeonhole the `2^{L−2}` vectors `a ∈ {0,1}^L` with `a_{L−1}=0` and `|a|` even into `F_{p^{δ_a}}`; a collision gives `ε = a−b`, whose support is a symmetric difference of two even-weight sets, hence even, and `≤ L−2`. Pure `|domain| > |codomain|` — no balance functional appears.

**The witness.** Row taken verbatim from `es_g_lanes/PROOFS.md:174-179`, already certified there as satisfying *"every rules-freeze constraint"*, and re-derived independently here (`p` prime by deterministic Miller–Rabin, `δ=1`, `q<2^256`, `2^41|q−1`, `B*≥3`, `w≤p`, `δ_a=1`):
```
p = 6597069766657 = 3·2^41+1,  e = 6,  q = p^6,  log2 q = 255.509775,  log2 B* = 127.510
log2 p = 42.585 < 126 = L−2   →  THEOREM DSA applies
ε  (U = 20, even):  support [0,2,3,4,5,9,10,11,12,13,14,17,19,21,23,24,25,26,27,29]
                    signs   [-1,-1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,1,-1,-1,1,-1,1]
```
`prize_exhibit.py verify` — **2854 checks, 0 failures** — establishes at `n = 2^41` itself: `|S'| = 126` with `p_1(S') = 0` by **direct summation over all 126 elements**; `S'` not an antipodal-pair union; `|S| = 2^33·126 = 1082331758592 = 2^40 − 2^34 = r'` exactly; `x_{2^33}(S) = 0`; and `x_s(S) = 0` for **every** other `s ∈ [1, 2^34−1]` via `x_s(S) = (Σ_{j∈S'} ζ^{sj})·G(s)` with `G(s) = Π_{i=0}^{32}(1+η^{s·2^i}) = 0` (the factor at `i = 32−v_2(s)` is `1+(−1)`) — verified on 1320 sampled `s` across all 33 valuation classes, with the product formula cross-checked against brute summation and the factorisation re-verified exhaustively at `n = 64, 128`.

```
|W_{2^34}| ≥ C(128,63) + C(108,53) = 2^124.149 + 24405824773509487458170913508896  >  C(128,63)
```

**Coverage of the refutation** (`coverage`, 19 pairs reproduced from scratch): **ALL = 10 pairs, PART = 6, NONE = 3**. And the dichotomy is clean:

> **`e = 1` rows are NEVER in the provable regime**: `B* ≥ 3` forces `q = p ≥ 3·2^128`, i.e. `log2 p ≥ 129.585 > 126`.

THEOREM DSA kills **tower rows only** — exactly the rows `es_g_lanes/REPORT.md:184` named *"the adversary's best choice against (ES-G)"* — and leaves the recorded prime rows untouched. Per the brief's G4 instruction ("report witness + reproduction script, stop"), I stopped here.

## 4. (G3) THE REFINED SPLIT

CS already makes `w > 2^37.3131` unconditional. At the **binding** stratum, over the 19 admissible `(class,e)` pairs:

```
   w      PROVED-ACCIDENT     EXPECTED-ACCIDENT    EXPECTED-CLEAN
   2^34   10 full +  6 part   16 full + 3 part      0 full
   2^35    3 full +  5 part   10 full + 6 part      3 full
   2^36    0 full +  0 part    2 full + 6 part     11 full
   2^37    0 full +  0 part    0 full + 0 part     19 full
```

**Exact remaining set:** (1) `w = 2^34` — (ES) REFUTED on 10 pairs outright + part of 6; only the `e=1` sub-range `log2 p > 202.875` is expected clean, which is where the recorded rows sit. (2) `w = 2^35` — REFUTED on 3 pairs + part of 5. (3) `w = 2^36` — nothing proved; heuristic accident zone at `log2 p < 50.719`. (4) `w = 2^37` — deep stratum expected clean everywhere, **no proof**. (5) **Strata `a < v−1`, including `a = 0`, are untouched by all of this.**

**The prime rows, re-priced (HEURISTIC, labelled as such):** at `log2 p ≈ 256` the expected relation count is `3^128/p = 2^{−53.1}`, orbit-corrected `2^{−61.1}`. This replaces a **0.089-bit failure** of the global functional with a **53–61 bit margin**, on a strictly better-founded count than the retired per-weight form (4.37 bits).

## 5. CATCHES

- **CATCH-18A (the campaign-critical one).** The (ES) crossing instance is **FALSE at admissible tower rows** — proved unconditionally by pigeonhole and exhibited explicitly at `n = 2^41`. The deep stratum is not empty "for a reason invisible to balance"; it is **full**, and balance was right to fail there. Round-17's `es_g_lanes` P4 ("no admissible row clears the deep-stratum requirement, 19/19") was not a pricing artefact — it was detecting a real refutation.
- **CATCH-18B.** The brief's lift-constraint conjecture is false **structurally**: the deepest stratum has exactly one condition, it is odd, and LEMMA OE shows odd conditions constrain only `ε` while even conditions constrain only `σ`. The "un-collapsed even-index conditions" mechanism is real but **vacuous precisely at the binding stratum**.
- **CATCH-18C.** The retired per-weight functional **mis-prices the deep stratum by 48.75 bits** (251.628 vs 202.875) by counting fibred solutions as independent. Both banked functionals are wrong here in the same way; the correct primitive count is `3^L`.
- **CATCH-18D (LEMMA ROT).** Relations are closed under `ε → −ε` and a twisted rotation of order `2L`, so they come in orbits of size `2L` and are **massively over-dispersed**. Measured at the toy: naive counting predicts 44.1 relations across five primes, orbit-corrected predicts 2.76, **observed exactly 2 orbits** (16-or-0 at each prime). Any Poisson-style accident estimate on this object over-predicts by the factor `2L`.
- **CATCH-18E (against my own script, self-caught, load-bearing).** My first prize-scale search used a 24-index birthday window predicting ~5.3 collisions and found **0 in six windows**. The prediction, not the code, was wrong — collisions in an `m`-window are clustered (`2^{m−U}` pairs per vanishing `ε`), so the count of *distinct* relations is `3^m/p = 0.043` at `m=24`. The toy had already shown this and I did not read it. THEOREM DSA is unaffected (it uses all 128 coordinates); only the search was resized (`3^30`, 31.2 predicted, 49 observed). Reported rather than repaired silently.
- **`r'_a = L − 2` uniformly in `v`** — the deep-stratum family is a single one-parameter family `(2L, L−2)`, `L = 2^{41−v}`, not six unrelated instances.
- **Minor.** `es_g_lanes/REPORT.md:105`'s `log2 S(2^34) = 117.149` is the per-sig-class shell; the structural count itself is `log2 C(128,63) = 124.149`, exactly `log2 128` larger. Not load-bearing there, but the two should not be interchanged.

## 6. HONEST RESIDUALS

- **Emptiness at prime rows is NOT proved.** §5 of PROOFS.md is a counting heuristic and is labelled so throughout. I did not close the low-`w` core; I moved the binding obstruction and refuted a large part of the row space.
- **The refutation's scope depends on the campaign's own adopted reading** that tower rows are in the crossing lane's obligation (`axis8_generating` PROVED + `es_g_lanes` FABLE_AUDIT adoption + `B* ≥ 3`). If the official family were later shown to exclude towers, CATCH-18A shrinks to nothing and only the re-pricing (CATCH-18C/D) survives.
- **Strata `a < v−1`, including `a = 0`, are untouched.** LEMMA OE gives the recursive structure to do them; I did not carry it out.
- **The sig/γ shell is not addressed.** The crossing count of record is `X_w(γ) = #{S ∈ W_w : ∏T(S) = γ}`. I refute the (ES) statement about `|W_w|` and computed `sig(S) = 1941325217792` for the witness, but did **not** determine which γ-shells the accidents populate, nor the consequence for `L_1`.
- **`δ_a = 2` rows** are handled only by the crude `p^{δ_a} < 2^{L−2}`; a Frobenius-adapted pigeonhole would cover more (this is why 3 pairs are NONE).
- **`w = 2^36, 2^37`** deep strata are expected clean but unproven; `w = 2^36` has an unexplained heuristic accident zone at `log2 p < 50.719`.
- **AK-UNIT: PASSES.** My conclusions are existence of an individual `S` and the inequality `|W_w| > C(n/M, r'/M)` — never a congruence on a count.
- **No balance smuggling (F5): PASSES.** THEOREM DSA is pigeonhole only. The ternary functional is a counting functional and appears exclusively in the explicitly heuristic columns.
- **Toy scale is `n ∈ {32,64,128}`**; the prize statements are consequences of lemmas proved for all `n`, and the witness is verified at `n = 2^41` itself, not extrapolated.
- **One registered prediction was refuted by my own measurement** (the birthday sizing, CATCH-18E); the four substantive registrations X0–X4 all held.
