# Trivialized-support shadow packing

- **status:** PROVED
- **scope:** the `T` branch of the denominator-root cancellation dichotomy

Put

```text
N = n-t,
M = m-t,
```

so `M>=k`. For each trivialized support `S_i'`:

1. its simultaneous degree-`<k` explaining pair `(p0_i,p1_i)` is unique;
2. for distinct slopes, `|S_i' intersect S_j'| <= k-1`;
3. therefore

```text
|T| binom(M,k) <= binom(N,k),
|T| <= floor(binom(N,k)/binom(M,k)).
```

This exact support theorem does not pay either deployed row. Uniformly for
`0<=t<=m-k`,

```text
binom(N,k)/binom(M,k) >= (N/M)^k >= (n/m)^k > (3/2)^k
                                                > 2^58.
```

The KoalaBear budget is below `2^58`; the Mersenne-31 budget is below `2^24`.
Thus the printed shadow bound exceeds both budgets throughout the pole-degree
range. A proof of `(E)` must exploit more than support intersection alone.
