# External replay

Upstream commit:

```text
05ff2348de8f2c0f99683875ff12a9a79dcf21ec
```

Modal full-review run:

```text
https://modal.com/apps/allengrahamhart/main/ap-10gKNlNiUWfK3GabTPFRru
```

The preserved ledger is
`../rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_moving_upstream_review_gate/modal_review_output.json`
with raw SHA-256

```text
71c116c5bc1fccf5ce104a92948e91ebca66a90c685b13399362a258b68183e0
```

Relevant result: seven direct cells, transport, import, `M03` parity, normal
Python, and optimized-mode refusal all PASS. The full Python replay is:

```text
PASS aligned-positive moving closure verifier payload_sha256=343b691abab47586545aca75393bea1e1fff1dfb63537f059e4faef341893145 mutations=29
```
