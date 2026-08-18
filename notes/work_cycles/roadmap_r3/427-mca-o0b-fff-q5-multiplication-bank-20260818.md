## MCA O0b `FFF` `q5` multiplication bank (2026-08-18)

### Exact result

The certified dimension-16 `q5` quotient now has a complete regular
representation:

```text
quotient basis size:       16
variable matrices:         s,x,r,c,b
nonzero matrix entries:    736
kernel normals:            k0..k5
terms per kernel normal:   8
fiber degree per normal:   2
```

All five matrices commute exactly. Quotient-basis SHA-256:
`aa3090c6c61b29e8a19f456d5a04b826423d9b08eb625d78c62b725ee00b5c8b`;
matrix-ledger SHA-256:
`29300862188e3e23b2b4a855c38ca82c0cc93c082932d6bff0fb517f7b71942e`.
The completed rerun is Modal app `ap-an7VJ4q5e54gxEGpu8967G`; result SHA-256
`3d216da7d91c82a1360f932673ce3529278c90f81e6a8a6767f14a34ad73a45e`.

### Next decision gate

1. Evaluate `D0,D1,D2` and `k0..k5` in the 16-dimensional regular
   representation.
2. Certify `det(M_D2) != 0`, invert it, and construct the 32-dimensional
   block matrix for multiplication by `E`.
3. Verify the `q7` matrix identity exactly.
4. Evaluate `q6` and retain the numerator and denominator of its 32-by-32
   multiplication determinant.
5. A nonzero numerator proves generic emptiness; all numerator and
   denominator roots become explicit exceptional fibers.

### Proof boundary

The bank itself imposes neither `q7` nor `q6`. It is an exact reusable
algebra representation, with every rational entry retained.
