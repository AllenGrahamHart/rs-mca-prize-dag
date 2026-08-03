# xr_graded_tangent_band_charge

- **status:** CONDITIONAL
- **ratification:** Route T + cascade-tier fold-in, user-ratified
  2026-08-02 (CAMPAIGN_LEDGER RATIFICATION block). Resurrects the mission
  of the archived `archive/retraction_xr_20260705/xr_partial_tangent_band`
  as a THIRD GENERIC COLUMN, never as a B_tan enlargement.
- **consumer:** `xr_smallcore_spread_count` (route of record).

## Current closure interface (2026-08-03)

The rounds 7-11 reconciliation replaces the monolithic occupancy red by
one exact leaf:

```text
xr_band_high_window_exclusion (SL-2)
  25 N_d <= 17 n^2 at every prize-row depth
  ceil(h/2) <= d <= h-2.
```

The projective multiplicity identity, high-depth projection
injectivity, and averaged window inequality are now isolated and proved
in `xr_band_windowed_projection_reduction`. The canonical MC/coset
adversary is excluded from the same depth window by the already proved
`xr_mc_depth_quantization`. The RowC occupancy budgets are vacuous. On
the prize rows the banked low-depth estimate already lies below the
same `17n^2/25` envelope, and the cascade tier has the stronger cap
`N_{h-1}<=n/2`. Therefore this node is conditional on SL-2 alone;
proving that leaf promotes this node without another mathematical
premise.

The historical reduction narrative below is retained for provenance.
Where it describes the iterated-core charge route as current, the
current closure interface above and consolidation Updates 5-6
supersede it.

## Statement (the obligation)

At each of the six clean-rate candidates define the exact free
third-column budget

```text
H_band(C) := s_lo(C) - 16 n^3,
```

where `s_lo=B*_C-B_quot_ub-(n-A+1)` is the banked post-strip allowance.
For every globally generic-branch received pair `(u,v)`, the band-column
slope count satisfies

```text
|Gamma_band| = #{ post-strip live slopes whose selected agreement support
                  shares a core of size in [k+1, A-1] with another live
                  member }                                <=  H_band(C).
```

This is the ratified third generic column. The phrase "the `13n^3`
headroom" in the campaign records is a floored description:
`H_band(C)>=13n^3`, while at the prize rows
`H_band(C)/n^3` is about `13.857`. The consumer uses the exact identity
`16n^3+H_band(C)=s_lo(C)`, not an asserted upper bound of `13n^3`.
`B_tan` remains untouched at `n-A+1`, and the `8n^3 + 8n^3` generic
reserves never split; the AZC discharge margin is 0.5005%. Depth grading
`d = core - k in [1, h-1]`; the depth-`h-1` CASCADE TIER is a NAMED tier
of this column (fold-in ratified), so the cascade forcing
(`xr_pencil_cascade`, scope-corrected) stays citable as structure while
its charge lives here.

## Reduction of record (banked pilot evidence, coordinator-verified)

`|Gamma_band| <= Sum_{d=1}^{h-1} Sum_{depth-d pairs P} L_P`, with the ledger
TIGHT at the cascade tier (k-packing exclusivity: the Lambda_P are
disjoint) and `L_P <= floor((n-J)/(A-J))` at joint agreement `J`. Under
the BAND OCCUPANCY LEMMA — `N_d <= 17n^2/25` at every band depth — the
proper-band column plus the separately capped cascade tier fits the
row-exact `H_band(C)` at all prize rows. The occupancy lemma is the
SINGLE open input. Its sharpened
form (SHARP-OCC, conjectured): `N_d <= floor((n-k+1)/(h-d))` at
`d <= (h-1)/2` and `<= floor((2(n-k)-1)/(2h-2))` above — in particular
`N_d <= n/2`; sharpest calibration on record: RowC 1/4, U-mechanism
`N_1 = 510` vs `n/2 = 512` (margin 2).

*(2026-08-03, audited round-7 refinements: a strictly weaker sufficient
hypothesis for the occupancy heart is PROVED available — the iterated
`(3, k+1)`-core form, item 12' of `notes/BAND_LANE_DEFINITIONS.md`;
only core rays of escape 0 or 1 can defeat per-ray charge 2. Same day,
the collapse pilot SETTLED the escape-0 channel at `V = 4` positively
(charge >= 2 proved, Prop 6) while refuting the zero-escape collapse
and `V <= m/2` as general statements — the heart's remaining open
channels are exactly V >= 5 zero-escape below the Corollary-3b
threshold, and escape-1. The reduction of record above is unchanged;
the re-pose was RATIFIED and APPLIED 2026-08-03 — the heart section
below is the form of record. LATER SAME DAY: channel (i) DECIDED —
charge >= 2 iff 2V <= 3h for the block class of record; at the prize
rows it holds by ~1e8 on a proved floor, so channel (i) is CLOSED at
the prize rows; the RowC toy rows provably fail the channel (the
arithmetic route is dead there); the sole remaining open channel is
escape-1. Definitions addendum 4; support-4 addendum 3. CHANNEL (ii)
RESOLVED same day (escape-1 pilot, 113/113): escape-1 core rays exist
gate-clean, but one alone never defeats charge 2 (the 3-DROP FLOOR); a
defeat needs n_1 >= 3h-2; every constructed counterexample is
band-INADMISSIBLE (LEMMA R: rank <= 2m-1 necessary for exact-A
liveness). CROSS-CHANNEL CATCH accepted: the zero-escape pencil family
at V = 11 passes the FULL gate and realises with charge 0.818 — the
per-ray-charge-2 route is FALSE as a universal for admissible systems;
it survives at PRIZE-ROW parameters (every known defeat class needs
2V > 3h or n_1 >= 3h-2, both false there by ~1e8). The occupancy
lemma's CONCLUSION and the column bound are untouched (the fixture's
own ledger: N_d = 0.11 n^2 << 0.68 n^2). Heart status of record: route
through ADMISSIBILITY + ROW ARITHMETIC; open = consolidating the
general-V admissible case at prize rows under the four new floors.
Definitions addendum 5.)*

Cost side PROVED (two-slope cost theorem): condition rank exactly `2h`
per generic pair (a FAMILY-RANK statement — per-ray accounting is the
accounting of record; the per-datum reading mispredicts the sunflower by
exactly 2x); sunflower cost exactly `h` (the unique known deficit
family, extremal, `d <= (h-1)/2` only); connectivity floor
`rank >= m = |union S| - k` (so `V <= m/2` implies occupancy);
MC quantized out of the band (depth profile supported on `{0, h-1}`);
standing calibration adversaries: K_V, MC, U-mechanism (deficit 1/ray).

## The heart (open; RE-POSED 2026-08-03 in the iterated-core form, ratified)

Form of record (item 12' of `notes/BAND_LANE_DEFINITIONS.md`): the
implication **"every ray of the `(3, k+1)`-core escapes `>= 2` points
relative to `W_infinity`" `=>` per-ray charge `>= 2`** is PROVED
(Corollary U5, round-7 unification); what remains OPEN is that
admissible band systems satisfy the hypothesis. The only channels that
can defeat it are exactly: (i) `V >= 5` zero-escape systems below the
Corollary-3b threshold `(V-3)t + |A_0| <= k-1` — pre-registered
falsifier: such a system with `rank < 2V`; and (ii) escape-1 core rays
(gate-clean realizability OPEN, unification flag 5). SETTLED: the
escape-0 channel at `V = 4` (charge `>= 2` unconditional, Prop 6 of
the collapse pilot). STRUCK (2026-08-03, refuted as general
statements): the former sub-items "zero-escape collapse
(`rank = 2m`)" and "`V <= m/2` for non-collapsing systems" — see
Addendum 2 of `background/nodes/xr_support4_structure/statement.md`;
the measured fixtures' collapses survive as THEOREMS (MDS-chain /
triple-cover criteria), and the old one-step escape form survives as a
sufficient special case of the form of record.

## Falsifier

A globally generic received pair at a scaled row with `|Gamma_band| >
H_band(C)`; or a band depth `d` with `N_d` super-quadratic; or an admissible
non-collapsing ray system with `V > m/2` (which would refute the heart's
route, not yet the column bound).

## NOT claimed

The occupancy lemma (open input); any charge through B_tan; any splitting
of the `8n^3` reserves; MC band population (proved zero); band pairs
being removable by the strip rungs (they are not — that overclaim is
corrected in `xr_strip_classification_rungs` and the bridge).
