# L1 Mersenne HNF m=8 order-one cubic three-two-one factor reduction

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_color_remainder_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the h=7 cubic color profile `3+2+1` on all four official rows

Order the three distinct colors as `(alpha,beta,gamma)`, where their
multiplicities are respectively `(3,2,1)`, and put

```text
lambda=(gamma-alpha)/(beta-alpha).                   (TOF1)
```

There are monic cubics `F,G` and a nonzero scalar `B` such that

```text
L_(r,d)=F G,
Res_W(G(W),X-F(W))
 =X^3-(2+lambda)B X^2+(1+2lambda)B^2 X-lambda B^3.  (TOF2)
```

For each of the seven cyclic color-set representatives, the six assignments
of the roles `(alpha,beta,gamma)` give at most 42 scale-free values of
`lambda`. Equations (TOF2), the h=7 conic, and the inherited norm-color
condition form a fixed-degree exact necessary packet for `3+2+1`.

Saturate by the HNF factors, `B`, the three color differences, `disc(L)`,
and the subresultants fixing the `(3,2,1)` gcd degrees. A unit saturation of
all role packets closes the profile.

No unit verdict, `2+2+2` claim, four-or-more-color cubic packet, higher
degree, cyclotomic converse, inner lift, or L1 close is asserted.
