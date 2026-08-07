# Sharp rate-half FPC5 pure dyadic quotient absence

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t2_payment`

At the official rate-half sharp endpoint,

```text
n=2^41,       5ell=k+4,       j=2ell-3.
```

The split-locator intersection

```text
P(V_F) intersect D_j(C)
```

contains no proper multiplicatively periodic locator. More precisely, for
every `M>1` dividing `n`, there is no degree-`j` locator of the form

```text
F(X)=g(X^M),                                            (QA1)
```

and no `j`-point root set in `H_n` that is a union of complete
`mu_M`-orbits.

## Scope

This removes the pure multiplicative quotient-pullback stratum from the sharp
flat. It does not remove incomplete-orbit/tail forms `L_B(X)g(X^M)`, general
rational pullbacks, or reciprocal/dihedral symmetry. Those classes can have
odd total degree and require separate ownership or counting arguments.
