# Rank-eleven heavy-ruling degree-24 order-32 seed

- **status:** PROVED
- **scope:** the heavy orientation emitted by the low-margin Segre ruling
  router

Fix the ruling orientation containing at least

```text
M_or=322476359
```

nonzero first-owned records. It uses at most `Q_4=58361` chosen low pair
types. Call a pair type heavy when it owns at least two records. Singleton
types cost at most `Q_4`, so heavy types own at least

```text
M_heavy=322417998.                                     (D24-1)
```

Their componentwise pair cores have common intersection `J` satisfying

```text
|J|<K-2.                                               (D24-2)
```

Indeed, if `K-2` common coordinates existed, exact cancellation to residual
dimension two would leave at most `Q_2=241` pair types. Fixed-pair
multiplicity is `981115`, so heavy records plus every possible singleton
would total at most

```text
241*981115+58361=236507076<M_or.                       (D24-3)
```

One heavy pair owns at least

```text
ceil(322417998/58361)=5525                             (D24-4)
```

records. Anchor there. Since every chosen pair component lies in the same
four-dimensional correction space, the anchor and at most four further
heavy pair types span all heavy component differences. If `t` further pair
types are needed, then `1<=t<=4`.

Choose two records from every further pair and `32-2t` records from the
anchor pair. These are 32 distinct actual records, with at least 24 on the
anchor pair line. Their exact selected-support intersection `C` satisfies

```text
|C|<=|J|<K-2.                                         (D24-5)
```

Cancel `C` exactly. The residual row has dimension at least three, the same
32 slopes and actual support-wise MCA-bad witnesses, and empty common
selected support. At least 24 shortened explanations lie on one affine
codeword line and at least one lies off it. Therefore the unique
coefficientwise interpolation in the slope, and equivalently the residual
slope-error polynomial, has degree

```text
24<=deg_Z<=31.                                        (D24-6)
```

## Nonclaim

This is one branch-local actual packet, not a whole-line chronology owner.
It does not pay the pure-locator, rational, spread, exception, or
high-complexity outputs and does not close the heavy bucket or MCA.
