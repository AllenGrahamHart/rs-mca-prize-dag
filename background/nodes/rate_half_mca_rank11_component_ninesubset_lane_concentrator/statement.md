# Rank-eleven component nine-subset lane concentrator

- **status:** PROVED
- **scope:** the complete non-dense post-near rank-eleven residual family
- **units:** distinct `(record, nine-coordinate subset)` pairs

Let the full-rank affine-owner and rank-deficient kernel lanes be the two
lanes in the component-incidence dichotomy. One lane carries at least

```text
495405467/10^9
```

of all record/eleven-subset incidences. Uniformly for

```text
n'=1048576+K',  m'=67472+K',  10<=K'<=1048576,
```

there is one fixed nine-subset `B` and at least

```text
2578110
```

distinct records for which some lane incidence `(record,T)` in the same
dominant lane satisfies `B subset T subset S_record`, `|T|=11`.

If the dominant lane is affine-owner, every selected `T` has evaluation
rank ten. If it is the kernel lane, every selected `T` has evaluation rank
at most nine. The theorem chooses one lane before averaging and therefore
does not mix the two labels in its population floor.

## Falsifier

A component incidence outside the two declared lanes; a lane below half of
their combined floor; more than `C(m'-9,2)` eleven-subsets extending one
fixed `(record,B)` pair; a shortened endpoint below `K'=10`; or a dominant
lane with no fixed nine-subset carrying 2578110 distinct records.
