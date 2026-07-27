# Audit

- The mask atlas has one affine orbit for each of `1,234` masks.
- The production relaxation uses a signed zero-sum kernel and incremental
  four-plus-two scoring.
- The audit relaxation derives coefficients from cyclic base vectors and pair
  sums, then scores a three-plus-three decomposition.
- The production actual engine uses folded oriented chords.
- The audit actual engine multiplies directly in `Z[X]/(X^128+1)`.
- The two relaxation engines agree row by row on `44,779,702,968` assignments.
- The two actual engines agree row by row on `23,638,891,776` vectors.
- FLINT and PARI agree entry by entry on all `1,232` primitive resultants.
- The actual audit checkpointed at `864/1,191` when the local launcher reached
  its wall limit, then resumed only the remaining `327` tasks to completion.

Modal applications:

```text
relaxation production  ap-R8qZ3NFpBLlaSCjEPobazm
relaxation audit       ap-HhZLnYkj1E6sx207Qc1FwO
actual production      ap-tzoEgc0dyKoBc3yghLmKLF
actual audit partial   ap-NXOjRlg7idEiFtq2ALTgxX
actual audit resume    ap-BZCZ0tCpInuxZwZoxLl7V4
exact norms            ap-BngTsJiGLxbGZxPkOOPRU6
```

Aggregate worker time was `180.698917` seconds for the two relaxations,
`7,022.563690` seconds for the two actual engines, and `4.108949` seconds for
the two norm engines. Every remote task used 256 MiB.
