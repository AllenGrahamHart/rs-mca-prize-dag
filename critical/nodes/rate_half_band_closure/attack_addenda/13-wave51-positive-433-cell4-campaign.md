# Wave-51 addendum: the positive 433-1b cell-4 campaign (2026-08-08, coordinator-extracted)

[Coordinator note, CATCH-W51: this content was appended by Codex
in-place to the ARCHIVED attack_sections/12 packet across three
wave-51 commits, breaking the lossless-decomposition sha pin (the
schema's own rule: sections are immutable archives; live updates go
to addenda). Extracted verbatim below; the section is restored to
its archived bytes. Standing rule for the worker: campaign progress
on sectioned nodes goes in attack_addenda/, never in
attack_sections/.]


The subsequent exact campaign has now gone substantially beyond that
instruction.  Product-rank drop is globally excluded for `433-1b -> O0a`;
principal role cells `[0]`, `[1,2]`, `[3,6]`, and `[14]` are closed.  The
remaining common-role orbits are

```text
[4,7], [5,8], [9,10], [11], [12,13].
```

Cell `4` has an exact four-basis common tower over `F_p(r)`: a quadratic in
`t`, a palindromic quadratic in `b`, and linear recovery of `c`.  Its first
three outside slices are now PROVED empty:

```text
xi=0, pairing=0: opposite-DE norm and boundary replay;
xi=1, pairing=0: exchange of the two parallel positive DE copies;
xi=2, pairing=0: equal-DE norm and exhaustive finite lift replay.
```

The new `xi=2` norm has degree `308`, eight target roots, and ten total
target/inverse candidates in each source-sign row.  Five terminate on
`r` guards, two lifted branches on `t` guards, six `(r,t)` branches have no
base-field `b`, and four guarded common points have nonzero direct cut.  This
pays another `16` raw cases and leaves `102` of the `105` cell-4
missing/matching slices.  Test matching permutations `1` and `2` using the
cell-3 missing-sum and parallel-edge transports before launching independent
norm jobs.

That matching test is now complete.  Canonical matchings `0`, `1`, and `2`
are exactly the three perfect matchings whose first pair is residual positions
`(0,1)`.  Consequently the three matching-zero exclusions transport directly
to all three matchings: the opposite-`DE` cut pays `xi=0,1`, and the equal-
`DE` cut pays `xi=2`.  The PROVED
`rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_de_firstpair_complete_exclusion`
closes `3*3*4*4=144` raw cases, or nine of the `105` slices.  The live cell-4
ledger is `96` slices.  Matching `3`, whose first pair is `(0,2)`, is the
first genuinely new pairing; quotient the remaining matching table by
parallel-`DE` exchange and target-lane signs before another norm campaign.

The parallel-`DE` quotient is now exact.  Its matching action is

```text
{0}, {1}, {2}, {3,6}, {4,9}, {5,12}, {7,10}, {8,13}, {11,14}.
```

Missing roles `xi=0,1` form one orbit at each fixed matching index; for
`xi=2,...,6`, the missing role is fixed and the displayed matching action
applies.  Hence the `105` labeled slices form `60` orbits.  The first-pair
theorem pays six quotient orbits, leaving `54` representatives for `96`
live slices.  Compute only pairing representatives `3,4,5,7,8,11`, beginning
with pairing `3`; each result automatically transports to its displayed
partner.  Target lanes remain separate.
