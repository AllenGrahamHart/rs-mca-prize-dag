# Proof - L1 mixed-residual intersection pin

The polarized petal-entropy ledger proves that for every fixed `E_root`, all
exact support strata with

```text
p+e <= E_root
```

have total size at most

```text
2^M binom(M+E_root,E_root)n^(E_root+1).
```

At the lower cutoff `M=O(log n)`, this is polynomial in `n`. Hence `(I1)` is
polynomially bounded.

Fix `E_d,V_2,V_R`. The B11 first-match router partitions every word with
`d<=ell+E_d` into `J`, `A2`, `AR`, and `RES`. If `G_2<=V_2`, the word is in
`J` or `A2`. If `G_2>V_2` but `G_R<=V_R`, it is in `J`, `A2`, or `AR`.
Therefore every word in `(I2)` belongs to the proved `J/A2/AR` union.

The B11 bound for that union is

```text
n(n-k+1)/((s+lambda_J)^2-n(k-1))
+ binom(M,2) sum_(v=0)^V_2 binom(2ell,v) q^(2E_d+V_2+2)
+ M sum_(w+v<=V_R) binom(b,ell-w)binom(ell,v)
    q^(2E_d+V_R+2),
```

with the optional replacement of the first term by `1`. Its first
denominator is a positive integer by the definition of `lambda_J`. For fixed
`E_d,V_2,V_R`, all remaining sums have fixed width, `M=O(log n)`,
`b<ell<=n`, and `q=poly(n)`. Thus `(I2)` is polynomially bounded.

The union of `(I1)` and `(I2)` is polynomially bounded. Its complement is,
by De Morgan's law,

```text
p+e > E_root
and
(d > ell+E_d or (G_2 > V_2 and G_R > V_R)),
```

which is `(I3)`.

Finally, `petal_reserve_rich_fiber_reduction` applies to every non-planted
listed residual in the same maximal chart. It supplies the displayed rich
fiber independently of which side of the two ledger partitions the word
occupies. Intersecting that necessary condition with `(I3)` proves the final
claim.

For `(I4)`, apply `l1_polarized_b11_box_closure` with the fixed parameters
`P,E`. It proves the complement of `(I4)`, namely `p<=P` and
`d<=ell+E`, polynomially bounded. Therefore its unpaid complement is exactly
`p>P or d>ell+E`.

Finally, on the bounded-`p` side, apply
`l1_marked_constant_shift_subtwoell_exclusion` to any three dense selected
petals whose full locators are `P-a_i`. Their missing locators have total
degree `v<=p`. If `ell<d` and `d+p<2ell`, then `d+v<2ell`, so the marked
strict-strip theorem excludes the contributor. This is only the claimed
common-pencil subbranch; no arbitrary-locator or two-dense conclusion is
inferred.

For a general strip index `m>=1`, apply
`l1_marked_constant_shift_multistrip_exclusion` instead. If at least `2m+1`
dense selected petals share the pencil, `m ell<d`, and
`d+p<(m+1)ell`, then `v<=p` gives `d+v<(m+1)ell`, so that contributor is
excluded. This proves exactly the stated multistrip refinement.

When equality holds at the survivor endpoint `T=2m`, apply
`l1_marked_constant_shift_extremal_kernel_normal_form`. Its exact-rank proof
and coefficient reconstruction give the determinant-`Q` matrix stated in the
pin. The same dependency constructs saturated examples, so no exclusion or
payment is inferred beyond that normal form.

For every lower endpoint `t<=2m`, apply
`l1_marked_constant_shift_forney_window_normal_form`. The interpolation-
module index theorem, saturation gate, and predictable-degree reconstruction
give the displayed Forney range and exact generator count. Its sharp families
show that this is a classification only, not a payment.

Fixing one Forney cell, its marks, and its defect locator, apply
`l1_marked_common_pencil_crt_fiber_bound`. Pairwise coprimality of the support
locators gives the singleton numerator conclusion above the lower endpoint
and the `q^(2p)` endpoint bound. The canonical marked reduction then removes
any further codeword multiplicity.
