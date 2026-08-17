# Proof

For `xi=2,pairing=0`, the three record pairs are `(0,1)`, `(3,4)`, and
`(5,6)`. Their S0 records are

```text
be, cf, -de, df, -df, -ef.
```

In `FFI`, the third pair is at infinity. Its two leading-coefficient
equations are

```text
z5 + d*f*z2 = 0,
z5 + e*f*z2 = 0.
```

Subtracting gives `f(d-e)z2=0`. Admissibility includes `f != 0` and
`d^2-e^2 != 0`; the latter implies `d-e != 0`. Hence `z2=0`, and either
equation gives `z5=0`.

In `FIF`, the second pair is at infinity. The equations are

```text
z5 + d*e*z2 = 0,
z5 - d*f*z2 = 0.
```

Their difference is `d(e+f)z2=0`. Admissibility gives `d != 0` and
`e^2-f^2 != 0`, hence `e+f != 0`. Again `z2=z5=0`. QED.
