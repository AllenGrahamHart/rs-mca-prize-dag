# Proof - L1 m=4, h=3, nu=0, h=0 projective quarter certificate

The three monic degree-`p` fiber locators are `R-beta_i`. Their root products
are `lambda_i=beta_i-r`. All roots lie in one multiplicative domain coset, so
the ratios of these products lie in the order-`n=4(p+1)` subgroup `K`. The
domain identity at zero makes every `lambda_i` nonzero; squarefreeness of the
outer cubic makes them distinct. Since `beta_1+beta_2+beta_3=0`,

```text
lambda_1(1+u+v)=-3r,
```

so `s=1+u+v` is nonzero and `lambda_1=-3r/s`.

The other two elementary symmetric identities give

```text
a=-3r^2+lambda_1^2q,
-b=-2r^3+r lambda_1^2q+lambda_1^3uv.
```

Dividing by the indicated powers of `r` proves the first two equations in
`(PQC3)`. The dependency proves

```text
B=2A(2A+3)/9.
```

Substitution and clearing `s^4` turns this relation into

```text
E(u,v):=q(4q-s^2)-3uvs=0,                            (1)
```

which proves the last equation in `(PQC3)`.

Put `N=p+1`. For `w in K`, the quarter `theta=w^N` lies in `mu_4` and

```text
w^p=theta/w.                                          (2)
```

Thus every solution of (1) with quarters `(epsilon,eta)` also satisfies

```text
u^3v^3 E(epsilon/u,eta/v)=0.                          (3)
```

For each of the 16 quarter pairs, the checked-in exact certificate eliminates
`v` between (1) and (3), saturates the forbidden factor `u=0`, and computes
the complete gcd of the resultant with `u^N-epsilon` over `F_(p^2)`. The
nonconstant gcds are exactly

```text
(epsilon,eta)       all p                         p=2147483647 addition
(1,1)               U^4-1                        none
(1,-1)              U+1                          U^2-830673015U+1
(1,+/-i)            U^2+1                        none
(-1,1)              none                         U^2-241623698U-1
(-1,-1)             none                         U^2+241623698U-1.            (4)
```

Every omitted quarter pair has gcd one. For the four constant roots, direct
factorization of `E(u,V)` resolves every `v`:

```text
E(1,V)=-2V(V-1)^2,
E(-1,V)=4(V-i)(V+i),
E(i,V)=(-1-i)(V+1)(V+i)(V-1-i),
E(-i,V)=(-1+i)(V+1)(V-i)(V-1+i).                    (5)
```

After deleting zero, repeated, and `s=0` packets, reconstruction by `(PQC3)`
gives only `(A,B)=(6,20)`. On the largest characteristic, exact arithmetic in
each of the three quadratic quotient fields in (4) gives a unique common
`v` and the same additional pair

```text
(A,B)=(844833809,2002167159).                         (6)
```

The checker independently verifies `u^N=epsilon`, `v^N=eta`, all
nondegeneracy conditions, and reconstruction for each quadratic packet.
Equations (4)--(6) therefore prove the complete table `(PQC4)`.

Finally, under the normalization `Y=r(X+1)`, the outer cubic becomes

```text
X^3+3X^2+(3+A)X+(1+A+B).
```

Substituting `(A,B)=(6,20)` gives `(PQC5)`.
