# Audit - PMA sigma-one first-layout domination

## Load-bearing semantic check

The word **carried** must retain the universal meaning proved by the
core-defect reduction: once a layout represents `U`, every listed codeword
which is not one of that layout's planted anchors is a non-planted extra in
the layout. If carriage were an arbitrary sparse relation selected separately
for each codeword, `(FL1)` would be false and the existing first-carried
Top/Post theorem would need a different source definition.

## Checked points

1. The theorem does not count paired cores. It fixes the first paired core and
   uses its complete anchor set as the only possible later first-match mass.
2. A codeword planted in `C_1` may become a non-planted extra in a later
   layout. All such cases are safely covered by the single `M` term.
3. No two-anchor uniqueness is needed for `(FL1)`. First-match disjointness and
   `|Anch(C_1)|=M` are sufficient.
4. The local payments may overcount Top members, periodic members, and later
   globally owned members. Applying them to `E_C1` by subset remains safe.
5. The theorem does not claim that the first layout has few residual extras.
   It removes only the chart multiplier.
6. The official arithmetic uses the exact payment formulas and checks the
   stronger combined line `(FL3)` at all 128 rows.

## Mutation boundary

The verifier includes a sparse-carriage mutant in which a codeword not
planted in the first layout is artificially withheld until a later layout.
That mutant violates `(FL1)`, confirming that universal carriage is a genuine
hypothesis rather than set-theoretic decoration.
