# Audit

1. The exact function-field basis packet certifies `gcd(P,L_2)=1`; this makes
   chart 2 global over `F_2130706433(t)`, but says nothing by itself about
   every specialization of `t`.
2. The primary colored computation is over `F_2130706433(t)`, not a sampled
   field or sampled `t` value.
3. All five proved primitive factors are covered independently.
4. The returned gcds are backed by explicit Bezout multipliers; four are
   exactly `e^2-1` and the octic is exactly `1`.
5. A second exact program reparses and verifies every generic identity
   without rerunning the gcd algorithm.
6. The regular `t=2` replay is an additional finite-subfactor audit, not the
   basis for the generic theorem.
7. The target-collision guard is explicit in the full outside target support:
   all squares of `1,b,c,d,e,f` are pairwise distinct.
8. The theorem uses only necessary consequences of the signed pair and
   colored edge, so dropping the other outside records cannot create a false
   exclusion.
9. Finite exceptional fibers, other sign rows, and other matching cells
   remain printed nonclaims.
