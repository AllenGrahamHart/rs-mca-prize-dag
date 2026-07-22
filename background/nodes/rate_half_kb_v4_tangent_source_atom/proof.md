# Proof

The exact identity in `rate_half_mca_sparse_layer_reduction` splits received
pairs into a column-far case and a column-close case. It also proves that one
codeword-pair translation in the latter case preserves the complete
support-wise MCA-bad slope set. Choosing the first translating pair in a fixed
public finite order changes neither assertion.

In the column-far case the architecture defines the source-coordinate tangent
image to be empty, so `(KB-T3)` is immediate. In the column-close case, the
chosen pair agrees jointly with the received pair outside a discrepancy
support `Sigma` of cardinality at most `n-a`. After translation, each eligible
coordinate `x` with `e_1(x)!=0` contributes at most one finite slope, namely
`-e_0(x)/e_1(x)`. Mapping coordinates to slopes can merge values but cannot
increase cardinality. Therefore

```text
|Z_paid|<=|T|<=|Sigma|<=n-a=981104.
```

For completeness, write `Z=Z_bad`, let `Q` and `BC` denote the two frozen
predicate sets, and define the chronology literally by

```text
Z_paid = Z intersect T,
R_1    = Z \ Z_paid,
Z_Q    = R_1 intersect Q,
R_2    = R_1 \ Z_Q,
Z_BC   = R_2 intersect BC,
Z_new  = R_2 \ Z_BC.
```

Successive set differences make these four sets pairwise disjoint, and direct
substitution gives their union as `Z`. Taking cardinalities and applying the
first-cell cap proves `(KB-T4)`.

Finally `|F|=p^6`. Exact integer division and subtraction give `(KB-T5)`; the
node verifier replays those operations and the frozen partition digest. QED.
