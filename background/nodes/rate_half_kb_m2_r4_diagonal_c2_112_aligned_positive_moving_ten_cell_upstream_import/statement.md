# KoalaBear aligned-positive moving ten-cell upstream import

- **status:** PROVED
- **scope:** ten literal moving aligned-positive cells over
  `F_(2130706433^6)`
- **provenance:** Przemek repository PR #1144, exact commit
  `05ff2348de8f2c0f99683875ff12a9a79dcf21ec`
- **consumer:** source-line literal-assignment coverage

The following ten named-open systems are empty:

```text
M00-R02, M00-R11, M00-R20,
M01-R02,          M01-R20,
M02-R02,          M02-R20,
M03-R02, M03-R11, M03-R20.                         (KBM10-1)
```

Seven cells in `(KBM10-1)` were independently rebuilt and localized in
fresh Sage 10.9/Singular processes. `M00-R11` was independently checked as
the exact operational import from the GREEN PR #1138 object. The complete
literal `b -> b^-1` transport was replayed and sends the proved `M01-R02`
and `M01-R20` cells to `M02-R02` and `M02-R20`.

The direct `M03-R11` replay includes the full `J/I` parity chain and exact
nilpotence terminal. Its separate parity derivation also passed. The
fail-closed Python certificate verifier passed all 29 semantic mutations,
and optimized execution was rejected as required.

This theorem does not claim `M01-R11` or `M02-R11`. The external
Sage/Singular text bridge fails while returning the large `M01-R11`
Groebner basis in three independent Sage environments. Those two cells
remain in the sibling review-gate node.

## Falsifier

A failed direct-cell PASS marker, failed operational import, failed literal
transport, a content-pin mismatch, or an attempt to include either balanced
`M01/M02-R11` cell in this ten-cell conclusion.
