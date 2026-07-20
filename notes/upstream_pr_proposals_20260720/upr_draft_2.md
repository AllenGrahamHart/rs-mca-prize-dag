# PR DRAFT 2 (RANK 2) — Exact self-contained two-sided MCA threshold for the n=2^41 rate-1/2 family, 2^128 < q < 2^167

> Title: **A determined rate-1/2 MCA threshold family below half-distance: a_RH(q) = n − floor(q/2^128) + 1 for 2^128 < q < 2^166.5, self-contained**

Base: `origin/main@9908454995f3f195cfe748f35a1135211609d066`.
Cross-repo reference (SHA-pinned): `github.com/AllenGrahamHart/rs-mca-prize-dag@b8a169acb020f4a8cf990a552daf12b29127337b`,
node `background/nodes/rate_half_quadratic_exact_range/statement.md` (PROVED, wave-10 audited,
`WAVE10_AUDIT_FINDINGS.md`); supporting layers
`background/nodes/rate_half_far_ca_anchor_pencil_normal_form/statement.md`,
`background/nodes/rate_half_half_distance_safe_bracket/statement.md`.

## Scope

For the rate-1/2 family of prize-admissible rows

```text
C = RS[F_q, D, k],   n = |D| = 2^41,   k = 2^40,   rho = 1/2,
q prime,  q = 1 mod 2^41,   2^128 < q < 2^166.502834419,  |F| < 2^256,
D = order-2^41 subgroup of F_q^*,   eps* = 2^-128,
```

the support-wise MCA threshold is **determined exactly and two-sidedly**, with
`B_* = floor(q/2^128)`:

```text
a_RH(q) = n - B_* + 1,
B_mca(a_RH(q))     = B_*  <=  B_*   (safe: quadratic-staircase equality),
B_mca(a_RH(q) - 1) >= B_* + 1       (unsafe: universal MDS coordinate-tangent witness family).
```

Equivalently the closed integer radius crosses at `r = B_* − 1`, i.e. `delta` runs up to (just below)
the half-distance value `1/4` as `q → 2^167`. The determination is **self-contained**: it rests only
on the quadratic-staircase count, the exact anchor-pencil far-CA layer
(`2r < d_min ⇒ per-slope uniqueness`, elementary), and the universal coordinate-tangent unsafe
family. It does **not** use the BCIKS half-distance import.

## Where this sits relative to your roadmap (explicit crosswalk)

| your item | relation |
|---|---|
| §0.2 self-contained safe edge `(1−ρ)/3 = 1/6` | strengthened here to an EXACT two-sided crossing up to `δ→1/4`, self-contained, **for this `n=2^41` family only** |
| §0.2 "with the BCIKS import: `δ ≤ 1/4`" | matched in reach, but as an exact crossing and WITHOUT the import (for `q<2^167`) |
| §3.1 regular-overdetermined regime `δ ≲ (1−ρ)/2 = 1/4` | this family lives exactly in your "controlled proving ground"; it is NOT the near-capacity band |
| §0.4 four adjacent finite targets | **DIFFERENT LANE — does NOT touch them** (see fence) |
| §10 "threshold-pinned rows, not just lower bounds" | this is such a family |

## Verification

- wave-10 audit: all 7 node verifiers PASS; 25/25 independent checks PASS
  (`w10_checks.py`, incl. own-convention exhaustive toy). Node commits `e86b0b88`+`568178b8`;
  far-CA `8997e257`.
- stdlib-only fail-closed re-verifier of the crossing arithmetic for a supplied admissible `q`
  (checks `a_RH = n − floor(q/2^128) + 1`, the staircase equality at `a_RH`, and the tangent
  witness count at `a_RH − 1`).

## Non-claims (fence)

This PR does **not**:

- solve, bound, or bear on your **§0.4 four adjacent targets** — those are `n=2^21` extension-field
  rows (KoalaBear `q≈2^185.9`; Mersenne `q≈2^123.4`, `ε*=2^-100`) at `δ≈0.4678`; our `q<2^167`,
  `n=2^41`, `δ≤1/4` determination provably does not reach them,
- reach the **near-capacity band** or say anything about `B_ap` / the v12 Hankel term,
- cover `q ≥ 2^167`: there only the bracket `a_RH ∈ [k+2^34, 3n/4]` holds, and the upper `3n/4`
  endpoint for `q ≥ 2^169` DOES use the BCIKS import (that piece is not self-contained and is not
  claimed here),
- resolve the residual exact-budget cases `B_* ∈ {2^39, 2^39+1}` at the very top of the range,
- claim any Grand MCA / list / Proximity Prize result; official score unchanged.

## Falsifiability note (your §0.5)

Within this determined family there is no super-polynomial primitive prefix fiber and no
super-polynomial primitive split-pencil family: the far-CA uniqueness (`2r<d_min`) forces at most one
codeword per non-anchor slope, and the bad-slope count is exactly `B_*`. This is offered as a
positive-side calibration of the envelope in the below-half-distance regime, not as a counterexample.
