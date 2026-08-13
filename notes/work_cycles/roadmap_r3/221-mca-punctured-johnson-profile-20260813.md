# Cycle 221: MCA punctured Johnson profile (2026-08-13)

The sparse-direction route had used the affine-span list bound after
puncturing the direction residual.  At the official top dimensions this paid
only `e<=5` for KoalaBear and `e<=1` for Mersenne-31.  The omitted
ordinary-list structure is much stronger throughout the classical Johnson
regime.

For transformed explanation deficit `h`, puncture the residual support
`E`.  Distinct degree-`<K` explanations have agreement-set intersections
of size at most `K-1`.  The standard incidence calculation gives

```text
J_h=floor((N-e)(m-h-K+1)
          /((m-h)^2-(N-e)(K-1))).
```

Combining these cumulative caps with the already-proved owner multiplicity
`floor(e/h)` gives the exact deficit profile and the coarse bound

```text
|Z| <= sum_h (J_h-J_(h-1))*floor(e/h)
    <= (e-1)J_floor(e/2)+J_e.
```

The weakest Johnson denominator is positive through exactly

```text
KoalaBear:   e=63908, D_e=1218;  e=63909 gives -5924;
Mersenne-31: e=65236, D_e=2794;  e=65237 gives -1636.
```

An exact scan of every support in each prefix places the maximum coarse
bounds at the endpoints:

```text
KoalaBear:   4607583 <= 274980728111395087;
Mersenne-31: 2605443 <=          16777215.
```

The primary verifier checks 129,144 official supports and four mutations.
An independent rational-arithmetic implementation reconstructs both walls,
checks the profile-to-coarse inequality on two synthetic rows, and rejects
two contract mutations.

```text
start:                   6efd673cf
canonical prize:         c8d48cd4b (no newer Fable commit)
upstream frontier:       #1163, #1164, #1165; no superseding MCA result
upstream export head:    #1165 @ 442a223a; import note posted to #1164
result:                  NARROWED + EXPORTED; one PROVED field-general
                         compiler
DAG delta:               +1 PROVED node, +3 edges
critical status delta:   none; replacement target remains TARGET
upstream terminal delta: low-support top-rank walls moved from e<=5/1 to
                         e<=63908/65236; official rows remain open
full-lift residuals:     KoalaBear 63909<=e<=1044238;
                         Mersenne 65237<=e<=1044241
delta-star movement:     none
compute:                 exact local integer arithmetic under RAMguard;
                         no Modal
next route action:       exploit the near-Johnson failure strip and the
                         codimension-one near-MDS extension structure in the
                         remaining middle-support intervals
```
