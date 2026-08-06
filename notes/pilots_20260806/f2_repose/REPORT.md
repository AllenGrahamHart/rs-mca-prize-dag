(Coordinator-persisted verbatim from the pilot's final message, 2026-08-06.)

All 60 checks pass, citations verified, writes confined to the pilot dir, no commit. Report follows.

---

# PILOT REPORT — THE F2 RE-POSE (mystery 2, round 20, `f2_repose`)

**Opus 5, 2026-08-06.** Replay: `tools/ramguard local -- python3 notes/pilots_20260806/f2_repose/verify.py` → **60 checks, 0 FAIL**, digest `F2_REPOSE_ALL_PASS`. Artifacts (all inside the pilot dir): `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/f2_repose/{PREREG.md (brief + my appendix B1–B7), PROOFS.md, verify.py, VERIFY_LOG.txt}`.

## HEADLINE

**I pre-registered that (O1) was over-posed relative to its consumer. It is the opposite: (O1) is UNDER-posed, and the consumer's tolerance is the fifth face of the same one inequality the whole lane already sits on.** Tracing the chain down to `u2c`'s "extras ≤ n³ = 2^123" and multiplying back up by `q^t`, the consumer's tolerance is **`log2 TOL(b) = 3 log2 N + t·L − log2 C(N,b)`** — i.e. *the counting-balance surplus `t·L − N`*, up to `O(log N)`. My formula reproduces the banked `2^{1.05e12}` to **0.047%** from the consumer's own sentence. The four-face seam (`f2_o1_status_split:61-65`) therefore has a **fifth face: the consumer's own budget**, and the campaign has it pinned at zero.

Then the arithmetic collapses beautifully. At the balance with the extension reading, `log2|K1| = t·L/2 = N/2 = m`, so **`|K1|·2^m = 4^m` exactly**, and Lemma 1's punctured form gives `sum_{c∈K1, c≠0} T_W(c) = 2^N(Z(L) − 1)`. Against the budget `2^{4 log2 N + t·L}` this is **exactly `Z(L) ≤ 1 + N^3`** — a *finite* target of **90.98 bits** at the witness. The F2 terminal is not an asymptotic question: it is `Z_1 ∈ [2^{17.98}, 2^{22.75}]`, **a 4.77-bit window**.

And under the **ruled** calibration `(T*)` it dies for a reason nobody had named: LEMMA 3 *forces* `Z ≥ 2^{4.84e7}` while the contract caps `Z` at the same value with multiplicative headroom `2^{164−9.68e7}`. The obligation becomes an **exact-value** obligation on `Z`. No mass *upper* bound of any strength can meet it. **The lane has no candidate at generating rows under (T\*)** — not because `Z_1` is unbounded, but because the consumer's budget is negative.

## R1 — THE CONSUMER CONTRACT (quoted, then derived)

**THEOREM C1 (absolute form).** `|Σ_{c≠0} ε_c exp(S_c) − STRUCT DRIFT| ≤ N^3·q^t` per slice, `N^4·q^t` summed. Derived in one step from `u2c_giant_tnull_dichotomy/node.json:8` (*"consumes ONLY the count '#{non-coset-union t-null blocks + trade families} &lt;= n^3 = 2^123'"*) and the census identity. **COROLLARY C1.1:** the tolerance *is* `t·L − N`.

**Four reading ambiguities, priced (PREREG §2 clause 1 — reported, not resolved):**

| | ambiguity | price |
|---|---|---|
| **A1** | ensemble calibrating `t`: (C) vs the ruled (T\*) | budget **+91 bits** vs **−9.68e7 bits** — decides whether a candidate exists at all |
| **A2** | ambient `N`: `2^41` (I1) vs `2^40` (tolerance prose) | tolerance **+1.05e12** vs **−4.90e10** |
| **A3** | `log2\|K1\|`: extension / base / effective | extension ⇒ the collapse; base ⇒ a trivially-met `Θ(N)` contract |
| **A4** | PP5.0 "add / Cauchy / multiply" (`BRIEF5_PRO_DOSSIER.md:41-42`) | forced multiplicative for fixed `c`; the **sum over `c` does not factor** |

**A2 is a defect, not a choice**: `EXTRAS_CONTRACTION_TARGET.md:24-27` computes the tolerance against `n = 2^40` while the same node's I1 annotation pins the budget's `n^3` to `N = 2^41`. **A1 likewise**: the consumer's mean is the *slice* `C(n,b)/q^t` while its window-empty test is the *`2^n` balance* — both ensembles, one sentence.

**Also of record:** the chain fences its own `o(n)` language — *"bare `2^o(n)` is NOT a finite certificate"* (`BRIEF5_PRO_DOSSIER.md:43-45`). (O1)'s target was never a certificate.

## R2 — THE RE-POSED INTERMEDIATE (weakest tested first, as mandated)

- **(i) MEDIAN / quantile — REFUTED as sufficient.** The brief's suggested weakening dies cleanly: PP5.0 is ruled = SUM, and by Lemma 1 the consumer's object is the *exact* first moment `2^m·Z`. There is no mean/median gap to exploit — `Z` is not a distribution over `c` but a single number fixed by `L^perp`. A median bound is **necessary, never sufficient**.
- **(ii) TAIL-COUNT — not weaker** (quantifies over all `c`; equivalent to the mass bound).
- **(iii) CAUCHY–SCHWARZ (my B3) — REFUTED at its own pre-registered falsifier.** It bounds a *ratio*; the contract is *absolute*. With `E_c[T^2] ≥ 6^m`, C-S gives `2.52e12` against Lemma 1's exact `2.199e12` — **worse by 3.22e11 bits**.
- **(iv) PARTIAL WINDOWS — a real candidate, CONDITIONAL.** At `m_W = N/4` the budget is **5.498e11 bits** and THEOREM 7 delivers **4.897e11** — it fits, with `6.00e10` bits of slack, **at every `k`**. Blocked: sectors partition `μ_N` (`Σ_j m_j = N/2` exactly, verified) and the sum over `c` doesn't factor. **Needs a PP5.0 Hölder composition. PP5.0 has no statement. Labelled conditional, not sound.**
- **(v) THE ANSWER — `F2-MASS-N^3`: `Z(L) ≤ 1 + N^3`,** i.e. `Z_1 ≤ 2^{22.75}` at `e=4`. **OPEN, not refuted, NOT proved.** Z-FLOOR (`Z≥1`) and the knife edge (`Z ≥ 2^{71.9}`) are both *inside* it. THEOREM 7 misses by `9.794e11` bits — **its exponent constant must shrink by 1.08e10×**, which is the exact size of the remaining gap. *Pre-registered falsifier:* an admissible generating row with `Z_1 &gt; 2^{22.75}`.

## R3 — NON-GENERATING ROWS: one candidate per route, with verdicts

- **(i) coset/class decomposition — NO CANDIDATE.** ADM-1/2 survives at `k&lt;e`, but the deficit is *object-level* (Z-3), not a decomposition artefact; re-decomposing cannot pay `2^{m(1−k/e)}`. Every class misses by `2^{Θ(N)}` (`2^{5N/12}` at `(1,6)`, matching `f2_adm` CATCH-1 exactly). My verdict uses only ADM-3, so it survives the plus/minus-branch correction.
- **(ii) partial windows — CANDIDATE, CONDITIONAL ON PP5.0**, as R2(iv). The `k`-dependence *vanishes* because LEMMA 3 is vacuous at `m_W = N/4`.
- **(iii) an existing proved node — YES, at `k=1`, by a one-line reduction.** `k=1 ⟺ N | p−1 ⟺ μ_N ≤ F_p^*`, so every power sum of `S ⊆ μ_N` lies in `F_p` and **the `F_q`-census IS the `F_p`-census**. Hence `f2_k1_contraction_theorem` (**PROVED**, critical) applies verbatim — hypotheses verified at admissible scale — giving per-condition loss `≤ 4` against tolerance `2^15`, **bypassing (O1) entirely**. This covers the banked killer exhibit `p = 3·2^41+1, q = p^6` *and* the whole `e=1` generating class. **NOT covered: `k ∈ {2,4}`** — named upstream as *"the summit's minimal probe"*. **The right split is `k=1` vs `k≥2`, not generating vs non-generating.**

**And the scope question was already settled inside the chain.** `f2_o1_status_split:25-28` carries it as an open *MAINTAINER QUESTION*. But `u2c` CATCH #11 (banked **2026-07-07**) states: *"Consumer rule: x4/b2_modp_giant_extras consumes F2 only where |B0|^t &gt;= 2^n; base-domain extension rows route through the f1/ext descent."* With `B0 = F_{p^k}` and the ambient balance, that rule **is exactly `k = e`** (verified at 7 `(k,e)` pairs). **The consumer supplies the missing "generates F" hypothesis; the maintainer question is ours, not the spec's.**

## R4 — THE LANE STATEMENT

Full NODE-DRAFT in `PROOFS.md` §7 (`f2_consumer_contract_repose`, DRAFT), with PROVED / OPEN / FALSE / CONDITIONAL / SCOPE parts separated as required. Coordinator mints after audit.

## CATCHES

1. **CATCH-R1 (structural, new).** The consumer's tolerance IS the counting-balance surplus — **the seam's fifth face**. All five faces are one inequality, pinned at zero.
2. **CATCH-R2 (defect in the consumer chain).** `EXTRAS_CONTRACTION_TARGET.md`'s `2^{1.05e12}` is computed at `n = 2^40`; the same node's I1 pins the budget at `N = 2^41`. Corrected, **the tolerance is negative by `4.90e10` bits** — numerically identical to BRIEF5's "49.5G bits" threshold. Two banked numbers, one arithmetic error.
3. **CATCH-R3 (against `f2_adm` D5's framing).** "The sum reading spends the whole target, counted twice" reads as a bust; against the consumer's *actual* budget `2^{123+t·L}` spending `N` bits is exactly affordable, and the residual is exactly `N^3`. **The sum reading converts (O1) into a finite certificate rather than busting it.**
4. **CATCH-R4 (subtraction, hard law 5).** THEOREM Z-3 / ADM-B (2026-08-06) re-derives `u2c` CATCH #11 (2026-07-07) at a different scale: I reproduce CATCH #11's banked `2^{1,740,627}` to 0.4% and show it equals `(1−k/e)·t·log2 q`. **The non-generating kill is a re-derivation, not a discovery.**
5. **CATCH-R5.** `(O1)` is **under-posed**: the contract needs `Z ≤ 2^{O(1)}`, strictly stronger in `n` than `2^{o(n)}` — and the chain's own fence already says the `o(n)` label isn't a certificate.
6. **CATCH-R6 (new kill mechanism).** Under `(T*)` the obligation is an **exact-value** obligation on `Z` (relative window `2^{−9.68e7}`), so it is unreachable by mass *upper* bounds as a class — a stronger statement than "no named route remains".

## THE COORDINATOR CORRECTION — recorded verbatim in `PROOFS.md` §8, and independently checked

**Verified myself (S14):** `p = 2^61−1` is `3 mod 4`, `v_2(p−1)=1`, `v_2(p+1)=61`, `v_2(q−1)=62` so `2^41 | q−1`, `p ≡ −1 mod 2^41` so `ord = 2 = e` (**generating**), `log2 q = 121 &lt; 256` (**admissible**) — and `e_p = 1` is outside `{≥41,40,39}`. **THEOREM G1 is FALSE as stated.**

**Item 4 verified independently as THEOREM D (exact descent), 89,252 checks, 0 bad, on 3 non-generating rows + 1 generating control** — but **my verdict differs from the coordinator's expectation**. The descent is exact (`Tr_{F_q/F_{p^k}}` is `F_{p^k}`-linear and `x^l ∈ F_{p^k}`, so `L`, `L^perp`, `dim L`, `Z`, min weight and `E[T_W]` are identical to the `(p, p^k)` row, fibres all `p^{(e−k)|Λ|}`). But it holds at *fixed* `Λ`, and the non-generating row's `t` is pinned by the *ambient* balance — so **the descent reproduces Z-3's excess rather than removing it**. It explains the kill; it does not answer R3. What answers R3 is CATCH #11 plus the `k=1` reduction.

**Effect on deliverables:** C1/C2/C3 and THEOREM D use only Lemma 1, the balance, `|Λ| = ceil(t/2)` and ADM-3 — **none uses ADM-1/2** — so the contract and the finite target are branch-independent and cover all five classes. Plus-branch-only is the *object* whose `Z_1` must be bounded, hence **every instrument**: THEOREM 7, Z-1's `2R+1`, Z-NOGO. **Named residual: on the two minus-branch generating types the target stands but the campaign has no object model to attack it with.**

## HONEST RESIDUALS

1. **My pre-registration was wrong where it mattered, and I say so.** B1 REFUTED (the contract is *tighter*, not looser); B3 REFUTED at exactly the falsifier I named; B4 REFUTED at the full-group window; B6 REFUTED at the failure mode I flagged in advance (ADM-3 bounds `dim L`, not `|K1|`). Confirmed: B2, B5, and B7's quoted part. **The one hypothesis I took real risk on — that the consumer was looser than (O1) — is dead.**
2. **THEOREM C1 is DERIVED, not quoted.** No chain text states the contract in absolute form. My evidence that the derivation is theirs is that it reproduces `2^{1.05e12}` to 0.047% from their own sentence. A maintainer could reject the reading; then A1–A4 are the live fork.
3. **Nothing here bounds `Z_1`.** `F2-MASS-N^3` is OPEN. `Z ≤ 1 + N^3` is "not refuted", not sound — labelled as such per PREREG §2.
4. **The `(C)` vs `(T*)` fork is not mine to settle.** Under `(C)` there is a finite live target; under the ruled `(T*)` **the lane has no candidate at generating rows**. I report both; I choose neither.
5. **PP5.0 remains the largest gap** — no statement anywhere, and R2(iv)/R3(ii) both hang on it.
6. **`k ∈ {2,4}` is uncovered by every route I found**, generating or not.
7. DRAFT ONLY: writes confined to `notes/pilots_20260806/f2_repose/`; no node/dag/tools edits; no commit, no push; `tail_count/` not read; no post-marker ledger entries read. No status flip proposed.

result: F2 lane rebuilt from the consumer down — the consumer's tolerance is proved to be the counting-balance surplus (fifth face of the seam, reproducing the banked 2^{1.05e12} to 0.047%), collapsing (O1) into the finite target Z ≤ 1 + N^3 (a 4.77-bit window for Z_1) under calibration (C), while under the ruled (T*) the lane has NO candidate at generating rows because the obligation becomes an exact-value one; non-generating rows are settled by the consumer's own banked CATCH #11 scope rule plus a k=1 reduction to a PROVED node, leaving k∈{2,4} uncovered; 60/60 checks pass, THEOREM G1 independently refuted, and my headline pre-registration refuted at its own falsifier.
