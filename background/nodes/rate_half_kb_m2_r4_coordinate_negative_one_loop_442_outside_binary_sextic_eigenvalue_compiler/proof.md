# Proof

The trace-zero matrix satisfies `M^2=Delta I`.  If binary-sextic invariance
holds with scalar `lambda`, applying it twice gives

```text
lambda^2 H(X,Z)=H(M^2(X,Z))=H(Delta X,Delta Z)=Delta^6 H(X,Z).
```

Odd characteristic and `Delta!=0` therefore give
`lambda=+/-Delta^3`.

Work over an algebraic closure and diagonalize `M`.  Its two projective fixed
points have eigenvalues `s` and `-s`, where `s^2=Delta`.  A degree-six form
with eigenvalue `-Delta^3` vanishes at both fixed points: evaluating at
either eigenvector makes the left side `Delta^3 H` and the right side
`-Delta^3 H`.  The residual roots are concrete packet products, and the
involution compiler plus product injectivity rules out a fixed residual
root.  Hence the negative branch is impossible and `(KB41EV-1)` follows.
The converse is immediate, and the preceding invariance compiler identifies
invariance with the residual paired-product gate.

Expanding

```text
sum_j h_j(Alpha X+Beta Z)^(6-j)(Gamma X-Alpha Z)^j
```

and choosing `p` copies of `Beta Z` in the first factor and `ell-p` copies
of `-Alpha Z` in the second gives `(KB41EV-2)`.  Coefficient comparison gives
`(KB41EV-3)` without division.

Finally, in an eigenbasis of `M`, the degree-six monomial
`X^(6-j)Z^j` has eigenvalue `(-1)^j Delta^3`.  There are four even values of
`j` and three odd values.  Since `2Delta^3` is nonzero, the operator
`H |--> H(M)-Delta^3 H` has a four-dimensional kernel and rank three.  Rank
is unchanged by scalar extension or change of basis. QED.
