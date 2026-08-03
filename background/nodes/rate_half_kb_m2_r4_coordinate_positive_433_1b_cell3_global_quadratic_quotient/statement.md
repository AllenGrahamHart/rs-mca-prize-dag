# Statement

## Claim `(KBP1B3-QUOT-1)`

Work over `F_2130706433`, with `iota=16711679`.  On the guarded
product-rank-five branch of deployed positive `433-1b -> O0a` role cell `3`,
fix source signs `(epsilon_1,epsilon_2)` and write the compact common-curve
coordinates as `(t,r,c,b)`.  The saturated common ideal has the following
global three-relation presentation on every one of the six product-cofactor
charts:

```text
E_epsilon(t,r) = 0,
A_epsilon(t,r)(b^2+1) + B_epsilon(t,r)b = 0,
D_epsilon(t,r)c + C_epsilon(t,r,b) = 0,
```

where

```text
A_epsilon = r^2(t + epsilon_2 iota r),
D_epsilon = t - epsilon_1 epsilon_2 r^2.
```

More precisely:

1. `E_epsilon` has total degree `6` and `14` terms;
2. the palindromic `b` relation has total degree `7` and `16` terms;
3. the `c`-linear recovery relation has total degree `3` and `6` terms;
4. `A_epsilon` and `D_epsilon` are units on the guarded common curve;
5. after localization by the printed route guards, selected product cofactor,
   and the two displayed recovery coefficients, these three relations generate
   exactly the full ten-generator block-lex common ideal; and
6. the presentation is byte-identical across all six cofactor charts for each
   fixed source-sign pair.

Thus cell `3` is globally represented by a palindromic quadratic extension in
`b` over the irreducible `(t,r)` base curve, followed by linear recovery of
`c`.  The claim does not assert birationality, rationality, common-locus
emptiness, an outside signed-edge exclusion, complete cell-3 closure, K3,
LIST, MCA, or either Prize result.
