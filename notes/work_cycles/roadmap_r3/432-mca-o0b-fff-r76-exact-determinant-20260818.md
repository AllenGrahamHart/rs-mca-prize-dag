## MCA O0b `FFF` exact `R76` determinant (2026-08-18)

### Exact theorem input

The determinant of the column-cleared `R76` multiplication matrix is now an
explicit polynomial in `GF(2130706433)[t]`:

```text
degree:       19060
nonzero terms: 18711
```

The reconstruction used a 32,768-point NTT. Completeness is deterministic:
the matrix-entry degree bound gives `deg det(P)<=22208<32768`, and every
inverse-transform coefficient above 22208 was zero.

Two direct matrix evaluations independently verify the recovered polynomial:

```text
det(P(2)) = 1087830147
det(P(3)) = 1736903607.
```

Modal app: `ap-JRNgbYBHv9QaOl3g3LaTBx`; coefficient SHA-256:
`4f34c966c8cc12eb1b40227b9b7a7d6b232fba7990c2e55e09608cdbc3469ae5`;
result SHA-256:
`a222789bb3e54df1a4198536644a6d331972087d968b61b227634eca22a79786`.

### Consequence

For every `t` where all sixteen column LCMs are nonzero,

```text
det(P(t)) != 0
```

implies the rational `R76` multiplication matrix is invertible. Therefore
`R76` is a unit in the specialized `q5` quotient and `q7,q6` cannot have a
common solution. The remaining candidate fibers are exactly the base-field
roots of the determinant together with every transformation denominator.

### Next exact action

Use FLINT to form an LCM across:

1. the determinant polynomial;
2. the sixteen column LCMs;
3. generic-basis and q5-extension denominators;
4. q5 multiplication and kernel-normal denominators; and
5. q7-coefficient denominators.

Compute the base-field root part by `gcd(H,t^p-t)`, factor it into linear
terms, and retain the exact root list. Those roots become the complete
specialization workboard for the original necessary subsystem.

### Status discipline

The determinant is proved and exact. The `FFF` chart remains open until all
roots in the complete transformation ledger are replayed against the
original equations.
