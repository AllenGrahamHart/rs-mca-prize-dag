# Audit

- `verify.py` uses Lucas/Hasse derivatives on every two- and four-element
  parity support in residues modulo `32`, then factors every local-reciprocity
  candidate by trial division.
- `verify_audit.py` instead expands each `(1+Y)^r` as a bit mask and reads its
  first nonzero coefficient. It independently scans and factors the cofactor
  candidates.
- The two implementations agree on the full multiplicity sets, subset-count
  ledger, cofactor ceiling, `6622` pre-sieve candidates, `1133` survivors,
  and the count at every valuation.
- Both verifiers are tiny local arithmetic: fewer than forty thousand
  four-subsets and fewer than seven thousand integer factorizations below
  `1.71e6`. No Modal or broad vector census is used.
- The proof does not infer actual collision existence from necessary local
  conditions. This distinction is load-bearing.
