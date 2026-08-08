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

## Standalone Singular route fence

Direct Singular removes the failing Sage basis-conversion bridge. Three
bounded runs at the same pinned source recover the exact common prefix:

```text
q-slice basis size 168, dimension 2
J remainder degree 21, 6510 terms
J basis size 174, dimension 2
w=0 basis size 35, dimension 1, localizer square zero (staged run)
```

The 1740-second staged and monolithic runs stop before completing the `I`
normal form. A 3540-second run decomposes the exact 151178-term `I` input
into 148 blocks of 1024 terms, but stops before its first eight-block progress
checkpoint. Peak child RSS is below 4.70 GiB in all three runs. The route is
therefore memory-safe remotely but computationally unsuitable in this form.

```text
staged:    https://modal.com/apps/allengrahamhart/main/ap-IMd9cUzIUpWLnRcL1OarSo
monolithic:https://modal.com/apps/allengrahamhart/main/ap-D9i2YWXIRRNOgw0Gta35QD
chunked:   https://modal.com/apps/allengrahamhart/main/ap-wjo20K1vuWBR0ei6u4HhuU
```

Pinned raw SHA-256 values:

```text
certificate  da9273a631a0f88056ba57433fc5ff2c9ced4f223e0aa6ad515744c765431855
schema       659772381a053d2f0e0598a0dfc91502065b07c6685f0fdebb22486f8bf6c41b
Python       13fab1b9fc1c77b7cc880f52194ab212c040eab946edc851f24891de09ff71a0
Sage         2ed13fbab353d0ac3017fa31cab68de3f3b66f190061ba63fd277dbdc7958675
theorem note 14130c7ebd867487e28393fc815dc99e150626b19b6e7f88baba449792cbf6ff
direct Sage  3dbc9582186ab26f891b46c579565ccb796bde2a544b7de76ae4754afd50a7ba
Modal wrap   6b75c78fee905a0707d6968ca2d3399dcbe9b986f4e2e767b0909575f246e04b
staged out   d21e707c9728259e4c3e44225167bc3928fbb37fc7d465eca6851d969cbe0384
mono out     641e48ad765e58c42959a72206ac056c9e66b74cf7722bf2e36958a3e9c00333
chunked out  0d8e525bac83f54ca4623e5520c07214a9dbdce84a4b82e69a87b8202b0caf37
```
