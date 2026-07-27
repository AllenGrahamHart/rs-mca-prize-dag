# Critical proof-artifact recovery audit

Date: 2026-07-27.

## Canonical finding

Canonical commits `867ee19b`, `8806a46f`, and `342b52d9` established that the
historical `proof_sketch/` tree is not recoverable from any accessible tree or
history. The old references checker skipped such paths on the assumption that
their content had been copied into node folders. That assumption is false for
a substantial population.

The same guard, replayed in this worktree, currently reports:

```text
hollow legacy refs                    197
  PROVED                              112
  CONDITIONAL                           7
  CONJECTURE                            10
  PROVABLE                              22
  REFUTED                               10
  TARGET                                30
  WALL                                   6
hollow nodes on the critical surface   44
hollow critical nodes marked PROVED    42
empty-statement critical PROVED nodes  36
```

`tools/verify_prize_dag.py` now pins those local counts at `197` and `36`.
They may decrease as proofs and statements are reconstructed, but may not grow.

## Ruling

This is not evidence that all affected propositions are false, so a bulk
mathematical refutation or arbitrary status rewrite would be unsound. It is
conclusive evidence that the current tree cannot support a submission-ready
claim for those nodes. The joint goal's completion audit therefore requires
zero unresolved critical proof-artifact debt.

Recovery is route-driven: when an affected node becomes load-bearing, recover
its exact statement and write an in-tree proof, independently reconstruct the
needed theorem at the consumer's actual scope, or replace it with a proved
route. A legacy label and a passing structural DAG check are not proof.

The new E1 prime-field reduction is unaffected: its inputs and proof are
present in-tree and replayed by exact verifiers.
