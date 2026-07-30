# Conductor-256 character-diagonal exponent router

- **status:** PROVED
- **closure:** finite-group Fourier diagonalization of the full circular-unit
  basis
- **dependency:** `e1_pure_cofactor_common_prime_associate_router`
- **consumer:** `e1_official_low_square_mass_pair_budget` (evidence)

Let

```text
G=(Z/256Z)^x/{+-1},       |G|=64,
```

represented by the odd integers `1,3,...,127`.  The class of `5` generates
`G`; write its powers as `g_t=5^t`, `t in Z/64Z`.  Put

```text
f_t=2 log |sin(pi*g_t/256)|,
kappa_j=sum_(t=0)^63 f_t exp(-2 pi i j t/64).          (CER1)
```

The value of the sine is independent of the representative modulo sign.

Write a conductor-256 unit, modulo its torsion factor, in the full circular
unit basis as

```text
u=product_(a in G\{1}) eta_a^x_a,       x_a in Z.      (CER2)
```

Extend the exponent vector to a zero-sum integer function `xi:G->Z` by

```text
xi(a)=x_a  (a!=1),       xi(1)=-sum_(a!=1)x_a.         (CER3)
```

For the 64 conjugate-pair logarithms

```text
lambda_b(u)=log |u(zeta_256^b)|^2,
```

one has the exact convolution and Fourier diagonalization

```text
lambda_(g_s)=sum_(t=0)^63 xi(g_t) f_(s+t),
widehat(lambda)_j=kappa_j widehat(xi)_(-j).            (CER4)
```

All indices are modulo `64`.  Every nontrivial eigenvalue is nonzero:

```text
kappa_j!=0,       1<=j<=63.                            (CER5)
```

Now fix one official E1 row, one reduction root, and one residual cofactor
`2^mu`, `mu in {1,2,3,4}`.  If two profile-`(3,6,S=18)` collisions in that
cofactor differ by `u`, put

```text
D=log(18^64/(2^mu p)),
R=2(D+sqrt(128D)).                                    (CER6)
```

Then `D>=0`, `||lambda(u)||_1<=R`, and `(CER4)` gives the explicit necessary
bounds

```text
|widehat(xi)_j| <= R/|kappa_(-j)|,                    (CER7)

sum_t xi(g_t)^2
  <= (R^2/64) sum_(j=1)^63 |kappa_j|^(-2),            (CER8)

max_t |xi(g_t)|
  <= (R/64) sum_(j=1)^63 |kappa_j|^(-1).              (CER9)
```

The stronger weighted ellipsoid

```text
sum_(j=1)^63 |kappa_j|^2 |widehat(xi)_(-j)|^2
  =64 sum_(s=0)^63 lambda_(g_s)^2
  <=64R^2                                                (CER10)
```

is also necessary.  Thus every fixed-cofactor associate family lies in an
explicit finite integer exponent box and ellipsoid.  A complete count may
enumerate that box with certified outward intervals for `(CER1)`, but every
retained vector must still pass both exact algebraic filters from the
associate router:

1. the power-basis coefficients of `u` and `u^(-1)` obey the cofactor box
   `1006,503,251,125` for `mu=1,2,3,4`; and
2. exact multiplication in `Z[X]/(X^128+1)` carries the selected collision
   vector to another profile-`(3,6,S=18)` vector.

This is a complete finite-search reduction for each nonempty fixed-cofactor
associate family.  It does not count the vectors, prove the aggregate
`367`-orbit cap, pay lower profiles, or close E1.

## Falsifier

A pair of same-root, same-cofactor pure collisions whose unique circular-unit
exponent vector violates any of `(CER7)--(CER10)`, or a zero nontrivial
Fourier eigenvalue in `(CER5)`.
