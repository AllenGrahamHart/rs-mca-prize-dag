All deliverables executed. Returning the full REPORT verbatim, as the brief directs.

---

**Headline for relay:** **the side door is legal — I closed the ledger, and it buys exactly one merge and not one more — but the door is budget-neutral and the round found a NEW obstruction one layer down that neither prior round ever imposed.** D1 closes: at `O = 2` every axiom passes with margin 1 or sits at equality, and my pre-registered killer was *refuted* (the `(DEG-m)` form I derived is a 2-sharing corollary; under 3-sharing it is free). Exhaustively over deficiency placements, **the merge demand is >= 10 and 10 is attained by exactly TWO placements** (one double-root outer fibre; or the middle fibre losing a reserved slope) — 9 is unreachable because a second placement costs 6 units against `(SAT4)`'s budget of `m = 4`. D2 confirms my central pre-registered prediction **bit-identically at both fields**: a tangency costs exactly 2 dimensions and obeys round 37's cost table verbatim, so the prescribable budget drops 8 -> 7 exactly as the demand drops 11 -> 10 — **the structural deficit stays exactly 3**. Best legal object: **`|slopes| = 14` at BOTH fields** (ties round 36 at `q=193`, **beats round 36/37's `q=257` ceiling of 15**), and a genuine Door-A object at `q=193` with exactly one double-root fibre, 23 slots, 9 merges — one short. D3 ran the pipeline for the first time in this lane: `|W| = 27`, the 4/4 per-side split, the full incidence table with **every cap respected**, the **first ever `mu(x)`-at-middles verification**, and bank 2's `biv_core.py` deficiency-aware system (`102 x 57 = 2a + Delta_W`), rank **56 by bank 2 and 56 by my independent solver**, nullity 1, blockwise-nonzero kernel **found** — the Door-A object *survives* the bivariate layer. And the new fence: **48-82% of all structurally legal objects cannot be completed to `|W| = 27` at all**, because the 9th (middle) fibre's slope cubic must split over `F_q` and avoid the outer slope set. **My first instrument reproduced round 36's common-root false positive on 100% of 1600 draws and my first verifier accepted a 3-double-root object that `(SAT4)` forbids; both are mine, both are below.**

---

# REPORT — r38_side_door (round 38)

## VERDICT (first)

**The side door is ARITHMETICALLY LEGAL and the ledger CLOSES — no axiom kills it. It is also BUDGET-NEUTRAL: it does not close the gap, it moves it. `m = 4` is NOT decided. No witness. And the binding constraint has moved off the slope layer onto the COMPLETION layer.**

```text
THE SIDE DOOR, PRICED  (d1_ledger_results_a.txt:14-31, d2_build_results_e.txt:6-40)

                        slots  reserved  avail  DEMAND   prescribable   DEFICIT
  BASELINE (r36/r37)      24       2       13     11          8            3
  DOOR A (double root)    23       2       13     10          7            3   <- TIE
  DOOR B (middle branch)  24       1       14     10          8            2   <- undecided

  demand drops by one; the budget drops by one.  THE GAP IS INVARIANT.

MINIMUM DEMAND IS 10 AND NOT 9  (d1_ledger_results_a.txt:21-31, exhaustive)
  every 3-unit deficiency placement buys EXACTLY 1 merge; two placements cost
  6 units against (SAT4)'s cap of m = 4.  Demand 9 is UNREACHABLE.

MEASURED, BIT-IDENTICALLY AT q=193 AND q=257  (d2_build_results_e.txt:7-14,50-57)
  span dim      0   2   4   6   8  10  12 |  14        tangency at dim 0: cost 2
  cost of item  2   2   2   2   2   2   2 |   1        (n = 1500 per cell)
  max items prescribable = 8 :  base = 8 merges ; doorA = 1 tangency + 7 merges

BEST LEGAL OBJECTS THIS ROUND
  q=193  |slopes| = 14, 10 merges, 24 slots   (results_e.txt:41-44)   = r36
  q=257  |slopes| = 14, 10 merges, 24 slots   (results_d.txt:105-108) BEATS r36/r37 (15)
  q=193  |slopes| = 14, 9 merges, 23 slots, ONE double-root fibre     (results_d.txt:70-73)
         -- a genuine (SAT4)-legal DOOR A object, one slope short of 13.
  13-slope configurations found: 0 in 6600 draws.

THE NEW FENCE (D3): the 9th fibre.  Over LEGAL objects, W CANNOT be completed
  to 27 points in  77/160 (48.1%) and 28/52 (53.8%) at q=193,
                  108/143 (75.5%) and 50/61 (82.0%) at q=257.
                                        (d2_build_results_e.txt:40,78,118,155)
```

---

## MISSES FIRST

1. **MY HEADLINE PRE-REGISTERED KILLER IS REFUTED BY THE BANKED TEXT — FALSIFIER F1 FIRED.** I registered R1.3 at `P = 0.75` that `(DEG-m)`, in the form `n_1 + 2(rho-s) <= 2m-2`, kills the door by exactly one unit via a cancellation identity (`n_1 + 2(rho-s) = 2rho - SLOTS = 30 - SLOTS`, so `SLOTS >= 24` forced). The algebra is right; **the axiom is not the one I quoted.** Banked `(DEG-m)` (`critical/nodes/rate_half_band_crossing_location/statement.md:3761-3766`) is a **sigma-design corollary**: *"in sigma-designs `X' = 2 deg_H`, so `deg_H(gamma) + X''_gamma >= ceil((m-1-eps~)/2)`"*. Under 3-sharing `X'_gamma = 3 d_gamma`, so a degree-1 slope has `X' = 3 >= m-1 = 3` and needs **no** middle support: `(DEG-m)` is **free**, exactly as round 36's R1.12 said (`r36 REPORT.md:165`). I took a 2-sharing instrument for an axiom. **My blind prior `P(D1's ledger closes) = 0.25` resolved YES against me**, and my nominated killer was wrong.

2. **NO 13-SLOPE CONFIGURATION. NO WITNESS. `HIT_A = 0` IN 6600 DRAWS** (`d2_build_results_{d,e}.txt:36,74,114,151` and `:33,69,104,138`). Best legal is `|slopes| = 14` at both fields; the best Door-A object misses by **one slope / one merge**. `P(a 13-slope O=2 configuration is built) = 0.08` registered; **resolved NO**.

3. **MY FIRST INSTRUMENT COLLAPSED INTO ROUND 36's OWN FALSE POSITIVE, ON 100% OF DRAWS.** The greedy minimum-cost slope scan drove `Psi` onto a common root, producing `|slopes| = 9,10,11` with hypergraph degree 8 — *precisely* the artefact `r36 REPORT.md:229` reported. In 1600 draws (`d2_build_results_b.txt:19-27,58-66`) **every single realized configuration was ILLEGAL**. My MISS-2 guard clause G1 caught it (the verifier, not the counter), and I added a non-degeneracy guard to the prescription itself. **The instrument error is mine, and the guard is the only reason it is a miss and not a result.**

4. **MY FIRST VERIFIER ACCEPTED A CONFIGURATION `(SAT4)` FORBIDS.** At tag `c` it reported `BEST LEGAL |slopes|=14` on a draw with **three** double-root fibres and a triple root (`d2_build_results_c.txt`, `q=193 doorA` and `q=257 doorA`). Three degenerate fibres cost `3x3 = 9` deficiency units against `(SAT4)`'s cap of `m = 4`. I had verified degree, pair multiplicity, bipartiteness and per-side balance but **not the deficiency budget itself** — in a round whose entire subject is that budget. Fixed (`sat4 = 3*ndbl + 6*ntpl <= 4`), re-run, and the object is now correctly rejected. **This is the r36 MISS-2 failure mode recurring inside my own code and I report it as mine.**

5. **THE BEST OBJECT AT `q=257` CANNOT BE COMPLETED AT ALL.** `d3_pipeline_results_a.txt`: *"NO USABLE MIDDLE FIBRE ... the 9th fibre cannot be assembled"*. The 10-merge, 14-slope, fully verified `q=257` object has **no** unused pencil fibre whose slope cubic splits over `F_q`, so `|W| = 27` cannot be built. My headline `q=257` improvement is therefore a **slope-layer** improvement on an object that is **dead at the completion layer**, and I flag it rather than banking it as progress.

6. **MY SYNTHETIC 13-SLOPE TEST HAS ZERO POWER AND I NEARLY MIS-READ IT.** 24 of 24 synthetic legal Door-A incidence tables (12 per field) give **nullity 0** — no kernel, i.e. "excluded". That looks like the door dying at the bivariate layer. **It is not.** The synthetic slope values are 17 *random* field elements, not values realized by a bidegree-(3,3) curve; the real Door-A object with curve-derived values has **nullity 1 with a blockwise-nonzero kernel**. The synthetic run therefore calibrates the instrument (S2 is not trivially degenerate) and **excludes nothing**. Had I reported it as an exclusion it would have been the round's worst error.

7. **DOOR B IS DERIVED BUT NOT DECIDED, AND IT IS THE BETTER DOOR.** If the middle fibre's cubic can carry **two** non-type-2 roots, each middle drops to `d_x = 3`, the deficiency is again `3 = 1+O` with `O = 2`, only **one** type-2 slope is reserved, `s <= 14`, the demand is **10 with the outer structure completely unchanged at 24 slots** — i.e. exactly the object rounds 36 and 37 already build. That would put the deficit at **2, not 3**. I could not settle from the banked text whether a middle admits two non-incident cubic roots (the mechanism exists — one root is already non-incident — but its multiplicity is not stated anywhere I read). **This is the single item I would hand back first**, and it is the same `mu(x)`-at-middles hole that `r36 MISS 10` and `r37 MISS 11` left open.

8. **I DID NOT EXECUTE MY OWN REGISTERED SOLVE ROUTES.** R2.5 (the kernel-of-Vandermonde formulation: `K F = 0`, 16 linear equations in the 8 scales, corank `>= 1` with a nowhere-zero kernel vector) and R2.6 (the sequential `A`-side root scan) were derived before any code and **neither was implemented**. I ran an incremental linear instrument instead — *exactly the operation round 37 proved cannot reach the variety* (`r37 REPORT.md:216`). So this round adds a third measurement of a fence round 37 had already derived, and does not attack the determinantal solve that both rounds now name as the open route.

9. **`(SAT2)`'s SECOND CLAUSE IS UNVERIFIABLE AT MY LAYER AND I DID NOT VERIFY IT.** `(SAT2)` reads `0 <= O <= sum_{gamma in Z} c_gamma <= delta = m-1` (`background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md:33`), with `c_gamma = rho - rank M(gamma)`. `O = 2` therefore demands **at least two units of rank deficiency in the `M(gamma)`** — a Hankel-layer condition invisible to the W-layer. Both doors need it and I checked neither. Every "the ledger closes" statement in this report is conditional on that clause.

10. **LAYER A WAS NOT RUN.** The brief asked for it on any survivor; there was no survivor, and I did not run it on the near-miss objects either. Carries forward from rounds 34-37 untouched, now for the fifth consecutive round.

11. **I NEVER TESTED WHETHER THE `mu` ROOT IS THE ONE THE GEOMETRY CHOOSES.** My `mu(x)` check verifies that at least two of the middle cubic's three roots avoid the outer slope set, so that the two *incident* middle slopes can be chosen among them. In Object A exactly two avoid (`20, 190`), which **forces** `mu = 24`. Whether the actual construction's `mu` equals 24 is beyond the W-layer. So the check I ran is the necessary half, not the sufficient one.

12. **ONE COMPLIANCE JUDGMENT CALL, DISCLOSED, NOT HIDDEN.** One run used `> /dev/null` to discard stdout (`d2_build.py` tag `e`). `/dev/null` is an existing device node and the write-discipline rule names "shell redirection onto an existing file". I judged it compliant — nothing in the repo is written, the redirection discards rather than writes, and the script wrote its own results file — but it is a redirection and I flag it for the coordinator rather than let it pass silently.

13. **`|Z| = 18 > T = 17` IN THE OBJECT I RAN THE PIPELINE ON.** Object A has 14 outer type-2 slopes + 2 middle + 2 type-1 = **18** supported slopes against `(SAT3)`'s `T = rho+2 = 17` (`d3_pipeline_results_a.txt`, the `|Z| = 2+16 = 18` line). Its survival of the bivariate system is therefore **not** a witness and not evidence about a legal configuration — it is the first exercise of the machinery, and nothing more.

---

## CATCH-24A — own-repo subtraction, run BEFORE every novelty claim

Every recursive grep carried, at the **SEARCH** level, `--exclude-dir=r38_urate_genericity --exclude-dir=r38_cauchy_lattice --exclude-dir=r38_sporadic_det --exclude-dir=pilots_20260802 --exclude-dir='prize-codex-*' --exclude-dir=.git --exclude-dir=__pycache__` **and `--exclude=dag.json`**. Hyphenated and spaced variants searched separately.

| object | in-repo prior | verdict |
|---|---|---|
| **the side door itself** | **`critical/nodes/rate_half_band_crossing_location/statement.md:4892-4903`: *"THE SIDE DOOR IS ARITHMETICALLY LEGAL (coordinator check — the round-38 headline anchor): one fibre with a repeated slope drops the slot count 24 -> 23, so 10 merges suffice"*; also `:5011-5013`, `:5020-5022`. `"side door"` = 4 files, `"side-door"` = 2** | **NOT MINE — the coordinator's, priced by round 37's R3.4 (`r37 REPORT.md:88`).** My contribution is only the ledger's *closure*, its *margins*, and the demand-minimality theorem. |
| **double root / tangency / root multiplicity** | `"double root"` = **60 files**; `"tangency"` = 46, of which `critical/nodes/rate_half_band_crossing_location/statement.md` itself, `critical/nodes/spi_exceptional_class/proof.md`, `critical/nodes/l1_mixed_petal_amplification/*` and a background node literally named **`rate_half_ca_hankel_a1_first_degree_core_free_cubic_root_multiplicity_router`** | **HEAVILY BANKED — the load-bearing subtraction.** Cubic root multiplicity is this lane's own machinery. I claim **only** the cost arithmetic inside round 37's Segre budget: that the tangency spans `w(t_*) (x) span{v(alpha),v'(alpha)}`, a **surface** of the same dimension 2 as `Sigma_ij`, hence cost 2 — and the invariance that follows. |
| **the Segre / rank-one-tensor merge budget, the rational normal cubic** | round 37's, itself subtracted against `background/nodes/rate_half_ca_hankel_endpoint_rational_normal_kernel_curve/statement.md:37` (`r37 REPORT.md:106`) | **BANKED TWICE OVER.** Inherited wholesale; I re-measure it and add one row (the tangency). |
| **`blockwise` (nonzero kernel), `deficiency-aware` system** | `"blockwise"` = **20 files**, incl. **`background/nodes/rate_half_bivariate_deficiency_clone_kernel_reduction/`** (claim_contract, node.json, audit) and `critical/.../statement.md:1072-1074`; `"deficiency-aware"` = **19 files** incl. 4 background nodes | **BANKED — PROVED NODES.** `Delta_W <= 1+O <= m` and the extra-column correction are `rate_half_bivariate_deficiency_clone_kernel_reduction`. I *use* bank 2's builder; I claim none of it. |
| **`(SAT1)-(SAT5)`, `(OUT-m)` identity, `(DEG-m)`, per-side cap, `(OV)`** | `background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md:13,33,40,53,59` (**PROVED**); `critical/.../statement.md:3329-3350` (`(OUT-m)` POSED + corrections), `:3752-3766` (the identity + `(DEG-m)`), `:3355-3356` (per-side cap) | **ALL BANKED.** Quoted, never re-derived, never re-claimed. Registered as zero-power item R5.6 before any search. |
| **the 9th/middle fibre and its reservation** | `"middle fibre"` = **1 prior file** (`r36 REPORT.md:101`, *"which is why the 9th fibre is reserved for the middles"*); `"9th fibre"` = same file | **the OBJECT is round 36's.** What is new is the **requirement** on it — that its slope cubic must split over `F_q` and have `>= 2` roots off the outer slope set — and its **measured failure rate** (48-82%). `"completion fence"` = 0 files; `"non-completable"` = 1 (`r36 REPORT.md:248`, the 2-sharing analogue). |
| **the `|slopes| = SLOTS - merges` identity, `K_{4,4}`, the interpolation law, the constant-norm census** | `r37 REPORT.md:18,182,186`; `r36 REPORT.md:169` | **BANKED (rounds 36-37).** Used, not claimed. |
| `"degenerate fibre"` | **1 file: my own `PREREG.md`** | terminology only; the object is the coordinator's "fibre with a repeated slope". |

**Claimed new, after subtraction:** (i) the tangency cost and the **budget-invariance** (R2.3); (ii) the **demand-minimality theorem** (`>= 10`, two placements, 9 unreachable); (iii) the **9th-fibre completion fence** and its measured rate; (iv) the first `mu(x)`-at-middles verification; (v) Door B as a *posed branch*. Nothing else.

---

## D1 — THE DEGENERATE-FIBRE LEDGER, COMPLETE, BEFORE ANY SEARCH

All axioms quoted from `background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md` (**PROVED**) and `critical/nodes/rate_half_band_crossing_location/statement.md`.

### D1.1 The W bookkeeping with the degenerate fibre among the 8

8 outer fibres x 3 + 1 middle fibre x 3 = **27 = a = 7m-1** (`d1_ledger_results_a.txt:9`); `|S_g| = |S_h| = 12 + 3 = 15 = rho` (`:10`). **The degenerate fibre is one of the 8 outer fibres.** It still carries 3 points — a double root of the *slope* cubic does not shrink the fibre — so `|W|` is untouched. Its three points have `A_x = {type-1 slope, alpha, beta}`, `d_x = 3 = m-1`.

### D1.2 The slot arithmetic and the exact demand

`SLOTS = 7x3 + 2 = 23`; `X'_gamma = 3 d_gamma <= 2m-2 = 6` gives `d_gamma <= 2`; two slopes are reserved to the middles (`X'' = 3` each, which saturates the per-side cap `m-1 = 3` and forces `X' = 0`), so `s <= 13`; `s = SLOTS - n_2` gives **`n_2 >= 10`**. Moreover a slope disjoint from `W` has `eps_gamma = 0` and `(OUT-m)` then demands `0 >= m-1 = 3`, which fails — so **`X_gamma = 0` remains impossible even at `O = 2 > m-3 = 1`**, every type-2 slope keeps W-incidence, and **`s = 13` and `n_2 = 10` are EXACT, not bounds** (`d1_ledger_results_a.txt:78-83`).

### D1.3 THE DEMAND-MINIMALITY THEOREM (exhaustive, `:15-31`)

> **Within `(SAT2)`+`(SAT4)` at `m = 4` the merge demand is `>= 10`, and `10` is attained by exactly two deficiency placements: (A) one outer fibre with a double root (`slots 24 -> 23`), or (B) the middle fibre reserving one slope instead of two. Demand `9` is unreachable.**

*Proof (enumerated).* A fibre's slope cubic with `k` distinct supported roots gives its 3 points `d_x = 1+k`, so `3(3-k)` deficiency units; the middle fibre reserving `r` slopes gives `3(2-r)` units. `(SAT4)` is an **identity** `sum_{x in D}(m-d_x) = 1+O` with `1+O <= m = 4`, and `(SAT2)` caps `O <= m-1 = 3`. Every unit-3 placement lowers the demand by exactly 1; every unit-6 placement (two double-root fibres, one triple root, or both doors at once) needs `1+O = 6 > m`. Hence `demand in {10, 11}`. QED. Not pre-registered as a theorem; derived in-round from the registered R1.2 arithmetic.

### D1.4 Every axiom, with its margin (`d1_ledger_results_a.txt:56-83`)

```text
DOOR A                                       value      cap        margin
 (SAT4) sum_x (m-d_x) = 1+O                    3       <= m = 4       1
 (SAT2) O                                      2       <= m-1 = 3     1
 (SAT5) N-(1+O) saturated points              61       >= 15m = 60    1
 (OUT-m) aggregate sum eps = 3 x (m-2)         6       <= (m-1)(1+O)=9  3
 (OUT-m) per slope, merged   X'+2X''= 6        >= m-1-eps = 3       PASS
 (OUT-m) at alpha,beta       eps = 3           RHS = m-1-3 = 0      PASS
 (OUT-m) middle-reserved     0 + 2x3 = 6       >= 3                 PASS
 per-side cap, merged slope  2+1 | 1+2 = 3|3   <= m-1 = 3        EQUALITY
 per-side cap, middle slope  X'' = 3           <= m-1 = 3        EQUALITY
 (OV) pair multiplicity      3                 <= 2rho-a = 3     EQUALITY
 per-slope eps cap           eps_alpha = 3     <= 1+O = 3        EQUALITY
```

**The `(OUT-m)` aggregate check is the one that had to be derived rather than read.** The identity is `sum_gamma eps~_gamma = sum_x def(x) t_x` charging `m-1 / m-2 / m-3` per unit at outside / symmetric-difference / middle points (`statement.md:3752-3757`). The three deficient points are **symmetric-difference** points, so the charge is `m-2 = 2` each and the aggregate is **`3 x 2 = 6`** — my registered R1.7 guess of `3(m-2) = 6`, made at `P = 0.35` **before reading the axiom**, is a **HIT**. And `eps_alpha = eps_beta = 3` because all three deficient points lie on both slopes: the per-slope cap `eps <= 1+O = 3` is met with **equality**.

**Answering the brief's two nominated suspects directly.** *"Does `X'_alpha` pick up 3 incidences from one fibre — does the cap `2m-2 = 6` hold?"* Yes: `X'_gamma = |S_gamma ^ (S_g D S_h)|` is a **set cardinality** (`statement.md:3332`), so a double root contributes **one** membership per point, `X'_alpha = 3` from its own fibre and `6` after one merge — at the cap, not over it. *"Does the per-side cap `m-1 = 3` hold given the `(2,1)/(1,2)` split?"* Yes, at **equality**: the degenerate fibre is a `(2,1)` triple and its merge partner a `(1,2)`, giving `3|3`. **My registered R1.4 (`P = 0.75`, `X'` counts points) is a HIT and falsifier F5 did NOT fire; my registered self-error E3 — "the per-side cap will hold and be irrelevant, i.e. the brief's nominated suspect is the wrong suspect" — is a HIT.**

### D1.5 The merge designs (`d1_ledger_results_a.txt:33-52`)

`Door A`: **976 labelled bipartite designs**, signatures `(3,3,2,2)|(3,3,2,2)` x612, `(3,3,2,2)|(3,3,3,1)` x216, `(3,3,3,1)|(3,3,2,2)` x108, `(3,3,3,1)|(3,3,3,1)` x40; `n_1 = 1+2 = 3`, `s = 10+3 = 13`. (Baseline: 432 designs, all `(3,3,3,2)|(3,3,3,2)`, `n_1 = 2`, `s = 13` — reproducing `r37 REPORT.md:182` exactly. Door B: 2248 designs, `n_1 = 4`, `s = 14`.)

**VERDICT D1: the ledger CLOSES. No axiom kills the door on paper.** My blind prior said `0.25`; it resolved **YES**.

---

## D2 — THE BUILD

### D2.1 What a double root costs — the registered prediction, measured

The tangency is `w(t_*)^T Psi v(alpha) = 0` **and** `w(t_*)^T Psi v'(alpha) = 0`, `v'(gamma) = (3gamma^2,-2gamma,1,0)` — two independent rank-one functionals spanning `w(t_*) (x) span{v(alpha),v'(alpha)}`, whose available-direction variety has dimension `1+1 = 2` in `P^15`, **the same dimension as round 37's `Sigma_ij`**. Predicted cost 2, obeying round 37's threshold. **Measured `2.000` in 1500/1500 draws at each field, at span dim 0** (`d2_build_results_e.txt:57,153`). **R2.2 HIT; falsifier F3 did not fire.**

**Pre-registered correction to the brief, upheld.** The brief's D2 places the condition on "the line in `P^3`". That is the wrong cubic: `disc = 0` on the *pencil* cubic `P - t_*Q` would collapse the fibre to `<= 2` points and destroy `|W| = 27`. The degeneracy is in the **slope** cubic `gamma |-> R(t_*,gamma)`, a condition on `Psi in P^15` that costs **nothing** in the pencil budget. Registered at `P = 0.88` before any read; **upheld** — and it is why the constant-norm census is untouched by the door.

### D2.2 THE INVARIANCE — the round's central result, confirmed at two fields

```text
d2_build_results_e.txt:6,49,87,127   "prescribed items per draw"
  q=193 base  {7:819, 8:681}          q=257 base  {7:936, 8:564}
  q=193 doorA {3:68,4:122,5:165,6:167,7:632,8:346}
  q=257 doorA {3:67,4:135,5:163,6:189,7:671,8:275}
                             MAX = 8 ITEMS IN EVERY CELL

  base  : 8 items = 8 merges          vs demand 11  ->  DEFICIT 3   (= r37)
  doorA : 8 items = 1 tangency + 7    vs demand 10  ->  DEFICIT 3
```

**`P(the instrument deficit is exactly 3) = 0.75` registered; HIT at both fields, in both modes.** The demand drops by one and the budget drops by one, because the tangency is worth exactly one merge edge in the only currency that matters. **The side door does not narrow the gap; it relocates it.**

The variety count agrees: `15 - 10 (merges) - 1 (disc) = 4 = 15 - 11`. The kernel-of-Vandermonde count (R2.5) agrees: 13 free slope values against a corank-`>=1` codimension `(16-7)(8-7) = 9` gives `4`. The `A/B` interpolation count (R2.6) agrees: 11 free `A`-roots (a double root is a *coordinate identification*, not an equation) `- 7 = 4`. **Four independent dimension counts, all 4** — `P = 0.70` registered, **HIT**, and my registered self-error E1 ("I expect one of my four counts to disagree") is **resolved NO**.

### D2.3 The objects actually built

```text
FREE (unprescribed) merges, q=193 base, 1800 draws (results_d.txt:30)
  {0:174, 1:72, 2:19, 3:3}   mean 0.44,  MAXIMUM 3
  -- round 37 measured mean 0.096/0.079 and had NEVER observed 3 (r37 REPORT.md:214).

BEST LEGAL, full structural verification (degree <= 2, pair multiplicity 1,
bipartite, 4/4 balance, (SAT4) deficiency budget):
  q=193 base  |slopes|=14  10 merges  24 slots   results_e.txt:41-44   TIES r36
  q=257 base  |slopes|=14  10 merges  24 slots   results_d.txt:105-108 BEATS r36/r37 (15)
  q=193 doorA |slopes|=14   9 merges  23 slots, exactly ONE double-root fibre
              results_d.txt:70-73  -- a genuine (SAT4)-legal DOOR A object.
```

The Door-A object at `q=193` is, to my knowledge, **the first `(SAT4)`-legal `O = 2` `(SHARE3-4)` object ever built**: 8 fibres, one of them `{121,121,118}`, 23 slots, 9 merges, 14 slopes, deficiency exactly 3. It needs **one more merge**.

**Registered self-error E4 ("I expect not to reproduce the prior rounds' 10 merges") is resolved NO** — I reproduced 10 merges at *both* fields and beat the `q=257` figure. That makes this the first round whose ALLOC-class replication is not disclaimed (contrast `r36 MISS 7`, `r37 MISS 5`).

---

## D3 — THE PIPELINE

### D3.1 Object A through the whole chain (`d3_pipeline_results_a.txt`)

```text
|slopes|=14 slots=23 merges=9 maxdeg=2   deficient fibres=[156]
per-side 2-colouring: (2,1) [0,11,36,44] | (1,2) [43,80,156,178]  -> 4/4 BALANCED
middle fibre t=149, slope-cubic roots in F_q: [20,24,190]
|W| = 27 (need a = 7m-1 = 27) OK ; distinct 27
d_x histogram {4:24, 3:3} ; sum_x (m-d_x) over W = 3 = 1+O -> O = 2   [(SAT4) cap 4]
INCIDENCE TABLE (18 slopes): every X'+2X'' <= 6, every per-side <= 3,
   (OUT-m) satisfied on every slope           -> ALL CAPS RESPECTED
S2 (deficiency-aware): 102 rows x 57 cols  [2a + Delta_W = 54 + 3]
   bank-2 biv_core rank = 56 ; independent rank = 56  -> AGREE
   nullity = 1 ; blockwise-nonzero kernel vector found: True
```

Three things this establishes, and one it does not.

- **The `(SHARE3-4)` object has now faced bank 2's verifier — the first time at `m >= 2` in this class.** `r36 MISS 9`, `r37 MISS 10` and `r37` zero-power 9 all recorded that nothing in those rounds was gated by it. This round is. The rank agrees between bank 2's packed-integer builder and my independent Gaussian elimination — **two implementations, one number.**
- **The deficiency-aware column count is exactly the banked one.** `2a + Delta_W = 54 + 3 = 57`, with `Delta_W = 3 <= 1+O <= m` — the proved node `rate_half_bivariate_deficiency_clone_kernel_reduction` (`critical/.../statement.md:1072-1074`), used as written.
- **The Door-A object SURVIVES the bivariate layer** (nullity 1, blockwise-nonzero kernel). The bivariate system does **not** automatically kill these objects.
- **It is not a witness** and I do not present it as one: it has `|slopes| = 14`, hence `|Z| = 18 > T = 17`, violating `(SAT3)` by one (MISS 13).

### D3.2 The `mu(x)`-at-middles check — the first ever, and it bites

A middle lies in `S_g ^ S_h`, so **both** type-1 slopes are in `A_x`; saturation `d_x = m = 4` therefore leaves exactly `m-2 = 2` type-2 slopes at a middle, and the middle fibre's cubic has 3 roots — so **exactly one root of the middle cubic must fail to be a type-2 slope**, and `sum_gamma X''_gamma = (m-1)(m-2) = 6` (`statement.md:3763-3764`) follows as an identity. The two *incident* roots carry `X'' = 3`, which saturates the per-side cap and forces `X' = 0`, so **they must avoid the outer slope set entirely.**

Measured on Object A: roots `[20, 24, 190]`, of which **`24` is already an outer type-2 slope** (degree 1, fibre `t=0`). The object passes the necessary test (`20` and `190` avoid, and become the reserved middle slopes) — but the identity of `mu` is then **forced to be 24**, with no freedom left. That is a sharp, falsifiable prediction for any future full construction, and it is the first time this lane has put a number on `r36 MISS 10`.

### D3.3 THE NEW FENCE — the 9th fibre (the round's second real result)

The middle fibre's slope cubic must (i) **split over `F_q`** and (ii) have **`>= 2` roots off the outer slope set**. Neither round 36 nor round 37 imposed either, because neither assembled `W`. Measured over **legal** objects only:

```text
                     unused fibres whose slope cubic SPLITS   W NOT completable
  q=193 base    {0:77, 1:63, 2:18, 3:2}                        77/160 = 48.1%
  q=193 doorA   {0:27, 1:15, 2: 9, 3:1}                        28/52  = 53.8%
  q=257 base    {0:108, 1:35}                                 108/143 = 75.5%
  q=257 doorA   {0:50,  1:11}                                  50/61  = 82.0%
                              (d2_build_results_e.txt:38-40,76-78,116-118,153-155)
```

The **AVOID** clause is nearly free (the `>= 2 roots off the outer set` histogram tracks the split histogram to within 2 draws in every cell); **the SPLIT clause is what binds.** The derivation: with `F` disjoint complete fibres in the pencil, `F-8` are available as middles and a random cubic splits with probability `~1/6`, so

> **`P(completable) ~ 1 - (5/6)^{F-8}`**: `F = 12` (`q=193`) gives `0.52` against measured `0.52 / 0.46`; `F = 9` (`q=257`) gives `0.17` against measured `0.245 / 0.18`.

Right shape, right magnitude, and the `q=257` cells run ~5 points high of the heuristic — reported as a discrepancy, not smoothed. **This is a second, independent, monotone-decreasing-in-`q` factor** stacking on top of round 37's exhaustive pencil census (`5056 / 960 / 128 / 0 / 0`): at `q = 257` and `q = 449` the census gives `F = 9`, i.e. exactly **one** candidate middle fibre, which splits about one time in five.

### D3.4 The synthetic test, and its zero power

24 synthetic legal 13-slope Door-A incidence tables (12 per field) on a real 27-point `W` with fresh random slope values: **nullity 0 in 24/24**. Because the values are not curve-realizable, this **excludes nothing** (MISS 6); its content is that S2 is discriminating rather than degenerate, which makes Object A's nullity-1-with-blockwise-nonzero-kernel a non-trivial fact about a *structured* object.

---

## D4 — VERDICT, THE `(BIV-CURVE)` `m`-BOUNDARY OF RECORD, CROSS-PILOT FLAG

```text
m = 1     : structurally disjoint, not exercised (statement.md:585-588)
m = 2     : REALIZABLE (rh_bivariate_system, two-field witness)
m = 3     : REALIZABLE (r34, two-field witness)
m = 4     : OPEN.  The side door is LEGAL and its ledger CLOSES, but it is
            BUDGET-NEUTRAL: demand 11 -> 10, prescribable 8 -> 7, deficit 3.
            Demand cannot go below 10 inside (SAT2)/(SAT4) [D1.3, exhaustive].
            Best legal: |slopes| = 14 at BOTH fields; a (SAT4)-legal DOOR A
            object exists at q=193 (23 slots, 9 merges) and misses by ONE.
            NEW: 48-82% of legal objects cannot be completed to |W| = 27.
            NEW: the first (SHARE3-4) object to face bank 2's verifier
                 SURVIVES it (nullity 1, blockwise-nonzero kernel).
m = 5     : OPEN, not easier (r35).      m >= 7 : Cauchy-Schwarz binds (r36).

CHANGED THIS ROUND
 * the side door : "legal, unchecked" -> LEDGER CLOSED, every margin measured
 * the demand    : 10 was a possibility -> 10 is the EXACT MINIMUM, two placements
 * the tangency  : unpriced -> cost 2, and the deficit is INVARIANT at 3
 * q=257 ceiling : 15 (r36, r37) -> 14
 * completion    : never attempted -> a measured fence killing 48-82% of objects
 * bank 2 gating : never -> the pipeline is gated, two implementations agreeing
 * mu(x)         : never verified -> verified, and it forces mu on Object A
UNCHANGED
 * m = 4 is OPEN.  No witness, no theorem, no exclusion.
```

**CROSS-PILOT FLAG (written self-contained; I read no sibling `r38_*` directory and never `ls`-ed the parent).**

> **Four transportable items.** (1) **A cheaper demand can come with a cheaper budget.** The whole round turned on noticing that the door's saving (one merge) and its cost (one tangency = one merge's worth of dimensions) are the *same size*. Any lane that finds a loophole lowering a demand should price the loophole **in the same currency as the demand** before calling it progress. (2) **A corollary is not an axiom.** I killed the door on paper with an inequality I had seen a prior pilot *use*; the banked form was a 2-sharing corollary (`X' = 2 deg_H`) that does not apply at `k = 3`. Grep the axiom to its **defining node** — mine was `background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md`, and it is PROVED, exact, and two lines long. (3) **Verify the budget you are spending.** My verifier checked degree, pair multiplicity, bipartiteness and balance — and accepted an object with **three** degenerate fibres in a round whose entire subject is that at most **one** is affordable. Whatever your round is about, put *that* quantity in the verifier first. (4) **Layers below the one you are stuck on can be cheaper to test and more decisive.** Two rounds hardened the slope layer; one afternoon at the completion layer produced a fence that kills half to four-fifths of the objects the slope layer certifies.

**Recommended node work (AUDIT-AND-DRAFT; I applied nothing and edited nothing outside my own directory).**

1. **Record the closed ledger**: at `O = 2` the door passes `(SAT2)`, `(SAT4)`, `(SAT5)`, `(OUT-m)`, the per-side caps and `(OV)`, with margin 1 on the three `(SAT)` rows and **equality** on the per-side cap, the `(OV)` pair multiplicity and the per-slope `eps <= 1+O`. The `(OUT-m)` aggregate is `3(m-2) = 6` (symmetric-difference charge), against `(m-1)(1+O) = 9`.
2. **Bank the demand-minimality theorem**: within `(SAT2)`/`(SAT4)` at `m=4` the `(SHARE3-4)` merge demand is `>= 10`; `10` is attained by exactly two deficiency placements; `9` is unreachable. This bounds the entire side-door family, not one door.
3. **Bank the tangency cost and the invariance**: prescribing a double root costs **2** dimensions (an available-direction *surface* in `P^15`, same as `Sigma_ij`), so the prescribable budget falls `8 -> 7` exactly as the demand falls `11 -> 10`; **deficit 3, invariant**, measured bit-identically at two fields. Grade it as round 37's fence is graded: a generic-position count, not a theorem.
4. **Correct `(OUT-m)`'s `X_gamma = 0` corollary for inside deficiency**: the banked corollary needs `O <= m-3`, but when the deficiency lies **inside `W`** every slope disjoint from `W` has `eps_gamma = 0` and `(OUT-m)` still forbids `X_gamma = 0`. So at `O = 2` the corollary survives for the side door, and `s = 13`, `n_2 = 10` are **exact**.
5. **Open the DOOR B branch** (MISS 7): may a middle carry two non-type-2 cubic roots? If yes, demand 10 with the **outer structure unchanged**, deficit **2**, and rounds 36/37's existing 14-slope objects become candidates. This is the cheapest live item on the board and it is a bookkeeping question, not a search.
6. **Bank the 9th-fibre completion fence**: the middle fibre's slope cubic must split over `F_q` and have `>= 2` roots off the outer slope set; `P(completable) ~ 1-(5/6)^{F-8}`; measured `48.1% / 53.8%` (`q=193`) and `75.5% / 82.0%` (`q=257`) **non**-completable over legal objects. Pair it with round 37's census: `F = 9` at `q = 257, 449` leaves exactly one candidate middle.
7. **Record the first `mu(x)`-at-middles verification** and its sharpened form: exactly one root of the middle cubic is non-incident; the other two carry `X'' = 3`, saturate the per-side cap and must avoid the outer slope set.
8. **Record that `(SHARE3-4)` has now been gated by bank 2**: `102 x 57 = 2a + Delta_W`, rank 56 by `biv_core` and by an independent solver, nullity 1, blockwise-nonzero kernel present — the class is **not** killed by the bivariate layer.
9. **Correct the brief's imported-script warning**: `biv_core.py` contains **no** `open(`, no `.write`, no `flush`, and no module-level statement but `import random`. The module-level `"w"`-mode write is in `share3_pencil.py` (`r37` compliance). The two files should not be conflated in future CONSTRAINTS.

---

## PREDICTIONS vs OUTCOMES

| registered (`PREREG.md`, "## Pilot registrations") | outcome |
|---|---|
| R1.1 the degenerate fibre must be OUTER, not the middle, `P=0.80` | **HIT for Door A**; and the middle *can* carry it — that is Door B (MISS 7). Graded PARTIAL |
| R1.2 slot identity `SLOTS=23`, `s<=13`, `n_2>=10`, `P=0.90` | **HIT** — and sharpened to `s = 13`, `n_2 = 10` EXACTLY |
| **R1.3 `(DEG-m)` kills the door by exactly one unit, `P=0.75`** | **REFUTED — falsifier F1 FIRED** (MISS 1). The algebra is right, the axiom is a 2-sharing corollary |
| R1.4 `X'` counts points not multiplicities, `P=0.75` | **HIT** — `X'_g = \|S_gamma ^ (S_g D S_h)\|`, a set cardinality (`statement.md:3332`); F5 did not fire |
| R1.4 `P(the killing axiom is the per-side cap) = 0.20` | **resolved NO** — it holds, at equality, and is irrelevant |
| R1.5 merge graph bipartite, degenerate vertex degree `<=2`, `n_1=3`, `P=0.75` | **HIT** — 976 designs, and the built object realizes `(3,3,2,2)` with the degenerate fibre at degree 2 |
| R1.6 `(OUT-m)` unaffected, `P=0.85` | **HIT** — free for every used slope |
| R1.7 the inside charge is `3(m-2) = 6`, `P=0.35` | **HIT** — derived blind from the brief's phrasing, confirmed against `statement.md:3752-3757` |
| R2.1 the brief names the wrong cubic (`P^3` line vs slope cubic), `P=0.88` | **UPHELD** — a pre-registered correction to the brief |
| R2.2 tangency costs 2 (prescription) / 1 (bare `disc=0`), `P=0.80` | **HIT** — `2.000` in 1500/1500 draws at each field; F3 did not fire |
| **R2.3(i) the instrument deficit stays exactly 3, `P=0.75`** | **HIT — the round's central result**, two fields, two modes |
| R2.3(ii) the variety dimension is 4, `P=0.80` | **HIT** — and three further counts agree |
| R2.4 `P(a 13-slope O=2 configuration is BUILT) = 0.08` | **resolved NO** — 0 in 6600 draws |
| R2.5 the kernel-of-Vandermonde solve; counts agree at 4, `P=0.70` | **HIT as a count, NOT IMPLEMENTED as an instrument** (MISS 8) |
| R2.6 `P(the sequential instrument beats 8 prescribed merges) = 0.15` | **not resolved** — not implemented (MISS 8) |
| **R3 `P(D1's ledger closes) = 0.25`** | **resolved YES, against my prior** |
| **R3 `P(a 13-slope O=2 configuration is built) = 0.08`** | **resolved NO** |
| **R3 `P(pipeline => m=4 witness) = 0.02`** | **resolved NO** |
| **R3 `P(killing axiom = per-side cap) = 0.20` / `(DEG-m) 0.55` / `(SAT)` `0.15` / nothing `0.25`** | **"nothing kills it" WINS at 0.25** — my two leading candidates both failed; the `(DEG-m)` bet was my worst |
| **R3 EXPECTED BEST OUTCOME** (*"legal in the budget but dies on `(DEG-m)` by one unit — and even if it lived, budget-neutral, deficit still exactly 3"*) | **HALF HIT**: the budget-neutrality clause is exactly right; the `(DEG-m)` clause is exactly wrong |
| R4 MISS-2 guard, five clauses | **USED, FIRED THREE TIMES** — G1 caught the common-root collapse (MISS 3); G2 stopped me reporting `merges` as a witness; **G3 stopped me reading the synthetic nullity-0 as an exclusion** (MISS 6) |
| R5 zero-power declarations | **HONOURED** — see below |
| R6 falsifiers F1-F5 | **F1 FIRED** (R1.3 refuted); F2, F3, F4, F5 did not fire |
| R7 E1 "one of my four dimension counts will disagree" | **resolved NO** — all four give 4 |
| R7 E2 "`(SAT4)`'s identity placement is what I will get wrong" | **resolved NO** — `1+O` and `O=2` were right first time |
| R7 E3 "the per-side cap will hold and be irrelevant" | **HIT** — the brief's nominated suspect was the wrong suspect |
| R7 E4 "I will fail to reproduce the prior rounds' 10 merges" | **resolved NO** — reproduced at both fields, and beat `q=257` |

---

## ZERO-POWER DECLARATIONS

1. **Nothing here decides `m = 4`.** The ledger closing is a **paper** result; no configuration reached 13 slopes; the objects built are near-misses and one of them violates `(SAT3)` by one slope (MISS 13).
2. **The budget-invariance is a GENERIC-POSITION COUNT, not a theorem.** It inherits round 37's grading exactly (its zero-power 2): it bounds what an *incremental linear* instrument can prescribe, not the variety. `1500` draws per cell with zero exceptions is evidence.
3. **The demand-minimality theorem (`>= 10`) is conditional on my slot/reservation model** — that an outer fibre contributes its distinct supported roots as slots and the middle fibre reserves `2 - def` slopes. The model is derived from banked text but the *enumeration* is mine and post-registration.
4. **`Delta_W`, the deficiency-aware columns, `blockwise` kernels and `(SAT1)-(SAT5)` are BANKED/PROVED**; I claim none of them.
5. **The synthetic 13-slope nullity-0 result EXCLUDES NOTHING** (MISS 6): random slope values are not realizable by a bidegree-(3,3) curve.
6. **Object A's survival of S2 is not evidence for a witness**: it has 18 supported slopes against `T = 17`.
7. **The 9th-fibre fence is measured over MY ensemble** (rank-greedy with a non-degeneracy guard, on one constant-norm pencil per field). It is a rate, not a bound, and a different pencil or instrument could differ.
8. **`(SAT2)`'s `O <= sum_gamma c_gamma` clause is UNCHECKED** (MISS 9); every "legal" statement is conditional on `>= 2` units of `M(gamma)` rank deficiency existing.
9. **Two fields is not `q`-uniformity**; no claim at official scale `q ~ 2^167`. The window is `q = 1 mod 64`, five fields (round 37's correction, upheld).
10. **Door B is POSED, not decided** (MISS 7), and its `deficit 2` figure is conditional on the branch.
11. **Layer A was not run; `(SAT3)`-conditionality is untouched; `m = 1` was not exercised; sporadic non-factoring sharing remains unsearched.**
12. **The `mu(x)` check I ran is the necessary half only** (MISS 11).

---

## MEASURED FUNCTIONALS (CATCH-19C)

`m, N=16m, rho=4m-1, T=rho+2, a=7m-1, delta=m-1`; `X'_gamma, X''_gamma, X_gamma, eps_gamma, d_x, d_gamma`; the slot count, merge count and `\|slopes\| = SLOTS - merges`; the shared-tuple hypergraph, its degree sequence, pair multiplicity and 2-colouring; the constant-norm `e3=1` slice (651 cubics, both fields, reproducing `r37`), its lines, and the max disjoint complete-fibre count (**12** at `q=193`, **9** at `q=257`, both reproducing `r37 REPORT.md:38-40` independently). **New here:** the **deficiency placement enumeration** and the resulting **demand function**; the **per-item cost conditioned on span dimension with the tangency as an item type**; the **number of prescribable items** per draw in tangency mode; the **double-root and triple-root fibre counts** per configuration and the `(SAT4)` spend `3n_2^{dbl} + 6n^{tpl}`; the **free-merge distribution** (mean `0.44`, max **3**); the **middle-fibre split count** and the **avoid count** over legal objects; the **`d_x` histogram over `W`** and `sum_x(m-d_x)` measured on a built object; the **full 18-slope incidence table** with per-side splits; **`Delta_W`** and the S2 column count `2a + Delta_W`; the **S2 rank by two independent implementations**, its **nullity**, and the **existence of a blockwise-nonzero kernel vector**. **Registered but not measured:** the R2.5/R2.6 solve instruments; Door B; `(SAT2)`'s `c_gamma` clause; layer A; sporadic sharing; the identity of `mu` from the geometry.

---

## COMPLIANCE

**Registrations.** R0-R7 were appended to `PREREG.md` under `## Pilot registrations` with the **Edit tool in three parts**, after reading **exactly** the two named anchors (`r37_share3_gap/REPORT.md`, `r36_m4_nonsplit/REPORT.md`) and **before any other read, any grep, any `ls`, and any interpreter invocation**. The entire D1 ledger, the tangency cost, the invariance prediction, the four dimension counts, the correction to the brief's `P^3` claim, and all five blind priors the brief demanded were derived and registered **before any search**. No post-registration addenda; every registration error (R1.3's refuted killer, R1.1's partial, the un-registered demand-minimality theorem and the un-registered 9th-fibre fence) is reported as an outcome, not edited.

**Compute law — NO BREACH. THE PRE-BASH CHECKLIST WAS APPLIED TO EVERY COMMAND.** Seven interpreter invocations, all seven of the form `tools/ramguard {tiny|local} -- python3 ...` from the repo root with the literal `--`: `tiny` x1 (`RAMGUARD_TIMEOUT=55`, `d1_ledger.py`), `local` x6 (`RAMGUARD_TIMEOUT=290`: `d2_build.py` tags `a,b,c,d,e`, `d3_pipeline.py` tag `a`). **Zero bare `python3` invocations of any kind — no patching, no probes, no empty heredocs, no no-ops between edits.** Every Bash command was scanned for the string `python3` before submission, per `CONSTRAINTS.md:3-13`; the two-round recurrence (`r36 MISS 1`, `r37 MISS 1`) does **not** extend to a third. **Ramguard status: 7/7 clean exits, zero wall kills, zero memory kills**; longest run `116.2 s` (`d2_build.py` tag `d`). Stdlib only (`random`, `sys`, `time`, `itertools`); no Modal, no network, no git, **no subagents spawned**.

**Write discipline — NO `sed -i`, `awk -i`, `perl -i` or `tee`, and no in-place shell stream edit of any file.** Every file edit went through the **Write/Edit tools** (`PREREG.md` x3, `d1_ledger.py` x1 Write, `d2_build.py` x1 Write + 6 Edits, `d3_pipeline.py` x1 Write). Scripts wrote only their own results and checkpoint files. **One judgment call, disclosed as MISS 12:** one run appended `> /dev/null 2>&1` to discard stdout. Nothing in the repo is written by that redirection and the script had already flushed its own results file, but `/dev/null` is an existing file node and I flag the call rather than pass it silently.

**Results-file rules — HONOURED.** Every results file is **versioned per run** by an argv tag: `d1_ledger_results_a.txt`, `d2_build_results_{a,b,c,d,e}.txt`, `d3_pipeline_results_a.txt`, and each is opened in **APPEND** mode (`open(..., "a")`), so no rerun can erase data. `d2_build_ckpt.txt` is append-only. **No results-producing run was piped through `head`.** Two runs were piped through `tail` and one through `grep`; all three consume their entire input and cannot SIGPIPE early, and in every case the script had already `flush()`ed its results file before printing.

**Imported-script rule — TRIGGERED, AUDITED, AND THE BRIEF'S WARNING CORRECTED.** The brief states *"biv_core.py writes at import time"*. **I audited it before any import and that is FALSE for this file**: `grep` for `open(`, `.write` and `flush` over `notes/pilots_20260811/rh_bivariate_system/biv_core.py` returns **nothing**, and the only module-level statement is `import random`. (The module-level `"w"`-mode write is in `share3_pencil.py`, the *other* banked script — `r37`'s compliance paragraph records exactly that, and the two must not be conflated.) The file is **byte-identical** to `r34_bivcurve_m34/biv_core.py` (`diff -q` -> IDENTICAL), so the bank-2 and round-34 copies agree. I imported it **read-only** with `sys.dont_write_bytecode = True` set **before** the import, precisely so no `__pycache__` could be created outside my write scope. **Verified after the run:** the `__pycache__` in that directory is dated `2026-08-11 09:20:42` and its parent `09:44:49`, both ~12 hours before my session's first tool call (my runs are stamped `21:57`-`22:06`) — **it pre-exists and I did not write it.** Consequence: **this round IS gated by bank 2's verifier**, and its rank agrees with my independent implementation.

**RAM discipline.** `dag.json` was **never opened**, and **every recursive grep carried `--exclude=dag.json`** plus the full `--exclude-dir` set. The one `find` I ran carried `-not -path "*/prize-codex-*" -not -path "./.git/*"`; it printed five `biv_core.py` paths, none in an `r38_*` directory. The `>5000`-line crossing statement was read **only** through `grep -n` and five bounded `Read` windows (`556-617`, `770-801`, `1060-1091`, `1195-1214`, `3318-3365`, `3740-3789`, `4826-4857`, `4880-4939`, `4990-5034`); the PROVED axiom node is 80 lines and was read whole. File-at-a-time throughout. All computation is small: the largest object is the 651-point slice with its line dictionary inside a `local` 1G cgroup; the linear algebra is `16`- and `57`-dimensional.

**Quarantine — CLEAN.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was **never opened and never appeared in any tool output**. **`notes/pilots_20260811/` was never `ls`-ed**; the only directories listed by exact path were my own and `rh_bivariate_system/` (a readable `rh_*` pilot). **None of `r38_urate_genericity`, `r38_cauchy_lattice`, `r38_sporadic_det` was read, listed, or named by any tool** — all three were carried as `--exclude-dir` at the **SEARCH** level on every recursive grep, together with `pilots_20260802`, `prize-codex-*`, `.git` and `__pycache__`. **No output filtering after traversal was used at any point.** No path containing `prize-codex-` was touched. Readable sibling names (`r37_*`, `r36_*`, `r35_*`, `r34_*`, `rh_*`, `pilots_20260810`) appeared in grep tallies; of those I opened only the two anchors and `rh_bivariate_system/biv_core.py`.

**Write scope.** Every write is inside `notes/pilots_20260811/r38_side_door/`: `PREREG.md`, three scripts, seven results files, one checkpoint — **13 entries and no `REPORT.md`** (the directory listing confirms it). **No** `dag/`, `nodes/`, `critical/`, `background/`, `experiments/` or `tools/` edits; no git; no scratch file anywhere, including `/tmp` and the session scratchpad. The nine node-work items in D4 are **recommendations only — nothing was applied** (AUDIT-AND-DRAFT).

**Method discipline.** Own-repo greps (CATCH-24A) preceded every novelty claim, **including hyphenated, spaced and infixed variants**, and produced **eight live subtractions, two of them load-bearing**: the side door is the **coordinator's** (`statement.md:4892-4903`), and `blockwise` / `deficiency-aware` kernels are **PROVED background nodes** (`rate_half_bivariate_deficiency_clone_kernel_reduction`) — so the D3 machinery is used, not claimed. Two-field confirmation on every structural claim (`F_193`/`F_257`), and **two-implementation confirmation** on the S2 rank. Every quantifier claim carries a `file:line`. Every max-quantified claim carries a zero-power declaration and its budget. The round's self-caught errors — the refuted headline killer, the instrument that collapsed on 100% of 1600 draws, the verifier that ignored the very budget the round is about, the un-run solve routes I had registered, and the synthetic result I nearly mis-read as an exclusion — are reported as errors, in the misses section, ahead of the results.

**`REPORT.md`.** The brief pre-declares that the harness refuses this write, so I did not spend a tool call attempting it; **the directory contains 13 entries and no `REPORT.md`**, and this report is returned verbatim as the final message per the brief's fallback clause.
