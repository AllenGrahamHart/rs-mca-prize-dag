# Proof

The Euler dependency proves that minimum support forces
`deg C=m=H-3`, so `c!=0`.  The canonical-cell theorem gives

```text
G_i=B+w_i z^H C=product_(a in A_i)(1-az),
|A_i|=r,       A_i subset mu_N.                       (1)
```

Both summands on the left of `(1)` have degree at most `r`, and the
coefficient of `z^r` is `ell_i=b+cw_i`.  Since every `G_i` has exact degree
`r`, this coefficient is nonzero.  Moreover `r=2H-3` is odd, so comparison
with the right side of `(1)` gives

```text
ell_i=(-1)^r product_(a in A_i)a=-product_(a in A_i)a in mu_N. (2)
```

The `w_i` are distinct and `c!=0`; hence the `ell_i` are distinct.  This
proves the first assertion in `(ICT2)` and shows that `O_inf` is squarefree
and divides `X^N-1`.

For the product assertion, `E` has leading coefficient `-P_src`.  Since
`Q=(1-z^N)/E`, its leading coefficient is `P_src^(-1)`.  On the other hand,
`Q=product_i G_i`, so its leading coefficient is `product_i ell_i`.  This
proves the second assertion in `(ICT2)` and the constant coefficient claim.

The centered outer quartic is

```text
Phi(W)=product_i(W-w_i)=W^4+alpha W^2+beta W+gamma.
```

Substitution of `W=(X-b)/c` and multiplication by `c^4` proves `(ICT3)`.
Because `N=2^40`, repeated squaring in the quotient by `O_inf` gives
`R_40=X^N mod O_inf`.  The divisibility just proved is therefore equivalent
to `R_40=1`, establishing `(ICT4)`.

For each root, affine scaling gives

```text
O_inf'(ell_i)
 =product_(j!=i)(ell_i-ell_j)
 =c^3 product_(j!=i)(w_i-w_j)
 =c^3 Phi'(w_i).                                     (3)
```

The common nonzero factor in `(3)` preserves every equality class among the
reciprocal derivatives.  The collision dependency proves that the outer
weights have exactly one repeated pair, so `(ICT5)` follows.

Finally the centered coefficients of `O_inf` are
`alpha_inf=alpha c^2`, `beta_inf=beta c^3`, and
`gamma_inf=gamma c^4`.  Substitution in the binary-quartic invariant gives
`J_inf=c^6J`.  The collision-branch dependency proves `J=0` when the
selected denominator pair is the unique antipodal pair.  This proves
`(ICT6)`. QED.
