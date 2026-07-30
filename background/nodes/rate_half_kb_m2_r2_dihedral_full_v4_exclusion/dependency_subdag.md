# Dependency sub-DAG

```text
dihedral_outer_factor_reduction: n in {2,3,5,6} [PROVED]
  + degree2_source_star_exclusion [PROVED]
  + degree3_source_facet_exclusion [PROVED]
  + degree5_source_star_exclusion [PROVED]
  + degree6_common_pole_exclusion [PROVED]
      -> rate_half_kb_m2_r2_dihedral_full_v4_exclusion [PROVED]
          -> rate_half_band_closure [evidence]
```

The other two `m=2` stabilizer types remain outside this close.
