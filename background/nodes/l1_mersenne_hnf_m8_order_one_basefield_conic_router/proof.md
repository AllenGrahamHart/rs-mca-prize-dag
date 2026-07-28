# Proof - L1 Mersenne HNF m=8 order-one base-field conic router

Every official `m=8` characteristic is

```text
p=2^q-1,       q in {13,17,19,31}.                    (1)
```

Thus `p=7 mod 8` and `p=1 mod 3`.

First take `z=-1`. The pullback equation is `c^2+c+1=0`. Since
`p=1 mod 3`, both nontrivial cube roots lie in `F_p`, so `c in F_p`. The
conic gives `w=+/-6`, and (BCR1) plus (OCR5) gives

```text
theta=(w-11z-5)/5=(w+6)/5 in F_p.                    (2)
```

This contradicts the shifted-value gate, which requires at least one of
`c,theta` to lie outside `F_p`. For `w=-6`, it also contradicts
`A_HNF!=0`. Hence both exceptional affine points are empty.

Now suppose `t in F_p` on the remaining chart. The rational formulas (OCR7)
give `z,w in F_p`, hence `theta in F_p`. The same shifted-value gate forces
`c notin F_p`. Since `c` satisfies `X^2-zX+1`, its other root is `c^(-1)`
and therefore

```text
c^p=c^(-1).                                           (3)
```

The order-one Frobenius gate also gives

```text
c^p=1+zeta/(c-1),       zeta=(c-1)^(p+1),
zeta^8=1.                                               (4)
```

Comparing (3) and (4) yields

```text
zeta=(c-1)(c^(-1)-1)=-(c-1)^2/c=2-z.                 (5)
```

Because `c` is quadratic, `(c-1)^(p+1)` is a prime-field norm, so
`zeta in F_p`. But `gcd(8,p-1)=2`; hence `zeta=+/-1`. If `zeta=1`, then
`z=1` and `c^2-c+1=0`. This polynomial splits in `F_p` because
`p=1 mod 3`, contradicting `c notin F_p`. Therefore `zeta=-1` and `z=3`.

Substitution in the conic gives `7w^2=5308`, and (OCR5) gives
`theta=(w-38)/5`. Equation (3) becomes `c^p=3-c`. Finally

```text
rho^p
 =theta/(c^p-1)
 =theta/(c^(-1)-1)
 =-c*theta/(c-1)
 =-c*rho,                                              (6)
```

which proves all identities in (BCR2).

The discriminant of `c^2-3c+1` is five. By quadratic reciprocity,
`5` is a square modulo `p` exactly when `p=+/-1 mod 5`. Since the order of
two modulo five is four,

```text
q=13,17:  p=1 mod 5,
q=19,31:  p=2 mod 5.                                  (7)
```

Thus the quadratic splits, contradicting `c notin F_p`, on the first two
rows. It is irreducible on the last two, where the conic equation leaves at
most two values of `w`. Since `z=3`, the line definition gives
`t=(w-6)/(z+1)=(w-6)/4`. This proves (BCR3)--(BCR4) and the stated finite
router without asserting later acceptance. QED.
