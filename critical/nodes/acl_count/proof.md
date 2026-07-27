# proof: acl_count

- **status:** PROVED
- **closure:** proof

## Source

`archived/slackMCA_v3.tex#thm:exactcount`.

## Class count

Partition `mu_(N')` into `n_1=N'/2` antipodal pairs. An `l'`-subset has,
on each pair, one of four states: empty, full, positive singleton, or
negative singleton. If there are `t` singleton pairs and `u` full pairs,
then

```text
t+2u=l'.
```

An antipodal-rearrangement class is determined by the signed singleton
positions and the number `u`; the positions of the full pairs among the
remaining pairs are rearrangement-equivalent. Thus the number of classes at
fixed `(t,u)` is `binom(n_1,t)2^t`. The conditions `t>=0`, `u>=0`, and
`u<=n_1-t` give exactly the sum in `statement.md`.

At `rho=1/2`, `l'=n_1+1`, so admissible `t` have parity opposite to `n_1`.
The binomial parity identity

```text
sum_(t parity opposite n_1) binom(n_1,t)2^t
  =(3^n_1-1)/2
```

gives the printed closed form.

## Stable reduction

Two distinct characteristic-zero classes give a nonzero cyclotomic
difference. The standard conjugate bound places its absolute norm at most
`(2l')^(N'/2)`. If the row prime is strictly larger, it cannot divide that
nonzero norm, so reduction cannot identify the two classes. The canonical
line therefore has exactly the characteristic-zero class count in this
stable range.

Finally, Stirling's formula applied to `t=theta n_1` and Laplace domination
of the finite sum gives the entropy maximum `beta(rho)` in the statement.
Outside the strict norm threshold this injectivity step is unavailable; that
is precisely the separate `zone_b` scope.
