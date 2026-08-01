# Proof

The source-facet census gives five outside `I-I` and two outside `I-J`
edge orbits.  The deficient common pairs `B,C` each require exactly one
colored orbit; `A` requires none.

The common loop is one root of the nonzero quadratic `A_1`.  It is nonzero
because every common nonloop has `A_1+qB_2=0` with `qB_2!=0`.  Hence there
is at most one outside loop.

Let `r_D+r_E+r_F=2` count colored incidences, let `l_i in {0,1}` with
`sum l_i<=1`, and let `m_ij<=2` count internal cross-pair orbits.  Degree
four at the outside pairs gives

```text
2l_D+m_DE+m_DF=4-r_D,
2l_E+m_DE+m_EF=4-r_E,
2l_F+m_DF+m_EF=4-r_F.                              (KB433S-3)
```

Also `sum l_i+sum m_ij=5`.  Exact bounded enumeration of these equations
gives twelve labeled solutions.  Quotienting by `S_3` leaves exactly the
three representatives `(KB433S-1)`, with orbit sizes `3,3,6`.
Multiplicity two uses both signed products.  Assigning the deficient colors
to the nonzero entries of `r`, then changing signs of `D,E,F`, gives exactly
the forms `(KB433S-2)`.  The source-facet location census puts one internal
record at `eta` and the remaining six outside records over `L^c`. QED.
