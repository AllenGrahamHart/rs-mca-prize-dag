# KoalaBear near-positive projective-boundary literal coverage

- **status:** PROVED
- **scope:** every literal positive near-aligned homogeneous endpoint-boundary
  q-slice cell over characteristic `p=2130706433`
- **dependencies:** ramified complete-source repair, internal-star
  reconstruction, and the q-slice resultant gate
- **consumer:** source-line literal-assignment coverage

Keep the literal coordinate frame

```text
J_0={2,1/2,b,1/b},       q_hom=Y(T-dY),       w=0. (KBLB-1)
```

There are twelve compatible internal edge assignments

```text
F00 F01 F02 F03 F04 F05 F06 F07 M00 M01 M02 M03,
```

and four literal near-target roots

```text
A=1/2,       TA=2,       OB=1/b,       OI=b.      (KBLB-2)
```

Thus the literal boundary census has `12*4=48` cells. For every cell,
reconstruct the repaired positive source form directly from the two
homogeneous membership equations and the three internal-star equations. No
endpoint Möbius covariance or normalized-template transport is used.

Put `G=U^2-WV^2`. The projective q-slice is

```text
G(d,W) * coeff_(T^4) G(T,W),                     (KBLB-3)
```

after dividing the forced `W^2` from each factor. If the target root in
`(KBLB-2)` is `r`, the necessary q-slice gate requires `(KBLB-3)` to be
projectively equal to

```text
((W-r^-1)(W-d^-1))^2.                            (KBLB-4)
```

For each of the 48 cells, the four cross-multiplied nonleading coefficient
equations generate the unit ideal on the complete named open. The named open
contains the `J_0` and boundary-label collision factors, the internal-label
and reconstruction determinants, projective degree, and every rational
denominator. One-step Rabinowitsch localization and sequential saturation by
the same irreducible factors agree on all 48 unit classifications.

Hence no literal positive near-aligned projective-boundary cell passes the
necessary q-slice gate.

This theorem does not classify aligned-negative or near-negative literal
assignments.

## Falsifier

A compatible boundary assignment or target root absent from the 48-cell
census, a denominator or degree-drop component outside the named open, or a
nonunit complete-chart ideal.
