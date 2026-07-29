# L1 Mersenne HNF m=8 order-one cubic three-two-one role weld

- **status:** PROVED
- **dependencies:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_common_quadratic_compiler`, `l1_mersenne_hnf_m8_cubic_three_two_one_role_factor_compiler`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the h=7 cubic color profile `3+2+1`

In the common-quadratic core put

```text
R=a(3y^2+2g_1y+g_2),       S=B.                    (TRW1)
```

The inherited saturations give `R*S!=0`, and (TQC7) gives

```text
lambda=1+R/S.                                      (TRW2)
```

Define

```text
A_0=S^2+RS+R^2,
B_0=(2S+R)(S+2R)(R-S).                             (TRW3)
```

The four rational role packets (RFC2) become

```text
B_0^2+50A_0^3=0,

B_0^4-224B_0^2A_0^3-578A_0^6=0,

B_0^4-4B_0^2A_0^3+54A_0^6=0,

125B_0^4-2404B_0^2A_0^3+13448A_0^6=0.             (TRW4)
```

After (TQC3) and (TQC6), `R,S,A_0,B_0` are explicit rational polynomials
in `(g_1,y,r,d)`. For each line of (TRW4), the complete p-free
common-quadratic core is the three equations (TQC5), the h=7 conic, and
that one role equation: five equations in four variables, with no `lambda`
or color-field extension variable. No packet is declared empty.
