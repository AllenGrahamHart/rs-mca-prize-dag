# Audit

- The local coefficient vectors after moving `alpha` to zero span the same
  `W_Q` as the original homogeneous coefficient forms.
- The terminal equation `M_1q_e=0` is needed to include the top coefficient;
  the middle recurrence alone covers only `q_0,...,q_(e-1)`.
- Source weights `eta_x` are nonzero and form an invertible diagonal matrix,
  so they do not alter evaluation rank.
- The rank bound is `m-c_alpha=j_(alpha,beta)`, not `m-c_alpha+1`.
- Core-freeness is used only to make every row form nonzero at the rank-one
  boundary; it does not supply point separation.
- No Smith-exponent equality is used, so the `E_1` slope is included.
