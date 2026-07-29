# L1 Mersenne HNF m=8 order-one conic reduction

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_order_one_involution_component_exclusion`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the four official `(m,h)=(8,7)` next-to-maximal rows

Put

```text
u=rho*c*(c-1),
A=11c^2+5c+11,
B=c^4+c^2+1.                                         (OCR1)
```

The residual order-one equation `Psi_7(rho,c)=0` is exactly

```text
35u^2+14Au+120B=0.                                   (OCR2)
```

Equivalently, with

```text
D(c)=247c^4+770c^3+1269c^2+770c+247,                (OCR3)
```

it is the reciprocal-quartic square condition

```text
D(c)=7(5u+A)^2.                                      (OCR4)
```

Since every survivor has `c!=0,1`, define

```text
z=c+c^(-1),
w=(5u+A)/c=5rho(c-1)+11z+5.                         (OCR5)
```

Then (OCR4) is the conic

```text
7w^2=247z^2+770z+775.                                (OCR6)
```

It has the base-field point `(z,w)=(-1,6)`. On the affine line chart through
that point, `w=6+t(z+1)`, every other point with `247-7t^2!=0` is

```text
z=(7t^2+84t-523)/(247-7t^2),
w=6(7t^2-46t+247)/(247-7t^2).                       (OCR7)
```

Thus the live `h=7` curve can be represented by the projective conic
parameter `t`, the single quadratic pullback

```text
c^2-zc+1=0,                                          (OCR8)
```

and `rho=(w-11z-5)/(5(c-1))`. The vertical-line point `(-1,-6)`, represented
by `t=infinity`, and the denominator-zero projective chart must be handled
separately; the base point is the tangent specialization `t=23/7`.

This does not prove the curve empty or impose reciprocal traces, pointwise
Frobenius, torsion, cyclotomic divisibility, or an inner lift. The `h=15`
row is outside its scope.
