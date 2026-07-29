# L1 Mersenne HNF m=8 cubic three-two-one role-polynomial compiler

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_common_quadratic_compiler`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the ordered color-role ratio in every cubic `3+2+1` packet

Put

```text
C(U)=(U^8-1)/(U-1)=U^7+U^6+...+U+1.                (RPC1)
```

For an indeterminate `lambda`, define

```text
R(lambda)=Res_U(C(U),C(1+lambda(U-1))).             (RPC2)
```

The polynomial `R` has degree 49 and is divisible by `(lambda-1)^7`.
Define the role polynomial

```text
Lambda_321(lambda)=R(lambda)/(lambda-1)^7.          (RPC3)
```

It has degree 42. Over every official characteristic, after squarefree
reduction its roots are exactly the distinct values

```text
lambda=(gamma-alpha)/(beta-alpha)                  (RPC4)
```

for ordered pairwise-distinct `alpha,beta,gamma in mu_8`, modulo common
color scaling. Consequently the common-quadratic compiler may adjoin the
single equation

```text
Lambda_321(lambda)=0,       lambda*(lambda-1)!=0,   (RPC5)
```

perform its shared elimination once with symbolic `lambda`, and factor the
retained role polynomial only afterward. This replaces at most 42 separate
input specializations; it supplies no unit verdict for the resulting system.
