# Audit

1. The primary computation is over `F_2130706433(t)`, not a sampled field or
   sampled `t` value.
2. All five proved primitive factors are covered independently.
3. The returned gcds are backed by explicit Bezout multipliers; four are
   exactly `e^2-1` and the octic is exactly `1`.
4. A second exact program reparses and verifies every generic identity
   without rerunning the gcd algorithm.
5. The regular `t=2` replay is an additional finite-subfactor audit, not the
   basis for the generic theorem.
6. The target-collision guard is explicit in the full outside target support:
   all squares of `1,b,c,d,e,f` are pairwise distinct.
7. The theorem uses only necessary consequences of the signed pair and
   colored edge, so dropping the other outside records cannot create a false
   exclusion.
8. Charts 3--5, exceptional fibers, and the second signed family remain
   printed nonclaims.
