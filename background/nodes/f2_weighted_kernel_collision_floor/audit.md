# Audit

1. The normalization is `2^m Z=sum_v N(v)^2`; omitting `2^m` changes the
   exponent by the full block length.
2. The denominator in the floor is `p^d`, where `d` is the actual rank of
   the syndrome map, not the number of displayed extension-field rows.
3. The floor is useful for refutation when `m-d log_p 2` is linear, but it
   does not provide the upper bound needed on saturated generating rows.
4. No randomness, average over codes, or maximum-fiber assertion is used.
5. This is the field-generic core of canonical Round-18 THEOREM Z-FLOOR;
   the proof here is self-contained and does not inherit its row
   classification.
6. For the weighted mass the Fourier factor is `1+cos`, equivalently
   `2cos^2`. The factor `1+2cos` counts ternary words without the
   `2^-wt` weight and is not the prize terminal.
