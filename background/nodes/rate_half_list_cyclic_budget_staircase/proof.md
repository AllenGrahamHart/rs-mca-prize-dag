# Proof

Instantiate the PROVED `rate_half_cyclic_rotated_prefix_floor`. Its
statement: for `C = RS[F, D, n/2]` on a multiplicative coset of order `n`,
any `c | n/2` with `N = n/c`, any `s`-subset of one `c`-fiber with
`0 < s < c`, and any `1 <= d <= N/2 - 1` with `m = N/2 + d`, there is a
received word with at least

```text
ceil( C(N-1, m) / (N q^(d-1)) )
```

distinct codewords agreeing on exactly `n/2 + dc + s` coordinates.

Take `d = 1` and `s = c - 1`. Then `m = N/2 + 1`, the field factor is
`q^(d-1) = 1`, and the count is the field-independent

```text
Lambda(N) = ceil( C(N-1, N/2+1) / N ).
```

The agreement is

```text
n/2 + c + (c-1) = k + 2c - 1 = k + 2n/N - 1,
```

using `k = n/2`. Codewords agreeing on exactly `a` coordinates agree on at
least `a`, so `L_1(k + 2n/N - 1) >= Lambda(N) > B*` whenever
`B* < Lambda(N)`.

## Hypothesis admissibility at the official row

For `n = 2^41` and dyadic `N_0` in `{8, 16, 32, 64, 128, 256}`:
`c = n/N_0 = 2^(41 - log2 N_0)` divides `n/2 = 2^40` (since
`log2 N_0 >= 1`); `c >= 2^33 >= 2`, so `s = c - 1` satisfies `0 < s < c`;
and `d = 1 <= N_0/2 - 1` since `N_0 >= 4`. All hypotheses hold.

## The exact counts

`Lambda(8) = ceil(C(7,5)/8) = ceil(21/8) = 3`;
`Lambda(16) = ceil(C(15,9)/16) = ceil(5005/16) = 313`;
`Lambda(32) = ceil(C(31,17)/32) = ceil(265182525/32) = 8,286,954`;
the values for `N_0 = 64, 128, 256` are the exact integers printed in the
statement, replayed by `verify.py`.

## Monotonicity and tier selection

The six exact printed values of `Lambda` are strictly increasing along the
listed dyadic orders, as replayed by `verify.py`.  The agreement
`k + 2n/N - 1` is strictly decreasing in `N`. Hence for a given `B*`, every tier with
`Lambda(N_0) > B*` applies, and the smallest such `N_0` gives the highest
certified unsafe agreement; the budget intervals in the statement are
exactly the intervals on which each `N_0` is that smallest order. QED.
