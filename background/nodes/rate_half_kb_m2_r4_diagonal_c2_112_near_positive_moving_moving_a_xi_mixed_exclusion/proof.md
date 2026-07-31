# Proof

Use `a=xi=2`, `(eta,ell)=(c,d)`, `w=1/c`, and moving-moving source edges
`{2,b},{2,1/b}`. Assign both residuals the distinct roots `1/2,1/d`.

After exact removal of the finite-incidence square from the product
conditions, the primitive degree, term-count, and digest records in `(b,c,d)`
are

```text
c product (4,8,7) 344 35eb7004118a99f6
c sum     (4,12,9) 634 61250edd35fc0302
d product (4,6,7) 264 3d61fea968400cdc
d sum     (4,10,9) 534 7365d626fc5dc28f.             (1)
```

Each is reciprocal in `b`. Exact reduction and reverse lift through
`s=b+1/b` gives

```text
c product (2,8,7) 208 c4cd8952673f0927
c sum     (2,12,9) 382 bcea0eb05a3f0389
d product (2,6,7) 160 886ca4ba23104dc5
d sum     (2,10,9) 322 14d50a46ac8b6b61.             (2)
```

The within-root eliminants have digests `ff275ab748f48780` and
`345a2353ff8883f5`. Their complete factor multiplicities are pinned. Every
factor except `067a3b42540bb240` over `c` and `07c011183de4549a` over `d` is
mechanically bound to a zero, fixed, inverse-fixed, reciprocal, or `z=1`
equation. Thus there is one component pair.

Its degree-128 projection has digest `70f26589e602e699` and factors over `QQ`
as standard powers times components of degrees `2,12,12,32`, with digests

```text
badaaa15f719fc0a, 7c38bfaa7ed117b9,
ddc62481be50cdd9, c23e461afce62a1f.               (3)
```

Complete factorization of `(3)` modulo `p=2130706433` gives four linear,
five quadratic, one cubic, one degree-five, one degree-seven, and one
degree-29 factor. Only the first ten can have roots in `F_(p^6)`.

For each retained factor, adjoin the four trace equations `(2)` and saturate
by

```text
c d; c,d in {2,1/2,1,-1}; c-d; cd-1;
2s-5; s^2-4; cs-c^2-1; ds-d^2-1;
5cd-4c-4d+5; 4c^2d-2c^2-3cd+3c+2d-4.             (4)
```

Every saturated basis is `[1]`. Hence every deployed-field point is
forbidden and the chart is empty.

The primary uses direct matrix inversion and resultants. The no-import audit
checks the source independently with `DomainMatrix.solve_den`, reverse-lifts
the trace forms, and uses a fresh direct reconstruction plus terminal
subresultants for the bounded router shards. Both recover `(1)`--`(4)` and
all ten unit saturations. QED.
