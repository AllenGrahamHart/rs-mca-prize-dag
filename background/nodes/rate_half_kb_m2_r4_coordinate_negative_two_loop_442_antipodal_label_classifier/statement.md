# KoalaBear m2 r4 coordinate negative two-loop 442 antipodal-label classifier

- **status:** PROVED
- **scope:** every negative-parity coordinate packet in the two-loop
  `(4,4,2)` skeleton `(1,1,0;1,1,1)`
- **dependencies:**
  `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature` and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

Name the two loop edge types `A,A` and `B,B`.  Let their common-`K` fiber
labels be `k_A,k_B`, and let the three cross-edge fiber labels be
`k_AB,k_AC,k_BC`.  Every actual packet satisfies

```text
k_B^2=k_AB k_AC,       k_A^2=k_AB k_BC.           (KB44-1)
```

Normalize by `k_AB` and put

```text
l=k_A/k_AB,       m=k_B/k_AB.
```

Then the five normalized labels are

```text
X=1,       L=l,       M=m,       Y=m^2,       Z=l^2. (KB44-2)
```

They must contain exactly two antipodal pairs and one singleton.  Among the
fifteen possible singleton/matching patterns, exactly three can have five
distinct nonzero labels:

```text
singleton X, pairs LY|MZ:
    l=-m^2, m=-l^2, l^3=-1, l!=-1;               (KB44-3a)

singleton L, pairs XY|MZ:
    m=-l^2, l^4=-1;                               (KB44-3b)

singleton M, pairs XZ|LY:
    l=-m^2, m^4=-1.                               (KB44-3c)
```

Consequently the complete invariant six-set `I`, after scaling, is one of

```text
{+/-1,+/-l,+/-l^2},       l^3=-1, l!=-1,
{+/-1,+/-l,+/-l^2},       l^4=-1,
{+/-1,+/-m,+/-m^2},       m^4=-1.                (KB44-4)
```

The first row is a sixth-root hexagon; the last two are the two possible
placements of the missing point in an eighth-root six-subset.  In particular
the banked `F_29` set `K={1,-1,4,-4,9}` admits no assignment satisfying
`(KB44-1)`, independently of the `J` labels and edge signs.

This theorem does not delete the three exceptional loci, the other
two-loop skeleton, positive parity, the coordinate orientation, an owner or
payment, a row, or either Prize result.

## Falsifier

An actual packet in this skeleton violating `(KB44-1)`, or an additional
five-distinct antipodal matching outside `(KB44-3a)--(KB44-3c)`.
