# compiler

- **status:** PROVED
- **closure:** artifact semantics

Given an exact row descriptor, object denominator, convention axes, and
upper/lower count packets on agreement cells, the compiler emits one of
`SAFE`, `UNSAFE`, `CONDITIONAL`, or `UNKNOWN` per cell. It emits a
prize-facing adjacent certificate only when all axes and consumed packets are
`PROVED`, the unsafe and safe cells are consecutive, and the exact integer
inequalities straddle `floor(denominator/2^128)`.

Open axes, conjectural ledgers, absent adjacency, contradictory packets, and
ambiguous crossings fail closed.

