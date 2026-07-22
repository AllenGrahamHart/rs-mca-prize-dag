# Audit - L1 general first-layout domination

## Checked axes

1. The layout represents the same received word as the listed codewords.
2. Subtracting the base polynomial preserves the degree-below-`k` condition.
3. Background carriage uses `U=Q` on the layout background; an arbitrary
   leftover word is not silently treated as zero.
4. Distinct nonzero petal labels make the planted anchors exact and distinct.
5. Universal carriage means every listed non-anchor, not a sparse relation
   chosen separately for each contributor.
6. The theorem counts all selected first-layout non-planted profiles as an
   upper bound; a word changing from mixed to full under re-layout causes no
   gap.
7. Global owners may be removed first because taking a subset preserves
   `(GL4)`.
8. The `M` remainder is additive, not multiplied by the number of layouts.
9. Internal quotient/rechart multiplicity is explicitly retained.

## Route effect

The L1 critical path no longer needs a census or transport theorem over
maximal source layouts. It still needs a payment for the non-planted residual
inside one fixed first source, including any contributor-dependent internal
recharts used to obtain quotient structure.
