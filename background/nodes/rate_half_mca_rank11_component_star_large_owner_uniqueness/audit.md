# Audit

The proof uses within-support cores, so no global-core containment is
silently assumed. Distinct pairs need differ in only one component; that one
nonzero degree-below-`K'` polynomial already gives the `K'-1` root cap.

Exact margins are

```text
2*22320=44640<67472,
(m'-44640)-(K'-1)=22833.
```

Both verifiers recompute these constants independently. The primary replay
also rejects six proof-critical mutations.
