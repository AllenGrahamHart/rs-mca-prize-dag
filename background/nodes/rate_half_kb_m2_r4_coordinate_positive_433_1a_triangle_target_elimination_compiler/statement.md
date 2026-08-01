# KoalaBear m2 r4 positive 433-1a triangle target elimination compiler

- **status:** PROVED
- **scope:** the two oriented residual matching templates `(A)` and `(B)`
  below, with the missing mate carrying `ef`
- **dependency:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_quadratic_paired_product_resultant_interface`
- **consumer:** `rate_half_band_closure`

On a supported common survivor put

```text
F(W)=A_0(W)/A_2(W),
H(W)=W B_1(W)^2/A_2(W)^2,
x=F(xi)=ef.                                        (KBTEC-1)
```

All displayed target representatives are nonzero.  Orient three residual
source deck pairs as `{u,-u}`, `{v,-v}`, `{w,-w}`.

## Template A

Suppose their target products are

```text
(F(u),F(-u))=(de,-df),
(F(v),F(-v))=(-de,cf),
(F(w),F(-w))=(df,be).                              (KBTEC-2A)
```

Then every actual lift satisfies the target-free product chain

```text
F(v)=-F(u),
F(w)=-F(-u),
F(-v)F(-w)=bc F(xi),                               (KBTEC-3A)
```

and the single squared-sum row at `u` is exactly

```text
H(u) F(xi) F(-u)
 + F(u)(F(-u)-F(xi))^2 = 0.                        (KBTEC-4A)
```

Thus `(KBTEC-3A)--(KBTEC-4A)` eliminate `d,e,f` completely.

## Template B

Suppose instead

```text
(F(u),F(-u))=(de,cf),
(F(v),F(-v))=(-de,df),
(F(w),F(-w))=(-df,be).                             (KBTEC-2B)
```

Then every actual lift satisfies

```text
F(v)=-F(u),
F(w)=-F(-v),
F(-u)F(-w)=bc F(xi),                               (KBTEC-3B)
```

and the squared-sum row at `u` is exactly

```text
H(u)c^2 F(xi)^2 F(-u)^2
 -(F(u)F(-u)^2+c^2 F(xi)^2)^2 = 0.                (KBTEC-4B)
```

These identities are division-free after substituting the supported
quadratic forms and clearing their displayed denominators.  They retain
the three distinct outside deck pairs, common/source-label guards, and all
leading-support guards.

The theorem does not assert that templates A and B exhaust the 525-case
outside ledger over the deployed field.  It does not prove either template
empty, classify the other matching or missing-mate orbits, delete
`433-1a -> O0b`, close positive coordinate parity, K3, a Prize row, or
either Prize result.

## Falsifier

An actual supported lift of `(KBTEC-2A)` violating `(KBTEC-3A)` or
`(KBTEC-4A)`, or a lift of `(KBTEC-2B)` violating `(KBTEC-3B)` or
`(KBTEC-4B)`.
