# Proof

The prime-field reduction gives an odd prime `p=1 mod 256` and a primitive
root `r in F_p`.  Evaluation at `r` makes `theta_r` surjective, so its kernel
`P_r` is maximal and

```text
R/P_r = F_p,            Norm(P_r)=p.                  (1)
```

Suppose `theta_r(alpha)=0`.  Then `alpha in P_r`, hence `P_r` divides the
principal ideal `(alpha)`.  If `|Norm(alpha)|=2^mu p`, ideal norms give

```text
Norm((alpha) P_r^(-1))=2^mu.                          (2)
```

The prime `2` is totally ramified in `Q(zeta_256)`.  Its unique prime ideal
is `(pi)`, where `pi=1-zeta_256` and `Norm((pi))=2`.  Unique factorization of
nonzero ideals therefore turns `(2)` into

```text
(alpha) P_r^(-1)=(pi)^mu.                             (3)
```

Equivalently `(alpha)=P_r(pi)^mu`.  Since `(pi)^mu` divides `(alpha)`, the
quotient `g_alpha=alpha/pi^mu` is an algebraic integer.  Dividing (3) by the
principal ideal `(pi)^mu` gives

```text
(g_alpha)=P_r,
```

and its absolute norm is `p`.  This proves `(PCR1)`.

Apply the same argument to `beta`.  Both `g_alpha` and `g_beta` generate
`P_r`, so their quotient is a unit of `R`.  This proves `(PCR2)`.

Now suppose `mu=nu`, so `beta=u alpha`. In the power basis
`1,zeta_256,...,zeta_256^127`, let `A_alpha` be multiplication by `alpha`.
Its columns are the 128 negacyclic shifts of the coefficient vector of
`alpha`; every column has Euclidean norm `sqrt(18)`. Moreover

```text
|det A_alpha|=|Norm(alpha)|=2^mu p.                   (4)
```

The coefficient vector of `u` is the unique solution of

```text
A_alpha c(u)=c(beta).
```

Cramer's rule replaces one shift column by `c(beta)`, whose Euclidean norm is
also `sqrt(18)`. Hadamard's determinant inequality and (4) therefore give

```text
|u_j|<=18^64/(2^mu p)                                 (5)
```

for every `j`. Interchanging `alpha` and `beta` proves the same estimate for
every coefficient of `u^(-1)`.

The cofactor-window theorem gives

```text
floor(18^64/p_min)=2013.
```

Since `p>=p_min`, taking integer floors in (5) gives respectively
`1006,503,251,125` for `mu=1,2,3,4`. This proves `(PCR3)`.

For `(PCR4)`, Parseval in the 128 power-basis conjugates gives

```text
sum_(a odd)|alpha(zeta_256^a)|^2=128*18.
```

Conjugate values have equal squared absolute value, so selecting one from
each of the 64 pairs gives `sum_a y_a=64*18`. Their product is the absolute
field norm `2^mu p`. Hence `sum z_a=64` and the displayed product formula.
The linear terms cancel, so

```text
sum_a(z_a-1-log z_a)=-sum_a log z_a
                         =log(18^64/(2^mu p)).        (6)
```

To prove `(PCR5)`, first consider any positive vector `z` with sum 64 and
deficit `D` as in (6). Set `p_a=z_a/64` and `q_a=1/64`. Then

```text
KL(q||p)=D/64.
```

Pinsker's inequality in natural logarithms gives

```text
sum_a |z_a-1| <= sqrt(128D).                          (7)
```

Let `A=sum_(z_a>=1)(z_a-1)`. Since the deviations sum to zero, (7) gives
`A<=sqrt(32D)`. On the positive side, `log z<=z-1`. On the negative side,

```text
-log z=(z-1-log z)+(1-z).
```

Therefore

```text
sum_a |log z_a|<=D+2A<=D+sqrt(128D).                 (8)
```

The vectors for `alpha` and `beta` have the same `D_(mu,p)`, while
`lambda_a(u)=log z_a(beta)-log z_a(alpha)`. The triangle inequality and (8)
prove `(PCR5)`. Its coordinate sum is zero because `u` has norm one.

Dirichlet's unit theorem gives rank `64-1=63` for this totally imaginary
field. The kernel of the absolute-value log map consists of units all of
whose conjugates have modulus one; Kronecker's theorem identifies them with
the roots of unity, which in `Q(zeta_256)` are exactly `mu_256`. Multiplying
a nonzero coefficient vector by those roots gives its 256 distinct
negacyclic shift/sign associates. Thus shift/sign orbits inject into the
rank-63 log-lattice points in `(PCR5)`.

The proved dependency `e1_conductor256_full_unit_circular_basis` imports the
unconditional conductor-256 real class-number theorem and the prime-power
Kummer-Sinnott unit-index formula. It proves that the 63 displayed real
circular units form a basis of `R^x/mu_256`, with the stated sine-ratio log
matrix. Applying that theorem to `u` gives `(PCR8)`. In particular this is an
exact parametrization of the full lattice just used, not an assumption that
an arbitrary algebraic unit is circular.

For `(PCR6)`, every vector in profile `(3,6)` has the same dictionary weight
`M_33(3,6)`. Each torsion orbit contains 256 oriented vectors, so the
dictionary's factor one half gives `256M/2=128M` unordered collision pairs
per orbit. The proved post-profile-exclusion ledger gives the exact uniform
allowance

```text
E_max=65127585921474870475467050631501738502567,
floor(2E_max/M)=93962.
```

Therefore 368 orbits exceed the edge budget
using this profile alone, while 367 orbits contain 93952 oriented vectors.
This proves the necessary condition `(PCR7)`; no claim is made about the
remaining weighted profiles when it holds.

Finally, the exact profile cofactor theorem starts with twelve cofactors.
The proved exclusions for `1538,1024,1028,512,514,256,64,32` leave
`{2,4,8,16}`.  The two proved `m=16` support-division exclusions leave only
its primitive multiplicity-four branch.  All retained cofactors are powers
of two, so the preceding argument applies simultaneously to every retained
vector at the fixed reduction prime.  QED.
