# F3 h>=4 aggregate budget gate

Status: PROPOSED TARGET / RED.

## Scope

At an official X4/list corridor row, put

```text
A_row=k+t,
H_max(row)=min(A_row,floor(n/2)).
```

The ground-truth band audit at commit `79bd4b9` proves that the direct-column
obligation has outer width range

```text
2<=h<=H_max(row).
```

For each width, let `R_h` denote the number of fully stripped primitive
active-core records remaining after the quotient, dihedral, moment-trade, U2
boundary, and DLI/skew columns have been removed, in the direct-column counting
convention consumed by `x4_exactlist_staircase_split`.

## Statement

For every official row,

```text
sum_(h=4)^H_max(row) R_h <= 14n^3.              (HGE4-14)
```

An empty sum is zero. This one aggregate assertion replaces separate critical
premises for h=4,5,6,7,8 and the much larger h>8 band.

The constant `14` is a compiler allocation, not a predicted sharp constant:
the proved h=2 theorem and the conditional h=3 compiler each reserve less than
`n^3`, while the consumer accepts a strict total below `16n^3`.

## Falsifier

A complete official row certificate with the correctly stripped aggregate
strictly above `14n^3` falsifies `(HGE4-14)`. A large unstripped count, or one
large fixed-h count still paid by another column, does not.

## Proof routes

The existing fixed-width locator, pencil, and certificate packets are evidence
and possible components of a proof. They do not appear as premises in the
critical statement. Two legitimate routes are:

```text
1. prove a width cap and sum the surviving finite band;
2. prove a uniform weighted estimate sum_h R_h<=14n^3 directly.
```

The second route is forced if no small width cap is available.

