# Proof

The endpoint replay isolates two section-base points for each source-sign
row.  Evaluating all eight coordinates of the stored global polynomial
kernel section gives zero at each point, so substituting that section cannot
justify any missing-row equation.

Instead reconstruct the ten common rows directly from the five cell-9 roots,
products, and Vieta sums.  Exact Gaussian elimination over
`F_2130706433` gives rank seven at all eight points.  Choosing the unique
free column in reduced row-echelon form produces a nonzero kernel vector;
direct dot products with all ten rows vanish.

For this pointwise kernel evaluate `A`, `B`, and `beta` at `x=-t^2`.
In all eight cases `A(x)` is nonzero.  The product row equation
`-m A(x)+B(x)=0` and sum row equation `q A(x)+x beta(x)=0`, together with
`q^2=xS`, therefore give the two displayed values.  The values are source
data and agree across all four target-sign copies. QED.
