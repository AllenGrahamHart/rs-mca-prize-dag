# Proof

The global product-base theorem proves `rank B=6` in every matching cell.
Only the loop sum row among the six base rows has nonzero entries in the
last two `B_1` columns.  Projection of `rowspan(B)` to those columns is
therefore the line spanned by
`(lambda_0,lambda_0^2)`.

If a nonloop row `Q_i` belonged to `rowspan(B)`, its last-two-column vector
would lie on that line.  The determinant of the two vectors is exactly
`(KBPCU-2)`.  Every source quotient label is nonzero and the common labels
are pairwise distinct, so the determinant cannot vanish.  Thus no `Q_i`
belongs to `rowspan(B)`, and every quotient image `q_i` is nonzero.

The zero-image branch is therefore empty.  If the full common matrix has
rank at most seven, adjoining any one `Q_i` to `B` gives rank seven, so the
full matrix has rank exactly seven.  An `8`-column rank-seven matrix has a
one-dimensional kernel.  Finally, the pivot-chart theorem says that a
rank-one span of four nonzero quotient images satisfies every incident
three-minor chart, proving the remaining claims. QED.
