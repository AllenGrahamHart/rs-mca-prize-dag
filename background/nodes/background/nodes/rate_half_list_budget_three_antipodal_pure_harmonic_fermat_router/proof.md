# Proof

The centered outer parameters satisfy

```text
product_i(T+c_i)=T^4+e_4.                              (1)
```

They are distinct, so `e_4!=0`. Since the official field contains the eighth
roots of unity, the four `c_i` form a nonzero scalar multiple of the fourth
roots of unity. In the ordering `(1,-1,i,-i)`, their cross-ratio is `-1`.
The Möbius weld says that the matched `c_i` are one fractional-linear image of
the `a_i`; cross-ratio invariance proves `(HFR2)` after relabeling.

The original deleted quadratics have roots in the order-`4d` domain. Therefore
their constants `a_i` lie in its order-`2d` square subgroup, and
`b_i=a_i^2` lie in the order-`d` subgroup. If `a_i=a_j` or `a_i=-a_j`, their
squares would agree, so the printed non-antipodality follows.

Scale by `a_0^(-1)`, write the normalized lifts as `1,x,y,w`, and expand
`(HFR2)`. It becomes

```text
2x-y(1+x)-w(1+x-2y)=0.                                 (2)
```

If the coefficient of `w` vanished, then `1+x=2y`; substituting in the
remaining part of `(2)` gives `(x-1)^2=0`, hence `x=y=1`, contrary to
distinctness. Division is therefore valid and gives `(HFR3),(HFR4)`.

Now reverse the pure norm equation. Put

```text
B=z^rU(z^-1),       C=z^(r-1)V(z^-1).
```

Then `B(0)=1`, `C(0)!=0`, and

```text
Q=B^4+e_4 z^4 C^4.                                    (3)
```

All `c_i^4` equal `-e_4`, so `e_4C(0)^4` has a fourth root in the field: use
one `c_iC(0)` and a fourth root of `-1`. Normalize `Cbar=C/C(0)` and choose
`delta^4=e_4C(0)^4`. Setting `Z=delta z Cbar` turns `(3)` into `(HFR6)`.
The exact degree `deg V=r-1` gives `ord_0Z=1` and `deg Z<=r`; also
`deg B<=r`. Coprimality of `U,V` and `B(0)=1` give `gcd(B,Z)=1`.

Conversely, factor the right side of `(HFR6)` over the four roots `rho_i` of
`T^4+1`:

```text
Q=product_i(B+rho_i Z).                                (4)
```

Since `ord_0Z=1`, reverse `B` and `Z/z` to obtain a monic degree-`r`
direction and a degree-`r-1` direction. Harmonicity is exactly equality of the
unordered cross-ratio orbits of the `a_i` and `rho_i`, so after relabeling
there is a fractional-linear matching. As in the canonical-span converse,
any three matched columns `(1,a_i,rho_i,a_irho_i)^T` are independent and all
four are dependent; the unique kernel has no zero entry and supplies the two
locator relations. Equation `(4)` and the antipodal-descent converse then
reconstruct the pure component.

The existing pure-quartic theorem supplies squarefreeness and the exact linear
Wronskian residual for every reconstructed solution. QED.
