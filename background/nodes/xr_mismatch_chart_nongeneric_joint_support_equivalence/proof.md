# Proof

Assume first that the chart is nongeneric. Let `R subseteq T`,
`|R|>=A-d`, be a common agreement set for `b_i` and `g_i`. The product
`P_Zg_i` has degree below `d+(K-d)=K`, so `c_i'=c_i+P_Zg_i` is a codeword.
On `Z`, the product vanishes and the original recovered pair already agrees
with `(u,v)`. On `R`, the equality `b_i=g_i` is exactly
`e_i=P_Zg_i`. Hence `(c_0',c_1')` explains `(u,v)` on `Z union R`, whose
size is at least `d+(A-d)=A`.

Conversely, suppose a codeword pair `(c_0',c_1')` explains `(u,v)` on
`Z union R`, where `R subseteq T` and `|R|>=A-d`. On `Z`, both the original
and new codeword pairs equal the received pair. Therefore each difference
`c_i'-c_i` vanishes on `Z` and is divisible by `P_Z`; write it as `P_Zg_i`
with `deg g_i<K-d`. On `R`, agreement of the new pair gives
`e_i=P_Zg_i`, hence `b_i=g_i`. The chart is nongeneric at radius
`|T|-(A-d)`.

Finally, let distinct codeword pairs explain the same received pair on
supports `Y,Y'`. At least one component difference is a nonzero polynomial
of degree below `K`; it vanishes on `Y intersect Y'`, so
`|Y intersect Y'|<=K-1`. This proves the low-core consequence.
