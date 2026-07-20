# Proof

The roots of `H_i(X^2)` are invariant under `X |-> -X`. Equation `(F2C2)`
says that its root set is `Z(A_i) union {rho_i}`. Squarefreeness shows that
`rho_i` is not a root of `A_i`, so `-rho_i` is the unique root of `A_i`
whose negative is outside `Z(A_i)`. Evaluating at `rho_i` also gives
`H_i(rho_i^2)=0`. Hence

```text
H_i(Y)=(Y-rho_i^2)G_i(Y),
A_i(X)=(X+rho_i)G_i(X^2),                              (1)
```

with `G_i` monic of degree `s-1`. This proves `(F2C3)`.

The completion roots are distinct. If `rho_i=rho_j` for `i!=j`, equation
`(1)` makes `X+rho_i` divide both `A_i` and `A_j`, contrary to pairwise
coprimality.

Substitute `(1)` in the locator relation. Separating its odd and even
monomial supports and using injectivity of `F[Y] -> F[X]`, `Y |-> X^2`, gives
the two relations `(F2C4)`.

We next classify where the completion roots lie. If `rho_i` belongs to a
different block `Z(A_j)`, then its negative `-rho_i` lies in `Z(A_i)` and not
in `Z(A_j)`. Since `-rho_j` is the unique point of `Z(A_j)` whose negative
is outside that block, one has

```text
rho_i=-rho_j.                                           (2)
```

Conversely `(2)` puts `rho_i=-rho_j` in `Z(A_j)` by `(1)`. Thus cross-block
completion roots occur exactly in antipodal index pairs. Every unpaired
`rho_i` lies in `Z(E)`. After removing those unpaired roots, the remaining
`2c` roots of `E` occur in antipodal pairs: if an exceptional root `e` had
`-e` in a block, the preceding unique-unmatched-point argument would make
`e` one of the completion roots already removed.

Now group the linear factors in

```text
E(X) product_i A_i(X)
 =E(X) product_i(X+rho_i)G_i(X^2).                     (3)
```

An unpaired completion root contributes
`(X-rho_i)(X+rho_i)=Y-rho_i^2`. An antipodal index pair contributes the same
kind of factor from its two `X+rho_i` terms. Each residual exceptional pair
`{e,-e}` contributes `Y-e^2`. There are respectively `4-2c`, `c`, and `c`
such factors, for a total of four. Their quotient-subgroup roots are distinct
because all original domain roots occupy disjoint blocks or the exceptional
set. Their product is the monic squarefree quartic `D_*` described in the
statement. Equations `(F2C1)` and `(3)`, with `Y=X^2`, prove `(F2C5)` and the
more precise inventory `(F2C6)`.

If two `G_i` shared a nonconstant factor `C(Y)`, then `C(X^2)` would divide
the pairwise-coprime locators `A_i,A_j`. Thus the `G_i` are pairwise coprime.
The two coefficient vectors in `(F2C4)` are independent because the
`lambda_i` are nonzero and the `rho_i` are distinct. Hence the `G_i` span at
most two dimensions. A one-dimensional monic span would make all `G_i`
equal; for `s>=2` this contradicts pairwise coprimality. Their span therefore
has dimension two.

Choose a monic `U` and a lower-degree `V` spanning the pencil, and write
`G_i=U+c_iV`. Pairwise coprimality makes the `c_i` distinct. The two relations
in `(F2C4)` make the matrix with columns

```text
(1,rho_i,c_i,rho_i c_i)^T                              (4)
```

singular. Its cross-ratio determinant says that `c_i=T(rho_i)` for one
fractional-linear map `T`. The same base change used in the Mobius-weld
theorem therefore gives independent `R,S` and nonzero `mu_i` with
`G_i=mu_i(R+rho_iS)`. Multiplication and `(F2C5)` give `(F2C7)`.

Any common divisor of `R,S` would divide all four pairwise-coprime `G_i`, so
`gcd(R,S)=1`. Since every `R+rho_iS` has degree `s-1`, the reduced map
`-R/S` has degree `s-1`. This number is odd, while every nontrivial divisor
of the dyadic quotient order `2d=4s` is even. Degree multiplicativity rules
out every nontrivial cyclic or dihedral pullback.

It remains to prove the degree floor with the general quartic `D_*`. Center
the distinct pencil parameters so `sum_i c_i=0`, put `r=s-1`,
`v=deg V`, `h=r-v`, and reverse at infinity:

```text
B(z)=z^rU(z^-1),       C(z)=z^vV(z^-1),
E_*(z)=z^4D_*(z^-1).                                  (5)
```

The product equation has the form

```text
E_*(B^4+e_2z^(2h)B^2C^2+e_3z^(3h)BC^3+e_4z^(4h)C^4)
 =1-z^(2d).                                            (6)
```

Thus `E_*B^4-1` is divisible by `z^(2h)`. Its derivative is

```text
B^3(E_*'B+4E_*B'),
```

and the parenthesized factor has degree at most `r+3`. In characteristic
zero or characteristic greater than `2d`, the usual zero-derivative escape
is impossible because `E_*` has degree four. Therefore

```text
2h-1<=r+3,
v>=ceil((r-4)/2)=ceil((s-5)/2),                       (7)
```

which is `(F2C8)`.

When `c=0`, the quartic is exactly `product_i(Y-rho_i^2)`, so `(F2C9)`
identifies the matched antipodal norm equation and imports its four-coset
exclusion. For `c=1,2`, the explicit factor inventory proves the stated
denominator mismatch.

Finally, on the maximal budget-three row the field-degree collapse gives
extension degree one or two. Since `q>=3*2^128`, the characteristic exceeds
`2^64`, hence exceeds `2d=2^40`. Substitution of `s=2^38` in `(7)` gives
`deg V>=2^37-2`, proving `(F2C10)`. QED.
