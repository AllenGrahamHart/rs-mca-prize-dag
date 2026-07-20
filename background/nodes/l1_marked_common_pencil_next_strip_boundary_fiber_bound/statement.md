# L1 marked common-pencil next-strip boundary fiber bound

- **status:** PROVED
- **role:** bound numerator multiplicity on the thin edge omitted by the
  strict Forney window
- **consumers:** `l1_quotient_chart_bounded_core_boundary_closure`,
  `l1_mixed_residual_intersection_pin`, `l1_mixed_petal_amplification`,
  `petal_mixed_amplification`

## Statement

Work in one bounded-polarity common-pencil chart with exact list-threshold
parameters. Let `t` be the number of dense petals, let their total mark
degree be `v<=p`, and suppose

```text
p<=P_0,       ell>2P_0,
m ell<d<(m+1)ell,       d+p>=(m+1)ell.                (NB1)
```

Put

```text
g=(m+1)ell-d,       1<=g<=p.                         (NB2)
```

The list threshold forces

```text
t>=m+1.                                                (NB3)
```

For fixed exact supports, marks, and defect locator `F`, write

```text
S=product_i S_i,       deg S=t ell-v,
S_i | W-c_iF.                                          (NB4)
```

The numerator solutions form one CRT class modulo `S`. If `v<g`, there is at
most one degree-at-most-`d` numerator. If `v>=g`, there are at most

```text
q^(v-g+1)<=q^p                                         (NB5)
```

such numerators. Thus the entire thin next-strip edge has fixed-locator
numerator multiplicity at most `q^p`, uniformly in `m,d`.

## Scope

The theorem assumes every dense petal used in the count lies in one common
constant-shift pencil. It does not count support patterns or defect locators,
aggregate source charts, or treat arbitrary petal locators. The condition
`ell>2P_0` is automatic eventually at the L1 cutoff for fixed `P_0`.

