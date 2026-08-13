# Dependency sub-DAG

```text
recursive exact-layer line bank --------+
                                         +--> layer slot cores --> MCA router
high/low actual-core capped dichotomy ---+
```

The node restores exact-layer ownership information after the aggregate
line-slot pigeonhole.  It supplies evidence to the existing rate-half MCA
routers and changes no critical-node status.
