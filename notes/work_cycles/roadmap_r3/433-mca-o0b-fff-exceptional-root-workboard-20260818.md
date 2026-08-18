## MCA O0b `FFF` exceptional-root workboard (2026-08-18)

### Exhaustive root set

Across every rational transformation used by the generic proof and the exact
cleared determinant, the complete base-field exceptional set is

```text
0
1
16711679
47655010
451278922
465887767
666570304
676802667
1036595577
1141382033
1629292471
1893783428
2113994754
2130706432
```

The global exceptional LCM has degree 19060. Its base-field root part has
degree fourteen. The exact determinant contributes all fourteen roots and
already contains the union from every denominator group.

Modal app: `ap-5hqyVNmIQiOaC6j0YkZe3N`; root-polynomial SHA-256:
`3589dc59d90716f76248f83b667411527fda6ceaff5b845b9dc673afbc5d4592`;
result SHA-256:
`e845607b89e7d21159bd308cbf00f9a3fd74a25120bc4d479a607f7e9d8751a7`.

### Proven generic coverage

For every other `t` in `GF(2130706433)`, all transformations are defined and
the cleared determinant is nonzero. Therefore `R76` is a unit in the q5
quotient and the `FFF` necessary subsystem is empty.

### Specialization rule

Each of the fourteen roots must be replayed from denominator-free generators:

1. use the original admissible ratio-graph equations and guards over the
   prime field;
2. append `t-t0`;
3. impose original `q5`, `q7`, and `q6` equations from the cached packet;
4. prove the guarded ideal is the unit ideal, or retain an exact survivor;
5. do not specialize the generic rational Groebner basis or multiplication
   matrices at these roots.

The fourteen independent fibers can be sharded across Modal containers with
per-root checkpoints.

### Status discipline

The generic family is fully covered and the finite workboard is exhaustive.
The `FFF` chart remains open until every listed root is closed against the
original system.
