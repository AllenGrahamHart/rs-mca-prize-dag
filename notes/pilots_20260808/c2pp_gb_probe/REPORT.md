# REPORT — c2pp_gb_probe (persisted verbatim by the coordinator, task a90216d3390d652ec, 2026-08-08)

# C2''-r3 G-b PROBE — round 24, `c2pp_gb_probe`

**Headline: G-b cannot fire. Not "did not fire" — *cannot*.** Its own functional is bounded above by a constant that contains no `q` at all, so "growing without bound in `q`" has no possible referent. I measured it anyway, at the deepest depth exact census permits (**J = 4** consecutive junctions, not 8), across **25 octaves of `q` at 8 tower cells**, and the measurement confirms the structure: `Sigma_W(q)` grows only below the balance point `log2 q = n/t` and then **freezes exactly**, at an integer-identical, closed-form, `q`-free value. No status flip, no closure claim, nothing written outside the pilot directory.

## 1. The functional, quoted not reconstructed

&gt; `- **(G-b) SELECTION GROWTH**: a demonstration that the coset selection factor `omega_j := P[state_j in the coset column | null] / P[state_j in the coset column]` has an aggregate `sum_j log2(omega_j)` growing without bound in `q` along admissible rows, measured on `&gt;= 8` consecutive junctions at `&gt;= 3` increasing q-scales.`
&gt; — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260807/c2pp_diag/REPOSE_C2PP_R3_DRAFT.md:133-137`

The claim it attacks, and the descent it lives on:

&gt; `sum_{j=1}^{33}  log2 ( E_U[ rho_j | state_{&lt;j} null ] / E_U[ rho_j ] )   &lt;=   21.` — `REPOSE_C2PP_R3_DRAFT.md:49-52` (= `critical/nodes/dli_c2pp_joint_reserve/statement.md:94`)

&gt; `m_{j+1}(i) = m_j(i) + m_j(i + h_{j+1})`, `d_j(i) = m_j(i) - m_j(i + h_{j+1})` … `S_j = { i : 0 &lt; m_{j+1}(i) &lt; 2^{j+1} }` — `notes/pilots_20260802/c2pp_nullity_structure/dli_model.py:14-33`

&gt; `COSET column = k = 0` — `critical/nodes/dli_prime_weighted_large_block_support/notes/m1_dli_m1_tower_census_modal.py:25`, with `k = #singletons = |S_0|` (`:15-16`). So **coset column at junction `j` := `{S_j = empty}`** — the unique reading reducing to the banked `k=0` column at `j=0`.

## 2. The instrument (D1)

**The conditioning lemma** (registered before computing, `PREREG.md` §P1, asserted in code): the accumulated conditioning at junction `j`,
`N_{&gt;j} := AND_{j'&gt;j}{block j' holds} = { m_{j+1} is T_{j+1}-null }`, `T_{j+1} = floor(t/2^{j+1})`.
At `j=0` this is exactly the banked kernel's `e = floor(t/2)` even moments — which is why the **positive control passes 8/8 bit-exact** against `BANKED_F2B` (`m1_..._modal.py:192-201`): `443841 / 223041 / 10881 / 7713 / 443841 / 223041 / 4369 / 1137`.

This is genuine sequential conditioning: `N_{&gt;0} ⊂ N_{&gt;1} ⊂ … ⊂ N_{&gt;J-1}`, one tower, consecutive junctions, nothing raised to a power. Bayes flip (asserted in code): `omega_j = (C_j/2^h)/(Z_j/2^n)`, with `C_j` a subset census and `Z_j` a weighted state census, both exact integers by meet-in-the-middle — **cost independent of `q`**, which is what bought 25 octaves.

**Divergences from the official schedule**, all named in `PREREG.md` §P3 (D-1…D-11). The load-bearing ones: **D-3** `h_{j+1}/L_j = 2` vs official `256` (OS-1) — factor 128; **D-4** the official row sits at/below the balance `log2 q ≤ 256 = n/t`, no admissible toy can go there with &gt;2 junctions; **D-2** depth 4 vs 33.

## 3. Depth: registered target 8, achieved 4 — and 8 is impossible

I registered the wall *before* measuring (`PREREG.md` §P5) and then quantified it. Exhaustive scan over all `(n=2^s, t, window)`:

| J | cheapest exact census | at |
|---|---|---|
| 4 | **2^12.7 states** | n=32, t=16, window 0–3 |
| 5 | 2^25.4 | n=64, t=32, window 0–4 |
| 6 | 2^50.7 | n=128, t=64, window 0–5 |
| 7 | 2^101.4 | n=256, t=128, window 0–6 |
| **8** | **2^202.9 states** | n=512, t=256, window 0–7 |

Every extra consecutive junction roughly **squares** the census, because any `J`-window contains a junction with `T &gt;= 2^{J-1}` constraints. **J = 8 is unreachable at any budget, Modal included.** My working budget hits exactly J = 4, and the optimum cell the scan returns *is* my pre-registered primary cell. **Deepest honestly achieved: J = 4. Nothing is extrapolated to 8 or to 33.**

## 4. Measured `omega_j` and junction sums (D2) — toy scope, every number

**Primary cell L0 (n=32, t=16, W={0,1,2,3}, J=4), all 15 q-scales from 97 to 2^32:**

`log2 omega = (1.0000, 4.2119, 3.5793, 1.8370)`, `Sigma_W = 10.6281`, `R3_W = 11.3367` — **identical at every one of the 15 scales**, to the last integer (`C_j=2`, `Z_j = 65538 / 1810690 / 44916498 / 601080390` throughout).

**All cells** (`sat q` = the `q` at which the integers freeze forever):

| cell | n | t | J | balance | sat q | Σ(low q) | Σ(saturated) | bits/junction | slope(top half) |
|---|---|---|---|---|---|---|---|---|---|
| L0 | 32 | 16 | 4 | 2 | 97 | 10.6281 | 10.6281 | 2.657 | 0.0000 |
| L1 | 32 | 8 | 3 | 4 | 193 | 8.9835 | 9.0305 | 3.010 | 0.0000 |
| L2 | 64 | 32 | 4 | 2 | 193 | 22.5426 | 22.5426 | 5.636 | −0.0000 |
| L4 | 128 | 64 | 3 | 2 | 1153 | 20.2497 | 20.2497 | 6.750 | 0.0000 |
| S1 | 32 | 2 | 1 | 16 | 65537 | 0.1228 | 3.3203 | — | 0.0118 |
| S2 | 32 | 4 | 2 | 8 | 4129 | 3.5612 | 6.8032 | 3.402 | 0.0012 |
| S3 | 64 | 8 | 2 | 8 | 262337 | 6.7448 | 14.1060 | 7.053 | 0.0088 |
| S4 | 64 | 4 | 1 | 16 | 16777601 | 0.3998 | 6.9657 | — | 0.1627 |

The S-cells are the control that makes the L-cells readable: they show the `q` axis is **alive** below balance (S4: `0.40 → 6.97` bits over 8 octaves) and then **dead** above it. Saturation onset tracks the balance point `log2 q = n/t`.

## 5. Verdict (D4): **G-b SILENT — and structurally incapable of firing**

Against the criterion registered in `PREREG.md` §P6, at every cell: **(F1)** J≥8 **False** (4 achieved); **(F2)** strictly increasing **False** (dead flat at L0/L2/L4; and non-monotone even below balance — S1/S4 both *drop* from q=193 to q=257); **(F3)** no-saturation **False** (top-half slope ≤ 0.16 bits/octave, ≡ 0.0000 at every depth cell); **(F4)** False at 7 of 8 cells. **No cell reaches even a SUB-DEPTH GROWTH SIGNAL.**

**The reason is a theorem, not a budget** (verified over all 273 measured (row, junction) pairs):

&gt; `P[state_j in the coset column]` is a **support condition on the unconditional measure** — `P_U[S_j = empty] = 2^{h_{j+1}-n}`, brute-force confirmed, **no `q` in its definition or its value**. Since a conditional probability is ≤ 1,
&gt; **`omega_j(q) &lt;= 2^{n - h_{j+1}}` for every admissible `q`**, hence `sum_j log2 omega_j` is bounded uniformly in `q` by a constant of the **schedule alone**.

At the official schedule that ceiling is `sum_{j=0}^{32}(2^41 - 2^{40-j}) = 2^46 + 256` bits. Finite and `q`-free — so *"growing without bound in q"* is impossible. But it exceeds the 21-bit reserve by **3.35 × 10^12**, so the non-firing **carries no information about C2''-r3 either**. G-b is vacuous in both directions.

## 6. The shape (D3)

- **Not flat, not early-dominated, not deep-dominated — middle-peaked.** L0: `1.00, 4.21, 3.58, 1.84`. The deepest junction is the *smallest* term in every depth cell.
- **Exact saturation law, closed form** (verified integer-identical at every `n/t = 2` row): the only `T`-null level states are the **constant** states `c·1`, so
  `Z_j^inf = sum_{c=0}^{u} C(u,c)^h`, `C_j^inf = 2`, `log2 omega_j^inf = (n-h+1) - log2( sum_c C(u,c)^h )` — manifestly `q`-free. E.g. `Z_3 = C(32,16) = 601080390` exactly.
- **Per-junction charge grows with `n`**: 2.66 (n=32) → 5.64 (n=64) → 6.75 (n=128) bits/junction. Official `n = 2^41`. Toy scope; flagged, not transported.
- **Reserve comparison, scope stated**: L0's `Sigma_W = 10.63` bits vs the window-scaled `21·4/33 = 2.545` bits — 4.2×. The `J → 33` transport is **not licensed**; this is a shape descriptor, not evidence about the official reserve.

## 7. Self-corrections, plainly

1. **PR2 REFUTED.** I predicted `log2 omega_j` increases with depth. It does not — it peaks mid-window and the deepest junction is always smallest.
2. **PR5 REFUTED.** I predicted the sum is dominated by the deepest junctions. It is dominated by the middle ones.
3. **PR3 REFUTED as a prediction, correct as an inequality.** I registered the ceiling `n - h_{j+1}` (98 bits at L0) as the *attained* value. Attained is 10.63 — 10.8% of it. The formula survives only as the upper bound that became the theorem in §5; my registered prediction of what would be *reached* was wrong.
4. **My registered q-ladder was insufficient as registered.** L0 came back perfectly flat, which alone cannot distinguish "saturated" from "the functional is q-blind and I measured nothing." I added cells **S1–S4 mid-flight** to cross the balance point. **These were not pre-registered as cells** — the criterion was, the cells were not. I report them as **controls on the instrument**, not as evidence-bearing depth cells, and the G-b verdict rests on L0/L1/L2/L4.
5. **The brief's operating premise needs amending.** It framed G-b as "measurable NOW" with a possible board-level firing. The correct finding is that G-b is not a falsifier at all. I did not discover this by reasoning ahead of the measurement — I found the bound while explaining L0's flatness, then verified it independently.
6. **PR1, PR4, PR6 confirmed.** `omega_j &gt; 1` everywhere; the toy is already saturated at the bottom of its admissible ladder exactly as predicted; the banked control passes 8/8.

## 8. Catches for the coordinator (I edited nothing outside the pilot dir)

- **GB-1** **G-b is a vacuous falsifier** — `omega_j &lt;= 1/P[coset column]` with a `q`-free denominator; bounded uniformly in `q` by `2^46 + 256` bits at the official schedule. It can never fire, and its silence says nothing. C2''-r3's second registered falsifier should be withdrawn or re-posed.
- **GB-2** Independently: official admissible `q` are a **finite** set (`q &lt; 2^256`, `background/nodes/dli_official_support_forcing/statement.md:6-10`), so "growing without bound in `q` along admissible rows" has no referent on the official family even before the bound.
- **GB-3** **The freeze law.** Every census freezes exactly once `log2 q &gt;= n/t`. The official row has `n/t = 256` and `log2 q ∈ [41, 256]` — it sits *entirely inside* the pre-saturation regime and terminates exactly at the freeze point. Any `q`-growth argument about the official family lives only there.
- **GB-4** **G-a's depth is also unreachable**: `&gt;= 8` consecutive junctions costs `2^203` states by exact census. If the falsifier is to be testable, it needs a reachable depth or an analytic form.
- **GB-5** The **first non-stacked datapoint on the actual r3 object**: `R3_W = 11.34` bits over 4 consecutive junctions at (n=32, t=16), vs the window-scaled `21·4/33 = 2.545` bits — **4.5×**. This is **not** a G-a firing (depth 4, and I register no `J → 33` transport), and it uses the `U`-induced binomial skew law rather than `dli_model.py`'s uniform-on-domain `rho_j` (declared divergence D-10). It is not comfortable and it is the object worth escalating.

## Artifacts (all under `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260808/c2pp_gb_probe/`, stdlib only, every `python3` via `tools/ramguard local -- python3`)

`PREREG.md` (registrations appended before any script existed) · `gb_probe.py` (the instrument, checkpointed) · `analyze.py` (scores the registered criterion) · `verify_law.py` (V1 brute-force `n=16` independent-machinery cross-check, V2 `q`-freeness of the coset probability, V3 the ceiling theorem over 273 pairs, V4 the closed form — **ALL CHECKS PASS**) · `gb_results.json`, `gb_checkpoint.json`.

Full clean-checkout reproduction: **80 seconds**. Rules honoured — 2-power grids and prime `q` only (CATCH-Z6); every window has `T &gt;= 1`, `L_j &gt;= 1`, `h &gt;= 2` by design, never by post-hoc filtering (CATCH-19B); every functional named in §P2 before computing (CATCH-19C). **QUARANTINE honoured**: `CAMPAIGN_LEDGER.md` never opened; the three sibling round-24 pilot dirs never read; the clause was passed **verbatim** to the single read-only search subagent I dispatched. No `dag.json`/`nodes/`/`tools/` edit, no git, no Modal.
