# Proof

The middle-adjugate theorem gives `(BHF1)`. Replacing column `k` of a
square matrix by a vector `v` gives

```text
det M[k<-v]=e_k^T adj(M)v.                          (1)
```

Apply `(1)` to `v=v_s` and substitute `(BHF1)--(BHF2)`:

```text
det M[k<-v_s]
 =D_1(e_k^Tq)(q^Tv_s)
 =D_1q_kR_(d+1+s).                                 (2)
```

This proves `(BHF3)`. The entries of the primitive vector `q` have gcd one.
Taking the gcd of `(2)` over the Cartesian set of `k` and `s` therefore
gives `(BHF4)`.

Order the exponent set `E_s` with `d+1+s` last. The corresponding moment
matrix has block form

```text
widehat M_s=[ M    v_s ]
            [v_s^T c_s ].                          (3)
```

The bordered determinant identity is

```text
det widehat M_s
 =c_s det M-v_s^T adj(M)v_s.                       (4)
```

Here `det M=0`. Substituting `(BHF1)--(BHF2)` in `(4)` gives

```text
det widehat M_s=-D_1(q^Tv_s)^2
                =-D_1R_(d+1+s)^2,                 (5)
```

which is `(BHF5)`.

The source moment representation is

```text
h_j(t)=sum_(x in U_0)omega_x(t)x^j.                 (6)
```

Let `V_s` be the matrix with entries `x^a`, with `a in E_s` indexing rows
and `x in U_0` indexing columns. Equation `(6)` says

```text
widehat M_s=V_s diag(omega_x) V_s^T.                (7)
```

Cauchy-Binet applied to `(7)` is exactly the subset sum in `(BHF6)`. Its
equality with the right side follows from `(5)`.

The dual-MDS split-biform reduction gives polynomials

```text
H_x=omega_xQ(t,x)/Lambda
```

and the omitted-recurrence theorem gives

```text
R_(d+1+s)=Lambda sum_x H_x x^(d+1+s).              (8)
```

The sum in `(8)` is a parameter polynomial of degree at most `e-2`; call
it `Theta_s`. For `s=0`, unitriangular coefficient extraction has no lower
omitted term, so `Theta_0=[X^n]G`. The Pade regular-factor identity gives
`D_1=c_Dg_*S_B^2`. Substitution in `(BHF6)` proves `(BHF7)--(BHF8)`.

It remains to split the off-line flag. In shape A, `d_A=1`. The heavy-row
factorization gives

```text
g_*=g_off gcd(g_*,Lambda),       deg g_off=e-7.    (9)
```

The roots of `g_off` are exactly the off-line padded-heavy slopes. The
remaining root of `g_*` is a center slope, while the sole root of `S_B` is
the unsupported collision parameter. Hence, after writing
`H_off=g_offH_reg`,

```text
gcd(H_reg,D_1)=1,
deg H_reg=3e-(e-7)=2e+7.                           (10)
```

All displayed factors are squarefree except the printed square on `S_B`,
whose root is absent from `H_off`.

Because `H_reg` is squarefree and coprime to `D_1`, equation `(BHF6)` gives

```text
gcd(H_reg,B_0,...,B_r)
 =gcd(H_reg,R_(d+1),...,R_(d+1+r)).                (11)
```

The two factors of `H_off` are coprime. Splitting its gcd with the defects
between those factors and using `(11)` proves `(BHF10)--(BHF11)`.

At a root `delta` of `H_reg`, equation `(10)` makes `D_1(delta)` nonzero.
Thus `M(delta)` has rank exactly `d` and kernel spanned by `q(delta)`.
Since `M(delta)` is symmetric, its column space is the hyperplane
orthogonal to `q(delta)`. Therefore every appended `v_s(delta)` lies in
that column space if and only if

```text
q(delta)^Tv_s(delta)=R_(d+1+s)(delta)=0.           (12)
```

The omitted-recurrence theorem identifies simultaneous vanishing through
`s=r` with `q_delta>=r+1`. This proves `(BHF12)`. QED.
