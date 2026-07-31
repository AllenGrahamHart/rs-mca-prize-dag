# Proof

Write

```text
U=M^4+6M^2+1,       V=(M^2-1)^2.
```

## Product and q equations

Use the three product rows indexed by `A,+,-`.  Their rank is three under
the actual guards.  The signed maximal-cofactor vector in cell `M2` is

```text
(3bM^2+b-M^2+1,
 -bM^2-3b-M^2+1,
 b(bM^2-b-3M^2-1),
 b(bM^2-b+M^2+3)).                                (1)
```

Pairing `(1)` with the `C` and `BC` product rows gives respectively
`(M-1)E_2` and `-bE_1`, where

```text
E_1=U(bc+1)+V(b+c),
E_2=(M+1)^2(b^2-c^2)+(M-1)^2b(1-c^2).             (2)
```

In cell `M3`, the cofactor vector is

```text
(M^2(bM^2+3b-M^2+1),
 -3bM^2-b-M^2+1,
 bM^2(bM^2-b-M^2-3),
 b(bM^2-b+3M^2+1)).                               (3)
```

The remaining pairings are `M(M-1)E_2` and `-bE_1`, now with

```text
E_1=U(bc+1)-V(b+c),
E_2=(M+1)^2(b^2-c^2)-(M-1)^2b(1-c^2).             (4)
```

All displayed prefactors are actual guards.  Thus `(2)` or `(4)` is
equivalent to all five product minors, including the projective boundary
where the constant denominator coefficient vanishes.  The second squared
weld is

```text
M2: Q=4M^2(c^2+b)^2+c^2(1+b)^2V,
M3: Q=(M^2+1)^2(c^2+b)^2+c^2(1+b)^2V.             (5)
```

## Elimination

Let `I_2=<E_1,E_2,Q>` for `(2),(5)` and `I_3` analogously for `(4),(5)`.
Set

```text
P_4 =M^4+M^3+4M^2+M+1,
P'_4=M^4+2M^3+10M^2+2M+1.
```

Exact integral lexicographic elimination gives

```text
M^2(b+1)(M^2+1)^3 U^2 P_4 P_6 in I_2,
M(b+1)(M^2+1)^3(M^4+1)U^2 P'_4 P_6 in I_3.        (6)
```

The non-`P_6` branches are collision components.  Exact branch bases give

```text
<I_2,U>       contains b(b+1),
<I_2,P_4>     contains (b+1)^2;

<I_3,M^4+1>   contains (b-1)(b+1),
<I_3,U>       contains b(b+1),
<I_3,P'_4>    contains (b+1)^2.                   (7)
```

Actual packets have `M!=0`, `M^2+1!=0`, and `b!=0,+/-1`.  Equations
`(6)--(7)` therefore force `P_6=0` in both cells.

After adjoining `P_6`, the two ideals contain

```text
(b+1)(4b^2+epsilon A b+4),
(b+1)(8c+bD+epsilon E).                           (8)
```

Since `b+1!=0`, this is `(KB43M-3)`.  Conversely, exact reduction modulo
`<P_6,4b^2+epsilon A b+4,8c+bD+epsilon E>` sends `E_1,E_2,Q` to zero for
each sign.  By the cofactor calculation it also sends all five product
minors to zero.  This proves necessity and sufficiency under the guards.

The sextic followed by a genuine quadratic gives at most twelve geometric
points per cell; the equation for `c` is linear because the characteristic
is odd.  Direct substitution proves both `F_41` examples in `(KB43M-4)`
have five distinct labels, three distinct signed pairs, five distinct
products, product rank three, and zero weld residual.

Finally, the first label identity fixes one edge-orbit sign.  In `(5)` all
factors divided before squaring are nonzero under the same guards, and
reversing the `BC` deck assignment changes the remaining sign without
changing a product.  Hence one orientation realizes the unsquared weld and
the product-to-q theorem reconstructs the five common-`K` rows.  Combining
the exact cell atlas with the three dependency classifications gives the
cap 48 and the stated complete common-`K` frontier. QED.
