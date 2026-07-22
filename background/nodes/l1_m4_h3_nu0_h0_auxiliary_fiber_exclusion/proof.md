# Proof - L1 m=4, h=3, nu=0, h=0 auxiliary-fiber exclusion

The surviving projective branch satisfies

```text
9B=4A^2+6A.
```

The tangent value and the third root of the auxiliary cubic
`Hg(Y)-4alpha Y` are therefore

```text
tau=-3B/(2A)=-(2A+3)/3,       sigma=-1-tau=2A/3.      (1)
```

The pinned value `H=4alpha/(Cr^2)` makes that cubic proportional to

```text
(Y-r)(Y-tau r)(Y-sigma r).
```

Since `2aY+3b=2a(Y-tau r)`, cancellation in the Euler identity gives

```text
DXR'=(H/(2a))(R-r)(R-sigma r).                        (2)
```

The table packets have `sigma!=1`. Let `rho_1,rho_2` be the numbers of
distinct roots of `R-r` and `R-sigma r`. Every root multiplicity is less
than `p`; otherwise one of these monic degree-`p` polynomials would be a
`p`th power and (2) would force `R'=0`.

At a nonzero root of `R-r` having multiplicity `e`, the two sides of (2)
have orders `e-1+d` and `e`, where `d in {0,1}` is its multiplicity in the
squarefree polynomial `D`. Hence `d=1`. The same comparison applies at every
root of `R-sigma r`; none is zero because `sigma!=1`. Thus `D` contains the
disjoint union of all `rho_1-1` nonzero roots of the first fiber and all
`rho_2` roots of the second.

On the other hand,

```text
deg gcd(R-r,R')=p-rho_1,
deg gcd(R-sigma r,R')=p-rho_2.
```

The two gcds are coprime and their product divides `R'`. Since the exact
Euler degree is `deg R'=p-5`,

```text
rho_1+rho_2>=p+5.                                     (3)
```

Using `deg D=p+4` and the root containment gives

```text
p+4=deg D>=rho_1-1+rho_2>=p+4.
```

Equality holds throughout. Both sides of `(AFE2)` are monic, proving the
exact auxiliary-fiber factorization.

Every root of `D`, and every root of each split fiber `R-beta_i`, lies in the
same domain coset `cK`. The product of the `p` roots of `R-sigma r`, counted
with multiplicity, is `(sigma-1)r`. The corresponding product for
`R-beta_i` is `beta_i-r=rx_i`. Both products lie in `c^pK`, so

```text
(sigma-1)/x_i in K,       x_i/(sigma-1) in K.         (4)
```

The shifted-value polynomial is

```text
L(X)=X^3+3X^2+(A+3)X+C.
```

Therefore `(4)` is exactly the divisibility `(AFE3)` by `W^n-1`.

For the exceptional packet, exact arithmetic in `F_p[W]/(P_A)` gives the
coefficients and nonzero constant remainder in `(AFE4)`. Hence `(AFE3)`
fails and the exceptional packet cannot lift. The dependency already
excludes `(A,B)=(6,20)`, so no constant-eliminant packet remains.
