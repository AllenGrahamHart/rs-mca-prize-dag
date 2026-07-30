# KoalaBear m2 r2 residual one-parameter quartic normal form

- **status:** PROVED
- **scope:** the surviving `n=3,6` full-V4 dihedral profiles
- **dependency:**
  `rate_half_kb_m2_r2_dihedral_residual_coefficient_quartic_pin`
- **consumer:** `rate_half_band_closure`

Every actual residual coefficient quartic is geometrically equivalent to
the canonical pullback from the symmetric sibling conic

```text
x^2+y^2-a*x*y+(a^2-4)=0,
```

where

```text
a=-1 for n=3,       a=1 for n=6.                  (KBMN-1)
```

The source V4 branch passport forces exactly one branch value of the
endpoint quadratic `h` to be a branch value of the degree-two projection
`Y`. Normalize that value to `2`, write the other as `b`, and note
`b notin {2,-2}`. After the target change

```text
m(x)=(x-2)/(x-b)
```

and a source change making `m composed h(t)=t^2`, the sibling coefficients
in the notation of the canonical quartic pin are

```text
A=(a-2)(a-b^2+2),
B=-(a-2)(2a-b^2-2b+4),
C=(a-b)^2,
D=4a^2-a*b^2-4a*b-4a+16b-16,
E=-2(a-2)(a-b),
F=(a-2)^2.                                         (KBMN-2)
```

Substitution of `(KBMN-2)` into

```text
Q=A P^4+B S^2P^2-2B P^3+C S^4-4C S^2P
  +(2C+D)P^2+E S^2-2E P+F                         (KBMN-3)
```

gives every actual residual coefficient image. Thus each of `n=3,6` has
one geometric parameter `b`, rather than six independent sibling
coefficients or an arbitrary plane quartic.

Actual existence still requires `(KBMN-3)` to be irreducible and to realize
the complete pole/source equations. Neither profile is deleted here, and
no owner, payment, row, or Prize problem is closed.

## Falsifier

A residual with `a` outside `(KBMN-1)`, zero or two endpoint branch values
in the branch set of `Y`, or transformed sibling coefficients outside
`(KBMN-2)`.
