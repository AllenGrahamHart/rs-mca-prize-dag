# Audit - L1 m=4, h=3, nu=0, h=0 auxiliary-fiber exclusion

1. The branch relation is used to identify both auxiliary roots; no packet
   value is assumed during the root-containment argument.
2. `sigma!=1` is checked for every packet before separating the two fibers.
3. Multiplicity `p` is excluded before using the derivative order `e-1`.
4. `D` is squarefree, so its local multiplicity is exactly zero or one.
5. The two fiber gcds are coprime because their values differ.
6. `deg R'=p-5` is the exact constant-eliminant Euler degree, not an upper
   bound.
7. The loss of one root from `rad(R-r)` is exactly the root zero, where
   `D(0)!=0`.
8. Root products are counted with multiplicity; repeated auxiliary roots do
   not invalidate the domain-coset argument.
9. The modular remainder is replayed by polynomial arithmetic and an
   independent companion-matrix implementation.
10. The endpoint closure combines this packet exclusion with the preceding
    universal-packet theorem; it does not claim any other stratum.
