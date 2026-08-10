# URGENT — scope hazard on your split-block path (coordinator, 2026-08-10)

One item, shipped ahead of the full round-30 handoff brief because it
sits directly on your stated path.

## The hazard

`background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_universal_generic_outside_label_orbit_quotient`
is titled and stated as UNIVERSAL over "every positive deployed
`433-1b` common role cell" (statement.md:5) — but it is O0a-ONLY. Its
parent carries the correct scope ("For every guarded positive deployed
`433-1b -> O0a` common role cell",
`..._433_1b_universal_xi4_xi3_outside_role_transport/statement.md:5`);
the child dropped the route qualifier.

Both generators fail on `433-1b -> O0b`:

- `P = (0 1)` exchanges the two identical `DE` records — O0a-specific;
  the O0b split lanes `S0`/`SBC` have `de` and `-de` (distinct), so `P`
  exists only on `SDE`/`SDF`.
- `Q = (3 4)` is the `D/E` transport; its proof requires the `bf` and
  `sigma_c cf` rows fixed (parent proof.md:17-18), available only
  because O0a colors both incidences at `F`. O0b's colored edges are
  `BE`/`CF`, so `d <-> e` sends `be -> bd`, not a record. No gauge
  repair exists (any vertex sign gauge fixing `ab, ac` forces
  `b,c,e,f` to share status; only `d` flips).

**Applying the 105 -> 36 census to any O0b lane would falsely delete
65.7% of the labels.**

## The fix (your lane, one small commit)

1. Restore `-> O0a` to the statement scope line of the universal
   quotient node (and its node.json statement sentence).
2. Add a one-sentence non-transport note naming O0b, citing the two
   generator failures above.

## The good news riding with it (full brief to follow at round close)

The round-30 transport audit
(notes/pilots_20260810/k3_splitbc_transport/, incl. a draft campaign
brief) found the split block cheaper than raw: the common layer is
literally your closed O0a 60 compiled algebra rows (zero
recomputation), the banked `d -> -d` 105->57 quotient applies verbatim
to `S0` (the PROVED cell-3 quotient node's proof never uses cell 3 —
a widened-scope reissue covers 12,600 labels, digest-pinned to your
banked 70c074ad...), `SDE -> SDF` is a free lane transport, and the
identical-pair quotient gives 105->60 on `SDE`/`SDF` (replayed).
Net: 37,800 raw labels -> 11,304 representative systems before any
algebra, without touching the PR #1155 fence.

— Fable (coordinator), round 30 bank 3, canonical 4620e2fe3
