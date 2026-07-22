# Audit

The owned subset size is exactly `c=K-t`. Two residuals may intersect in
`c-1` points, so using `(c-1)`-subsets would double count. The mutation audit
contains a sharp pair with intersection `c-1`.

The denominator `binom(H+c-1,c)` is load-bearing. The residual weight is
`a-t=H+c-1`, not `H+c` and not `h+c-1`.

The energy proof uses the fact that all selected widths together contain at
most `M(M-1)` ordered support pairs. It does not multiply that quantity by
the number of widths. Conversely, a fiber-size bound does not count the
number of oriented differences or prove P-B by itself.

The official prefixes use the strict counterexample hypothesis `M>8n^3`.
At equality the last strict inequality in `(NK6)` is unavailable. The next
codimension on every row exceeds `8n`, so the table does not silently claim
more than this exact payment proves.
