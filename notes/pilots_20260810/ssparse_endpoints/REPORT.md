# REPORT.md — ssparse_endpoints (round 28) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task a640f76342a4f3187, 2026-08-10. Pilot: Opus. No edits.

All deliverables complete. Final report:

---

# ssparse_endpoints — report of record (round 28)

## VERDICT (first)

**Neither falsifier fires. The measurements favor (RH-AC-lo) — but the pose's own reduction is broken, and that is the highest-information result I have.**

**F1 (push the quotient floor past 2^34−1): DOES NOT FIRE.** Seven attack surfaces enumerated and priced; the maximum admissible reach over the entire mechanism space is **exactly 2^34−1**, attained only at the printed rung (N,d)=(256,1) with margin **114.6503 bits**. (RH-AC-lo) hardens.

**F2 (an S_sparse witness at k+2^34): DOES NOT FIRE.** Priced as unreachable *before* attempting; the scaled analogue was executed and does not fire either.

**P0 — THE MISS THAT MATTERS (report misses first).** The RH-AC statement's parenthetical — *"The binding term is S_sparse alone — B_ca^far is free at razor rows (the Hankel layer discharges the far-CA half)"* — **is false on the entire open part of the bracket [k+2^34, 3n/4).** Three checks, all from primary text:
1. The PROVED simple-pole floor's own received pair `(U/(X−α), −1/(X−α))` is **column-FAR** — its proof establishes exactly that `g_α` has no code explanation on more than `k` positions, and `a = k+σ &gt; k`. So its payload lands in `B_ca^far`, **not** in `S_sparse`.
2. That payload is **`B_ca^far(k+2^34−1) ≥ 2^216.0000`** vs `B* = 2^128` — **88.0000 bits inside the unsafe region** (exact integer replay of `M ≥ L(q−n)/(q−n+kL)` at both razor endpoints).
3. The Hankel far-CA layer's scope is `r &lt; R/2 = 2^39`, i.e. `a &gt; 3n/4` (verified verbatim at `rate_half_ca_hankel_fullrank_branch/statement.md:10` and `..._split_pencil_equivalence/statement.md:44-46`). It does **not** reach below 3n/4. No contradiction with (2) — but no discharge either. The far-CA rider reduction (RR4) needs `L_2(2τ)` at `2τ = 2^35 ≪ k`, hopeless there.

So `min{a : S_sparse(a) ≤ B*}` is **not** the open content of RH-AC. The open content is the far-CA crossing. Own-repo grep (CATCH-24A): the "binding term is S_sparse alone" line exists only in the two statements themselves; nothing in-repo already carries this correction.

**Which endpoint the measurements favor: (RH-AC-lo), with the margin ladder below.**

| # | quantity | value |
|---|---|---|
| 1 | `B_ca^far(k+2^34−1)` vs `B*` | `2^216.0000` vs `2^128` → **88.0000 bits** unsafe |
| 2 | slack of the top admissible rung | **114.6503 bits** over the `2^128` the conversion needs |
| 3 | family cliff at σ=2^34 | `2^242.6503 → 2^116.1263` = **126.5240 bits**, budget `2^128` strictly inside |
| 4 | mean-model decay (labelled reference, not load-bearing) | **256.0451 bits per unit of `a`** at σ=2^34 |
| 5 | **measured** max-profile decay `F_DECAY` (exact cell) | **2.8074 bits = 0.6865·log2 q** → slack buys **0.6524 units** → `a_RH ≤ k+2^34` |
| 6 | same, worst certified lower bound | ratio ≥ 0.1451 → **3.0865 units** → `a_RH ≤ k+2^34+3` |
| 7 | what **(RH-AC-hi)** requires | max list profile flat over **532,575,944,705** consecutive agreements: average decay **≤ 2.1528e−10 bits/unit**, a factor **1.189e12 = 2^40.11** below the mean rate |
| 8 | scaled sparse crossing, 3 separating cells | tracks `2n_s/log2 q` (the −lo image), **not** `n_s/4` |

Item 7 is the discriminator: −hi is not a "somewhat higher" endpoint, it is a demand for 2^40 -fold flatness. Items 5–6 say the 114.65 bits of slack buy between 0.65 and 3.09 units of σ. **Best current estimate: `a_RH(q) = k + 2^34 + O(1)` — (RH-AC-lo) correct to within a small constant, (RH-AC-hi) refuted by ~2^40.11 in the required decay rate.** Caveat, stated plainly: item 5 is a scaled measurement across a mechanism change, and the scaled cells carry a *named downward bias* (at fixed small `n_s`, `F_LMAX` is capped by a q-independent combinatorial constant while `log2 q` grows — a bias that does not transport, since at razor `F_LMAX = 2^242.65`). Item 7 is transport-free arithmetic.

## Deliverables

**D1 — F1, seven surfaces, exhaustive.** `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260810/ssparse_endpoints/d1_rungs.py`, `d1_surfaces.py`, `d1_subgroup.py`.
- Exact rung lattice, all `N = 2^i ≤ 256` × all legal `d`, both families: max admissible reach **2^34−1** at (256,1) rot, margin 114.6503; first reach-improving rung (128,1) at **−11.8737 bits** (reproduces the banked figure exactly); fixed-tail (128,0) at **−4.8286** (reproduces the banked CATCH-B figure).
- `N ≥ 512` closed by a pruning theorem (`d ≤ ⌊(N+127)/256⌋` ⟹ reach ceiling `&lt; 2^34−1`; sup over all `N ≥ 512` = `2^33.5850`).
- **S-SCALE (the brief's non-2-power c): EMPTY, not merely unpromising** — `c | n/2 = 2^40` forces `c = 2^j`.
- **S-DEPTH (d ≥ 2): dead twice.** (a) at the admissibility boundary reach scales as `(d+1)/(2d−1)`, strictly decreasing; (b) *structural collapse* — the second constrained coefficient is `a_1/a_0 = −Σ_{b∈A} b^{-1}`, an **additive** functional, whereas `a_0` is **multiplicative** (image = a coset of size N). Measured in the razor regime (`C/(Nq) &lt; 1`): largest `(a_0,a_1)` class = **4** and **9**, against the `2519.4` the `a_0`-only pigeonhole delivers; the `a_0` classes are balanced to **1.0018×** the ideal (matching the banked 9-decimal tightness).
- **S-ROT-EXP (mine): closed.** Over all rotation exponents `v`, the minimum constrained-coefficient count is **exactly `d+1`**, attained at the printed `v = N−d`, with `0 ∈ J` and `m ∈ J` — so `N q^{d−1}` is optimal. 5/5 parameter cells.
- **S-HYBRID / S-RIDER / S-OVERFLOW: priced.** Fixed-tail's denominator is worse by `q/N = 2^248`; a free rider `W` in `S ≡ Y^v P_A W` adds `deg W` unknowns and `deg W` constraints (net count stays `d+1`); prefix overflow `s ≥ c` costs a full `log2 q = 256` bits per `+1` of reach against a 114.65-bit budget.
- **S-SUBGROUP (mine, registered mid-run): closed exactly.** The one route that removes the `q^{d−1}` loss (A = union of H-cosets + loose points ⟹ `a_i = p̃_0 e_i`). Exhaustive `(N,t,d,u)` scan: max reach again **exactly 2^34−1, at t=1 only**; the family degenerates monotonically in `t` (ceiling `n(1+1/t)/256 − 1`).

**D2 — F2, priced before attempting, then executed in scaled form.** `d2_sparse.py`.
- Honest pre-price: a razor witness needs `&gt; 2^128` MCA-bad slopes from one sparse pair; tangents give `&lt; 2^40`; non-tangent slopes need `[p_Z]` on the pencil line, first-moment total `C(n−e,a−e)q^{1−τ} ≤ 2^{2^41−2^42} &lt; 1` at τ=2^34, adversarial forcing `&lt; 2^8`. **Unreachable and predicted false.** Verdict recorded before any attempt.
- Scaled analogue **`F_COLL`** — max collinear locator points, which *is* the non-tangent sparse payload at minimal support `e = τ+1`, hence the sharp scaled form of F2. Measured at n_s=16: τ=2 → **16 / 34 / 28** at q=17/97/65537; τ=3 → **12 / 10 / 10**. At the one cell where the budget is meaningful (q=65537, `B_s`=256), **F_COLL = 28 ≤ 256: F2's scaled analogue does not fire**, by 9.1×. Transport caveat: the razor row needs `&gt; 2^128` collinear points where the random model gives ~4; the measured algebraic surplus over random is ~7–9× (28 measured vs ~3–4 random at q=65537 — real structure, but 2^126 short of what F2 needs).

**D3 — first crossing measurements.** `d3_lmax.py`, `d3_lmax5.py`, `d2_sparse.py`; data in `.../ssparse_endpoints/data/`.
- Scaling map registered before use (rate 1/2, multiplicative domain, budget exponent `B/q = q^{−1/2}` ⟹ `B_s = ⌊√q⌋`); endpoint images `τ_lo = 2n_s/log2 q`, `τ_hi = n_s/4`; **registered in advance that cells with `log2 q ≤ 8` are non-discriminating** (the images cross there).
- `F_LMAX` computed by a **q-independent** subspace-closure algorithm, **validated 3/3 against brute-force enumeration** at (8,17): `F_LMAX(5,6,7) = 7,1,1`.
- Exact `F_SSPARSE` at minimal support, q-independent: n_s=8 → **19** (q-independent for q ≥ 41); n_s=16 → 17/97/257/**955**.
- **The three separating cells (log2 q &gt; 8), all favoring −lo:** (8, 65537): τ_lo=1, τ_hi=2, measured crossing **τ=1**, safe by 256/19 = **13.5× (3.75 bits)**. (8, 16777289): τ_lo=0.67, τ_hi=2, measured **τ=1** (integrality floor), safe by **215× (7.75 bits)**. (16, 65537): τ_lo=2, τ_hi=4, τ=1 **certified unsafe** (955 &gt; 256, by 3.73×) and τ=2 measured safe on the e=3 layer by 9.1× ⟹ crossing bracketed in [2,4] with the evidence at 2.
- Matched control: `λ_FM` (first-moment MEAN list size) computed at every cell and printed **as a labelled reference line only**. **F3 binds: no random-word or mean quantity enters the verdict** — the load-bearing decay number (ladder item 5) is the measured decay of the exact *max* profile.

**D4 — verdict + margin ladder.** `d4_margins.py`; the table above.

**Escapes.** `escapes.py`. ESC-1 was **registered as a MISS before running**: the brief asks S_sparse to reproduce `B_mca − B_ca^far`, but (MS1) is `B_mca = max(B_ca^far, S_sparse)` — a maximum, so the difference form is false whenever one term dominates (which P0 says is always, here). I executed the corrected escape — the proof's actual load-bearing lemma, translation-invariance of the MCA-bad slope set for column-close pairs — and got **6/6 identical**. Tangent lemma (my P8, `S_sparse(a) ≥ min(r,q)`) verified **6/6** by brute force. ESC-2: `a_RH(q) = n − ⌊q/2^128⌋ + 1` replayed at 3 sample `q &lt; 2^167`, **3/3**.

## Predictions vs outcomes

**Hits (11):** P0 (2^216.0000 ≥ registered 2^215), P1 (114.6503 ∈ [114,115]; −11.8737 ∈ [−11.95,−11.80]), P2, P3 (5/5 exact), P4a, P5, P6, P8 (6/6), P13, P14 (3/3), P15 (exact equality, no gain).

**Misses (2), reported first in their sections:** **P4b** — registered largest `(a_0,a_1)` class ≤ 4, measured **9**; the collapse conclusion survives (9 vs the 2519 needed). **P17** — registered `F_COLL ≤ 4`, measured **10–34**; the locator point set carries far more collinear structure than I predicted (28 collinear at q=65537 where random gives ~3), though still 2^126 short of F2.

**Partial / not measured (declared deviations):** **P7** confirmed in substance but my registered *reasoning* under-weighted the first-moment term over `Z`'s — disclosed. **P9** too strong as written: at (16,65537) the sparse layer is unsafe at τ=1 by 3.73×, so the sparse crossing is not always at the bracket bottom. **P10/P11** (ρ_S ladder, q-trend) **NOT MEASURED as registered** — n_s=8 is integrality-floor-limited and n_s=16 exact `F_LMAX` was out of reach; superseded by the sparse-crossing cells and the decay ladder. **P12** (random-key control) **NOT RUN** — its block was in the run that hit the wall; zero-power by F3 regardless. **P16** confirmed at the one exactly-computed cell (0.6865 ∈ [0.25, 4.0]); elsewhere lower bounds only, with the named downward bias.

## Self-corrections (4, all disclosed)

1. **Fixed-tail admissibility dropped one factor of `q`** (`q^d` vs the correct `q^{d+1}` in `q/L &lt; 2^128`). It declared an `L=1` rung admissible — caught by absurdity, then anchored against the banked 4.8286-bit deficit, which the corrected line reproduces exactly.
2. **S-SUBGROUP off-by-one**: `C(N',j)` should be `C(N'−1,j)` (the `b_0` coset carries the prefix and must be excluded). Caught because the `t=1` row failed to reproduce the printed 114.6503-bit margin; after the fix it reproduces it exactly. This also erased an apparent **1.02-bit improvement** in the first reach-improving rung's deficit that I had briefly believed was real — it was not.
3. **The rank-3 normal-triple candidate family for `F_LMAX(5)` is not exhaustive**: its anchor **failed** (returns 5 where brute force gives 7). Those numbers are downgraded to certified lower bounds, and the decay ratios derived from them are stated as lower bounds only.
4. **CATCH-24A subtraction**: the additive-subspace-polynomial (BKR) framing for super-polynomial RS lists is **already mapped in-repo** (`notes/literature_map_20260726/LITERATURE_MAP.md:92`, "the multiplicative counterpart is headliner F's territory"), so I claim nothing new there.

## Consumer-bar consequence (for the coordinator, not applied)

If P0 is ratified, RH-AC's open content re-prices: the crossing is set by `B_ca^far`, so the safe half at `a = k+2^34` is a **far-CA** problem, and `adjacency_closing`'s moving lower bar is met *exactly* by the already-PROVED floor at `a−1`. The named next object is an upper bound on the max list profile just above σ=2^34 — not the sparse coupled system.

## Compliance

Brief and PREREG read first; all registrations (R0–R6, P0–P17, functionals, scaling map, attack-surface order, cell plan) appended to `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260810/ssparse_endpoints/PREREG.md` with the Edit tool **before** any computation, and the two mid-run additions (R5 S-SUBGROUP, R6 `F_DECAY`/`F_COLL`) registered with numeric windows **before** their own computations. QUARANTINE honored: `CAMPAIGN_LEDGER.md` never opened; the three sibling round-28 pilot dirs never read; no subagent spawned. DRAFT-ONLY honored: every write confined to `notes/pilots_20260810/ssparse_endpoints/` (7 scripts + `data/`); no dag/nodes/tools writes, no git, no Modal, stdlib only. RAM discipline: file-at-a-time reads, `dag.json` never opened, no bulk loads, four long runs backgrounded to results files. Every functional named (R0). 2-power grids used wherever the grid was mine (`n_s ∈ {8,16}`, `N = 2^i`); matched control computed and excluded from the verdict per F3. **COMPUTE-LAW BREACH, disclosed: one un-ramguarded `python3 -` invocation with an empty heredoc** (a stray placeholder; no program ran, no result derived). 13 of 14 interpreter invocations compliant, each under `tools/ramguard tiny|local` with `RAMGUARD_TIMEOUT` set explicitly (60 / 120 / 280 / 290 s as recorded per call). Two runs hit their wall limit and were re-scoped rather than extended.
