# KoalaBear m12 secondary degree-five decomposition exclusion

- **status:** PROVED
- **scope:** last inner-degree-12 transverse type `(r,delta)=(4,12)`
- **dependencies:** `rate_half_kb_m12_diagonal_socle_route_cut`,
  `rate_half_kb_degree5_decomposition_exclusion`
- **consumer:** `rate_half_band_closure`

The full diagonal simple socle on the five degree-12 blocks forces a second
block system for the degree-60 geometric monodromy: twelve columns, each of
size five. Indeed, after equivariantly identifying the five equal degree-12
socle actions, every monodromy element acts by one common permutation on the
12-point coordinate and by its outer permutation on the five blocks. The
common-permutation assertion follows because the centralizer of a faithful
nonregular two-transitive action is trivial.

The size-five column blocks give a second functional decomposition of the
endpoint map with inner degree five. The proved deployed-field degree-five
decomposition exclusion applies to every such geometric decomposition and
rules it out. Therefore

```text
the inner-degree-12 branch is empty.                  (KBS-1)
```

All five `r=4` normal-form families are deleted as actual producers. The
distinct live decomposition degrees are now

```text
{2,3,4,6,10}.
```

This closes `m=12` only. It does not close the other five degrees, construct
an owner, move the ledger, close `u=2`, establish cap `68`, certify the
adjacent crossing, or close the KoalaBear row.

## Falsifier

A nonidentity centralizer of one of the faithful degree-12 simple-socle
actions, a normalizer of the full diagonal socle that does not preserve the
size-five column partition, failure of that partition to yield an inner-
degree-five decomposition, or failure of the proved degree-five exclusion
for the secondary decomposition.
