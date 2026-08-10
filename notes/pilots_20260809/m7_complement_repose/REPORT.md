# REPORT.md — m7_complement_repose (round 25) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task a80b02f14f87e6bd4, 2026-08-09. Pilot: Opus. No edits.

All computation complete; all writes confined to my pilot dir. Final report follows.

---

# REPORT — m7_complement_repose (round 25), Opus pilot

**VERDICT: the re-pose is REAL, PROVED-already, and DEAD FOR MYSTERY 7 — a named kill with an exact threshold.** The instrument is correct and I state it below (D1), but (a) it is already a PROVED node in our own repo in two orientations, (b) its efficacy threshold is `sigma &lt; 2a`, and (c) every mystery-7 cell of ours sits on the wrong side of that threshold *by construction*, and stays there *because our own guards put it there*.

Registrations (R0–R5, sections Q1–Q2, P1–P9, E1–E4) were appended to `notes/pilots_20260809/m7_complement_repose/PREREG.md` with the `Edit` tool **before any interpreter ran**.

---

## 1. D1 — THE RE-POSED INSTRUMENT, STATED (draft; no status flip)

The brief asked me to derive the exact form behind `binom(n-(j-s),?)/binom(s,?)`.

**Base lemma** (the instrument as it already stands, set-theoretically): distinct `a`-subsets `A_i` of a `sigma`-set with `|A_i ∩ A_j| &lt;= rho` and `0 &lt;= rho &lt; a` satisfy `M &lt;= C(sigma,rho+1)/C(a,rho+1)` — each `A_i` owns `C(a,rho+1)` distinct `(rho+1)`-subsets, none owned twice.

**(PC3′) ANNULUS ANTICODE.** Let `T_1..T_M` be the root sets (size `j`) of the split members of a flat. Put

```
K = ∩ T_i,   U = ∪ T_i,   kappa = |K|,   sigma = |U| - kappa,
a = j - kappa,            r = max |T_i ∩ T_j|,   delta = j - r
```

(`delta` = half the **minimum** symmetric difference; it is invariant under core removal *and* under complementation). Work in the annulus `P* = U \ K` with `A_i = T_i \ K`. Then

```
(PC3'-direct)  M &lt;= C(sigma, a  - delta + 1) / C(a , a  - delta + 1)
(PC3'-comp)    M &lt;= C(sigma, a' - delta + 1) / C(a', a' - delta + 1),   a' = sigma - a
(PC3'-disj)    if sigma &lt; a + delta the annulus complements are pairwise
               disjoint and M &lt;= floor(sigma / a')
```

Hypotheses: distinct equal-size root sets (gives `delta &gt;= 1`); `rho = a - delta &gt;= 0` for the orientation used; nothing else. In the brief's parametrization (`kappa = j - s`, so the varying part has size `s`) the exact form is

&gt; **`binom(n - (j-s), s - delta + 1) / binom(s, s - delta + 1)`, `delta = j - r`** — and the sharper ground set is `|U| - kappa`, not `n - kappa`.

**Q1 (registered): the two orientations differ only through `min(a, a')`, so the complement orientation beats the direct one iff `sigma &lt; 2a`.** Confirmed at every fixture and cell tested (below). This is the "regime threshold" the brief asked for.

**Consistency check — both fixtures reproduce (`d3_pricing.txt` §A):**

| fixture | kappa | sigma | a | a′ | delta | AC_direct | AC_comp | truth |
|---|---|---|---|---|---|---|---|---|
| #1148 (16 branches) | **0** | 514 | 479 | 35 | 33 | 2^117.02 | **3437 = 2^11.747** | 16 |
| ours, M31 route-cut | **4979** | 67449 | 1 | 67448 | 1 | **67449** | 67449 | 67449 exhibited |

The harvest's `C(514,3)/C(35,3) = 3437` and the node's `m-(t-1) = 67449` are both reproduced exactly. **But the two fixtures use two *different* orientations of one instrument**: #1148 is `kappa = 0`, complement-in-the-union; M31 is `kappa = t-1`, common-core. The round-25a addendum calls them "the same move" (`l1_rootfree_rational_q_projective_packing/statement.md:76-82`); they are the same *instrument*, opposite *orientations*, selected by opposite sides of the `sigma &lt; 2a` threshold.

**A correction to the calibration of record.** The 2^836 "vacuous" figure decomposes exactly as

```
840.188 bits (ambient = the 1023-point fixture domain)
 -723.165  &lt;- ambient corrected to U = 514 (the actual union of the root sets)
 =117.023  bits (direct orientation, correct ambient)
 -105.276  &lt;- direct -&gt; complement orientation
 = 11.747  bits  vs truth 4.000  -&gt; residual looseness 2^7.747
```

**723 of the 836 bits were a ground-set error, not the root-sharing wall.** The core (509 points) is the *evaluation* domain; no locator has a root there. Only 105 bits are attributable to the root-sharing regime the mystery-7 lead is about.

---

## 2. D2 — THE VERTEX-VS-HULL TEST (adversarial, run first)

The caveat of record, verbatim (`background/nodes/l1_rootfree_rational_q_projective_packing/statement.md:85-86`):

&gt; "the complement / structure is a property of the exhibited VERTICES — an / arbitrary hull member need not have its roots inside U."

### ARM A — our FPC5 rate-half m4_t2 cells, FULL exact chart enumeration

`d2_arm_a.py`, reusing `rh_m4t2_census.build_flat` and `rh_bucket`'s `rref_kernel / monic_chart / enumerate_split / maxpack` unchanged. `EXACT_full_chart = true` and `maxpack_exhaustive = true` on every config reported.

**Full pairwise-overlap distribution over ALL enumerated split members (full contributor filters: primitivity + untouched-petal nonagreement):**

| cell | configs | NSPLIT mean | OVL 0 | OVL 1 | OVL 2 | OVL max | sharpened cap `ell-3` | KCORE&gt;0 | PENCIL_MAX | MAXPACK |
|---|---|---|---|---|---|---|---|---|---|---|
| ell=4, q=97 | 32 | 20.9 | **71.57%** | 28.43% | — | 1 | 1 (tight) | **0/32** | 1 (all) | 4 (×30), 3 (×2) |
| ell=4, q=193 | 15 | 163.7 | **86.50%** | 13.50% | — | 1 | 1 (tight) | **0/15** | 1 (all) | 4 (×15) |
| ell=5, q=127 | 16 | 71.6 | **60.54%** | 32.48% | 6.99% | 2 | 2 (tight) | **0/16** | 1 (all) | 4 (×16) |

**Vertices (one maximum core packing per config), same runs:**

| cell | OVL 0 | OVL 1 | OVL 2 | vertex mean | hull mean | ratio |
|---|---|---|---|---|---|---|
| ell=4, q=97 | 14.52% | 85.48% | — | 0.839 | 0.283 | 3.0× |
| ell=5, q=127 | 2.08% | 46.88% | 51.04% | 1.490 | 0.464 | 3.2× |

**Answers.** The distribution is **unimodal and decaying, with its mode at overlap 0** — the *opposite* of the root-sharing regime. The vertices are genuinely a distinct stratum (3× the mean overlap, `VERT_mean &gt; ALL_mean` in 63/63 configs), but they are shifted *within the same cap*, not into a new mode. `∩ T_i = ∅` in **every** config; `PENCIL_MAX = 1` in every config, i.e. **no two members share even `d-1` roots**. So `kappa = 0`, the annulus reduction removes nothing, and no stratified form is needed at these cells.

**LS6 cell (round-23 probe cell, `(ell,b,a) = (4,1,1)`, q=101, 16 trials, exact 1,030,301-point chart)** — I re-ran `mf_wall_adversary/ls6_probe.py` unchanged; its `owner_frac_all_pairs_g` *is* the full pairwise-overlap distribution:

```
measured over ALL pairs:            g=0: 53.11%   g=1: 36.36%   g=2: 10.53%   (cap h = ell-2a = 2)
hypergeometric ref | g &lt;= h:        g=0:  0.58%   g=1: 14.20%   g=2: 85.22%
```

The measured mass at `g=0` is **91.6×** its parametric reference — reproducing round-23b's "92×" exactly. In annulus language, **the trivial-owner concentration *is* the statement `kappa = 0` for the bulk**: the re-pose's common-core orientation has nothing to remove, and the measurement that round-23b withdrew as *classification* evidence is precisely the measurement that kills the re-pose *as an instrument* here.

### The one place the root-sharing stratum *did* appear — and what deleted it

Under the **split-only** filter at ell=4 one config in 32 (config 18) had `NSPLIT=94`, `OVL_MAX=4 = d-1`, `MAXPACK=13`, and `2775 = C(75,2)` pairs at overlap 4 — i.e. **75 members sharing one common 4-set: a perfect sunflower `P(X)·(X-a)`, the M31 route-cut structure verbatim, spontaneously inside our own chart.** Under the FULL contributor filters the same config collapses to `NSPLIT=18, OVL_MAX=1, MAXPACK=4, PENCIL_MAX=1`.

&gt; **This is the mechanism of the kill, stated as a sentence: the root-sharing regime where the re-posed instrument is sharp is exactly the regime the FPC5 guards (primitivity `gcd(F,W_F)=1` + untouched-petal nonagreement) delete. What survives the guards is the low-overlap regime where the re-pose is vacuous.**

The banked round-23b run shows the identical phenomenon at ell=5 and already handles it: `out_ell5.jsonl` (split-only) `MAXPACK_hist {'4': 24, '16': 1}` vs `out_ell5_full.jsonl` (full filters) `MAXPACK_hist {'4': 25}`.

### ARM B — our M31 route-cut fixture (`d2_arm_b.py`)

`(RC1)` `V = span{RX, R, 1, X, X², X³}` is 6-dimensional; its monic degree-`t` members are `F = R(X+beta) + c(X)`, `deg c &lt;= 3` — a `q^5` family. The node's `67449` are the `c = 0` members, i.e. **vertices**; the node never claims completeness. I enumerated the *whole* hull in a scaled analogue (same shape, scale condition `m &gt;= 2t-4` preserved so a `c != 0` member is not excluded by counting alone):

| q | m | t | exhibited `m-t+1` | measured extras (mean of 8 draws) | first-moment prediction `C(m,t)/q^(t-5)` | ratio |
|---|---|---|---|---|---|---|
| 31 | 16 | 6 | 11 | **253.25** | 258.32 | 0.980 |
| 31 | 16 | 8 | 9 | 0.25 | 0.432 | 0.579 |
| 31 | 16 | 9 | 8 | **0.00** | 0.0124 | 0 |

At `t = 9` the overlap histogram is `{8: 224}` — every pair shares exactly `t-1 = 8` roots: a pure sunflower, **no hull escape at all**, and no exhibited member ever missing (`draws_with_MISSING_gt_0 = 0` throughout). The extras obey the first-moment law to 2%; extrapolating that law to the node's real parameters (`m=72428, t=4980`, `q = 2^31-1`) gives **`log2 E[extras] = -128066.3`**.

**So: the vertex structure is the hull structure at our M31 fixture** — by a first-moment argument with 128,000 bits of margin, not by proof.

---

## 3. D3 — THE FPC5 APPLICATION: does it price the caps?

### m4_t2 (the cap-4). Exact pricing, `d3_pricing.txt` §B

`d = 2ell-3`, ambient = the core `|C| = N = 5ell-5`, sharpened overlap cap `ell-3`, `delta = ell`.

| ell | d | N | log2 (RH0b) | log2 AC(ambient n) | **log2 AC_DIRECT** | **log2 AC_COMP (the re-pose)** | measured MAXPACK |
|---|---|---|---|---|---|---|---|
| 4 | 5 | 15 | 4.807 | 5.615 | **3.322** (=10) | **5.728** (=53) | **4** |
| 5 | 7 | 20 | 7.707 | 8.358 | **5.000** (=32) | 7.870 | **4** |
| 6 | 9 | 25 | 10.546 | 11.069 | **6.644** (=100) | 9.994 | **4** |
| 12 | 21 | 55 | 27.250 | 27.258 | 16.340 | 22.637 | — |
| 16 | 29 | 75 | 38.307 | 38.028 | 22.785 | 31.047 | — |

Asymptotics (computed to ell=4096): `AC_DIRECT -&gt; 2^(1.609 ell)`, `RH0b -&gt; 2^(2.754 ell)`, **`AC_COMP -&gt; 2^(2.097 ell)`**.

Three findings:

1. **`AC_DIRECT` is not new — it is the node's own banked sharpening.** `critical/nodes/l1_fpc5_ratehalf_m4_t2_payment/statement.md:129-131`: *"feeding it into the packing improves (RH0b) from / `2^{2.755 ell}` to `2^{1.61 ell}`"*. My independent computation gives 2.754 and 1.609. MATCHED.
2. **The re-pose is strictly WORSE, at every cell, by a fixed rate.** `AC_COMP &gt; AC_DIRECT` in 100% of cells and configs; asymptotically it costs **+0.49 bits per `ell`**.
3. **The reason is structural and permanent.** By Q1 the complement orientation bites iff `sigma &lt; 2a`; here `sigma = 5ell-5`, `a = 2ell-3` (measured `kappa = 0`), so `sigma &lt; 2a` reads `5ell-5 &lt; 4ell-6`, i.e. **`ell &lt; -1` — never.** The ratio `sigma/a -&gt; 2.5` is pinned by the cell's own arithmetic (`|C| = k-1 = 5ell-5` against `d = 2ell-3`).

**Answer: NO. The complement instrument does not price the cap-4.** It gives 53 against a measured 4 at ell=4, and 2^(2.10 ell) against a measured 4 asymptotically — worse than the instrument already banked on the node.

### LS6 (the Bonferroni-3). `d3_pricing.txt` §C + `out_ls6_411_q101.json`

| cell | J | regime | node's own admissibility | BONF | measured MAXPACK | AC_DIRECT | AC_COMP |
|---|---|---|---|---|---|---|---|
| (4,1,1) | +19 | OFF-TAIL | **fails** | **3** | **3** (hist {2:5, 3:11}) | 13 | 19 |
| (9,8,1) minimal live | −5 | LIVE TAIL | holds | — (never fires) | not computable | 4855 | 81503 |
| (11,8,1) | −9 | LIVE TAIL | holds | — | not computable | 29123 | 521819 |

**Answer: NO.** Where the Bonferroni-3 exists it is *exact* (3 = 3) and both annulus orientations are strictly worse (13, 19). In the actual live tail (`J &lt;= 0`) there is no Bonferroni number to price at all, and the complement orientation is again ~17× worse than the direct one.

**Audit catch, flagged.** The round-23 owner-quality cell is `(ell,b,a) = (4,1,1)` (`l1_fpc5_ratehalf_m4_t3_split_slice_payment/statement.md:136-137`), and the addendum reads *"max core packing = 3 = EXACTLY the proved / Bonferroni cap from the pair-determinant overlap bound (the / instrument is tight)"* (`:140-142`). But the node's own admissibility is `b&gt;=7, 1&lt;=a&lt;=floor((b-3)/4)` and `J&lt;=0` (`:12-14`) — at `(4,1,1)` **all three fail** (`b=1&lt;7`; `floor((1-3)/4) = -1 &lt; 1`; `J=+19&gt;0`). The tightness claim is therefore made at a cell outside the node's parameter family, not merely "off-tail". Evaluating the node's printed fixed-owner bound there gives `C(8,3)/C(7,3) -&gt; 1`, against a measured 36-member atom — a further sign the cell is out of domain. I did **not** resolve which; I flag it.

---

## 4. D4 — THE CJ2/CJ3 CHART AUDIT AT `M &gt;= 5`: **DECIDED — the hypotheses TRANSFER**

The queued item, verbatim (`critical/nodes/l1_fpc5_large_source_payment/statement.md:108-110`):

&gt; "(CJ2)/(CJ3) of l1_joint_core_background_johnson_bound / is proved at arbitrary h and would rescue 71 residual rows — its / chart hypotheses at `M &gt;= 5` are UNAUDITED (the named next probe)."

`d4_cj3_audit.py` replays `tpetal_cj3_probe.probe_a` verbatim **and** re-derives it independently while checking each hypothesis row-by-row over all 408 residual rows.

**Replay MATCHED exactly**: 71 rows rescued, 3,972,788,690,368 d-values, fraction **0.01969549** — identical in both paths.

**Hypothesis ledger (failures out of 408 rows):**

| hypothesis | source | failures |
|---|---|---|
| `0 &lt;= b &lt; ell` (background capacity) | `l1_fixed_support_defect_johnson_bound/statement.md:16` | **0** |
| `b &gt; 0` (needed by (CJ3)) | `l1_joint_core_background_johnson_bound/proof.md:44` | 1 |
| `g = ell - b &gt;= 1` | `.../statement.md:17` | **0** |
| list threshold `h &gt;= d+g` | `.../statement.md:18` | (identical to next) |
| `0 &lt;= u &lt;= b` (canonical pick) | `(CJ1)` + `proof.md:32` | **82** |
| `r = 2d-h &gt;= 0` | `(CJ2)` | **0** |
| core / petal / background pairwise disjoint | `proof.md:16` | **0** |
| `N = |C| = k-1` | `statement.md:13` | **0** |

The disjointness hypothesis is *verified arithmetically at every rate*: `(k-1) + S = rate·k` and `S = M·ell + b` hold identically, so core and source partition the ambient domain. The only binding condition is the list threshold `h &gt;= d+g`, which is **algebraically the same inequality** as round-24's `u &lt;= b` correction (`u = d-(t-1)ell &lt;= b ⟺ t·ell &gt;= d + ell - b`) — so round-24 already imposed the right constraint under a different name.

**VERDICT (D4): the chart hypotheses transfer at `M &gt;= 5`. Claim (ii) of the large-source node — `"(ii) NO background-guard analogue at M &gt;= 5"` (`statement.md:35`) — is FALSE, by the same bookkeeping mechanism that made claim (i) false in round 24.**

Scope of the win, stated honestly:
- 71 of 408 residual rows get a **partial** rescue; **0 rows are fully rescued** (max 74.2% of any one row's `d`-window); the residual **row count stays 408**.
- Coverage: `t = 2..5` (53/8/6/4), `M = 5..18`, rates 1/2 (24), 1/4 (39), 1/8 (8) — **rate 1/16 gets nothing**.
- `(CJ4)` delivers `m &lt;= 97` on the leading sampled row and `m` between 2 and 2.33e13 across the 71; all `&lt;= n^3`. "Rescued" means *a defined finite polynomial payment exists*, not *cheap*.

---

## 5. HARD LAW 5 — the subtraction that decides the novelty question

The round-25a addendum states (`l1_rootfree_rational_q_projective_packing/statement.md:86-88`):

&gt; "Own-repo / subtraction: complement coordinates appear once (a lineage note) / and never against the packing instrument."

**This is incorrect.** A grep for `binom(·,·)/binom(·,·)` across node statements returns three PROVED nodes that state the packing instrument in complement/difference coordinates — all three consumed by `l1_mixed_petal_amplification`, the same consumer chain as the instrument owner:

- `background/nodes/xr_lowcore_near_k_difference_packing` (**PROVED**) — the full annulus form. `statement.md:24-35`: `c=K-t, v=N-2t=N-2K+2c, w=a-t=H+c-1` … `|R_(X,Y)| &lt;= floor(binom(N-2K+2c,c)/binom(H+c-1,c)). (NK4)` … *"Indeed, two distinct residuals intersect in at most `c-1`, so no `c`-subset can occur in two residuals."* That is (PC3′) verbatim, in oriented-difference coordinates, **with an official prize-row payment table** (`statement.md:58-70`).
- `background/nodes/l1_band_complement_dimension_packing` (**PROVED**) — `statement.md:27`: `Z_m(U) &lt;= floor( binom(n,s) / binom(omega,s) ). (CP2)` with `omega = n-m` the complement and `s = omega-w`: the complement orientation, plus the identical scope caveat *"It can be exponential for `s=Theta(n)`"* (`:43-44`).
- `background/nodes/l1_official_max_split_value_complement_census` (**PROVED**) — `statement.md:54-56`, `(MSC4)`.

And the common-core orientation is already deployed against *this very red*: `l1_fpc5_ratehalf_m4_t3_split_slice_payment/statement.md:110-116` (`|F_G| &lt;= floor(binom(2ell+a+b-2,h-g+1)/binom(2ell-a-g,h-g+1))` after removing the common divisor `G`). **Its measured failure mode — 52.4% of the atom at the trivial owner `g=0` — is precisely the re-pose's failure, already banked since round 23.**

So the "coordinate-change proposal" is a **re-derivation** of PROVED repo content, and the round-25a subtraction line needs correcting.

---

## 6. REGISTERED PREDICTIONS vs OUTCOMES

| # | registered | outcome |
|---|---|---|
| **Q1** | complement wins iff `sigma &lt; 2a` | **CONFIRMED** — both fixtures, all cells, 0/63 configs where it wins |
| **Q2** | `kappa &gt;= 1` at #1148 (free sharpening), p≈0.5 | **REFUTED** — `kappa = 0` (`∪B_i = U = 514`). No free sharpening exists |
| **P1** | OVL max = `ell-3`, mode 0, ≥60% at 0 | **CONFIRMED** (full filters): max 1/1/2 = cap; 71.6% / 86.5% / 60.5% at 0 |
| **P2** | `KCORE = 0` in ≥15/16 configs | **CONFIRMED** — 0/32, 0/15, 0/16 configs with a common core |
| **P3** | `ANN_ACO &gt; ANN_A` in 100% | **CONFIRMED** — 100% (63/63) |
| **P4** | vertex mean overlap &gt; hull mean | **CONFIRMED** — 63/63; 3.0×–3.2× |
| **P5** | `M31_EXTRA = 0` in ≥7/8 draws | **REFUTED at the tested scale** (t=6: 253 extras). Mechanism identified: first-moment law, ratio 0.980; holds at t=8, t=9. Extrapolation to real parameters: 2^−128066 |
| **P6** | `AC_COMP &gt;= AC_DIRECT`; `AC_DIRECT ~ 2^(1.61 ell)` | **CONFIRMED** — 1.609 asymptote; `AC_COMP -&gt; 2^(2.097 ell)` |
| **P7** | LS6: `AC_DIRECT &gt; 3` and `AC_COMP &gt; AC_DIRECT` | **CONFIRMED** — 13 and 19 vs Bonferroni 3 = measured 3 |
| **P8** | the orientation is already in our own repo | **CONFIRMED and stronger** — three PROVED nodes, not one implicit bound |
| **P9** | CJ hypotheses transfer (0.6) + a second binding condition; H5 notation collision on `b` | **SPLIT: transfer CONFIRMED; the H5 collision REFUTED** (see self-correction 3); no second condition |
| **E1** | bimodal ⟹ stratified form needed | **FIRED then DISSOLVED** — bimodal under split-only, unimodal under the full contributor filters |
| **E2/E4** | common core live / Q1 threshold wrong | did not fire |
| **E3** | `M31_EXTRA &gt; 0` ⟹ withdraw "EXACT" | fired; see verdict below |

---

## 7. SELF-CORRECTIONS, STATED PLAINLY

1. **Compute-law violation, mine.** One file patch ran as a bare `python3 - &lt;&lt;EOF` heredoc instead of `tools/ramguard tiny -- python3`. Every other interpreter invocation in this pilot — runs, JSON peeks, the PREREG append (Edit tool, no interpreter) — complied. I switched to the `Edit` tool for subsequent patches. Reported, not papered over.
2. **My first reported histogram was misleading and I corrected it mid-pilot.** The ell=4 split-only merged distribution `{0: 58.0%, 1: 19.7%, 4: 22.3%}` looked bimodal; disaggregation showed **all 2775 overlap-4 pairs came from one config in 32**. The merged aggregate was the wrong statistic. Per-config data and the full-filter rerun are the valid ones.
3. **P9's registered H5 was wrong.** I registered, before computing, that `tpetal_cj3_probe.py:80-81`'s `b = S - M*ell` was a global background block colliding with `(CJ1)`'s `b = ell-g`. It is not: `notes/pilots_20260807/fpc5_diag/fpc5_exact.py:110-112` already enforces `if not (0 &lt;= b &lt; ell): continue`, so the probe's `b` **is** the node's background capacity. Measured `b_range = [0, 5.13e11]` against `ell_range = [6.47e10, 5.31e11]`, with 0/408 violations. I flagged a collision from reading one file in isolation; that was careless.
4. **P5 refuted at the tested scale.** My scaled M31 analogue at `t=6` produced ~253 extra hull members. This is a scale artifact whose size I can predict to 2%; I report the refutation first and the explanation second, not the reverse.
5. **Q2 refuted.** I predicted a free `kappa`-sharpening at #1148 with p≈0.5. `kappa = 0`; there is none.
6. **The ell=6 arm produced zero usable configs** (`out_ell6_q61_full.json`, `configs_used: 0`) — at q=61 the pool (33 points) is too small for degree-9 split members to exist, and the q needed (127) makes exact enumeration infeasible here. I did **not** substitute a sampled run; ell=6 carries no claim from me. The brief specified ell = 4, 5, both of which are exact.
7. **A correction to the calibration of record, not mine but load-bearing:** 723 of the 836 bits of the banked "2^836-vacuous" figure come from using the 1023-point fixture domain as the anticode ambient rather than `U = 514`. That is a ground-set error, not evidence about root-sharing.

---

## 8. D5 — VERDICT

**The re-pose is not killed as mathematics; it is killed as a route to mystery 7.** Precisely:

- **The instrument is correct and now stated exactly** (D1, with hypotheses and the `sigma &lt; 2a` threshold). It reproduces both fixtures.
- **It is not new.** `xr_lowcore_near_k_difference_packing` (PROVED) is (PC3′) in difference coordinates with a prize-row table; `l1_band_complement_dimension_packing` (PROVED) is it in complement coordinates; the common-core orientation is already on the m4_t3 red. The round-25a subtraction line is wrong and should be corrected.
- **It cannot move any mystery-7 red.** Every rate-half FPC5 cell has `|C| = 5ell-5` against `d = 2ell-3`, so `sigma/a -&gt; 2.5` and the complement orientation is *permanently* on the losing side of the threshold; the direct orientation is the node's already-banked `2^(1.61 ell)`. Measured: `kappa = 0` and `PENCIL_MAX = 1` in 63/63 exactly-enumerated configs.
- **Mystery 7's wall is re-described, not moved.** Round-25a said the wall is "the live flats consist of locators sharing almost all their roots." The measurement says the opposite at *our* cells: our live flats consist of locators sharing **almost none** of their roots (mode 0, max = the sharpened cap), and the root-sharing stratum that does exist in the ambient chart is **deleted by our own guards** (config 18: 75-member sunflower, 94→18 members under primitivity + untouched-petal nonagreement). The two exhibited M31 flats are root-sharing; they are also the two flats that are *already PROVED or not-our-lane*.

**REGISTERED FALSIFIER for the re-pose as a mystery-7 route** (so this kill is checkable, not rhetorical): exhibit one FPC5 rate-half or large-source cell, satisfying its node's own admissibility conditions, whose *guarded* split members have either `∩ T_i != ∅` or `|U| &lt; 2d`. Either would put the cell on the winning side of `sigma &lt; 2a` and reopen the route. Cheapest place to look: the `M &gt;= 5` large-source cells now legalized by D4, where `b` can approach `ell` — I did not test those charts' overlap structure and say so.

**Recommended (draft only; no status flips, nothing adopted):** (i) correct the round-25a addendum's subtraction line and its "same move at both fixtures" framing, and record the 723/105/7.7-bit decomposition; (ii) apply the D4 verdict to `l1_fpc5_large_source_payment` claim (ii) as a forced correction of the same kind round 24 applied to claim (i), with the honest scope (71 partial rows, 0 full, 1.97% of `d`-mass, no rate-1/16 coverage); (iii) flag the `(4,1,1)` admissibility issue on the m4_t3 red.

**Compliance.** Quarantine observed — `notes/pilots_20260802/CAMPAIGN_LEDGER.md` never opened; no other round-25 pilot dir read; no subagent dispatched. RAM discipline: file-at-a-time reads, `dag.json` never opened (node.json shards and greps only), no bulk directory reads. Draft only: no edits to `dag.json`, `nodes/`, or `tools/`; no git writes; no Modal; stdlib only. All writes confined to `notes/pilots_20260809/m7_complement_repose/` (verified by `find`; nothing outside touched). Every measured functional named (CATCH-19C); 2-power config grids where mine (32/16/8); no shift-0 cells. Compute law complied with except for the single patch noted in self-correction 1.
