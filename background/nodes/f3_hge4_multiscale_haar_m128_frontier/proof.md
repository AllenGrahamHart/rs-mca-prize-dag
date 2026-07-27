# Proof - balanced-factor Haar augmentation and `m=128`

The signed support difference has equally many `+1` and `-1` coefficients,
so `F(1)=0` as an integer identity. Gauss division gives `(MX1)`.

For each order in the nonzero norm product,

```text
F(zeta_O)=(zeta_O-1)F_1(zeta_O).
```

The cyclotomic identity `Phi_O(1)=2` for dyadic `O>=2` shows that the
absolute norm of `zeta_O-1` is two. There are exactly `1+|S|` nonzero norm
factors. If a Haar scale is zero, the existing proof factors the
corresponding `Phi_(N_a)` from `F`. Those cyclotomic polynomials are distinct
from `X-1` and pairwise coprime in `Z[X]`; hence their norm contributions and
the `X-1` contributions multiply. Appending these factors to `(MHN6)` proves
`(MX2)`.

The row prime satisfies `p>n^2`. Thus the lower side of `(MX2)` is strictly
larger than

```text
2^(T_2(S)+1+|S|) n^(2R_S).
```

The weighted AM--GM upper side remains exactly `U_S`. Therefore `(MX3)` is a
sufficient contradiction, including equality.

It remains only integer arithmetic. The verifier evaluates the
cross-multiplied form of `(MX3)` at the smallest ambient exponent `s=13`.
For each width it enumerates all `2^ell` zero/nonzero Haar patterns, where
`ell=1+floor(log_2 floor((h-1)/2))`. It proves every pattern at widths
`12,...,31` and obtains exactly the residual masks printed in `(MX4)` at
widths `9,10,11`. Increasing the ambient exponent only increases the left
side.

Finally, `m/4<=h<m/3` is `32<=h<=42`, so the proved quarter-width exclusion
deletes that interval. The proved complement-third gate deletes `3h>=128`,
hence every `43<=h<=64`. Together with the integer gate this proves `(MX5)`.
QED.
