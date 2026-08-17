## MCA O0b `FFF` generic `q7` coefficient bank (2026-08-17)

### Exact result

The staged base-algebra calculation retains `a2m`, `bm`, both squares, and
all three coefficients of

```text
q7 = D0 + D1*E + D2*E^2.
```

Every one of the seven representatives has fiber degree two and exactly
eight terms. The coefficient hashes are

```text
D0 175919493e8500089bd1d528d2d768b83f9e47df021048ceea6ea637bf9a5b34
D1 1d7f55723f5a0cee8ebe409c879a480637a0b0bd6fa5fb9d2b4a95f25cb7f8dd
D2 d52a21d795e753e4aa04582fa3d67f65003a48b3406383db4a84730b528e961d
```

Modal app `ap-34Gk6WjaK7Ptlv0Jy93XKc`; result SHA-256
`37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d`.

### Next decision gate

Embed the three coefficient representatives into
`GF(p)(t)[E,s,x,r,c,b]`, adjoin their 24-term quadratic to the certified
16-element `q5` basis, and retain the resulting finite quotient. If the
extension survives, reduce and impose `q6` there.

### Proof boundary

This closes coefficient construction only. It does not assert that the
`q5,q7` extension is empty and does not discharge denominator fibers.
