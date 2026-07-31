# Proof

The source-facet census gives five outside `I-I` edge orbits and two outside
`I-J` edge orbits.  The two common loops force the quadratic `A_1` to vanish
at their distinct `K` labels.  It is not the zero polynomial because the
same common skeleton has three nonloops, where
`A_1+qB_2=0` with `qB_2!=0`.  An outside loop would force a third root of
`A_1`, so no such loop exists.

The common `J` degrees are `(4,4,2)`.  Thus `A,B` have no outside incidence,
while each signed label in pair `C` has two.  Deck pairing groups these four
incidences into two colored `C-I` edge orbits.

Let `r_i` count their incidences on the `I` pairs and let
`m_DE,m_DF,m_EF` count the five loop-free internal orbits.  Degree four at
each `I` pair gives

```text
r_D+r_E+r_F=2,
m_DE+m_DF=4-r_D,
m_DE+m_EF=4-r_E,
m_DF+m_EF=4-r_F.                                  (1)
```

Product injectivity bounds every `m_ij` by two, the number of signed
products between two fixed antipodal pairs.  If both colored records met
one pair, `(1)` would give internal multiplicities `(1,1,3)` up to
permutation, impossible.  Hence `r=(1,1,0)`, and `(1)` has the unique
solution `(1,2,2)`.  Multiplicity two uses both signed products, proving
`(KB44S-1)--(KB44S-2)`.

The source-facet census places one internal orbit at `eta`, with the other
four internal and the two `I-J` orbits over `L^c`.  The colored-quotient
compiler identifies the latter two as the colored records. QED.
