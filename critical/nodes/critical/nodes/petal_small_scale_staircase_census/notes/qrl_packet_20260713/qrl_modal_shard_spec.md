# Deferred Modal shard spec: QRL-MODAL-1 (falsification probe at the first open quotient size)

NOT LAUNCHED (RAM law). Pre-registered before any run.

## Purpose

The open window's binding cell is `a = k'+1` at `n' = 64`. Exact worst-case
enumeration is infeasible anywhere (`C(64,32) ≈ 1.8e18`), so this shard is a
FALSIFICATION PROBE of the missing lemma (row-level aperiodic sub-Johnson
quotient bound), not a verification: it measures the realized aperiodic
exact-agreement lists of the strongest known engineered families at the
quotient row.

## Setup

- Model rows: `n in {256, 512, 1024}`, `rho in {1/2, 1/4}`, `M in {2, 4}` so
  that `n' = n/M in {64, 128, 256, 512}`, `k' = rho n'`; fields: the first 4
  primes `q ≡ 1 (mod n)` with `q >= n^2`.
- Words: the banked g2-falsification engineered fiber-aligned family
  (catches #55-#58 generator, `critical/nodes/petal_growth/notes/
  g2_falsification_20260710/`) built directly AT the quotient row, plus its
  descended-from-parent variants, plus 64 random-scalar sunflower controls
  per (row, q).
- Enumeration: the family's OWN complete contributor generator
  (fiber-subset interpolation, the `periodic_contributors` pattern) plus
  sunflower `lambda L_Z` sweeps — complete for the constructed classes ONLY.
  HONEST CAVEAT (pre-registered): this bounds the realized-by-construction
  part; it cannot certify the worst case.
- Measure per (row, q, word): `L_P(a)` for `a in {k'+1, k'+2, k'+4, k'+8}`,
  aperiodic exact supports only.

## Pre-registered expected values (falsifier armed)

- `max L_P(k'+1) <= 2 n'` over the whole grid (the sunflower family realizes
  `~(n'-k')/2` = #petals; nothing known exceeds linear at the aperiodic cell).
- Ratio to the minted cap: `max L_P(k'+1) / ((63/64) n'^6) < 10^-6` at
  n' = 64, decreasing in n'.
- FALSIFIER: a SUSTAINED super-quadratic growth of `max L_P(k'+1)` in n'
  across n' = 64 -> 128 -> 256 -> 512 (fit exponent > 2 with all four points
  monotone) would kill the `n'^6` form's plausibility and re-open catch #106
  in a stronger form; a single super-`n'^6` cell falsifies the lemma outright.

## Budget

Per (row, q): <= 10^7 interpolations of degree < k' <= 256 — Modal-sized;
grid total <= ~3e9 field ops. Shard output: JSON of (row, q, word-class,
a, L_P) tuples + the two pre-registered aggregates.

## REFUTED-BY-DESIGN-BLINDNESS (2026-07-13, catch #126)

The probe's pre-registered expectations are FALSE: at its own grid cell
(n'=64, q=65537) every W_tau-family word has list ~2.71e13 — x2.1e11 the
expected "<= 2n'". The design enumerated CONSTRUCTED classes only and was
structurally blind to the subset-sum family (sjb refutation, catch #124).
DO NOT RUN as specced. Any successor probe must include degree-(k'+1)
received words.
