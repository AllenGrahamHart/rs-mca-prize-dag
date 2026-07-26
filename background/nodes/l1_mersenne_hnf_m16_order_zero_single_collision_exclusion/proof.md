# Proof - L1 Mersenne HNF m=16 order-zero single-collision exclusion

Assume that a quadratic `E_s` has exactly one repeated color. Normalize that
color to one and choose a primitive sixteenth root `zeta`. The 15 colors are

```text
M_(i,j)=mu_16 \ {zeta^i,zeta^j} disjoint_union {1},
1<=i<j<=15.                                          (1)
```

There are `binom(15,2)=105` patterns.

Write the normalized quadratic as

```text
E_s(W)/delta=y W(W-S)+x,       y!=0.                 (2)
```

For roots `a_1,...,a_15` of `P_s`, Newton's identities give

```text
sum_r a_r^k=-s,       1<=k<=15.                      (3)
```

Put `u_r=a_r(a_r-S)` and `z=1-S`. Expansion through the third power uses
only `(3)` through degree six, and therefore

```text
sum_r u_r^k=-s z^k,       k=1,2,3.                  (4)
```

The centered moments of the `u_r` are

```text
M_2=-s(15+s)z^2/15,
M_3=-s(15+s)(15+2s)z^3/225.                         (5)
```

For `(1)`, set

```text
P_k=1-zeta^(ik)-zeta^(jk),
C_2=P_2-P_1^2/15,
C_3=P_3-3P_1P_2/15+2P_1^3/225.                     (6)
```

Exact arithmetic checks `C_2!=0` for all 105 patterns. Since affine maps
scale centered moments by `y^k`, every candidate `s` obeys

```text
I_(i,j):=C_3^2/C_2^3
         =-(15+2s)^2/[15s(15+s)],                   (7)
q_(i,j)(X):=(15+2X)^2+15 I_(i,j)X(15+X)=0.         (8)
```

No zero denominator is lost: `s,15+s` lie outside zero because
`s notin F_p`, and the nonzero second color moment then forces `z!=0`.

The constant coefficient of `P_s` is

```text
b_15(s)=binom(s+14,15).                              (9)
```

The product of the 15 roots is `-b_15(s)`. Since every root belongs to
`mu_n` and `n` is even, cyclotomic divisibility supplies the independent
necessary condition

```text
b_15(s)^n=1.                                         (10)
```

Here `p=8191=-1 mod 16`, so `F_p(mu_16)=F_(p^2)`. The primary exact
certificate presents this field as

```text
F_p[z]/(z^2-128z+1)
```

and uses the verified primitive sixteenth root `5644+923z`. For every one of
the 105 patterns it reduces `(10)` modulo `(8)` and proves

```text
gcd(q_(i,j)(X), b_15(X)^131072-1)=1.                (11)
```

The independent audit uses `F_p[u]/(u^2+2)`, the primitive root
`6456+2822u`, and the Sylvester resultant of `(8)` with the reduced linear
remainder. All 105 resultants have nonzero field norm; their canonical record
digest is

```text
9c05ecd35081cb2eb38869300a434b03e5b440771410ec60427bfca118e9e31f.
```

A common root in any extension would make `(11)` nontrivial. Thus the
single-collision system is empty. The multiplicity conclusion `(MS2)` follows
from the two dependency theorems and the proved `m=8` exclusion. QED.
