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

Finally, the exact profile cofactor theorem starts with twelve cofactors.
The proved exclusions for `1538,1024,1028,512,514,256,64,32` leave
`{2,4,8,16}`.  The two proved `m=16` support-division exclusions leave only
its primitive multiplicity-four branch.  All retained cofactors are powers
of two, so the preceding argument applies simultaneously to every retained
vector at the fixed reduction prime.  QED.
