# Dependency sub-DAG

```text
mismatch trace-resolvent elimination [PROVED] --+
c=2 outer torsion-trace gate [PROVED] ----------+
                                                  v
                         joint pair-torsion selector [PROVED]
                                  --evidence--> adjacent crossing [TARGET]
```

The new node intersects the two existing necessary equations at the same
trace value. It removes outer-only false positives but retains all later
canonical-span, gap, and cycle conditions.
