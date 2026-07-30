# Proof

## 1. Degree-six companion

Use the BelyiDB map `phi=N/D` with

```text
N=(625/624)x^6,

D=x^6-(16/715)x^5-(192/1573)x^4-(16384/51909)x^3
  -(65536/190333)x^2+67108864/345454395.
```

Direct factorization gives

```text
D=(11x-8)^2
  (2854995x^4+4088832x^3+4088832x^2+2883584x+1048576)
  /345454395,

N-D=(11x+32)^5(55x-32)/5527270320.
```

Thus the natural degree-six branch profiles are `6`, `5.1`, and
`2.1.1.1.1`.

## 2. Unordered-pair curve

An unordered pair of roots is represented by

```text
q(X)=X^2-yX+z.
```

Write the remainders modulo `q` as

```text
N=N0+N1 X,       D=D0+D1 X.
```

The quadratic divides `N-tD` exactly when the two remainder vectors are
proportional. Their determinant is the irreducible quintic

```text
C(y,z)=
-4194304y^5+7434240y^3z^2+16777216y^3z+6814720y^2z^3
+2635380yz^4-14868480yz^3-12582912yz^2
+483153z^5-6814720z^4.                              (1)
```

The generic fiber consists of the 15 unordered pairs of six roots.

Project from the triple point `(0,0)` by writing `z=my`. After removing the
fixed factor `y^3`, equation `(1)` is quadratic in `y`, with discriminant

```text
2^20 m^2(11m+16)^4(3025m^2-2816m+1024).             (2)
```

The remaining conic has rational point `(m,w)=(0,32)`. Its line
parametrization is

```text
m=-64(u+44)/((u-55)(u+55)),
w=-32(u^2+88u+3025)/((u-55)(u+55)).                  (3)
```

Substitution into the quadratic formula gives

```text
y=-192(u-55)(u+44)(u+55)^2/E(u),
z=12288(u+44)^2(u+55)/E(u),

E=u^5+55u^4-9680u^3-425920u^2+28623155u+1257325157.
                                                                    (4)
```

Equations `(3)`--`(4)` satisfy both the conic and `C(y,z)=0` identically.
Conversely, away from the finitely many projection exceptions, `m=z/y` and
the quadratic square root recover `u`; hence this is the normalization of
the pair curve.

## 3. Degree-15 map and branch fibers

On the determinant curve, `t=N0/D0=N1/D1`. Substituting `(4)` and cancelling
gives `(KBM4-1)`. Direct subtraction gives `(KBM4-2)`.

The numerator has finite zeros of orders six and three and a zero of order
six at infinity. The numerator-minus-denominator has three distinct roots,
all of order five. Finally `Q4`, `Q6`, and `u+143` are squarefree and pairwise
coprime, so the pole profile is four double roots and seven simple roots.
The three branch indices are `12,12,4`, whose sum `28=2*15-2` proves that
there is no additional branch value.

The degree-six companion has monodromy `S6` in its natural action. Passing to
unordered pairs gives its transitive degree-15 two-subset action, exactly the
retained passport of the parent theorem.

## 4. Challenge-field pole descent

For the target transform `F=T/(T-1)`, the pole points are the roots of

```text
(u+77)(u^2-44u-4961).
```

The quadratic discriminant is

```text
21780=66^2*5.
```

Let `p=2130706433`. In every even extension of `F_p`, every nonzero base-field
element is a square: `(p^6-1)/(p-1)=1+p+...+p^5` is even, so Euler's exponent
is a multiple of `p-1`. The characteristic divides none of `2,3,5,11`.
Consequently the three displayed points are distinct and lie in `F_(p^6)`.

This proves the normal form and pole descent. It does not supply the fixed
active fiber or the quartic source-star incidence.
