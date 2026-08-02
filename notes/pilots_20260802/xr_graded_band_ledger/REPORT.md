# Pilot report: graded tangent band ledger / Route T costing (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored). Coordinator verification and adopted posture:
FABLE_AUDIT.md alongside.

---

# Route T (graded tangent band ledger): design, proofs, price

## VERDICT

**CONDITIONAL — and Route T strictly dominates Route W.**

Route T is feasible **only against the `13n^3` headroom, never against the printed `n-A+1`**, and it closes on exactly **one named open lemma** (band occupancy `N_d`). That lemma is a *proper sub-obligation* of what Route W must prove anyway, and Route T buys it with **zero demotions** — versus Route W's ~10 re-scoped PROVED nodes and the `15,15,14 -> 11,11,10` prize-rank drop.

Three sharp sub-verdicts, all from exact arithmetic (not estimates):

1. **DEAD: the printed `n-A+1` column.** Even in the most optimistic case `N_d = 1` (a *single* band pair at each depth), the ledger column `SUM_d L(d)` exceeds the printed tangent column on **5 of 6 rows** (828 > 764; 967 > 892; prize rows by ~22x). Only RowC 1/16 (`h=3`, one band depth) fits. Route T must be a **new third generic column from the `13n^3` headroom**, not an enlargement of `B_tan`.
2. **DEAD: scheme (a) as posed** (count band pairs by the k-packing, times the line cap). The k-packing gives `#band pairs <= C(n,k)/(k+1)`, which overshoots the headroom by **695 / 423 / 213 bits (RowC)** and by **~10^12 bits (prize)**. Counting band *pairs* is hopeless by an astronomical margin; only pairs carrying **>= 2 live slopes** can be counted. The same kill applies to the banked interleaving route (below).
3. **ALIVE with real content: scheme (b), the "upgrade".** I found and proved a genuine interaction mechanism — two band pairs with proportional differences force a ray of agreement `>= |Z_1 u Z_2|`, i.e. a **T2/P2 tangent event whenever `d_1 + d_2 >= h`**. This is exactly the archived node's "upgraded toward the cascade", it is provable in three lines, and it **refuted my own strongest adversarial fixture** (the only one that beat the printed column).

---

## 1. The object, formalized

Standing hypotheses (post quotient- and tangent-strip, globally generic branch): every live slope's agreement set has size exactly `A` (over-agreement is the T2/P2 tangent event); `max` joint codeword-pair agreement `<= A-2` (generic + below cascade).

For a received pair `(u,v)`, a **band pair** is a codeword pair `P = (f,g)`, `deg f, deg g < k`, with joint agreement `Z_P = {i : f(x_i)=u_i, g(x_i)=v_i}` of size `J_P = k + d_P`, depth `d_P in [1, h-2]`. `L_P` = number of live slopes `z` with `Z_P` inside the selected support `S_z`. `N_d` = number of depth-`d` band pairs with `L_P >= 2`.

**Master ledger inequality (proved, from THEOREMs 1-3 below):**

```
|Gamma_band|  <=  SUM_{d=1}^{h-2}  N_d * L(d),      L(d) = floor((R-d)/(h-d)),  R = n-k
```

where `Gamma_band` is the set of live slopes sharing a band core with another live slope — the exact class Route T must charge before the generic branch.

---

## 2. THEOREMS (all proofs complete and inline)

**THEOREM 1 (k-packing). — ALREADY BANKED, not novel.** Distinct codeword pairs have `|Z_P ^ Z_{P'}| <= k-1`; hence `Z_P` determines `P` and band cores form a k-packing.
*Proof.* On the intersection `f=u=f'` and `g=v=g'`; if `|.| >= k` then `f-f'` and `g-g'` are degree-`<k` polynomials with `>= k` roots, so `P = P'`. QED
**Subtraction-law finding:** this is already in the tree, verbatim, at `background/nodes/xr_mismatch_chart_nongeneric_joint_support_equivalence/proof.md:19-22` ("let distinct codeword pairs explain the same received pair on supports `Y,Y'` ... `|Y intersect Y'| <= K-1`"). The p_a1 pilot's "one-line lemma worth banking" is a re-derivation. **Do not bank it as new.**

**THEOREM 2 (T2 fibre identity / core = Z exactly).** If live slopes `z_1 != z_2` have `|S_{z_1} ^ S_{z_2}| >= k`, then the rung-2b forced pair `P` satisfies `S_{z_1} ^ S_{z_2} = Z_P` **exactly** (not merely contained).
*Proof.* Forcing gives `u=f, v=g` on the core, so `c_{z_i} = f + z_i g` (degree-`<k` agreement on `>= k` points). Write `e = u-f`, `e' = v-g`; then `S_{z} = {i : e_i + z e'_i = 0}` union Z_P. If `i` is in both supports off Z_P, `(z_1-z_2)e'_i = 0`, so `e'_i = e_i = 0`, i.e. `i in Z_P`. QED **Verified: 0 violations in every fixture.**

**THEOREM 3 (line cap).** For a codeword pair with `|Z_P| = J >= k`, the number of slopes `z` whose forced ray `f+zg` has agreement `>= A` is at most `floor((n-J)/(A-J))`.
*Proof.* `S_z \ Z_P` has size `>= A-J` and, by the THEOREM-2 argument, these sets are pairwise disjoint over distinct `z` inside the `n-J` points off `Z_P`. QED
**Precision note:** the banked `critical/nodes/common_code_line_budget` prints the same formula but under the hypothesis `a + b - n >= k`, which at the six rows evaluates to `2k+h+d-n < 0` — **the banked node does not cover the band**. The applicable hypothesis is `J >= k` (interpolation), and the four-line proof above is the one that must be banked. Also strictly sharper than the F5 sunflower form `(n-k)/(t-d)`.
**Verified tight at every depth**: `L = cap` exactly at `d = 1, 2, 3` (`2, 3, 4`) in the depth-sweep fixtures; and `L = cap+1` is unrealisable by point count.

**THEOREM 4 (ray rigidity — new, not found in the tree).** Two distinct codeword pairs with `|Z| >= k` are subordinate to **at most one common ray**, and only if `f_1 - f_2 = -z(g_1 - g_2)` as polynomials — which determines `z` uniquely.
*Proof.* Subordination to `(z,c)` forces `c = f_i + z g_i` (interpolation on `Z_i`). Equating, `(f_1-f_2) = -z(g_1-g_2)`. If `g_1=g_2` then `f_1=f_2`, contradiction; otherwise `z` is the unique scalar of proportionality. QED **Verified: 0 violations and the proportionality identity confirmed at every shared slope, across all fixtures (largest single fixture: 1.15M pair comparisons; battery total > 4e7).**

**THEOREM 5 (union agreement — the upgrade mechanism; new).** If `(f_1-f_2) = -z*(g_1-g_2)` for some `z* in F_q`, then `c := f_1+z*g_1 = f_2+z*g_2` agrees with `u+z*v` on **all of `Z_1 u Z_2`**.
*Proof.* On `Z_1`, `u+z*v = f_1+z*g_1 = c`; on `Z_2`, `u+z*v = f_2+z*g_2 = c`. QED
**COROLLARY (band interaction strip).** With THEOREM 1, `|Z_1 u Z_2| >= J_1+J_2-(k-1) = k + d_1 + d_2 + 1`. So **`d_1 + d_2 >= h` forces a T2/P2 tangent event** and the received pair leaves the generic branch entirely. In particular, for `h >= 4` (RowC 1/4, 1/8 and all three prize rows) **two top-of-band pairs can never have proportional differences in the generic branch**. When `|Z_1 ^ Z_2| = k-1` exactly, proportionality is *automatic* by degree (both differences are constant multiples of the degree-`(k-1)` vanishing polynomial of the overlap) — so that whole configuration class is stripped.
**Verified exactly:** fixture `INT-forced-tangent` — differences proportional `True`, `z* = 57`, agreement at `z*` = `10` = `|Z_1 u Z_2|`, `A = 9`, tangent forced `True`.

**THEOREM 6 (slope-fibre = punctured-MDS list; new).** Fix a ray `(z,c)`, `z != 0`, support `S`, `|S| = A`. The pairs subordinate to it with `|Z_P| >= k` are in bijection with codewords `g` of the punctured code `C|_S` (an `[A,k,h+1]` MDS code) with `|{i in S : g(x_i)=v_i}| >= k`, via `P = (c - zg, g)`, `Z_P = {i in S : g(x_i)=v_i}`.
*Proof.* `c = f+zg` gives `f = c-zg`; for `i in S`, `u_i+zv_i = c(x_i)`, so `u_i = f(x_i) <=> z v_i = z g(x_i) <=> v_i = g(x_i)`. QED
**Consequence (a warning, not a tool):** per-ray band multiplicity is exactly an MDS list size at agreement `k+1` out of `A`, i.e. **far below the Johnson radius** (`sqrt(kA) ~ k + h/2`). It is not polynomially bounded by anything banked. Hence the master inequality can be **arbitrarily lossy**, and a sharp ledger must eventually count slopes directly, not sum over pairs.

**THEOREM 7 (two-column determinacy — new; the anti-concentration lever).** Write `zeta_P(i)` for the unique `z` with `(u_i-f(x_i)) + z(v_i-g(x_i)) = 0` — geometrically, the pencil direction of the line joining the received point `(u_i,v_i)` to the pair's centre `(f(x_i),g(x_i))` in `A^2`. Then for any two pairs with `zeta_{P_1}(i) != zeta_{P_2}(i)`, the values `(u_i,v_i)` — and hence `zeta_P(i)` for **every** other pair — are determined by that ordered pair of directions.
*Proof.* The `2x2` system `u + z_s v = f_s(x_i)+z_s g_s(x_i)` has determinant `z_2-z_1 != 0`. QED
This is why my shared-block attack could steer exactly **two** pairs per coordinate and no more, and it is the natural handle for the missing occupancy lemma (band occupancy becomes a point-line incidence count in `A^2`). The banked `zeta_c(x)=(c(x)-u(x))/v(x)` (F5_SKELETON) is the one-sided `g=0` special case; the centre-and-direction form for codeword *pairs* I did not find in the tree.

---

## 3. CONJECTURE (the single named gap)

**BAND OCCUPANCY LEMMA (open).** At each of the six clean-rate rows, for every globally generic, tangent-stripped received pair and every `d in [1, h-2]`:
`N_d <= 0.68 n^2` (prize 1/16 binding; row-exact thresholds below).
Equivalently, in aggregate: `SUM_d N_d L(d) <= 13 n^3`.

This is precisely "the F5-OS anti-concentration heart re-posed one notch above `k`" — the same species as P-A1's own open heart at `d=0`, and **Route W needs it too**.

---

## 4. EXACT PRICING (`band_arith.py`; recomputes `B*`, `B_quot_ub`, `s_lo` from scratch — all banked pins reproduced, ALL CHECKS PASS)

| row | h | band depths | `SUM_d L(d)` | printed `n-A+1` | fits printed? | required uniform `N_d` for the headroom |
|---|---|---|---|---|---|---|
| RowC 1/4 | 5 | 3 | **828** | 764 | **NO** | ~6.4e61 (vacuous) |
| RowC 1/8 | 5 | 3 | **967** | 892 | **NO** | ~5.5e61 (vacuous) |
| RowC 1/16 | 3 | 1 | 479 | 958 | YES | ~1.1e63 (vacuous) |
| prize 1/4 | 2^33+1 | 2^33-1 | **3.684e13** | 1.641e12 | **NO** | 4.00e24 = **0.827 n^2** |
| prize 1/8 | 2^33+1 | 2^33-1 | **4.301e13** | 1.916e12 | **NO** | 3.43e24 = **0.709 n^2** |
| prize 1/16 | 2^32+1 | 2^32-1 | **4.476e13** | 2.057e12 | **NO** | 3.29e24 = **0.681 n^2** |

Headroom recomputed, not quoted: `s_lo = B* - B_quot_ub - (n-A+1)`; `floor(s_lo/n^3) = 29` on prize rows, `s_lo - 16n^3 = 13.857 n^3` (RowC: astronomically larger, `~2^122`, so RowC never binds).

Columns implied by candidate occupancy bounds (units of `n^3`, prize 1/4 / 1/8 / 1/16):

| bound | column | `<= 13n^3`? |
|---|---|---|
| `N_d <= n` | 7.6e-12 / 8.9e-12 / 9.3e-12 | YES, with vast room |
| `N_d <= n^{3/2}` | 1.13e-5 / 1.32e-5 / 1.37e-5 | YES |
| `N_d <= C(n,2)` | 8.38 / 9.78 / 10.18 | **YES** |
| `N_d <= n^2` | 16.75 / 19.56 / 20.36 | **NO** (fails by 1.21-1.47x) |
| `N_d <= n^3` | 3.7e13 / 4.3e13 / 4.5e13 | NO |

**The `n^2` / `n^2/2` boundary is where this lives.** `N_d <= n^2` misses; `N_d <= n(n-1)/2` clears.

**Correction to a prior expectation.** "A per-depth sum that grows with `h` is DEAD" is *too crude*. `SUM_d L(d) = R * (H_{h-1} - 1) ~ 22.3 R` — **harmonic, not linear in `h`** — because `L(d)` decays as `R/(h-d)`. A *fixed cost per depth* of up to `3548 n^2` still fits the headroom on prize rows. What is dead is an `n^3`-scale column per depth (short by ~6.2e8). The band's astronomical width is survivable; the harmonic structure of the line cap is what saves it.

**Cascade separability (explicit, as requested).** `L(h-1) = n-A+1` **exactly**, on all six rows (verified) — the printed tangent column is precisely the cost of one cascade pair, and exactly two saturated top-of-band pairs (`(n-A+1)/L(h-2) = 2.0000`, all six rows). If the parallel audit finds the cascade tier **unpaid**, extend the ledger to `d in [1,h-1]`; the added term needs only `N_{h-1} <= 18.5 n^2` — a **27x weaker** requirement than the band's own `0.68 n^2`. **The ledger's feasibility therefore does not depend on the cascade audit's outcome**; only the phrasing of its upper endpoint does.

---

## 5. FIXTURE BATTERY (`bandlib.py` + `battery.py`; 8 checkpoint JSONs)

Every fixture is gated **exhaustively** before any number is read off it: one pass over all `k`-subsets recovers *every* codeword pair with joint agreement `>= k` and *every* ray with agreement `>= A` together with its full agreement set (both exhaustive by interpolation-uniqueness). Gate = globally generic **and** below cascade **and** no over-agreement ray **and** `v` nowhere zero.

| fixture | shape | result |
|---|---|---|
| **V1** (validation) | `n=14,k=5,t=4,J=7,L=3`, 3 seeds | reproduces the banked `planted_band.py` exactly: cores `{7:3}`, `L=3`, banked `floor(R/h)=2` **violated**, widened cap `3` tight. (One of my three re-drawn seeds was *rejected* by the gate — over-agreement 10 — showing the gate is non-vacuous; the banked fixtures themselves are clean, `max_ray_support=9`.) |
| **S1** saturation | `n=16,k=5,t=4,J=7,L=4` | `L = cap = 4` achieved; `L=5` needs `7+10=17 > n` — cap unbeatable by point count |
| **Depth sweep** | `n=16,k=4,t=5`, `d=1,2,3` | `L = cap = 2,3,4` at every depth: **the line cap is tight across the whole band**, not just at the top |
| **M1** 2 cores, disjoint blocks | `n=20,k=5,t=4` | admissible; column 4-5 vs printed 12 |
| **M2** 2 cores, **shared blocks** | `n=16,k=5,t=4`, overlap `k-1` | **column 14 > printed 8 — the only fixture that beat the printed column** — but **NOT admissible**: forced ray of agreement `10 > A`. Refuted by THEOREM 5, verified numerically. The shared-block construction also *spontaneously generates* 3 extra depth-1 band pairs (also predicted by the mechanism). |
| **M3** 3 cores | `n=27,k=5,t=4`, 24 builds | best admissible: 5 band pairs (2 at `d=1`, 3 at `d=2`), 10 band slopes, column 12 < printed 19 |
| **Random adversarial search** | 5 shapes x 400 samples (~2000 fixtures) | 97-100% admissible; **max column 5 vs printed 7 — nothing beat the printed column** |

**Invariants across the entire battery: 0 violations** of the k-packing (both the direct pairwise form and the exhaustive `count(Z) = C(J,k)` form), the T2 fibre identity, the line cap, and ray rigidity (with the proportionality identity confirmed at every shared slope). The banked `kappa=k` cap `floor(R/h)` was **violated repeatedly** on verified-admissible fixtures, independently re-confirming the earlier pilot's central measurement.

**Result that IS a result:** the shared-block doubling attack is the natural way to beat the column (each free coordinate can be steered for **two** pairs at once — THEOREM 7), and it **does** beat the printed column — but at maximal overlap it is automatically proportional, hence automatically tangent, hence stripped. At overlap `<= k-2` the arithmetic of the family gives column `~ R-2h+2 < R-h+1 = ` printed, so that family cannot beat it either. Multi-core band configurations proved strongly tangent-prone in construction (most builds died on the gate) — evidence that **the tangent strip already charges more of the band than the tree credits it with**.

---

## 6. ROUTE T vs ROUTE W — honest comparison

| | Route W (widen P-A1) | **Route T (graded band ledger)** |
|---|---|---|
| new mathematics | the widened P-A1 at `kappa=A-2` = exact-`k` heart **+ band occupancy** | **band occupancy only** (a proper sub-obligation) |
| PROVED nodes re-scoped | ~10 (uniform-cell / Maxwell / shell-exclusion fan) | **0** |
| prize paid ranks | `15,15,14 -> 11,11,10` | **unchanged** |
| budget | new `4n^3` sub-column, `13n^3` headroom | new third column, `13n^3` headroom, **must not** enlarge `B_tan` |
| P-B | verbatim | verbatim |
| bridge R2 edit | required | required (common to both) |

**Recommendation: take Route T.** Both routes are gated by the same missing occupancy input; Route T pays for it without touching the banked exact-`k` machinery. The band column must be **its own third generic column** from the `13n^3` headroom — never by enlarging `n-A+1` (dead on 5/6 rows) and never by splitting the `8n^3` (catch #158 / the 0.5005% AZC margin).

---

## 7. FILE INVENTORY (all under `notes/pilots_20260802/xr_graded_band_ledger/`)

- `band_arith.py` / `band_arith.json` — exact six-row pricing; recomputes `B*`, `B_quot_ub`, `s_lo` and reproduces every banked pin; divisor-block evaluation of `SUM_d L(d)` at `h ~ 2^33` (validated against brute force at RowC); scheme-(a) kill; interleaving-route arithmetic. ALL CHECKS PASS.
- `bandlib.py` — exhaustive toy engine (`O(nk)` per `k`-subset, barycentric).
- `battery.py` — fixture battery, groups `v1 s1 depth multi shared interact triple search`.
- `battery_{v1,s1,depth,multi,shared,interact,triple,search}.json` — checkpoints.

Nothing written outside this directory; no commits, no pushes; nothing m2-related. All runs under `tools/ramguard local -- python3`.

---

## 8. HONEST CAVEATS

1. **The master inequality can be arbitrarily lossy.** THEOREM 6 shows many band pairs can be subordinate to one ray, so `SUM_d N_d L(d)` over-counts slopes. A sharp ledger should count `|Gamma_band|` directly; the `0.68 n^2` threshold is therefore *sufficient*, not necessary.
2. **`N_d` is not bounded by anything banked.** The banked interleaving collapse (`list_subsqrt_interleaving_collapse`, pointwise in the agreement threshold) does give `N_d <= L_2(k+d) <= L(k+1)` under `L(k+1)^2 < q` — but `L(k+1)`, the RS list size at the *lowest nontrivial* agreement, is astronomically above `n^2` even on average (`~C(n,k+1)/q`). **True but vacuous**; do not cite it as progress.
3. **Toy scale.** Everything empirical is `n <= 27`, `q <= 101`. The fixtures establish tightness, admissibility, and the refutation of the shared-block attack; they say nothing about band population at official `A`.
4. **Selection.** All fixtures had `max_rays_per_slope = 1`, so slope-indexed and ray-indexed rigidity coincide there. THEOREM 4 is stated for **rays**; the program's per-slope *selection* step means a slope with several exact-`A` rays could be re-selected. My fixtures show **no re-selection freedom ever arises** (0 slopes with >1 ray), so "Route S" (dodge the band by re-selecting supports) has no purchase — worth recording as a killed alternative, not a proven impossibility.
5. **Two claims I nearly banked as new were already in the tree** (k-packing at `xr_mismatch_chart_...:19-22`; the line-cap *formula* at `common_code_line_budget`, though under a hypothesis that fails at the six rows). I checked before claiming; the four genuinely new items are THEOREMs 4-7.
6. **Not audited by me:** whether the tangent column `n-A+1` actually pays the cascade tier (the parallel pilot's job). My design is explicitly separable from it (section 4) and the extension is cheap.
7. `band_arith.py` section 4/9 prints RowC's (vacuous, ~1e61) thresholds in a float field and overflows the column width — cosmetic only; the JSON carries exact integers.
