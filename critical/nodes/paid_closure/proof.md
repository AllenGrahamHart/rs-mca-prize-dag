# paid_closure proof

The paid ledger uses a first-match convention. For each witness at agreement
index `A`, charge it to the first applicable paid stratum in the ordered list:

```text
tangent, quotient, extension.
```

The three component functions are now proved:

- `paid_tan_fn` gives the tangent contribution.
- `paid_quot_fn` gives the quotient contribution, interval-valued in the
  unresolved zone-(b) cells.
- `paid_ext_fn` gives the extension contribution.

Define

```text
Paid(A) = Paid_tan(A) + Paid_quot(A) + Paid_ext(A)
```

with first-match deduplication. Since each component is computable in the
sense recorded above, `Paid(A)` is a computable paid ledger function.

The only caveat is inherited from `paid_quot_fn`: when zone `(b)` is live,
`Paid(A)` is an interval-valued function. This is intentional and is the
object consumed downstream; closing `zone_b` would refine the interval to a
point value, but it is not needed for this assembly statement.
