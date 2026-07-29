# Dependency sub-DAG

```text
rate_half_kb_degree60_decomposition_divisor_adapter [PROVED] --req--+
                                                                    v
                 rate_half_kb_decomposition_source_pencil_compiler [PROVED]
                                                                    ^
rate_half_kb_degree5_decomposition_exclusion [PROVED] --------req---+
                                                                    |
                                                                    +--ev-->
                                                rate_half_band_closure [TARGET]
```

The compiler reduces the distinct live degree rows from seven to six but
does not supply an owner charge.
