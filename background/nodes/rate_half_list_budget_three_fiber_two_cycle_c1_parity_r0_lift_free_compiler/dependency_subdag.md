# Dependency sub-DAG

```text
c=1 nonharmonic scalar compiler [PROVED] --------+
c=1 Frobenius router [PROVED] -------------------+
                                                  v
                              R0 lift-free compiler [PROVED]
                                    --evidence--> adjacent crossing [TARGET]
```

The node removes a lift variable and produces a constant-size selector. It
does not turn the official Legendre gate into a bounded computation.

