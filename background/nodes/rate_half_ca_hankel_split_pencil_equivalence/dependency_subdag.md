# Dependency sub-DAG

```text
rate_half_ca_hankel_split_pencil_equivalence [PROVED]
  --ev--> rate_half_band_closure [TARGET]

spi_component_control [PROVED]       (crosswalk only)
spi_exceptional_class [PROVED]       (crosswalk only)
spi_point_counting [CONDITIONAL]     (generic count remains open)
```

No SPI node is a logical dependency of the equivalence. The crosswalk
identifies reusable machinery without importing a quantitatively insufficient
or conditional point bound.
