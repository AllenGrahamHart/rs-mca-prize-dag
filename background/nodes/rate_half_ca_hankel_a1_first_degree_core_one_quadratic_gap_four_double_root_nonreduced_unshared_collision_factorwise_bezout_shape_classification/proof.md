# Proof

The center-adjusted unsupported-root budget excludes profiles II and III
when `d_A=1`. The exact factor trichotomy therefore gives `(FBS1)`, with

```text
2n_L-3m_L=-1,       2n_j-3m_j=0 for j in O.       (1)
```

We first distribute the projective intersection cycle factorwise. The
source locator curve has bidegree `(3e-2,e)`, while `Q_j` has bidegree
`(n_j,m_j)`. They are coprime because the source locator curve is
coprime to `G`. Hence their total intersection number is

```text
(3e-2)m_j+e n_j.                                  (2)
```

On the classified grid, `Q_j` has exactly `(3p-2)m_j` roots. They are
actual-support roots and are transverse intersections of `Qbar` and `G`.
Exactly one factor of `G` vanishes at each such point, so subtracting the
grid leaves the nonnegative factorwise capacity

```text
c_j=e n_j+(3e-2-(3p-2))m_j.                       (3)
```

There are exactly `e-7` padded-heavy first copies off the center line.
The center-adjusted heavy row identifies all of them with the distinct
roots of `g_off` on `x_*`. Assign each first copy to one factor that
vanishes there; initially call the assigned count `r_j^0`, so

```text
sum_j r_j^0=e-7.                                  (4)
```

The collision contributes exactly four further intersection units. Indeed,
at `(tau,x_*)` both `Lambda` and `L_U0` are units, and the Pade syzygy

```text
Qbar B-Lambda G=L_U0 P_F                          (5)
```

identifies the local ideals `(Qbar,G)` and `(Qbar,P_F)`. The exact
collision Smith router gives contact length four in each of its profiles
`[4]`, `[1,3]`, and `[2,2]`. Additivity over the factors gives

```text
sum_j ell_j=4.                                    (6)
```

Every assigned padding copy and every local collision intersection lies
outside the classified grid. Thus

```text
c_j>=r_j^0+ell_j.                                 (7)
```

Summing `(3)` and using `sum n_j=p-3`, `sum m_j=e-2`, and `2p=3e-1`
gives

```text
sum_j c_j=e-3=(e-7)+4.                            (8)
```

Equations `(4),(6)--(8)` force equality in `(7)` for every factor. In
particular, there is no second factor or excess local multiplicity at a
padded-heavy point, and there is no other residual intersection. We may
therefore write `r_j=r_j^0`; these are exactly the simple `g_off` roots
of `Q_j(t,x_*)`. This proves `(FBS5)` and the first sum in `(FBS4)`.

It remains to identify the local contribution. Complete at the collision,
write `z=t-tau`, `y=X-x_*`, and let

```text
q=y^2+c_1(z)y+c_0(z),       ord c_1>=3,
ord c_0=6                                                   (9)
```

be the local quadratic factor of `Qbar`. For the local germ `f_j` of
`Q_j`, reduction modulo `q` has the form `u_j(z)+v_j(z)y`. Since
`ord_z f_j(z,0)=b_j<=2`, reduction changes its constant term only in
order at least six, and `ord u_j=b_j`. Multiplication by this remainder
on the rank-two algebra `F[[z]][y]/(q)` has determinant

```text
u_j^2-u_jv_jc_1+v_j^2c_0.                         (10)
```

Its three terms have orders `2b_j`, at least `b_j+3`, and at least six.
For `b_j=0,1,2`, the first term is uniquely minimal. Therefore

```text
ell_j=2b_j.                                       (11)
```

The heavy-row factorization is

```text
G(t,x_*)=g_off(t)S_B(t)T_3(t),
deg(g_off,S_B,T_3)=(e-7,2,3),       T_3(tau)!=0.  (12)
```

Every specialized factor has exact degree `m_j`. After removing its
simple `g_off` roots and its correction order `b_j`, the remaining degree
is the nonnegative integer `t_j` in `(FBS3)`. Degree additivity in `(12)`
proves the other two sums in `(FBS4)`.

Now use `(1),(3),(5)`. For the large factor,

```text
c_L=(3m_L-e)/2=r_L+2b_L
   =m_L-b_L-t_L+2b_L,
```

so `m_L=e+2b_L-2t_L`. For an ordinary factor,

```text
c_j=3m_j/2=r_j+2b_j
   =m_j-b_j-t_j+2b_j,
```

so `m_j=2(b_j-t_j)`. This proves `(FBS6)`.

An ordinary factor has positive degree, hence `b_j-t_j>=1`. Since the
total correction order is two, the only possible ordinary records are

```text
(m,n;r,b,t;ell)=(2,3;1,1,0;2),
(m,n;r,b,t;ell)=(4,6;2,2,0;4).                    (13)
```

There can be no ordinary factor, one quadratic, one quartic, or two
quadratics, and no other multiset. Subtracting each choice from the totals
in `(FBS4)` and applying the large-factor equation in `(FBS6)` gives
exactly A--D in `(FBS7)`. The large-factor eligibility and nonnegativity
checks are immediate from `7m_L>=3e`, the sharper proved threshold, and
`r_L>=0`; they give the small-`e` exclusions stated after the table. QED.
