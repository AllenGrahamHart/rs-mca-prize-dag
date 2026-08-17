## MCA O0b `FFF` `q7` multiplication-algebra pivot (2026-08-17)

### Retired extension

The exact 24-term `q7` input was constructed over the dimension-16 `q5`
quotient, but its Groebner extension exceeded 600 seconds. Modal app
`ap-cPK9VPOH7bzcXjc8ME08LD`; result SHA-256
`a3d3dd55da213b58af78e415df88c1004348b838e7430c8150234bdb732e0b22`.
No basis or status was produced.

### Selected finite-algebra route

Let `A` be the certified 16-dimensional `q5` quotient. Extract the regular
multiplication matrices of `s,x,r,c,b`. The retained `q7` coefficients give

```text
D2*E^2 + D1*E + D0 = 0.
```

The route guard `a2m != 0` makes `D2=-a2m^2` a unit on the admissible
zero-dimensional algebra; certify this by its multiplication determinant.
Then the `q7` extension is represented explicitly on `A + A*E` by the block
matrix

```text
M_E = [[0, -D2^{-1}D0],
       [I, -D2^{-1}D1]].
```

Evaluate `q6` in these commuting 32-by-32 matrices. Its multiplication
determinant is nonzero exactly when `q6` is a unit, which proves generic
emptiness of the necessary subsystem.

### Next decision gate

First bank the 16-dimensional quotient basis, five variable multiplication
matrices, and the normal representatives of `k0..k5`. Then run the block
extension and determinant as a separate certificate. Retain numerator roots
and every denominator as exceptional fibers.
