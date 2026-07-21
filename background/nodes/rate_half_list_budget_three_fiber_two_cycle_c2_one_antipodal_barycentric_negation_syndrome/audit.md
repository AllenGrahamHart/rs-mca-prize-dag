# Audit

1. The weights are attached to the pencil parameters `w_i`, not to the
   multiplier roots in the cells.
2. The normalization `lambda_i=1/Phi'(w_i)` fixes
   `sum lambda_i w_i^3=1`; rescaling the weights rescales the syndrome.
3. The endpoint is `-2H`, not `-H`, because `3H` is odd and negation doubles
   the weighted cell moment.
4. Nonvanishing uses the official characteristic bound.  It is not a
   characteristic-zero inference.
5. The derivative formula is an equality-case classification only.  It says
   nothing about supports larger than `3H+1`.
6. No Modal or official-order enumeration is involved.
