# Round-18 F2 branch-split node replay preregistration

## Fixed inputs

- compiled `dag.json` after the minus-branch scope correction;
- the plus-branch direct-sum, Newton-distance, and weighted-L2 node packets;
- the all-admissible direct-sum counterexample node;
- the repaired `f2_conditional_close` packet;
- the already banked direct-sum replay and counterexample result JSON files.

## Pass condition

One isolated Modal container runs all five node verifiers. PASS requires
five zero return codes and each verifier's own DAG/status assertions. No
search, sampling, or parameter tuning occurs in this replay.

## Resource ceiling

One CPU, 1024 MiB RAM, one container, 120-second function timeout, no
retries. The launcher records partial stdout and stderr on failure.

## Result

Modal app `ap-nC5KaETV5g1U6tiXAhfyDg` returned PASS. All five node verifiers
exited zero, including 328,240 signed-distance checks and the repaired
`5/5` status, `6/6` edge contract.
