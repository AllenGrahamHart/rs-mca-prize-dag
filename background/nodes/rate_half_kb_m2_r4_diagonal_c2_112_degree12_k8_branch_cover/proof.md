# Proof

On `K10!=0`, the leading coefficient of `A0` is a named unit times `K10`.
The parent pseudo-remainder identity is therefore reversible. Exact
factorization leaves the following determinant-core degree pairs:

```text
F04-R02: (37,37)    F05-R02: (38,37)
F06-R02: (37,37)    F07-R02: (38,37).
```

The differing first degrees are retained literally; no assignment transport
is used. Intersecting the two cores with `R12=K8=0` gives exact bases of
sizes `62,61,61,62`, all of dimension one. Sequential reduction of `s`,
`L6`, `K10`, and every transported named-open factor reaches zero at named
factor 14 in all four cells. Thus no point survives any `K10!=0` chart.

The complementary chart has `K10=0`. Every source point then lies in the
three-equation ideal `(R12,K8,K10)`. Its exact basis has size 27 and
dimension one in every cell. The product of `s`, `L6`, and all transported
named-open factors again reduces to zero at named factor 14, without using
either quartic source row. Thus even this larger residual variety has no
admissible point.

The cases `K10!=0` and `K10=0` exhaust `K8=0` in each literal cell. QED.
