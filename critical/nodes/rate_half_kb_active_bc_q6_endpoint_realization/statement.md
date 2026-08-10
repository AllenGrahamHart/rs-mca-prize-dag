# Active balanced-core witness to Q6 endpoint realization

- **status:** TARGET
- **input:** canonical source certificates from the active BC compiler
- **output:** actual `Q=6,s=6,u=2` endpoint records and components

For every canonical active balanced-core source certificate, prove all
equality-wall hypotheses needed by the existing K3 endpoint chain and
construct an actual endpoint record and residual component on the same
received line. The map must preserve:

```text
affine slope; selected support; explaining data; first-match owner;
endpoint/source labels; chronology.
```

The endpoint parameter line and evaluation carrier remain distinct. Print an
injection or exact finite multiplicity for every certificate-to-record and
record-to-component fiber.

## Falsifier

A valid source certificate outside the `Q=6,s=6,u=2` hypotheses, a missing
actual component, changed owner/support/slope, a parameter/carrier
identification, or an uncontrolled realization fiber.
