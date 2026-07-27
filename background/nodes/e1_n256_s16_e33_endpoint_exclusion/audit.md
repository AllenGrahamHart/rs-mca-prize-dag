# Audit

- The parent verifier independently enumerates all 21 energy-33 profiles and
  confirms the four-profile reduction.
- Each of the four child exclusions has a separate proof packet and audit.
- The synthesis verifier checks the exact profile set, all five requirement
  edges, both evidence edges, and every dependency status.
- Mutation controls reject omission of any child and insertion of a fifth
  profile.
