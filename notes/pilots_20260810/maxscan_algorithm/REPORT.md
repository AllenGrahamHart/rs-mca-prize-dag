# REPORT.md — maxscan_algorithm (round 28) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task adc1a5646e15df795, 2026-08-10. Pilot: Opus. No edits.

# VERDICT — the wall broke by algorithm, and the answer is COLLAPSE at four scales

**The wall broke.** The n=32 exact maxscan that round 27 priced as "Modal-class, out of stdlib reach" ran in **4 minutes on one core inside `ramguard local`, using ~130 MB.** Then a theorem I proved mid-run pushed the same object to **n=64** — a scale nobody had costed — in another 4 minutes. No compute was rented.

**The scaling verdict (the one undetermined number on RH-AC's supply side):**

| n | MAXSCAN_0 (char-0 exact) | PLATEAU = C(n/2−1,n/4) | RATIO | surplus |
|---|---|---|---|---|
| 8 | 6 | 3 | 2.0000 | **+1.000 bits** |
| 16 | **46** | 35 | 1.3143 | **+0.394 bits** |
| 32 | **1974** | 6435 | 0.3068 | **−1.705 bits** |
| 64 | **1946902** | 300540195 | 0.0065 | **−7.270 bits** |

The δ=1 flank maximum **collapses**, monotonically and with accelerating speed (bit-deficit steps −0.61, −2.10, −5.57). It crosses below the slack-0 plateau between n=16 and n=32 and is 7.27 bits *under* it at n=64. Against the razor's +4.73…+4.83-bit need, this mechanism is ~12 bits short and moving the wrong way. **Round 27's honest conflict is resolved on the δ=1 side: the growing curve was the maximal-slack (δ=6) one; the δ=1 curve dies.** The round-27 model called the direction right (0.174 predicted vs 0.307 true at n=32) but for partly wrong reasons — see self-correction 1.

## What broke the wall (D1)

Two independent breaks, neither of them "more RAM":

1. **Signal separation replaces μ≈1.** The banked runs used q ≈ N because the target was 46. When the comparator is 6435, μ = N/q up to ~20 is harmless, so **q ≈ 3·10⁷ instead of q ≈ 5.7·10⁸** — and a dense `array('i')` counter of length q (120 MB) replaces the 9 GB of subset arrays. RAM wall gone.
2. **The antipodal identity.** Pairing μ_n into {ζ^j, −ζ^j} and writing B as (S, σ, T) gives `e1 = P`, **`e2 = (P² − ω_S − 2ω_T)/2`** with ω = ζ². At α=0, e2 depends on σ only through P², so σ and −σ collapse: **N/2 inner increments** and the whole n=32 subset space streams in 4 minutes.

Priced and rejected before building: the banked loop as-is (q·N ≥ 5.7·10¹³, 9 GB); the 2-D histogram (N + q³ — its balance point q≈827 and its signal window q≳10⁵ are disjoint); plain meet-in-the-middle (the coupling 2·p1L·p1R is bilinear, so the join work is exactly N — RAM only); orbit quotients alone (factor n·φ(n) = 512, insufficient).

**The residual wall I did *not* break: the number of α.** ~q/32 ≈ 9.4·10⁵ orbit reps × N = 3.3·10¹³. The full (α,β) space at n=32 is still out of stdlib reach. I registered that asymmetry in advance: a lower bound proves GROWS, only an upper bound proves COLLAPSES. So `MODAL_REQUEST.md` is emitted as required — but the pricing changed completely (below).

## The theorem (D4 — the closed-form bonus, delivered)

**PARITY THEOREM.** Split S into even- and odd-indexed pairs. The odd part of E(S,σ) factors as **ζ·X·Y** with X = Σ_{j∈S_even} σ_j ω^{j/2}, Y = Σ_{j∈S_odd} σ_j ω^{(j−1)/2}. Both exponent sets lie in [0, n/4), a **Q-basis** of Q(ω), so X=0 iff S_even=∅ and Y=0 iff S_odd=∅. Z[ω] is a domain, hence:

&gt; E(S,σ) ∈ Z[ω] ⟺ S lies entirely in the even pairs or entirely in the odd pairs.

Since ω_T is always in Z[ω], the antipodal-pair-locator targets c = ω^i (i.e. e2(B) = x², x ∈ μ_n — exactly round 27's maximizer) receive contributions **only** from such S. **Corollary: only strata s ≤ n/4 contribute.** This is what makes n=64 reachable: the count drops from C(n,n/2−1) to (3^{n/4}−1)/2 nodes — a 155× exact reduction at n=32, and the enabling structure at n=64.

**Verified, not asserted:** n=8 → 6 (s=3 excluded, measured STRAT_3 sits at different fibers); n=16 → 46 with strata 5,7 contributing exactly 0 (confirmed by a restricted mod-q run); n=32 → 1974, with the mod-q stratum probe giving s=5 → **exactly 0** at the maximizing fiber and s=7, s≥9 giving 4 and 10 — pure collision contamination against expected 6.2 and 10.3.

**Closed form for the |S|=1 (antipodal-pair-locator) family**, derived before computing and hit at tolerance 0 at **four** scales:

&gt; **STRAT_1^max(n) = (M+2)·C(M/2−1, M/4−1), M = n/2** → 6, 30, 630, 218790.

Its ratio to the plateau is 2, 0.857, 0.098, 7.3·10⁻⁴ — the family dies on its own.

## Predictions vs outcomes — **misses first**

- **P6 — MISS.** I registered the largest non-structural fiber count at n=32 in [35, 70]. The measured bulk runs continuously to 80 with multiplicity ~1000 and decays smoothly past it: the e2-value distribution is **over-dispersed relative to Poisson** (7,536 empty cells where Poisson(18.86) predicts 0.2). My background model was wrong. The separation argument survives on measured numbers, not the model: top 1988, runner-up **792**, bulk ~80 — and every value ≥250 has multiplicity exactly 16 (rotation orbits), i.e. is structural.
- **P9 — MISS (my own honest-reachable-point call was too pessimistic).** I registered n=16 as the largest fully reachable scale. The α=0 slice reached n=32 *and* n=64. The full (α,β) scan is still capped at n=16, so the registered claim was right only for the object I named and wrong about what mattered.
- P1 — HIT, tol 0 (n=8 replay byte-identical, incl. histogram).
- P2 — HIT, tol 0 (n=16 replay byte-identical to both banked files).
- P3 — HIT, tol 0, and stronger than registered: my enumerator reproduced MAXSCAN_0 **and** the banked argmax field elements (1; 6891; 4729) at n=8 and both n=16 fields; my `fullscan` mode then reproduced the **entire banked per-W1 max histogram** at both fields through a completely different algorithm.
- P4 — HIT, tol 0, at n=8/16/32/64 (6, 30, 630, 218790).
- **P5 — HIT.** Point estimate 1500, window [630, 4000]; measured **1988** (mod-q) / **1974** (char-0). R32 = 0.307 &lt; 1 ⇒ **COLLAPSES**, as predicted.
- P7 — HIT. The second-tier heavy-α family at n=16 is exactly **{W1 = x : x ∈ μ₁₆} at W2 = 0**, level 39 — a 1-term height-1 cyclotomic identification, confirmed independently in both fields (g itself appears in both lists).
- P8 — HIT. |1988 − 1988| = 0 across the two n=32 fields.
- P10a/b/c (registered while the n=64 job ran, before it returned) — all HIT: 1946902 ∈ [10⁶, 5·10⁷], ratio 0.0065 &lt; 0.1, STRAT_1 = 218790, and s=5 switched on (199024).

## Two-field confirmation of every structural claim

MAXSCAN_0(32) = **1988 at q=30000001 and q=30000193, identical.** The char-0 value **1974** is confirmed three independent ways: the exact cyclotomic enumerator; the mod-q strata-{1,3} run at q₁ (630+1344); and the same at q₂ (1974 directly, μ=0.26). The residual 14 is measured collision background. Off-axis: the lifted μ₃₂ family gives **1697 (q₁) / 1679 (q₂)** at W2=0 — below 1988 in both fields, mirroring 39 &lt; 46 at n=16; a generic α gives 188. So **α=0 wins at n=8, n=16 and n=32**.

## Self-corrections

1. **I corrected the banked round-27 model, and my correction was itself only half the story.** The model n·C(n/4−1,n/8−1) omits the S∩T=∅ exclusion and overcounts the s=1 family by 2M/(M+2) (48 vs the true 30 at n=16). But the model's n=32 number 1120 landed near the truth 1974 *for the wrong reason*: true s=1 is 630, and the missing 1344 comes from s=3, which the model does not contain at all.
2. **I nearly reported 1988 as the answer.** 1988 is the mod-q maximum; the char-0 quantity is 1974. Reported as the pair, with the 14 decomposed by stratum.
3. **The stratum ceiling s ≤ n/4 is necessary, not sufficient.** s=5,7 are permitted at n=32 and contribute exactly 0 there for arithmetic reasons — while s=5 contributes 199024 at n=64. I do not claim the ceiling explains the vanishing.
4. **n=64 is a lower bound, not a proved maximum.** I compute the count at the antipodal target, which *is* the α=0 argmax at n=8/16/32 but is assumed at n=64.
5. **A compute-law violation I caught and undid:** one launched job piped ramguard output into a bare `python3 -c`. I stopped it with TaskStop before it produced any result and re-ran it with results written to files. No number in this report came from an unguarded interpreter.
6. The third generic-α probe (α=271828181) was still running at report time; I stopped it. Two off-axis points are reported, not three.

## Deliverables (all in `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260810/maxscan_algorithm/`)

- `PREREG.md` — brief + my registrations (D1 route table with prices, ladder, P1–P10, thresholds), all appended before the corresponding computation.
- `scratch/ms_strat.py` — the R3 enumerator (modes `alpha0`, `alpha0s`, `strata`, `fullscan`, `alphas`).
- `scratch/ms_exact.py` — the char-0 parity-theorem enumerator (n=64 reachable).
- `scratch/nf_maxscan_copy.py` — banked script, md5 `909f6684…` identical, run unmodified.
- `data/` — 39 files: escape tests, the ladder, the two-field n=32 target, the stratum decomposition, the n=16 heavy-α census, `E_exact_64.json`, `SUMMARY_scaling.json`.
- `MODAL_REQUEST.md` — the priced draft. **Its headline is that the run is now optional and cheap:** a two-stage subsampled sieve (1/64 subsample detects any line of weight ≥800; exact confirmation on survivors) prices the full n=32 (α,β) scan at **~8–28 core-hours, well under $5**, with sharding, a fail-closed manifest, and four cross-check gates (α=0 must return 1988; the μ₃₂ orbit 1697; the n=16 histograms byte-for-byte; cell totals = 565,722,720). It would upgrade "argmax at α=0" from three-scale empirical to proved by exhaustion — it does not gate the collapse verdict.

Follow-up worth one line: the parity theorem may apply recursively (E on one parity class is itself an e2 one level down), which is the only visible route to n=128.

## Compliance

QUARANTINE honoured: `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was never opened at all, at any line; the round-28 pilot dirs `apolar_origin`, `ssparse_endpoints`, `mca_safe_rewire` were never read or listed — I disclose that a `ps` process listing incidentally showed a filename under `apolar_origin`; I did not read it or act on it. No subagents were spawned, so the clause needed no forwarding. COMPUTE LAW: every interpreter invocation ran as `tools/ramguard tiny|local -- python3 …` from the repo root, including all JSON peeks, summaries and the prime search; `tiny` with RAMGUARD_TIMEOUT 60/120/300 for peeks and small runs, `local` with 600 (strata q₂), 1800 (stratum sweep), 2400 (n=16 escape + heavy scans), 5400 (n=32 targets, off-axis α, n=64); no run hit its wall, no OOM; the one pipeline that would have run an unguarded `python3 -c` was stopped before yielding output and re-run compliantly (self-correction 5). BANKED SCRIPTS ran only from a scratch copy, md5-verified identical and unmodified. RAM DISCIPLINE: file-at-a-time reads, `dag.json` never opened, no bulk loads, dense counters sized to fit (120 MB against the 1 G wall — the ceiling was beaten by design, never relaxed), every long run backgrounded to a results file, `alphas` mode checkpointing after each α. DRAFT-ONLY: every write confined to `notes/pilots_20260810/maxscan_algorithm/`; no dag/nodes/tools edits, no git, **no Modal invoked** (the request is a draft for the coordinator to file), stdlib only. Registrations preceded computation, including the late P10 appended while the n=64 job ran and before it returned. Misses reported first. Every measured functional is named in PREREG §R0 (F_SUBSET, MAXSCAN, MAXSCAN_0, TAIL_0, STRAT_s, PLATEAU, RATIO, SURPLUS) plus ANTIPODAL introduced in D4. Two-field confirmation for every structural claim. Own-repo grep/read before claiming anything: the price, the banked maxima, the histograms and the argmax field elements were all located and replayed from the banked round-27 files rather than assumed.
