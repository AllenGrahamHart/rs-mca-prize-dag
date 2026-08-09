# Proof

The exact pivot scout enumerates four sign rows and six cofactor charts. All
24 guarded ideals have dimension one, basis size `17`, lex size `8`, empty
pivot boundary, and exact compact quotient; each sign has one chart-independent
lex signature.

The tower replay reduces all eight lex generators to zero in both candidate
recoveries. Recovery row `6` has a palindromic quadratic relation for `b`, a
linear relation for `c`, and unit `b`- and `c`-leading boundaries. Its base
discriminant factors as `(r-1)(r+1)` times a square-free quartic, so no
unrecorded leading fiber remains on the guarded route.

The kernel compiler removes the exact polynomial gcd and normalizes the first
nonzero coordinate. The resulting eight-coordinate vector is identical in all
four sign rows. Seven row identities vanish formally; Singular reduction by
each exact common ideal sends the remaining three to zero. `verify.py` checks
the complete ledgers and custody hashes, while `verify_audit.py` reconstructs
the discriminant and the seven formal identities from the source compiler.
