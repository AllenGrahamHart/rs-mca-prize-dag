# Proof

Over `K=F_p(t)`, the proved primitive-coordinate packet gives
`u=p_u(L)` for `u in {x1,x0,b}`.  The primary Nemo calculation forms every
entry of the full matrices `p_u(L)` in reduced rational-function form.  Their
maximum numerator/denominator degree is 126, and none of their 1,728
denominators vanishes at any of the 38 map-only fibers.  Hence the apparent
map poles are removable at the multiplication-operator level.

The independent checker verifies the exact rational matrix identity

```text
M_x1+2*M_x0+3*M_b=L,
```

and at the regular fiber `t=2` independently reconstructs each `p_u(L)` from
the old coordinate maps.  At every routed fiber it evaluates all three
matrices, checks pairwise commutation, and replays the dynamic Krylov solve.

For 33 fibers `ell'=x1+2*x0+b` is cyclic; for the other five
`ell'=x1+3*x0+b` is cyclic.  In each case the checker verifies the invertible
24-column Krylov matrix, solves for all three coordinates and the monic
degree-24 minimal polynomial, and reconstructs each full coordinate matrix
from the solved polynomial.  Independent factorization proves the minimal
polynomial squarefree and accounts for total degree 24.

On every irreducible factor, the checker reduces the solved coordinates,
verifies the defining equation for `ell'`, and reconstructs the chart-2
values of `r,c`.  The fresh finite replay then rebuilds the necessary pair
polynomial and colored outside-edge polynomial.  Across all 804 factors the
monic gcd is `1` in 220 cases and `e^2-1` in 584 cases.  The former have no
common target root; every root in the latter violates the retained target
square-distinctness guard.  Therefore every routed component, and hence all
38 fibers, is empty. QED.
