# REPORT.md — cancellation_recon (round 27) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task a3c905d5323d8c35c, 2026-08-09. Pilot: Opus. No edits.

All computations complete and banked. Here is my report.

---

# cancellation_recon — round 27 report of record

## VERDICT (first)

**D2 fired option (a) TRANSPORTS — but the transport is already banked, and it buys exactly zero new reach.** Z-FLOOR's mechanism is not merely transportable to band counts: it is *already deployed there*, in the PROVED node `rate_half_cyclic_simple_pole_mca_floor`. Its proof (`background/nodes/rate_half_cyclic_simple_pole_mca_floor/proof.md:42-56`) is literally Z-FLOOR's two moves — a volume pigeonhole supplying a mass `L`, then Cauchy–Schwarz on fiber multiplicities (`sum r_j^2 &lt;= L + kL(L-1)/(q-n)` ⟹ `M &gt;= L(q-n)/(q-n+k(L-1))`). Re-deriving Z-FLOOR for the band produces that theorem and nothing more. My registered P3b (prob 0.55 that the transport self-subtracts against our own repo, hard law 5) **hit**.

**Does any floor serve any consumer bar? No — and the correct statement is sharper than "no".** Of the three consumers, only `adjacency_closing` has an open band **lower-bound** clause at all (P1 hit, count = 1):

- `mca_safe` consumes the **upper half only** — "The proved cyclic simple-pole theorem is an unsafe lower bracket and is **not an upper input**" (`critical/nodes/mca_safe/conditional.md:98-99`). BAND-AC-LB serves it in no way.
- `list_adjacency_closing`'s rate-half lower half is **already discharged** by the PROVED `rate_half_cyclic_rotated_prefix_floor`; its open piece is the *safe* side (`rate_half_list_adjacent_crossing`, TARGET).
- `adjacency_closing` needs both halves of (RH-ADJ), and its LB bar is a **moving bar**: not a fixed radius but "wherever the safe side lands minus one". No lower bound discharges it alone.

## D1 — the need, stated exactly

**BAND-AC-LB.** For `n=2^41, k=2^40, C=RS[F,D,k], 2^128&lt;q&lt;2^256, B*(q)=floor(q/2^128)`, with `B_mca(a)` = max number of finite slopes carrying a failed support-wise MCA witness at agreement `&gt;= a`: produce `sigma_LB(q)` and prove `B_mca(k+sigma) &gt; B*(q)` for all `1 &lt;= sigma &lt;= sigma_LB(q)`.

**State of the art: `sigma_LB = 2^34 - 1`, uniform in q, PROVED** (SP2 + the wave-10 optimized re-instantiation). Per-consumer bars (CATCH-24C):

| consumer | band clause consumed | LB bar |
|---|---|---|
| `mca_safe` | safe half of (RH-ADJ) only | **none** |
| `list_adjacency_closing` | `rate_half_cyclic_rotated_prefix_floor` (PROVED) + list safe side | **already met** |
| `adjacency_closing` | full (RH-ADJ) | `sigma_LB(q) = a_RH(q)-k-1`, i.e. must *meet the safe side* |

The live gap is therefore **not** the nominal band `(2^33, sigma*]` (width 2,978,146) — that interval is entirely covered by the proved reach `2^34-1`. It is `sigma in [2^34, 2^39]`, the bracket between the proved LB reach and the proved safe side `a_RH &lt;= 3n/4` (P2 hit: width `&gt;= 2^38`, ~1.8×10^5 times the nominal band).

**K5 framing + CATCH-A.** WP5 (2026-07-10) minted K5 as "a priced witness family covering `(R(lq), sigma*]`". That interval was superseded eight days later by wave-10's optimized floor. Own-repo grep (`notes/kernel_basis/`, `critical/nodes/rate_half_band_closure/`) finds **no record** that K5's coverage target is discharged; `BRIEF_K5_RAZORBAND.md:12-13` still states "unsafe reach caps at 2^33 = n/256". **K5 as minted is discharged; the live kernel need is `(2^34-1, a_RH-k-1]`.**

## D2 — the transport, with its mechanism skeleton

Z-FLOOR (scope, per the f2 calibration clause: any `F_p`-subspace `L ⊆ F_p^m`, ternary difference set `T`, no MDS/GRS/genericity) rests on three corners: (i) a **fixed known mass** `sum_s |F_s| = 2^m`, (ii) a **free codomain ceiling** `p^d` from linearity, (iii) Cauchy–Schwarz, yielding the unknown third corner `sum_s |F_s|^2 &gt;= 2^m·2^m/p^d`.

The band count sits on the same triangle with the corners permuted: `B_mca` **is** the image cardinality `#{z : f_z&gt;0}`, the mass is the (codeword, heavy-slope) incidence count `L`, and the second moment is `sum_j r_j^2`. The in-repo proof supplies mass by pigeonhole and the second-moment ceiling by the degree bound (`P_i-P_j` has `&lt;= k` roots, averaged over `q-n` poles). So the transported theorem exists, is proved, and reads `M &gt;= L(q-n)/(q-n+k(L-1))`.

**Lower-priority survey (own-repo grep over all 22 nodes matching "floor"):** exactly two mechanisms produce band lower bounds. **M1** the tangent/direct-value family (`rs_tangent_flexible_budget_unsafe_floor`, `mca_full_agreement_endpoint`): `B_mca(a) &gt;= n-a`, a *construction*, not a count — but its whole payload is `&lt;= k = 2^40`, so it is **dead for every `q &gt;= 2^168`** (computed: `B* = 2^40` exactly at `log2 q = 168`, matching the banked `q&lt;2^167` determined range). **M2** the counting family (rotated-prefix and fixed-tail variants + simple-pole conversion). Everything else on the list is an upper bound, a fence, or a different lane. The E1/x4/qfloor floors are other lanes' objects and do not produce slope-count lower bounds.

## D3 — the weakest usable floor, attacked at the real parameters

The weakest floor that would improve anything is **the next rung of M2**: reach `2^35-1`. I attacked it *at the razor parameters*, exactly, with no small-scale extrapolation.

**Result 1 — the whole family's frontier is exactly the banked one.** Optimizing reach `= c(d+1)-1` over every `c | n` and every `d`, subject to the node's own admissibility `N q^d &lt; 2^128 C(N-1,m)`, both variants, all rungs: **max reach = 2^34-1 at (c,d)=(2^33,1)** (`frontier.txt`). The law behind it: `reach(c) ≈ n/log2 q + c - 1`, capped at `2·n/log2 q`. Computed ratio `reach / (n/log2 q) = 2.0000` — **P4 hit exactly**.

**Result 2 — the pigeonhole normalizer is exactly unrecoverable.** The `1/N` in `(CR1)` comes from pigeonholing `a_0(A) = (-1)^m prod b`, which lands in a size-`N` coset; for `d=1` the class is determined by a subset-sum mod `N`. I computed the **exact class profile by DP at the real rung parameters**: at `N=64` and `N=128` the largest class equals the guarantee `C(N-1,m)/N` to **9 decimal places** (`+0.000000 bits`; max/min spread `1.000000000`). The construction supplies exactly what the pigeonhole promises and not one bit more. The "recover the 7 bits" route is **dead by exact computation**.

**Result 3 — the deficits, exactly.**

| rung | reach | supply | verdict |
|---|---|---|---|
| rotated `N=256, d=1` (current) | `2^34-1` | `2^242.65` | ADMISSIBLE (114 bits margin) |
| **rotated `N=128, d=1`** (first real improvement) | `2^35-1` | `2^116.1263` | **SHORT by 11.8737 bits (×3750)** |
| fixed-tail `N=128, d=0` | `2^34-1` (**ties**) | `C(127,64)=2^123.1714` | SHORT by 4.8286 bits (×28.41) |

**CATCH-B (live-number correction).** The campaign's quoted band deficit — "×28.4, 4.73–4.83 bits, flat across all 2,978,146 band cells" (witness-hunt 2026-07-12, still quoted in `rate_half_band_closure/node.json:230`) — is the deficit of the **fixed-tail `N=128, d=0` rung, whose reach merely ties the current proved reach**. Closing it buys **zero**. The live deficit is **11.8737 bits**. **CATCH-C:** the difference is exactly `log2(128) + log2(65/63) = 7 + 0.0451 = 7.045` bits — the pigeonhole normalizer plus the `m = N/2+d` vs `N/2` shift — and Result 2 proves the 7 is not recoverable.

**Result 4 — the second registered repair route is also dead** (P12/P13, run as registered on the banked sunflower cells, 9-point ladder, matched by `(n,k,sigma)`): the end-to-end simple-pole conversion loss `LOSS_tot` runs `8.006 → 1.120` as `q` goes `97 → 1153`, i.e. **the conversion becomes lossless as `q` grows**, and the razor rows have `q ~ 2^256`. Registered kill line (`&lt; 28.4` sustained over `&gt;= 3` ladder points) fired on all 9. `LOSS_CS` = 1.000–1.249 (Cauchy–Schwarz is tight); the loss lives entirely in the pole-averaging step, whose measured slack is `colTOT/bound ≈ 0.10 ≈ 1/k` — the degree bound over-counts roots by exactly the factor `k`, as expected.

**Verdict on D3: the weakest usable floor is dead, twice over, at the real parameters.**

## D4 — the barrier map

1. **Both in-repo LB mechanisms die at the same line, for different reasons.** M1 (construction) dies at `q = 2^168` because its entire payload `n-a &lt;= 2^40` is smaller than the budget. M2 (counting) caps at `2·n/log2 q - 1 = 2^34-1` because ball volume falls below the budget: `C(N-1,m)` is the volume, `q/2^128` the budget, and the rungs are 2-power quantized. The residual `q &gt;= 2^168` is exactly the region where M1 is dead and M2 is capped.
2. **The barrier is quantitative and now exact: 11.8737 bits (×3750)**, at a rung where the supply is a single binomial and the normalizer is provably tight. Even the physically impossible idealization (all subsets in one class, no normalizer) is short by 4.87 bits *at a reach that ties*.
3. **The named structural feature.** Above `sigma = n/log2 q` the *average* number of codewords in a ball is below the budget, so no counting argument can produce a witness; only atypically-clustered algebraic configurations can. Every in-repo floor mechanism is either a volume count (M2) or a bounded-payload construction (M1). This is the same barrier WP7 recorded independently on the clean-rate lane ("where pigeonhole works it is not needed; where needed it provably cannot engage by counting", shortfall 212 bits there vs 11.87 bits here) — the rate-1/2 instance is by far the closest to closing.
4. **CATCH-E (the model).** The proved reach `2^34-1` is `2.0000×` the ball-volume/budget line `n/log2 q = 2^33` (which is the random-word first-moment crossing to four decimal places). So an in-repo PROVED theorem exhibits a **structural surplus of exactly a factor 2 over the random-word first moment** — the surplus is the `+c` from the maximal prefix `s=c-1`. WP5 recorded this tension qualitatively; the factor and its origin are pinned here. Consequence: `rate_half_band_closure`'s floor pose ("band determination = the first-moment prediction") is **refuted in its random-word reading by a proved theorem**, and its worst-word reading remains unformalized — the floor is currently un-attackable as posed, which is why its pre-registered falsifier has never fired.
5. **Sharpest bracket on the truth:** for `q &gt;= 2^169`, `sigma_true in [2^34, 2^39]` — 5 binary orders wide, LB capped by counting exhaustion, UB by the far-CA/Hankel layer.

## Predictions vs outcomes (misses first)

- **P13 MISS.** Predicted `M_best &gt;= 0.9L` at `(16,8,1,q=97)`; measured `75/113 = 0.664`.
- **P12 half-MISS.** Magnitude window `LOSS_tot in [3,12]` at `q=97` **hit** (8.006), but I predicted it would **increase** with `q`; it strongly **decreases** (→1.120). The route died the opposite way from how I framed it.
- **P5, P6, P7 NOT RUN — registered-plan deviation, disclosed.** The registered small-scale ladder (F-A/F-B/F-C, band-analogue `(n,q)` grid, matched controls) was superseded by exact computation at the real rung parameters, which is strictly stronger (no extrapolation) but leaves those three predictions unresolved. The one small-scale family I did run (P12/P13) used matched controls across the banked 9-point ladder.
- P1 **hit** (exactly 1 of 3 consumers). P2 **hit** (live width `&gt;= 2^38`). P3b **hit** (self-subtraction, 0.55). P4 **hit** (ratio 2.0000). P8 **hit** (ZFRATIO `1.0000008 / 1.3477 / 1.4731`, all `&gt;= 1` and `&lt;= 2`). P10 **hit** (max reach `2^34-1` at `(2^33,1)`). P11 **hit** (`log2 C(127,64) = 123.1714`; deficits 4.7286–4.8286 bits = ×26.5–28.4). P9 **hit**.
- New, unregistered: the exact equidistribution of the class profile (Result 2) and CATCH-B.

## Self-corrections

1. Before reading `proof.md` I believed the transport would *require* a new second-moment ceiling (registered as P3a's failing clause). Wrong: the ceiling is already supplied in-repo by the degree bound. I withdrew P3a's clause rather than defend it.
2. My P12 rationale — "if the conversion loss exceeds ×28.4 the next rung opens" — was **economically wrong**, and I caught it before running: the conversion loss sits in the `k·q/(q-n) = 2^40` term of `1/E`, while the binding term at the next rung is `Nq^d/B = 2^139.87`. An infinitely sharp conversion buys nothing. I ran the registered test anyway; it killed the route independently.
3. E1 reported "EXACT MATCH: False" on one cell. That is a **banked print truncation** (`SWEEP.tsv` shows `675.629394531`, exact value `675.62939453125`), not a replay failure. Stated rather than silently rounded.

## Deliverables (all under `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260809/cancellation_recon/`)

`PREREG.md` (brief + registrations R0–R4) · `escape.py`/`escape.txt` (Z-FLOOR replay ×3 cells; three banked F7-A2 ladder points reproduced exactly) · `cap.py`/`cap.txt` (banked instantiations replayed, family optimization, razor need/supply) · `attack.py`/`attack.txt` (exact class-profile DP at `N=32/64/128`; in-vivo conversion-loss ladder) · `frontier.py`/`frontier.txt` (both mechanisms, all rungs, exact deficits) · `scratch_zcore.py`, `scratch_e22_core.py`, `scratch_e22_census.py` (scratch copies).

## Compliance

Quarantine honoured: `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was never opened at any line, and none of `pincer_formalization`, `nonpoly_flank_census`, `staircase_extension` was read (their names appeared only as grep path output). No subagents were launched, so the clause needed no propagation. COMPUTE LAW: all 8 `python3` invocations went through `tools/ramguard` (`tiny` for `escape.py`/`frontier.py`, `local` for `cap.py`/`attack.py`); `RAMGUARD_TIMEOUT` was never used; no other interpreter ran. Banked scripts were copied to scratch before execution (three copies, listed above); no banked file was executed in place or modified. RAM discipline: file-at-a-time reads, `dag.json` never opened (statuses read from `node.json` shards), no bulk loads, no run exceeded 5 minutes so no checkpointing or backgrounding was needed. Draft-only: every write is inside `notes/pilots_20260809/cancellation_recon/`; no `dag/`, `nodes/`, or `tools/` edits; no git, no Modal, stdlib only. Registrations R0–R3 were appended before any computation, with my document-read state disclosed; R4 was appended before the D3 runs and is marked as mid-course. Every measured functional is named in R1 (CATCH-19C); the f2 calibration clause was honoured by stating Z-FLOOR's scope before transporting it; each "no such floor / not recorded" claim is gated by the own-repo grep shown inline (CATCH-24A); per-consumer bars are named separately (CATCH-24C); the in-vivo conversion test used the banked 9-point ladder as matched controls. Deviation from the registered D3 plan (P5/P6/P7 not run) is disclosed above.
