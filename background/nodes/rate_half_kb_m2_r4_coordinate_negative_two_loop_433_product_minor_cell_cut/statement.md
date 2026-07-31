# KoalaBear m2 r4 coordinate negative two-loop 433 product-minor cell cut

- **status:** PROVED
- **scope:** every negative-parity coordinate packet in one of the nine
  antipodal cells `(KB43-3)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler` and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_antipodal_label_atlas`
- **consumer:** `rate_half_band_closure`

Normalize the signed `J` pairs by `A=1`, `B=b`, `C=c`.  On the ordered edge
types `(A,C,AB+,AB-,BC)`, the five products are

```text
(-1,-c^2,b,-b,bc).                                (KB43P-1)
```

The first maximal-minor pass has the following exact consequences:

```text
X1:  deleted,
N2:  deleted,
Z1:  deleted;                                     (KB43P-2)

X2:  b=-c^3,
N1:  b=-c^3,
L1:  b=-c^3.                                      (KB43P-3)
```

Indeed, after the cell substitutions, one `4 x 4` product minor is

```text
X1,N2: -2 M(b-c)(b+c)(M-1)(M+1),
Z1:     4 M(b-c)(b+c),                            (KB43P-4)
```

and every factor is nonzero by odd characteristic, label distinctness, and
distinct signed `J` pairs.  A second minor is

```text
X2,N1:  2bM(b+c^3)(M-1)(M+1),
L1:    -4bM(b+c^3),                               (KB43P-5)
```

so the same guards force `(KB43P-3)`.

The exact common-`K` product frontier is therefore six cells:

```text
X2,N1,L1 with b=-c^3;       M1,M2,M3 unrestricted by this cut. (KB43P-6)
```

This theorem does not classify the remaining product minors, impose the
second q weld, use the other seven fibers, delete the `(4,3,3)` skeleton or
coordinate orientation, move an owner/payment, close a row, or prove either
Prize result.

## Falsifier

An actual packet in `X1,N2,Z1`, an actual packet in `X2,N1,L1` with
`b!=-c^3`, or failure of any determinant formula `(KB43P-4)--(KB43P-5)`.
