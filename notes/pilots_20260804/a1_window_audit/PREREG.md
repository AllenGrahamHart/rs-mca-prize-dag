# A1 — PRE-REGISTRATION (written BEFORE the derivation reconstruction)

**Pilot:** A1, C1'-r3 window-extension audit (+5 -> +7, 2026-07-21).
**Author:** Opus audit pilot, round 15, 2026-08-06.
**Rule:** everything below is committed before I open the r3 derivation
files. Scored honestly at the end of REPORT.md whether right or wrong.

## What I already knew when writing this (state at prereg time)

Read only: `c1_sharpest_leaf/FABLE_AUDIT.md`, `BRIEF1_PRO_DOSSIER.md`,
`BRIEF1_DOSSIER_AUDIT.md`, and the *names* of the ten slot node dirs.
From those, three facts are already fixed:

1. The window is `[L+1, L+7]` in the C1-ZERO/SWIF-4 statement
   (BRIEF1_PRO_DOSSIER.md:31-32).
2. Newton short-window exclusion covers the whole window iff `L+7 <= 2L`
   iff `L >= 7` (BRIEF1_DOSSIER_AUDIT.md:22-23), so only schedule levels
   `L in {1,2,4}` survive.
3. Slot dirs present: (1,5) (1,6) (1,7) (1,8) (2,7) (2,8) (2,9)
   (4,9) (4,10) (4,11).

Derived (arithmetic, not yet checked against the notes): at `W = 5` the
windows are L=1:[2,6], L=2:[3,7], L=4:[5,9], whose TARGET residues are
exactly {(1,5),(1,6),(2,7),(4,9)} — the stated four-slot residual. The
six added slots are therefore exactly
**{(1,7),(1,8),(2,8),(2,9),(4,10),(4,11)}**, i.e. the two top weights of
each level. NOTE: `W >= 5` and `W >= 7` both leave the SAME level set
{1,2,4} unresolved (Newton needs `L >= W`), so the extension bought
nothing at the level granularity — only at the weight granularity.

## PREDICTION (committed)

**Verdict I expect: LOSSY, partial — minimal `W = 6`, not 5 and not 7.**

Confidence: verdict class LOSSY-or-CONDITIONAL 0.7; the specific
`W_min = 6` 0.35; full rollback to `W = 5` 0.25; TIGHT 0.2.

Reasoning I am committing to (so it can be scored):

- P1. I expect the `7` to come from a **pigeonhole/Minkowski-style
  doubling step**: Boolean vectors of weight <= t collide mod an ideal of
  norm `q^L`, and the difference is a signed vector of weight <= 2t. Any
  such step carries a factor-2 and a ceiling, and both are classic
  overshoot sites. If instead the 7 comes from a *summed tail* bound
  (sum over w > L+W of the per-slot contribution), I expect the sum to be
  geometric and hence dominated by its first term, which is exactly the
  situation where a crude "take two more weights for safety" step gets
  written.
- P2. I predict the binding constant is a **worst-case additive slack of
  +2 over the honest requirement**, and that at least ONE of the two
  extra units is recoverable from the newer banked results (norm-gate
  energy ceiling `1 <= Norm <= E^{h/2}`, official support forcing, or the
  LAT1 minima law), but not both — hence `W = 6`.
- P3. Consumer side: I predict the zone budget does **not** bind the
  window at all. Per-slot contribution `512*ell/2^w` gives, for the ten
  slots, 16, 8, 4, 2 / 8, 4, 2 / 4, 2, 1 — every single one exceeds the
  `1/32` budget (the smallest, `(4,11) = 1`, by 32x; `(1,8)/(2,9)/(4,10)
  = 2` by 64x, matching the audit's "32-64x" phrasing). So the budget
  gives NO tail truncation: it demands emptiness of every slot inside
  whatever window the theorem asserts. **The window width is set purely
  by the SUPPLY side (what the existence theorem can prove), never by
  the DEMAND side.** Corollary I commit to: minimal `W` is whatever the
  existence proof needs; the zone arithmetic cannot rescue a rollback,
  it can only fail to obstruct one.
- P4. A2 (`W_ext = 0` overkill): I predict the gap is quantified by the
  consumer's allowance ladder, `E_j <= 41/8` per level with the assembly
  tolerating allowance 6 and failing at 7 while C1 uses 4
  (BRIEF1_PRO_DOSSIER.md:76-77). Predicted gap: **2 allowance units**,
  i.e. the ten-slot route buys `W_ext = 0` where `W_ext <= 1/32` would
  do, and the slack in the final product is a factor I predict to be
  `(1+1/32)^34 ~= 2.9`, comfortably inside the 6-vs-7 fence.

## Falsifiers for my own prediction

- If the derivation's `7` is forced by an inequality whose constants are
  all already-sharp banked theorems (no rounding, no worst case), the
  verdict is TIGHT and P1/P2 are refuted.
- If the zone budget DOES admit a tail truncation (i.e. some slot's
  contribution is below `1/32`), P3 is refuted outright.
- If the six added slots are NOT the top-two-weights-per-level set above,
  my whole reconstruction of the geometry is wrong and I say so.

## Discipline

Derivation audit only. No node edits. No compute beyond exact rational
arithmetic under `tools/ramguard tiny`. Subtraction: every claim checked
against banked notes before being called new.
