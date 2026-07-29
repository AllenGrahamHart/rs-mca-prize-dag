# L1 Mersenne HNF m=8 order-one cubic three-two-one official Frobenius-role split

- **status:** PROVED
- **dependencies:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_galois_role_weld`, `l1_mersenne_next_to_maximal_exceptional_reduction`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the official h=7 cubic color profile `3+2+1`

Every official characteristic in this chamber satisfies `p=7 mod 8`. Fix
`s in F_p` with `s^2=2`, and retain `R,S` from (TRW1). The three rational
quadratic role packets become

```text
H_1=R^2+2RS+2S^2,
H_2=R^2+S^2,
H_3=2R^2+2RS+S^2.                                  (FRS1)
```

For `T=R/S`, the nine rational quartics split into the following conjugate
quadratic pairs over `F_p`:

```text
Q_4^+ =T^2+sT+1,                 Q_4^- =T^2-sT+1,
Q_5^+ =T^2+sT+2-s,               Q_5^- =T^2-sT+2+s,
Q_6^+ =T^2+3+2s,                 Q_6^- =T^2+3-2s,
Q_7^+ =T^2+2T+4+2s,              Q_7^- =T^2+2T+4-2s,
Q_8^+ =T^2+(2+s)T+3+2s,          Q_8^- =T^2+(2-s)T+3-2s,
Q_9^+ =T^2+(2+s)T+2+s,           Q_9^- =T^2+(2-s)T+2-s,
Q_10^+=2T^2+2T+2+s,              Q_10^-=2T^2+2T+2-s,
Q_11^+=2T^2+(2+2s)T+2+s,         Q_11^-=2T^2+(2-2s)T+2-s,
Q_12^+=4T^2+(4+2s)T+2+s,         Q_12^-=4T^2+(4-2s)T+2-s.              (FRS2)
```

More precisely, for the quartics `P_j` in (GRW1),

```text
Q_j^+(X-1)Q_j^-(X-1)=P_j(X),       4<=j<=9,
Q_j^+(X-1)Q_j^-(X-1)=2P_j(X),     10<=j<=12.        (FRS3)
```

The scalar two is a unit on every official row. Hence, on `R*S!=0`, the
complete role condition is the disjunction of 21 systems: one equation
`H_i=0` for `1<=i<=3`, or one homogenized equation

```text
S^2 Q_j^epsilon(R/S)=0,
4<=j<=12,       epsilon in {+,-}.                   (FRS4)
```

All 21 displayed quadratics are irreducible over the official `F_p`. Thus
they are exactly the Frobenius-pair packets, not merely a possibly finer
factor list. Each branch retains (TQC5), the conic, and all inherited HNF
and exact-fiber saturations. This is an exact official-field degree-two
compiler, not a unit verdict.
