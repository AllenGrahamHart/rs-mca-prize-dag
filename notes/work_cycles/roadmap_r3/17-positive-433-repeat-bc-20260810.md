## Work cycle 17: positive 433-1b repeated-BC cells 3/6 closure

### Scope and taxonomy

This cycle concerns the coordinate-positive `433-1b -> O0b` route node, not
the separately exported K3 role-cell campaign.  Its unit is the guarded
repeated-`BC` outside-system census in owner cells 3 and 6.  The existing
`BC+` aggregate had already excluded all 840 systems in each cell.  This
cycle closes the matching `BC-` block.

The closure is deliberately split into reviewable DAG leaves:

```text
BC- genus-two common tower [PROVED]
  + generic uncolored rank atlas [PROVED]
  + exhaustive uncolored guard fibers [PROVED]
      -> DE residual exclusion [PROVED]  240 labels
      -> DF residual exclusion [PROVED]  240 labels
      -> EF residual exclusion [PROVED]  120 labels
      -> uncolored aggregate [PROVED]     600 labels

BC- genus-two common tower [PROVED]
  -> colored norm atlas [PROVED]
  -> colored finite exclusion [PROVED]   240 labels

colored 240 + uncolored 600 + exact cell-3/6 transport
  -> cells-3/6 BC- complete outside exclusion [PROVED]
```

### Uncolored finite payment

All 360 representative residual-pairing systems have generic rank 16.  The
47 one-variable rank/construction guards have 73 root incidences and 48
distinct deployed-field roots.  Exact tower lifting and endpoint replay pay
all exceptional fibers:

```text
packet  representative cases  exceptional fibers  unit endpoint rows  labels
DE+     120                   640                 512                 240
DF+     120                   864                 1408                240
EF      120                   832                 1152                120
total   360                   2336                3072                600
```

No survivor or unresolved row remains.  The exact `d -> -d` quotient pays
the opposite `DE` and `DF` signs.

### Colored finite payment

For missing `BE` and `CF`, eliminate the unknown endpoint without dividing
by the missing `A` value.  The resulting necessary cut is

```text
r^4 k^2 betam^2 + (k^2 am + bm)^2 = 0,
```

where `k=b` or `c`.  Successive norms through the certified genus-two
quadratic tower produce eight exact rational functions in `q`.  The `BE`
numerators have degree 92 and the `CF` numerators degree 100; their
denominators have degrees 104 and 112.  Four construction guards record
every inversion.

The complete union of numerator roots, denominator roots, and construction
guard roots has 136 incidences but only eight `q` values.  Exact finite
replay classifies them as

```text
projection-denominator boundary: 3
no base-field y:                 2
only Mobius/target-guard lifts:  3
guarded common points:           0
```

Hence all 120 missing-`BE` and all 120 missing-`CF` systems are empty before
any residual matching solver is needed.

### Audit and compute custody

- Uncolored replay: 360/360 rows, 2,336 fibers, 3,072 endpoint rows; three
  result shards remain below the 50,000-line artifact ceiling.
- Colored norm run: `ap-TTQ0R12MXpviluGNnM1EbZ`.
- Colored finite replay: `ap-y6eox0bJ27lgXvolqxNXnU`.
- The colored primary verifier independently recomputes every deployed-field
  root set via pure-Python `gcd(P,q^p-q)`, rebuilds all incidences, and
  replays every `y,b,c` boundary.
- Seven new PROVED nodes have primary and hostile verifiers.  The compiled
  DAG and sectioned-document gates pass, and the verifier manifest is
  refreshed.

### Board effect and next move

Both `BC` signs are now closed for the repeated-`BC` cells-3/6 owner block:

```text
BC+ cell 3: 840 empty     BC+ cell 6: 840 empty
BC- cell 3: 840 empty     BC- cell 6: 840 empty
```

This is strict evidence for
`rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment`; it does
not promote that critical node because other owner blocks and split-`BC`
lanes in `433-1b -> O0b`, plus the other ten positive routes, remain unpaid.
The next attack should first compile the exact residual partition of the
`433-1b -> O0b` route after subtracting all now-closed owner blocks.  Only
then should another elimination campaign be selected, preferring an exact
transport or quotient over a fresh per-system census.

```text
lane:                    MCA / coordinate-positive 433-1b -> O0b
result:                  repeated-BC cells 3/6 closed for BC+ and BC-
DAG status delta:        +7 background PROVED; critical orbit unchanged
delta-star movement:     none
new assumptions:         none
live compute requests:   none
next:                    compile the post-closure 433-1b/O0b residual owner census
```
