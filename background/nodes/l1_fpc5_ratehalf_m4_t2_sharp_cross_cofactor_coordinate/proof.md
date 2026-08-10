# Proof: sharp cross-cofactor coordinate

Every pair in the guarded slice satisfies

```text
c_2L_1A'_1 == c_1L_2A'_2  (mod L_0),                 (1)
```

and the anchor satisfies the same congruence. The petal locators and labels
are units modulo `L_0`, so there is one unit

```text
mu=c_2L_1/(c_1L_2) mod L_0
```

with `A'_2=mu A'_1` and `A_2=mu A_1` modulo `L_0`. Hence
`Delta_A=0 mod L_0`. Since both cofactors have degree at most `ell-3`,
`deg Delta_A<=2ell-6` and division gives `deg E<=ell-3`.

The guarded vector slice has dimension `ell-1`. Its nonempty monic
degree-`2ell-3` chart `M` is therefore an affine space of dimension
`ell-2`, equal to the dimension of `K[X]_(<=ell-3)`. The map in `(CC2)` is
affine linear and sends the anchor to zero.

It remains to prove injectivity. Suppose two points of `M` have the same
`E`. Subtract their cofactor pairs and call the difference `(B_1,B_2)`.
Then

```text
A_1B_2-B_1A_2=0.                                      (2)
```

The anchor is primitive, so `gcd(A_1,A_2)=1`. Unique factorization in
`K[X]` gives `(B_1,B_2)=T(A_1,A_2)` for some polynomial `T`. The cofactor
formula is linear, hence the corresponding locator difference is `TF_0`.
Both original locators are monic of degree `2ell-3`, so their difference has
degree at most `2ell-4`. If `T!=0`, the monic degree-`2ell-3` polynomial
`F_0` makes `deg(TF_0)>=2ell-3`, a contradiction. Thus `T=0` and the two
points coincide. Equal affine dimensions now prove the bijection.

For `(CC3)`, let `x` be a root of `F_0`. It lies in the core, so
`L_0(x),L_1(x),L_2(x)` are nonzero. The anchor vector
`(A_1(x),A_2(x))` is nonzero by primitivity and lies in the one-dimensional
kernel of

```text
(u,v) -> L_1(x)u-L_2(x)v,                             (3)
```

because `F_0(x)=0`. Since `L_0(x)!=0`, the equation `E(x)=0` is equivalent
to the determinant of the anchor vector and
`(A'_1(x),A'_2(x))` being zero. This holds exactly when the second vector
also lies in the kernel in `(3)`, which is exactly `F(x)=0`. Therefore `E`
and `F` have the same roots on `Z(F_0)`. The anchor locator is squarefree,
so their monic gcds with `F_0` are equal. The bijection shows `E=0` only at
the anchor; hence a distinct contributor has `E!=0` and
`deg gcd(E,F_0)<=ell-3`. This proves `(CC3)--(CC4)`. QED.
