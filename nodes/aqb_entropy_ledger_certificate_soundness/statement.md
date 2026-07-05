# aqb_entropy_ledger_certificate_soundness

- **status:** PROVED
- **closure:** proof

## Statement

For an AQB averaged `c=2` quotient-box family, suppose a ledger gives:

- certified lower bounds for all positive shared-family entropy terms; and
- certified upper bounds for every charged box, overlap, multiplicity, and
  quotient/fiber normalization cost.

If the certified lower bound

```text
sum positive_lower_bounds - sum cost_upper_bounds
```

is at least `429,645,547` bits, then the true net shared entropy gain of the
family is at least `429,645,547` bits.

## Falsifier

A ledger whose certified lower-minus-upper bound clears the threshold while
the true net entropy gain is below it.
