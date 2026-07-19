# Proof

The swap involution on the `m=P(t)` ordered product representations has
`d=D(t)` fixed points, so `d` has the same parity as `m`. For every feasible
`m,d`,

```text
68(m-18)_+ <= m(m-2)+d.
```

For `m>=19`, the difference is `(m-34)(m-36)+d`; only `m=35` needs parity,
which gives `d>=1`. Summation after multiplication by `R(t)` proves the first
claim. If `S_ns<=1200n^2`, divide by four to obtain
`17X_18<=300n^2`.

---

## Addendum — NARROWING r3 (2026-07-13, wave-5 audited import; catch #160b)

Terms with `m<=18` vanish on the left of the pointwise inequality, so they
need not be included on the right. Summation over only `P(t)>=19`, after
multiplication by `R(t)`, proves `68X_18<=S_ns^rich`. Nonnegativity of every
retained term gives `S_ns^rich<=S_ns`. If `S_ns^rich<=1200n^2`, divide by
four as in the original proof above.
