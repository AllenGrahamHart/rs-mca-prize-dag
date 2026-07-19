# Budget-three antipodal intermediate cube-part router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_intermediate_hensel_certifier`

Retain `(IHC1)--(IHC9)` and the underlying pairwise-coprime quotient pencil.
For every valid intermediate candidate, write `C=C_u` and
`u=phi/theta`. The exact multiplied identity is the coprime factorization

```text
Rbar=theta C^3 L,       L=B+u z^h C,
gcd(B,C)=gcd(C,L)=1.                                  (ICR1)
```

If

```text
Rbar=lambda product_P P^m_P
```

is its irreducible factorization over the base field, define

```text
Cube(Rbar)=product_P P^floor(m_P/3).                  (ICR2)
```

Then every valid direction satisfies

```text
C | Cube(Rbar),
C^2 | gcd(Rbar,Rbar'),
C | gcd(Rbar,Rbar',Rbar'').                          (ICR3)
```

There is also an exact converse classifier. Enumerate normalized polynomials
`C` with

```text
C(0)=1,       deg C<=2h-2,       C^3 | Rbar,
L_C=Rbar/(theta C^3).                                (ICR4)
```

Such a `C` is an intermediate Hensel candidate exactly when

```text
L_C-B=u z^h C                                         (ICR5)
```

for a base-field scalar `u`. It is a valid intermediate pencil exactly when,
in addition, `W^4+theta W+theta u` splits into four distinct centered
parameters with the required fractional-linear matching to the deleted-root
lifts.

Thus polynomiality is an exact cube-part and cofactor test on the known
residual; it does not require a sampled formal-series prefix. This theorem
does not bound the official cube part, prove that `(ICR5)` always fails, or
close the adjacent crossing.
