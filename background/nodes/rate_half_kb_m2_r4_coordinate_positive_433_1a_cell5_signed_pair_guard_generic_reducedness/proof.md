# Proof

Write `K=F_p(t)` with `p=2130706433`.  By the proved stable-rank theorem,
the finite quotient `A` has

```text
A_g = A[g^-1] = im(m_g^2),
dim_K A_g = 24,
```

where `g=d0*d1`.  The first 24 columns of the exact `m_g^2` matrix form a
basis `U` for this image.

## Exact multiplication operator

Set `ell=x1+2*x0+3*b`.  Groebner.jl reduces `ell` times every one of the 64
standard monomials against the hash-pinned 18-element basis.  Nemo then
forms `ell*U`, solves its coordinates through the nonsingular top-left
24-by-24 block of `U`, and checks all 64 rows of

```text
U*L = ell*U.                                      (1)
```

The merged operator packet covers all 24 columns and has SHA-256

```text
d49311b27680acf3b4b548547a9c4f8c94f5d1ea63ae3154982e5972bc5de026.
```

Thus `L` is exactly multiplication by `ell` on `A_g`, not a sampled or
fitted matrix.

## Regular squarefree specialization

All denominators in `U`, `L`, and the target matrix in (1) are nonzero at
`t=2`.  The independent standard-library checker evaluates them in `F_p`
and rechecks the entire 64-by-24 identity (1).

Let `v=e_1`.  Gaussian elimination over `F_p` proves that

```text
v,L(2)v,...,L(2)^23 v
```

are independent.  Solving for `L(2)^24v` gives the monic degree-24 minimal
polynomial.  Its canonical coefficient hash is

```text
d26bd2c06273091759c96100b517f2aae3e57f1d966eb20b8f025358afea6e65,
```

and Euclid's algorithm returns derivative gcd `1`.  Hence `L(2)` is cyclic,
its minimal polynomial equals its characteristic polynomial, and that
polynomial is squarefree.

## Generic conclusion

The specialized Krylov determinant is nonzero, so the corresponding
rational function over `K` is nonzero.  Therefore `v,Lv,...,L^23v` are
independent generically and `ell` generates the 24-dimensional algebra.

Because `L` is regular at `t=2`, its generic characteristic polynomial
specializes to the squarefree characteristic polynomial of `L(2)`.  Its
discriminant therefore has a nonzero specialization and cannot be the zero
rational function.  Thus the generic characteristic polynomial `chi_L` is
squarefree.  The surjection `K[s] -> A_g`, `s |-> ell`, now induces

```text
K[s]/(chi_L) ~= A_g.
```

A quotient by a squarefree polynomial over a field is reduced, proving
`(KBGR-1)`.  QED.
