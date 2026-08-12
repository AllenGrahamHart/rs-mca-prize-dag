# Proof

Work over `F=GF(11)` on `D={1,...,10}` with `k=5` and `m=7`. The received
line and all seven explanation polynomials are printed in
`source_contract.json`.

For each listed slope `gamma`, direct evaluation gives exactly the printed
seven-point agreement support. Exhausting all `binom(10,7)=120` candidate
supports and interpolating shows that the printed polynomial is the unique
degree-`<5` polynomial with at least seven agreements.

On that support, interpolate the two received words separately to degree
below seven. Their degree pairs are

```text
gamma:  0  2  3  5  6  8  9
degrees (4,6) (6,6) (6,6) (6,6) (6,6) (6,6) (5,5).
```

At least one degree is at least `k=5` in every case. Since interpolation on
seven points is unique, no pair of degree-`<5` polynomials simultaneously
explains the received pair on that same support. Each slope is therefore an
actual support-wise MCA-bad witness.

Intersecting the six printed maximal supports in `R1` gives `{8,10}`;
intersecting those in `R2` gives `{10}`. Both records contain slope `0`.
Finally, the coefficient vectors are not affine functions of the slopes:
the line through the explanations at slopes `0` and `2` misses every one of
the remaining four explanations in each record. Thus neither record is a
global affine block.

The same slope therefore belongs to two valid non-affine critical records
with different record-local cores. This proves the route cut.
