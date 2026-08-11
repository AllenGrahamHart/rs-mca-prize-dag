# `A=1` core-free cubic gap-one two-slope coefficient clone-rank gate

- **status:** PROVED
- **closure:** coefficient-row rank bounded by two-support union excess
- **consumer:** `rate_half_band_crossing_location`

Retain any core-free cubic double-plus-simple `u=1` packet. Write the
primitive kernel biform in any parameter basis as

```text
Q(U,V;X)=sum_(i=0)^e Q_i(X)U^(e-i)V^i,
W_Q=span{Q_0,...,Q_e},       dim W_Q=e+1.            (CRK1)
```

For distinct supported slopes `alpha,beta`, put

```text
X_(alpha,beta)=S_beta\S_alpha,
j_(alpha,beta)=|S_alpha union S_beta|-rho>=1.        (CRK2)
```

Let

```text
Ev_(alpha,beta)
 =(Q_i(x))_(x in X_(alpha,beta), 0<=i<=e).          (CRK3)
```

Then

```text
rank Ev_(alpha,beta)<=j_(alpha,beta).               (CRK4)
```

Equivalently, the restrictions to `X_(alpha,beta)` of all parameter
coefficient forms span a space whose dimension is at most the excess of the
two error-support union above `rho`.

In particular, on the minimum-union boundary

```text
|S_alpha union S_beta|=rho+1,                       (CRK5)
```

the matrix in `(CRK3)` has rank exactly one. Hence all nonzero row forms

```text
Q(-;x) in F[U,V]_e,       x in S_beta\S_alpha,      (CRK6)
```

are pairwise proportional. They have the same projective parameter zero
divisor, with multiplicity. At union `rho+s`, their coefficient-row rank is
at most `s`.

## Scope

The theorem applies also at the possible `E_1` slope: it uses the complete
kernel coefficient recurrence, not first-order Smith transversality. It does
not prove that the coefficient map `x |-> [Q(-;x)]` separates domain points,
so the rank-one conclusion is a gate rather than an exclusion. No
proportionality is claimed when `j_(alpha,beta)>1`.
