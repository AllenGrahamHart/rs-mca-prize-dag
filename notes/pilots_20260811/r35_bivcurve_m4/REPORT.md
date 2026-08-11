All deliverables are complete. Here is the full REPORT text.

---

**Headline for relay:** **round 34 named the wrong obstruction at `m = 4`.** I imported anchor 2's linear-hypergraph compiler as the brief asked and it **decides the selection layer POSITIVELY** (explicit `Z_12` certificate: 12 triples, 3-regular, linear, 12 slopes) — so I ablated round 34's own search and measured that **dropping the `(OV)` linearity constraint entirely does not move the ceiling by a single triple** (7 → 7, 8 → 8, two fields), while **dropping the slope budget reaches 12 of 12 in 383 of 383 draws.** The `m=4` obstruction is 100% arithmetic value-confinement and 0% the `(OV)` pair cap. I also **raised the ceiling from 7 to 9** with value-prescribed pencils (two fields), so round 34's ceiling was soft; ran **route (b)** (derivation first: the invariant factor is Möbius in the quotient coordinate for *any* involution, so `sigma(x)=c/x` does **not** remove injectivity — the brief's hypothesis is refuted before searching) and **route (c)** (8 of 24, blowout); and built a **new non-split ansatz `(QUAD-4)`** (14 parameters vs `(SPLIT-4)`'s 10) that is genuinely route (a) — ceiling still 7. **`m = 5` REFUTES the parity prediction**: 7/15 and 6/15 on two fields with no invariant factor forced. The corrected `(OUT-m)` **survived every stress** and its aggregate is **exactly tight** on the `m=3` witness.

---

# REPORT — r35_bivcurve_m4 (round 35)

## VERDICT (first)

**`m = 4` is NOT DECIDED — but its obstruction is RELOCATED, RE-SCOPED, and its ceiling is RAISED.** Four ansatz classes are now searched-negative instead of one, and the mechanism round 34 named is measured to have **zero power**.

```text
THE LAYER SEPARATION (m_engine_results.txt:26-29, m_engine_results_s2b.txt:9-11)
  m=4, 12 shared triples needed, DFS budget 12000-30000 (r34 used 4000)
    V1 FULL      linear + deg<=3 + <=15 slopes : BEST = 7 (q=193) / 8 (q=257)
    V2 NO-LINEAR         deg<=3 + <=15 slopes : BEST = 7 (q=193) / 8 (q=257)
    V3 NO-SLOPES linear + deg<=3              : BEST = 12 of 12 in 383/383 draws
  m=5, 15 shared quadruples (m_engine_results_s3a.txt:8-10, _s3b.txt:6-8)
    FULL         : BEST = 7 (q=241) / 6 (q=401)
    NO-PAIRCAP   : BEST = 7 / 6      -- histograms BIT-IDENTICAL to FULL
    NO-SLOPES    : BEST = 15 of 15 in 500/500 draws

THE m-BOUNDARY IN ONE CURRENCY (coincidences needed vs achieved)
  demand D(m) = 3m(m-1) - (rho-1) :   m=3: 8     m=4: 22    m=5: 42
  ACHIEVED, best over all searches :   m=3: 8     m=4: 12    m=5:  9
  m = 3 IS THE LAST m WHERE SUPPLY MEETS DEMAND.  Supply is FLAT in m;
  demand grows as 3m^2-7m+2.  Parity is not the mechanism.

THE CEILING IS SOFT (m4_struct_results.txt:9-10,25-26; two fields, matched
budget and draw count in the same run)
    RANDOM  (r34's ensemble) : BEST = 8 (q=193) / 7 (q=257)
    ALLOC-A (7 values of phi prescribed by linear algebra) : BEST = 9 / 9
```

Five results, in decreasing order of how much they move the board:

1. **The obstruction round 34 named is not the obstruction.** `statement.md:3196-3202` records the `m=4` negative as *"the `(OV)` pair cap `2rho-a = m-1 = 3` forcing the 12 shared slope-TRIPLES to form a linear (partial-Steiner) 3-uniform hypergraph (measured ceiling 7 of 12)"*. I removed that constraint from the search and **the ceiling did not move at either field**. The binding constraint is the `<= rho` slope budget alone — the arithmetic layer.

2. **Anchor 2's compiler transports and DECIDES the selection layer — positively.** The abstract problem (12 linear triples, degrees `<= 3`, `<= 15` slopes) is satisfiable, with two independent certificates (`sel_layer_results.txt:16-27`): the `Z_12` difference set `T_i = {i, i+1, i+3}` (12 triples, **12** slopes, 3-regular, linear, and carrying an SDR so each triple owns its own `chi`-slope — the pencil-shaped form), and a from-scratch DFS (441 nodes). **Both survive the min-degree tightening I derive in D3.** So the selection layer is free and the separation from the arithmetic layer is clean and total.

3. **Route (b) is refuted at the derivation level, before searching, exactly as the brief asked.** For **any** involution `sigma` of `P^1`, the invariant subfield is `F_q(w)` for one degree-2 quotient coordinate (`w = x^2` for `-x`; `w = x + c/x` for `c/x`), so an invariant factor of `deg_x <= 3` is **Möbius in `w` after cancellation, hence injective on orbits**. Confirmed on 167/167 and 177/177 factors (`route_bc_results.txt:14-19`). The fixed points do **not** touch the cross-coincidence term. Measured ceiling: 7, both fields.

4. **A new non-split ansatz, `(QUAD-4)`, is the first real route-(a) probe — and it is measured, not speculated.**
   > `G(Z,x) = Q(Z,u) L(Z,u)`, `u = x^2`, `Q = A(u)Z^2+B(u)Z+C(u)` with `deg_u <= 3`, `L = S(u)Z - R(u)` with `deg_u <= 1`. `Q` is **irreducible over `F_q(u)`** generically, so `G` does not split into linear-in-`Z` factors — genuinely route (a) — yet `Q` is `sigma`-invariant, so its two roots are **shared by the orbit** exactly as `(SPLIT-4)`'s swapped pair is. `(SPLIT-4)` is precisely the sub-family where `disc(Q)` is a square **in `F_q(u)`**.

   Parameters: **14 vs `(SPLIT-4)`'s 10.** Non-splitness confirmed structurally: the fraction of orbits with `disc` a nonzero square is `15.7/32` and `15.6/32` (`route_bc_results.txt:36,39`) — a split `Q` would give 32/32. **Ceiling still 7 of 12, both fields**: the four extra parameters are paid straight back by losing half the orbit pool.

5. **`m = 5` refutes the parity prediction, and the `(OV)` cap's `m=4`-specificity is confirmed to be irrelevant.** `(SPLIT-5)+sigma` all-swapped has **no invariant factor forced** — the exact configuration anchor 1's parity reading calls easy (`statement.md:3205-3208`) — and reaches **7 of 15 and 6 of 15**. It is *further* from its target than `m=4` is from its. The relaxed pair cap (`floor((m-1)/2) = 2` at `m=5`) never binds: the FULL and NO-PAIRCAP histograms are bit-identical at both fields.

---

## MISSES FIRST

1. **I DID NOT DECIDE `m = 4`.** No witness, no theorem. What I deliver is a **relocation** (arithmetic, not `(OV)`), a **re-scoping** (four searched-negative classes instead of one), a **softer ceiling** (9, not 7), and a route-(a) probe. The general `m=4` question — a fully general non-split `G` that is **not** `sigma`-invariant and **not** a `Q·L` product — is **untouched**. `(QUAD-4)` is one sub-route of route (a), not route (a).

2. **MY OWN DFS SILENTLY IGNORED ITS OWN `mindeg` ARGUMENT ON THE FIRST RUN.** `sel_layer.py`'s `dfs_hypergraph` took a `mindeg` parameter and never enforced it; the first run reported `degmin=1` while the surrounding text claimed the min-degree tightening. I caught it in the output, fixed it with the Edit tool, and re-ran (`sel_layer.py:74`, `A2`/`A3` now return `degmin=2`). **This is exactly the MISS-2 family my own R6 registration was written against: a registered quantity that was not the quantity computed.** Reported here, not buried.

3. **MY REGISTERED `(SUPPLY-CODIM)` USES A SUPPLY PROXY THAT OVERSTATES.** R3 equates achievable coincidences with the parameter count `P`. Measured: at `m=5`, `P = 14` but the best achieved is **9**; at `m=4`, `P = 10` and structured pencils achieve **12** (better than `P`, because the DFS also harvests luck). The model's **direction and ordering are confirmed at every point**, its **calibration is loose in both directions**. It stays graded HEURISTIC (R9.2) and I make no inference of non-existence from it.

4. **ONE PROBE IN `route_bc.py` HAD ZERO POWER AND I RAN IT ANYWAY.** The line *"random `deg<=3` phi that happen to be `sigma`-invariant on `mu_64`: 0 found"* (`route_bc_results.txt:16,18`) tested nothing — a random degree-3 map is essentially never invariant, so the sample size was 0 by construction. The real confirmation of R1.1 is the Möbius-in-`w` test (167/167, 177/177). Declared rather than dropped.

5. **THE `m=4` CELLS ARE NOT ALL BUDGET-MATCHED ACROSS SCRIPTS.** `m_engine` ran `q=193` at DFS budget 30000 with 83 draws and `q=257` at 12000 with 300 draws; the ceilings (7 vs 8) therefore differ partly by **draw count, not by field**. The RANDOM-vs-structured comparison inside `m4_struct.py` **is** matched (same budget 12000, same 220 draws, same run, same field) and that is the only comparison I draw a conclusion from.

6. **MY FIRST `m_engine` RUN WASTED ITS BUDGET AND PRODUCED THREE ZERO-DRAW CELLS.** The internal 240 s deadline was consumed by an 800-draw `m=3` control, leaving `m=4 q=257` and both `m=5` cells with 0 draws (`m_engine_results.txt:30-52` — the `BEST = 0` rows are **not** measurements). I re-ran those cells individually (`_s2b`, `_s3a`, `_s3b`). No ramguard kill occurred; this was my own scheduling error.

7. **EVERY CONFIGURATION THIS ROUND IS A SELECTION-LAYER OBJECT ONLY.** I built **no** outside completion, **no** bivariate system, **no** full `W`. The `k=9` `m=4` candidates are partial and were never completed; `biv_core.py` was copied in but **never imported**, so unlike round 34 nothing here is gated by bank 2's independent verifier. My `(OUT-m)` stress therefore runs on the banked `m=3` witness (complete) plus partial configurations.

8. **I NEVER VERIFIED THE PER-SIDE SPLIT ON MY `m=4` CANDIDATES.** The per-side cap `|S_gamma ^ S_g| <= m-1` equals `deg_H` **only if** each selected orbit puts one point on each side. I imposed the global degree cap and assumed the split; I did not construct `S_g`/`S_h`. A candidate could fail per-side even at `deg_H <= 3`.

9. **THE `Z_12` CERTIFICATE IS STANDARD COMBINATORICS AND I AM NOT CLAIMING IT.** `{0,1,3}` has all six differences distinct — a Sidon/perfect-difference argument. `grep -ril "Sidon"` returns **186 files** repo-wide. It is new *in this lane* (zero hits in `statement.md` or the `u1_x4` notes) and nowhere else.

10. **NOTATION COLLISION I INHERITED AND PROPAGATED.** `deg_H` in this lane means the degree in the shared-slope-tuple hypergraph; `deg_H` at `background/nodes/rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction/statement.md:41` means the degree in the bipartite **non-incidence** graph of the `A=1` core-one active partition — and that node carries a **PROVED lower bound `deg_H(gamma) >= n_X - r`**. Same symbol, same repo, different object, and it is a partial prior on my `(DEG-m)` (see CATCH-24A).

11. **LAYER A WAS NOT RUN** (inherited from round 34's MISS 7; `statement.md:3136` records the orthogonality expectation). **`(SAT3)`-conditionality carries forward untouched** (`T = rho+2`). Nothing here bears on either.

12. **ONE RECURSIVE GREP TRAVERSED `dag.json`.** My first subtraction batch (8 patterns) carried `--exclude-dir` but not `--exclude=dag.json`; `dag.json` appears as a **filename** in three of those outputs. No content entered my context, and every later grep carried `--exclude=dag.json`. Disclosed as a deviation in the letter of the RAM clause.

---

## CATCH-24A — own-repo subtraction, run BEFORE every novelty claim

Every grep carried `--exclude-dir` at the SEARCH level (`pilots_20260811`, `pilots_20260802`, `prize-codex-{1,2,3}`, `.git`, `__pycache__`), and **hyphenated / infixed variants were searched separately** — the round-34 catch (`FABLE_AUDIT.md:79-92`).

| object | in-repo prior | verdict |
|---|---|---|
| linear 3-uniform hypergraph, pair-uniqueness forcing linearity | anchor 2, `F3_H3_REPEAT_LINEAR_HYPERGRAPH_COMPILER.md:31,35-39` (PROVED); flagged as transport candidate at `statement.md:3208-3213` | **BANKED — it is my mandate's imported machinery.** My contribution is transporting it and finding it **decides the layer positively**, i.e. the opposite of the effect the transport was proposed for. `"linear hypergraph"` = 0 files; `"linear-hypergraph"` = **10 files**; `"3-uniform"` = 12; `"partial Steiner"` = 0; `"partial-Steiner"` = 1 (`statement.md`, r34's own). |
| `(OUT-m)` and its coordinator corrections | `statement.md:3220-3236` | **BANKED.** I re-derive the display from scratch, verify it, and **offer a refinement** (the exact aggregate identity). `grep -rl "OUT-m"` outside the pilot dirs: **1 file**, that node. |
| `(OV)` cap, `(SPLIT-m)`, the involution device, `sum X = (m-1)(7m-2)`, capacity `(4m-1)(2m-2)` | `statement.md:3196-3202`; r34 `REPORT.md:200-211` | banked; reproduced, not re-derived. `"cross-coincidence"`, `"coincidence supply"`: **1 file each**, that node (r34's addendum). |
| min-degree law forced by an incidence budget — my `(DEG-m)` | **`background/nodes/rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction/statement.md:41`: `deg_H(x)>=n_Z-e_*, deg_H(gamma)>=n_X-r` (AIR2), PROVED**; also `background/nodes/xr_rank_five_richline_hierarchy/node.json:14` ("exact minimum degrees at r=3 are 123/120/27") | **PARTIAL SUBTRACTION, live.** The *form* — a proved minimum-degree law on an incidence graph, **using the identical symbol `deg_H(gamma)`** — is banked in a sibling `rate_half` lane. The *object* differs (bipartite non-incidence graph of the `A=1` core-one partition vs my shared-tuple hypergraph on type-2 slopes). I claim only the **derivation of `(DEG-m)` from the corrected `(OUT-m)`**, not the idea of a min-degree law. `"min degree"` = 0 files, `"minimum degree"` = 1, `"degree-1 slope"` = 0. |
| the `Z_12` `{0,1,3}` certificate | Sidon sets: **186 files** repo-wide (e.g. `background/nodes/f3_h3_quotient_galois_orbit_scalar_decomposition/statement.md`); zero in `statement.md` or the `u1_x4` notes | **NOT CLAIMED.** Standard difference-set combinatorics; new only as an instance in this lane (MISS 9). |
| `(QUAD-4)`: non-split `sigma`-invariant quadratic factor | `"QUAD-"` = 1 file (`experiments/xr_smallcore_quad_scan.py`, different object); `"non-split"` = 12 files, of which `statement.md` is r34's own use and the rest are `pb_design_ceiling`, `tern_master_threshold`, `xr_lowcore_spread_heart` — none a `(BIV-CURVE)` object | claimed **new here**, and deflated: it is the *obvious* first step past `(SPLIT-m)` (allow the `Z`-quadratic not to factor) and its content is a parameter count plus one measured square-rate. |
| "the invariant factor is even in `x`, `deg_x <= 2`, Möbius in `u = x^2`, injective on orbits; the `3+3+2` split is forced" | **`notes/pilots_20260811/r34_bivcurve_m34/FABLE_AUDIT.md:65-72` (coordinator hand-check 6)** | **BANKED BY THE COORDINATOR, for `sigma(x) = -x`.** I registered it blind (R1.2) before reading the audit, and it is **not** mine. What is new is the **generalisation to an arbitrary involution** via the quotient coordinate (R1.1) — which is what decides route (b). |
| "a fields-searched negative is not a theorem"; positive controls | `statement.md` round-34 `(SAT3)` addendum; `"positive control"` = **111 files** | banked methodology, used not claimed. |

---

## D1 — THE `m = 4` DECISION PROGRAM

### D1.1 The compiler import, and what it decides (`sel_layer_results.txt:9-45`)

Anchor 2 proves pair-uniqueness ⟹ linear 3-uniform (`F3_H3_REPEAT_LINEAR_HYPERGRAPH_COMPILER.md:31`). The transport to `(BIV-CURVE)` `m=4` is exact in form: a shared triple puts 2 points into each of its 3 slope pairs against the `(OV)` cap `m-1 = 3`, so two slopes co-occur in at most one triple. **Generalised here to every `m`:**

> **PAIR-MULTIPLICITY CAP `= floor((m-1)/2)`.** `m=3 -> 1` (distinct pairs), `m=4 -> 1` (**linear**), `m=5 -> 2` (**not linear**). Linearity is the `m=4` face of one law, exactly as r34's cross-pilot flag warned (`statement.md:3205-3207`).

**The decision.** Two independent certificates, both satisfying the `(DEG-m)` tightening of D3:

```text
A1  Z_12 : T_i = {i, i+1, i+3} mod 12
    12 edges, 12 slopes (<=15), degmax 3, degmin 3, pair mult 1, SDR True
    linear because the differences of {0,1,3} are +-1,+-2,+-3, all distinct
A2  from-scratch DFS (no Z_12 structure), 441 nodes
    12 edges, 14 slopes, degmax 3, degmin 2, pair mult 1
```

`A1` additionally has the **pencil shape**: each triple owns a distinct vertex (SDR), which is the `chi`-slope slot the `sigma`-invariant factor must supply — so the certificate is not merely abstract, it is the shape a `(SPLIT-4)` design would have to realise.

**Two-field note:** this layer is field-free (pure combinatorics), so "two fields" is replaced by **two independent constructions**, one explicit and hand-checkable, one machine-searched.

### D1.2 The ablation: which layer actually binds (`m_engine_results.txt:26-29`, `m_engine_results_s2b.txt:9-11`)

| variant | constraint set | `q=193` | `q=257` |
|---|---|---|---|
| V1 FULL | linear + `deg<=3` + `<=15` slopes | **7** of 12 | **8** of 12 |
| V2 NO-LINEAR | `deg<=3` + `<=15` slopes | **7** | **8** |
| V3 NO-SLOPES | linear + `deg<=3` | **12** (83/83 draws) | **12** (300/300) |

**Linearity has zero power.** The ceilings are identical at both fields; the histograms differ by a handful of draws in the interior (`(6,57),(7,26)` vs `(6,53),(7,30)` at `q=193`), i.e. linearity costs the occasional triple mid-distribution and never at the ceiling. At `m=5` the corresponding histograms are **bit-identical**. **The slope budget alone is the whole obstruction**, and it is satisfied trivially the moment it is lifted.

This **refutes the mechanism of record** at `statement.md:3200-3202`. The `(OV)`-forced linear hypergraph is real, proved, and **inert**.

### D1.3 Route (b) — `sigma(x) = c/x` — derived before searching, as the brief required

**Orbit arithmetic (`route_bc_results.txt:4-10`, two fields).** `sigma` preserves `mu_N` iff `c ∈ mu_N`; `Fix = {x : x^2 = c}` has size 2 if `c ∈ (mu_N)^2 = mu_{N/2}` and 0 otherwise. Measured at `N=64`: **32 values of `c` give 2 fixed points, 32 give 0 — never odd.**

**Consequence 1 (R2.3).** `|S_g ^ S_h| = m-1 = 3` is odd, and a `sigma`-stable set of odd size needs an odd number of fixed points. **No involution of either family makes `W` `sigma`-stable at even `m`.** Route (b) buys no stability.

**Consequence 2 (R1.1), the one that matters.** The invariants of `x -> c/x` are generated by `w = x + c/x`. An invariant factor with `deg_x <= 3` carries a forced common factor; after cancelling it, `chi` is a **Möbius map in `w`**, hence `deg_x chi = 2` and **`chi` is injective on orbits** — the same defect `sigma(x) = -x` has. Verified: 167/167 (`q=193`) and 177/177 (`q=257`) invariant factors injective on all 33 orbits. **The brief's hypothesis that route (b) "changes exactly that term (fixed points!)" is refuted at the derivation level.**

**Consequence 3 (R2.4).** Placing both fixed points in `S_g D S_h` gives `24 = 2 + 11` orbits and slot count `11*3 + 2*2 = 37 >= 36`, so route (b)'s coincidence demand is **not lower**. A fixed point is harmless only at a middle, where the free root absorbs the repeated root.

**Search:** ceiling **7 of 12 at both fields** (`route_bc_results.txt:24-25`) — identical to random `(SPLIT-4)`.

### D1.4 Route (c) — un-symmetrised `(3,3,3)` — a blowout

Without the involution there is no sharing: all 24 points of `S_g D S_h` carry their own triple, so 24 tuples are needed instead of 12 and the demand becomes `6m(m-1) - (rho-1) = 58` coincidences against 21 parameters. Searched under a **relaxation** (global caps `deg <= 2m-2 = 6`, pair multiplicity `<= m-1 = 3`, `<= 15` slopes; per-side caps not imposed, so the ceiling is a genuine ceiling): **8 of 24 at both fields** (`route_bc_results.txt:31-32`). Route (c) is the worst route by a wide margin, and it is now measured rather than asserted.

### D1.5 Route (a) — `(QUAD-4)`, and what it costs

The parameter arithmetic, derived before the run:

```text
(SPLIT-4) : A,B deg 3 (7 proj.) + Mobius in u (3)                  = 10
(QUAD-4)  : A,B,C deg_u 3 (11 proj.) + Mobius in u (3)             = 14
            (SPLIT-4) = the sub-family where disc(Q) is a square in F_q(u)
x-degree  : 6 + 2 = 8 < 9 = 3m-3   (split: 3 + 3 + 2 = 8 < 9)
```

> **DERIVED, general:** at **even `m`** every `sigma`-symmetric `(BIV-CURVE)` ansatz **wastes one unit of the `3m-3` `x`-degree budget**, because a `sigma`-invariant factor has *even* `x`-degree. This is the sharp form of the `3+3+2`-vs-`(3,3,3)` tension in r34's own report (`REPORT.md:370-374` says `(3,3,3)` is forced; `REPORT.md:99-100,429` says the split is `3+3+2`), and it extends past split ansätze to `(QUAD-4)`. The coordinator's audit already resolved it for the split case (`FABLE_AUDIT.md:65-72`).

**Measured:** ceiling **7 of 12 at both fields**; orbits with `disc` a nonzero square **15.7/32 mean (min 10, max 24)** at `q=193` and **15.6/32** at `q=257` (`route_bc_results.txt:35-39`) — a split `Q` would give 32/32, so **`Q` is confirmed non-split, structurally, on two fields**. The four extra parameters are paid straight back: **half the orbit pool is lost**, since only orbits where the discriminant is a square yield a rational triple.

### D1.6 Structured pencils — round 34's declared blind spot, and the soft ceiling

Round 34 declared itself zero-power over structured pencils (`REPORT.md:568-570`). The construction (R5.1): `phi(x) = t` is `A(x) - tB(x) = 0`, **linear** in `phi`'s 8 coefficients for fixed `t`, so **seven prescribed values determine `phi` projectively** by a `7x8` nullspace — the exact analogue of prescribing two size-3 fibres with one parameter left over. Targets are taken from the `Z_12` certificate: `{phi(x_i), phi(-x_i)} = {c_{i+1}, c_{i+3}}` with `c_i` the orbit's `chi`-value.

```text
(m4_struct_results.txt:9-10,22,25-26,38 -- matched budget 12000, ~215 draws each,
 same run, same field)
  q=193  RANDOM  8 of 12    ALLOC-A  9 of 12    ALLOC-B  8 of 12
  q=257  RANDOM  7 of 12    ALLOC-A  9 of 12    ALLOC-B  8 of 12
  ALLOC-A realises 2.96 / 2.97 targeted triples per draw (max 4)
          -- the "3 guaranteed from 7 of 24 arrows" prediction, hit exactly
```

**Round 34's ceiling 7 was soft.** It moves to 8 with more draws and to **9 with structure, on both fields**. The `m=4` negative must be re-graded accordingly: it is a ceiling that has now been raised twice, not a wall.

### D1.7 The `m = 4` verdict, with scope stated exactly

**`m = 4` remains OPEN.** The obstruction is **extended in scope** to four searched-negative classes and **relocated** to the arithmetic layer:

```text
EXCLUDED (searched-negative, scope named, budgets named):
  1. (SPLIT-4)+sigma(-x), RANDOM ensemble        ceiling 8   (2 fields, 520 draws)
  2. (SPLIT-4)+sigma(-x), VALUE-PRESCRIBED       ceiling 9   (2 fields, ~430 draws)
  3. (SPLIT-4)+sigma(c/x), 2 fixed points        ceiling 7   (2 fields, 398 draws)
  4. un-symmetrised (3,3,3)                      ceiling 8 of 24 (2 fields)
  5. (QUAD-4), non-split sigma-invariant quadratic ceiling 7 (2 fields, 373 draws)
UNTOUCHED:
  * general non-split G with NO sigma-symmetry and no Q*L factorisation
  * any ansatz outside the pencil/quadratic families
  * every claim above is a DFS ceiling under budgets 12000-30000 nodes per draw
NOT the obstruction (measured, not argued):
  * the (OV) linearity / selection layer -- ZERO power (D1.2)
  * the ramification budget -- free in every class searched here
```

---

## D2 — THE `m = 5` PARITY FALSIFIER

**The prediction under test** (`statement.md:3205-3208`; r34 `REPORT.md:187-192`): odd `m` easy (no `sigma`-invariant factor forced), even `m` obstructed. `(SPLIT-5)+sigma` all-swapped is `m-1 = 4` factors as two swapped pairs, `3+3+3+3 = 12 = 3m-3` — the budget met with equality and **no invariant factor**, so parity says this is the easy case.

**The selection layer is free** (`sel_layer_results.txt:47-56`): 15 quadruples, 17 slopes (`<=19`), `degmax 4`, `degmin 2`, pair multiplicity 2 — found in 4182 DFS nodes. And the round-34 caution is confirmed: the cap `m-1 = 4` admits **two** quadruples per slope pair, so **linearity genuinely vanishes at `m=5`** — and it changes nothing, because linearity was already inert at `m=4` (D1.2). The character of the selection problem changes; its contribution to the obstruction is zero in both cases.

**The arithmetic layer refuses:**

```text
m_engine_results_s3a.txt:8-10 / _s3b.txt:6-8
  q=241 : FULL 7 of 15   NO-PAIRCAP 7   NO-SLOPES 15 of 15 (250/250)
  q=401 : FULL 6 of 15   NO-PAIRCAP 6   NO-SLOPES 15 of 15 (250/250)
  FULL and NO-PAIRCAP histograms are BIT-IDENTICAL at both fields
```

**The parity prediction is REFUTED as a predictor of realizability.** `m=5` — the configuration parity calls easy — is *further* from its target (7 of 15) than `m=4` is from its (9 of 12). The parity **mechanism** (an invariant factor is forced at even `m`, and it is injective on orbits) is real and confirmed twice over (R1.1, `route_bc_results.txt:14-19`); it is simply **subdominant**. The dominant law is one line, and it is parity-free:

```text
COINCIDENCE DEMAND   D(m) = 3m(m-1) - (rho-1) = 3m^2-7m+2 :  8, 22, 42
COINCIDENCE ACHIEVED (best over every search this round)  :  8, 12,  9
                                                       m =  3,  4,  5
```

Demand grows quadratically; achievable supply is **flat**. `m = 3` is the last `m` where they meet, and it meets exactly — which is why r34's `m=3` witness cost 632 trials at `q=97` and 24939 at `q=193` (`REPORT.md:309-310`), and why my calibrated control reaches 9 of 9 in **28 of 400** draws at `q=97` but only **2 of 400** at `q=193` (`m_engine_results.txt:14-19`).

**The positive control is the load-bearing part of this negative.** The same engine, same DFS, same budget, same ensemble reaches the **full target 9 of 9 at `m=3` on both fields**. Without it the `m=4`/`m=5` ceilings would be uninterpretable.

---

## D3 — `(OUT-m)` STRESS TEST, CORRECTED FORM

**The corrected statement I tested** (`statement.md:3220-3236`, read from the node; the brief's paraphrase agrees, so R7.5 did not trigger): `X'_g + 2X''_g >= m-1 - eps~_g` with `eps~_g` the **total** saturation deficiency on `S_gamma` and `eps~_g <= 1+O` per slope; aggregate `sum_g eps~_g <= (m-1)(1+O)`; the `X=0` corollary gated on `O <= m-3`.

**I re-derived the display from scratch** before testing: outside demand `(rho-X)(m-1) - eps_out` against capacity `(rho-1)(m-1) - sum_delta I_in` with `sum_delta I_in = (m-2)X' + (m-3)X'' - def_in`, rearranging to the display. It reproduces exactly.

**Stress 1 — the banked `m=3` witness, both fields** (`sel_layer_results.txt`, `m=3 WITNESS` blocks):

```text
q = 97  : per-slope min slack 0 (TIGHT on slope 55: X'=2=m-1) -> HOLDS
          max eps~ per slope 1 = 1+O -> OK ; deficient point 66 is OUTSIDE W, t_x = 2
          AGGREGATE sum_g eps~_g = 2 = (m-1)(1+O) = 2      -> EXACTLY TIGHT
          the REFUTED original rider (<= 1+O = 1) FAILS 2 > 1 -> coordinator catch reproduced
          X=0 gate O <= m-3 = 0 : O = 0, corollary APPLIES ; min X = 2
q = 193 : identical structurally (tight slope 43; deficient point 21 outside W)
```

> **A refinement I offer (AUDIT-AND-DRAFT, nothing applied).** The aggregate is not merely bounded, it is an **identity**: `sum_g eps~_g = sum_x def(x) * t_x`, verified `2 == 2` on both fields, where `t_x` is the number of type-2 blocks through `x`:
> ```text
> x outside W      : t_x = m - def(x)        -> a unit of deficiency charges m-1
> x in S_g D S_h   : t_x = m-1-def(x)        -> charges m-2
> x in S_g ^ S_h   : t_x = m-2-def(x)        -> charges m-3
> ```
> So `(m-1)(1+O)` is attained **only** by outside deficiency. The `m=3` witness attains it (deficient point outside, charge 2); the `m=2` exhibit does not (deficient point inside `W`, charge `m-2 = 0`) — which is exactly the coordinator's diagnosis at `FABLE_AUDIT.md:41-47,55-58`, now as an equality rather than a bound. **This is the deficient-point-placement stress the brief asked for, and both banked placements are reproduced.**

**Stress 2 — a new consequence, `(DEG-m)`.** In a `sigma`-symmetric design `X'_gamma = 2 deg_H(gamma)` and `sum_gamma X''_gamma = (m-1)(m-2)` exactly, so the corrected form becomes a **min-degree law with a budget**:

```text
deg_H(gamma) + X''_gamma >= ceil( (m-1-eps~_gamma) / 2 )
   m=2: >=1   m=3: >=1   m=4: >=2   m=5: >=2   m=6: >=3   m=8: >=4
```

At `m=3` this is **exactly tight** on the witness's two degree-1 slopes and is satisfied by `al0` through `X''=2` with `deg_H = 0` — the full measured `X`-profile `[2,2,2,4,4,4,4,4,4,4,4]` is reproduced by `X = 2 deg_H + X''`. **At `m >= 4` a degree-1 slope requires middle support**, a constraint r34's `m=4` DFS never imposed (it capped degrees from above only) — so its ceiling 7 was measured on a **relaxation** of the true problem. The `Z_12` and DFS certificates both survive the tightening (min degree 3 and 2), so the selection layer stays satisfiable.

**Stress 3 — every configuration this round produced** (`outm_configs_results.txt`):

```text
m=4 q=193 k=9 : 15 slopes, degseq [1x6, 2x6, 3x3], pair mult 1
                6 slopes need X'' >= 1 ; demand 6 vs EXACT budget (m-1)(m-2) = 6
                -> CONSISTENT, and at the budget boundary
m=4 q=257 k=9 : structurally identical (same degree sequence, same demand 6 of 6)
m=5 q=241 k=7 : 19 slopes, degseq [1x12, 2x5, 3x2] ; demand 12 vs budget 12
                -> CONSISTENT, also exactly at the boundary
counting bound (independent of (OUT-m)): a COMPLETE m=4 configuration has
    sum_g (m-1-deg) = 3s - 36 <= 9, so at most FOUR degree-1 slopes; the k=9
    candidates have six, i.e. they are not completable without degree growth.
```

**VERDICT ON D3: the corrected `(OUT-m)` survived every stress. Falsifier R7.3 did NOT fire.** Deficient points were exercised outside `W` (the `m=3` witness) and analysed inside `W` and at middles (the charge identity); the `X=0` corollary's gate was checked and applies at `m=3` with `O=0`.

---

## D4 — VERDICT, THE `m`-BOUNDARY OF RECORD, AND THE CROSS-PILOT FLAG

```text
m = 1     : structurally disjoint, not exercised (statement.md:585-588)
m = 2     : REALIZABLE (anchor 1, two-field witness)
m = 3     : REALIZABLE (r34, two-field witness; my control reproduces the
            selection layer 9 of 9 at both fields, 28/400 and 2/400 of draws)
m = 4     : OPEN.  FIVE classes searched-negative (D1.7), ceiling raised
            7 -> 9 of 12.  Obstruction is ARITHMETIC value-confinement;
            the (OV)/linear-hypergraph selection layer is DECIDED FREE and
            measured INERT.  General non-split G untouched.
m = 5     : OPEN, and NOT easier -- 7 and 6 of 15, two fields.  The parity
            prediction is REFUTED as a predictor; the parity mechanism is
            real but subdominant.
m >= ~16  : first-moment heuristic says infeasible; HEURISTIC ONLY
```

**The one-line law of record, replacing parity:** coincidence demand `3m^2-7m+2` against a coincidence supply that is flat in `m`. `m=3` is the boundary because that is where the curves cross, and nothing about `m=4` is special.

**CROSS-PILOT FLAG (written self-contained; I read no sibling `r35_*` directory).**

> **Do not read an `m=4` obstruction of the `(OV)`/linear-hypergraph type as a mechanism.** I ablated it: removing the linearity constraint from the `m=4` selection search does not change the ceiling at either field, and the abstract selection problem is satisfiable with a 3-regular linear certificate on 12 slopes. Any lane whose `m=4` obstruction is stated in terms of the pair cap should re-run it with the pair cap removed before banking the mechanism. **The transportable object in the other direction is `(DEG-m)`**: the coordinator-corrected `(OUT-m)` forces `deg_H(gamma) + X''_gamma >= ceil((m-1)/2)` on any shared-tuple incidence structure with `X' = 2 deg_H`, i.e. a **minimum-degree law with an exact budget `sum_g X''_g = (m-1)(m-2)`** — available to any lane that needs to exclude low-incidence slopes. Note the **symbol collision**: `deg_H` already denotes the bipartite non-incidence degree in `rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction` (`statement.md:41`, PROVED bound `deg_H(gamma) >= n_X - r`). Two objects, one symbol, same `rate_half` family.

**Recommended node work (AUDIT-AND-DRAFT; I applied nothing).**
1. An addendum to the round-34 `(BIV-CURVE)` block (`statement.md:3196-3213`) recording that **the named `m=4` obstruction is measured inert** (linearity ablation, two fields), that **the selection layer is decided satisfiable** (`Z_12` certificate), that the ceiling is **9, not 7**, and that **four further classes** (`sigma(c/x)`, un-symmetrised `(3,3,3)`, `(QUAD-4)`, value-prescribed `(SPLIT-4)`) are searched-negative. The sentence *"the linearity constraint is SPECIFIC to `m = 4`"* (`statement.md:3206-3207`) should be extended: it is specific **and inert**.
2. The `m=5` parity falsifier **fired**: `statement.md:3207-3208` should record that the odd/even prediction is refuted as a realizability predictor (7/15, 6/15) while the invariant-factor mechanism survives as subdominant.
3. `(OUT-m)`'s background node (coordinator mint queue item 1, `FABLE_AUDIT.md:125-127`) should carry the **aggregate identity** `sum_g eps~_g = sum_x def(x) t_x` with the three per-placement charges `m-1 / m-2 / m-3`, and the `(DEG-m)` corollary with its budget.
4. `(QUAD-4)` is worth one line in the `(SPLIT-m)` template node (mint queue item 3) as the first non-split neighbour, with its 14-vs-10 parameter count and its measured `~50%` orbit-pool cost.

---

## PREDICTIONS vs OUTCOMES

| registered (`PREREG.md`, "## Pilot registrations") | outcome |
|---|---|
| R1.1 invariant factor Möbius in the quotient coordinate ⟹ injective on orbits, `P = 0.90` | **HIT** — 167/167 and 177/177, two fields |
| R1.2 the split is `3+3+2`, not `(3,3,3)`; anchor internally inconsistent, `P = 0.90` | **HIT — but SUBTRACTED**: the coordinator's audit already had it for `sigma(x) = -x` (`FABLE_AUDIT.md:65-72`). Only the arbitrary-involution generalisation is mine |
| R1.3 route (b) does **not** remove injectivity, `P(removes) = 0.10` | **resolved NO** — the brief's hypothesis is refuted at the derivation level |
| R2.1 `#Fix(c/x) ∈ {0,2}`, never odd, `P = 0.95` | **HIT** — 32/32 split at both fields |
| R2.3 `W` never `sigma`-stable at even `m`, `P = 0.85` | **HIT** (parity of `m-1 = 3` against `#Fix` even) |
| R2.4 route (b) is not cheaper (demand `>=` route (a)'s), `P = 0.80` | **HIT** — 37 slots vs 36, and ceiling 7 = route (a)'s |
| R3 `(SUPPLY-CODIM)` table `E = +2/-1/-12/-13/-37/-28` | **DIRECTION AND ORDERING HIT, CALIBRATION LOOSE (MISS 3)** — measured supply 8/12/9 vs the model's `P = 7/10/14` |
| R3.1(i) no witness at `m=4` or `m=5` in any searched class | **HIT** |
| R3.1(ii) parity is not the mechanism | **HIT — this is the round's main result** |
| R3.2 the decisive fork: parity says `m=5` lands, `(SUPPLY-CODIM)` says it does not | **RESOLVED FOR `(SUPPLY-CODIM)`** — 7/15 and 6/15 |
| R4.1 selection layer satisfiable, `P = 0.93`; certificate from a design | **HIT** — `Z_12` `{0,1,3}` (I predicted `KTS(15)`; the difference set is cleaner and hand-checkable) |
| R4.2 falsifier (if unsatisfiable, my verdict inverts) | did not fire |
| R4.3 pre-declared zero-power of the abstract decision | **HONOURED** — reported as a relocation, never as progress toward a witness |
| R5.1 seven prescribed values determine `phi` projectively (`7 = 6+1`) | **HIT** — the `7x8` nullspace works; ALLOC-A realises 2.96/2.97 targeted triples, matching "3 guaranteed" |
| R5.2 `P(k_max > 7) = 0.60` | **HIT** — 9 of 12, both fields |
| R5.2 `P(k_max = 12, a witness) = 0.05` | **resolved NO** |
| R6 MISS-2 guard, both directions | **USED, FIRED TWICE** — (a) stopped me reading `V3 = 12/12` as progress (it is an ablation, not a configuration); (b) caught my own `mindeg` dead parameter (MISS 2) and the powerless invariance probe (MISS 4) |
| R7.1 corrected `(OUT-m)` survives, `P = 0.85` | **HIT** — per-slope, aggregate, and on all five configurations |
| R7.2 the `X=0` gate forces `O = 0` at `m=3` | **HIT** — verified on the witness (`O = 0`, corollary applies) |
| R7.3 falsifier | **did NOT fire** |
| R8 `P(m=4 via (a)) = 0.20` | **resolved NO for the `(QUAD-4)` sub-route** (ceiling 7); general non-split `G` **not resolved** |
| R8 `P(via (b)) = 0.05` / `P(via (c)) = 0.03` | **resolved NO** (7 of 12; 8 of 24) |
| R8 `P(m=5 witness) = 0.10` | **resolved NO** |
| R8 `P(compiler transports usefully) = 0.75` | **HIT** — it decides the layer, in the opposite direction to the transport's motivation |
| R8 `P(corrected (OUT-m) survives) = 0.85` | **HIT** |
| R10.1 expected an off-by-one in slot bookkeeping | **HIT** — my `D(m)` uses `rho-1`, r34's uses `rho`; the 21-vs-22 ambiguity is real and I report both |
| R10.2 expected the `m=5` run to risk the wall | **PARTIAL** — no ramguard kill; my own internal deadline starved three cells instead (MISS 6) |

---

## ZERO-POWER DECLARATIONS

1. **Every negative is a DFS ceiling under a named budget over a named class.** Budgets: 12000–30000 nodes per draw; draws: 200–520 per `(m, q)` cell. A ceiling under a truncated search is not an upper bound (R6b).
2. **`(SUPPLY-CODIM)` is a dimension heuristic and is graded HEURISTIC throughout.** Its supply proxy is measurably wrong in both directions (MISS 3). No non-existence is inferred from it anywhere.
3. **The abstract selection-layer decision has no power over realizability.** It relocates the obstruction; it does not advance a witness (R4.3, honoured).
4. **The linearity ablation shows linearity is inert *within the classes searched*.** It does not show the `(OV)` cap is inert in general — only that it is not what stops these searches.
5. **`(QUAD-4)` is one sub-route of route (a).** A general non-split `G` — no `sigma`-symmetry, no `Q·L` factorisation — is untested, and route (a) is **not** closed.
6. **Two fields per scale is not `q`-uniformity** (`F_97/F_193` at `m=3`; `F_193/F_257` at `m=4`; `F_241/F_401` at `m=5`). No claim at official scale.
7. **No configuration this round was completed.** No outside completion, no bivariate system, no `W`, no per-side split verified (MISS 7, MISS 8). Every object is a selection-layer object; the only complete configuration tested is the banked `m=3` witness.
8. **Layer A was not run**; **`(SAT3)`-conditionality is untouched**; **`m = 1` was not exercised**.
9. **The `m=3` positive control validates the harness, not the measure.** It shows the engine finds what exists; it says nothing about how many `m=3` witnesses there are.
10. **`(DEG-m)` is a corollary of a POSED (not proved) statement.** `(OUT-m)` is posed with coordinator corrections (`statement.md:3220`); everything I derive from it inherits that status.
11. **The `k=9` `m=4` candidates are not near-witnesses.** They are 9 of 12 with six degree-1 slopes against a completeness bound of four — i.e. **provably not completable as they stand**, and reported as ceiling evidence only.

---

## MEASURED FUNCTIONALS (CATCH-19C)

`m, N=16m, rho=4m-1, R=8m, e=m, T=rho+2, T_1=2, T_2=rho, a=7m-1, delta=m-1`; `|S_g ^ S_h| = m-1`, `|S_g D S_h| = 6m`; `S_gamma, d_x, A_x, O, def(x)`; `X_gamma, X'_gamma, X''_gamma, eps~_gamma`; `t_x` (type-2 blocks through `x`). **New here:** the shared-tuple hypergraph `H` with its degree sequence, **pair-multiplicity** and its general cap `floor((m-1)/2)`; the three-way ablation (linearity / slope budget / both); the **coincidence count** `C = k(m-1) - |slopes|` as the common currency across `m`; the pencil parameter count `P(class)`; the **discriminant-square rate** of a non-split invariant quadratic (`15.7/32`, `15.6/32`); the number of **targeted triples realised** per prescribed draw (`2.96/2.97`); the `7x8` prescription nullspace; the **aggregate identity** `sum_g eps~_g = sum_x def(x) t_x`; the middle-support budget `sum_g X''_g = (m-1)(m-2)`; the completeness bound on degree-1 slopes. **Registered but not measured:** per-side incidences `|S_gamma ^ S_g|` on the `m=4` candidates (MISS 8); the outside completion and the bivariate system at any `m` (MISS 7); layer A anywhere.

---

## COMPLIANCE

**Registrations.** R0–R10 were appended to `PREREG.md` under `## Pilot registrations` with the **Edit tool**, after reading **exactly** the two named anchors and **before any other read, any grep, any `ls`, and any interpreter invocation**. No post-registration addenda; the two registration weaknesses (R3's supply proxy, R5's `KTS(15)` guess) are reported as outcomes, not edited.

**Compute law — NO BREACH. Nine interpreter invocations, all nine `tools/ramguard PROFILE -- python3 ...` from the repo root with the literal `--`.** `tiny` x2 (`RAMGUARD_TIMEOUT=55` each: `sel_layer.py`, and its re-run after the MISS-2 fix), `local` x7 (`RAMGUARD_TIMEOUT=290` each: `m_engine.py` x4, `m4_struct.py`, `route_bc.py`, `outm_configs.py`). **Zero bare `python3` invocations, for any purpose** — no file patching, no no-op probes, no heredocs. **Ramguard status: nine clean exits, zero wall kills, zero failures.** The only starvation was my own internal `DEADLINE` argument (MISS 6), not the guard. Stdlib only (`random`, `sys`, `time`, `itertools`); no Modal, no network, no git, **no subagents spawned**.

**Write discipline — NO BREACH.** Every file edit went through the **Write/Edit tools** (`sel_layer.py`, `m_engine.py` x2 edits, `m4_struct.py`, `route_bc.py`, `outm_configs.py`, `PREREG.md`). **No `sed -i`, no `awk -i`, no `perl -i`, no `tee`, no shell redirection onto an existing file, no in-place shell stream edit of any file** — the round-34 censure does not recur. One `cp` copied four banked scripts (`biv_core.py`, `m3_phi.py`, `m3_build.py`, `m4_search.py`) from `r34_bivcurve_m34/` into my own directory before use, which the brief explicitly requires; it is a byte copy, not a stream edit. Scripts wrote only their own results and checkpoint files (explicitly permitted).

**Banked scripts — honest declaration.** `m4_search.py` was **read** (as the template for the constraint set and for apples-to-apples fairness) and **never executed**, because it writes its results into the `r34` directory and executing it would breach write scope. `m3_phi.py` and `m3_build.py` were copied and **never executed** for the same reason. **`biv_core.py` was copied but never imported** — my engine defines its own `mu_N`. Consequently, unlike round 34, **nothing this round is gated by bank 2's independent verifier** (MISS 7); the `m=3` witness data I audit was read verbatim from the banked `m3_build_results.txt`.

**RAM discipline.** `dag.json` was **never opened**; it was traversed by one recursive grep in my first subtraction batch and appears there as a filename only (MISS 12), and every subsequent grep carried `--exclude=dag.json`. The only large file touched (`critical/nodes/rate_half_band_crossing_location/statement.md`, >3400 lines) was read **only** through `grep -n` and two bounded `sed -n` windows (`3180-3270`, `3205-3216`). All computation is small: the largest object is a 40-orbit tuple list; every driver writes its own results file and `m_engine.py`, `m4_struct.py`, `route_bc.py` additionally checkpoint (`m_engine_ckpt.txt` 4789 B, `m4_struct_ckpt.txt` 831 B, `route_bc_ckpt.txt` 908 B), so every batch is independently recoverable.

**Quarantine — CLEAN.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was **never opened and never appeared in any tool output**. **`notes/pilots_20260811/` was never `ls`-ed**; the only directories listed under it were my own and `r34_bivcurve_m34/` (explicitly readable), each by exact path. **No other `r35_*` directory was read, listed, or named by any tool.** Every recursive grep carried `--exclude-dir` at the **SEARCH** level (`pilots_20260811`, `pilots_20260802`, `prize-codex-1/2/3`, `.git`, `__pycache__`); **no output filtering after traversal was used at any point**. No path containing `prize-codex-` was touched.

**Write scope.** Every write is inside `notes/pilots_20260811/r35_bivcurve_m4/`: `PREREG.md` (registrations), five new scripts, four copied scripts, seven results files, three checkpoint files. **No** `dag/`, `nodes/`, `critical/`, `background/`, `experiments/` or `tools/` edits; no git; the session scratchpad was not used and no scratch file went to `/tmp`. The node work in D4 is a **recommendation only — nothing was applied** (AUDIT-AND-DRAFT).

**Method discipline.** Own-repo greps (CATCH-24A) preceded every novelty claim, **including hyphenated and infixed variants** (`"linear hypergraph"` 0 vs `"linear-hypergraph"` 10 — the round-34 catch reproduced), and produced **eight live subtractions, two of which are load-bearing**: the coordinator's own audit already contained my R1.2 (`FABLE_AUDIT.md:65-72`), and a **PROVED `deg_H(gamma)` lower bound already exists in a sibling `rate_half` lane** (`...active_partition_incidence_reconstruction/statement.md:41`). Two-field confirmation on every structural claim. Every quantifier claim carries a `file:line`. Every max-quantified claim carries a zero-power declaration and its search budget. The round's self-caught errors — the dead `mindeg` parameter, the zero-power invariance probe, the unmatched `m=4` budgets, the starved first run, the `dag.json` grep — are reported as errors, in the misses section, ahead of the results.

**`REPORT.md`.** The brief pre-declares that the harness refuses this write, so I did not spend a tool call attempting it; **the directory contains 23 entries and no `REPORT.md`**, and this report is returned verbatim as the final message per the brief's fallback clause.
