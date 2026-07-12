# PARTIAL PROOF PACKET: the row-uniform quotient-row ledger (census gate residual, catch #106)

- **status:** PARTIAL (three proved windows + exact coverage table + named missing lemma)
- **consumer:** `petal_small_scale_staircase_census` (via `intrinsic_scale_geometric_ledger`)
- **worker:** fresh-context proof worker, 2026-07-12/13; read-only on repos
- **verifier:** `qrl_verify.py` (ALL CHECKS PASS; mutations M1/M2 correctly rejected;
  0.6 s, 13.5 MB RSS, max 83,521 enumerated states — inside the RAM law)

## The minted claim (verbatim scope; NOT strengthened)

For every dyadic quotient row `RS[F, H^M, k/M]` arising from an official row
(`n = 2^s`, `13 <= s <= 41`, `k = rho n`, `rho in {1/2, 1/4, 1/8, 1/16}`;
`M` dyadic with `2 <= M <= t`, `t = (n-k)/(sigma+1)`, `sigma = 1`; quotient row
`n' = n/M` points, `k' = k/M`, SAME field, `q >= n^2 = (M n')^2`), the APERIODIC
(`c(S') = 1`) part of the exact-agreement list at descended agreement `A/M` is
`<= C (n/M)^6` with `C <= 63/64`, uniformly over received words and over ALL
such (row, M) pairs.

## What is actually counted (reconciliation of the crux — resolved)

Per the descent chain (`cyclic_fiber_interleaving_descent` +
`exact_support_interleaving_projection`), the object is `L_P`: for a received
word on the quotient row, the number of codewords (`deg < k'`) whose EXACT
agreement support has size exactly `a = A/M` and is aperiodic in `Z_{n'}`.

**The feared interpolation-degenerate cell `a = k'` does not exist.** At
official rows `M | k` (both dyadic, `M <= k`), the scale-`M` supports satisfy
`M | A`, and contributors satisfy `A >= k + sigma = k+1`; divisibility forces
`A >= k + M`, hence `a >= k' + 1 > k'` at every consumed cell (verified for all
2900 official (row, M) pairs, S2). Consequently each support of size `a`
carries at most ONE codeword (interpolation on `>= k'` points), so the list is
support-faithful — the count of codewords equals the count of exact supports.
Two corollaries banked by the same arithmetic: the EDGE band `A = k+sigma` is
EMPTY for every `M >= 2` (k even makes `k+1` odd), and the OWN-scale band
(P1-own reading) is the single cell `A = k + M`, i.e. `a = k' + 1`.

## Proved windows (proofs in qrl_proof.md)

- **T1 (support-count window).** For `n' <= 32`: EVERY cell, both the
  single-word claim and the ESP-free class-level ledger bound, unconditionally:
  `L_P <= C(n', a) <= C(32,16) = 601,080,390 <= (63/64) 32^6 = 1,056,964,608`.
  At any `n'`: cells with `a <= 6` or `a >= n' - 6` (`C(n',a) <= n'^6/720`).
  Field-free; also covers the `M ∤ k` scales at class level.
- **T2 (Johnson window).** Cells with `a^2 > (k'-1) n'` (equivalently
  `A^2 > (k-M) n`): `L_P <= floor(n'(a-k'+1)/(a^2-(k'-1)n')) <= n'^2`
  (`petal_k4_johnson_slice` / Paper D `thm:capf-johnson-list(ii)` at quotient
  parameters — generic in the evaluation set, quotient rows qualify), and the
  class-level transport through descent + ESP closes with total `<= 2 n'^2
  <= (63/64) n'^6` (ESP inflation `< 4n'/(3n'-2) <= 2` at `q >= 4 n'^2`).
- **T3 (large-scale one-fiber lemma; new, 3 lines).** For every dyadic
  `M >= k` (including the `M ∤ k` scales `M in {2k, 4k}` at `rho in {1/8,1/16}`
  where the minted claim does not parse): the scale-`M` class has at most
  `n/M` members — a scale-`M` support contains a full `M`-fiber, and a fiber
  (`M >= k` points) pins the codeword; so at most one codeword per fiber.

## Open window (the honest residual)

For `n' >= 64` (scales `M = 2^j`, `j <= s-6` — present at EVERY official row),
the cells `a in [max(k'+1, 7), min(n'-7, isqrt((k'-1) n'))]` are NOT covered by
any tool in the audited kit; this band is nonempty at every such (s, rho, M)
(S3). Under the P1-own reading it is the single cell `a = k'+1` (open iff
`k' >= 8`; the one exception `(rho=1/16, n'=64)` has `a = 5 <= 6`, covered).

**MISSING LEMMA (named):** ROW-LEVEL APERIODIC SUB-JOHNSON QUOTIENT BOUND —
for dyadic rows `(n' = 2^{s'} >= 64, k' = rho n')` with `q >= (M n')^2`,
`q ≡ 1 (mod M n')`, and every received word, the number of `deg < k'`
codewords with aperiodic exact agreement support of size `a`, for
`7 <= a <= sqrt((k'-1) n')`, is at most `(63/64) n'^6`. This is exactly the
sub-Johnson kernel of `petal_k4_primitive_bound` (K4, itself TARGET) in
row-level form at official-shaped rows with oversized fields; no banked node
supplies it, matching catch #106's assessment.

## Consistency vs the banked ground truth

All 514 profile cells of the 372 banked census records satisfy the packet's
bounds (multiplicity 1, `M | A`, `M <= t`, `A >= k+1`, `A >= k+M` where
`M | k`, `classes <= C(n', a)` and `<= (63/64) n'^6`); the tightest cell is
(8,3,17) edge `(2,4)`: 4 classes vs support bound 6 (ratio 0.667). Fresh
in-vivo replay at the 42 rate-half words: descended aperiodic exact lists
obey the claim at all 240 (word, component, a) cells; class -> S/K injection
and the descent inequality verified; descent EXACT at 4/7 banked cells
(matching the dag's "EXACT at the four banked rate-half cells").

## Catches

#109 (ESP transport insufficiency at the minimal official field),
#110 (deep-regime window verified but non-consumable and nearly subsumed),
#111 (M ∤ k scales unpriced by the minted claim; closed here by T1/T3).
Details in `qrl_catches.md`.
