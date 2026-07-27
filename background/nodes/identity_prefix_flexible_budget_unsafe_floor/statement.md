# Identity-prefix flexible-budget unsafe floor

- **status:** PROVED
- **closure:** proof

Let `B <= F` be finite fields, let `D subset B` have size `n`, and let
`C=RS[F,D,k]`, where `q=|F|>n`. Fix `k+1 <= m <= n`, a target exponent `t`,
and put

```text
w = m-k-1,
B* = floor(q/2^t),
L0 = B*+1.
```

If

```text
binom(n,m) > |B|^w B*
binom(B*+1,2) k < q-n,
```

then one simple-pole received line has at least `B*+1` distinct ambient-field
slopes that are support-wise MCA-bad at agreement `m`. Consequently

```text
B_C(m) > B*,
epsilon_mca(C,1-m/n) > 2^-t.
```

If the pole is required outside `B`, the same conclusion holds with the
second right-hand side replaced by `q-|B|`; the resulting line is not
projectively `B`-rational.

This is a lower-bound theorem. Failure of either sufficient inequality is not
a safety certificate.
