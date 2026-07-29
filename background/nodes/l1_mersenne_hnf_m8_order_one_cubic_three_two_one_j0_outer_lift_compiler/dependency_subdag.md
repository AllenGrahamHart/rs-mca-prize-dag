# Dependency sub-DAG

```text
J-zero role/P_4 compiler [PROVED] -------------------------+
3+2+1 factor reduction [PROVED] ---------------------------+
official Frobenius-role split [PROVED] --------------------+
order-one Frobenius gate [PROVED] -------------------------+--req-->
coefficient-field degree-eight router [PROVED] ------------+        |
                                                                    v
                                      J-zero outer-lift compiler [PROVED]
                                                                    |
                                                                    +--ev-->
                                                  l1_mixed_petal_amplification [TARGET]
```

The new node compiles only the outer replay of a retained J-zero role
candidate. It leaves the actual common roots, guards, replay outcomes,
inner lift, other shapes, and critical target open.
