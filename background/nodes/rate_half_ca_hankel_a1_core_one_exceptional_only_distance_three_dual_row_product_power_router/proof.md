# Proof

For every active outside row `x`, saturation says that the parameter
polynomial `Q_x(z)=Q(z;x)` vanishes at exactly the `e` external slopes whose
blocks contain `x`. These roots are distinct. Since `deg Q_x<=e`, its degree
is exactly `e`, its leading coefficient `l_x` is nonzero, and

```text
Q_x(z)=l_x product_(gamma in Z_x)(z-gamma).           (1)
```

Every external block has `r=2e+1` active roots. Multiplying `(1)` over the
`6e+3` roots of `C` therefore makes every root of `P_Z` occur exactly `r`
times. Both sides have degree

```text
e(6e+3)=3er=r(3e),
```

and comparison of leading coefficients proves `(DRP2)`.

The pair-Lagrange normalization gives

```text
Q(0;X)=A(X),
Q(xi_i;X)=lambda_i B(X)A(X)/D_i(X).                  (2)
```

The active rows are disjoint from the roots of `A`, `B`, and `D_i`, while
the external slopes are distinct from `0` and `xi_i`. Hence every factor in
the following quotient is nonzero. Divide `(DRP2)` at `z=xi_i` by the same
identity at `z=0` and use `(2)`:

```text
lambda_i^(6e+3) product_(C(x)=0) B(x)/D_i(x)
 = (P_Z(xi_i)/P_Z(0))^r.                             (3)
```

Since `6e+3=3r`, rearranging `(3)` proves `(DRP3)` and hence `(DRP4)`.

For monic polynomials, the definition of the resultant gives

```text
product_(C(x)=0) B(x)=Res(C,B),
product_(C(x)=0) D_i(x)=Res(C,D_i).                  (4)
```

Now `deg C=6e+3` is odd, `deg B=3`, and `deg D_i=2`. Resultant reciprocity
turns `(4)` into

```text
Res(C,B)=-product_(t in T)C(t),
Res(C,D_i)=C(a_i)C(b_i),                              (5)
```

which proves `(DRP5)`. Differentiating `P_X=ABC` at a simple root of `B` or
`A` gives the first two formulas in `(DRP6)`. The final formula is the smooth
multiplicative-domain derivative identity from the dependency.

The multiplicative group of a finite field is cyclic. The image of the
`r`th-power map has index `g_r=gcd(r,q-1)` and is the kernel of
exponentiation by `(q-1)/g_r`; this proves `(DRP7)`. Direct multiplication
gives `(DRP8)`, and `gcd(e,2e+1)=1`. QED.
