# Proof

Fix a retained target `t` and let `g(t)` be the number of generic unordered
shifted-product representations in its split-pencil fiber. Every generic
representation is non-diagonal and therefore accounts for two distinct
ordered representations counted by `P(t)`. Hence

```text
2g(t)<=P(t).                                        (1)
```

The split-pencil router identifies `N_6^disj(t)` with a subset of the
unordered pairs of these `g(t)` vertices. Therefore

```text
N_6^disj(t)<=binom(g(t),2)
             <=(1/2)(P(t)/2)(P(t)/2-1)
             =P(t)(P(t)-2)/8.                      (2)
```

Multiply `(2)` by the nonnegative quotient weight `R(t)` and sum separately
over the two retained target classes. By definition of the disjoint moments,

```text
D_6,25^0<=F_25^0/8,       D_6,25^A<=F_25^A/8.     (3)
```

The primitive shift-pair adapter gives `K_25^c=2D_6,25^c`. Thus

```text
10K_25^0+17K_25^A
 =20D_6,25^0+34D_6,25^A
 <=(1/4)(10F_25^0+17F_25^A).                       (4)
```

The two class sums are disjoint restrictions of the nonnegative `t!=1`
sum. On every retained target, `P(t)(P(t)-2)<=P(t)(P(t)-1)`. Consequently

```text
10F_25^0+17F_25^A
 <=17(F_25^0+F_25^A)
 <=17M_21.                                         (5)
```

Equations `(4)--(5)` prove `(RFC1)`. Dividing `(RFC2)` or `(RFC3)` by
`160` makes its left side respectively
`(10F_25^0+17F_25^A)/4` or `(17/4)M_21`. Thus `(RFC1)` gives in either case

```text
10K_25^0+17K_25^A<=(76599/160)n^2.                 (6)
```

The global overlap-cover payment proves that `(6)` is sufficient for DSP8
on every official row. Finally `680*69=46920<76599`, so the older `FM69`
target implies `(RFC3)`. QED.
