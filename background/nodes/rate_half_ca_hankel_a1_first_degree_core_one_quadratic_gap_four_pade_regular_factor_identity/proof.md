# Proof

The contracted source representation is

```text
M_1(t)_(i,j)=Phi_t(X^(i+j))
            =sum_(x in U_0)omega_x(t)x^(i+j).       (1)
```

The split-biform interpolation identity says

```text
Lambda(t)G(t,x)=L'(x)omega_x(t)Q(t,x)
                                             (x in U_0).       (2)
```

Lagrange interpolation of the degree-at-most-`p-3` polynomial `G` gives

```text
Lambda G
 =sum_(x in U_0)omega_x(t)Q(t,x)L(X)/(X-x).         (3)
```

Subtract `(3)` from `QB` and use `(PRI2)`. This proves `(PRI3)`. Each
difference quotient in `(PRI2)` has degree at most `d-1`, proving the
degree bound for `P_F`.

We next prove the resultant formula on the generic separable locus and
then extend polynomially. Let

```text
Q=a product_(i=1)^d (X-r_i).
```

The first `d` moments have unique weights `theta_i` on these roots. The
kernel recurrence `M_1q=0` extends that representation through every
moment used by `M_1`. Applying the two representations of `Phi_t` to
`Q(X)/(X-r_i)` gives

```text
P_F(r_i)=theta_i Q_X(r_i).                           (4)
```

Let `V` be the `d by d` Vandermonde matrix on the roots. The corner
cofactor of the moment matrix is

```text
det(V)^2 product_i theta_i.
```

The same cofactor in `adj M_1=D_1qq^T` is `D_1a^2`. Hence, up to the fixed
ordering scalar,

```text
det(V)^2 product_i theta_i=D_1a^2.                  (5)
```

Using `(4)`, the root-product convention for the formal resultant gives

```text
Res_X^(d,d-1)(Q,P_F)
 =a^(d-1) product_i [theta_i Q_X(r_i)]
 =c_F a^(2d-1)det(V)^2 product_i theta_i
 =c_F a^(2d+1)D_1.                                  (6)
```

Both sides of `(6)` are polynomial in the parameter, so the identity
extends across inseparable fibers and degree drops. This proves `(PRI4)`.

Reversing coefficients in `(PRI2)` gives exactly the truncated reciprocal
numerator in the core-stripped contact theorem. Thus `P_F|_C` has contact
order

```text
d+rho=2d+1                                           (6a)
```

along the domain-infinity divisor, and the quotient by that fixed contact
is `s_F`. The raw formal resultant has parameter degree

```text
e(d-1)+(e+1)d=2de-e+d.                              (6b)
```

Since `a` has homogeneous parameter degree `e`, removing
`a^(2d+1)` subtracts `e(2d+1)` and leaves

```text
(2de-e+d)-e(2d+1)=d-2e=e-2.                        (6c)
```

This is exactly both `deg D_1` and `deg div(s_F)`. Formula `(6)` therefore
says that the remaining norm is `D_1`; equivalently its homogeneous
parameter divisor is the pushforward of the zero divisor of `s_F`. This
proves `(PRI5)`.

At `u=4`, the proved contact divisors are

```text
double root:  div(s_F)=R_*+2B,
two simple:   div(s_F)=R_1+R_2+P_1+P_2.             (7)
```

Their parameter pushforwards are cut out respectively by

```text
g_*S_B^2,       G_1G_2S_1S_2.                      (8)
```

Equation `(PRI5)` therefore gives the first identities in
`(PRI6)--(PRI7)`. The regular-quartic pin already gives

```text
D_1=c g_*E_4,       or       D_1=c G_1G_2E_4.      (9)
```

Cancel the nonzero supported forms in the polynomial ring. This proves the
two identities for `E_4`, even when the cancelled forms share roots with
the correction factors. QED.
