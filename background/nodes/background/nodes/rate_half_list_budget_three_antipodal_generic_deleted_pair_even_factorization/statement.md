# Budget-three antipodal generic deleted-pair even factorization

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_parity_reduction`,
  `rate_half_list_budget_three_antipodal_generic_canonical_span_criterion`

Retain the maximal generic floor with `d=16M`, `h=2M+1`, and suppose the
four deleted roots are two antipodal pairs. Normalize their squared ratio to
`t in mu_(8M)\{1}` and put `w=z^2`. If a candidate passes the primary and
secondary gaps and the complete canonical span/splitting criterion, write

```text
Q_0(w)=(1-w^(8M))/((1-w)(1-tw)),
B(z)=B_0(w),       Cbar(z)=C_0(w).                    (DEF1)
```

Then the odd canonical coefficient is forced to vanish:

```text
beta=0.                                               (DEF2)
```

There are distinct nonzero `lambda,mu` in the base field, with
`lambda+mu=alpha` and `lambda mu=gamma`, such that

```text
Q_0(w)
 =(B_0(w)^2+lambda w^(2M+1)C_0(w)^2)
  (B_0(w)^2+mu     w^(2M+1)C_0(w)^2).                (DEF3)
```

Both factors have constant term one and exact degree `4M-1`. They are
coprime and their roots partition

```text
mu_(8M) \ {1,t^(-1)}.                                (DEF4)
```

Let `A_lambda,A_mu` be the two root cells. Their inverse-root power sums have
the exact flat prefix

```text
sum_(a in A_lambda)a^(-j)
 =sum_(a in A_mu)a^(-j)=-(1+t^j)/2,       1<=j<=2M, (DEF5)
```

and the first difference is printed:

```text
sum_(a in A_lambda)a^(-h)-sum_(a in A_mu)a^(-h)
 =-h(lambda-mu),       h=2M+1.                       (DEF6)
```

Thus any surviving deleted-pair candidate is an exact two-cell square-pencil
factorization with a half-length flat Fourier prefix on the punctured
`8M`-torsion binomial. This theorem does not classify or exclude
factorizations `(DEF3)`.
