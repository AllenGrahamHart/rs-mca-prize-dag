# E22 reconstruction + correctness gate — worst_word_challenger_pricing

- **Node:** `worst_word_challenger_pricing` (TARGET; prices/exhausts the E15
  structured non-planted challenger class).
- **Task:** E22 challenger-class census (completes the E15 repair; feeds QL.5).
- **Date:** 2026-07-04.
- **Gate outcome:** **PASSED** — census launched on Modal (app `rs-mca-e22`).
- **Modal app ID:** `ap-QykRVGNgAiJQYt8KBg5FN0`
  (https://modal.com/apps/allengrahamhart/main/ap-QykRVGNgAiJQYt8KBg5FN0),
  launched `--detach` 2026-07-04; in-Modal gate re-run `passed=True`
  (`{1:(False,0,0), 2:(True,6,0), 4:(True,23,0), 8:(True,56,0)}`); 135 cells.
  Retrieve results: `~/.venvs/modal/bin/modal app logs ap-QykRVGNgAiJQYt8KBg5FN0`
  and grep for the `E22_RESULTS {...}` JSON line.

## 0. Key correction to the task premise

The task brief states the E15 (#197) adversarial-search code is **LOST — only
prose survives**. This is **not** the case. The original verifier survives
**byte-identical** (md5 `b3561a606ff30a581dff1895ea9de2e9`) as
`experimental/scripts/verify_e15_worst_word_challenge.py` in ~34 rs-mca
worktrees (e.g. `rs-mca-upstream-xr-sunflower/…`, `rs-mca-codex-critical/…`).
The reconstruction below is therefore not a guess from prose — the exact
field/polynomial/sunflower machinery is **copied verbatim** into
`e22_core.py` / `e22_census_modal.py`, and the census simply extends the same
code. Companion note:
`experimental/notes/l1/e15_worst_word_challenge.md`.

## 1. The toy cell (STEP 1a)

- **Field:** `F_193`. `p - 1 = 192 = 2^6·3`, so it hosts multiplicative
  subgroups of every order dividing 192 — in particular `n ∈ {16, 32, 64}`.
- **Domain `D`:** the order-`n` multiplicative subgroup, `D = {g^i}_{i<n}`
  with `g = primroot^{(p-1)/n}`. Evaluation points are re-indexed by a
  **layout** permutation (`cyclic_step_c` or `shuffle_seed`).
- **Rate / radius grid:** `n = 16..64`, toy official rates `k/n ∈
  {1/16, 1/8, 1/4, 1/2}`, slack `sigma`. Petal size `ell = sigma + 1`.
  Crossing radius (agreement) `s = k + sigma`. List = all degree-`<k`
  polynomials agreeing with the received word on `≥ s` of the `n` points.

## 2. The planted sunflower family and its count (STEP 1b)

Construction of the planted received word (`sunflower_word`):

1. `core` = the first `k-1` layout points; `L_core` = their degree-`(k-1)`
   locator (monic, roots at the core points).
2. `petals` = the remaining points cut into disjoint blocks of size
   `ell = sigma+1`; `M = ⌊(n-(k-1))/ell⌋` petals; leftover = `background`.
3. Received word value: on petal `p`, `value(x) = scalar_p · L_core(x)`;
   on core and background, `value = 0`. Scalars are `linear` (`1..M`) or
   `geometric` (`5^i`).

**Planted codewords:** `{ scalar_p · L_core : p = 1..M }`. Each has degree
`k-1 < k`, so it is a legal codeword, and it agrees with the word exactly on
`core (k-1) + petal p (ell) = k + sigma = s` points (it vanishes on the core
where the word is 0, matches its own petal, and disagrees elsewhere). Hence:

> **planted_count = M = ⌊(n-k+1)/(sigma+1)⌋.**

These `M` codewords are the "planted list" the naive worst-word heuristic
claims is the entire list at radius `s`.

## 3. "List count at sigma" concretely (STEP 1c)

For the fixed planted received word, the **list count** at slack `sigma` =
the number of distinct degree-`<k` polynomials agreeing with the word on
`≥ s = k+sigma` points. Computed exactly by enumerating every size-`s`
agreement subset, interpolating the unique degree-`<k` polynomial through it
(reject if degree `≥ k` or if it fails on the remaining agreement points),
and deduplicating (`exact_cell`). `list_count ≥ M` always; the question is
whether it **exceeds** `M`.

## 4. The E15 challenger structure (STEP 1d)

A **challenger** = a NON-planted codeword appearing in the planted word's
list. `classify_pattern` labels each list member by its petal-agreement
profile:

- `planted` — one of the `M` planted scalars.
- `full_petal` — agrees fully on `≥2` petals and no partial petal.
- `mixed_petal` — touches `≥2` petals with at least one partial.
- `one_petal_nonplanted` / `background_or_core_only` — touches `≤1` petal.

The **E15 structured challenger class** = petal-structured non-planted
codewords = `mixed_petal ∪ full_petal`. The documented #197 finding: at
`sigma = 1`, the planted word's own list is **larger than `M`** — extra
`mixed_petal` codewords (plus a few `full_petal`) sit at the same crossing
radius, falsifying "planted is always worst". At `sigma ≥ 2` (exact `n=16`)
the list collapses back to exactly `M`.

**E22 third-class alarm:** any non-planted list member classified
`one_petal_nonplanted` or `background_or_core_only` is **UNCLASSIFIED** — a
challenger outside both known classes, i.e. the node's falsifier.

## 5. Correctness gate (STEP 2) — PASSED

`e22_gate_local.py` re-derives the planted word in the toy cell
(`F_193`, `n=16`, `cyclic_step_1`, `linear`) and exhaustively enumerates the
list at `sigma=1`, reproducing the E15 phenomenon exactly:

```text
  k sig   s    M  list chal uncl beats  class_counts
  1   1   2    8     8    0    0 False  {planted:8}          <- negative control
  2   1   3    7    13    6    0  True  {mixed_petal:6, planted:7}
  4   1   5    6    29   23    0  True  {mixed_petal:23, planted:6}
  8   1   9    4    60   56    0  True  {full_petal:1, mixed_petal:55, planted:4}
  control k=2 sigma=2: list=5 = M   (planted stays worst)
  control k=4 sigma=2: list=4 = M
  control k=8 sigma=2: list=3 = M
```

A non-planted structured challenger beats the planted count at `sigma=1`
for `k ∈ {2,4,8}` (and not for `k=1`), with UNCLASSIFIED = 0 — exactly the
E15 invariants (`verify_e15_worst_word_challenge.py::assert_invariants`).
**Gate PASSED.**

Interpolation cost benchmark (sizes the Modal exhaustive cap): ~90 µs/interp
at `n=16/32` (k≤8), ~510 µs at `n=64` (k=16). `1e6` interps ≈ 1.5 min
single-core.

## 6. Census design (STEP 3)

`e22_census_modal.py` (app `rs-mca-e22`, cpu=8, memory=8192, timeout 6 h;
gate re-run inside the Modal function before the census):

- **Sweep:** `sigma = 1..3`, `n ∈ {16,32,64}`, `k` = the toy official rates
  per `n`. Cheap cells get 2 layouts × 2 scalars; heavy exhaustive cells get
  a single representative layout.
- **Per cell:** exhaustive over all `binom(n,s)` agreement sets when
  `binom(n,s) ≤ 30M`; otherwise an E15-style **structured scan**
  (full-petal bounded-excess + two-petal locator pencil). The full-petal
  sub-scan is guarded (`2^M·C(core,d) ≤ 5M`) so it never explodes at large
  petal count — matching E15's pencil-only treatment of `n=64`.
- **Reported per cell:** `list_size`, `planted_count = M`,
  `classified_planted`, `classified_challenger`, `unclassified`,
  `beats_0p9_planted`, full `class_counts`, and a `challenger_count_grid`
  `(n,k,sigma,ell,M,challenger)` over the exhaustive cells for formula
  extraction.
- **Interpretation:** `total_unclassified_on_exhaustive_cells == 0` →
  `TWO_CLASSES_EXHAUST` (QL.5 two-column arithmetic closes the repair);
  `> 0` → `THIRD_CLASS_ALARM` (iterate the E15 protocol). NB the third-class
  alarm is only meaningful on **exhaustive** cells; structured scans generate
  only petal-structured candidates and cannot detect a novel third class.

Result emitted as a single `E22_RESULTS {...}` JSON line in the Modal logs.
