# L1 Mersenne HNF m=8 order-one cubic three-two-one exceptional-E J-zero role/P4 compiler

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_j0_structural_consistency_compiler`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** one fixed alternative official role packet on the fully
  proportional `E_G=X_*=J_*=L_*=F_b=0` chart

Retain (FPR1)--(FPR5), (DQR5)--(DQR7), and (FJS1)--(FJS7). For the selected
irreducible role quadratic write

```text
Phi(X,Y)=c_2X^2+c_1XY+c_0Y^2,
delta_Phi=c_1^2-4c_2c_0,

R_j=A(3Y_j^2+2xY_j+G_j),
S_j=(Y_j-A)V_j-Q_j,
a_d=b-6.                                            (FJR1)
```

The inherited role packet has `c_0*delta_Phi*R_j*q!=0`. Define two rational
role filters

```text
L_Phi=18c_0S_j+9c_1R_j+c_0q a_d,

W_Phi=c_0^2(q^2a_d^2+144qR_j^0)
       -81delta_Phi R_j^2,                         (FJR2)

R_j^0=-qP/(2880b).
```

Then `L_Phi=W_Phi=0` is exactly the fully proportional pair
`U_1=U_0=0` for this role packet. Uncancelled numerator representatives
satisfy

```text
deg Num(L_Phi)<=12,       deg_q Num(L_Phi)<=6,
deg Num(W_Phi)<=18,       deg_q Num(W_Phi)<=8.     (FJR3)
```

After `q=5bM/T`, define

```text
Lhat_Phi(b)=T^m Num(L_Phi)(b,5bM/T),   m=deg_q Num(L_Phi),
What_Phi(b)=T^n Num(W_Phi)(b,5bM/T),   n=deg_q Num(W_Phi). (FJR4)
```

These are univariate, with

```text
deg Lhat_Phi<=24,       deg What_Phi<=34.          (FJR5)
```

Let `eta` be either root in the ambient quadratic field of

```text
c_0 eta^2+c_1 eta+c_2=0.                           (FJR6)
```

On `Lhat_Phi=What_Phi=0`, reconstruct

```text
d=3(eta R_j-S_j)/q.                                (FJR7)
```

This reconstruction automatically satisfies `P_4=0` and the transported
role equation. Conversely every original `P_4`/role solution arises from
one of the two roots in (FJR6). Thus, for this fixed role packet, the
complete coefficient, structural, role, and `P_4` endpoint is exactly

```text
Bhat=Ehat=Fhat=Xhat=Zhat_D^j=Zhat_R^j
    =Lhat_Phi=What_Phi=0,                          (FJR8)
```

with `q` and `d` reconstructed by (FJ06) and (FJR7). The 21 official role
packets are alternatives, not simultaneous equations. Every inherited
nonzero guard and arithmetic-lift filter must be applied to both
reconstructed `eta` branches. This is an exact role/`P_4` compiler, not a
common-root, saturation, lift, emptiness, or critical-node verdict.
