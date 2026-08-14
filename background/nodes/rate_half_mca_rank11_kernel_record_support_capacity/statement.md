# Kernel record-support capacity

- **status:** PROVED
- **scope:** one residual record and one evaluation-corank stratum
- **units:** rank-deficient eleven-subsets of the record's exact support

Let one residual record have an exact support `S` of size `m'`. For
`1<=d<=9`, let `I_d(S)` be the number of eleven-subsets `T subset S` with

```text
rank(ev_T:W->F^T)=10-d.
```

Then

```text
I_d(S) <= floor(
  C(m',10-d) C(K'-10,d+1)/(d+2)).                    (RS)
```

Indeed, decorate each `T` by every rank basis. It has at least `d+2`
bases. For a fixed basis `B subset S`, the other `d+1` coordinates are
common zeros of `ker(ev_B)`, leaving at most `K'-10` choices.

This is independent of the support-local multi-record cap `M_d`. It is a
per-record alternative to the ambient fixed-basis capacity, not a complete
kernel-lane payment.

## Falsifier

A rank-deficient eleven-subset with fewer than `d+2` bases; a fixed basis
with more than `K'-10` additional common-zero coordinates; or one record
whose rank-`(10-d)` eleven-subset count exceeds (RS).
