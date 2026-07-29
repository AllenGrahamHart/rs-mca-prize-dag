# Audit

## Quantifier checks

- Both collision vectors use the same row, primitive quotient root, and
  cofactor before the associate unit is introduced.
- The strict field floor `p>2^255` is used; replacing it by `p>=2^255` would
  not weaken the printed strict `D<6.845` conclusion.
- Equal-to-one coordinates may be assigned to the positive entropy side;
  all 63 possible nontrivial side sizes are checked.
- The entropy calculation is an upper bound for every positive vector, not a
  two-level ansatz. Jensen's inequalities prove that two-level vectors are
  the extremal reduction.
- The extension multiplicity from `Q(v)` to the 64 conjugate pairs is
  `64/d`; the squared-absolute logarithm contributes the separate factor two.
- Schinzel is applied to the totally real unit representative, not to a
  general complex unit.

## Independent arithmetic

`verify.py` imports only the hash-pinned directed-Decimal logarithm engine.
`verify_audit.py` reconstructs all logarithm bounds with exact rational
atanh series, dyadic range reduction, and explicit tail bounds. Both check
the deficit, all 63 entropy side sizes, and the golden-ratio separation.

## Scope ruling

Cofactor `2` remains live. A total maximum-profile cap of `367` therefore
reduces to a cap of `364` for that branch only after charging the possible
three high-cofactor orbits. Lower profiles still have to be paid in the exact
weighted sum.
