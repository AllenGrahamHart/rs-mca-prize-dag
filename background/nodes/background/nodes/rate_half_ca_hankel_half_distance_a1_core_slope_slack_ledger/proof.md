# Proof

## 1. Strip the fixed core

The half-distance `A=1` matrix has

```text
R-r=4m rows,       r+1=4m+1 columns,
generic rank rho=4m.                                   (1)
```

Its rational right kernel is one-dimensional. The two-sided minimal-index
theorem identifies it with the degree-`rho` apolar generator `Q` and says
that its unique right singular block is `L_e`. The homogeneous kernel vector
of `L_e` has `e+1` independent parameter coefficient vectors. Constant
Kronecker equivalence preserves their independence, so the coefficient forms
of `Q` are independent.

The exceptional-root theorem proves that a live degree has one of the three
core ranges `(A1L3)` and that the fixed factors in `H` are simple. Multiplying
by `H` is injective, so independence of the coefficients of `Q=H Qbar`
implies independence of those of `Qbar`. This gives the rational-normal
claim. No point of `D\S` is a fixed root of `Qbar`, and `N-s>d`, so evaluation
on `D\S` is injective on degree-at-most-`d` forms.

## 2. Residual root charge and Euclidean cap

Contracting by `H` gives the residual pencil from the exceptional-root
theorem. Its generic rank is `d`, its nullity sum is `1+s`, and its regular
Kronecker size is

```text
Delta=d-(1+s)e.                                        (2)
```

At a supported slope, use the notation of the contracted-root proof: if the
original rank loss is `c_gamma` and `j_gamma` fixed factors disappear from
the specialized minimal generator, then `Qbar_gamma` has at least
`d-c_gamma+j_gamma` distinct roots in `D\S`, while the residual rank loss
satisfies `cbar_gamma>=c_gamma-j_gamma`. It therefore has at least
`d-cbar_gamma` such roots. Local Smith multiplicities give

```text
sum_gamma cbar_gamma<=Delta.
```

This proves the omission bound in `(A1L6)`. Since every nonzero degree-`e`
form `Qbar(U,V;x)` has at most `e` distinct finite roots,

```text
T*d-O=I<= (N-s)e.                                      (3)
```

Combining `(2),(3)` gives `T*d<=L`, hence `T<=T_max`.

For the explicit division, use `N=4rho` and `d=rho-s`:

```text
L=d+(N-1-2s)e=(4e+1)d+(2s-1)e.                        (4)
```

For `s=0`, division of the last term `-e` gives `(4e,d-e)`. For `s=1`,
`e<d` gives `(4e+1,e)`. For `s=2`, the residual constraint `3e<=d` gives
the last two rows of `(A1L5)`. A failure has `T>=rho+2`, proving `(A1L7)`.

Substitute `T=T_max-ell` and

```text
(N-s)e=T_max*d+eta-Delta
```

into the definition of `C`. This gives `(A1L8)`. Every nonsaturated residual
row contributes at least one to `C`, proving `(A1L9)`.

If `cbar_gamma=0`, the residual factor constructed in the contracted-root
proof has degree `d`, divides `Qbar_gamma`, and is squarefree and split over
`D\S`. It therefore equals `Qbar_gamma`. The simple fixed core is disjoint
from those roots, so `Q_gamma=H Qbar_gamma` is a split degree-`rho` locator.
At most `Delta` supported slopes have positive residual rank loss, proving
the clean-column count.

## 3. Residual product-code word

Every row and column of `W` is nonzero. In a failing profile
`T>=rho+2>e`, so evaluation on `Z` is injective through degree `e`.
Coefficient independence and injective evaluation on `D\S` give

```text
rank W=e+1.
```

The zero entries are exactly the `I` residual root incidences. Therefore

```text
wt(W)=(N-s)T-I=T((N-s)-d)+O=(N-s)(T-e)+C,
```

and `(N-s)-d=N-rho`, proving `(A1L11)`.

## 4. Sharp-cap norm and complementary factors

Assume `ell=0`. Each of the `ubar_gamma` distinct residual root incidences
contributes a factor `L_gamma` to `Rbar`. Hence

```text
Rbar=(product_gamma L_gamma^ubar_gamma)Sbar.
```

The residual degree is `C`, and `(A1L8)` with `O<=Delta` gives `C<=eta`.
Multiplication by `J` proves `(A1L12)`.

At a saturated residual row, `Qbar(U,V;x)` has `e` distinct roots in `Z`, so
it divides the squarefree form `P` of degree `T_max`. Interpolate the
coefficients of

```text
V_x=P/Qbar(U,V;x)
```

over the saturated rows. This produces `Vbar` with the degrees in `(A1L13)`.
The biform `Qbar Vbar-P` vanishes on `D_sat`, so it is divisible by `P_sat`;
the quotient has the stated parameter degree and `X`-degree at most `d-1`.

## 5. Component chambers

Factor `Qbar` over the algebraic closure, with multiplicity. A component of
parameter degree zero would be a fixed `X`-factor. At a clean supported slope
it would split over `D\S`, contradicting maximality of the stripped core.
An `X`-degree-zero component would contradict parameter primitivity. Thus all
`r_i,e_i` are positive.

Let `I_i` count distinct zeros of `Q_i` on `(D\S) x Z`, and put

```text
D_i=T_max*r_i-I_i,       C_i=(N-s)e_i-I_i,
E=sum_i I_i-I.
```

Grid-line Bezout makes both deficits nonnegative. Incidence accounting gives

```text
sum_i D_i=O-E<=Delta,       sum_i C_i=C-E<=eta.         (5)
```

Since `N-s=4d+3s`, `T_max=4e+beta`, and `r_i=4e_i-a_i`, direct subtraction
gives

```text
C_i-D_i=T_max*a_i-lambda*e_i.                          (6)
```

If `a_i<0`, the right side of `(6)` is less than `-T_max<-Delta`,
contradicting `(5)`. Thus `a_i>=0`, and summing its definition gives
`sum_i a_i=4e-d=g`. Bounds `(5),(6)` give `(A1L15)`.

Both `Delta` and `eta` are less than `d<T_max`, so the chamber width is less
than two. For `s=1`, `Delta+eta=d-e<T_max`; for `s=2` it is either `d` or
zero, again below `T_max`. For `s=0` it is `2(d-e)`, which is below `T_max=4e`
when `d<3e`. This proves the chamber assertions.

Finally set `e=m+1`. The table `(A1L5)` gives maximum slacks `2,3,3`.
Substitution into `(A1L9)` gives `5m+1,3m+1,m+1`, respectively. The minimum
clean count `T-Delta` occurs at `T=rho+2` and gives `m+3,2m+5,3m+7`.
This proves `(A1L16)` and completes the proof. QED.
