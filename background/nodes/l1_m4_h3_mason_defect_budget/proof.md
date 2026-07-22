# Proof - L1 m=4, h=3 Mason defect budget

The three complete fibers occupy `3p` domain points. Their monic product has
the squarefree complement `D` of degree

```text
u=4(p+1)-3p=p+4.
```

Translation of the inner polynomial depresses the monic outer cubic, giving
`(MDB2)`. Its three roots are distinct. The maximum-value complement theorem
also proves that the Frobenius-degenerate arm of the associated polynomial
abc triple is impossible when `h<m`: here `u=p+4>p`.

Move the lower two outer terms to the second summand:

```text
R^3D+((aR+b)D+alpha)=X^n.                              (1)
```

Because `D(0)!=0`, the first term has exact valuation `3nu`. Since
`3nu<3p<n`, the second term has the same valuation. Dividing (1) by
`X^(3nu)` gives

```text
U^3D+B_0=X^(n-3nu).                                    (2)
```

The three terms are pairwise coprime. A common nonzero root would divide the
monomial on the right, while exact valuation removes zero. The excluded
Frobenius arm says that (2) is not entirely in `F[X^p]`, so polynomial
Mason--Stothers applies.

We first retain the Wronskian rather than only its degree. Put

```text
L=n-3nu,       A=U^3D,       W=A'B_0-AB_0'.             (3)
```

Since `A+B_0=X^L`,

```text
W=A'X^L-A(X^L)'
 =X^(L-1) U^2 (3X U'D+X U D'-LUD).                    (4)
```

The Wronskian is nonzero. Otherwise `(A/B_0)'=0`; coprimality over the
perfect algebraic closure would make `A` and `B_0`, and hence their sum,
scalar `p`th powers. That is exactly the excluded Frobenius-degenerate arm.
Call the final factor in (4) `H`; thus `H!=0`.

If `a=0`, distinctness of the cubic roots gives `b!=0` and
`deg B_0=u-3nu`. Comparing the degree of (4) with
`deg W<=L+deg(B_0)-1` would give

```text
deg H<=u-2p-nu=4-p-nu<0,
```

contradicting `H!=0`. Hence `a!=0`, proving `(MDB3)`. Equivalently, direct
Mason--Stothers in this case would require `p-4+nu<=0`.

Now `aRD` is the unique leading term of `(aR+b)D+alpha`, so

```text
deg B_0=p+u-3nu=2p+4-3nu.                              (5)
```

The same Wronskian degree comparison now gives

```text
deg H<=deg(B_0)-2deg(U)=u-p-nu=4-nu.                  (6)
```

Since `H` is nonzero, this proves `nu<=4` and `(MDB5)`.

The definitions in `(MDB6)` give the exact radical degrees

```text
deg rad(U^3D)=p-nu+u-delta_A,
deg rad(B_0)=p+u-3nu-delta_B.                          (7)
```

The monomial contributes one radical root and the `-1` in the Mason bound
cancels it. Substituting (7) into that bound yields

```text
4p+4-3nu
 <= (2p+4-nu-delta_A)+(2p+4-3nu-delta_B).
```

Therefore

```text
delta_A+delta_B<=4-nu.                                 (8)
```

Both defects are nonnegative, so (8) proves `(MDB7)`. When `nu=4`, (6)
makes `H` constant and nonzero, and both defects vanish. Since `D` is already squarefree,
`delta_A=0` says that `U` is squarefree and shares no root with `D`, while
`delta_B=0` says that `B_0` is squarefree. The remaining case statements
follow directly from the integer budget.
