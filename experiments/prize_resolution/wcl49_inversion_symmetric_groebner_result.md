# WCL (4,9) inversion-symmetric Groebner result

Status: `COMPLETE`, route-selected; no WCL status change.

Modal app `ap-uGwcJZUDyu3EvGCS3q7hKx` computed the exact rational
lexicographic Groebner basis for the four anti-reciprocity equations in
`0.151924` seconds with `86 MB` peak RSS. The basis is zero-dimensional. Its
univariate eliminant factors as

```text
c0(c0-2)(c0^3-12c0-8)(c0^3-12c0+8)
  (c0^3-6c0^2+8)(c0^3-6c0^2+24).
```

Thus inversion-invariant Pell candidates lie over 14 possible algebraic
values of the quartic constant coefficient. This does not yet impose
`P | Y^1024-1`. The next exact step is branchwise modular powering followed
by integer Bezout certificates for the six eliminant factors. No support
census or retry was launched.
