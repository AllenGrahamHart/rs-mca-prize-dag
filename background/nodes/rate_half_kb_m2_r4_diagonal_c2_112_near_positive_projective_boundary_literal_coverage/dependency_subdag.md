# Dependency sub-DAG

```text
ramified complete-source repair [PROVED] --\
internal-star reconstruction [PROVED] -----+--> boundary literal coverage [PROVED]
q-slice resultant gate [PROVED] ----------/                         |
                                                                    +--ev--> literal coverage [TARGET]
```

The new leaf does not use the old seven-shard normalization to infer literal
coverage. It reconstructs all 48 cells in the fixed literal frame.
