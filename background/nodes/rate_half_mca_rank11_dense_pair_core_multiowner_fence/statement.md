# Rank-eleven dense pair-core multi-owner fence

- **status:** PROVED
- **closure:** explicit algebraic construction
- **scope:** the deployed KoalaBear code and line field

## Statement

Let `C=RS[F,D,K]` on the deployed order-`2^21` KoalaBear domain, with

```text
n=2097152, K=1048576, m=1116048, w=m-K=67472,
F=F_p^6, p=2130706433.
```

There is one received line with `12` distinct selected pair types
`(a_e,b_e)` such that all of the following hold.

1. Every pair has exact global common core of size `m-1`, hence deficiency
   `delta_e=1`.
2. Every pair owns exactly `238825` distinct finite slopes. Each slope has
   an exact size-`m` agreement support, is same-support pair-noncontained,
   is outside the proved near-rational stratum, and selects this pair with
   support-local margin `theta=1`.
3. All `12*238825=2865900` slopes are globally distinct.
4. The selected explanation codewords have affine span exactly `10`, and
   the selected error words have linear rank exactly `11`.
5. The `12` pair lines are distinct and no one pair is a common owner for
   the records assigned to another pair.

In particular, the local hypotheses of the PR `#1168` rank-eleven terminal,
including the stronger `delta<=4` and at least `200632` records condition,
do not force a unique dense pair, a single global affine owner, or
coalescence of different dense cores. A valid next theorem must use an
additional chronology/classification premise or prove an aggregate payment
for a genuinely multi-owner family.

## Nonclaims

The construction has only `2865900` bad slopes, far below `B_*`. It does not
refute an aggregate rank-eleven bound, the active order-32 S/A/E
classification, a chronology-correct owner router, or KoalaBear safety. It
does not claim that the complete abstract singleton packing from `#1168` is
simultaneously realizable.

## Falsifier

Failure of the degree, carrier, partition, field-avoidance, exact-support,
pair-noncontainment, post-near, margin, affine-span, or error-rank check; or
an identification of two of the displayed pair types.
