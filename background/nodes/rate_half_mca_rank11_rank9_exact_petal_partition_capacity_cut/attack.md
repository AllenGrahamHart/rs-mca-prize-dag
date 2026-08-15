# Attack surface

1. Search for a partition with `s_p<=a` and total at most `981105+a` whose
   convex charge exceeds the full-petals-plus-remainder formula.
2. Check every `a` at the largest row, especially quotient transitions
   `70078/70079`, `75469/75470`, and `81758/81759`.
3. Recompute the adjacent demand/cap cross-products without decimal
   rounding.
4. Try to make the final factor `H(K')` decrease at or after `15529`.
5. Reject any argument that silently replaces a residual core by an
   original-row core or divides by a zero petal size.
