# Proof

The independent Modal replay checked out upstream commit
`05ff2348de8f2c0f99683875ff12a9a79dcf21ec` and used the pinned PR #1144
compiler without modifying its algebra. Each selected direct cell ran in a
fresh Sage 10.9 process and emitted its required exact PASS marker:

| direct cell | payload |
|---|---|
| `M00-R02` | `c7a51a67c0bee0afcceeec67aa001b77957f265af9f54bbcb9e5d396adb31fe9` |
| `M00-R20` | `1b99f4383fce516553c5fa601aa56725a5eadf99e9ba7a2eb643d59a16ddf400` |
| `M01-R02` | `c3d2519a0ebde56ce3855658e08a24ca02d9ecfcca470b858fd6f33fe34bd73b` |
| `M01-R20` | `a280ddb2371258c2155900d22e84e9a8867d86a519adcd32d209a887e718eb76` |
| `M03-R02` | `44390de13c14dcd980364f6b4f492b24477984a337c95a20afdfd4c3506302e4` |
| `M03-R11` | `4a71077a836998f1ddedb75d8faf7ef48f5b9f00d05c8470e2000d5f45ebbf39` |
| `M03-R20` | `a0d55e0006e3e9ae851c74b3ca472fffdfc4a77799b3f4cf146846b0692d1acc` |

The direct-cell mode reconstructs the complete source and q-slice system,
factors before localization, retains every declared nonunit branch, and
asserts exact agreement with the certificate metrics. For `M03-R11`, it
also reconstructs both quotient-parity equations and verifies the terminal
named-open nilpotence witness.

The transport-only replay returned payload

```text
cd7de8f6eda007fee2cac220bb971a64eb3b59ad99dd1017a69ca7334ee5114b
```

and checks the complete `M01(b^-1)=M02(b)` source identity, q-slice targets,
named open, and quotient factors. Applying it only to the proved `R02` and
`R20` source cells gives the two `M02` conclusions in `(KBM10-1)`.

The import-only replay returned payload

```text
39247988d1a0cc806d191514c701928514ecebf3d42a5cf8002880fa2e8c1b50
```

and verifies the exact PR #1138 `M00-R11` commit, certificate, Sage object,
field, scope, conclusion, nonclaims, and prior GREEN review record.

Finally, the Python verifier returned the full certificate payload

```text
343b691abab47586545aca75393bea1e1fff1dfb63537f059e4faef341893145
```

with all 29 hostile semantic mutations rejected. The local verifier binds
the independent review ledger by SHA-256 and rejects either balanced
`M01/M02-R11` cell from the conclusion. Therefore exactly the ten systems
in `(KBM10-1)` are empty. QED.
