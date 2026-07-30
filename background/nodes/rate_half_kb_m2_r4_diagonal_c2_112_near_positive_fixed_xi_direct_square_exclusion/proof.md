# Proof

Put `q(T)=(T-c)(T-d)`, `a=xi=2`, and `w=1/c`. The positive odd part is

```text
V=(cd-w)+(1-wcd)T-(c+d)(1-w)Y,
```

in the reciprocal basis used by the parent reconstruction theorem. The
incidence coordinate is

```text
z=-N/H,
H=4c^2d-2c^2-3cd+3c+2d-4.
```

The finite affine chart has `H!=0`. Solve the five exact reconstruction rows
directly for the five coefficients of `U`; its determinant is

```text
3(c-2)^2(c-1)^5(c+1)^5(2c-1)^2(d-2)^2(2d-1)^2
 (cd-1)^2(5cd-4c-4d+5) / (c^4 H^6).              (1)
```

Every factor in `(1)` is nonzero for an admissible finite-chart candidate.
In particular, `5cd-4c-4d+5=0` gives `z=1` after excluding `c=1`.

At each root `r` of `q`, both `U(r,W)` and `V(r,W)` vanish at `W=w`.
Divide `U(r,W)^2-WV(r,W)^2` by `(W-w)^2` and call its coefficients
`A_r W^2+B_r W+C_r`. The direct-square allocation `(KBNDS-1)` is equivalent
to

```text
C_c-(1/2)^2 A_c=0,        B_c+2(1/2)A_c=0,
C_d-(1/d)^2 A_d=0,        B_d+2(1/d)A_d=0.         (2)
```

After clearing only chart-nonzero denominators, each first equation in `(2)`
is `H^2` times two primitive lines in `b`. Choose one line at each endpoint.
Their `b`-resultant has exactly the three excluded factors

```text
c-1,        cd-1,        5cd-4c-4d+5
```

and one residual bidegree `(3,3)` curve `C_ij(c,d)`.

On the open part where the full coefficient of `b` in the chosen left line
is nonzero, solve that line for the rational function `b(c,d)`. Substitute
it in the two middle equations in `(2)`, obtaining `M_0,M_1`. Exact
elimination of `c` gives the following resultant and gcd degrees:

```text
line pair    deg Res(C_ij,M_0), Res(C_ij,M_1)    deg gcd
(0,0)                       (24,51)                 24
(0,1)                       (24,51)                 20
(1,0)                       (30,51)                 18
(1,1)                       (30,51)                 18.
```

In every case the squarefree gcd is exactly `(KBNDS-2)`. Thus the generic
part has no admissible common zero. This implication uses resultants only in
their necessary direction, so no leading-coefficient specialization is
lost.

It remains to cover the locus where a selected left line is zero as a
polynomial in `b`. If its coefficient and constant are `L_1(c,d)` and
`L_0(c,d)`, respectively, then

```text
Res_c(L_1,L_0) = unit *
 (d-2)^3(d-1)^3(d+1)^2(2d-1)^3(5d-7)
```

for the first line, and the last factor is `53d-55` for the second. At the
only noncollision roots, the gcd in `c` is `5c-1` and `7c+5`, respectively.
These give exactly `(KBNDS-3)`, and direct substitution puts both on the
excluded `z=1` factor. Hence the exceptional loci are inadmissible before
the right line or middle equations are imposed.

Finally, clear rational coefficient denominators and reduce every univariate
resultant and Bezout certificate modulo `p=2130706433`. Their squarefree gcd
supports are unchanged. A common zero over the algebraic closure of `F_p`
would force one of the forbidden factors above, so no solution exists over
`F_(p^6)`. QED.
