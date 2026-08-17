## MCA O0b `FFF` R76 bracket bank (2026-08-17)

### Exact result

The progressive quotient prefix is now materialized as a complete,
hash-pinned 14-polynomial bracket bank:

```text
M0: 5 representatives; M0[2] = 0
M1: 5 representatives; M1[0] = 0
M2: 4 representatives; all nonzero
nonzero term range: 1,117--1,202
result hash: 08dc7fefd108d4b8d17a1c7a5345f37312b65b9a74389cf7e7dfc94827b0446f
Modal app:   ap-WkUJ6xUaL50A2ireij9cYb
```

All 14 individual polynomial hashes are recorded in the result artifact and
recomputed by the hostile checker. The 61-stage prefix no longer needs to be
rerun.

### Sparse final identities

Writing

```text
M0 = [a,b,0,c,d]
M1 = [0,e,f,g,h]
M2 = [i,j,k,l],
```

the final coefficients are

```text
R0 = a^2
R1 = 2ab - ei
R2 = b^2 - ej - fi
R3 = 2ac - ek - fj - gi
R4 = 2ad + 2bc - el - fk - gj - hi
R5 = 2bd - fl - gk - hj
R6 = c^2 - gl - hk
R7 = 2cd - hl
R8 = d^2.
```

These identities are the next exact DAG payload; they preserve the two zero
brackets and avoid all unnecessary products.

### Next decision gate

1. Split each distinct nonzero bracket product into deterministic term
   blocks and reduce each block modulo the 48-element graph basis.
2. Cache repeated products across the nine coefficients and assemble each
   coefficient only after every block hash passes.
3. Prefer a small pilot on `R0=a^2` to calibrate block size and cost before
   launching the full sparse product ledger.
4. No monolithic square or raw resultant expansion is permitted.
