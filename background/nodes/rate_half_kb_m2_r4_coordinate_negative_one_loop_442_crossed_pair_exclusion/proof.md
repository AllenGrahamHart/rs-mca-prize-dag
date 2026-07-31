# Proof

For `(KB41X-1)`, write the two independent product minors and the two
denominator-cleared q welds.  Remove only their explicit nonzero guard
factors.  Exact deployed-field Gröbner reduction places both polynomials
`P,Q` in their ideal.

Since `b,c` are nonzero, divide by those factors.  Both residual equations
are linear in `r`, and direct elimination gives `(KB41X-3)`.  The field is
odd and the six target labels include `+/-1,+/-b,+/-c`, so `b^2=1` is a
forbidden collision.  No representative solution exists.

Changing the sign of `C` swaps the two crossed matchings.  Changes of the
`B` and `C` representatives, followed by renormalizing the first source
root, independently toggle the two relative square-root signs.  Thus the
representative deletion covers the whole orbit. QED.
