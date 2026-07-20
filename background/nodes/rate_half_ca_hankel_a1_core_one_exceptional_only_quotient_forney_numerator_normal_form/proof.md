# Proof

For `0<=j<=r+1`, define the quotient syndrome functional by

```text
ell_j(c(x))=A(x)x^j,       s_j=ell_j(h_1).            (1)
```

The degree of `A(X)X^j` is at most `2r`, so these are valid functionals on
the full moment space. They vanish on `W_A`. Applying `(1)` to the minimal
source representation in `(QFN2)` gives

```text
s_j=sum_(t in T)omega_t A(t)t^j.                     (2)
```

The first-order kernel equation is

```text
M_0q_1+M_1u=0.                                       (3)
```

Since `h_0` has source weights `beta_a` on `R_A`, row `j` of its first term
is

```text
(M_0q_1)_j=sum_(a in R_A)beta_a q_1(a)a^j.
```

Row `j` of `M_1u` is `s_j`. Thus `(3)` proves `(QFN6)` for `0<=j<=r`.

Put `C=AB_T`. Its roots are distinct because `A` and `B_T` are squarefree
with disjoint root sets. On those roots define

```text
w_t=omega_t A(t)             (t in T),
w_a=beta_a q_1(a)            (a in R_A).             (4)
```

Equations `(QFN6)` say

```text
sum_(x:C(x)=0)w_x x^j=0,       0<=j<=r.              (5)
```

Here `deg C=(r-1)+h`. The standard Lagrange duality map

```text
F |--> (F(x)/C'(x))_(C(x)=0)                         (6)
```

is an isomorphism from polynomials of degree at most `h-3` to the nullspace
in `(5)`. Indeed, for `deg F<=h-3`, the Lagrange coefficient identity gives

```text
sum_(C(x)=0)F(x)x^j/C'(x)=0,       0<=j<=r,
```

because `deg(FX^j)<=deg C-2`. Both spaces have dimension `h-2`, proving
surjectivity and uniqueness. Therefore one unique `F` of degree at most
`h-3` satisfies

```text
w_x=F(x)/C'(x).                                      (7)
```

At `t in T`, `C'(t)=A(t)B_T'(t)`. Combining this with `(4),(7)` gives
`(QFN4)`. At `a in R_A`, `C'(a)=A'(a)B_T(a)`, giving `(QFN5)`.

It remains to identify the degree and leading coefficient. Write

```text
A(X)=sum_(i=0)^(r-1)a_iX^i,       a_(r-1)=1.
```

The quadratic moment pin and `(1)` give

```text
Theta_2=sum_(i=0)^(r-1)a_i s_(i+2).                 (8)
```

Use `(QFN6)` for the terms through `s_r`. At a root `a` of monic `A`,

```text
sum_(i=0)^(r-2)a_i a^(i+2)=-a^(r+1).
```

Substitution in `(8)` proves `(QFN7)`. By `(4)`, its left side is

```text
sum_(C(x)=0)w_xx^(r+1)
 =sum_(C(x)=0)F(x)x^(r+1)/C'(x).                    (9)
```

Since `deg C-1=r+h-2`, the final Lagrange coefficient identity says that
`(9)` is the coefficient of `X^(r+h-2)` in `F(X)X^(r+1)`. It is zero when
`deg F<h-3` and equals `lc(F)` when `deg F=h-3`. The transversality theorem
gives `Theta_2!=0`; hence

```text
deg F=h-3,       lc(F)=Theta_2.                      (10)
```

Every `omega_t` is nonzero by minimality of `T`, while
`A(t)B_T'(t)!=0`. Equation `(QFN4)` therefore gives `F(t)!=0` for every
`t in T`, or `gcd(F,B_T)=1`.

Now fix `a in R_A`. Its row is saturated, and `Q(z;a)` has exactly `e`
distinct supported parameter roots. One is the exceptional root `z=0`, so
that root is simple. In the monic local kernel normalization its derivative
is `q_1(a)`, hence `q_1(a)!=0`. Also `beta_a!=0`, `A'(a)!=0`, and
`B_T(a)!=0`. Equation `(QFN5)` gives `F(a)!=0`. Thus `gcd(F,A)=1`, and the
two coprimality statements combine to `gcd(F,AB_T)=1`.

For `h=3`, `(10)` makes `F` the constant `Theta_2`, recovering the
barycentric formula. QED.
