# `A=1` core-one exceptional-only Hankel factor pin

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_middle_adjugate_factorization`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_full_reciprocal_square_descent`

Retain the official `b=0,D_*=1,c=z=1` exceptional-only face. Then the full
residual generator is the dominant component, its exceptional supported
fiber at `E=0` is squarefree of degree `r-1`, and every ordinary supported
fiber has nominal degree `r=d=2e+1`.

Let `M` and the primitive coefficient vector
`q=(q_0,...,q_r)^T` be as in `(MAF2)--(MAF4)`. There is a nonzero field
scalar `c_H` such that the middle-Hankel adjugate is exactly

```text
adj M=c_H E q q^T.                                  (HFP1)
```

In particular,

```text
gcd(nonzero maximal minors of M)=E                  (HFP2)
```

up to a nonzero field scalar. After dividing every cofactor by `E`, the
exceptional specialization is the nonzero rank-one matrix

```text
(adj M/E)|_(E=0)=c_H q(gamma_0)q(gamma_0)^T.        (HFP3)
```

The reciprocal infinity coefficient is the top kernel coordinate

```text
q_r=[X^r]Q=E q_bar.                                 (HFP4)
```

Hence the top cofactor row and column vanish in `(HFP3)`, while the full
quotient matrix remains nonzero of rank one. Globally the pinned entries are

```text
(adj M)_(i,r)=c_H E^2 q_i q_bar,
(adj M)_(r,r)=c_H E^3 q_bar^2.                      (HFP5)
```

No square root of `c_H` is assumed, and no exact `E`-adic valuation beyond
the displayed polynomial identities is claimed. This pins the Hankel factor
used by the reciprocal classifier but does not exclude the corrected square.
