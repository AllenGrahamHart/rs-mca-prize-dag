# Audit

1. The quotient labels are regenerated from the pinned norm-one element;
   no downloaded label table is trusted.
2. Exact order, duplicate-freeness, active-root folding, and both punctures
   are checked before the witness supports are built.
3. All sixteen `T_64` blocks are checked directly and have size `64`.
4. Every support is checked as a distinct `479`-subset of `Q'`.
5. Locator multiplication checks the printed depth-32 target and the stronger
   first-63 equality; the proof does not infer equality from a hash.
6. Deficiency is the one-sided distance `|A\B_i|=64`, not symmetric
   difference `128`.
7. The rooted degree lower bound counts the six neighbors and not the anchor.
8. The exact binomial comparison is over integers; no logarithmic or
   floating-point estimate is used.
9. Intercept six is a recalibrated floor only. The actual rooted degree may
   exceed the six exhibited neighbors.
10. The support-level object is not silently promoted to a received-word,
    first-owner, or slope-count statement.
