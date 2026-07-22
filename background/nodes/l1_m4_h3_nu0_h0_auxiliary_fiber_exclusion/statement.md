# L1 m=4, h=3, nu=0, h=0 auxiliary-fiber exclusion

- **status:** PROVED
- **dependency:** `l1_m4_h3_nu0_h0_universal_packet_exclusion`
- **consumer:** `l1_mixed_petal_amplification`

Assume the surviving nonzero-`b`, constant-eliminant branch and put

```text
r=R(0),       A=a/r^2,       B=b/r^3,
sigma=2A/3,   C=1+A+B.                                (AFE1)
```

For either packet in the complete projective table, `sigma!=1`. The Euler
identity and exact degree accounting force

```text
D=rad(R-r)/X * rad(R-sigma r).                        (AFE2)
```

Let `x_i=(beta_i-r)/r` be the three normalized shifted split values and put
`s=sigma-1`. Every `x_i/s` must lie in the order-`n=4(p+1)` subgroup `K`.
Equivalently, the monic cubic

```text
P_A(W)=s^(-3)[(sW)^3+3(sW)^2+(A+3)sW+C]              (AFE3)
```

must divide `W^n-1`.

For the sole packet left by the dependency,

```text
p=2147483647,       A=844833809,       B=2002167159,
P_A(W)=W^3+1800058023W^2+664831389W+573306971,
W^n-1 mod P_A=876663072!=0.                           (AFE4)
```

The exceptional packet is therefore impossible. Combined with the universal
packet exclusion, the entire `nu=0,b!=0,deg H=0` endpoint is empty on all
four official characteristics. This does not treat the cubic eliminant,
zero `b`, positive valuation, wider `m`, or close L1.
