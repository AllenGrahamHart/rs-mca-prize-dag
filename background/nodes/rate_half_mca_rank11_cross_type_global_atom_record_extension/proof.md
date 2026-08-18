# Proof

Let `p` be a large type and choose any distinct large type `q`. In the
canonical edge construction, the `p`-anchored packet contains 18 fixed
records of `p`, at least five records of `q`, and three records of every
other represented recovery type.

Take any record `x` owned by `p`. If it is already one of the 18 fixed anchor
records there is nothing to prove. Otherwise replace one fixed `p` record by
`x`. The modified packet still has:

- 18 records from `p`;
- the same represented pair types and hence the same complete core `J_3`;
- at least three records from every represented type;
- an off-anchor `q` record; and
- slope-interpolation degree in `18..31`.

The core-saturated partial-relative argument therefore gives high complexity
or a nontrivial scalar-locator rational certificate. Pure locator remains
excluded and the common-pole argument remains valid, so the rational
certificate is pole-simple.

The canonical and modified packets differ by one record and share 31 exact
supports. Their shared deck contains 17 fixed records from `p` and at least
five records from `q`. The pole-simple atom-identity theorem applies and makes
the modified certificate projectively identical to the canonical edge atom,
which is `C_*` by the global-atom hypothesis. Thus `x` is certified by
`C_*`.

Repeat for every record of `p`, then for every large type. If no replacement
emits high complexity, `C_*` certifies all large-type records. QED.
