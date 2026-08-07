# Dependency sub-DAG

```text
upstream #1144 exact candidate + Python replay
                         |
                         v
             moving review gate (PROVABLE)
                         |
                         v
          literal coverage TARGET (evidence only)
```

No logical requirement edge is used until the review gate is discharged.
