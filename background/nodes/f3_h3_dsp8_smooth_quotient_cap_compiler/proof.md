# Proof

Fix one base tuple counted by `U_sm^c`. The unit-product normal form fixes its
target `t` and leaves only the quotient variables, with

```text
z in H,       w=tz+(1-t) in H,       z,w!=1.        (1)
```

The number of admissible ordered pairs in `(1)` is exactly `R(t)`. Since
`t` is retained, `t` and `1-t` are nonzero. Thus the affine forms

```text
L_1(Z)=Z,       L_2(Z)=tZ+(1-t)                     (2)
```

are nonconstant and nonproportional. Mattarei's theorem bounds the full
simultaneous `H`-membership count for `(2)` by `C_M n^(2/3)`; deleting the
identity endpoint only decreases it. Summing over the base tuples proves
`(SQC3)` with no multiplicity loss.

Put

```text
U_w=10U_sm^0+17U_sm^A,
W_sm=10G_sm^0+17G_sm^A.
```

The proved rational estimate `C_M<189/100` and `(SQC3)` give

```text
W_sm<(189/100)n^(2/3)U_w.                           (3)
```

Under `(SQC4)`, the right side of `(3)` is at most

```text
(144344/100)n^2=(36086/25)n^2,                     (4)
```

which is exactly the uniform target from the smooth residual router. This
proves `(SQC4)`.

Finally, nonnegativity gives

```text
U_w<=17(U_sm^0+U_sm^A),       189*17=3213.          (5)
```

Hence `(SQC5)` implies `(SQC4)`, and division by `3213` gives `(SQC6)`.
No estimate for either unweighted count has been used. QED.
