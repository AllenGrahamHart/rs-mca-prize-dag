# Dependency Sub-DAG

```text
cell-4 xi3 pairing-0 exclusion [PROVED] --------+
                                                   +--> cell-4 xi4 pairing-0
universal xi4 -> xi3 transport [PROVED] ---------+    exclusion [PROVED]
                                                            |
                                                            v evidence
                                                   rate_half_band_closure [RED]
```

Both required parents are PROVED. No conditional or computational leaf is
introduced by this transport application.
