# L-D core-count pilot — PRE-REGISTRATION (written before any computation)

Scope: L-D, the consolidated primary route to the band occupancy lemma
(`notes/band_heart_consolidation_20260803/CONSOLIDATION.md` sections 2, 4, 5).
Row constants: `notes/pilots_20260802/support4_relation/stage5_escape.json`.

## 0. The two readings I will separate (fixed now, not after seeing numbers)

For an admissible received pair `(u,v)` and depth `d in [1, h-1]`:

* **RAW_d** := `#{Z subset D : |Z| = k+d, A(Z) = B(Z) = 0}` — the literal
  wording of L-D in CONSOLIDATION.md section 4 and in the task ("(k+d)-subsets
  Z of the n evaluation points with A(Z) = B(Z) = 0").
* **RAW_d^sel** := the same, filtered by `L_Z >= 2` (`L_Z` = number of SELECTED
  supports containing `Z`, definitions item 8).
* **MAX_d** := `#{codeword pairs (f,g) : |W(f,g)| = k+d}` where
  `W(f,g) = {x : u(x)=f(x) and v(x)=g(x)}` — i.e. cores required to be the FULL
  joint agreement set (maximal). **MAX_d filtered by `L >= 2` is the ledger's
  `N_d`** (`xr_band_ledger_theorems`: "band pair = codeword pair with joint
  agreement `Z_P` of size `k+d`").

Registered claim under test: L-D asserts `<= 0.68 n^2` for which of these.

## 1. Pre-registered falsifiers

**F1 (raw form).** An explicit `(u,v)` at a toy row with
`RAW_d > 0.68 n^2` refutes L-D in its literal (non-maximal) wording.
*My prediction, registered now: F1 FIRES.* Predicted mechanism: a single
codeword pair at depth `e > d` contributes `C(k+e, k+d)` distinct depth-`d`
joint-explanation subsets, all with `A = B = 0`.

**F2 (the `L >= 2` filter does not rescue F1).** If `Z' subset Z` and `Z` lies
in two selected supports, so does `Z'`. *Prediction: F2 FIRES* — i.e.
`RAW_d^sel` blows up too, so the selection semantics of item 8 (which is what
defeats the MC `2^197` non-example) does NOT defeat the subset explosion.

**F3 (maximal form survives).** No toy fixture will show `MAX_d^{L>=2} =
N_d > 0.68 n^2`. *Prediction: F3 does NOT fire* (the maximal reading is the
intended, defensible one).

**F4 (fiber identity).** `RAW_d != SUM_{e >= d} MAX_e * C(k+e, k+d)` on some
fixture would refute my claimed exact fiber decomposition.
*Prediction: identity holds exactly, 0 violations.*

**F5 (uniqueness of the pair).** Two distinct codeword pairs `(P,Q) != (P',Q')`
with a common `Z`, `|Z| >= k+1`, in both joint agreement sets.
*Prediction: never occurs* (interpolation uniqueness).

**F6 (internal contradiction in the ratified note).** CONSOLIDATION.md section 2
concludes "N_d counts joint-explanation (k+d)-sets of one received pair,
pairwise <= k-1". If two distinct joint-explanation `(k+d)`-sets sharing
`>= k` points exist on a fixture, that sentence is false as written.
*Prediction: F6 FIRES* (two `(k+d)`-subsets of one deep `W` share `k+d-1`).

**F7 (subtraction, hard law 5).** If the route-(1) chain
"cores -> codeword pairs -> agreement counts" is already banked upstream, this
pilot must report it as a re-derivation, not novelty. *Registered before
computing: the sweep already located `notes/pilots_20260802/xr_band_occupancy/
REPORT.md` THEOREM 2 (`N_d <= min_z #{c : agr(c,w_z) >= k+d}`, `M = 1` for
`2d >= h`), THEOREM 4 (partial linear space, `SUM_{d >= ceil(h/2)} N_d <=
|Gamma_band|/2`), PROPOSITION 5 (slope-side no-go) and the DEAD verdict on the
dimension count. I therefore predict route (1) yields NO new bound.*

**F8 (calibration).** The U-mechanism pin `N_1 = 510` at RowC 1/4 must be a
MAX/`L>=2` count, not a RAW count. If my identity predicts a RAW count
inconsistent with 510 being the recorded `N_1`, that confirms the reading
split rather than refuting it. Recorded as a consistency check, not a test of 510.

## 2. Pre-registered quantities (computed, not chosen, after this file is written)

* `g*(row, d)` := least gap `g >= 1` with `C(k+d+g, g) > 0.68 n^2` — the depth
  separation at which one single deeper pair refutes RAW_d.
* `m*(row, d, g)` := least number of depth-`(d+g)` pairs needed to breach the
  budget, `= ceil(0.68 n^2 / C(k+d+g, g))`.
* `V*(row)` := largest `V` with `C(V,2) <= 0.68 n^2` — the exact slope-count
  boundary the pair-graph bound needs.
* Toy fixture: `n=20, k=6, h=6, A=12, q=101`; cascade depth `e = h-1 = 5`,
  core size `k+e = 11`; `d = 1`, `k+d = 7`; budget `0.68 n^2 = 272`;
  predicted `RAW_1 >= C(11,7) = 330 > 272`.

## 3. What would count as PROVED / PARTIAL / OBSTRUCTED

* PROVED: an unconditional `N_d <= 0.68 n^2` at all six rows, all `d in [1,h-1]`.
* PARTIAL: a bound valid on an explicitly delimited depth range or under an
  explicitly named open input, with the exact numeric boundary printed per row.
* OBSTRUCTED: route (1) shown to terminate in a named open statement, with the
  obstruction sourced. **Registered expectation (F7): OBSTRUCTED, with the
  correction in F1/F2/F6 as the pilot's positive output.**

## 4. Compute law

All computation via `tools/ramguard tiny -- python3 ...` (256M/60s) or
`tools/ramguard local -- python3 ...` (1G/5min) from repo root. No network,
no Modal. Everything in `verify.py` in this directory.
