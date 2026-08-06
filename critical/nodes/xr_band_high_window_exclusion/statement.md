# XR band high-window exclusion (SL-2)

- **status:** CONDITIONAL
- **scope:** the three prize rows, where the band occupancy budget binds
- **consumer:** `xr_graded_tangent_band_charge`
- **board alias:** SL-2, unstructured high-window exclusion

Let `(u,v)` be any globally generic-branch received pair after the
ratified strip order, and use the support-wise first-match selector. For
each band-proper high depth

```text
ceil(h/2) <= d <= h-2,
```

let `N_d` be the number of selected depth-`d` joint-explanation pairs
having at least two selected live slopes, exactly as in items 7-9 of
`notes/BAND_LANE_DEFINITIONS.md`. Then

```text
25 N_d <= 17 n^2.                                           (SL2)
```

The exact remaining premise is now
`xr_band_maximal_window_divisor_count` (SL-2-RES). The proved window
system and maximality filter identify its residual locator set
bijectively with the pairs counted by `N_d`; hence closing SL-2-RES
promotes this node without another mathematical premise.

The constant `17/25=0.68` is deliberately uniform. Together with the
banked low-depth envelope and the stronger cascade cap, the exact
full-band ledger fits the row-specific free budget
`H_band=s_lo-16n^3`. It must not be compared directly with the separate
`0.8008/0.6859/0.6596` single-word window thresholds: those price a
stronger sufficient list-size route, not the selected occupancy asserted
here. The three RowC rows are not claimed here because their occupancy
budgets are vacuous.

The proved `xr_mc_depth_quantization` theorem excludes the canonical
MC/coset construction from every band-proper depth at the official odd
values of `h`. Consequently a falsifier to `(SL2)` must use a
non-coset or finite-characteristic-accidental mechanism. This is a
restriction on known adversaries, not an exhaustive classification of
all supports.

The proved `xr_band_windowed_projection_reduction` gives a sufficient
route through the averaged single-member window counts `W_d(z)`, but
that route is not part of the assertion. Large `W_d(z)` values from
codewords which do not assemble into selected joint pairs do not
refute `(SL2)`.

The round-12 locator coordinates are also a reduction only. Counting
all degree-`n-k-d` divisors in the affine window intersection is the
raw-subset currency and is not equivalent to `N_d`: a deeper maximal
pair contributes `binom(k+e,k+d)` raw divisors. Exact maximality and
selected liveness are load-bearing in SL-2-RES.

## Falsifier

One prize-row, globally generic-branch pair `(u,v)`, one depth in the
displayed range, and an auditable support-wise first-match ledger with
`25N_d>17n^2`. A large raw list, an unselected support family, a
cascade-tier family at `d=h-1`, or a RowC fixture is not a falsifier.

## Addendum (2026-08-06, mint-4 — the W = 5 rollback RATIFIED + the functional status)

1. THE W = 5 ROLLBACK IS RATIFIED (coordinator ruling 2026-08-06
   under user delegation; round-16 a1_window_audit verdict LOSSY):
   the +7 window extension was a +2 overshoot with no derivation;
   W_min = 5 EXACT (the q = 918552577 w6-orbit binding inequality)
   is the window of record. Board effect: 10 leaves / 8 routeless ->
   4 leaves / 1, all closable; consumer arithmetic bit-identical;
   costs are watch-line (margin 2.85x -> 2.30x). The CR-W5-ELL1
   census is DEFERRED until the lane's balance functional is
   re-posed (below), so compute calibrates the functional of record.
2. FUNCTIONAL STATUS (rounds 16-18): the per-weight balance form is
   REFUTED and retired; the global form is unavailable at this
   lane's rows (esg_lane_rescope: rate 1/16 NEVER, low-depth 1/4-1/8
   excluded; the banked q >= 2^209 pin computes the RETIRED
   threshold and must be re-derived). The re-pose candidate of
   record is the TERNARY functional (crossing_dsa_refutation LEMMA
   TC: primitive count 3^L with 2L-orbit correction).
