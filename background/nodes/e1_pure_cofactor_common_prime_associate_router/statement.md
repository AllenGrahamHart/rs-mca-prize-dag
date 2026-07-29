# E1 pure-cofactor common-prime associate router

- **status:** PROVED
- **closure:** ideal factorization proof
- **scope:** prize-envelope `N=256` prime-field E1 collisions
- **consumer:** `e1_official_low_square_mass_pair_budget`

Let `R=Z[zeta_256]`, put `pi=1-zeta_256`, and fix one official quotient
root `r in F_p` of order `256`.  The reduction map

```text
theta_r:R -> F_p,       theta_r(zeta_256)=r
```

has kernel `P_r`, a prime ideal of norm `p`.

If a nonzero collision value `alpha in R` satisfies

```text
theta_r(alpha)=0,       |Norm(alpha)|=2^mu p,
```

then

```text
(alpha)=P_r (pi)^mu,    g_alpha=alpha/pi^mu is integral,
(g_alpha)=P_r,          |Norm(g_alpha)|=p.             (PCR1)
```

Consequently, if `beta` is another collision at the same row and quotient
root with `|Norm(beta)|=2^nu p`, there is a unit `u in R^x` such that

```text
beta/pi^nu = u alpha/pi^mu,
pi^mu beta = u pi^nu alpha.                            (PCR2)
```

Thus same-row pure-power-of-two cofactor collisions are not independent
principal-norm events: after removing their exact ramified factor at two,
they are unit associates generating the one fixed reduction prime.

There is also an exact coefficient box inside each fixed cofactor. If
`mu=nu`, write the unique power-basis representatives

```text
u=sum_(j=0)^127 u_j zeta_256^j,
u^(-1)=sum_(j=0)^127 v_j zeta_256^j.
```

Because both collision vectors have coefficient square mass `18`,

```text
max_j(|u_j|,|v_j|) <= floor(18^64/(2^mu p)).           (PCR3)
```

Uniformly over the prize interval this gives

| `mu` | cofactor | coefficient bound |
|---:|---:|---:|
| 1 | 2 | 1006 |
| 2 | 4 | 503 |
| 3 | 8 | 251 |
| 4 | 16 | 125 |

Thus a fixed-cofactor branch is a finite bounded inverse-pair problem in
`Z[X]/(X^128+1)`, not an unbounded unit-group search.

The same branch has an exact logarithmic body. Choose one representative
from each conjugate pair and put

```text
y_a=|alpha(zeta_256^a)|^2,       z_a=y_a/18,       a in (Z/256Z)^x/{+-1}.
```

Then

```text
sum_a z_a=64,       product_a z_a=2^mu p/18^64,
D_(mu,p):=sum_a(z_a-1-log z_a)=log(18^64/(2^mu p)). (PCR4)
```

If `beta=u alpha` is a second collision in the same cofactor and

```text
lambda_a(u)=log|u(zeta_256^a)|^2,
```

then

```text
sum_a lambda_a(u)=0,
sum_a |lambda_a(u)| <= 2(D_(mu,p)+sqrt(128 D_(mu,p))). (PCR5)
```

The logarithmic embedding of `R^x` has rank `63` and kernel exactly the 256
roots of unity. Consequently the number of negacyclic shift/sign orbits in
one fixed-cofactor collision family is at most the number of points of the
full unit log lattice in the explicit `L1` body `(PCR5)`. This is a counting
reduction, not a lattice-point estimate.

The conductor-256 unit-index theorem makes that full lattice explicit. For
odd `a=3,5,...,127`, put

```text
eta_a=zeta_256^((1-a)/2)(1-zeta_256^a)/(1-zeta_256).
```

Every unit has one unique representation

```text
u=zeta_256^j product_a eta_a^x_a,      j mod 256, x_a in Z,       (PCR8)
```

and its log vector is the corresponding integer combination of

```text
lambda_b(eta_a)=2 log |sin(pi*a*b/256)/sin(pi*b/256)|,
b=1,3,...,127.
```

This is the full algebraic-unit lattice, not a finite-index surrogate.

Let `T_36(p,r)` be the total number of these 256-element orbits across the
four residual cofactors. The exact weighted-kernel dictionary gives the
profile contribution

```text
E_36=128 M_33(3,6) T_36(p,r),
M_33(3,6)=1386246316188473270092082114587711840.       (PCR6)
```

The recalibrated binding-row vector allowance is `93962`. Since

```text
367*256=93952,       368*256=94208,
```

the complete low-mass pair budget necessarily requires

```text
T_36(p,r)<=367.                                      (PCR7)
```

This orbit cap is not sufficient for the complete budget because all
lower-weight profiles still contribute.

For the currently surviving prize `N=256`, profile `(3,6,S=18)` branches,
the proved cofactor exclusions leave only

```text
m in {2,4,8,16};
```

the `m=16` once- and twice-divided support branches are also excluded.  Hence
all live vectors of this maximum-weight profile at a fixed `(p,r)` satisfy
`(PCR2)`, with `mu in {1,2,3,4}` and only the primitive multiplicity-four
support branch remaining at `mu=4`.

This is an aggregate coupling theorem, not a count.  The remaining payment is
to count or sharply bound the integer exponent vectors in `(PCR8)` whose
products with `pi^mu` have profile `(3,6,S=18)`, jointly with the lower-weight
profiles in the exact weighted-kernel ledger.

## Falsifier

Two same-root collisions of pure cofactor whose normalized principal ideals
are distinct, or a live profile-`(3,6)` cofactor outside `{2,4,8,16}` after
all stated exclusions are consumed.
