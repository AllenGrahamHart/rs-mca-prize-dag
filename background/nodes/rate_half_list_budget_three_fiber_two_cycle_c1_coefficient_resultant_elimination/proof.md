# Proof

Give `A,S` weight one and `P` weight two. Inspection of `(MTR6)`
shows

```text
wt(X)=wt(Y)=wt(F_0)=2,       wt(E_0)=3,
wt(J_even)=wt(I_even)=6,     wt(J_odd)=wt(I_odd)=5.
```

Consequently `K_0` and `K_1` have weights six and five, and
`N=K_0^2-PK_1^2` is weighted homogeneous of weight twelve. A monomial
`A^aS^bP^c` in `N` therefore has

```text
a+b+2c=12,       0<=c<=6.                            (1)
```

Substitute `S=e_1-A-C` and `P=e_4/(AC)`. Multiplication by
`(AC)^6` clears every denominator. By `(1)`, the degree in either
`A` or `C` is at most

```text
6-c+a+b=18-3c<=18.                                   (2)
```

This proves the polynomial and degree assertion for `Nhat`.

Now specialize `A` to a root of `D_*`. Since `D_*` is monic and
squarefree, `H(A,C)` is the monic cubic

```text
D_*(C)/(C-A)=product_(C_0 in Omega\{A})(C-C_0).      (3)
```

The root-product formula for the inner resultant gives

```text
Res_C(H(A,C),Nhat(A,C))
 =product_(C in Omega\{A}) Nhat(A,C).                (4)
```

Applying the same formula to the monic outer polynomial `D_*(A)` yields

```text
R_1=product_(A,C in Omega, A!=C) Nhat(A,C).           (5)
```

For an ordered pair of distinct roots, its complementary roots are exactly
`{B,D}`, so

```text
S=e_1-A-C=B+D,       P=e_4/(AC)=BD.                   (6)
```

Equations `(C1R2)` and `(6)` turn `(5)` into the product in
`(C1R6)`. Across all twelve ordered pairs, each root occurs three times
as `A` and three times as `C`. Hence

```text
product_(A!=C)(AC)^6=e_4^36.                          (7)
```

This factor is nonzero. Therefore `R_1=0` exactly when one of the twelve
norms vanishes. The dependency proves that this is exactly passage of one of
the 24 original lift-sign invariant tests. QED.

