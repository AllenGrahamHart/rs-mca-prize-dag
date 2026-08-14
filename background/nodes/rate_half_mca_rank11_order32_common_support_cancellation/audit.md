# Audit

## Semantic checks

1. `A` and `B` interpolate only the common support, whose size is strictly
   below `K`; no received word is assumed polynomial globally.
2. Polynomial division is applied to the explanation differences, where
   locator divisibility is proved. The received columns are divided only
   pointwise off the locator roots.
3. A residual simultaneous pair explanation lifts with degree below `K` and
   agrees on the complete original support, so actual MCA-badness is
   preserved rather than assumed.
4. The deleted set is the exact intersection of all 32 supports, making the
   residual common intersection empty.
5. The unchanged critical order follows from the two invariant differences;
   it is not a claim that every deployed-domain theorem is puncture-stable.

## Executable controls

The primary verifier checks all official endpoint identities and a GF(17)
polynomial lift/division example whose direction column has forbidden
residual degree. Six mutations are rejected. The independent checker
reconstructs the toy pointwise and rejects four separate mutations.
