# Low-budget rate-half list certificate generator

- **status:** PROVED
- **closure:** artifact semantics
- **consumer:** `list_grand`

There is a deterministic, fail-closed map from a canonical
`prize-row-input-v1` object and an explicit object selector in
`{LIST, INTERLEAVED_LIST}` to a self-contained adjacent-crossing certificate
on precisely the proved rate-half branches

```text
B*=floor(|F|/2^128) in {1,2}.
```

For `LIST` the certificate has arity one. For `INTERLEAVED_LIST` it records
scope over every positive common-support arity. In both cases it emits

```text
unsafe agreement = 3n/4-1,
safe agreement   = 3n/4,
largest safe closed radius numerator = n/4,
next boundary numerator              = n/4+1 (not attained).
```

The output contains the canonical row descriptor, theorem claim identifier,
proved upper and lower packets, all four compiler axes, compiler output, exact
endpoint, and the descriptor's external row preconditions. Inputs outside the
proved rate, budget, length, or object scope are rejected rather than assigned
a conditional or guessed certificate.
