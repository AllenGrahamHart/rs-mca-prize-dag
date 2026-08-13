# Dependency sub-DAG

```text
recursive affine-line peeling ---------+
                                        +--> joint-core charge --> MCA router
total-core line packing ---------------+
```

Both parents are `PROVED`.  The new node replaces the independent
worst-case line charges by their joint convex envelope.
