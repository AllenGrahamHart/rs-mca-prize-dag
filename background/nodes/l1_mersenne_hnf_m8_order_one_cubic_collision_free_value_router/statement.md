# L1 Mersenne HNF m=8 order-one cubic collision-free value router

- **status:** PROVED
- **dependencies:** `l1_mersenne_hnf_order_one_color_degree_barrier`,
  `l1_mersenne_hnf_m8_order_one_conic_reduction`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** cubic colored interpolants taking six distinct values on the
  six reduced h=7 roots

Fix a primitive eighth root `omega`. Up to cyclic multiplication of all
colors, the two missing colors have one of the four forms

```text
{1,omega^delta},       delta in {1,2,3,4}.            (CFV1)
```

Define

```text
M_delta(X)=(X-1)(X-omega^delta),
V_E(X)=Res_W(L_(r,d)(W),X-E(W)).                     (CFV2)
```

Every collision-free cubic packet lies on one of the four bounded systems

```text
35d^2r^2+14d(11d^2+27d+27)r
 +120(d^4+4d^3+7d^2+6d+3)=0,

V_E(X)M_delta(X)=X^8-1,       deg E=3.               (CFV3)
```

The second line is an equality of monic degree-eight polynomials and hence
gives eight fixed-degree coefficient equations, with the leading one
automatic. For an official row adjoin the norm-color equation for `d` and
saturate by the inherited HNF factors, `lc(E)`, `disc(L)`, and
`disc(V_E)`.

A unit saturation of all four distance packets closes the complete
collision-free cubic chamber. No unit verdict, repeated-color cubic packet,
higher degree, cyclotomic converse, inner lift, or L1 close is asserted.
