(RECOVERED 2026-08-06: this pilot's final-message report was never persisted at bank time — a systematic coordinator defect caught by the round-16 es_boundary_adversary pilot. Recovered VERBATIM from the session transcript by task-id; the opening sanity line matches the ledger's bank entry. The FABLE_AUDIT.md in this dir remains the audit of record.)

Sanity check complete: deleted `results/` and replayed from scratch — **66 PASS, 0 FAIL**, digest `F2_OPENING_K1_MASS_ALL_PASS (V1-V12)`. Re-read the ask: all four deliverables present. `REPORT.md` writes were harness-blocked, so the report follows here.

# F2 OPENING — the K1 mass obligations, opened and mostly discharged

Pilot: `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/f2_opening/`
Replay: `tools/ramguard local -- python3 notes/pilots_20260804/f2_opening/verify.py`

**HEADLINE.** (O1) and (O2) are **discharged exactly** at official rungs 1–13, with `o(n) = 0`: `E_{c in K1}[exp S_c] = 2^{n/2}` on the nose, and `E_c[V_b] = C(m, b/2)` at fixed `b`. The mechanism is not analytic — it is **surjectivity**. (O2) is **implied by (O1)** and is not an independent obligation. (O3) is an exact three-line lemma. And **T3 is not an analytic-number-theory question at all** — as a uniform statement it is FALSE, refuted here by explicit construction, with no character-sum input.

This round was launched 2026-08-04 (`CAMPAIGN_LEDGER.md:1060-1066`) and never banked; this is that round.

## 1. Obstruction map

**Why the fixed-sector route died** (cited, not re-derived): Theorem B, `f2_fixed_sector/REPORT.md:31` — *any composition "generic → slice theorem; parity-pure → fixed sector" is FALSE, independently of PP5.0*, because `-1 ∈ μ_{2^24}` puts the fixed sector itself in class K1. That is why the obligations are about **mass**: `eps_c = +1` on all of K1, so there is no signed content anywhere.

**What (O1)–(O3) actually require.** The pilot's central identity (V2) converts mass into a **vanishing-power-sum** question:

```
E_{c in K1(Λ)}[T_W(c)] = 2^m · Z(L),   Z(L) = Σ_{ε ∈ L^⊥ ∩ {-1,0,1}^m} 2^{-wt(ε)}
```

where `ε ∈ L^⊥ ∩ ternary` is exactly a subset `S ⊆ W` taking at most one element of each antipodal pair with `Σ_{z∈S} z^l = 0` for every `l ∈ Λ`. So (O1) requires the deployed window to admit no low-weight vanishing odd-power-sum relations — nothing analytic, nothing about cancellation. **(O1) has zero slack**: `ε = 0` is always in `L^⊥`, so `E[T_W] ≥ 2^{n/2}` for *every* condition set. The fixed-sector pilot's "dead heat, zero structural margin" is now a theorem.

**Does the antipodal/parity machinery constrain K1's mass? No — proved negative.** V10: the same deployed window, on which every K1 frequency of either condition set returns the *identical* certificate output (`all Δ even`, `D = m`, `flat = 0`), while the mass differs by **15.06×** (p=17) and **675.6×** (p=97). The certificate is a functional of the Δ multiset; the mass is a functional of additive relations among the `y_i^l`. For (O1) it is the **wrong functional** — no sharpening can pay. **Where it IS informative:** only on parity-inhomogeneous windows, i.e. class G — so its live use is as the **T3 vehicle**.

## 2. The proved partials (all three candidates landed)

**THEOREM A — (O1) discharged exactly** (V3, V3b, V12). If `Λ ⊇ {1,3,…,2m−1}` the evaluation map `K1(Λ) → F_p^m` is **surjective**: the matrix is `diag(y_i)·Vandermonde(y_i²)`, and the squares are distinct because `y ↦ y²` is 2-to-1 with fibres the antipodal pairs. Hence pair values are exactly independent and uniform, and `E[exp S_c] = 2^{n/2}` exactly. Brute-force confirmed over **all 390,625 frequencies** at p=5 on both window types; rank verified at 16 further rows to p=97, m=32. This supplies exactly the step the fixed-sector pilot could not take — its P6 banked the per-element constant 2 as exact but the *product* level as "a FIRST-MOMENT HEURISTIC". The missing ingredient was independence, and independence is surjectivity.

**THEOREM B — (O2) is implied by (O1)** (V4). `E_c[V_b] = Σ_{|A|+2|B|=b} N(A)` with `N(A) ≥ 0` integer counts, so all `E_c[V_b] ≥ 0` and they sum to `E_c[T_W]`; hence `E_c[V_b] ≤ E_c[T_W]`. **The obligation list shortens from three to two.** Sharp form: `E_c[V_b] = C(m, b/2)` for even b, 0 for odd b — the **Hamming-slice fence is answered on its own terms**, the fixed-b moment being a factor `√m` *better* than the full-window value.

**LEMMA 4 — (O3) exact** (V8, 12 rows, exact in `Z[ζ_p]`). `f(x) = g(x^{2^d})` ⟹ `P_{μ_n}(f;z) = (P_{μ_{n/2^d}}(g;z))^{2^d}`, since `x ↦ x^{2^d}` is onto with every fibre of size `2^d`. PP5.0 must carry this as a **power**, not a factor.

**LEMMA 3 — a rigorous necessary condition** (V6; tight, 3856 ≥ 3855). Total positivity plus the `c=0` term give `E[T_W] ≥ 4^m/p^{dim L}`, so (O1) *forces* `dim L ≥ m/log₂p`. Official margin at rung 16: **7.89×** — not orders of magnitude.

**The banked drift, explained** (V7). `C3b_annealed_exact.json`'s per-pair means 1.7433843858482772 / 1.9790806830379395 / 2.216211414430072 — rising past the target 2.0, flagged by the mint-prep auditor as "a live falsifier direction nobody has followed up" — are reproduced **exactly** (rel. error 0.0, 3.4e-16, 0.0). They are `Λ={1}` *punctured* means with `dim L = 2`, so `Z(L)` is large (226.9 / 4.56e5 / 4.95e14); with `c=0` included the same rows give 2.807 / 3.005 / 3.393, all `≥ 2` exactly as the floor requires. **The falsifier direction is closed.**

## 3. T3 — exact inequality and verdict

T3 needs, for every rung, every odd `k ≠ p`, and **every** generic frequency:
`|Σ_{i∈H_j} ζ_p^{k·a(y_i)}·ε(s_i^+)·ε(s_i^-)| ≤ (1−δ)·m_j`, `δ = 0.0860`, over the half-system of the genuine part of `μ_{n_j}` — note this asks only for a `1−δ` bound, not square-root cancellation.

Against standard shapes: **Weil** vacuous (folded degree up to `n_j−1 ≫ √q`); **subgroup Gauss sums** need `|H| &gt; √q` and fail at every rung (`2^25` vs `2^31` at rung 1); **Pólya–Vinogradov/Burgess** are interval bounds, wrong shape for a subgroup of a large extension; **BGK/sum-product** needs fixed `δ`, but `δ_j = (24+j)/(31·2^j)` collapses to `1.46e-4` by rung 13.

**Verdict: neither internal nor Burgess-strength — as a uniform statement T3 is FALSE.** Theorem C (V9): whenever `t ≥ n_j` (official rungs **1–12**), the folded frequency is an *arbitrary* function on `μ_{n_j}`, so one can simply **construct** a generic-class frequency with every `Δ_i` even, `|R_p| = 1`, `flat = 0` exactly. Exhibits at p = 41, 17, 97. On rungs 13–16 the construction doesn't apply, but `δ_j ≤ 1.5e-4` puts it beyond all known technology. **T3-uniform is dead at every rung.**

The re-posing that survives: T3 **in measure** over frequency space — a second/fourth-moment computation on `R_k` over a linear subspace, i.e. **internal work needing no character-sum input**, composing naturally with (O1)–(O3), which are moment computations over frequency space too. So T3 was billed as "the program's one analytic-number-theory-shaped question" and **it is not one** — the analytic shape was an artefact of asking for uniformity the frequency space cannot supply. **The F2 lane has no analytic-number-theory dependency left.**

## 4. Ranked sub-lemmas with pre-registered falsifiers

1. **SL-1 (TOP) — rungs 14–16: bound `Z(L)`.** At rungs 15–16, `dim L ≤ t &lt; m_j` forces `L^⊥ ≠ 0`. Prove no low-weight ternary vanishing odd-power-sum relation exists. *Falsifier*: exhibit `ε` of weight `w = o(m)` with `Σ ε_i y_i^l = 0` for all odd `l ≤ t`. *Prediction*: none exists for `w &lt; t/2`. The only thing between this pilot and a complete (O1).
2. **SL-2 — the `|K1|` normalisation seam.** (O1) is an *average*; the consumer needs the *sum*. *Falsifier*: PP5.0 needs the sum and the `p^{2|Λ|}` factor is unpayable — Theorem A stays true but insufficient.
3. **SL-3 — T3 in measure.** `Pr_c[max_{k≠p}|R_k| &gt; 0.914] ≤ 2^{−Ω(m)}` via second moment + the same ternary-dual counting. *Falsifier*: the off-diagonal fails to be `o(1)`.
4. **SL-4 — the exceptional-set budget.** Price `#{bad c}·(trivial bound)` against the good-`c` saving. *Falsifier*: the needed exceptional fraction is below what SL-3 can deliver.
5. **SL-5 — the K2 terminal sign** (named residue, 1/40 at p=641). *Falsifier*: the sign occurs at a rate bounded away from 0 uniformly in p.
6. **SL-6 — extend Theorem A to any `m` distinct odd exponents**, making the rung cut-off robust to the 2× window ambiguity.

## 5. Prediction vs measurement

P1–P10 all **CONFIRMED**. P2 **strengthened** (V12: only `2m−1` conditions needed, not `n−1`, moving the cut-off from rung 12 to 13). Two self-catches: P5's margin was mis-stated as ~4× because I wrote `m_16 = 2^39` (it is `2^38`) — corrected to **7.89×**; and my first P8 exhibit landed in class K2 at two of three primes, fixed by breaking the antipodal symmetry explicitly, not by weakening the claim.

## 6. Catches for the coordinator

- **CATCH-1.** `C3b_annealed_exact.json` labels the p=193 row a "20k sample" of a 37,248-element class, but exhaustive recomputation matches to relative error **0.0**. Either mislabelled or a 16-digit coincidence.
- **CATCH-2.** `(O1)/(O2)/(O3)` collides with an unrelated triple in `notes/f2_campaign/EXTRAS_CONTRACTION_TARGET.md:44,48,80`; "K1" collides with the `k=1` of `f2_k1_contraction_theorem`.
- **CATCH-3.** (O1) is written as an average but the alignment bound consumes a **sum**; the `|K1|` factor is unaccounted. Should be settled *with* the PP5.0 freeze.
- **CATCH-4.** Lemma 3 makes `t` load-bearing for a *proved* necessary condition with only 7.89× margin at rung 16; `t ~ 7e10` is currently an approximate figure carried in prose and should be pinned.

## 7. Files and flags

- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/f2_opening/PREREG.json` — frozen before any computation
- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/f2_opening/PROOFS.md` — Lemmas 1–5, Theorems A–C
- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/f2_opening/verify.py` — V1–V12, 66 PASS
- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/f2_opening/results/` — `verify_results.json`, `VERIFY_LOG.txt`

Nothing written outside this directory; no commits; no imports from other pilots (window model re-implemented from scratch); no Modal, no network; exact integer and `Z[ζ_p]` arithmetic under `ramguard local`. Nothing m2-related.

**Status posture: nothing minted, no status flips proposed.** The theorems look mint-shaped to me pending coordinator replay, but the honest DAG headline is "(O1)+(O2) discharged at rungs 1–13, SL-1 open at 14–16" — *not* "(O1) discharged". `f2_antipodal_descent_lemma`, `f2_parity_defect_certificate`, PP5.0 and the F2A.1 seam are all unchanged.

result: F2 round-14 pilot banked at notes/pilots_20260804/f2_opening/ (V1–V12, 66 PASS): (O1) and (O2) discharged EXACTLY at official rungs 1–13 via a new surjectivity theorem (E[exp S_c] = 2^{n/2} with o(n)=0, E[V_b] = C(m,b/2)), (O2) proved to be implied by (O1) so the obligation list shortens to two, (O3) given as an exact pullback-ramification lemma, the banked 1.74/1.98/2.22 "heuristic drift" reproduced exactly and closed as a single-condition artefact, and T3 refuted as a uniform statement by explicit construction — removing the F2 lane's last analytic-number-theory dependency; six ranked sub-lemmas with falsifiers left as the next round's anchors.