# Proof

Fix `(epsilon_1,epsilon_2)`.  The two common product determinants are
linear in `c`.  With

```text
U=r^2t^2-3r^2+3t^2-1,   V=(r^2-1)(t^2+1),
```

after a common nonzero determinant scaling, the coefficient and constant
term of the first determinant are
`b(bV-U)` and `-b^2(bU-V)`.  If `bV-U=0` and the determinant also
vanishes, then `bU-V=0`; adding these equations in the form

```text
b(bV-U)+(bU-V)=(b^2-1)V
```

forces `V=0`.  This contradicts `r^2!=1` and `t^2!=-1`.  Hence the
denominator is guarded and the first determinant gives `(KB41B-5)`.
The second determinant is then equivalent to one compatibility polynomial.

Substitute `c` into the q weld using the `AC+` row.  Its numerator,
after deleting only guarded factors, is

```text
H_e(r,t)=r^2t+e*i*r^2+2e*i*rt+2r+t+e*i.
```

Before deletion the factors are
`b(b-1)(b+1)(r-t)(r-e*i)(t^2+1)H_e`.  All preceding factors are label or
target guards.  Writing `H_e=A_e t+B_e`, where

```text
A_e=r^2+2e*i*r+1,       B_e=e*i*r^2+2r+e*i,
```

gives `gcd(A_e,B_e)=1` in the deployed field.  Therefore its
coefficient-zero branch is empty and `t=-B_e/A_e`, which is
`(KB41B-4)`.

Substitute this value into the product compatibility and the remaining q
weld.  Their numerator gcd is the guarded factor `b(r^4-1)`.  Divide it
from both and take their direct resultant in `b`; no leading coefficient
is inverted.  Put `t=N/A` and form the routed label guard

```text
L=r(r^4-1)N(N^2-A^2)(N^2+A^2)
  (N^2-r^2A^2)(N^2+r^2A^2).
```

Exact factor saturation gives, in every sign row,

```text
Res_b(product,q) / gcd-saturation-by-L
  = (r^2+epsilon_2*i)^2.                           (1)
```

Thus every guarded solution obeys the first equation in `(KB41B-3)).
At either of its two deployed roots, the gcd in `b` of the two routed
numerators is exactly the monic form of `2b^2+3b+2`.  This proves the
second equation.

The two quadratics in `r` and `b` split into two distinct deployed
roots.  Reconstructing `t,c` by `(KB41B-4)--(KB41B-5)` gives four
packets per sign row.  Direct substitution checks all four original
determinants, and their five source labels and five common products are
nonzero and pairwise distinct.  Hence all candidates are guarded
solutions, proving the converse and the exact count. QED.
