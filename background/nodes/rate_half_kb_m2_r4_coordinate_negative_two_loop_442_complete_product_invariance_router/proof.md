# Proof

Before choosing representatives, the three singleton edge signs give

```text
{u cD,v cE,w DE,DF,-DF,EF,-EF},
u,v,w in {+1,-1}.                                 (1)
```

Replace `D` by `uD` and `E` by `vE`.  Both doubled signed pairs are unchanged
as multisets, the two colored signs become positive, and the third sign is
`sigma=wuv`.  This proves `(KB44R-1)` and leaves exactly two sign orbits.

The skeleton has a residual exchange `D <-> E`, which swaps `cD,cE` and
swaps the two doubled pair types.  Replacing `F` by `-F` swaps the signs in
both doubled types.  Hence the seven occurrences have exactly the three
orbits represented in `(KB44R-2)`.  No other edge product occurs by the
complete-edge skeleton theorem.

The outside-product compiler forces `p_xi=N_r/H_r`; its protected
denominator allows the division-free equation `(KB44R-3)`.  Therefore every
complete packet enters one of the 36 indexed cells.

For each row, the product involution has homogeneous matrix

```text
J_r=[ Alpha_r  Beta_r ]
    [ Gamma_r -Alpha_r],

J_r^2=(Alpha_r^2+Gamma_r Beta_r) I.               (2)
```

The parent compiler proves the scalar in `(2)` nonzero.  If the six
residual values are three involution orbits, their root divisor is invariant
under `J_r`.  Pulling back its binary equation gives `(KB44R-5)`, so it is
projectively proportional to `R`.  This proves necessity.

Conversely, proportional binary forms have the same root multiset, so
`J_r` permutes the six roots.  Squarefreeness is product distinctness, and
coprimality with `(KB44R-7)` excludes fixed roots.  An involution without
fixed roots on a six-element set has exactly three two-cycles, which are
the remaining rows of the paired-product gate.

A binary sextic has seven coefficients, so projective proportionality is
equivalent to its 21 pairwise coefficient minors.  The independent choices
are six common rows, two signs, and three forced-location orbits, proving
`(KB44R-8)`.  The common q-orientation choice affects edge sums but not the
seven product values, so it is not an additional product cell.

Finally, `l` is a source/quotient `W` coordinate, while `D,E,F` are
endpoint-root coordinates in `T`.  The normal form identifies combinatorial
label positions across the construction, not affine values in independently
normalized projective charts. QED.
