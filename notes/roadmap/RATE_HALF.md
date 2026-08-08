# Rate-Half Finite Lane

This lane attacks the deployed KoalaBear rate-half band required by
`rate_half_band_closure`.

## Current decomposition

The positive `433-1b -> O0a` role-cell ledger has closed:

```text
[0], [1,2], [3,6], [4,7], [14]
```

and retains:

```text
[5,8], [9,10], [11], [12,13].
```

Representative cell 4 is now complete. Its principal product-rank-five
ledger is assembled from three independently verified, disjoint suppliers:

```text
parallel-DE xi={0,1,2}: 45 labels,  720 raw systems;
outside     xi={3,4}:    30 labels,  480 raw systems;
endpoints   xi={5,6}:    30 labels,  480 raw systems.
```

The union is all `7*15=105` labels and 1,680 raw systems. The global
product-rank-drop theorem excludes the complementary rank branch, so role
cell 4 is PROVED empty. Exact `B/C` duplicate-role transport then maps every
principal cell-7 system bijectively to cell 4 while the global rank-drop
theorem covers cell 7's exceptional branch. Therefore orbit `[4,7]` is
PROVED empty. Historical matching-by-matching details remain in
`critical/nodes/rate_half_band_closure/attack_addenda/13-*` through `34-*`.

Representative cell 12 now has a complete structural common-locus packet.
The selected `AC` pivot covers all 24
source-sign/product-cofactor charts. Its leading-open common curve is an
exact elliptic four-basis tower, the leading complement is 12 classified
zero-dimensional fibers with eight deployed rational points, and one
sign-independent primitive kernel annihilates all ten common Vieta rows.
All 105 outside labels in all four target lanes are now PROVED empty at each
of those eight rational points. Thus only the generic elliptic leading-open
chart remains on the principal cell-12 frontier. Two universal outside
involutions quotient its 105 labels to 36 exact representatives. Exact
source-compatibility cuts and two independent residual censuses close the
`BF` and `sigma_c CF` endpoint roles: 30 labels, or 12 generic orbits. The
live generic ledger is therefore 24 representatives covering 75 labels. An
exact `B/C` duplicate-role transport is also ready: once cell 12 is empty, all
1,680 signed principal cell-13 systems follow bijectively, while the global
rank-drop theorem pays the complementary branch. These are PROVED suppliers
for the `[12,13]` orbit, not a cell closure.

## Node hierarchy

```text
cell-4 four-basis tower
        |
        +-- xi0/pairing0 exclusion
        +-- xi1/pairing0 transport
        +-- xi2/pairing0 exclusion
                     |
                     v
       parallel-DE pairing0 closure      [PROVED]
                     |
            DE first-pair block           [PROVED]
                     |
            matching-orbit quotient       [PROVED]
                     |
            pairing-3 through 13 blocks   [PROVED as scoped]
                     |
          all parallel-DE matchings       [PROVED]
                     |
          xi5/xi6 endpoint roles          [PROVED]
                     |
           xi4 <-> xi3 transport          [PROVED]
                     |
            xi3 matching 0 payment        [PROVED]
                     |
          xi3 matchings 1 and 2           [PROVED]
                     |
          pairing-3/6 exchange block        [PROVED]
                     |
          pairing-4/9 exchange block        [PROVED]
                     |
          pairing-5/12 exchange block       [PROVED]
                     |
          pairing-7/10 exchange block       [PROVED]
                     |
          pairing-8/13 exchange block       [PROVED]
                     |
          pairing-11/14 exchange block        [PROVED]
                     |
          disjoint 105-label assembly         [PROVED]
                     |
             complete cell 4                  [PROVED]
                     |
             role orbit [4,7]                 [PROVED]
                     |
       cell-12 elliptic common locus           [PROVED]
                     |
       cell-12 global common kernel            [PROVED]
                     |
       rational-boundary outside exclusion      [PROVED]
                     |
       generic 105-to-36 label quotient          [PROVED]
                     |
       endpoint roles: 12 orbits / 30 labels     [PROVED]
                     |
       attack 24 generic representatives         [NEXT]
                     |
       close cell 12                              [OPEN]
                     |
       exact cell-12 -> cell-13 transport         [PROVED implication]
                     |
       audit role orbits [5,8], [9,10], [11]   [OPEN]
```

This hierarchy is intentional: each child has a reusable exact statement,
while source-sign rows and norm roots remain certificate records.

## Compute posture

Use symmetry and source-only cuts before launching a census. Cell 12's
rational boundary and both endpoint-role families are paid. The generic
ledger has 24 representatives in the parallel-`DE`, reciprocal `DF/EF`, and
fully mixed families. The immediate router should seek another necessary
source-only compatibility cut against the fixed kernel without computing
large norms. Modal jobs must be route-deciding and remain within the active
protocol budget. Larger campaigns go to the deferred compute ledger.
