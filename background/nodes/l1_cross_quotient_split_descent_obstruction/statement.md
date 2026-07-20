# L1 cross-quotient split-descent obstruction

- **status:** PROVED
- **role:** refute universal recursive split-locator descent in the live tail
- **consumer:** `l1_mixed_petal_amplification`

## Statement

There is an exact saturated maximal-chart cell in the sub-Johnson tail whose
cross-determinant quotient is not split over the base field.

Work over `F_23` with

```text
ell=2,
C={0,1,2,3,4,5,6,7},
B={13},
T_i={(8+i),(14+i)} for 0<=i<5,
X={8,9,10,11,12},
(c_0,...,c_4)=(1,2,4,3,8).                              (SQ1)
```

The two exact saturated pairs are

```text
D_0={0,1,5,7},
F_0=11X+X^2+10X^3+X^4,
W_0=20+5X+19X^2+13X^3+5X^4,

D_1={2,3,4,6},
F_1=6+4X+11X^2+8X^3+X^4,
W_1=3+9X+16X^2+2X^3+13X^4.                              (SQ2)
```

Both have exactly the five singleton petal agreements `X`, the background
agreement `13`, and four retained-core agreements. Thus their total agreement
is `10=k+ell-1`. Nevertheless

```text
(W_0F_1-W_1F_0)/L_X
 =16+9X+4X^2+15X^3
 =(X-13)(20+15X+15X^2),                                 (SQ3)
```

and the quadratic factor has discriminant `14`, a nonsquare in `F_23`.
Hence the quotient has only the forced background root and is not a split
polynomial. Here `N=8,d=4,h=5`, so

```text
N(2d-h)=24>=d^2=16;                                     (SQ4)
```

the witness lies in the exact nonpositive-Johnson tail.

## Consequence

A proof may use the cross quotient as an injective coordinate, but it may not
recursively reinterpret every quotient as a smaller split defect locator.
Such a descent needs an additional splitting theorem or a different owner.
