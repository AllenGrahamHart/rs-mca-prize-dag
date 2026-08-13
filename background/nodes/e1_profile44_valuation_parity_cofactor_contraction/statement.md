# E1 profile-(4,4) valuation-parity cofactor contraction

- **status:** PROVED
- **closure:** complete singleton-support census plus exact product threshold
- **scope:** binding prize rate-`1/8` row, profile `(4,4,S=20)`

Let `mu` be the local `pi=1-zeta_256` valuation and let

```text
q=#{d in {1,...,63}: A_d is odd}
```

be the positive-half autocorrelation parity weight. A complete normalized
four-singleton census proves that

```text
mu in {3,5,6,9,10,12,17,18,20}  =>  q in {2,4,6}.    (P44-P1)
```

For every official collision in these valuation branches,

```text
E=sum_d A_d^2>=6,          V=2E>=12.                  (P44-P2)
```

The energy-adaptive product majorant then forces

```text
m<=853574.                                             (P44-P3)
```

Intersecting `(P44-P3)` with the former branchwise `657`-cofactor frontier
removes exactly twelve values:

```text
854024, 860192, 862216, 866312, 874504, 886792,
897032, 901184, 905224, 911368, 917512, 921608.
```

Exactly `645` cofactor values remain. This is not an orbit count or profile
payment.

## Falsifier

A four-singleton support with one of the displayed valuations and parity
weight outside `{2,4,6}`, an official collision in those branches with
`E<=5`, or an exact cofactor replay leaving a count other than `645`.
