# Proof

In `S0`, the seven outside records are ordered

```text
BE, CF, DE+, DE-, DF+, DF-, EF.
```

Replacing `d` by `-d` fixes `BE,CF,EF` and exchanges each displayed signed
`DE` and `DF` pair, including both its product and squared sum. It leaves all
five common rows and every source root untouched. Signed coordinate guards
are invariant under `d->-d`, so this is an exact complete-system
automorphism in every role cell and source-sign row. Its action on 105 labels
has nine fixed labels and 48 doubletons by the proved D-sign router.

The B/C--E/F action has outside permutation

```text
(BE CF)(DE+ DF+)(DE- DF-).
```

This commutes with `(DE+ DE-)(DF+ DF-)`. On `S0`, the B/C--E/F action is
fixed-point-free on the 120 lane/cell/source-sign states, whereas the D-sign
action fixes those states. Thus the two generators give a Klein-four action
on all `120*105=12,600` rows.

The identity fixes 12,600 rows. The D-sign element fixes `120*9=1,080`.
The B/C--E/F element and its product with D-sign fix none because their
state action is fixed-point-free. Burnside gives

```text
(12,600+1,080)/4 = 3,420.
```

Equivalently, the exact orbit router obtains 540 doubletons and 2,880
four-element orbits. The non-`S0` split lanes contribute 12,600
representatives under the first involution, hence the full split block has
`3,420+12,600=16,020`. QED.
