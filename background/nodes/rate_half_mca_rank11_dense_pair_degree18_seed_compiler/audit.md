# Audit

## Semantic checks

1. The dense pair is forced from actual low-margin records, not abstract
   pair weights: the exact pigeonhole lower bound is `220` slopes.
2. The eighteen records are selected before cancellation and have distinct
   slopes on one parameterized pair line.
3. The component basis is re-anchored at the dense pair. At most ten other
   heavy pairs are needed, and the `18+14` schedule leaves at most six of
   their cores singly represented.
4. A singly represented pair costs its actual support exception set, at
   most `387` points. No disjointness between different pairs is assumed.
5. The off-line record is certified using two records owned by a distinct
   heavy pair; equality at two slopes would identify the pair components.
6. After cancellation, equality to the dense affine line is equivalent to
   the original polynomial identity. Puncturing cannot erase the off-line
   witness because all compared differences already vanish on `C`.
7. The degree pin is a root-count argument in the slope variable and is
   independent of the punctured evaluation-domain geometry.

## Executable controls

The primary verifier recomputes all deployed counts, checks every
`1<=t<=10` selection schedule, and evaluates a degree-18 finite-field
interpolation fixture pinned by eighteen affine values. The independent
audit uses a separate finite-difference degree calculation and mutation
controls.
