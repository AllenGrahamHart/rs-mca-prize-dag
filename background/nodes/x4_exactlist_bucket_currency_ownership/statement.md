# Exact-list bucket ownership and currency separation

- **status:** PROVED
- **closure:** proof

Let `F_z` be a depth-`t` locator-prefix fiber of `A`-subsets after a
support-wise first-match partition. If `S0` is one residual member, then every
other residual member `S` determines the canonical record

```text
P=S\S0,  Q=S0\S.
```

The map `S -> (P,Q)` is injective, `|P|=|Q|=h`,

```text
t+1 <= h <= min(A,n-A),
```

and `P,Q` have equal elementary coefficients through order `t`. Therefore an
injection of all such residual records into a universal record ledger of size
`R` proves

```text
|F_z| <= 1+R.
```

This is the primitive shift-pair (`SP`) bucket. It is different from the
structured moment/null pullback bucket: `t`-null blocks are special staircase
generators, and the number of generators need not equal the number of list
members produced by all allowed combinations. It is also different from
QA.22's MCA bad-slope count, whose quantifiers are per ordered pair rather
than per received word.

Consequently a correct `x4` certificate needs separate statements for:

1. the actual list-member population of the structured pullback bucket;
2. coverage of every primitive star record by the `u1` record ledger; and
3. one list-side sum of all disjoint bucket bounds against `B*`.
