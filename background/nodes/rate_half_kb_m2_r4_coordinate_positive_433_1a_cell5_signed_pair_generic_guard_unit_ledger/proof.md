# Proof

By the primitive residue ledger, each

```text
E_j=K[s]/(phi_j)
```

is a field.  It is therefore enough to show that each printed guard is
nonzero in every `E_j`.

Use the regular specialization `t=2`.  The factorization checker verifies
that every coefficient denominator of every `phi_j` is nonzero there and
that all five monic factors preserve their degrees.  The primitive-map
checker likewise verifies all 72 map coefficients are regular and exactly
reproduce multiplication by `b,x0,x1` at this fiber.

The chart-2 lift formulas give

```text
r=-M_r(b,t)/L_r(t),   c=-M_c(b,t)/L_c(b,t).
```

The checker pins the atlas packet, evaluates these formulas in each
`F_p[s]/(phi_j(s,2))`, and verifies both denominators are invertible.
It then reduces all 22 declared common-chart guards and the eight factors
in (KBGU-1).  All 150 remainders are nonzero.  Their canonical ledger hash
is

```text
a48d3a028d422b19edda8d6ecac1f663bf2710fbc491a492b660b6b6e264bcb6.
```

If a generic guard were zero in `E_j`, its exact rational representative
would specialize to zero modulo `phi_j(s,2)` wherever its denominators
and the monic factor specialize regularly.  The computed nonzero remainder
contradicts this.  Hence every listed guard is nonzero in every `E_j), and
therefore is a unit.

The common labels are exactly those printed by the ratio-chart theorem.
Squaring them gives `1,t^4,r^4,r^4,1`; together with the nonzero source
guard this yields precisely (KBGU-1).  Hostile tests reject altered
coordinate, factor, and atlas inputs.  QED.
