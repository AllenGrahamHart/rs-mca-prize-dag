# L1 Mersenne HNF m=8 order-one cubic three-double affine-invariant formula

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_double_affine_color_compiler`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the h=7 cubic color profile `2+2+2`

Let three centered parameters `v_i` have elementary invariants

```text
sum_i v_i=0,       p=sum_(i<j) v_iv_j,       eta=v_1v_2v_3.    (AIF1)
```

For the three values of the quadratic map

```text
y_i=A v_i^2+L v_i,                                (AIF2)
```

let `P,Q` be the depressed-cubic invariants of the `y_i`. Then

```text
P=L^2p-3AL eta-A^2p^2/3,

Q=A^3(eta^2+2p^3/27)-A^2Lp eta
  +(2/3)AL^2p^2+L^3 eta.                           (AIF3)
```

For the scaled HNF core (TLR1)--(TLR8), put

```text
z=x^2+q/6,
p=b-12,
eta=-xp-q(d+2)/6,
ell=z-2p/3.                                        (AIF4)
```

The affine invariants (TAC8) of the three cubic fiber values are exactly

```text
P=ell^2p+6x ell eta-(4/3)x^2p^2,

Q=-8x^3(eta^2+2p^3/27)-4x^2 ell p eta
  -(4/3)x ell^2p^2+ell^3 eta.                      (AIF5)
```

Consequently the full squarefree characteristic-zero color equation is the
product of four rational factors

```text
50P^3-27Q^2,

729Q^4+6048P^3Q^2-578P^6,

729Q^4+108P^3Q^2+54P^6,

91125Q^4+64908P^3Q^2+13448P^6.                    (AIF6)
```

Their product is `Phi_8(P,Q)` from (TAC6). Thus the generic `2+2+2`
branch has four rational color packets, not a degree-42 role resultant. On
each packet, use

```text
alpha=(q-d)A_5=-(q-d)xz,
beta=(q-d)B_5+6dG,
b=-beta/alpha                                      (AIF7)
```

off (TLR9), clear only the displayed denominators, and retain the conic,
the substituted `D_b`, and `alpha B_6-A_6 beta=0`. This is an explicit
three-variable rational packet in `(x,q,d)`. No packet is declared empty.
