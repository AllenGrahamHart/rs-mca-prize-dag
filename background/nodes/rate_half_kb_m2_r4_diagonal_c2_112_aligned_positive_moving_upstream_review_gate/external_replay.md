# External replay

Detached commit: `05ff2348de8f2c0f99683875ff12a9a79dcf21ec`

Command:

```text
python3 experimental/scripts/verify_kb_mca_v4_m2_aligned_positive_moving_closure_v1.py --check --tamper-selftest
```

Output:

```text
PASS aligned-positive moving closure verifier payload_sha256=343b691abab47586545aca75393bea1e1fff1dfb63537f059e4faef341893145 mutations=29
```

## Independent Sage review

The full sharded Sage 10.9 review ran at:

```text
https://modal.com/apps/allengrahamhart/main/ap-10gKNlNiUWfK3GabTPFRru
```

Thirteen of fourteen checks passed. Seven direct cells, transport, import,
both standalone parity derivations, the Python verifier, and optimized-mode
refusal passed. The complete `M01-R11` direct cell failed while Sage compiled
the large basis expression returned by external Singular:

```text
RecursionError: maximum recursion depth exceeded during compilation
```

The failure was independently reproduced under:

```text
conda Sage 10.7:
https://modal.com/apps/allengrahamhart/main/ap-OymjIWQ3IdqMYPrlqHeXzl

official SageMath 10.9:
https://modal.com/apps/allengrahamhart/main/ap-fGiDmeLqL0dHnjIqmzs01e
```

An alternate review changed only the two backend selectors from external
`singular:slimgb` to in-process `libsingular:slimgb`. It avoided the bridge
exception but reached the bounded 1740-second subprocess timeout:

```text
https://modal.com/apps/allengrahamhart/main/ap-BfXZZx4jVTADDgcfmfgAcz
```

No failed or timed-out computation is used as a theorem. The successful
subset is banked in the sibling ten-cell node; this gate retains exactly
`M01-R11` and its `M02-R11` transport companion.

Pinned raw SHA-256 values:

```text
certificate  da9273a631a0f88056ba57433fc5ff2c9ced4f223e0aa6ad515744c765431855
schema       659772381a053d2f0e0598a0dfc91502065b07c6685f0fdebb22486f8bf6c41b
Python       13fab1b9fc1c77b7cc880f52194ab212c040eab946edc851f24891de09ff71a0
Sage         2ed13fbab353d0ac3017fa31cab68de3f3b66f190061ba63fd277dbdc7958675
theorem note 14130c7ebd867487e28393fc815dc99e150626b19b6e7f88baba449792cbf6ff
```
