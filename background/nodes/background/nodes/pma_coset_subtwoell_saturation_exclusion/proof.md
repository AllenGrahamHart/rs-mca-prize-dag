# Proof - PMA constant-shift-pencil sub-two-ell saturation exclusion

Divide by the common monic locator polynomial `P`. Since
`deg F,deg W<2ell`, there are unique polynomials of degree less than `ell`,

```text
F=F_0+P F_1,       W=W_0+P W_1.
```

For each residue `0<=r<ell`, let

```text
v_r=(f_(0,r),f_(1,r),w_(0,r),w_(1,r)) in K^4
```

be the vector of `X^r` coefficients in `(F_0,F_1,W_0,W_1)`. Reduction
modulo `P-a_i` gives

```text
w_(0,r)+a_i w_(1,r)-c_i f_(0,r)-c_i a_i f_(1,r)=0.
```

Thus every `v_r` lies in the kernel of the matrix whose rows are

```text
R_i=(-c_i,-c_i a_i,1,a_i).                         (1)
```

## 1. Saturation forces rank at most two

If the matrix in (1) had rank at least three, its kernel would have
dimension at most one. It cannot have dimension zero because `F` is nonzero.
Hence all coefficient vectors would be scalar multiples of one vector:

```text
v_r=h_r(A,B,C,D).
```

With `H(X)=sum_r h_r X^r`, this gives

```text
F=H(A+B P),       W=H(C+D P).                      (2)
```

Because `P` is monic and `deg F=d>ell`, equation (2) has `B!=0` and
`deg H=d-ell>=1`. Equation (2) therefore gives a
nonconstant common divisor of `F` and `W`, contradicting `gcd(F,W)=1`.
The row matrix in (1) consequently has rank at most two.

## 2. Rank two forces one constant label

After reordering and changing signs, the rows in (1) are

```text
(1,a_i,c_i,a_i c_i).
```

Take any three distinct quotient labels `a_1,a_2,a_3`. Rank at most two
forces the minors on columns `(1,a,c)` and `(1,a,ac)` to vanish. Therefore
there are affine polynomials satisfying, on these three points,

```text
c_i=A+B a_i,       a_i c_i=C+D a_i.
```

The polynomial

```text
B Z^2+(A-D)Z-C
```

has the three distinct roots `a_1,a_2,a_3`, so it is zero. Hence `B=0`
and the three `c_i` are equal. Applying the same argument to
`(a_1,a_2,a_j)` shows that every `c_j` equals one scalar `c`.

The pairwise-coprime polynomials `P-a_i` now all divide `W-cF`, so their
product divides it. But

```text
deg(W-cF)<=d<2ell<t ell.
```

Therefore `W=cF`. This again contradicts `gcd(F,W)=1`, because `F` has
positive degree. The assumed pair cannot exist.

## 3. PMA interpretation

The theorem applies to every full-petal chart whose locator polynomials are
constant shifts `P-a_i` of one common monic `P`. The proved coset-chart
residue bridge supplies the special case `P=X^ell`, while the exact-defect
saturation theorem supplies `gcd(L_D,W)=1`. In the strict strip and for
`t>=3`, the capped upper condition `d<2ell<=(t-1)ell` is automatic.

No existing theorem says that every below-band carried PMA source has a common
constant-shift locator pencil. This proof supplies no such bridge and is
consumed only evidentially by the universal PMA target.
