# L1 polarized B11 box closure

- **status:** PROVED
- **role:** close every bounded polarized-entropy/cofactor-excess box
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Work in one maximal-sunflower chart at the L1 lower cutoff. For a
non-planted listed word put

```text
p=sum_i min(a_i,ell-a_i),       a_i=|S_i|,
d=exact missed-core defect.
```

For every fixed pair of nonnegative integers `P,E`, the full class

```text
p<=P,       d<=ell+E                                      (PB1)
```

is polynomially bounded in `n`.

More precisely, every word in `(PB1)` satisfies the automatic B11 gate

```text
G_2<=2P       or       G_R<=P.                            (PB2)
```

If `ell>P`, the first bound improves to `G_2<=P` whenever two or more petals
are dense. If exactly one petal is dense, then `G_R<=p<=P`.

Consequently, after proved payments, any super-polynomial mixed/partial
family must escape every fixed two-parameter box:

```text
p -> infinity       or       d-ell -> infinity.           (PB3)
```

The sequence notation means that for every fixed `P,E`, the residual lies in
`p>P or d>ell+E`; it does not assert that one coordinate grows uniformly
without passing to a subfamily.

## Scope

This theorem does not count the union of the two growing branches in `(PB3)`,
classify a natural-scale owner, or promote either target.
