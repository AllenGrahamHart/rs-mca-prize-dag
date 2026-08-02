# KoalaBear positive 433-1a cell-5 signed-pair generic reducedness

- **status:** PROVED
- **scope:** deployed characteristic, generic `t`, cell 5, signs
  `(-1,-1)`, chart 2, guard-localized squared `DE+/DE-` pair
- **consumer:** signed-pair residue and colored-norm ledger

Let `A_g=A[(d0*d1)^-1]` be the 24-dimensional algebra from the stable-rank
theorem and put

```text
ell = x1 + 2*x0 + 3*b in A_g.
```

Exact normal forms give the multiplication matrix `L=m_ell` in the stable
basis `im(M^2)`.  Every coefficient used below is regular at `t=2`.  At that
fiber the first coordinate vector is cyclic for `L(2)`: its 24 Krylov
vectors are independent.  The resulting degree-24 minimal polynomial
`m_2(s)` satisfies

```text
gcd(m_2,m_2') = 1 in F_2130706433[s].
```

Therefore the generic Krylov determinant and characteristic discriminant
are nonzero.  Hence `ell` is a primitive element,

```text
A_g = K[ell] ~= K[s]/(chi_L(s)),
```

and `chi_L` is squarefree.  In particular

```text
A_g is reduced over K=F_2130706433(t).            (KBGR-1)
```

This is generic-function-field reducedness.  It does not factor `chi_L`,
classify residue fields or geometric points, determine the exceptional-`t`
locus, restore source signs or distinctness, impose the colored `BE` edge,
cover charts 3--5 or the `DF` family, delete cell 5 or `433-1a -> O0b`,
close K3, or prove either Prize result.

## Falsifier

A pole at `t=2`, failure of the exact stable-basis multiplication identity,
a singular 24-vector Krylov matrix, a nonconstant specialized derivative
gcd, or a failure of the specialization argument.
