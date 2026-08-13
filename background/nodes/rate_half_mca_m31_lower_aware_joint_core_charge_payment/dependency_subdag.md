# Dependency sub-DAG

```text
joint-core charge theorem -------------------+
                                              +--> lower-aware charge --> MCA router
recursive line bank + distinct-core packing -+
```

The node strengthens only the charge used for lines already peeled by the
parent recursion.  It supplies evidence to the two existing rate-half MCA
routers and does not change a critical-node status.
