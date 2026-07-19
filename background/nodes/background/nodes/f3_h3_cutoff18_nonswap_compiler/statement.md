# C36' cutoff-18 non-swap compiler

- **status:** PROVED
- **consumer:** `f3_h3_mobius_excess_half`

With `X_18` and `S_ns` defined in the critical packet,

```text
68X_18<=S_ns.
```

Therefore `S_ns<=1200n^2` implies the critical target
`17X_18<=300n^2`.

---

## Addendum — NARROWING r3 (2026-07-13, wave-5 audited import; catch #160b: strengthened form appended, original claim above preserved)

Put

```text
S_ns^rich=sum_(t!=1,P(t)>=19) [P(t)(P(t)-2)+D(t)]R(t).
```

Then

```text
68X_18<=S_ns^rich<=S_ns.
```

Therefore the strictly weaker estimate `S_ns^rich<=1200n^2` already implies
the critical target; the original full-`S_ns` form above is retained as the
strictly stronger envelope.
