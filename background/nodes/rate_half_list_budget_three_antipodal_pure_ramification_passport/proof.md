# Proof

Put `A=DU^4` and `B=e_4DV^4`. The pure norm equation says

```text
A+B=Y^d-1.                                             (1)
```

The Euler construction gives

```text
Phi=TU^3=dA-YA',       Phi'=(d-1)A'-YA''.              (2)
```

Using `(1)` to replace `B',B''` in the Wronskian gives

```text
A'B''-A''B'
 =dY^(d-2)((d-1)A'-YA'')
 =dY^(d-2)Phi'
 =dY^(d-2)U^2V^2L.                                    (3)
```

Comparison with the exact factorization in the pure degree-rigidity theorem
proves `Lambda=dL`. The characteristic hypothesis makes `d` nonzero. This
proves `(PRP2)`.

Let `alpha` be a root of `U`. Squarefreeness and coprimality give
`U'(alpha)!=0` and `V(alpha)!=0`. Direct evaluation of the definition of `T`
gives

```text
T(alpha)=-4 alpha D(alpha)U'(alpha).                   (4)
```

Hence `T(alpha)=0` exactly when `alpha` is zero or a root of `D`. Similarly,
at a root `beta` of `V`,

```text
C(beta)=4 beta D(beta)V'(beta),                        (5)
```

which proves the two zero-set identities in `(PRP3)`. The degree-rigidity
theorem allows at most one root of `UV` in `Z(D) union {0}`.

If `alpha` is common to `U,T`, then `Phi=TU^3` has order at least four there.
On the other hand, `(PRP1)` gives

```text
ord_alpha Phi'=2+ord_alpha L,
ord_alpha Phi'=ord_alpha Phi-1.                        (6)
```

All multiplicities are below the characteristic, so the second equality is
exact. It follows that `L(alpha)=0` and `T` has an exact simple root there.
The same argument applied to `Phi+d=e_4V^3C` proves the corresponding claim
for `V,C`. This completes `(PRP3)`.

The numerator and denominator of `R` differ by the nonzero scalar `d`, so
they are coprime. Both have degree `N=4r`; therefore `R` has degree `N`.
In positive characteristic `N<d<char(F)`, while in characteristic zero
separability is automatic. Its fibers above zero and infinity are read
directly from

```text
R=TU^3/(e_4V^3C).                                     (7)
```

The identity

```text
R-1=-d/(Phi+d)                                        (8)
```

shows that `Y=infinity` is the only point above `1`, with ramification index
`N`.

It remains to classify the root `ell` of `L`. First suppose that `ell` is
outside `Z(UV)`. Then `Phi'` has a simple root at `ell`. If
`c=Phi(ell)` is different from `0,-d`, the point has ramification index two
above the fourth value `lambda=c/(c+d)`. The factors `T,C` have no repeated
roots: the Euler router localizes every such root at `ell`, while neither
factor vanishes there. The value `lambda` is also different from `1` because
`d!=0`. This gives `(PRP5)`.

If instead `c=0`, then `T(ell)=0`. Since `U(ell)!=0` and `Phi'` has order
one, `T` has exact order two. This replaces two simple parts above zero by
one part of size two and gives `(PRP7)`. The case `c=-d` is identical with
`V,C` in place of `U,T`, giving `(PRP9)`.

Now suppose `ell` is a root of `U`. The preceding collision calculation
forces a simple root of `T` there. One part of size three and one part of
size one therefore merge into one part of size four, proving `(PRP6)`.
If `ell` is a root of `V`, the same argument proves `(PRP8)`. Coprimality of
`U,V` and the scalar gap between `Phi` and `Phi+d` make the five alternatives
mutually exclusive. They are exhaustive because every finite critical point
is a root of `U`, `V`, or `L`.

For completeness, the generic ramification contributions are

```text
0: 2r,       infinity:2r-2,       1:N-1,       lambda:1.
```

Their sum is `8r-2=2N-2`. Each of the four defect cases absorbs the final
unit contribution into one of the first two fibers, so the same equality
holds. This also independently confirms that no branch value is missing.
In positive characteristic all indices are smaller than the characteristic,
so every profile is tame; characteristic zero is tame automatically. QED.
