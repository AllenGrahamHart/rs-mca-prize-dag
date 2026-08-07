# KoalaBear aligned-positive literal-cell crosswalk

- **status:** PROVED
- **scope:** the six canonical aligned-positive unramified systems compiled
  by the local `c2(1,1,2)` fixed/moving routers
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_literal_assignment_coverage`

Use the literal registry

```text
v0=2, v1=1/2, v2=b, v3=b^-1,
Eij=(T-vi)(T-vj).
```

The local fixed-moving reconstruction uses `{E01,E02}`, hence is `F00`.
The local moving-moving reconstruction uses `{E02,E03}`, hence is `M00`.
If `q(T)=T^2+tT+p=(T-c)(T-d)`, the three local residual allocations are

```text
same = R20,       swap = R02,       mixed = R11.   (KBCW-1)
```

Thus the six local systems are exactly

```text
F00-R20, F00-R02, F00-R11,
M00-R20, M00-R02, M00-R11.                         (KBCW-2)
```

This is a semantic crosswalk, not a transport theorem. In particular, the
matching centralizer's transitivity on combinatorial edge assignments does
not make the full q-slice systems covariant. A generic endpoint
normalization commuting with `T -> 1/T` changes the reciprocal target roots
unless the quotient coordinate `W` is moved as well; moving `W` changes the
observed source divisor. Therefore `(KBCW-2)` cannot close the other literal
`Fxx` or `Mxx` cells without a separately proved symmetry or cell-specific
classification.

## Falsifier

A mismatch between the local source-edge formulas and `F00/M00`; a root of
the local same/swap/mixed proportionality equations not having the
`R20/R02/R11` target respectively; or a generic matching-centralizer action
that preserves both the target in `W` and the observed source divisor.
