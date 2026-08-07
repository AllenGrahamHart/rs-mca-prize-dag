# Dependency sub-DAG

```text
local source/quotient interfaces -----+
upstream #1141 exact GREEN packet ----+--> F02/F03 six-cell import
                                                  |
                                                  v
                               literal coverage TARGET (evidence)
```

The upstream proof objects are pinned by immutable commit and content hashes.
