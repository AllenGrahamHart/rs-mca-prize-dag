# Small-profile rank probe

The strongest `e=7,d_A=1` analogue has

```text
28 classified rows,
21 off-line slopes,
row degree 5,
14 slope columns of degree 7,
7 slope columns of degree 6,
domain degree 7.
```

On the smooth grid `mu_28 x mu_21`, the circulant incidence rule with
offsets `{0,1,7,8,14}` realizes this ledger exactly. Its coefficient-MDS
matrix has rank `28` over both `F_337` and `F_421`, so it has no biform
realization. Starting from that graph, 250 deterministic degree-preserving
switch trials in each field also gave rank histogram

```text
{28: 250}.
```

This is evidence that the new gate has substantial power. It does not prove
full rank for every admissible incidence pattern or at the official row.
