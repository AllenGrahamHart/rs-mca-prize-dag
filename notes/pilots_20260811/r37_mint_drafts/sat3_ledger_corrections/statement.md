# The (SAT3) realizability ledger: three corrections, their stacking, and the first-moment gate

- **status:** **HEURISTIC / RECORD.** Not one instrument here is a mechanism.
- **closure:** a bookkeeping record with an explicit warning attached
- **consumer:** `rate_half_band_crossing_location`

## Why the status is HEURISTIC

The round-36 close is explicit that **counting died as a verdict-carrier
three more times** in this lane (`11m-4` against the dead `+4`; the H1+H2
nullity-1 families against the excess; the `q^-12` moment refuted `3400x` on
constant-norm sets). This node records what the ledger says and how it was
corrected. It does **not** license the conclusion.

## The counting rows (exact, PROVED as arithmetic)

```text
(L2) overdetermination:  (m+2)(4m+1) - 16m = 4m^2-7m+2 = -1, +4, +17, +38
                         at m = 1,2,3,4 -- negative ONLY at m = 1.
```

Both of the source's reductions preserve the deficit exactly
(`m(4m+1) - (8m-2)` gives the same polynomial), and the (BIV-G) deficit
`(7m^2-9m+2) - (3m^2-2m)` is the **same quadratic**.

**DEF-ID, closed as a COINCIDENCE:**

```text
(m+2)(4m+1) + m(3m-2) = (m-1)(7m-2) + 16m = 7m^2 + 7m + 2
```

is an exact identity (verified `m = 1..59`), but the two systems' shapes are
incompatible and — decisively — **the shared quantity governs NEITHER
layer's existence**: `(L2)` is nonempty at `m=2` despite `+4`, and (BIV-G) is
realizable at `m=3` despite `+17`.

## The three independent corrections and their stacking

| correction | side | effect on the m=2 cell |
| --- | --- | --- |
| round-33 ledger (uncorrected) | — | `-1-O` |
| **(ERC2)-forced dim 18** (round 36) | curve side, `5` units | `-1-O -> +4-O` |
| **automorphism quotient** (round 34) | solution-orbit side | `+4..+6` |
| **stacked** (the two are INDEPENDENT) | — | **`~ +8..+10`** |

- The `18` is `23 - 5`: (ERC2) (PROVED) forces `e = m` for (SAT3), so the
  curve must lie on the `18`-dimensional `(L2)` component, not the ambient
  `23`-dimensional space the round-33 ledger used.
- The automorphism group acts freely with finite stabilisers (a
  positive-dimensional stabiliser would fix `9` slopes and `32` points):
  orbit dimension `>= 4` (`AGL_1 x AGL_1`), `>= 6` generically
  (`PGL_2 x PGL_2`). Round 34's corrected excess alone was `+3..+5`.
- **Consequence:** the round-33 conjecture "realizable iff `m <= 2`" is
  **doubly re-posed to `m <= 1`**, consistent with the round-34 TCAP re-pose.

**Controls preserved:** `m = 1` stays `-9..-7`; the `e=1` ladder stays
`-8m-1 < 0` for every `m`; an independent locator-layer bookkeeping agrees in
VERDICT (`-5` at `m=2`, `+7` at `m=1`).

**SIGN-CONVENTION FLAG (found here):** the locator-layer row uses the
**opposite sign convention** to the TCAP row (`+3..+5` at `m=2` and `-9..-7`
at `m=1` versus `-5` at `m=2` and `+7` at `m=1`). "Agree in verdict" is true
only after flipping. **The two rows must never be added.**

## The C(16m, 4m-1) first-moment gate

The multiplicative domain enters only through `C(16m, 4m-1)`, the
`q`-INDEPENDENT count of degree-`rho` squarefree divisors of `x^N - 1`,
against ambient `q^rho`:

```text
C(16,3) = 560,  C(32,7) = 3365856,  C(48,11) = 22595200368,
C(64,15) = 159518999862720.
```

**The m=1 double calibration (the lane's only calibrated instrument):**

- at `q = 17`, `log2 E = +13.75` where **EXACTLY 16 configurations exist and
  they ARE the 16 realized (SAT3) families** — two independent
  constructions. Since `16 = 2^4`, the gate **overestimates by `2^9.75`**
  (`~2^9.8` as banked), which is the SAFE direction;
- at `q = 97`, `log2 E = -0.94`, where none are realized.

It is NEGATIVE for every `m >= 2` at every field (`~ -1952 m^2` bits at
official scale; sharpened to `-61.3` bits at `q=97` by the dim-18 input).
**A negative first moment proves nothing.**

## MISSING CONSTANT (blocking — see DISCREPANCY)

**The gate's EXPRESSION is never printed** — only its calibrated values. They
are not mutually reconstructible: a pure power law through the two `m=1`
points needs exponent `5.85`, and `-0.94 - 2 log2 97 = -14.1`, not `-61.3`.
**The formula must be recovered from the pilot before this gate is ever
re-priced.** This package therefore verifies the binomial counts and the
`16 = 16` calibration arithmetic, and refuses to recompute the bits.

## The four emptiness instruments (all counting, no mechanism)

`(1)` round-34's fields-searched negative; `(2)` TCAP + the automorphism
quotient; `(3)` the `C(16m,4m-1)` gate; `(4)` the flipped ledger. **Still no
mechanism** — and the pilot's own positive half shows why counting stays
untrustworthy: `T = 3` over `mu_32` sits at `+62.5` bits **`q`-independently**
(the `18-6T` exponent vanishes at `T = 3`), yet no exact solve reaches it.

## Scope

- The `pb_design_ceiling` blind spot is live; round-34 bank 4's own MISS 2
  (a degenerate `1.4%`-rate family briefly misread as refuting the naive
  count) is an instance inside the same report.
- `-1952 m^2` and `-61.3` are **carried, not recomputed** here.
- **ZERO POWER:** nothing in this node bears on existence.

## Source

- `critical/nodes/rate_half_band_crossing_location/statement.md:3428-3439`
  (round 34 bank 4: the automorphism quotient, TCAP-DIM re-posed).
- ibid. :4380-4396 (round 36 bank 2: (ERC2)-forced dim 18, the stacking, the
  double re-pose, the four instruments, the `+62.5`-bit `T=3` cell).
- ibid. :3846-3860 (round 35 bank 4: the gate and its `m=1` double
  calibration).
- ibid. :3403-3407 (the (L2) overdetermination row);
  `notes/pilots_20260811/r35_l2_gate/d1_results.txt:34-44`.
- DEF-ID posed and closed: ibid. :3497-3505 and :3588-3595.

## Replay

```text
tools/ramguard tiny -- python3 \
  notes/pilots_20260811/r37_mint_drafts/sat3_ledger_corrections/verify.py
```
