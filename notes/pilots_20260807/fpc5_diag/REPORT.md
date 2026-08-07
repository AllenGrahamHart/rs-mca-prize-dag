# REPORT — fpc5_diag (persisted verbatim by the coordinator from the session transcript, task a1f7a9281cb13bb84, 2026-08-07)

All artifacts confined to `notes/pilots_20260807/fpc5_diag/`. No node, dag, or tool touched; no git writes; quarantine held (the `ge_lattice_cert` entries in `git status` are another pilot's — I never opened them).

---

# FPC5 DIAGNOSIS — the three new reds classified

**Headline: all three are the SAME mystery, and I can now say exactly which one, in one line.** The FPC5 first moment is not a problem anywhere — I derived and checked an exact identity showing the F-flat's codimension **equals the reserve σ**, so the mean occupancy is below 1 by the corrected reserve itself (margin `2^(-7.95e12)` at the official rate-half row). What is left in all three is max-to-mean for a split-locator flat of projective dimension Θ(n) — the master split-locator flatness wall the audit already names. The mandatory adversarial attempt **failed** at reachable scale, and it failed against a hard, q-invariant, ell-invariant cap of **4** that I found by an attack the banked work had not tried.

---

## 0. Self-corrections and compliance, stated plainly

1. **COMPUTE-LAW SLIP (mine).** One command in this session piped through a bare `python3 -c` JSON pretty-printer (`cat file | python3 -c ...`) instead of `tools/ramguard`. It **errored and produced no output** (the shell fell through to `head`), and **no number in this report comes from it**. Every measurement below ran under `tools/ramguard tiny|local -- python3 ...` from the repo root. Flagging it rather than hiding it.
2. **H3, corrected before registering.** I initially reasoned that `t &gt;= M+1` was reachable, which would have handed red 3 free pair-uniqueness. It is impossible: `t` counts petals touched, `M` petals exist, so `t &lt;= M`. Registered as H3 in PREREG before computing.
3. **Unsound prune, caught and fixed mid-run.** My first max-packing branch-and-bound pruned on "each further member adds ≥1 new point". A member can add **zero** new points. Re-ran with the sound bound `len(chosen)+(m-i)`; **the answer did not change** (4 at `ell=4,q=97`, 25 trials; 4 at `q=193`, 3 trials).
4. **Registered P6 threshold was vacuous.** I registered "FALSIFIED if ≥50% of non-base members have `g &gt;= h-2`". At `h=ell-2a=2`, `h-2=0`, so the test is trivially 100%. Useless as written; I report the measured distribution instead and draw the substantive conclusion from it.
5. **Registered cells not executed:** `ell=6, q=157` for P3 (cost: `binom(25,9)=2,042,975` subsets × ~300 cells needed for one hit — infeasible under the 5-min guard); **A4, the μ_7-period attack at `ell=5, n=42`, was registered and NOT run.** Both are honest gaps, not silent omissions.
6. **The strong adversary uses a relaxation.** Its FREE-DOMAIN regime lets the adversary choose the n-point evaluation domain; the official domain is `mu_n`. I ran the honest MU-DOMAIN regime too and report both. I also did **not** verify sunflower-source *maximality* for the constructed cells — an unchecked guard on the free-domain construction.
7. `rh_adversary.py` (a hill-climb) was written but superseded by `rh_pack_adversary.py` before running; it contributes no numbers.

---

## 1. Two structural facts I derived, then checked

### (I) The codimension–reserve identity — `codim = σ` exactly

For a full-petal contributor with `t` touched petals, exact core defect `d`, background agreements `r`, core `N=|C|=k-1`:

- agreement `A = (N-d) + r + t·ell`, so by definition `sigma = A - k = t·ell + r - d - 1`;
- the linear system on `W` (deg ≤ d, `L_i | (W - c_i F)` for `i=1..t`, `W=0` on `R`) imposes `t·ell + r` conditions on `d+1` unknowns, so the induced conditions on `F` number **`t·ell + r - (d+1)`**.

Hence **codim(F-flat) = σ**, identically. Verified by exact integers for both printed families (`fpc5_exact.py`, `IDENT_codim_equals_sigma`):

| family | codim | σ | checked |
|---|---|---|---|
| rate-half `M=4,t=2` sharp (`t=2, r=b=ell-3, d=2ell-3`) | `ell-1` | `ell-1` | `ell` 4..39 |
| rate-half `M=4,t=3` LS6, `R` empty (`t=3, r=0, d=2ell-a`) | `ell+a-1` | `ell+a-1` | `ell` 8..39, all `b,a` |

Both match the nodes' own printed codimensions: `l1_fpc5_ratehalf_m4_t2_payment/statement.md:70-73` prints
```text
P(V_F) intersect D_(2ell-3)(C),
|C|=5ell-5,       dim P(V_F)=ell-2,
affine codimension=ell-1.                              (RH1)
```
and `l1_fpc5_ratehalf_m4_t3_master_flat_descriptor/statement.md:23-24` prints `projective dimension: r=ell-2a+1; projective codimension: j-r=ell+a-1`.

**Consequence.** First moment `= binom(N,d)/q^sigma &lt;= binom(n,k+sigma)/q^sigma`, which the corrected reserve (`imgfib/statement.md:9`: *"once sigma log2(q_D) &gt;= (1+eps) log2 C(n, k+sigma)"*) forces below `2^(-eps·sigma·log2 q)`. At the sharp rate-half official cell (`k=2^40`): `ell = 219,902,325,556`, `d = 439,804,651,109`, `sigma = 219,902,325,555`, `log2 binom(N,d) = 1.0676e12`, `sigma·log2 q &gt;= 9.016e12`, so **`log2(first moment) &lt;= -7.948e12`**. Independent cross-check: my `ell` and `d` reproduce the banked constants `official_ell == 219902325556` and `official_j == 439804651109` asserted in `l1_fpc5_ratehalf_m4_t2_sharp_dyadic_quotient_absence/verify.py`.

**None of the three reds is a first-moment problem.** All three are max-to-mean.

### (II) `e` IS the flat dimension — the shape-pun statement

Each petal imposes `ell` conditions on the `2(d+1)` coefficients of `(F,W)`, so the ambient `t`-petal slice has dimension `&gt;= 2d+2-t·ell = e+1`. So FPC5's clause (`CONJECTURE_F_FALSE_GREEN_AUDIT_20260807.md:87-88`)
```text
M&gt;=4,  d&lt;ell(M-2),  t&lt;2M-4,
max(0,2d+1-t ell)-&gt;infinity.                         (FPC5)
```
literally says: *count split-on-core locators in a flat whose dimension grows*. One parametrized statement,

&gt; **(MF)** Count monic degree-`d` locators split on `C` inside a linear flat of projective dimension `e = 2d+1-t·ell` whose codimension is exactly `sigma`.

specializes **exactly** to red 1 (`t=2`, guarded: proj dim `ell-2`, codim `ell-1=sigma`), to red 2 (`t=3`: proj dim `ell-2a+1`, codim `ell+a-1=sigma`), to red 3 (all `t`), and to the upstream `prob:capfr1-master-flatness` target the audit names at `notes/CONJECTURE_F_FALSE_GREEN_AUDIT_20260807.md:51-54`. **The shape-pun test passes** — this is not a family resemblance, it is one statement.

---

## 2. Red 1 — `l1_fpc5_ratehalf_m4_t2_payment`

### D1 — consumer contract, quantified
Router asks (`l1_full_petal_fpc5_payment/claim_contract.md:6-8`): *"one disjoint polynomial payment or one legitimate quotient/profile owner, with aggregate multiplicity preserved."* Currency: `#ImgFib_U(k+sigma) &lt;= n^B` (`imgfib/statement.md:9`) against the exact banked allowance `floor(n^6/C(n+6,6)) = 719` columns at exponent 6 (`petal_staircase_allowance_719/statement.md:6-20`), with `petal_growth/conditional.md:89-95` forbidding the `log2(6!) = 9.4919` bits of slack. Scope: **one fixed maximal `M=4` source**, 6 touched pairs, all `(s,R)` cells; `+4` anchors globalize by `l1_general_first_layout_domination` (GL7: `M&lt;=n/ell&lt;=log_2(n)/c_0`). This is the **loosest** of the three contracts — a single fixed source must fit in ≤719 columns.

### D2 — the obstruction made exact, and MEASURED
I built the guarded congruence kernel explicitly, via an independent CRT route (`W = rem_P(F·G)`, `P=L_0L_1L_2`, `G=c_1e_1+c_2e_2`) rather than the banked cofactor route.

**A1 replication gate — PASS** at the banked cell `(n,k,ell,M,b,s,d)=(32,16,4,4,1,1,5)` over `H_32 ⊂ F_97^*`, 240 (source,pair) cells: `dim V_F = 3 = ell-1`, syndrome rank 3, locator codimension 3. Matches `l1_fpc5_ratehalf_m4_t2_codimtwo_guarded_slice` (GS5)/(GS6) exactly.

**The count the payment must bound** (functionals named per CATCH-19C): `N_split(source,pair) = #{D ⊂ C, |D|=d : L_D ∈ A_F}`; `N_prim` adds `gcd(F,W_F)=1`; `N_exact` adds untouched-petal nonagreement. Prediction `mu_t2 = binom(5ell-5,2ell-3)/q^(ell-1)`.

| cell | domain | cells | `mu_t2` | mean `N_split` | ratio | max `N_exact` |
|---|---|---|---|---|---|---|
| `ell=4, q=97` (**2-power, μ_32, the banked cell**) | μ_n | 5400 | 3.2903e-3 | 2.778e-3 | **0.844** | 1 |
| `ell=4, q=37` | free | 5400 | 5.9286e-2 | 6.352e-2 | **1.071** | 2 |
| `ell=5, q=43` (NON-2-POWER) | μ_n | 768 | 2.2675e-2 | 2.083e-2 | **0.919** | 1 |

**P3 CONFIRMED** at 3 of 4 registered cells (the 4th, `ell=6,q=157`, was not run). The guarded flat is **first-moment generic** — no bias, no anomaly.

### The scope catch (P2 CONFIRMED — this one matters)
`l1_fpc5_ratehalf_m4_t2_sharp_cell_nonemptiness/statement.md:18-20` banks
```text
41 nonempty layouts,
71 primitive exact contributors,
maximum five in one layout.
```
That is **71 over 50 layouts × 6 pairs = 300 cells = 0.2367 per cell**. Its solver *derives* the label ratio `λ` from the second-petal system (`proof.md:11`: `W_1(x)+lambda W_2(x)=lambda F(x)`, solved exactly) — so `λ` is **free**, worth one extra dimension. My fixed-source measurement at the identical cell gives **0.002778 per cell**, a factor **85** smaller; the predicted inflation is exactly `q = 97`. Agreement to 13%.

**This is not an error in the node** — the certificate's stated job is nonemptiness, and its own `claim_contract.md:9` disclaims *"an official-row contributor, or payment of the rate-half target."* But it is a scope pin worth carrying: **the object the payment must bound is ~q times smaller than the banked census suggests**, and the route-cut headline "41/50 layouts nonempty" reads, for a *fixed* source, as "≈1 source in 300 is nonempty at all."

### D3 — MANDATORY ADVERSARIAL: attempted, and it FAILED against a hard cap

The registered random-source search is weak, and I found why. **The guarded flat `V_F` does not depend on `C` at all** — it is determined by `(L_0,L_1,L_2,c_1,c_2)`. So the real adversary fixes the background and petals, enumerates the whole monic chart `A_F` (`q^(ell-2)` points), keeps every member that is squarefree and fully split off the petals, and then **chooses the core** to contain as many of their root sets as fit in `5ell-5` points. That is a set-packing problem the banked work never poses, and it is a strictly stronger attack than anything in the node's `attack.md`.

Result, with **exhaustive** branch-and-bound over all split members (sound bound):

| cell | regime | trials | split members/cell (mean, max) | **max packed** | escape threshold `4(ell-2)` |
|---|---|---|---|---|---|
| `ell=4, q=97` | FREE | 25 | 20.6, 29 | **4** | 8 |
| `ell=4, q=193` | FREE | 3 | 162.0, 172 | **4** | 8 |
| `ell=4, q=389` | FREE | — | (timed out) | — | 8 |
| `ell=5, q=127` (chart sampled 3e5 of 2,048,383) | FREE | 5 | 10.6, 14 | **4** | 12 |
| `ell=5, q=43` | **MU (official)** | 6 | **0.0, 0** | **0** | 12 |

**Neither pre-registered escape test fires.** `ESCAPE-RH(a)`: max `N_exact = 4 &lt; 8`. `ESCAPE-RH(b)`: max is 4 at `ell=4` and 4 at `ell=5` — flat, not doubling.

**The mechanism that stopped it, quantified.** The cap is **4 and stays 4 when the number of split chart members grows 8-fold** (21 → 162 as `q: 97 → 193`). That q-invariance is the finding: this is not a small-sample artifact and not a counting accident. Adversarial core placement buys **~1200x over the mean** (4 vs 3.3e-3) and **2x over the best random source**, and then stops dead. On the official `mu_n` domain at `ell=5` the adversary finds **nothing at all**.

**A DERIVED sharpening of the node's own instrument, checked on the witnesses.** `l1_fpc5_ratehalf_m4_t2_joint_support_distance` (JD1) proves `|D∩D'|+|R∩R'| &lt;= 2s`. At the sharp cell `r=r'=b=ell-3` is *forced* (every background point is an agreement — `CONJECTURE_F_FALSE_GREEN_AUDIT_20260807.md:141`: *"Thus every background point is an agreement"*), so `|R∩R'| = b` and
```text
|D intersect D'| &lt;= 2s - b = ell-3          (sharpened, not 2s = 2ell-6)
```
Every measured witness obeys it exactly: at `ell=4` all six pairwise root overlaps of the 4-packing are `&lt;= 1 = ell-3`; at `ell=5` all are `&lt;= 2 = ell-3`. Feeding `lambda = ell-3` into the packing instead of `2s` improves (RH0b) from `2^(2.755·ell)` to `2^(1.61·ell)`. **Still not a payment** — and it cannot be, because `l1_fpc5_ratehalf_m4_t2_distance_only_no_go` fences every distance-only route at `2^((0.099865...+o(1))(ell-2))` (`statement.md:59`).

### D4 — cross-lane matrix (applies / fails-because)

| instrument | red 1 | why |
|---|---|---|
| rate-quarter uniqueness (`2ell&gt;k-1`, `proof.md:5-8`) | **FAILS** | needs `t·ell &gt; k-1`; here `2ell` vs `5ell-5`, true only for `ell&lt;5/3` |
| `l1_general_first_layout_domination` | **APPLIES** | proved; `+4` anchors; `M&lt;=log_2(n)/c_0` (GL7). Not the bottleneck |
| LS6 determinant chart + canonical owner packing | **FAILS** | needs the `Etilde` multiplier / Padé coordinates; the m4_t2 guarded flat is a background-congruence kernel with no such multiplier |
| mystery 6's counting laws (`Λ=2ell+b-2`, `BOX=Θ(n^(4ell+2b-4))`, empty once `σ&gt;Λ`) | **FORM transfers, CONTENT does not** | the emptiness law *is* my `codim=σ ≥ 0`; but mystery 6's rescue was `BOX = Θ(n^6)` at `ell=2` (`l1_pma_diag/REPORT.md:34`), a *counting fact*. Here the box is `binom(N,d)` with `d ≈ 0.4N` — exponential. **FPC5 cannot be rescued the way mystery 6's clause (a) was.** |
| exact-shell / Hankel prefix machinery | **FAILS** | no prefix/shell coordinates in the guarded flat (it *does* apply to red 2 — see below) |
| Johnson / Plotkin / distance packing | **APPLIES AS A NO-GO** | fenced at `2^(0.0998(ell-2))` |
| dyadic quotient absence | **APPLIES, but by arithmetic luck** | `d=2ell-3` odd, `n` a 2-power. At my toy `ell=5, n=42, d=7` a `mu_7` pullback is arithmetically admissible — **I registered A4 to hunt it and did not run it** |

### D5 — VERDICT: **MYSTERY-HARD**, sharing the master split-locator flatness wall
The concreteness bar is the PROVED sibling's over-determination (`2ell&gt;k-1` ⇒ two codewords agreeing on a touched pair coincide ⇒ absolute bound `6+4=10`). **No over-determination exists at rate half** — the flat has projective dimension `ell-2 = Θ(n)`, and every cheap route is already proved shut: emptiness (certificate), flat-wide gcd (GT2), pure dyadic pullback (QA1), distance-only (Gilbert fence). Verdict: mystery-hard, same wall as `prob:capfr1-master-flatness`, shape-pun test passed against red 2.

**Cheapest decisive next probe.** The measured cap `4` is the first positive lead this node has ever had. At `ell=4` the chart is a **2-dimensional affine plane**, so "can 5 split members share a 15-point core?" is a *finite, decidable* question over each `q`. Probe: at `ell=4`, enumerate over all `(L_0,L_1,L_2,c_1,c_2)` up to affine equivalence (the reduction is small) and either exhibit a 5-packing or prove `&lt;=4` at that `ell`. Cost: hours, not Modal. Free rider: bank the sharpened overlap cap `|D∩D'| &lt;= 2s-b` (a two-line addendum to `joint_support_distance`, already checked on witnesses).

---

## 3. Red 2 — `l1_fpc5_ratehalf_m4_t3_split_slice_payment`

### D1 — consumer contract, quantified
`first_layout_atom_collapse` (AC2) gives `#FPC5_(M=4,t=3) &lt;= 4n·B(n)+4` with **fewer than `4n`** `(triple,a)` atoms (`statement.md:26`). So to land inside the 719-column, exponent-6 allowance, the **per-atom** bound must be `B(n) &lt;= n^(B-1)/4` — i.e. the atom-level payment must beat the global exponent by a full power of `n`. That is the tightest contract of the three.

### D2 — the obstruction made exact
**P5 CONFIRMED, and it is a hard fact about reachability.** Exhaustive integer search over `b&gt;=7`, `b&lt;ell`, `1&lt;=a&lt;=floor((b-3)/4)`, `J = ell(4a-b+2)+a^2+2ab-4a &lt;= 0` (cross-checked against the primitive `J = d^2-N(e-1)` at every point) for `ell&lt;=400` finds **1,909,782** live cells, the smallest being

```text
(ell,b,a) = (9,8,1),  N=|C|=42,  j=17,  n=86,  k=43,  J=-5,
binom(42,17) = 254,661,927,156.
```

**The live LS6 tail cannot be instantiated at any local scale, ever.** Not by subset census (`2.5e11`), not by chart enumeration (`q^(ell-2a+1) &gt;= 87^8 ≈ 3.3e15`). This is a qualitative separation from red 1, which *is* reachable at `ell=4`.

So I measured the **chart** (which is `J`-independent) at shape-matched OFF-TAIL cells, exactly, via last-coordinate bucketing (each pool point prescribes the unique last chart coordinate making it a root — one pass enumerates the entire split locus with no sampling).

`(ell,b,a)=(4,1,1)`, `q=101`, 25 trials, **full chart of 1,030,301 members enumerated exactly** per trial:
- slice dimension observed `= 4 = ell-2a+2` ✓ (matches (LS10)); `codim = sigma = ell+a-1 = 4` ✓;
- free-core atom size: mean **39.16**, max 49 — versus the generic prediction `q^r · binom(83,7)/q^7 = 39.9`. **Match to 2%.** No anomaly, no amplification;
- max core packing (exhaustive BB): **3**, never more. This is *exactly* the Bonferroni bound from the proved overlap cap `h=ell-2a=2`: `m·j - binom(m,2)·h &lt;= N` gives `3·7-3·2 = 15 = N` (feasible) and `4·7-6·2 = 16 &gt; 15` (infeasible). **The measured cap is the proved cap** — the pair-determinant instrument is tight here;
- **canonical-owner histogram** `g = |Z(D_0) ∩ Z(D_H)| = deg gcd(D_0,D_H)` over 954 non-base pairs: **`g=0`: 500 (52.4%), `g=1`: 335 (35.1%), `g=2`: 119 (12.5%)**.

### The sharp reading of the aggregation gap (this is the D2 payload)
`l1_fpc5_ratehalf_ls6_canonical_owner_packing` pays `|F_G| &lt; 3^(c+1)` where `c = h-g` (`statement.md:62-65`), and its own limit is `statement.md:76-77`: *"Summing `(CO7)` over all possible `G` can still be exponential."* The measurement says something sharper:

&gt; **The majority of the atom (52.4%) sits at `g=0`, i.e. under the SINGLE trivial owner `G=1`, whose co-deficiency is maximal (`c=h=ell-2a`) and whose (CO8) charge is `3^(ell-2a+1)` — exponential in `ell`.**

So the gap is *not* mainly "too many owners to sum" (there is one owner holding the majority). It is: **the fixed-owner packing theorem is worthless precisely on the chamber that holds most of the mass.** The node's attack list (`attack.md:36-39`: *"the live task is to coalesce the realized `G` strata or transport them to chronology-valid quotient/dihedral owners"*) is aimed at owner-multiplicity; the measurement says the binding problem is **owner-quality at `G=1`**, not owner-count. (Honest label: MEASURED at one off-tail cell, `h=2`; the trivial owner's share at larger `h` is untested — `ell=5` timed out.)

### D4 — cross-lane matrix
| instrument | red 2 | why |
|---|---|---|
| rate-quarter uniqueness | **FAILS** | `3ell` vs `k-1 = 4ell+b-3`; needs `b&lt;3-ell` |
| first-layout atom collapse | **APPLIES** | proved: `&lt;4n` atoms `+4` anchors, `lambda` determined not free |
| LS6 determinant chart / canonical owner packing | **APPLIES, and is exhausted** | fixed-owner top chambers paid; the mass is elsewhere (measured) |
| master flat descriptor (MF4 `&lt;=2^(-3ell-4)`) | **APPLIES as first moment only** | its own `audit.md:9-10`: *"Sub-balance is an average-scale statement and does not imply maximum flatness"* |
| **exact-shell / prefix machinery** | **THE ONE GENUINE CROSS-LANE HIT** | the low ladder `a&lt;=e&lt;=ell-a` has literal prefix coordinates of depth `h_e = ell+e-1` (PL4) with exact `Q_0^(e-a)` cancellation (PL5). `l1_exact_shell_prefix_hankel_bridge` is already an `ev` feeder of `imgfib`. **Hypothesis match should be checked explicitly — it was not, and I did not do it.** |
| mystery 6 counting laws | **FORM only** | same disanalogy as red 1: box is `binom(N,j)`, not `n^6` |
| Johnson / distance | **NO-GO** | `J&lt;=0` is the *definition* of the tail; and (PD8) shows the pair-determinant route re-derives the identical `J` |
| dyadic quotient absence | **PARTIAL** | odd `a` only; even-`a` and dihedral strata explicitly open (`master_flat_descriptor/statement.md:61-66`) |

**Notation hazard worth banking** (found while harvesting, not by me alone): `e` means `2d+1-3ell` in `pma_three_petal_projective_johnson_bound` but `deg Etilde` in the ladder/Padé nodes; `M` means `L_2L_3`, the petal count, *and* the pullback scale; `Q` means Euclidean quotient, field order `Q_0`, generated-field size `|B_0|`, and the layout polynomial. Two are self-flagged; the `e` collision is not, and `e-1 = h = ell-2a` only by coincidence of the `t=3` specialization.

**One quoting nit:** the target restates the supplier's `binom(n,j)/Q^(j-r) &lt;= 2^(-3ell-4)` as a strict `&lt;` (`split_slice_payment/statement.md:38` vs `master_flat_descriptor/statement.md:48`). Harmless in context; worth a one-character fix.

### D5 — VERDICT: **MYSTERY-HARD**, same wall as red 1, plus a strictly harder access problem
Shape-pun passes against red 1 via (MF). It is *worse* than red 1 in one respect and *better* in another: worse, because its live tail is provably unreachable by any census (`binom(42,17)`), so it can never be probed the way I probed red 1; better, because its chart is fully coordinatized and its residual is now a **single, named, measurable quantity**.

**Cheapest decisive next probe.** Since `g=0` holds the majority, the decisive question is the **base-cover number of the `G=1` stratum**: how many bases `D_0` are needed so that every member has `deg gcd(D_0,D_H) &gt;= h-c` for bounded `c` against *some* base? If that number is `O(1)`, the fixed-owner theorem composes and the atom is paid; if it grows, the route is dead. This is computable **from the data `ls6_bucket.py` already produces** (I have the root sets; it is a set-cover on the same 39-member atoms), costs minutes, and is a sharper question than "coalesce the `G` strata". Run it at `(4,1,1)` and `(5,1,1)` with several `q` and watch the `ell`- and `h`-dependence.

---

## 4. Red 3 — `l1_fpc5_large_source_payment`

### D1 — consumer contract, quantified
`statement.md:22-24`: *"The target is one disjoint polynomial/profile allocation across first-owned sources, touched-petal sets, defects, and exact owners. Raw enumeration of sources or touched subsets is not an admissible payment."* Scales: `M&gt;=5` (rates 1/2, 1/4), `M&gt;=7` (1/8), `M&gt;=15` (1/16), all with `2&lt;=t&lt;2M-4`, `d&lt;ell(M-2)`, `e-&gt;infinity`. It has **one** supplier (`pma_official_rate_small_source_degree_sieve`), no reduction theorem, no chart, no descriptor.

### D2 — "what exactly", made exact for the first time
Two derivations, both checkable:

**(a) Touched-subset multiplicity is NOT the obstruction.** By (GL7) `M&lt;=n/ell&lt;=log_2(n)/c_0` at the L1 cutoff (`l1_general_first_layout_domination/statement.md:68`), so `binom(M,t) &lt;= 2^M &lt;= n^(1/c_0)` — polynomial. The node's `attack.md:3` (*"Price touched-petal multiplicity and source multiplicity together"*) is aiming at something already free.

**(b) The Johnson sieve, computed exactly at `k=2^40`.** Under H4 (the `e-1` overlap cap — **PROVED at `t=2`** by the cofactor determinant, since `2s = 2d-2ell = e-1`; **PROVED at `t=3`** by (PJ2); **CONJECTURAL for `t&gt;=4`**), `J = d^2 - N(e-1)` with `N=k-1`, and `J&gt;0` ⟺ `d &lt; N(1-sqrt(1-t·ell/N))`. Exact integer enumeration over `M in [M_min, M_min+11]` at all four rates, at the low/mid/high ends of each admissible `ell` window:

| `(rate, M)` | `t` values with a nonempty `J&lt;=0` residual |
|---|---|
| `(1/2, 5)` | 2, 3, 4 |
| `(1/2, 6)` | 2, 3, 4, 5 |
| `(1/2, 7)` | 2, 3, 4, 5, 6 |
| `(1/2, M&gt;=10)` | **all** of 2..M |

**408 residual rows total.** Representative: rate 1/2, `M=5`, `t=2`, `ell = 183,251,937,963`, `b = 183,251,937,962` — Johnson pays only `d &lt; 201,764,143,008`, the FPC5 cap is `d &lt;= 549,755,813,888`, leaving a residual window of width **347,991,670,881** with `e` running up to **733,007,751,851 = n/3**.

**P7 CONFIRMED.** *Self-correction:* my hand estimate said `t=M` is always Johnson-paid; that assumed `b ≈ 0`. With `b` near `ell` the exact computation shows `t=M` has a residual for `M&gt;=10`.

**So the exact obstruction is:** for every `M&gt;=5`, at every rate, on a `d`-window of length `Θ(n)`, count degree-`d` locators split on `C` inside a flat of projective dimension `e` reaching `n/3` — with (i) **no mu-basis theorem at all for `t&gt;=4`** (`pma_three_petal_mu_basis_reduction` is a *three*-petal theorem, so even the quantity `J` is undefined there), (ii) **no background-guard analogue** (red 1's collapse from `2s+2` to `ell-1` used the sharp-cell forcing `r=b`; nothing comparable is proved for `M&gt;=5`), and (iii) the same `codim=sigma` first moment and the same max-to-mean wall.

### D3 — the registered ESCAPE-LS: **FIRES as an EXPOSURE** (as pre-registered)
I registered: *"SUCCEEDS IF the exact large-source cell enumeration exhibits a cell with `t=2` and `e` growing for which no proved instrument in the whole banked set applies — reported as an EXPOSURE, not a witness."* It does: rate 1/2, `M=5`, `t=2` has `e` up to `n/3` and the only instrument reaching it is a `t=2` cofactor determinant with no background guard and no chart. **This is not a violating witness** (no counterexample family constructed) and it does **not** re-pose the FPC5 partition. It is an honest statement that red 3 is the least defended of the three.

### D4 — cross-lane matrix
| instrument | red 3 | why |
|---|---|---|
| rate-quarter uniqueness | **APPLIES on exactly one stratum** | `t·ell&gt;k-1` ⟺ `(t-M)ell&gt;b-2`; since `t&lt;=M` (H3), this is `t=M` **and** `b&lt;=1` only |
| first-layout domination | **APPLIES** | `+M` anchors, `M=O(log n)` |
| small-source degree sieve | **APPLIES, already consumed** | it *defines* the `5,5,7,15` floors; pays nothing above them |
| three-petal mu-basis / projective Johnson | **APPLIES ONLY at `t=3`** | the `t&gt;=4` generalization does not exist |
| two-full-petal slice reduction | **APPLIES at `t=2`** | gives the envelope `dim 2s+2`, but no background guard at `M&gt;=5` |
| LS6 chart, owner packing, master-flat descriptor | **FAIL** | all are `M=4` constructions |
| mystery 6 counting laws | **FAIL** | mixed/partial-petal branch, disjoint by the fence at `l1_mixed_petal_amplification` |

### D5 — VERDICT: **MYSTERY-HARD, and the weakest of the three**
Same wall (MF), plus two *additional* missing pieces that reds 1 and 2 already have: a multi-petal reduction theorem and any guard at all.

**Cheapest decisive next probe (and it is genuinely cheap).** Prove or refute the `t`-petal generalization of the overlap cap:

&gt; for two distinct primitive members `(F,W)`, `(F',W')` of the `t`-petal slice, `|Z(F) ∩ Z(F')| &lt;= e-1`.

It is one lemma (the cofactor/syzygy determinant argument that already works verbatim at `t=2` and `t=3`), it is what makes the entire `J`-sieve legal, and **`fpc5_exact.py` is already written to consume it** — the sieve table above becomes a proved sieve the moment the lemma lands, removing the `t&lt;M`-with-`J&gt;0` cells at a stroke. Second-cheapest: port red 1's background-guard collapse to general `M` — the `codim=sigma` identity tells you in advance what the answer must be, which makes it a checkable target rather than an open search.

---

## 5. Predictions vs outcomes

| # | prediction | outcome |
|---|---|---|
| P1 | sharp `m4_t2` cells are 2-power only at `ell in {4,52,820,...}` | **CONFIRMED** exactly, `ell&lt;=4000`: `n = 32, 512, 8192`. Only `ell=4` is reachable — which is why the banked certificate is at `n=32` |
| P2 | banked 71/50-layouts is `lambda`-FREE; fixed-source mean within 10x of `mu`, not within 3x of `q·mu` | **CONFIRMED**: 0.002778 vs `mu`=0.003290 (ratio 0.844); vs `q·mu` ratio 0.0087. Banked cell density 0.2367 = **85x** the fixed-source mean; predicted factor `q=97` |
| P3 | `mean/mu ∈ [1/3,3]` at four cells | **CONFIRMED at 3 of 4** (0.844 / 1.071 / 0.919). `ell=6,q=157` **not run** |
| P4 | max does not double per `ell` | **HELD**: random-source max 2→1; adversarial max 4→4 |
| P5 | minimal `J&lt;=0` LS6 cell is `(9,8,1)`, `N=42`, `j=17`, `binom=2.5e11`, unreachable | **CONFIRMED** exactly; 1,909,782 live cells for `ell&lt;=400` |
| P6 | owner distribution concentrated at `g=0`, not `g&gt;=h-2` | **threshold VACUOUS at `h=2`** (my error). Measured: `g=0` 52.4%, `g=1` 35.1%, `g=2` 12.5% — the substantive claim (mass at the trivial owner) **holds** |
| P7 | `J&lt;=0` residual nonempty at rate 1/2, `M=5` | **CONFIRMED**: `t ∈ {2,3,4}`; 408 residual rows overall |
| P8 | both m4 reds are max-to-mean, first moment exponentially below 1 | **CONFIRMED and strengthened**: `codim = sigma` identically, margin `2^(-7.95e12)` at the official row |
| ESCAPE-RH (a)/(b) | fires if `N_exact &gt;= 4(ell-2)` or max doubles twice | **DID NOT FIRE**: 4 vs 8 / 4 vs 12; flat in `ell` and invariant under `q` |
| ESCAPE-LS6 | fires if atom grows `&gt;= q^(1/2)` per `ell`, or `sum_G |F_G| &gt; 3^(h+1)` | **DID NOT FIRE**; atom matched the generic prediction to 2%; packing = the proved Bonferroni cap |
| ESCAPE-LS (red 3) | fires as an EXPOSURE | **FIRED as registered** — `t=2, M&gt;=5`, `e` to `n/3`, no instrument |

---

## 6. Artifacts (all under `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260807/fpc5_diag/`)

- `PREREG.md` — brief + my registrations, appended before the first compute run
- `rh_m4t2_census.py` — CRT flat construction + **A1 replication gate** (`gate` mode, PASS)
- `rh_fast.py` — fixed-source census with prefilter (P2, P3, P4)
- `rh_pack_adversary.py` — **the core-choosable adversary** with exhaustive sound branch-and-bound (D3)
- `ls6_owner.py`, `ls6_bucket.py` — LS6 atom + exact bucketed chart enumeration + owner histogram (red 2)
- `fpc5_exact.py` — P1, P5, P7, the `codim=sigma` identity, official first moment (reds 1–3)
- `rh_adversary.py` — written, superseded, **not run**; contributes nothing

No node, `dag.json`, or tool was modified; no git writes; no Modal; every run under `tools/ramguard`. Quarantine held: `CAMPAIGN_LEDGER.md` read only to line 1834 (marker at 2786), and `cw_shared_target`, `ge_lattice_cert`, `c2pp_diag` never opened — by me or by any of the three subagents, each of which carried the clause verbatim.

**Bottom line for the board.** Three reds, one wall, no status flips. The audit's own next-step line (`CONJECTURE_F_FALSE_GREEN_AUDIT_20260807.md:164`) — *"count split core locators in the rate-half dimension-(ell-1) guarded congruence kernel, or attack the guarded LS6 max-to-mean gap"* — is exactly right, and this pilot supplies the first quantitative handle on both: a q-invariant packing cap of **4** on the first, and a measured 52% concentration on the worthless trivial-owner chamber on the second. Red 3 needs a lemma before it can even be sieved.
