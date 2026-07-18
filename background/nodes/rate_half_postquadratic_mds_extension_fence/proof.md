# Proof

For a linear code with parity-check matrix `H`, a word is within one error of
the code exactly when its syndrome lies in the span of one column of `H`.
Likewise a received pair is within one column error of `C^2` exactly when both
syndromes lie in the span of the same parity-check column.

The dual of the displayed Reed-Solomon code has parity columns equal to
nonzero scalar multiples of `(1,x)` for `x` in the evaluation domain, so the
one-error syndrome directions are precisely `h_0,h_1,h_2,h_3`.

Neither `y_0=(0,1)` nor `y_1=(1,4)` has one of those projective directions.
In particular no one-column span contains both, and any pair lifting these
syndromes is column-far at radius one. The syndrome map is surjective, so such
a received pair exists.

The four identities `(PF2)` show that the combined syndrome at each nonzero
finite slope lies in a one-column span. Hence all four slopes are close at
radius one. Since the pair is column-far, each close slope is CA-bad and
therefore MCA-bad. This proves `(PF3)`. The displayed quadratic margin proves
that the example is immediately beyond the theorem's hypothesis. QED.
