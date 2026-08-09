# Proof

At each source point use the pointwise kernel from
`(KBP1B9-BASE-REG-1)`.  For omitted record `xi`, impose its recovered product
and squared sum.  Delete it from

```text
de, de, -de, df, sigma_o ef, bf, sigma_c cf
```

and impose the three exact paired-resultant equations for each of the 15
perfect matchings of the six residual records.  Finally invert the product
of all nonzero, distinct, and non-antipodal guards on
`1,b,c,d,e,f`.

The exhaustive ledger contains

```text
8 source points * 7 omitted records * 4 target lanes * 15 matchings
  = 3360 systems.
```

Exact Singular reduction gives dimension `-1`, basis size one, and basis
`{1}` in every system.  Therefore every guarded target lift is empty, for
all seven outside roles at all eight source points. QED.
