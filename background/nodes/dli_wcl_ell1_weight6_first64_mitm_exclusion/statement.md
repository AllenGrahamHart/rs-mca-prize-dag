# DLI WCL ell=1 weight-6 first-64 split-prime exclusion

- **status:** PROVED
- **closure:** computation
- **consumer:** `dli_wcl_slot_1_6_emptiness`

## Statement

Let `q=k*2^41+1`. For the first 64 prime values of `q` in increasing
positive `k`, namely `3<=k<=996` and

```text
6,597,069,766,657 <= q <= 2,190,227,162,529,793,
```

there is no reduced signed weight-6 relation at an order-512 root in
`F_q`. Equivalently, after rotating one term to `1`, no six distinct
order-512 roots with no antipodal pair sum to zero on any row of this panel.

## Certificate

The certified prime panel and its complete first-64 row ledger are inherited
from `dli_wcl_weight5_first64_mitm_exclusion`. On each row, the exact
meet-in-the-middle search constructs all

```text
C(510,2)-255 = 129,540
```

legal pairs and scans all

```text
C(510,3)-255*508 = 21,849,080
```

legal triples after the normalized term and its antipode have been removed.
Cross-compatibility tests reject repeated or antipodal exponents. The banked
64-row result records complete exhaustion and zero relations, totaling
`8,290,560` pairs and `1,398,341,120` triples.

## Nonclaims

This is finite exact evidence, not the universal WCL `(1,6)` theorem. It says
nothing about later official split primes, extension-field rows, other
weights or levels, or WCL-ZONE. The target remains `TARGET`.

## Falsifier

A mismatch with the certified panel, an incomplete pair/triple count, or one
compatible six-set summing to zero on any listed row.
