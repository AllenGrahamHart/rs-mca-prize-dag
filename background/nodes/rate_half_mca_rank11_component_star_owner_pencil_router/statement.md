# Rank-eleven component-star owner-pencil router

- **status:** PROVED
- **scope:** recordwise amplification of the dense-locator component
  incidence dichotomy

At least

```text
540546700 / 10^9
```

of the non-dense records in an unsafe residual have at least `98/100` of
their eleven-subsets lying on a positive-dimensional component through the
record. In particular there are at least

```text
148639925144138894
```

such records.

For each such record with support `S`, some ten-subset `B subset S` has at
least

```text
E(K')=ceil(98(m'-10)/100),       m'=67472+K',
```

component extensions `B union {x}`. Exactly one of the following holds.

1. **Large affine owner.** If `rank ev_B=10`, every component extension is
   an identity coordinate for one fixed affine owner of the record. Its
   core inside `S` has size at least `10+E(K')`, so its deficiency from
   `m'` is at most `22320`, uniformly over all shortenings.
2. **Owner pencil.** If `rank ev_B=9`, let `u` span the evaluation kernel.
   At most `K'-11` extensions remain rank deficient. The full-rank
   component extensions lie on one affine pencil of owner pairs whose
   differences are

   ```text
   beta*(-gamma*u,u).
   ```

   Their number is at least

   ```text
   E(K')-max(0,K'-11)>=45153.
   ```
3. **Kernel plane.** If `rank ev_B<=8`, at least a two-dimensional subspace
   of `V'` vanishes on the same ten support coordinates.

This theorem converts component-incidence abundance into a large-owner,
split-pencil, or codimension-two kernel target on more than half of all
unsafe residual records. It does not aggregate records sharing a target.

## Falsifier

Fewer than the stated number of 98-percent records; failure of the
ten-subset star average; a full-rank star with two owner curves; a rank-nine
kernel word with more than `K'-11` further roots; two rank-nine owner pairs
outside the displayed pencil; a shortening with pencil extension count
below 45153; or a rank-at-most-eight ten-subset with kernel dimension below
two.
