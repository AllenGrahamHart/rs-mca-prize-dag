# H3 non-swap moment reduction

- **status:** see `dag.json` (single source of truth)
- **role:** proved background reduction for the C36' weighted leaf

Put

```text
D(t)=#{a in A : a^2=t}
S_ns=sum_(t!=1) [P(t)(P(t)-2)+D(t)]R(t).
```

Then

```text
136 X_35 <= S_ns.
```

Consequently, the estimate `S_ns <= 68n^2` would imply
`X_35 <= n^2/2`.  Moreover, `S_ns` is exactly the product-product-quotient
factorial moment after deleting equal and swapped product representations, and
it has the four-variable multiplier parameterization proved in `proof.md`.

