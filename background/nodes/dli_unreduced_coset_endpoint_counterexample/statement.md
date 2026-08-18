# Unreduced DLI coset endpoint counterexample

- **status:** PROVED

At the admissible rate-half row

```text
n = 2^41,  t = 2^33,
k_RS = 2^40,
q = 115792089237316195423570985008687907766497981100801255856297059112812235718657,
```

the normalized count of all central `t`-null subsets, **before** removal of
the quotient-periodic column, is greater than `2^126`.  In particular, the
unreduced endpoint `X <= 2^121` is false.

Every member of the exhibited family is periodic under the order-`2^34`
subgroup and is therefore nonprimitive.  The counterexample does not attack
the primitive residue required by `x4_exactlist_staircase_split`; it proves
that the DLI consumer and its joint-reserve premise must use the explicitly
reduced object

```text
X_prim = q^(-t+H) W_cen^prim = E_U[product_j rho_j]_reduced.
```
