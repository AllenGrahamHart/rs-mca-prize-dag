# Audit

The primary and audit reconstruct the four equations separately after
loading the independent generic `5 x 5` source solver. The primary uses
successive ideal saturations; the audit uses one fresh Rabinowitsch variable
and no intermediate ideal from the primary.

The four Modal tasks all passed. Wall times were `30.43--51.13` seconds and
peak child RSS was at most `522344 KiB`.

Pinned SHA-256 values:

```text
primary source   0af9ac23b992663b905002ed3af0fc1d21f456cee4de37769f50cafe4b7bb9a8
audit source     6c970e9cd05d1ddb9279085fca09576b890f62177c43dac74bbe1bcae9b492f9
Modal wrapper    147572c07817d1d9bb4249ae76f30c4f2676b168edf6ce05ccc797fa0d738fb6
output           e3746c39c21ac49e5e1201029f36abfddd684c5d318c8f75f38bc545f84cfbbf
```

The exact exploratory lex census is not load-bearing. It first exposed the
common `c=d` support, after which the theorem was replayed directly by the
two proof paths above.
