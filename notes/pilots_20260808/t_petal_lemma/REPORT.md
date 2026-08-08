# REPORT — t_petal_lemma (persisted verbatim by the coordinator from the session transcript, task a4fb31b26cd8c4da6, 2026-08-08)

All writes confined to the pilot dir (the one file outside is an interpreter-generated `.pyc` from replaying the node's own verifier). Final report:

---

# VERDICT: **PROVED — at every `t`, not just `t &gt;= 4`.** And it was already banked in this repo.

## 1. The headline the board needs

The t-petal overlap-cap lemma is **clause 2 of an existing PROVED node**, `background/nodes/l1_fixed_support_defect_johnson_bound`, whose support pattern `X` has **arbitrary size `h`** and was never restricted to two or three petals:

- `background/nodes/l1_fixed_support_defect_johnson_bound/statement.md:39` — `|D_1 intersect D_2|&lt;=r_J;   (JB3)`
- `.../statement.md:30` — `r_J=2d-h,  e=max(0,r_J+1).   (JB2)`

Put `h = t*ell`: then `r_J = 2d - t*ell = e-1`, and `(JB3)` **is** `|Z(F) cap Z(F')| &lt;= e-1` verbatim. The consuming count `(JB4)` has denominator `d^2 - N*r_J` with `N=|C|=k-1` — which is the sieve's `J = d^2 - N(e-1)` exactly.

So the standing board claim at `critical/nodes/l1_fpc5_large_source_payment/statement.md:31-34` —

&gt; `(i) NO mu-basis / overlap-cap theorem exists for t &gt;= 4 (the three-petal theorems do not generalize as stated; even the Johnson functional J is undefined there)`

— **is wrong in both clauses.** The gap was bookkeeping, not mathematics. I replayed the node's verifier: `L1_FIXED_SUPPORT_DEFECT_JOHNSON_PASS sharp=3 boundary=6 local_not_global=24 set_cases=50 set_rows=991 positive=540112 tail=55552`, exit 0. Its `verify.py:45-58` already machine-asserts `support_locator * locator(intersection) | (w1*f2 - w2*f1)` and `len(d_1 &amp; d_2) &lt;= r_j` at arbitrary support size. All three of the node's dependencies are PROVED.

## 2. The general-`t` derivation — every step proved, none gapped

Write-up at proof standard: `notes/pilots_20260808/t_petal_lemma/LEMMA_TPETAL_OVERLAP_CAP.md`. With `Delta = F W' - F' W`:

1. **`Delta != 0`** — `gcd(F,W)=1` and `F | F'W` give `F | F'`; both monic of degree `d`, so `F=F'`, then `W'=W`. *Uses monicity + equal degree; nothing else.*
2. **`Lambda | Delta`** — mod `L_i`, `W = c_iF` and `W' = c_iF'`, so `Delta = c_iFF' - c_iF'F = 0`. **This step never mentions `t`**, and needs no distinctness of the labels `c_i`.
3. **`L_I | Delta`**, `I = Z(F) cap Z(F')` — `L_I` divides both `F` and `F'`.
4. **Coprimality** `gcd(Lambda, L_I)=1`, hence `Lambda*L_I | Delta`.
5. **Degree ledger** — `deg Delta &lt;= 2d`, so `h + |I| &lt;= 2d`, i.e. `|I| &lt;= 2d-h = e-1`. If `e&lt;=0` the slice has at most one member.

**Why `t=2,3` don't transcribe, and why it doesn't matter.** The `t=3` proof gets `deg H_12 &lt;= e-1` from the mu-basis budget `(BUDGET)` (`pma_three_petal_mu_basis_reduction/statement.md:127-131`), a **rank-2-syzygy** fact; at `t&gt;=4` the syzygy module has rank `t-1` and no two-generator budget exists. That is the real obstruction to transcription — and step 5 shows the budget is never needed: the degree bound is `deg Delta &lt;= 2d` minus `deg Lambda = h`, i.e. **counting degrees, not syzygy structure.** Concretely, expanding `(F_j,W_j) = u_j(F_p,W_p)+v_j(F_q,W_q)` bilinearly through `(DET)` gives `Delta = kappa * H_12 * Lambda`, so `(PJ2)`'s `H_12` (`pma_three_petal_projective_johnson_bound/proof.md:25`) is exactly `kappa^{-1}` times my cofactor. The mu-basis is a coordinate system, not an ingredient.

**Hypothesis-transfer audit (registered C8): clean.** Every `(JB1)` hypothesis holds at `t&gt;=4`. The one I expected to be delicate — that both members carry the *same* labelling `alpha` — is automatic because `alpha` **is the received word**: `l1_mixed_residual_intersection_pin/statement.md:201` ("For a fixed intrinsic fiber partition **and received word**"). The list threshold `h &gt;= d+g` is *not* used by `(JB3)`'s proof (only by `(JB7)`); label distinctness is not needed; full petals are not needed (`h = |X|` arbitrary).

## 3. Two results beyond the mandate

**(a) The disjointness hypothesis can be dropped.** `(JB3)` assumes `X` disjoint from `C`. For primitive members it's free: if `L_i(x)=0` and `F(x)=0` then `W(x)=c_iF(x)=0`, so `(X-x) | gcd(F,W)=1`. `Z(F)` never meets the petals. Machine-checked: 5671 primitive members over 360 *deliberately overlapping* configurations, zero with a petal root.

**(b) NEW — the slice-dimension theorem at general `t`.** Round-23b's red-3 split rests on `red3_split.py:5-11`: *"For t &gt;= 4 NO such [linear-flat] reduction is proved."* The same cross-determinant supplies it. If `V` contains a saturated pair `(F,W)`, the **linear** map `E(G,B) = (FB-GW)/Lambda` has image in degree `&lt;= e-1` (dimension `e`) and kernel exactly the line `K(F,W)` (from `gcd(F,W)=1`, `F|G`, `deg G &lt;= d = deg F`). Hence `dim V &lt;= e+1`; the evaluation count gives `&gt;= e+1`; so **`dim V = e+1` exactly, at every `t`**. This is the general-`t` replacement for `(TF3)` (`t=2`) and `(HF)+(BAL)` (`t=3`), needing no syzygy rank. Machine-checked at `t = 4,5,6,7,8`, `e = 1..5`: 215 cells, 155 saturated; `dim V = e+1` on all 155; image bound and kernel rank hold on all 155.

## 4. The refutation search — ran to completion, and it has power

`notes/pilots_20260808/t_petal_lemma/tpetal_refute.py` (reuses `rh_m4t2_census` exact `F_q` arithmetic + `rh_bucket`'s `rref_kernel` and last-coordinate bucketing, generalised from the `t=2` F-chart to the full `(F,W)` chart).

| arm | rows | exhaustive | cells w/ pairs | members | violations | MIN SLACK |
|---|---|---|---|---|---|---|
| MAIN seed 20260808 | 90 | 65 | 13 | 297 | **0** | **0** |
| MAIN seed 991155 (cap 2.5M) | 86 | 71 | 10 | 261 | **0** | **0** |
| BRK-PRIM | 90 | 60 | 12 | 309 | fires (4 cells) | **−1** |
| BRK-DISJ | 90 | 60 | 9 | 118 | none | 0 |
| BRK-LABEL | 90 | 60 | 16 | 491 | fires (15 cells) | **−2** |

- **`MIN_SLACK = 0`**: the cap is *attained tightly* at `t = 4, 5, 6` (e.g. `t=4, ell=2, d=6, q=19`: `MAXOVL = CAP = 4`). The search sits exactly on the boundary, so it has resolution — a violation would have been seen.
- **Power control PASSED**: 2 of 3 broken arms fire, as registered. Dropping primitivity or unlinking the labels both break the cap immediately.
- `DIVOK` and `DEGCOF &lt;= CAP` held on every pair in every MAIN cell; `DIMV = e+1` in all 176 MAIN rows.
- **Completeness**: CLASS-B (bucketed-exhaustive over the chart, `swept` verified). 15–25 cells exceeded the work cap and are CLASS-S/skipped — **they carry no confirmation claim**, only the ability to refute.

## 5. The payoff, executed

`tpetal_payoff.py` re-runs `fpc5_diag/fpc5_exact.py`'s `p7_large_source_sieve` and instruments the rows it silently pays, **asserting** its residual list is row-for-row identical to the verbatim function (408 = 408).

- Grid: **674 rows**. Paid by the sieve: **266**. Residual: **408** (split 142 `t&lt;=3` / 266 `t&gt;=4`, reproducing round-23b's 142/266 exactly).
- Of the 266 paid rows, **156 have `t &gt;= 4`** — those were being claimed *illegally* before this lemma.
- **Legality ledger: residual `564 -&gt; 408`. 156 rows die at a stroke** (27.7% of the previously-legal residual). All 674 rows now have a defined Johnson functional.
- `d`-mass: 36.3% of the admissible `d`-values paid overall; 39.1% at `t &gt;= 4`.
- With §3(b), the 266 `t&gt;=4` residual rows are now also **posable as flats** — the other half of what `red3_split.py` said was missing.

**Bonus probe (a probe, not a claim):** `(CJ2)/(CJ3)` in `l1_joint_core_background_johnson_bound` is *also* PROVED at arbitrary `h` — i.e. the node's second "missing piece", *"(ii) NO background-guard analogue at M &gt;= 5"*, may be mis-stated too. Arithmetically it would rescue **71 of the 408** residual rows (1.97% of residual `d`-mass). **Its chart hypotheses at `M &gt;= 5` are UNAUDITED**; this is the next decisive step, not a result.

## 6. Self-corrections, stated plainly

1. **Registered C7 was wrong in the direction I feared, then dissolved.** I registered that `dim V != e+1` at `t&gt;=4` was "the single most likely place for me to be wrong." Measured `dim V = e+1` in every one of 391 cells — and then *proved* it (§3b). The registered danger became a theorem.
2. **Registered BRK-DISJ expectation was wrong.** I predicted breaking core/petal disjointness would produce violations. It produced none. The reason is a proof, not search weakness: primitivity already forbids petal roots (§3a). I report this as a failed prediction with an explanation, not as a confirmation.
3. **The CJ3 probe was wrong on first run and I corrected it.** I imposed `u &gt;= 0` but not `u &lt;= b` — it "rescued" rows needing `u = 2.8e10` background points from a `b = 2` background block. Corrected: **67.4% -&gt; 1.97%** of residual `d`-mass. The uncorrected number is void.
4. **The pilot's mandate was mis-framed, and I registered that before computing.** The brief asked me to prove or refute an open lemma. It was not open. I appended this at PREREG R0(b) before any `python3` ran, so the reframing is not post-hoc. **The pilot's contribution to the cap itself is bookkeeping, not mathematics**; the mathematics it does add is §3(a) and §3(b).
5. **A process finding worth a catch:** the argument existed under six different names across `background/` (`l1_fixed_support_defect_johnson_bound`, `l1_joint_core_background_johnson_bound`, `l1_fixed_support_cross_determinant_fiber_bound`, `l1_affine_split_pencil_cross_determinant_uniqueness`, `l1_cross_quotient_split_descent_obstruction`, plus the `t=2`/`t=3` critical nodes) while three separate round-23 artefacts recorded it as missing. The naming variance — "Delta", "H_12", "cofactor determinant", "cross determinant", "fiber bound" — is what hid it. **Hard law 5's own-repo grep should be a gate on every "named gate" before it is priced.**

## 7. Compliance

Every `python3` ran via `tools/ramguard tiny|local -- python3 ...` from repo root, including the PREREG append. Stdlib only; no Modal; no git. All writes confined to `notes/pilots_20260808/t_petal_lemma/` (verified; the sole file touched elsewhere is an interpreter-generated `.pyc` from replaying the node's own `verify.py`). No `dag.json`, `nodes/`, or `tools/` edit. **No status flips and no closure claims** — `l1_fixed_support_defect_johnson_bound` was already PROVED; the new dimension theorem (§3b) and the dropped hypothesis (§3a) are drafts for coordinator replay. Quarantine observed: `CAMPAIGN_LEDGER.md` not read at or past line 3173, and no round-24 pilot dir opened; the clause was passed verbatim to the one subagent dispatched.
