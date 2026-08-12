# Record-local common cores are not slope owners

- **status:** PROVED
- **closure:** exact finite counterexample
- **scope:** route cut for common-core forest compilers; not a deployed-row
  counterexample

## Statement

For `RS[GF(11),GF(11)^*,5]` at agreement `m=7`, the relative critical
order is

```text
floor(2(n-k)/(m-k))+1=6.
```

There is one received line with seven displayed support-wise MCA-bad slopes
and a unique degree-`<5` explanation for each displayed slope. The two
non-global-affine critical records

```text
R1={0,2,3,5,6,8},
R2={0,2,3,5,6,9}
```

share slope `0`, but the intersections of their maximal agreement supports
are respectively

```text
C(R1)={8,10},
C(R2)={10}.
```

Consequently the record-local intersection `C(R)` is not an invariant of a
slope, even when every displayed explanation is unique and every witness is
on its exact maximal support. A compiler that sends each local record to its
own fixed-core family does not by that rule induce a disjoint partition of
slopes.

## Consequence

The common-core cancellation adapter remains valid for either record. What
fails is the naive use of its input core as an owner. A whole-line compiler
must add a line-global selector, prove an add-back/fiber bound for a declared
priority among competing cores, or bypass the forest with a same-owner
maximum theorem.

## Nonclaims

The example is below the deployed row, precedes the upstream first-match
strips, and does not refute the existence of a chronology-correct selector.
It gives no slope bound and moves no MCA ledger value.

## Falsifier

Failure of any exact explanation, maximal-support, noncontainment,
non-affinity, core-intersection, or shared-slope check in the certificate.
