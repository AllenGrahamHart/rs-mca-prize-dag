# Proof

Compile cell `4` from products `(-1,b,c,bc,-bc)` and roots `(KB433MX-1)`.
After exact guard division, each q row is linear in `t`.  The first row's
coefficient and constant have target-variable resultants, up to nonzero
scalars,

```text
(c^2-1)(r^2+1),       (b^2-1)(r^2+1),             (KB433MX-3)
```

so the row determines `t` on the guarded locus.

Both product minors are linear in `x=t^2`.  Their first row cannot lose
degree: eliminating either target variable from its coefficient and
constant leaves only

```text
target^2(target^2-1)^2(r^2-1)^2(r^2+1)^2.
```

For the `(+,+)` row, the stripped product and square compatibilities are

```text
G=c[b^2(r^2-1)^2+b(r^4+6r^2+1)]
    +b(r^4+6r^2+1)+(r^2-1)^2,
K=(b^2+1)(r^2-1)-4ibr.                            (KB433MX-4)
```

The resultant of the coefficient and constant of `G` is
`-16r^2(r^2-1)^2(r^2+1)^2`; hence `G` uniquely reconstructs `c` away from
guards.  Substitute this value in q compatibility and eliminate `b` with
`K`.  Exact factorization gives only guards times the square of the first
cubic in `(KB433MX-2)`.  The same division-free route gives the other three
cubics for the other sign rows.

The finite-field factorization has one degree-three factor of multiplicity
two in every row.  An independent Frobenius/gcd audit computes
`gcd(f,r^p-r)=1` for each cubic, proving that none has a base-field root.
Cell `4` is therefore empty.  The displayed target sign/exchange operations
map its matching successively to cells `5,7,8` while preserving the complete
product and q equations. QED.
