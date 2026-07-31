# Proof

The source-facet census gives ten `I-I` stars and four `I-J` stars outside
the five common-`K` fibers.  Each quotient record represents a deck-paired
orbit of two stars.  Hence there are five `I-I` and two `I-J` edge orbits.

The common-`K` skeleton has the antipodal `A` and `C` edges.  For negative
parity, every complete fiber satisfies

```text
A_1(kappa)+q_kappa B_2(kappa)=0,                  (1)
```

with `B_2(kappa)!=0`.  A loop has `q_kappa=0`, so the two common loops use
both roots of the nonzero quadratic `A_1`.  It is nonzero because the same
common-`K` skeleton has three nonloop records, where `q_kappa!=0`.  Any
outside loop would give a third distinct root of `A_1`, a contradiction.
Thus all five internal `I-I` orbits join distinct antipodal pairs.

The common degrees of `A,B,C` are `(4,3,3)`.  The four outside `J`
incidences therefore consist of one deck-paired `I-J` orbit incident to
`B` and one incident to `C`; `A` has none.  Let `r_i` count their incidences
on `D,E,F`.  Then

```text
r_D+r_E+r_F=2.                                    (2)
```

Let `m_DE,m_DF,m_EF` count the five loop-free internal orbits.  Degree four
at each `I` pair gives

```text
m_DE+m_DF=4-r_D,
m_DE+m_EF=4-r_E,
m_DF+m_EF=4-r_F.                                  (3)
```

Product injectivity permits at most the two signed products between any
two antipodal pairs, so every `m_ij<=2`.

If both `I-J` orbits met the same pair, take `r=(2,0,0)`.  Solving `(3)`
gives `(m_DE,m_DF,m_EF)=(1,1,3)` up to permutation, contradicting the cap
two.  Hence `r=(1,1,0)`.  Equations `(3)` then give the unique solution
`(1,2,2)`, proving `(KB43S-2)`.  Multiplicity two uses both signed products,
which yields exactly `(KB43S-1)` after naming the two attached pairs `D,E`
and the untouched pair `F`.

The source-facet census puts one `I-I` orbit over `eta`, four `I-I` orbits
over `L^c`, and both `I-J` orbits over `L^c`.  The colored-quotient theorem
identifies precisely those last two records as colored.  This proves
`(KB43S-3)`. QED.
