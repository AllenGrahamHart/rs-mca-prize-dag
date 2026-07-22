# Proof

Work first over an algebraic closure of an odd finite field. Put

```text
B=X^3-X,       R=X^2+1,
c(r)=r(r^2-1)/(r^2+1).                               (1)
```

Avoid the finite set of parameters where a denominator vanishes, `c(r)=0`,
or `B-c(r)R` is not squarefree. Direct division gives

```text
B-c(r)R=(X-r)D_r,
D_r=X^2+[2r/(r^2+1)]X+(r^2-1)/(r^2+1).              (2)
```

Choose `e` parameters for which the nonzero values `c_i=c(r_i)` are
distinct. Distinct fibers of `B/R` are disjoint because `gcd(B,R)=1`.
Consequently the quadratic factors `D_i=D_(r_i)` are squarefree and pairwise
coprime, and none meets the roots of `B`. All finitely many roots and
coefficients lie in one finite extension of the base field, so after that
extension every polynomial is split.

Write `D_i=X^2-s_iX+p_i`. Formula `(2)` gives

```text
s_i=-2r_i/(r_i^2+1),       p_i=(r_i^2-1)/(r_i^2+1),
s_i^2+p_i^2=1.                                     (3)
```

The conic in `(3)` is nondegenerate. Choose three noncollinear points on it
and then any further admissible points. The coefficient vectors
`(1,-s_i,p_i)` therefore span dimension three, proving `(GSSF2)`.

Put `A=product_i D_i` and use the notation in the statement. The space

```text
S=span({A^2} union
       {A U_i, X A U_i, U_i^2:1<=i<=e})             (4)
```

has dimension `3e+1`. Indeed, divide a relation in the displayed generators
by `A^2` and put `f_i=B/D_i`. At either root of `D_i`, the double-pole term
first forces the coefficient of `f_i^2` to vanish. The two remaining
simple-pole equations then force both coefficients of
`(alpha_i+beta_i X)f_i` to vanish. The constant term vanishes last.

The proof of the quadratic locator-rank gate gives `VV subset S`. We now
exhibit a nonzero functional on `S` that kills every product. Since

```text
B=c_i R+L_iD_i,       L_i=X-r_i,                    (5)
```

define

```text
ell(X A U_i)=1/c_i,
ell(A^2)=ell(A U_i)=ell(U_i^2)=0.                   (6)
```

This is well-defined by the independence just proved. It plainly kills
`U_0^2`, `U_0U_i`, and `U_i^2`. For `i!=j`, subtract the two identities in
`(5)` to obtain

```text
B=[c_i/(c_i-c_j)]L_jD_j
  -[c_j/(c_i-c_j)]L_iD_i.                           (7)
```

Multiplication by `B A^2/(D_iD_j)` expresses `U_iU_j` as the corresponding
linear combination of `A U_i` and `A U_j`. Its two `X A U_*` coefficients
are `c_i/(c_i-c_j)` and `-c_j/(c_i-c_j)`. Applying `(6)` gives zero.
Therefore `VV subset ker ell`, and the nonzero functional `(6)` gives

```text
dim(VV)<=dim S-1=3e.                                (8)
```

This proves `(GSSF3)` for every `e>=3`. QED.
