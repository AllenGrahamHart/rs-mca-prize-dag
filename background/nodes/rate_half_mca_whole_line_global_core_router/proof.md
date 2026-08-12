# Proof

Choose two distinct slopes `gamma_0,gamma_1`. If `c_*>=k`, the two selected
explanations determine degree-`<k` polynomials

```text
B=(h_gamma1-h_gamma0)/(gamma_1-gamma_0),
A=h_gamma0-gamma_0 B.
```

On `C_*`, every `h_gamma` equals `r_0+gamma r_1`. Hence
`h_gamma` and `A+gamma B` agree on at least `k` evaluation points. Both have
degree below `k`, so they are equal. Thus `c_*>=k` forces the global affine
case. In the non-global-affine case, `c_*<k<m`.

Let `G_*` be the squarefree locator of `C_*`, and let `a_0,a_1` be the
degree-`<c_*` interpolants of the received pair on `C_*`. For each slope,
the exchange-graph argument from the imported common-core theorem supplies
an actual size-`m` noncontained witness containing `C_*`. Subtract
`a_0+gamma a_1` and divide by `G_*`. The same division is used for every
slope, so it defines one shortened received line and sends

```text
h_gamma -> (h_gamma-a_0-gamma a_1)/G_*.
```

Pointwise equality off `C_*` proves maximal-support and witness transport.
The inverse `p_j=a_j+G_*p'_j` proves same-support noncontainment in both
directions. The affine slope is unchanged. Because `C_*` is defined once
from the entire declared family, each selected slope appears exactly once
and the slope projection is literally the identity.

The parameter identities are immediate. The official paid/residual outcomes
then apply the imported fixed-core and direction-separated boundaries to
this one family. No local-core payment is added.

In the `GF(11)` control from the local-owner route cut, the seven selected
supports have global intersection `{10}`. The single cancellation maps
`(n,k,m)=(10,5,7)` to `(9,4,6)` and preserves all seven slopes. The shortened
direction has maximum degree-`<4` agreement six, so separation fails and the
router honestly emits `DIRECTION_LIST_SHORTENED_S` at `s=4` rather than a
payment.
