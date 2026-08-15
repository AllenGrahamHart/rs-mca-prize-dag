# Audit

1. The balanced offset is paid by a line-count bound, not silently absorbed
   into the zero-offset cross charge.
2. `M=floor(P^2/4)` is a lower bound for both parities; odd `P` has harmless
   positive slack.
3. Clean lines have `d>=1` because every owner weight is at most `P-1`.
4. The same global light mass may be reused for different heavy owners; the
   proof prices that honestly through the factor `H` and the separate `hrP`
   term.
5. Collision lines are counted by heavy-owner pairs, and duplicate affine
   lines are excluded by hypothesis.
6. Small affine-plane enumeration retains every rich line and adversarially
   maximizes its selected partition.
