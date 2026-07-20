# Audit

The invariant is the cubic binary-quartic invariant, not the elliptic
`j`-invariant. Only its zero locus is used. The coefficient convention is
fixed by the normalized identity

```text
J(XY(X-Y)(X-lambda Y))
 =(1+lambda)(2lambda-1)(lambda-2).
```

The eight factors range over sign classes modulo simultaneous negation. There
are not sixteen independent factors because `J(F(X))=J(F(-X))`.

Squarefreeness of `D` is essential for applying the cross-ratio criterion:
it guarantees distinct roots for every signed lift quartic. Characteristics
`2` and `3` are excluded explicitly; they do not occur on the official rows.

The attempted full symbolic expansion exceeded the guarded tiny-local wall
limit. That expansion is neither needed nor requested: `(BQN3)` evaluates
the exact support gate using three quadratic norms, while `(BQN4)--(BQN5)`
evaluate it directly in the four deleted roots without choosing square
roots. Both are much smaller independently checkable certificates.
