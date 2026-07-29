# L1 Mersenne HNF m=8 order-one cubic three-double quadratic-quotient weld

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_double_affine_invariant_formula`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the generic h=7 cubic color profile `2+2+2`

Retain `p=b-12` from (AIF4), and put

```text
C=d^2+3d+3,
a=3x^2-q/2,
h=3qC/4+q^2/8.                                     (QQW1)
```

The quadratic equation `D_b=0` is exactly

```text
p^2+ap-h=0.                                         (QQW2)
```

Define pairs `(U_n,V_n)` by

```text
(U_0,V_0)=(0,1),       (U_1,V_1)=(1,0),
U_(n+1)=V_n-aU_n,      V_(n+1)=hU_n.                (QQW3)
```

Then `p^n=U_np+V_n` modulo (QQW2). Applying (QQW3) to (AIF5) gives
affine-linear remainders for `P,Q`, and hence for each of the four rational
color factors in (AIF6):

```text
F_i(P,Q)=c_(i,1)(x,q,d)p+c_(i,0)(x,q,d) mod (QQW2),
1<=i<=4.                                            (QQW4)
```

The first invariant already has the compact remainder

```text
12P=R_P p+S_P mod (QQW2),

R_P=-60x^4-8qx^2+8q(d+2)x+4qC+q^2,
S_P=-12xq(d+2)(x^2+q/6).                            (QQW5)
```

For the generic coefficient weld, define

```text
alpha=(q-d)A_5,
delta=12alpha+(q-d)B_5+6dG,
gamma=12A_6+B_6.                                    (QQW6)
```

On `alpha!=0`, the complete p-free generic core in color packet `i` is
equivalent to the following four equations in `(x,q,d)`:

```text
35q^2+14q(11d^2+27d+27)
 +120(d^4+4d^3+7d^2+6d+3)=0,

delta^2-a alpha delta-h alpha^2=0,

alpha gamma-A_6 delta=0,

alpha c_(i,0)-c_(i,1)delta=0.                       (QQW7)
```

All quantities in (QQW7) are explicit rational polynomials through
(TLR2), (TLR4), (TLR6), (AIF4)--(AIF6), and the recurrence (QQW3).
Clearing powers of `2,3,5` is harmless in every official characteristic.
No color packet is declared empty.
