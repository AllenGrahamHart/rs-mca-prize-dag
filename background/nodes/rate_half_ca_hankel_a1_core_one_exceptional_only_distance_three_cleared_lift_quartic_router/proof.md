# Proof

At an internal slope the calibrated normal form gives

```text
s_xH_x(xi_i)=c_iD_i(x).                                      (1)
```

Differentiate `G_xH_x=P_Z` in `z`. Since
`G_x=Q(z;x)/q_e(x)`, logarithmic differentiation at `xi_i` gives

```text
s_xH_x'(xi_i)
 =c_iD_i(x)
   [rho_i-partial_zQ(xi_i;x)/Q(xi_i;x)].                     (2)
```

The pair-Lagrange internal specialization is

```text
Q(xi_i;X)=lambda_i B(X)A(X)/D_i(X)=lambda_iE_i(X).            (3)
```

On the other hand, differentiating `(CKL5)` and evaluating at `xi_i`
yields

```text
s_xH_x'(xi_i)
 =partial_zR(xi_i;x)+I'(xi_i)J_x(xi_i).                      (4)
```

Substitution of `(2)--(3)` into `(4)` proves

```text
J_x(xi_i)=U_i(x)
 -c_iD_i(x)partial_zQ(xi_i;x)/
   [lambda_iI'(xi_i)E_i(x)]
 =N_i(x)/E_i(x).                                             (5)
```

The degree statements follow directly. The polynomial `E_i` has degree

```text
deg A+deg B-deg D_i=2e+3-2=2e+1.                            (6)
```

Both terms in `U_i` have `X`-degree at most two. Also
`deg_X partial_zQ<=2e+1`, so each term of `N_i` has degree at most
`2e+3`. This proves `(CLQ4)`.

The degree-`e` polynomial `J_x` has leading coefficient `s_x`. Therefore
`J_x-s_xI` has degree less than `e` and takes the values in `(5)` at the
roots of `I`. Lagrange interpolation proves `(CLQ5)`.

Now multiply

```text
R+I [s_XI+sum_i(N_i/E_i)L_i]                         (7)
```

by the common denominator `A B q_e`. Since

```text
s_X=A B/q_e,       (A B)/E_i=D_i,                    (8)
```

the result is exactly `(CLQ6)`. Its `z`-degree is at most `2e`: the three
parts have respective bounds `e-1`, `2e`, and `2e-1`. Its `X`-degree is at
most `4e+6`, because

```text
deg(A B q_e R)<= (2e+3)+(2e+1)+2,
deg(A B)^2=4e+6,
deg(q_eD_iN_i)<= (2e+1)+2+(2e+3).                   (9)
```

At an active row all denominators are nonzero. Equations `(CKL5)`, `(7)`,
and `(8)` give

```text
F(z;x)=A(x)B(x)q_e(x)s_xH_x(z)
      =(A(x)B(x))^2H_x(z),                           (10)
```

which is `(CLQ8)`.

Fix an external slope `gamma`. The polynomial `H_x` vanishes at `gamma`
exactly when the active row `x` is not incident with `gamma`. Exact design
saturation gives `4e+2` such rows, and `(10)` shows that they are distinct
roots of `F(gamma;X)`. Their monic locator is `K_gamma`, so
`K_gamma` divides `F(gamma;X)`. The quotient has degree at most four by
`(CLQ7)` and `(CLQ9)`. It is nonzero because the other `2e+1` active rows
are incident with `gamma`, and `(10)` is nonzero on each of them. This proves
`(CLQ10)`.

The final sharpness statement is the exact finite calculation in the node's
verifier: on the banked `F_17,e=1` Hankel design all three quotients have
degree four and only the two roots of `A` in `F_17`.

It remains to glue the quotients. At every active row, equations `(10)` and
`Q(z;x)=q_e(x)G_x(z)` give the polynomial identity

```text
F(z;x)Q(z;x)=(A(x)B(x))^2q_e(x)P_Z(z).              (11)
```

The active rows are exactly the `6e+3` distinct roots of `C`. Therefore

```text
FQ-(A B)^2q_eP_Z=C T                                (12)
```

for a unique biform `T`. The numerator has `X`-degree at most `6e+7` and
`z`-degree at most `3e`; since `deg C=6e+3`,

```text
deg_X T<=4,       deg_z T<=3e.                       (13)
```

At an internal slope, `(CLQ6)` and the pair-Lagrange specialization give

```text
F(xi_i;X)=A B q_e c_iD_i,
Q(xi_i;X)=lambda_i A B/D_i.                          (14)
```

Because `c_i lambda_i=P_Z(xi_i)`, the two terms on the left of `(12)`
agree identically. Hence `T(xi_i;X)=0` for every `i`, and `I` divides `T`
coefficientwise.

At `z=0`, equation `(10)` gives on every active row

```text
F(0;x)=A(x)B(x)^2q_e(x)P_Z(0).                       (15)
```

The two sides of `(15)` have `X`-degree at most `4e+7`. On the official
branch `e>=3`, so

```text
4e+7<6e+3=deg C.                                     (16)
```

Agreement at all roots of `C` therefore proves `(15)` as a polynomial
identity. Multiplication by `Q(0;X)=A(X)` shows that the numerator in `(12)`
also vanishes identically at `z=0`. Since zero is distinct from every
internal slope, `zI` divides `T`. Write `T=zIW`; equations `(13)` give

```text
deg_z W<=2e-1,       deg_X W<=4.                     (17)
```

We next prove that `I` divides `W` as well. Let `a` be a root in the pair
`D_k`. The pair-Lagrange specialization has the form

```text
Q(z;a)=eta_a zL_k(z)
      =eta_a zI(z)/[(z-xi_k)I'(xi_k)],       eta_a!=0. (18)
```

At `X=a`, every term of `(CLQ6)` except the last sum vanishes, so `I`
divides `F(z;a)`. After removing this visible `I`, evaluation at `z=xi_k`
leaves only the summand indexed by `k`, and that summand contains
`D_k(a)=0`. Hence

```text
I(z)(z-xi_k) divides F(z;a).                          (19)
```

Substitute `(18)` into `(12)` with `T=zIW` and use `A(a)=0`. Cancellation
of `zI` gives

```text
W(z;a)=eta_a F(z;a)/[C(a)(z-xi_k)I'(xi_k)].          (20)
```

Equation `(19)` proves that `I` divides `W(z;a)`.

Now let `t` be a root of `B`. The pair-Lagrange specialization is

```text
Q(z;t)=A(t)I(z)/I(0).                                 (21)
```

Again `(CLQ6)` visibly makes `I` divide `F(z;t)`. The polynomial identity
`(15)` gives `F(0;t)=0`, so in fact `zI` divides `F(z;t)`. Substitution of
`(21)` into `(12)` gives

```text
W(z;t)=A(t)F(z;t)/[I(0)C(t)z],                       (22)
```

and hence `I` divides `W(z;t)`.

Divide `W` coefficientwise in `z` by the monic polynomial `I` and consider
the remainder. It has `z`-degree less than `e` and `X`-degree at most four.
Equations `(20)--(22)` say that it vanishes at all `2e+3` distinct roots of
`A B`. Each of its `z`-coefficients is therefore a degree-at-most-four
polynomial in `X` with more than four roots, so the remainder is zero. Write

```text
W=I Omega,       deg_z Omega<=e-1,       deg_X Omega<=4. (23)
```

There is one final degree drop. For a root `a` of `D_k`, the explicit
specialization of `(CLQ6)` is

```text
F(z;a)=I(z)q_e(a)
       sum_(i!=k) D_i(a)N_i(a)L_i(z).                 (24)
```

The sum has degree at most `e-1` and vanishes at `z=xi_k`, because every
`L_i(xi_k)` in `(24)` is zero. Equations `(20),(23)--(24)` therefore give

```text
deg_z Omega(z;a)<=e-2.                               (25)
```

at all `2e` roots of `A`. The coefficient of `z^(e-1)` in `Omega` has
`X`-degree at most four. Since `2e>4` on the official branch, `(25)` forces
that coefficient to vanish identically. Thus `deg_z Omega<=e-2`, proving
`(CLQ11)--(CLQ12)`.

Finally, at an external slope write

```text
Q(gamma;X)=ell_gamma G_gamma^X(X).
```

Substituting `(CLQ10)` into `(CLQ11)` and using
`K_gamma G_gamma^X=C` gives

```text
ell_gamma C T_gamma=C gamma I(gamma)^2Omega(gamma;X).
```

Cancellation proves `(CLQ13)` and completes the proof. QED.
