# KoalaBear m2 r4 diagonal c2 (1,1,2) negative reconstruction factor gate

- **status:** PROVED
- **scope:** the negative-sign candidates of every saturated source-line
  `(1,1,2)` packet
- **dependency:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
- **consumer:** `rate_half_band_closure`

Use an endpoint coordinate commuting with `tau(T)=1/T` to orient the common
internal endpoint as `2`. Then

```text
J_0={2,1/2,b,1/b},       q(T)=(T-c)(T-d),
```

and let `w` be the forced-square quotient label. The twelve compatible
internal edge assignments have exactly two matching-preserving templates:

```text
F: {2,1/2} and {2,b},       8 assignments,
M: {2,b}   and {2,1/b},     4 assignments.          (KBNF-1)
```

Put

```text
E=cdw+4cd-2cw-2c-2dw-2d+4w+1,
A=5cd-4c-4d+5,
B=bcd-2bc-2bd+b+2cd-c-d+2,
C=2bcd-bc-bd+2b+cd-2c-2d+1,
Pi=(c-2)(2c-1)(d-2)(2d-1)
   *(w-1)^5(w+1)^5(cd-1)^2.                       (KBNF-2)
```

The incidence denominator gives `E!=0`. Label distinctness, absence of
`tau`-fixed labels, and `tau(J_1) subset I` give `Pi!=0`, as well as
`2b-1!=0` in template `F` and `(b-1)(b+1)!=0` in template `M`.

For the negative reciprocal source space, append the target value
`U(T,z)` from the two internal stars to the two forced-line equations. The
resulting `5 x 5` augmented reconstruction determinant is exactly

```text
Delta_F=-6 Pi A^2 B / ((2b-1)E^5),
Delta_M= 6 Pi A B C / (((b-1)(b+1))E^5).          (KBNF-3)
```

The coefficient matrix has rank four by internal-evaluation injectivity.
Consequently a negative candidate exists exactly on

```text
F: A B=0,
M: A B C=0.                                       (KBNF-4)
```

Off these printed hypersurfaces the negative sign is deleted before the
`q`-slice or full quotient resultants. On them the unique reconstructed
candidate must still pass those gates.

This theorem does not assert that `A`, `B`, or `C` is always nonzero, or
that a candidate on their union is realizable. It deletes no positive
candidate, full packet, branch, `(1,1,2)` row, owner, payment, row, or Prize
result.

## Falsifier

A compatible negative assignment outside the two templates, failure of the
determinant identities `(KBNF-3)`, or a negative reconstruction off the
factor loci `(KBNF-4)`.
