# Low-difference Johnson-positive wedge aggregate

- **status:** PROVED
- **closure:** proof

Fix a base support `S0` in a domain of even size `N`.  Let `D_(e,d)(S0)`
count any residual subfamily of incident records with side width `e` and
exact reduced locator-difference degree `d`, where

```text
1<=d<e<=N/2.
```

Put

```text
Delta_(e,d)=4e^2-N(e+d).
```

Then the complete Johnson-positive wedge satisfies

```text
sum_(Delta_(e,d)>0) D_(e,d)(S0) <=5N^3/16.             (JW-1)
```

The bound is uniform under arbitrary support-wise first-owner deletion.  In
particular, every nonconstant X4/SP record not paid by `(JW-1)` lies in the
explicit wedge

```text
4e^2<=N(e+d),       e>=t_XR+d+1.                       (JW-2)
```

For the official target `D_0+sum_(d>=1)D_d<=16N^3-1`, it is sufficient to
bound `D_0` plus the wedge `(JW-2)` by

```text
(251/16)N^3-1.
```

This theorem does not supply that residual estimate or transport its
numerical allowance to another tuple.

## Falsifier

A fixed base whose disjoint exact `(e,d)` strata with `Delta_(e,d)>0` have
aggregate above `5N^3/16`, or a record outside `(JW-1)` that violates
`(JW-2)`.
