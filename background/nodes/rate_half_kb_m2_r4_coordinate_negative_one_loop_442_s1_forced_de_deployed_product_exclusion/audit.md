# Audit

1. The sparse builder uses quotient multiplication matrices and emits 25
   outside monomials per equation; no large symbolic reduction is trusted.
2. Both cubic factors are checked for exact product and irreducibility.
3. The projection into each cubic component replays all six common quotient
   relations before the outside equations are reduced.
4. The primary verifier computes the first component; the audit verifier
   rebuilds the second independently.
5. The unit ideal is obtained before guard saturation, so no invalid `d=0`
   or `s=0` branch can hide a guarded solution.
6. The earlier `F_41` witness is compatible with this result: it proves
   characteristic dependence, not deployed survival.
