# Proof

The heavy-ruling parent places every triple-owner pair component in one
four-dimensional correction space. Start with an arbitrary triple-owner type
`p`. Greedily choose pair types whose component differences from `p` span
all differences. At most four are needed. At least one is needed because the
parent proves that the triple-owner family has more than one pair type. Call
their number `t`.

The same linear-span argument used in the parent shows that the cores of `p`
and these secondary types intersect in the complete triple-owner core `J_3`.
Every secondary type owns at least three records by definition. Choose three
from each. Since

```text
1<=t<=4,
s=32-3t in {29,26,23,20},
```

the assumption `r>=29` supplies enough anchor records for every possible
value of `t`.

Fix one exact size-`m` support containing its pair core for each of the `r`
anchor records and each selected secondary record. As in the parent proof,
two fixed supports from one pair intersect exactly in that pair core. Every
base or one-swap packet contains at least three records from every represented
pair, so all packets have complete support intersection `J_3`. After
cancellation they have the same residual anchor core, exception degree, and
anchor exception locators.

Choose a base set of `s` anchor records and replace one distinguished base
record by each record outside the base. Every packet has 32 records, at least
20 anchor records, and one off-line secondary record. The exact parent
trichotomy applies to each.

If any packet is high complexity, the first output holds. Otherwise the
split-pencil normal form gives one two-dimensional polynomial subspace for
every packet. A one-swap packet shares `s-1>=19` anchor locators with the base
packet. Any two are distinct monic degree-`e` polynomials with disjoint
nonempty roots, hence linearly independent. The base and swapped
two-dimensional subspaces are therefore equal. Every new anchor locator lies
in the base pencil, proving the second output. QED.

The proof is repeated independently for each populated pair type. It does not
identify pencils belonging to different types and never sums packet
certificates.
