# KoalaBear m2 r4 positive 433-1b product-rank-drop complete exclusion

- **status:** PROVED
- **scope:** the complete product-row rank-at-most-four branch of
  `433-1b -> O0a`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_deployed_rational_classifier`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas`,
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`, and
  `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature`
- **consumer:** `rate_half_band_closure`

The deployed rational classifier leaves exactly sixteen guarded common
points on the product-row rank-drop branch.  At each point the full common
matrix has rank seven, so it gives a unique projective coefficient kernel

```text
(A_2,A_0,B_1),       F(W)=A_0(W)/A_2(W).          (KBP1BRX-1)
```

Write `xi=-t^2` for the missing mate of the singleton common source label.
The signed atlas gives four lanes `(sigma_c,sigma_o)` and outside records

```text
de, de, -de, df, sigma_o ef, bf, sigma_c cf.      (KBP1BRX-2)
```

If record `x` lies over `xi`, then every actual packet satisfies

```text
x=F(xi),
xi B_1(xi)^2=s_x^2 A_2(xi)^2,                    (KBP1BRX-3)
```

where `s_x^2=u^2+v^2+2x` for the signed target endpoints of `x`.
After removing `x`, the other six source labels form three deck pairs.  For
products `y,z` on one such pair, define

```text
P_y(W)=A_0(W)-yA_2(W),
Q_z(W)=A_0(-W)-zA_2(-W),
C_F(y,z)=Res_W(P_y,Q_z).                          (KBP1BRX-4)
```

Thus each point and lane has the exhaustive necessary ledger

```text
7 choices for x at xi * 15 perfect matchings = 105 cases. (KBP1BRX-5)
```

For each case, form the ideal in target representatives `d,e,f` generated
by the missing-product equation, three equations `C_F(y,z)=0`, the
missing-mate squared-sum equation, and an inverse guard requiring the six
target representatives `1,b,c,d,e,f` to be nonzero and pairwise distinct
up to sign.

All

```text
16 points * 4 lanes * 105 cases = 6720            (KBP1BRX-6)
```

guarded ideals are unit ideals over `F_2130706433`.  Hence no deployed
`433-1b -> O0a` packet lies on the product-row rank-drop branch.

This theorem does not solve the principal product-rank-five branch, close
the whole route, positive coordinate parity, K3, LIST, MCA, or either Prize
result.

## Falsifier

An actual product-rank-drop packet, a missing point/lane/record/matching
case, a nonunit guarded ideal, an invalid paired-product or squared-sum
necessity, or a target guard that excludes admissible packets.
