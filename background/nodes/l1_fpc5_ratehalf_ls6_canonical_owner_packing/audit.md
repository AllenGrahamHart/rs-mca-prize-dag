# Audit

1. The base point `H=0` is excluded from the owner ledger; its planted charge
   is already paid.
2. `G` is the exact monic gcd, not a selected common divisor.
3. Candidate squarefreeness is used when making `G,A,B` pairwise coprime.
4. The shared-root guard `gcd(G,Q_H)=1` is retained; dividing by `G` does not
   erase it.
5. The packing universe is `C\Z(D_0)`, of size `|C|-j`, because exact owner
   equality forces every root of `B` outside the base locator.
6. `(CO8)` is per owner. There is no sum over the `binom(j,g)` possible
   owners and no critical status change.
7. The verifier uses a synthetic exact polynomial chart only as a regression
   companion; the written argument is the proof.
