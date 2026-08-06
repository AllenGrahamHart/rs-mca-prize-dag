# FULL-RANK WINDOW-DIVISOR COUNT — PRE-REGISTRATION

Opus 5, 2026-08-04 (round 13, wave-46 red leaf #1).
**Written BEFORE any code was run in this directory.**

Target: `xr_band_fullrank_window_divisor_count` (TARGET, red leaf).

Sources read first, read-only:
`critical/nodes/xr_band_fullrank_window_divisor_count/{node.json,
statement.md,attack.md}`;
`critical/nodes/xr_band_high_window_exclusion/{statement.md,node.json,
conditional.md,attack.md}`;
`critical/nodes/xr_band_maximal_window_divisor_count/{statement.md,
conditional.md,attack.md}`;
`background/nodes/xr_window_system_descent/{statement.md,proof.md}`;
`background/nodes/xr_joint_window_rank_syzygy_router/{statement.md,
proof.md,node.json}`;
`background/nodes/xr_band_windowed_projection_reduction/{statement.md,
proof.md}`; `notes/pilots_20260803/sl2_unstructured/{PREREG.md,
FABLE_AUDIT.md,algebra.py,planted.py}`;
`notes/band_heart_consolidation_20260803/CONSOLIDATION.md` (all six
UPDATEs + the CORRECTION); `notes/BAND_LANE_DEFINITIONS.md` (items
2,3,7,8,9,10 + addenda 5,6,7); `notes/pilots_20260803/listsize_program/
rows.py` (the six-row table).

## 0. The obligation, pinned verbatim

Fix an official prize row (`n = 2^41`; `k = n/4, n/8, n/16`;
`h = 2^33+1, 2^33+1, 2^32+1`; `A = k+h`; `q >= 2^250`, `n | q-1`,
`H = mu_n`), a globally generic-branch received pair `(u,v)` after the
ratified strip order, and a band-proper high depth
`ceil(h/2) <= d <= h-2`, `r' = n-k-d`.  `R_d(u,v)` is the set of monic
degree-`r'` divisors `E_T | X^n-1` such that

1. the top `d` coefficients of both `uE_T` and `vE_T` mod `X^n-1` vanish;
2. the reconstructed pair's full joint agreement set is exactly `H\T`
   (**maximality**, size `k+d`);
3. that pair has `L_P >= 2` selected live slopes (support-wise
   first-match selector, definitions items 7-8);
4. it survives the ratified strip order.

**Hypothesis of this leaf:** `rank J_d(u,v) = 2d` (full stacked
Toeplitz rank; the complementary stratum is the sibling red leaf
`xr_band_forced_commonroot_syzygy_count`).

**Assertion:** `25|R_d| <= 17n^2`.

Node's own no-go, restated so I cannot drift: *"Full linear codimension
alone is not treated as an anti-concentration proof."*

## 1. Predictions (P1-P8)

- **P1 (DUAL FORM — the syndrome 2-plane).** Write
  `sigma(w) = (w_k,...,w_{n-1})` for the top coefficients of the
  interpolating polynomial of a received word `w`, and for `T <= H`
  let `Syn(T) <= F_q^{n-k}` be the span of the `n-k`-vectors
  `gamma(t) = (t^{-k}, t^{-k-1}, ..., t^{-(n-1)})`, `t in T`
  (the syndromes of the point masses, a rational normal curve).  Then
  clause 1 of the obligation is **exactly**

  ```text
  pi := span(sigma(u), sigma(v))  subseteq  Syn(T),
  ```

  a 2-plane containment, and `dim Syn(T) = r'` always (MDS).  Predicted:
  EXACT agreement with LEMMA W's joint solution set, 0 mismatches,
  exhaustive over all `C(n,r')` divisors at every toy fixture.
- **P2 (TANGENT GATE = near-MDS position of the projected curve).**
  Project `F_q^{n-k} -> F_q^{n-k}/pi`.  A linear dependence among
  `{bar-gamma(t)}_{t in B}` is exactly an error vector supported in `B`
  whose syndrome lies in `pi`, i.e. an error of one pencil member
  `w_z = u+zv`.  Hence the tangent gate (max agreement `<= A` over all
  of `P^1`) is EQUIVALENT to: every `B` with `|B| <= n-k-h-1` has
  `{bar-gamma(t)}_{t in B}` independent.  Predicted: exact equivalence,
  0 mismatches on toys.  Consequence to be recorded: the leaf is a
  question about `r'`-subsets of a near-MDS point configuration that
  carry a **2-dimensional** dependency space, every dependency of
  support `>= |T| - (h-d)`.
- **P3 (THE RANK SPLIT DOES NOT ISOLATE THE RECORDED ADVERSARY).**
  The campaign's own surviving structured adversary — the sub-depth
  coset family of `sl2_unstructured/planted.py` (`u = X^{rho_u}U(X^M)`,
  `v = X^{rho_v}V(X^M)`, `rho_u != rho_v`, `M | d`, `M < d`, P3-evading)
  — has **full** stacked rank `rank J_d = 2d`.  Predicted: FIRES.  If it
  fires, this leaf inherits the entire coset/MC adversary and no
  "genericity" reading of full rank is available.
- **P4 (ANTI-CONCENTRATION FAILS UNDER FULL RANK ALONE).**  For that
  full-rank fixture the raw solution count exceeds the equidistribution
  value `C(n,r')/q^{2d}` by a large, measurable factor (report the
  excess in bits, and the same for a double-MC full-rank pair).
  Predicted: excess `>= 20` bits already at `n = 16`, growing with `q`.
  This is a ROUTE CUT (codimension does not bound the count), not a
  node falsifier.
- **P5 (TOY SUBCRITICALITY — pre-committed non-claim).**  For random
  full-rank `(u,v)` at toy rows, `|R_d^raw| in {0,1}` and the maximal
  selected count is `0` in almost every draw.  No count claim of any
  kind will be based on a toy: the budget `0.68n^2` exceeds the total
  divisor count `C(n,r')` at every reachable toy size, so a toy can
  neither confirm nor refute `(SL2-RES)`.  Predicted and pre-committed.
- **P6 (EXACT STRUCTURED-SURVIVAL TABLE INSIDE THE FULL-RANK STRATUM).**
  Combining `M | gcd(n,k,d)`, band-properness, `h` odd (so `h-d` is odd
  and `d <= h-3`), and THEOREM L (`M <= floor(r'/(h-d))`), the coset
  scales that survive every proved exclusion at the three prize rows are
  exactly the powers of two `2 <= M <= 2^20`, and for each such `M` only
  the depths with `h-d <= r'/M` — a thin slice at the TOP of the band.
  Predicted: max surviving `M = 2^20` at all three rows (matching the
  banked audit summary), with the exact `(M,d)` region computed here in
  exact integers for the first time.
- **P7 (LIFTED-MC PARITY).**  The specific lifted adversary of
  `planted.py` has upstairs excess `h_up` with `d = h_up - M`; combined
  with `M | d` this forces `M | h_up`.  Predicted: therefore that exact
  family is EMPTY at `h` odd (official rows) — the surviving structured
  residual is the *general* `M`-coset family with `h-d` odd `>= 3`, not
  the lifted-MC one.  (A sharpening of the recorded "M = 2^1..2^20
  survive", not a contradiction of it.)
- **P8 (MAXIMALITY IS NOT WHAT SAVES THE FULL-RANK STRATUM).**  For the
  structured full-rank fixtures, report RAW vs MAXIMAL vs
  `L_P>=2`-selected counts.  Predicted: the maximality filter removes
  the raw binomial inflation but leaves a family whose size still
  exceeds the equidistribution value by many bits — i.e. clause 2 alone
  does not restore anti-concentration.

## 2. Falsifiers (F1-F6)

- **F1 [the node's own falsifier].** One prize row, one band-proper high
  depth, full stacked rank, and an auditable family of more than
  `17n^2/25` locators passing clauses 1-4.  **PREDICT: NOT FIRED by this
  pilot** — by P5 no toy can reach it; a positive answer needs a
  prize-row construction, which this pilot does not attempt to complete.
- **F2 [P3 fails].** The recorded structured adversary is stacked-rank
  DEFICIENT.  **PREDICT: does not fire.**  If it does fire, that is
  GOOD news for this leaf (the adversary routes to the sibling leaf) and
  must be reported as such, loudly.
- **F3 [dual form wrong].** A toy divisor satisfying the window
  equations but not `pi <= Syn(T)`, or conversely.  **PREDICT: NEVER.**
- **F4 [gate equivalence wrong].** A toy pencil passing the tangent gate
  with a dependency of support `<= n-k-h-1` in the projected
  configuration, or vice versa.  **PREDICT: NEVER.**
- **F5 [survival table disagrees with the banked audit].** The exact
  integer computation gives a maximal surviving scale different from
  `2^20` at some prize row.  **PREDICT: does not fire**; if it fires,
  the banked audit line is corrected by this pilot (report as a catch).
- **F6 [an accidental proof].** A proof of `25|R_d| <= 17n^2` from full
  rank + the four clauses alone.  **PREDICT: does not fire.**  Standing
  honesty rule for this pilot: any claimed proof must be reduced to
  named proved nodes plus explicitly-listed new lemmas, each machine
  checked on toys; a first-moment or average-case estimate will NEVER be
  reported as a proof of a worst-case bound.

## 3. What each outcome means

| outcome | verdict |
|---|---|
| F1 fires | the leaf is FALSE; SL-2-RES and SL-2 die; flag immediately |
| P3 + P4 fire, F1 does not | PARTIAL: the rank split is a genuine dichotomy but the full-rank side inherits the whole arithmetic problem; report the exact boundary and the named obstruction |
| F2 fires | the full-rank stratum is cleaner than believed; re-price both leaves |
| F5 fires | catch against the banked SL-2 audit summary |
| F6 fires | PROVED (extraordinary; would require an anti-concentration theorem the program does not own) |

## 4. Compute discipline

Every run `tools/ramguard {tiny,local} -- python3 ...` from the repo
root, literal `--`.  No network, no Modal.  Nothing outside
`notes/pilots_20260804/fullrank_divisor_count/` is written; sibling
pilot code is imported READ-ONLY via `sys.path`.  Every fixture is
exhaustive over `C(n,r')` divisors; every claim in the report carries a
machine check id or is explicitly labelled as an argument.

## 5. Subtraction notice (hard law 5), stated up front

CONSUMED, not re-derived: LEMMA W, THEOREM D (descent bijection),
THEOREM R (single-word Toeplitz rank `d`), THEOREM L (liveness/parity
scale exclusion) — `xr_window_system_descent`; the rank/syzygy router
(`xr_joint_window_rank_syzygy_router`); `(WPR)`/`(WPR')`, the
projection injectivity at `2d >= h` and `beta_d`
(`xr_band_windowed_projection_reduction`); the maximality fiber identity
`RAW_d = sum_e MAX_e binom(k+e,k+d)` (definitions addendum 7,
`ld_core_count`); k-packing exclusivity of selected supports
(definitions item 9); the six-row table (`listsize_program/rows.py`);
BP(1)/BP(3)/THEOREM 5 (`xr_mc_depth_quantization`); the MC-1 sparse
window specialization and MC-3 coset count
(`xr_band_key_lemma_pencil_mass`); the sub-depth coset lift and its P3
evasion (`sl2_unstructured/planted.py`, L1-L5); the recorded dead routes
(single-word Johnson; raw `(k+d)`-subset packing; the `N = 1/rate`
counting route; the slope-side `|Gamma_band| <= 1.32n^2` requirement,
CONSOLIDATION section 3 + PROPOSITION 5).
NEW here, if the predictions hold: the dual syndrome-2-plane /
near-MDS-configuration form (P1, P2) as an exact coordinate change;
the rank stratification of the recorded structured adversary (P3);
the measured concentration excess under full rank (P4, P8); the exact
`(M,d)` structured-survival region at the three prize rows (P6); the
lifted-MC parity emptiness at `h` odd (P7).
