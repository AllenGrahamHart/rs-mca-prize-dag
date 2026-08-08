# Audit

The initial component test incorrectly reduced identities modulo the entire
cleared consistency numerator. For `F00`, that numerator is `B` times four
already-inverted factors, so ideal membership in the product ideal is too
strong. Direct substitution `b=-Q/P` confirmed both the consistency equation
and coefficient identity exactly.

The final compiler factors consistency first and checks each nonunit
component separately. It uses two complementary reconstruction minors, so
the `c+d=0` locus is not lost. The first all-cell run completed 22 cells and
timed out only on `M01/M02` generic. Those two were rerun unchanged with a
900-second bound and passed in 475.22 and 472.37 seconds. Peak recorded use
over all cells was 1,293,924 KiB.
