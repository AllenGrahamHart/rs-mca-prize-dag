# Proof

Work over the parameter polynomial ring. The infinity theorem and the exact
degrees `deg_X Q=r`, `deg_X B_1=D_0` give

```text
F(t,0)=[X^r]Q=E q_bar,
G(t,0)=[X^D_0]B_1=-j_inf q_bar.                     (1)
```

Consequently the constant term of `C=j_inf F+EG` vanishes, so there is a
unique polynomial `L` with `C=YL`. Comparing the coefficient of `Y` proves
the formula for `Delta_inf=L(t,0)` in `(RRD3)`.

For fixed-degree reversals, the resultant transformation is

```text
Res_Y(F,G)=(-1)^(rD_0)Res_X(Q,B_1).                 (2)
```

Here `r=2e+1` and `D_0=8e+7` are both odd. The unit-resultant theorem and
`(2)` therefore give

```text
Res_Y(F,G)=-c_X q_bar.                              (3)
```

Modulo `F`, the definition of `C` reads `C=EG`. Resultant multiplicativity
and scalar homogeneity yield

```text
Res_Y(F,C)=E^r Res_Y(F,G)=-c_XE^r q_bar.            (4)
```

On the other hand, `C=YL` and `r` is odd, so

```text
Res_Y(F,C)=Res_Y(F,Y)Res_Y(F,L)
          =-F(t,0)Res_Y(F,L)
          =-E q_bar Res_Y(F,L).                     (5)
```

The parameter ring is an integral domain. Cancelling the nonzero polynomial
`-E q_bar` between `(4)` and `(5)` proves `(RRD4)` with the same `c_X`.

It remains to prove `(RRD5)`. Suppose an irreducible parameter polynomial
`f` divides both `q_bar` and `Delta_inf`. Modulo `f`, the polynomials `F`
and `L` then have the common root `Y=0`, because

```text
F(t,0)=E q_bar,       L(t,0)=Delta_inf.
```

Hence `f` divides `Res_Y(F,L)=c_XE^(r-1)`, and therefore `f=E` up to a
nonzero scalar. But at the exceptional slope `E=0`, the fiber
`Q(gamma_0;X)` has exact degree `r-1`. Its leading coefficient is
`q_(r-1)(gamma_0)!=0`, while `j_inf!=0`; thus

```text
Delta_inf mod E=j_inf q_(r-1) mod E !=0.            (6)
```

So `E` does not divide `Delta_inf`, a contradiction. No irreducible common
factor exists, proving `(RRD5)`. QED.
