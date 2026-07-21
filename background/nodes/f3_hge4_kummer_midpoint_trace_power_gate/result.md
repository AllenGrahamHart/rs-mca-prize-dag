# Result

The retained near-third midpoint scalar is no longer a free Kummer parameter.
It is determined by one outside-factor trace:

```text
kappa=-(tau+2)/8,       C_m(tau)=2,
kappa^((p-1)/m)=1.
```

There are only `(m-2)/2` trace candidates before the power test, and the test
is invariant under swapping the ordered outside factors. A complete HGE4
generator can therefore reject a near-third candidate from its endpoint
coefficients before reconstructing the full midpoint factor. The number of
split pencils above a surviving trace remains open.

Every surviving ratio is also a square. When `(p-1)/m` is odd, necessarily at
the top exact-ratio level, this leaves only `m/4-1` traces before the full
power test.

The downstream gcd compiler counts these scalar candidates exactly without
enumerating midpoint factors.
