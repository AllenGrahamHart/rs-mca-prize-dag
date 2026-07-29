# L1 Mersenne HNF m=8 order-one cubic three-double x=0 quintic reduction

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_double_linear_remainder_reduction`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the exceptional `x=dU-3=0` branch of the h=7 cubic `2+2+2` profile

Put

```text
A=11d^2+27d+27,
B=d^4+4d^3+7d^2+6d+3,
C=13d^2+34d+33,
D=5d^4+21d^3+37d^2+32d+15,
P=5d^3+16d^2+18d+10.                              (XQ1)
```

On `x=0`, the reduced fifth equation factors as

```text
M_5=q(d+2)J/120,
J=25q^2+10Cq+24D.                                  (XQ2)
```

The saturated chamber has `q!=0`. The branch `d=-2` is impossible by the
norm-color equation. On the remaining branch `J=0`, combining `J` with the
residual conic

```text
C_0=35q^2+14Aq+120B=0                              (XQ3)
```

gives

```text
25C_0-35J=-10(2d+3)(35(d+2)q+12P).                 (XQ4)
```

The branch `d=-3/2` is also norm-impossible. Otherwise

```text
q=-12P/(35(d+2)),                                  (XQ5)
```

and substitution in (XQ3) gives

```text
35(d+2)^2 C_0|_(XQ5)=-24(d+3)P_5(d),               (XQ6)

P_5(d)=60d^5+407d^4+1147d^3+1659d^2+1218d+360.    (XQ7)
```

The branch `d=-3` is again norm-impossible. Consequently every surviving
`x=0` packet must satisfy (XQ5), (XQ7), and

```text
d^(p+1) in mu_8.                                   (XQ8)
```

Thus 32 degree-five norm gcds, one for each official row and eighth-root
color, suffice to close the complete `x=0` branch. No gcd verdict is claimed
here.
