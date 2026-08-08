# Proof

Fix a source-sign pair and target lane. Work on the proved cell-4 tower over
`F_p(r)` with basis `1,t,b,bt`, quadratic relations for `t` and `b`, and
linear recovery of `c`. Reduced FLINT fractions retain every numerator and
denominator introduced by inversion.

For `xi=0` and `xi=2`, respectively, the residual product lists are

```text
de, -de, df, sigma_o ef, bf, sigma_c cf,
de,  de, df, sigma_o ef, bf, sigma_c cf.
```

At matching 5, put `u=df`. The first two paired cuts are the quadratics

```text
P_u(u) = Pair(de,u),       P_f(f) = Pair(second_de,sigma_c*cf),
```

where `second_de=-de` for `xi=0` and `second_de=de` for `xi=2`. If `m,s`
are the omitted product and squared sum, take `de=m, eta=1` for `xi=0` and
`de=-m, eta=-1` for `xi=2`. Since `d=u/f` and `e=de*f/u`, every target
satisfies

```text
J(u,f) = (u^2 + eta*de*f^2)^2 - s*f^2*u^2 = 0.       (1)
```

Write `P_u=A*u^2+B*u+C`. After clearing the already-guarded missing-record
denominator, write (1) as

```text
a^2*u^4 + M*f^2*u^2 + de^2*a^2*f^4 = 0,
M = 2*eta*de*a^2 - S,
```

where `a` is the missing-record denominator and `S` is the squared-sum
numerator. Define

```text
L = a^2*(-B^3+2*A*B*C) - M*B*A^2*f^2,
N = a^2*(-B^2*C+A*C^2) - M*C*A^2*f^2
    + de^2*a^2*A^3*f^4.
```

For `A != 0`, the remainder of (1) modulo `P_u` is `(L*u+N)/A^3`, so a
common root forces

```text
E(f) = A*N^2 - B*L*N + C*L^2 = 0.                   (2)
```

This is degree eight in `f`. The displayed cleared expression also vanishes
identically when `A=0`, so leading-degree drops are included rather than
divided away. A division-free pseudo-remainder of (2) modulo `P_f` leaves
`R_1*f+R_0`. The quadratic resultant

```text
A_f*(R_1^2*C_f - R_1*R_0*B_f + A_f*R_0^2)
```

again includes `A_f=0`. Its four-dimensional tower norm is therefore a
necessary target-free cut with all degree-drop specializations retained.

For every one of the 32 computed rows, the compiler unions all field roots
of the norm numerator, norm denominator, and every inversion-guard numerator
or denominator. It lifts them through the original `t`, `b`, `c`, and compact-
kernel equations. At each guarded source point it solves `P_u=P_f=0`, tests
(1), reconstructs `d=u/f`, `e=de/d`, and evaluates the third colored pair
`Pair(sigma_o*ef,bf)` and all target guards.

The exact ledger has 320 candidate `r` values and 288 guarded source points.
Of 1,040 `(u,f)` rows, 960 fail (1). The remaining 80 consist of 16
`f=0` target boundaries and 64 rows with a nonzero third-pair cut. There is
no colored solution, witness, or unresolved branch, so `xi=0,2` are empty.

Deleting the other positive `DE` copy preserves the residual products,
missing squared sum, matching, and guards value-for-value. Thus the 16
`xi=1` cases transport from `xi=0`, proving all 48 cases. QED.
