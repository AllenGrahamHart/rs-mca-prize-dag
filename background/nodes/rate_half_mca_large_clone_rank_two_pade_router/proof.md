# Proof

On a clone coordinate `x`, the Mobius theorem gives

```text
p_0(x)+gamma p_1(x)+gamma^2 p_2(x)
 =(q_0(x)+gamma q_1(x))(r_0(x)+gamma r_1(x)).          (1)
```

Comparing slope coefficients yields

```text
p_0=q_0r_0,
p_1=q_0r_1+q_1r_0,
p_2=q_1r_1                                                   (2)
```

at `x`. Substitution of (2) into `(RP1)` cancels every term, so every clone
coordinate is a root of `Omega`. The degree bound `(RP2)` follows from
`deg q_i<=d` and `deg p_i<=m`.

If `c>=m+2d+1`, root counting makes `Omega` the zero polynomial. Since
`q_0,q_1` are nonzero, their monic least common multiple `L` exists. Direct
multiplication gives

```text
(q_0+gamma q_1)(p_0L/q_0+gamma p_2L/q_1)
 =Lp_0
  +gamma L(q_1p_0/q_0+q_0p_2/q_1)
  +gamma^2Lp_2.
```

The middle coefficient equals `Lp_1` exactly when `Omega=0`; this proves
`(RP3)`. Consequently `Nhat/Qhat=(A_*+gamma B_*)/L` in `F(X)(gamma)`.
Cancelling the common gcd of `L,A_*,B_*` leaves denominator degree at most

```text
deg L<=deg q_0+deg q_1<=2d.
```

If two source parameter values have root-free denominators on `D`, their
fixed owner values are finite at every domain coordinate. Solving the two
affine owner values for the fixed coefficient functions shows that both are
finite there, so every apparent domain pole of the common representation is
removable. The reduced common denominator is therefore root-free on `D`.

If `c=m+2d`, a polynomial of degree at most `c` vanishing at all points of
`C` is either zero or a scalar multiple of the monic degree-`c` locator
`Lambda_C`. This proves `(RP4)`. For smaller `c`, `(RP2)` gives no forced
global identity, leaving exactly the displayed support band. QED.
