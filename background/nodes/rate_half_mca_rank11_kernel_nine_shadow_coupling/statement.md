# Kernel nine-shadow coupling

- **status:** PROVED
- **scope:** one residual record and all evaluation-corank strata jointly
- **units:** rank-deficient eleven-subsets and their spanning nine-subsets

Let `S` be one exact residual support of size `m'`. For `1<=d<=9`, let
`I_d(S)` count eleven-subsets `T subset S` with

```text
rank(ev_T:W->F^T)=10-d.
```

Then

```text
sum_(d=1)^9
  [C(d+2,2)/C(K'-d-9,2)] I_d(S) <= C(m',9),          (NS)
```

with a zero denominator interpreted as forcing `I_d(S)=0`.

Indeed, every loopless rank-`(10-d)` matroid on eleven elements has at
least `C(d+2,2)` spanning nine-subsets. A fixed spanning nine-subset has
at most `C(K'-d-9,2)` same-rank eleven-set extensions because its closure
is the common-zero set of a `d`-dimensional polynomial space and has size
at most `K'-d`. The rank classes partition the `C(m',9)` nine-subsets of
the record.

This is one shared resource inequality across all coranks. It does not
assume that the nine separate record-support capacities can be saturated
simultaneously.

## Falsifier

A loopless rank-`r` eleven-element matroid with fewer than
`C(12-r,2)` spanning nine-subsets; a same-rank extension outside the
closure of the nine-subset; more than `K'-d` common zeros; or a record
violating (NS).
