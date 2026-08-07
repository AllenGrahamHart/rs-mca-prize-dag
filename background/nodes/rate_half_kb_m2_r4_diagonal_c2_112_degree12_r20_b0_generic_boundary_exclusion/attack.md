# Attack

This closes the `B0`, `K10!=0` side of the R20 degree-12 split. Do not spend
more compute on base-field `s` samples or on unspecialized Frobenius powers:
the block-order certificate is uniform and geometric.

The remaining R20 degree-12 task is the complementary leading-drop branch
`K10=0`. It should be intersected with the selected degree-12 factor and the
two pseudo-remainder cores before choosing a chart. A direct reuse of the
`B0` quotient is invalid because its pseudo-division inverted `K10`.
