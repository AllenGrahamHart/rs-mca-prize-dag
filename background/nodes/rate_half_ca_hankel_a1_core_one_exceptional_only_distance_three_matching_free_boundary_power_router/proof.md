# Proof

Fix one matched pair `D_i=(X-a)(X-b)` and write `A=D_iA_i`. At its roots,

```text
A'(a)=(a-b)A_i(a),       A'(b)=(b-a)A_i(b).          (1)
```

Therefore the ratio in the boundary root-unity theorem is

```text
U_(a,b)
 =B(a)A_i(a)/(B(b)A_i(b))
 =-B(a)A'(a)/(B(b)A'(b)).                            (2)
```

The fourth power removes the sign. Substitution in the definition of the
pair label gives

```text
zeta_(a,b)=-K_A(a)/K_A(b).                           (3)
```

The official exponent `e=2^38-1` is odd. Hence

```text
zeta_(a,b)^e=1
 iff -K_A(a)^e/K_A(b)^e=1
 iff Y_a=-Y_b.                                       (4)
```

This proves `(MBP3)`.

For two triple points, the boundary label is

```text
eta_(t,u)
 =[P_X'(t)/P_X'(u)]/
   ([A(t)/A(u)]^4[B'(t)/B'(u)])
 =K_B(t)/K_B(u).                                     (5)
```

Thus `eta_(t,u)^e=1` if and only if `Z_t=Z_u`, proving `(MBP4)`.

Every `Y_a` is nonzero and the official field has odd characteristic, so
the involution `y |--> -y` has no fixed point on these values. A perfect
matching satisfying `(MBP3)` exists exactly when each value and its negative
have the same multiplicity. This is central symmetry of the root multiset
of `M_A`. Since `deg M_A=2e` is even,

```text
product_a(-Y-Y_a)=product_a(Y+Y_a)=M_A(Y)
```

is equivalent to `M_A(-Y)=M_A(Y)`. This proves `(MBP6)` and the matching
reconstruction. Pairing the terms `y^m+(-y)^m` proves `(MBP7)` for odd `m`.
QED.
