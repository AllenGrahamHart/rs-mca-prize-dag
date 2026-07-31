# Proof

The source-facet census gives two outside `I-J` edge orbits and five outside
`I-I` edge orbits.  Common `J` degrees are `(4,4,2)`, so only pair `C` has
outside incidence, and the two colored records are `C-I` orbits.

The unique common loop at `h` forces `A_1(h)=0`.  The polynomial `A_1` is not
zero because every common nonloop has `A_1+qB_2=0` with `qB_2!=0`.  Every
outside loop gives another distinct root of `A_1`, so `deg A_1<=2` permits at
most one outside loop.

Degree four at the outside pairs gives

```text
2l_D+m_DE+m_DF=4-r_D,
2l_E+m_DE+m_EF=4-r_E,
2l_F+m_DF+m_EF=4-r_F.                             (1)
```

Here `sum r=2`, `sum l+sum m=5`, `l_i in {0,1}`, `sum l<=1`, and product
injectivity gives `m_ij<=2`.  Exhausting these bounded integer equations
gives twelve ordered solutions.  Quotienting by the six permutations of
`D,E,F` leaves exactly the three representatives in `(KB41S-1)`, with orbit
sizes `3,3,6` respectively.

When `m_ij=2`, injectivity forces the two signed products between those
pairs.  The source-facet census places one of the five internal records at
`eta`. QED.
