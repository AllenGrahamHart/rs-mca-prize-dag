# Pilot report: P-A1 widening cost pass (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored). Coordinator verification and adopted posture:
FABLE_AUDIT.md alongside.

---

## VERDICT (one paragraph)

The widening is **not free, and it is not merely a re-pricing**. Formally it is a single-parameter change — every banked P-A1 partial is really parameterized by a pairwise-core cap `kappa`, and the repair moves `kappa: k -> A-2 = k+h-2`. Three groups fall out cleanly. (1) The **k-set-keyed moment layer** (T1-T4, the sunflower per-`W` cap, H1) and the **core-agnostic charge layer** (GRK, DDR, all-LineRay/SEL, cogirth/ACG, all-zero/AZC) survive **verbatim** — the coordinator's guess in open question 2 was right about the sunflower, and right about more than the sunflower. (2) The **`kappa`-parametric charges** (PSP, RS common-root, RS flat-nullity, the collision-line ledger, the component atlas, the extension-family packing budget) survive **with stated edits but with numerically destroyed constants**: PSP's paid prize ranks drop `15,15,14 -> 11,11,10`; the collision-line rank-four thresholds go from `4,4,7,4,5,10` to `8,10,10,~1.7e10,~2.0e10,~2.1e10`, killing CLB3/CLB4 outright. (3) The **entire uniform-cell / Maxwell / shell-exclusion program breaks**, because it uses the cap to derive strict contradictions rather than constants — including the exact argument the task flagged (`k+2` zeros vs the post-strip cap `k`), which fails on **five of six rows**. The widened P-A1 is therefore **not plausibly provable from the banked partials plus stated edits**; it adds a genuinely new obligation, named below. **The joint edit is safe to write only as a three-part change** (widen + demote the invalidated PAID entries + open the band as a named sub-obligation); writing the widening alone would silently convert ~10 PROVED background nodes into over-claims.

---

## 1. CLASSIFIED INVENTORY

`S` = survives verbatim . `E` = survives with a stated edit . `M` = needs new mathematics . `F` = fails/refuted under the widening.
Row constants used throughout: `h = A-k = 5,5,3` (RowC 1/4,1/8,1/16) and `8589934593, 8589934593, 4294967297` (prize 1/4,1/8,1/16); band `[k, A-2]`.

### Group A — survives verbatim (S)

| # | Item | Class | Citation where the size-`k` assumption does **not** enter | Note |
|---|---|---|---|---|
| A1 | **Sunflower/pencil per-`W` cap `(n-k)/(t-d)` keyed on a common `k`-set `W`** | **S** | `critical/nodes/xr_smallcore_spread_count/notes/F5_P9_WCOLLISION_PAIR_MOMENT.md:28-34` (`mult(W)` defined for a *`k`-set* `W`), and the machine form `audit_p8p9_local_20260710.py:205-220` — the cap is **`d`-adaptive** (`d` = extra pencil-matching points outside `W`). A core of size `w >= k` contains a `k`-set with `d >= w-k`, giving cap `(n-k)/(k+t-w) = (n-k)/(A-w)`. **The cap self-adjusts.** | Empirically confirmed: 63/63 tests pass on the planted band fixtures (section 2). |
| A2 | **T1 pair-moment identity, T2 fiber identity, T3 regroup, T4 pencil collapse** | **S** (one wording edit) | `F5_P9_...MD:36-44` (T1 exact for **all** `J >= k`), `:48-56` (T2), `:60-64` (T3). T4's converse holds for **any** `J >= k` by interpolation on a `k`-subset. | Edit: `F5_P9_...:74` "far-pair regime (member cores <= A-2 = k at t=2)" — the `= k` is a `t=2` coincidence; restate as `<= A-2`. |
| A3 | **H1: `#high-core rays <= 2 * moment`** | **S** | `audit_p8p9_local_20260710.py:221-226` **already reads `if J >= k`** — the pinned verifier is already R2. | Margins measured in section 2. |
| A4 | **GRK fixed-chart ray bound** | **S** | `background/nodes/xr_generic_mds_kernel_ray_bound/proof.md:1-63` — parameters `R, d, h, r` and genericity only; the word "core" never appears. | Also valid at `d = 0` (`proof.md:43-52`), which the atlas repair needs. |
| A5 | **DDR direction-distance bound** | **S** | `background/nodes/xr_direction_distance_ray_bound/statement.md:5-26`; cap derived from the direction's minimum lift weight (`proof.md:34-35`), unrelated to `k`. | |
| A6 | **All-LineRay affine-core bound (AC)/(SEL)** | **S** | `background/nodes/xr_all_lineray_affine_core_bound/statement.md:6-42`; `:37-38`: "all retained LineRay pairs in **any chosen stratum**". | Pays `sigma <= 3` on all six rows at `8n^3` **and** at `4n^3` (section 3). |
| A7 | **Affine-core cogirth (ACG)** | **S** | `background/nodes/xr_affine_core_cogirth_ray_bound/statement.md:6-31` — hypotheses `Delta > r`, genericity at radius `r`, `|U|-r >= a+1`. No core hypothesis. | Full-domain ranks `4,4,3,11,11,10` unchanged, and unchanged at `4n^3`. |
| A8 | **Affine-core all-zero charge (AZC, covering-free)** | **S** | statement + proof in full: no `kappa`, no pairwise cap; the analogous role is a derived nonpersistent-zero disjointness at `proof.md:44-47`. | **But** its RowC-1/16 rank-4 discharge has margin **0.5005%** (`8,546,941,849 < 8,589,934,592`) — it dies under any sub-budget below `8n^3`. See section 4. |
| A9 | **Four/five-block circuit decomposition (Segre circuit atlas)** | **S** | `background/nodes/xr_trade_circuit_arity_segre_atlas/` statement (57 ll.) + proof (96 ll.): no cap used. | The *cell* it classifies is supplied by the split-pencil reduction, which does carry the cap (item C3). |
| A10 | **Intratrade fundamental-circuit owner** | **S** | `background/nodes/xr_rank_two_fundamental_circuit_owner/proof.md` — no cap. **Warning:** every `kappa` in this node is a *circuit vector*, not a cap. | |
| A11 | **Three-anchor dual-`GRS_3` coefficient atlas** | **S** | `background/nodes/xr_rank_two_three_anchor_grs3_factorization/proof.md` — Mobius hyperplane + Lagrange + Vandermonde kernel. No cap. | |
| A12 | **Four-anchor quadric/centroid coefficient atlas** | **S** | `background/nodes/xr_rank_two_four_anchor_quadric_centroid_atlas/proof.md:17-18,28-30` — no cap. | |
| A13 | **Dual-codeword support-extension certificate** | **S** | `background/nodes/xr_rank_two_dual_support_extension_factorization/proof.md:13` uses only the block size `|A_i| = a+h`; load-bearing step is a weight-vs-degree count at `proof.md:38-40`. | |
| A14 | **Received-pair alternating/zero router** | **S** | `background/nodes/xr_rank_two_received_pair_alternating_router/proof.md:42-48` — slope multiplicity + dual-`GRS_a` pairing only. | |
| A15 | **Per-row extension counting `C(|E_i|, tau_i)`** | **S** | `background/nodes/xr_rank_two_actual_block_extension_router/proof.md:44-45,56-57`; the node disclaims pairwise-intersection handling at `statement.md:77-80`. Per-row statement; the cap is cross-row. | |
| A16 | **Maxwell core-size cap `L_max = floor((2R+h-1)/h) = 384,448,960`** | **S** | `background/nodes/xr_higher_rank_uniform_split_pencil_reduction/proof.md:33-63` derives `(HR2)` from the kernel dimension `a` and `v_G <= N`, never from the pairwise cap. | Reproduced exactly (section 3). |

### Group B — survives with a stated edit; constants degrade (E)

| # | Item | Class | Citation where size-`k` **does** enter | Exact edit |
|---|---|---|---|---|
| B1 | **Canonical component-union atlas** (`#high-core = sum_C |Z_C|`, `(CA-GRK)`) | **E** | `background/nodes/xr_highcore_component_union_atlas/statement.md:13-14` (edge iff `|E u E'| = R` **exactly**), `:36-39`, `proof.md:6,18,58-64`. Under widening `|E u E'| = n-w in [r+2, R]`, `d_C` can go **negative** (to `2-h`) and band pairs are **never joined** — the atlas would *undercount*. | (a) edge relation -> `|E u E'| <= R` (equiv. `|S ^ S'| >= k`); (b) pad `U_C` with lexicographically least coordinates of `D \ U_C` up to `max(|U_C|, R)`, `d_C = |U_C^| - R >= 0`. GRK hypotheses are monotone under chart enlargement, so `(CA-GRK)` holds; at `d_C = 0` GRK gives `|Z_C| <= R = n-k`. Component count/excesses re-examined, not re-derived. |
| B2 | **Collision-line ledger (CLB1), (CLB1b)** | **E** (strictly stronger) | `background/nodes/xr_highcore_collision_line_basis_ledger/statement.md:22-23` ("exactly `k`"), `:27`, `proof.md:7`. | `|W_ell| = w in [k, A-2]`. Kernel argument survives (`z` supported on `n-w <= R <` min distance). `(CLB1b)` **improves**: `|U_ell| = R + m_ell - (w-k)` — each extra core point buys back one unit of chart excess. |
| B3 | **Collision-line population cap (CLB2) `L = floor(R/h)`** | **F as printed / E as re-derived** | `proof.md:51-61`: both `k`'s are the exact-core assumption. | Correct general form: `L(w) = floor((n-w)/(A-w))`, **increasing in `w`**; `L(A-2) = floor((r+2)/2)`. **Measured violation of the printed cap on a verified-generic band fixture — section 2.** |
| B4 | **(CLB3)/(CLB4) rank-four closes, thresholds `4,4,7 / 4,5,10`** | **M** | `statement.md:69-89`, `proof.md:63-81`. | Reproduced exactly at `kappa = k`; at `kappa = A-2` they become `8,10,10, 1.709e10, 1.995e10, 2.143e10`; the complementary branch needs charts of excess `~2e10` vs payable `3,3,2,10,10,9`. **CLB3/CLB4 dead on every row.** |
| B5 | **Post-strip affine-pencil charge (PSP)** | **E** | `statement.md:23` (`kappa <= k`), `:30`, `:33`; `proof.md:28-31`. Already parametric. | Drop `kappa <= k` to `kappa <= A-1`. Cost: paid ranks `4,4,4,15,15,14 -> 4,4,4,11,11,10` — at prize rows PSP degenerates to the core-agnostic ACG level. |
| B6 | **RS common-root basis charge** (source of the prize `16,16,14`) | **E** | `statement.md:20-21`, `proof.md:72-78,129-131`; `verify.py:206-211` treats `kappa` as input. | Same edit; `L` blows up by `~h/2 ~ 2^31` at prize rows; the `16,16,14` payment collapses. |
| B7 | **RS flat-nullity basis charge (FN3)/(FN4)** | **E** | `statement.md:13,51`, `proof.md:61,71-74,77`. | Both weaken monotonically in `kappa`; the RowC residual table must be re-run at `kappa = A-2`. |
| B8 | **Extension-family packing ledger** | **S** (identity) **+ E** (budget) | `(EC3)` is an exact identity — survives verbatim. `(EC4)` at `:36-42` is where the cap enters. | Budget becomes `ell_ij = z_i+z_j-d-1+(h-2)`; `(EC5)` aggregate `(t-1)Z - C(t,2)(d+1-(h-2))`. Only the constant moves. |
| B9 | **Prize flat-nullity first-core peeling owner** | **E** (improves locally) | `proof.md:15,17-18,37-40`. | `(PO1)` improves to `floor((2(R-v)-2h+3)/h)`. **But** its density trigger imports `xr_prize_flat_nullity_maxwell_trade_space_compiler/statement.md:21-26,32` hard-coding `kappa = a+u+v` — must be re-proved for the relaxed trigger. |

### Group C — breaks under the widening (M/F). **This is the cost.**

| # | Item | Class | Citation of the failing step | Why |
|---|---|---|---|---|
| C1 | **Collapsed minimum-face exclusion** — *the flagged argument* | **F on 5/6 rows** | `background/nodes/xr_higher_rank_collapsed_face_exclusion/proof.md:64-72` (`k+2` zeros vs cap `k`); also `statement.md:45-48`, `result.md:6`, re-banked inside P-A1 at `critical/nodes/xr_highcore_collision_count/statement.md:36-40` and `frontier.md:24-27`. | Only available cap is `A-2 = k+h-2`; contradiction needs `k+2 > A-2`, i.e. **`h < 4`**. BREAKS at RowC 1/4, 1/8 (h=5) and all prize rows (h ~ 2^33); survives only RowC 1/16 (h=3). No re-source found. |
| C2 | **Minimal face-syzygy dichotomy** (C1's dependency) | **F on 6/6** | `proof.md:9-12` (needs `a+1 > a+h-2`, i.e. `h < 3`). | Fails everywhere; `(MF2)`-`(MF7)` all fall. |
| C3 | **Higher-rank uniform split-pencil reduction: rank-one exclusion, `(HR7)`** | **F on 6/6** | `proof.md:22,93-96,104-128`; `statement.md:30`. | Cap becomes `a+h-2`; union lower bound `a+4-h` vacuous for `h >= 4`; `t <= a+2` and `rho <= 2a` fail. **Ambient cell for the entire rank-two/Maxwell fan.** |
| C4 | **Rank-two shell degree-vs-arity ledger `(SR2)`-`(SR5)`** | **F** | `proof.md:3-5,19-23,76-80`. | `z_i+z_j >= d+3-h <= 0` at all prize rows; `(SR5)` supply term **sign-flips**. |
| C5 | **Maxwell deficits / prize shell band `22,428,333; 19,217,048; 4,478,600`** | **F** (consequence) | `xr_prize_primitive_rank_two_shell_band/statement.md:30-46` derives from C4's `(SR5)`. | `L_max` survives (A16); the deficit does not; the printed depth band has no proof under the widening. |
| C6 | **First residual shell quadratic involution** | **F** | `proof.md:29-33` (`z_i+z_j >= 3` -> `>= 5-h`, vacuous for `h >= 4`). | `Z_i`-disjointness at `proof.md:11-14` is cap-free and survives. |
| C7 | **Prize first-shell primitive rank-three exclusion** | **F** | `proof.md:18-29`: supply constant `3C(t,2) -> (5-h)C(t,2)`, `(6)`/`(8)` go negative. | |
| C8 | **Prize uniform-trade private-point rank floor** | **F in content** | `proof.md:8-9,25-27,38-39`; `audit.md:7-9`. | Algebra survives with `a -> a+h-2` but the conclusion is negative on every prize row. Vacuous. |
| C9 | **Prize flat-nullity effective core floor** | **F** | `proof.md:11-13,48-54,66,71-77`. | `(7)` gives a negative floor on all three prize rows; the two-block exclusion also fails, losing `t >= 3`. |
| C10 | **Split-pencil trade rank-two support atlas (`kappa <= 4`)** | **F** | `statement.md:9-10,13-14`; `proof.md:18-33`. | With `kappa = h+2` the `t<=6, R<=8` conclusions and the `kappa <= 3` exclusion have no analogue; the five-profile table `(SA2)` is gone. |
| C11 | **Rank-five reuse core** | **F** (P-B branch worst) | `proof.md:43-44,50-51,54-56,59-60,63`. | P-A contradiction dies at cap `h+2`; the P-B count needs cap `<= 3` and is false at cap `h+1 >= 4`. The abstract peeling lemma (`proof.md:3-40`) is cap-free and survives. |

---

## 2. EMPIRICAL MEASUREMENT

Scripts (all in this directory, all run under `tools/ramguard`; the pinned `audit_p8p9_local_20260710.py` was **copied, never edited**):
`band_measure.py` / `.json`, `planted_band.py` / `.json`, `row_arith.py` / `.json`, `clb_recompute.py`.

### 2a. Band population on the banked toy fixtures — **the band is empty, and here is why**

`band_measure.py` replays the two pinned rows plus four new wide-band rows (`t = 4,5`), 18 fixtures total, **0 FAILS**. At the pinned `t=2` row the band `[k+1, A-2]` is arithmetically EMPTY (width 0); at every other row the organic corpus produces zero band-core cross pairs — every observed core `> k` sits at exactly `A-1` (pencil-cascade tier, paid) or at `A` (joint `A`-support, nongeneric, routes to P-A2). **The pinned machine evidence for the cap `k` comes overwhelmingly from a `t=2` row where the band is empty by arithmetic.**

H1 (widened class `J >= k`, the semantics already in the pinned file) holds with margin in every fixture (18/18; tightest x1.0 on a degenerate 3-ray fixture; x2660 on the near-pencil fixture, whose `+94` high-core slopes are all `J = A` joint-support mass routing to P-A2 — the POSEDNESS-PIN datum, not band mass). Sunflower cap S1: 0 violations everywhere, including on all `k`-subsets of larger cores.

### 2b. Planted band fixture — **the decisive measurement**

`planted_band.py`: `n=14, k=5, t=4` => `A=9, R=9, h=4, r=5`, band `[6,7]`, three seeds. A codeword pair `(f,g)` planted with joint agreement exactly 7 (top of band); three slopes each pick up `A-J = 2` further agreements on disjoint blocks. Verified exhaustively per fixture: max joint agreement over ALL codeword pairs = 7 < A (globally generic, below cascade threshold); max ray support = A exactly (no T2/P2 tangent event); `v` nonvanishing. **These pairs survive every banked strip and sit in the post-strip generic branch.**

Results (all three seeds): core histogram `{7: 3}`; high-core slopes CURRENT (`= k`) **0** vs WIDENED **3**; moment 63, H1 holds; slopes through the core `L = 3`; **banked cap `floor(R/h) = 2` VIOLATED** (`3 > 2`); widened cap `floor((n-w)/(A-w)) = 3` holds, tight; `d`-adaptive sunflower 0/63 violations, the `d=0` form 63/63 violations.

**Reading.** Not "a constant degrades": the banked `kappa = k` population cap — the same number appearing as `(CLB2)`, as `L` in PSP `statement.md:30`, and as `L` in `(FN3)` — is **false on the widened class**, demonstrated on a verified globally generic, tangent-free, cascade-free, post-strip configuration. The sunflower cap survives precisely because it is `d`-adaptive: `(n-k)/(t-d)` at `d = w-k` is exactly `(n-k)/(A-w)`. That single mechanical fact is why group A survives and group B does not.

---

## 3. EXACT ROW ARITHMETIC (`row_arith.py`, `clb_recompute.py`)

**Validation first** — the reimplementations reproduce every banked constant at `kappa = k`: PSP `4,4,4,15,15,14`; ACG `4,4,3,11,11,10`; CLB3 `4,4,7 / 4,5,10`; `L_max = 384,448,960`.

| row | `h` | `L(kappa=k) = floor(R/h)` | `L(kappa=A-2) = floor((r+2)/2)` | blow-up |
|---|---|---|---|---|
| RowC 1/4 | 5 | 153 | 382 | x2.50 |
| RowC 1/8 | 5 | 179 | 446 | x2.49 |
| RowC 1/16 | 3 | 320 | 479 | x1.50 |
| prize 1/4 | 8589934593 | 191 | 820,338,753,536 | x4.30e9 |
| prize 1/8 | 8589934593 | 223 | 957,777,707,008 | x4.30e9 |
| prize 1/16 | 4294967297 | 479 | 1,028,644,667,392 | x2.15e9 |

| charge | paid selector rank at `kappa = k` | at `kappa = A-2` |
|---|---|---|
| **(PSP)** | `4,4,4,15,15,14` | `4,4,4,` **`11,11,10`** |
| **(ACG)** core-agnostic | `4,4,3,11,11,10` | unchanged |
| **(SEL)** core-agnostic | `sigma <= 3` all rows | unchanged (also at `4n^3`) |
| **(CLB3)** at `s=4` | `B >= 4,4,7,4,5,10` | `B >= 8,10,10, 1.709e10, 1.995e10, 2.143e10` => **dead** |

**Net rank frontier.** Banked: paid `4,4,4,16,16,14`, first open `5,5,5 / 17,17,15`. Post-widening: only the core-agnostic layer + AZC survives — paid `4,4,4 / 11,11,10`, first open **`5,5,5 / 12,12,11`**. The widening costs 0 ranks at RowC, **5,5,4 ranks at prize**, plus the entire uniform-cell/Maxwell route.

**Cascade ceiling verified.** The `A-2` cap the widened statement needs IS supplied from a clean source: `critical/nodes/xr_pencil_cascade/statement.md:9` (PROVED) — a per-pair strip classification, genuinely independent of the strip item-3 over-claim.

**Budget headroom.** `B_quot_ub(A) + (n-A+1) + 16n^3 <= B*` at all six candidates, prize rows tight at `29n^3` (`30n^3` fails) => **a third generic column fits if `<= 13n^3`.**

**Do not split the `8n^3`.** SEL and ACG are unchanged at `4n^3`, but the covering-free AZC discharge of catch #158 at RowC 1/16 has margin **0.5005%** (`8,546,941,849 < 8,589,934,592`); at `4n^3` it fails by ~2x and catch #158 reopens. Use the `13n^3` headroom for a separate band column instead.

---

## 4. DOWNSTREAM-CONSUMER CHECK

`xr_highcore_collision_count` has exactly one out-edge — `req` to `xr_smallcore_spread_count` — and 65 `ev` in-edges.

| consumer | what it consumes | effect |
|---|---|---|
| **`xr_smallcore_spread_count`** (req, CONDITIONAL) | the budget `8+8 / 16` only; its own dag class is already "pairwise cores `< k+t-1`" | **SAFE.** Its re-surgery criterion 3 becomes moot rather than firing — retire or re-scope in the same edit. |
| **`xr_lowcore_spread_heart` (P-B)** | intrinsic `<= K-1` | **UNCHANGED, verbatim.** Widening closes a latent hole. |
| **`xr_quotient_global_core_collision_router`** | "size-`k` core ... exact class" routing sentence | **REPAIRED** (its `K_z` is a sub-core; the `= k` routing is already wrong when the full core exceeds `k`). |
| the 65 `ev` suppliers | the banked partials | **all the damage — section 1 groups B and C.** |

Records that become false and must be corrected in the same pass: `notes/kernel_basis/WAVE5_AUDIT_FINDINGS.md:34`, `notes/wave20_import_20260722/WAVE20_AUDIT_FINDINGS.md:36`, `notes/pro_briefs_20260801/BRIEF_3_xr_highcore_collision_count.md:12,26,85`, `notes/pro_briefs_20260801/responses/BRIEF3_DOSSIER_AUDIT.md:23`, `notes/literature_map_20260726/target_mappings.json:145`.

**New catch.** The P-A1 dag statement: *"PROVED AROUND IT: post-strip pairwise cores <= k (rung-2b two-slope forcing, replayed exhaustively — 4,662 forced pairs, 0 violations, plus a t=3 control)"*. The replay verified the FORCING identity, not the cap — and **4,662 is the count of core-`>= k+1` cross pairs in that very fixture**: the number is evidence that cores EXCEED `k`, cited as if it were evidence that they do not. Same genre as the averaged_xr and bridge-`= K` catches.

---

## 5. VERDICT AND THE NAMED NEW OBLIGATION

**Is the widened P-A1 plausibly provable from the banked partials plus stated edits? No.** Groups A + B, fully edited, deliver `sigma <= 3` everywhere, ranks `4,4,4 / 11,11,10`, the exact moment/sunflower bookkeeping, and the rank-two coefficient tower — but the cell the tower classifies (C3) no longer exists as posed, and every shell exclusion built on it (C1-C11) evaporates. **The widening adds a genuinely new obligation.**

### Candidate node statement — preferred decomposition (keeps P-A1's exact-`k` machinery intact)

**`xr_band_core_slope_count`** (P-A1b), status TARGET/red, consumer `xr_highcore_collision_count`:

> At each of the six clean-rate candidates, for every globally generic-branch received pair `(u,v)`, the number of post-strip live slopes whose selected agreement support shares a core of size in `[k+1, A-2]` with another live member is at most `4n^3` (fits the `13n^3` headroom alongside P-A1's `8n^3` and P-B's `8n^3`).
>
> **Equivalent form** (by the PROVED rung-2b forcing and the PROVED fiber identity T2): the class is exactly the union of live slopes over codeword pairs `(f,g)` with joint agreement `J in [k+1, A-2]` and live count `L(f,g) >= 2`, with `L(f,g) <= floor((n-J)/(A-J))`.
>
> **Handles already banked:** (i) core-agnostic charges A6-A8 apply verbatim; (ii) the `d`-adaptive sunflower cap A1 applies verbatim; (iii) *(one-line lemma worth banking)* distinct codeword pairs whose joint agreements have size `>= k` meet in at most `k-1` points (interpolation on a `k`-subset), so band cores form a `k`-packing and `(f,g) -> Z(f,g)` is injective.
>
> **Open:** the number of band cores carrying `>= 2` live slopes — the F5-OS anti-concentration heart re-posed one notch above `k`.

### The alternative, judged cheaper

**`xr_graded_tangent_band_charge`** — resurrect the mission of the archived cut node `archive/retraction_xr_20260705/xr_partial_tangent_band` ("design the GRADED tangent ledger charging depth-`d` partially-forced pairs"). If band pairs are *charged* rather than *classified*, they never reach the generic branch, **P-A1 keeps its exact-`k` form, and this entire inventory reduces to zero edits.** Cost: `B_tan` must exceed `n-A+1`; the consumption ledger has `13n^3` slack. Given that the widening route costs ~10 PROVED background nodes, this alternative deserves serious costing before the widening is committed.

### Is the joint R2 + P-A1 edit safe to write now?

**R2 on the bridge: yes, unconditionally** — routing-only, statement-level, costs nothing, already the semantics of every downstream instrument.

**The P-A1 widening: yes, but only as a THREE-part change**, all in one commit:

1. **Widen** the predicate to "core of size at least `k`", pinning one symbol for `K`/`k`.
2. **Demote in the same change** every entry the widening invalidates (frontier "cores at most k" PAID entry; attack.md `= k` and `= R` sentences; the collapsed-face paragraph; the dag statement's "PROVED AROUND IT ... 4,662 ... 0 violations" catch; the `= k` records listed in section 4). **Re-scope (not status-flip)** the group-C background nodes by adding the explicit hypothesis "assume the counted family has pairwise cores `<= kappa`" with `kappa = k`, relabelled as paying the exact-`k` sub-stratum only; widen the hypotheses of the parametric nodes (PSP/CRB/FN) to `kappa <= A-1` and re-run their verifiers at both values.
3. **Open the band as a named sub-obligation** (`xr_band_core_slope_count`) with its own frontier entry and its own budget from the `13n^3` headroom — NOT absorbed into P-A1's open paragraph, NOT by splitting `8n^3` (that reopens catch #158).

---

## 6. HONEST CAVEATS

1. **The `A-2` ceiling rests on `xr_pencil_cascade`'s payment being real.** Its statement classifies the received pair as TANGENT-PENCIL-paid — cleaner than the disputed per-slope removal — but whether that payment is actually charged inside `B_tan <= n-A+1` was NOT re-audited. If it is not, even `kappa = A-2` is unsourced. This is the natural next flag.
2. **Toy scale.** The organic corpus produces zero band events; the band evidence is a planted 3-seed construction at `n=14, k=5, t=4`. It establishes realizability under verified global genericity and refutes the `kappa=k` line cap on the widened class — it says nothing about band population at official `A`.
3. **The pinned verifiers of PSP/ACG/CRB/FN/AZC were not re-run at `kappa = A-2`**; the rank recomputations are reimplementations validated by reproducing the banked numbers exactly at `kappa = k` (four independent constants). A committed edit should re-run the pinned verifiers.
4. **Coverage gaps.** 19 nodes audited directly + 17 dependency-subdag entries; the `xr_rank_five_*`, `xr_split_pencil_*`, `xr_prize_*` fans were sampled (both samples break). `rigidity_kernel` / `rk_rigidity_kernel` not examined.
5. **`kappa` is overloaded in the repo** (cap in PSP/CRB/FN/prize-flat-nullity/split-pencil-atlas; circuit-scaling VECTOR in the three coefficient-atlas nodes). Grep-driven follow-ups must not conflate them.
6. **On the record:** a slope-level stratification into "max core `= k`" / "has a band core" does NOT restore the pairwise cap to the first stratum (two exact-`k` slopes can share a band core with each other); recovering `kappa = k` for a sub-family is a graph-partition problem, itself unbounded. Hence the recommendation of a separate band column rather than a re-stratified P-A1.

**Files:** `row_arith.py/.json`, `clb_recompute.py`, `band_measure.py/.json`, `planted_band.py/.json`. Nothing outside this directory modified; no commits, no pushes.
