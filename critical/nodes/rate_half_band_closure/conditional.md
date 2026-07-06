# rate_half_band_closure current status

- **status:** TARGET
- **closure:** open proof target

There is no active conditional proof of this node.

The older AQB-I conditional route is refuted: the averaging transfer is a
convex combination of single-box fiber counts, so the proposed box-sharing gain
is exactly canceled by the normalization.  The `aqb_average_member_transfer`
edge remains evidence/provenance only.

The later P6 dihedral-sibling route is also refuted by
`dihedral_sibling_window_certificate`: the proposed packet size is not a
Chebyshev top-degree drop, true Dickson fibers are too small in the first band,
and the endpoint sibling also overflows the degree budget.

The live full-determination target is therefore the strong closure statement in
`statement.md`: cover the rate-`1/2` band

```text
2^33 < sigma <= 8,592,912,738
```

by a genuinely new priced mechanism.  A bracket-grade obstruction for some band
radius is a valuable partial result, but it does not prove this node as consumed
by the full MCA/list adjacency parents.
