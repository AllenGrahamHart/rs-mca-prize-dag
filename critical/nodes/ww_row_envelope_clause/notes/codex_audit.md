# Audit: W3 direct re-pose

## Finding: FIXED

The node packet had retired K_cell, but the authoritative DAG statement still
asserted count <= C*K_cell/q^sigma with no independent definition or
certificate semantics for K_cell. A secondary direct_repose_20260712 field
said that a different statement was binding. This violated the single-source
rule and left consumers dependent on which field a reader selected.

The DAG statement now matches the packet exactly: bound the actual challenger
count by the exact conservative residual integer budget. K_cell is retained
only as historical route vocabulary and cannot be consumed as a premise.

This repair does not prove the direct count.
