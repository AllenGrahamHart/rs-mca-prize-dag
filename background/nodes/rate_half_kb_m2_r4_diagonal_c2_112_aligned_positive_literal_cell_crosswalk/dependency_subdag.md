# Dependency sub-DAG

```text
source reconstruction ----+
                          +--> literal-cell crosswalk
q-slice pair compiler ----+              |
                                         v
                          literal-assignment coverage target
```

The outgoing edge is evidence. The crosswalk does not turn a canonical
cell proof into an all-assignment theorem.
