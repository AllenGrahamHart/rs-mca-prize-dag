(RECOVERED 2026-08-06: this pilot's final-message report was never persisted at bank time — a systematic coordinator defect caught by the round-16 es_boundary_adversary pilot. Recovered VERBATIM from the session transcript by task-id; the opening sanity line matches the ledger's bank entry. The FABLE_AUDIT.md in this dir remains the audit of record.)

Final replay is clean and deterministic (213 checks, 4 deliberately-recorded failures, all my own mis-specified checks with corrected forms passing). REPORT.md writes are harness-blocked, so the report is below.

**Files** (all under `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/fullrank_divisor_count/`): `PREREG.md`, `dualform.py`, `rankstrat.py`, `cosetrank.py`, `maximalfam.py`, `rows.py` + sibling `.json` result files. Nothing outside this directory was written; `sl2_unstructured/algebra.py` imported read-only.

---

# FULL-RANK WINDOW-DIVISOR COUNT — REPORT (Opus 5, 2026-08-04)

Target: `xr_band_fullrank_window_divisor_count` (TARGET, red leaf). Pre-registration in `PREREG.md`, plus three dated in-file rounds (`rankstrat.py` S1–S4, `cosetrank.py` E1–E3, `maximalfam.py` X0–X2), each written before its file was run.

## 0. VERDICT — PARTIAL with an exact boundary

`25|R_d| &lt;= 17n^2` is **NOT proved**; it was not falsified. Delivered: (1) an exact dual coordinate system, (2) a new rank theorem that **routes the campaign's only recorded band adversary to the sibling leaf**, (3) a machine-verified route cut showing full rank buys no anti-concentration, (4) a dual-form proof of why the big families are non-maximal, (5) the exact `(M,d)` structured-survival region at the prize rows — which lies **inside this leaf**, and (6) a quantified route for the structured half plus the named obstruction for the aperiodic half.

## 1. Dual form (P1/P2 CONFIRMED, exhaustive)

With `sigma(w)=(w_k..w_{n-1})`, `gamma(t)=(t^-k..t^-(n-1))`, `Syn(T)=span{gamma(t):t in T}`: `dim Syn(T)=|T|` (MDS) and clause 1 of `R_d` is exactly the **2-plane containment** `pi = &lt;sigma(u),sigma(v)&gt; ⊆ Syn(T)` (`dualform.py` D0/D1/D1j, exhaustive over every divisor, 5 fixtures × 3 draws, 0 mismatches, both directions). Annihilator form `W_T = Syn(T)^⊥ = {Y^i E_{T^-1} : i&lt;d}` (check C0). So the leaf reads: *how many spaces `E_{T^-1}·F_q[Y]_{&lt;d}` can one fixed codimension-2 subspace of `F_q[Y]_{&lt;n-k}` contain?* Both `rank J_d` and `|R_d|` depend on `pi` **alone** — the leaf is a statement about one point of `Gr(2,n-k)`.

**Tangent gate = near-MDS position** (D2, 8 draws, exact): in `F^{n-k}/pi` a dependence among `{bar-gamma(t)}_{t∈B}` *is* an error of some pencil member supported in `B`; hence max agreement `= A` ⟺ smallest dependent subset has size `n-A`. New utility: exact ceiling over **all** `q+1` members in `O(C(n,k)·n)` (the interpolant is affine in `z`, so each coordinate votes for one slope) — the sibling pilot sampled slopes.

## 2. THEOREM SHIFT (new, proved) — the recorded adversary leaves this leaf

For a cyclic shift pencil `v_j = u_{j+delta}` (i.e. `v(x)=x^-delta u(x)`; the banked MC-5 pencil), the rows of `R_v(d)` are those of `R_u(d)` shifted, so the stacked row set is a union of two length-`d` cyclic intervals:

```
rank J_d &lt;= d + min(|delta|_cyc, d)
```

verified with **equality** at 25 `(n,k,d,delta)` fixtures (`rankstrat.py` A/S1, S1b). Hence every shift pencil with `|delta|_cyc &lt; d` is deficient → sibling leaf.

**COROLLARY (PREREG P3 REFUTED, F2 fired).** The recorded sub-depth coset adversary (`sl2_unstructured/planted.py`, the P3-evading mixed-class lift) **is** such a shift pencil, `delta = rho_u - rho_v + M = 1`, `rank J_4 = 5 &lt; 8 = 2d`. It is owned by `xr_band_forced_commonroot_syzygy_count`, not by this leaf.

## 3. Route cut: full rank buys nothing (P4 CONFIRMED)

Extremal search over 2-planes, constrained to `rank J_d = 2d`:

| fixture | `r'-2d` | divisors | max full-rank raw family | excess over equidistribution |
|---|---|---|---|---|
| `n=14,k=4,d=3,q=29` | 1 | 3432 | 8 | 20.4 bits |
| `n=16,k=4,d=3,q=97` | 3 | 11440 | **120** | **33.0 bits** |
| `n=16,k=4,d=3,q=17` | 3 | 11440 | **120** | 17.9 bits |

The `n=14` fixture is band-proper (`h=5`, band `[3,3]`, `d=3`) and gate-consistent — genuinely in scope. The identical `120/11440` at `q=17` and `q=97` shows this is not a small-field accident. The node's own no-go ("full linear codimension alone is not an anti-concentration proof") now has a witness.

## 4. Why those families die — LEMMA X0 (new proof, dual k-packing)

If `|T_1 ∪ T_2| &lt;= n-k`, MDS forces `Syn(T_1) ∩ Syn(T_2) = Syn(T_1 ∩ T_2)`, so both errors are supported in `T_1 ∩ T_2`, the true core is deeper, and **neither locator is maximal**. Hence two distinct maximal depth-`d` locators satisfy `|T_1 ∪ T_2| &gt;= n-k+1`, i.e. `|S_1 ∩ S_2| &lt;= k-1` — banked k-packing, re-derived as a **transversality** condition (`maximalfam.py` X0, 0 violations). This explains addendum 7 in one line: **raw inflation = the degenerate (dependent-union) regime; the maximal currency = the transversal regime.** Every large full-rank family in §3 has `maximal = 0`; families grown *under* the union condition are all-maximal and small (`raw = maximal = 3`). The full-rank stratum is **not vacuous**: full-rank 2-planes with 2- and 3-member maximal families exist (X1). Toy maximal counts are `O(1)` (X2) — as pre-committed, no count claim follows from any toy here.

## 5. Exact prize-row arithmetic (P6 CONFIRMED, sharpened)

- **R1 (new).** `J_d` is `2d×(r'+1)`, so full rank needs `n-k &gt;= 3d-1`; observed rule `rank = min(2d, r'+1)`. Margins at the three prize rows: **×64.0 / ×74.7 / ×160.0**; affine window dimension `r'-2d` between `1.62e12` and `2.06e12`.
- **R3 (new).** `h = 2^s+1` and `M | 2^s`, `M | d` force `h-d = jM+1`, `j&gt;=1`; THEOREM L then gives `1 &lt;= j &lt;= J(M) = min(⌊(⌊h/2⌋-1)/M⌋, ⌊(n-k-h+1-M)/(M(M-1))⌋)`. Surviving scales are exactly `M = 2^1..2^20` at all three rows (banked audit confirmed; F5 does not fire), with depth counts e.g. prize 1/4: `2^1:2147483647, 2^10:1566201, 2^15:1528, 2^19:5, 2^20:1`. At the top scale exactly **one** depth survives: `d = 8588886016` (1/4, 1/8), `d = 4293918720` (1/16), `h-d = 2^20+1`. THEOREM L is essentially inactive below `M ~ 2^9`.
- **R4.** Budget `17n^2/25 = 2^81.44`; raw first moment at the low band end `2^-4.08e11 / 2^-9.92e11 / 2^-3.49e11` at `q = 2^256` (banked ~`3.6e11`-bit order reproduced). Evidence only — an average, not a worst case.

## 6. Routing (E1'): the structured residual is THIS leaf's problem

Generic one-class (coset) pencils — both P3-evading `a != b` and common-class `a = b` — are stacked-**full** rank in 285/288 draws over 6 fixtures × 4 class patterns (3 exceptions are accidental syzygies at `q=41`). So the shift sub-case is deficient (sibling), but the **general** coset class is full-rank: the entire surviving region `M = 2..2^20` of R3 is an obligation of **this** leaf.

## 7. The exact boundary — what the leaf still needs

**(a) Structured residual**, scales `M ∈ [2, 2^20]` on the R3 region, currently excluded only by first-moment heuristics. *Quantified route:* THEOREM D bijects scale-`M` locators with the quotient instance `(n/M, k/M, d/M)`; the upstairs budget is `0.68n^2 = 0.68 M^2 (n/M)^2`, so **any** quotient count bounded by the same absolute number `0.68n^2` discharges the whole class — a factor `M^2` (up to `2^40`) weaker than the quotient's own occupancy statement. **Flagged gap:** transfer of maximality / `L_P&gt;=2` / strip survival through that bijection is not checked here and must be proved first.

**(b) Aperiodic residual** (scale-1). Boundary is sharp and negative: full rank + linear codimension + MDS position + the tangent gate do **not** bound the count; k-packing only separates maximal from raw. All four lenses are equivalent up to banked bijections and terminate in the same missing input:

```
divisor:    |R_d| &lt;= 0.68 n^2                     (this leaf)
list:       min_z L(w_z) &lt;= 0.68 n^2              (sub-Johnson RS list size)
slope:      |Gamma_band| &lt;= 1.32 n^2              (PROPOSITION 5: unavailable)
projection: 25 sum_z W_d(z) &lt;= 17n^2(q+1-beta_d)  (W17)
```

**Named obstruction:** an arithmetic anti-concentration theorem for split divisors of `X^n-1` on a codimension-`2d` window — equivalently a sub-Johnson list-size bound for RS on `mu_n` under the tangent gate. The only mechanism ever exhibited (coset/MC) is arithmetic, which is why the strips and THEOREM L do the real work.

## 8. Refuted / corrected predictions (honest record)

| id | prediction | outcome |
|---|---|---|
| P3 | recorded coset adversary is full rank | **REFUTED** — shift pencil, deficient (F2 fired) |
| D3 (as first written) | random pairs always full rank | over-broad; `rank = min(2d, r'+1)`; corrected D3' passes |
| E1 (as first written) | one-class pencils full rank in *every* draw | over-strict; 285/288; corrected E1' passes |
| E3 | toy full-rank families never band-proper | **REFUTED** at `n=14,k=4,d=3,q=29` — that fixture is in scope, which strengthens §3 |
| X1 (first selection rule) | global best vs. full-rank | selection flaw; per-stratum tracking, then passes |
| rows.py R3 (first pass) | `j`-loop with 4096 guard | truncated small-`M` rows; replaced by exact closed form |

F1 (node falsifier) did not and could not fire — toys are subcritical (`0.68n^2` exceeds `C(n,r')` at every reachable size). F3–F6 did not fire.

## 9. Flags

1. The `M^2`-slack route rests on an unverified transfer of maximality/liveness/strip survival through THEOREM D's bijection.
2. §3's excess-bit figures are toy-scale: they establish *no anti-concentration from rank*, not a lower bound at the rows.
3. E1's 3 exceptions are small-field accidents; the `q`-pin is load-bearing for "coset pencils are full rank".
4. THEOREM SHIFT covers *exact* cyclic shifts. Approximate shift pencils (shift + low-weight window perturbation) are not covered; whether the deficient stratum is closed under such perturbations is open and worth one round — it decides how much of the coset class the sibling leaf really owns.
5. No node file touched; only the pilot directory written.

## 10. Subtraction (hard law 5)

CONSUMED: LEMMA W / THEOREM D / R / L (`xr_window_system_descent`); the rank-syzygy router; `(WPR)`, projection injectivity at `2d&gt;=h`, `beta_d`; the maximality fiber identity (addendum 7, `ld_core_count`); k-packing exclusivity (item 9 — §4 re-derives it dually and says so); BP(1)/BP(3)/THEOREM 5; MC-1/MC-3/MC-5 + KEY LEMMA; the six-row table; the coset lift and its P3 evasion; the dead routes (single-word Johnson, raw-subset packing, `N = 1/rate`, slope-side `1.32n^2`).
NEW: the dual syndrome-2-plane / near-MDS form; THEOREM SHIFT + the adversary routing; the machine-verified route cut; LEMMA X0 and the transversality reading of raw-vs-maximal; the exact `(M,d)` survival region and the `n-k &gt;= 3d-1` non-vacuity rule; E1' routing the coset class into this leaf; the `M^2`-slack self-reduction.

## 11. Reproduction (repo root)

```
tools/ramguard local -- python3 notes/pilots_20260804/fullrank_divisor_count/dualform.py    # 56 checks, 1 recorded fail
tools/ramguard local -- python3 notes/pilots_20260804/fullrank_divisor_count/rankstrat.py   # 67 checks, 0 fail
tools/ramguard local -- python3 notes/pilots_20260804/fullrank_divisor_count/cosetrank.py   # 57 checks, 3 recorded fails
tools/ramguard local -- python3 notes/pilots_20260804/fullrank_divisor_count/maximalfam.py  #  9 checks, 0 fail
tools/ramguard tiny  -- python3 notes/pilots_20260804/fullrank_divisor_count/rows.py        # 24 checks, 0 fail
```

result: PARTIAL on red leaf `xr_band_fullrank_window_divisor_count` — not proved, not falsified; new THEOREM SHIFT (`rank J_d = d + min(|delta|,d)`) routes the campaign's only recorded band adversary to the sibling syzygy leaf, a machine-verified route cut kills "full rank ⟹ anti-concentration" (120 of 11440 divisors on a full-rank codim-2d window, 33 bits above equidistribution), and the exact prize-row survival table (coset scales `M = 2..2^20`, one depth at the top scale) plus E1' show the whole surviving structured class is *this* leaf's obligation, leaving exactly two residuals: the structured region (discharged by any quotient count `&lt;= 0.68n^2`, an `M^2`-slack self-reduction, with one flagged transfer gap) and the aperiodic scale-1 case (named obstruction: arithmetic anti-concentration / sub-Johnson RS list size on `mu_n`).