# Proof

The source-facet census leaves five outside `I-I` and two outside `I-J`
edge orbits.  The common degrees of `A,B,C` are `(4,3,3)`, so the two
colored orbits account for the missing incidences at `B,C`.

An outside antipodal loop has `q=0` and is therefore a root of the
quadratic `A_1`.  The five common records are nonloops, so their nonzero q
values and `B_2!=0` show that `A_1` is not the zero polynomial.  Hence there
are at most two outside loops.

For `i=D,E,F`, put `r_D+r_E+r_F=2`, `l_i in {0,1}` with
`sum l_i<=2`, and `m_ij in {0,1,2}`.  Degree four at the outside pairs and
the five internal records give

```text
2l_D+m_DE+m_DF=4-r_D,
2l_E+m_DE+m_EF=4-r_E,
2l_F+m_DF+m_EF=4-r_F,
l_D+l_E+l_F+m_DE+m_DF+m_EF=5.                    (KBZ433S-2)
```

Exact bounded enumeration of `(KBZ433S-2)` gives 21 labeled solutions.
Quotienting by `S_3` gives precisely `(KBZ433S-1)`, with orbit sizes
`6,3,3,3,6`.  Multiplicity two uses both signed products by product
injectivity, while a singleton cross type retains its sign choice.  The
colored incidence count attaches the two deficient common pairs, proving
the stated product-form compiler.

The source-facet location census puts one internal record at `eta` and the
remaining six records over `L^c`; the two `I-J` records are exactly the
colored records. QED.
