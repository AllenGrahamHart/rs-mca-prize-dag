# Dependency sub-DAG

```text
F00/F01 (6)  F02/F03 (6)  F04--F07 R02/R11/R20 (12)
       \          |                    /
        \         |                   /
         moving ten (10) + balanced pair (2)
                         |
                         v
          aligned-positive 36-cell coverage (PROVED)
                         |
                         v
             source-line literal coverage (TARGET)
```
