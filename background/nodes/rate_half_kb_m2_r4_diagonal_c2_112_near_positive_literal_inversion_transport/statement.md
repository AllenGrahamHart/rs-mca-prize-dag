# KoalaBear near-positive literal inversion transport

- **status:** PROVED
- **scope:** affine positive near-aligned `c2(1,1,2)` q-slice systems
- **dependencies:** source-line internal-star reconstruction and the q-slice
  resultant gate
- **consumer:** source-line literal-assignment coverage

Write the twelve literal source-star assignments as

```text
F00 F01 F02 F03 F04 F05 F06 F07 M00 M01 M02 M03.
```

In the affine positive near-aligned chart put `w=1/c`. For each assignment,
each root label

```text
A=1/2, TA=2, OB=1/b, OI=b,
```

and each allocation `RX,RL,RM`, reconstruct the positive source form and its
two residual quadratics. The two restricted substitutions

```text
B:  b -> 1/b,
TW: (b,c,d,W) -> (1/b,1/c,1/d,1/W)                (KBNI-1)
```

carry both residuals projectively, both target quadratics, and the complete
radical factor set of the reconstruction and q-slice named open to the
following companion assignment:

```text
F00<->F01   F02<->F03   F04<->F05   F06<->F07
M00->M00    M01<->M02   M03->M03.                 (KBNI-2)
```

`B` fixes `A,TA`, exchanges `OB,OI`, and preserves the allocation. `TW`
exchanges `A,TA`, fixes `OB,OI`, and preserves the allocation. These are
identities over `QQ(b,c,d)`, hence remain valid on every field chart where
the named open is nonzero.

After the existing semantic identification of the two orientations `OB/OI`,
the `12*3*3=108` affine cells form exactly

```text
7 assignment orbits * 2 xi orbits * 3 allocations = 42 orbits. (KBNI-3)
```

The canonical `F00` and `M00` systems represent twelve of these orbits. The
unrepresented literal frontier is therefore exactly

```text
{F02/F03,F04/F05,F06/F07,M01/M02,M03}
    x {{A,TA},other} x {RX,RL,RM},
```

or `5*2*3=30` orbit representatives.

This theorem does not transport either full colored quotient identity. It
does not cover `w=0`, any projective boundary, the near-negative sign, or
prove any of the 30 residual representatives empty.

## Falsifier

One assignment/target for which a transformed residual or target is not
projectively equal to its destination, one radical localizer factor gained
or lost under either map, a different semantic orbit count, or a claimed
transport across one of the explicit scope fences.
