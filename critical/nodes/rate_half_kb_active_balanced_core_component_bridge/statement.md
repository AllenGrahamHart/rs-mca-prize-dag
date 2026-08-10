# Active balanced-core bad-slope to component bridge

- **status:** TARGET
- **row:** deployed KoalaBear MCA at agreement `1116048`
- **partition:** Grande Finale v4, digest
  `4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc`
- **domain:** the first-match cell `Z_BC`
- **unit:** distinct bad finite slopes per received line

For every active slope, construct an actual endpoint record and residual
component while preserving the received line, chosen noncommon witness
support, affine slope, and first-match chronology. Prove that the existing
decomposition chain applies and leaves exactly

```text
(m,r,delta)=(2,4,2) or (2,8,1).
```

The map must be exhaustive and disjoint. It must print an injective
assignment or exact finite fiber multiplicities sufficient to sum payments
over endpoint records. The endpoint parameter line remains distinct from the
evaluation carrier; no coordinate identification between them is allowed.

## Falsifier

An active `Z_BC` slope outside the endpoint-component domain, a lost owner or
slope, an omitted live type, or an unpriced fiber of the assignment.
