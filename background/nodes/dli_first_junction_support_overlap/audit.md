# Audit

The main normalization trap is the factor `2^h`: the products defining
`p_Sq_S` contain `2^h E_SO_S`, while the junction ratio contains `2^n`.
The empty support is deleted only from the overlap numerator, not from either
marginal normalization.

The Vandermonde exclusions apply to nonempty sign supports. In particular,
`E_(Z/h)=1` is allowed because its signed complement is empty.

`verify.py` independently enumerates level-zero subsets, level-one sums,
junction skews, and support-conditioned factors. It also checks primitive
ownership and exact rational normalization on four small-field fixtures.

