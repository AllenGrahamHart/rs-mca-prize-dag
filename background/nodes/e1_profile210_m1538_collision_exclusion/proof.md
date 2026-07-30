# Proof

Let `y_u=|F(zeta_256^u)|^2` over one representative from each conjugate
pair. As for every square-mass-18 vector,

```text
sum y_u=64*18,
sum (y_u-18)^2=64V,
Norm(F(zeta_256))=product y_u.                       (1)
```

For fixed `V`, the sharp two-moment extremum has two values

```text
a=18-sqrt(V(64-j)/j),
b=18+sqrt(Vj/(64-j)),
M_(V,j)=a^j b^(64-j),                                (2)
```

with `1<=j<=63` and `a>0`. For fixed `j`, `(2)` is strictly decreasing in
`V`: differentiating with respect to `sqrt(V)` and using the fixed-mean
relation gives a positive constant times `1/b-1/a<0`.

Exact rational square-root intervals at `V=6` prove

```text
M_(6,j)<1538 p_min
```

for all 62 feasible values of `j`. Therefore a cofactor-`1538` collision has
`V<=4`. The variance is a nonnegative even integer.

If `V=0`, then the norm is `18^64`, whose 2-adic valuation is `64`, not one.
If `V=2`, there is one signed unit autocorrelation at a lag of odd 2-adic
order. The standard Lucas recurrence

```text
L_0=2,       L_1=18,       L_n=18L_(n-1)-L_(n-2)
```

gives `Norm=L_64`, and exact arithmetic gives

```text
L_64 mod 1538=2.
```

Thus `V=2` is also impossible.

It remains to treat `V=4`. Put

```text
E=sum_(d=1)^63 A_d^2=V/2=2.
```

Hence exactly two autocorrelations are nonzero, each equal to `+1` or `-1`:

```text
y_u=18+epsilon_d(zeta^(ud)+zeta^(-ud))
        +epsilon_e(zeta^(ue)+zeta^(-ue)),            (3)
```

where `1<=d<e<=63`. Modulo two, the autocorrelation polynomial is the norm
of the ten-singleton parity polynomial. Its multiplicity at one is twice the
local valuation. Since `v_2(1538)=1`, this multiplicity is two. Expanding the
four terms in `(3)` at one shows that this is equivalent to

```text
d+e=1 mod 2.                                         (4)
```

Because `769` divides the cyclotomic norm, `(3)` vanishes at a primitive
`256`-th root modulo `769`. The complete finite-field screen checks all 128
such roots, all lag pairs satisfying `(4)`, and all four sign pairs. It finds
640 hits. The diagonal Galois action reduces them to exactly five types:

```text
(d,e,epsilon_d,epsilon_e)
(11,20,-1,-1)
(14,15,+1,+1)
(18,21,+1,-1)
(19,50,-1,+1)
(36,49,-1,+1).                                      (5)
```

For an exact norm computation, let `C_0=2`, `C_1=T`, and

```text
C_n=T C_(n-1)-C_(n-2).
```

Then `C_d(zeta+zeta^-1)=zeta^d+zeta^-d`, and `C_64` is the degree-64
minimal polynomial of `zeta_256+zeta_256^-1`. The norm for a row of `(5)` is

```text
|Res_T(C_64,18+epsilon_d C_d+epsilon_e C_e)|.        (6)
```

Exact Bareiss determinants give the following quotients by `1538`:

```text
94726573109454554355723205753386381132700979257546174561074519931854171378433
94726572813333334850450851147142254866189741290919693369950466971809955939327
94726573091729884801570429320134633068624255208740225490737339440982526158079
94726573091644995672964768686916625315139627899621468752369565038943115036671
94726573091678309360928070176107749808616100579343144696817893372730754023169.
```

Every one is below

```text
p_min=108037839417390090843359763492907651257884484313348964300411102808750191280128.
```

Thus none is an official row prime. All possible variances have been
excluded, so cofactor `1538` is impossible. QED.

