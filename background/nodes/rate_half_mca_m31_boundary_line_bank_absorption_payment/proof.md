# Proof

For `h<=h0`, use the independently truncated full-lift
Johnson/mean-centered prefix.

Fix an exact layer `h0<h<=U` and one anchor.  Every assigned explanation in
the layer owns at most one slope because `2h>e`.  Relative to the anchor,
each nonzero normalized codeword direction agrees with the gauged direction
on at least `A_h=2h-e` inside coordinates.  Distinct directions have
agreement blocks meeting in at most `c`.  The constant-block Johnson count
therefore permits at most `J_h` direction classes.

Each direction class together with the anchor lies on one affine codeword
line.  If the actual number of classes is `j<=J_h`, append `J_h-j` empty
slots of line-size one.  The layer identity is then

```text
|D_h| = 1-J_h + sum_(r=1)^J_h |L_(h,r)|.
```

The top union exists only when `H<m`; the cross-layer synchronization
theorem puts it on one further affine line.  Summing the prefix, all exact
layers, and that optional top line proves `(LB1)`.  No outside-core
denominator is used here.

If the family is unsafe, `(LB1)` and pigeonhole give `(LB2)`.  Since
`lambda_e>=2`, the selected slot is an actual affine explanation line with
two anchors.  Total-core line packing forces

```text
g_e=ceil((lambda_e*m-N)/(lambda_e-1)).
```

Its nonzero degree-`<K` direction has at most `c` zeros outside the gauged
direction support, so at least `u_e=g_e-c` common-core coordinates lie
inside that support.  Every assigned explanation of deficit

```text
h>=a_e=e-u_e+K
```

shares at least `K` of those coordinates with two line anchors.
Restriction injectivity puts it at its actual slope on the same line.

All remaining explanations have outside agreement at least `m-a_e+1`.
The punctured ordinary-Johnson cap `M_e` counts them; each owns at most `e`
slopes.  Hence

```text
|Z| <= e*M_e + (N-m+1).                            (LB3)
```

The source-bound endpoint verifier reconstructs `(LB1)`--`(LB3)`.  The
constant-memory C replay checks every support from `101157` through the
adjacent wall `124806`, all guards, and the exact branch census.
