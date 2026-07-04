# paid_tan_fn proof

The tangent paid column is the sum of the tangent staircase contribution and
the residual common-code-line charge.

The node `staircase` supplies the explicit staircase formula for tangent
families at agreement index `A`. The node `common_code_line_budget` supplies
the residual MDS payment for slopes that lie on a common code line but are not
already counted by the primary staircase stratum.

Use the first-match ledger convention: a witness is charged to the first
applicable tangent cell, and residual common-line witnesses are then charged
by `common_code_line_budget`. Since both inputs are proved computable
functions of the row and `A`, their first-match sum is a computable function
`Paid_tan(A)`.
