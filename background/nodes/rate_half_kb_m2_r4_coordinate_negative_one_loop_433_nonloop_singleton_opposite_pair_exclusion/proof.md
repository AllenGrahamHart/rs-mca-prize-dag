# Proof

Write the moving product row as `A_xx+B_x`, the static product row as `P_0`,
the moving q row as `Q_2t^2+Q_1t+Q_0`, and the static q row as `H`.  The
static q row is linear in `c`; its coefficient and constant cannot vanish
together away from guards.  Similarly, `A_x=B_x=0` eliminates only to
source/target guards.  Thus an actual packet uniquely reconstructs `c` and
has `A_x!=0`.

Eliminate `c` between `P_0` and `H`, substitute `x=-B_x/A_x` in the moving
q row, and protect the resulting linear equation

```text
(Q_1A_x)t+(Q_0A_x-Q_2B_x)=0.                     (KB433OP-2)
```

The common projection of the two coefficients of `(KB433OP-2)` has four
linear factors per sign row.  At each root, the gcd in `b` of the static
compatibility and both coefficients reduces to `b` or `b+1`.

On the ordinary branch, square `(KB433OP-2)`, impose `t^2=-B_x/A_x`, and
eliminate `b`.  Exact factorization gives `(KB433OP-1)`.  At each of its
four linear roots, the gcd of the static and square equations again strips
completely by `b(b+1)`.  All linear projections therefore violate product
nonzero or target signed-pair distinctness.

The remaining factors are one irreducible quadratic and one irreducible
quartic per sign row, each squared.  An independent Rabin audit checks both
the linear and possible quadratic divisor tests, so in particular no
quartic hides a quadratic splitting.  Cell `11` is empty, and target sign
change gives cell `14`. QED.
